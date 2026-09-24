#!/usr/bin/env python3
"""Finite construction checks for dedicated-factor and commuting-query bounds.

No optimizer; these diagnostics supplement the supplied symbolic proof.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import numpy as np

BASE = 'a383214b357ccbd83a62ae0c94660083cb8b090e'
SEED = 2026092408
TOL = 1e-9
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
R = math.sqrt(2)
DELTA = 2-R


def kron(items):
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


def query_refs(n):
    return [kron(p if j == i else I for j in range(n))
            for i in range(n) for p in (X, Z)]


def top(a):
    return float(np.linalg.eigvalsh((a+a.conj().T)/2)[-1])


def norm(a):
    return float(np.linalg.norm(a, 2))


def require(value, label):
    if value > TOL:
        raise AssertionError(f'{label}: residual {value}')


def unitary(rng, dim):
    q, r = np.linalg.qr(rng.normal(size=(dim, dim))+1j*rng.normal(size=(dim, dim)))
    d = np.diag(r)
    return q@np.diag(d/np.abs(d))


def block(angle):
    return Z, math.cos(angle)*Z+math.sin(angle)*X


def bell_top(angle):
    b, d = block(angle)
    h = np.kron(X, b)+np.kron(Z, d)
    u = math.sqrt(2+2*abs(math.sin(angle)))
    if abs(math.sin(angle)) < 1e-12:
        _, ref = np.linalg.eigh(X+math.cos(angle)*Z)
        coefficient = np.column_stack((ref[:, -1], ref[:, 0]))/R
    else:
        _, vectors = np.linalg.eigh(h)
        coefficient = vectors[:, -1].reshape(2, 2)
    require(norm(h@coefficient.reshape(4)-u*coefficient.reshape(4)), 'Bell eigenvector')
    require(norm(coefficient@coefficient.conj().T-I/2), 'Bell marginal')
    return coefficient, u, math.sqrt(max(0., 4-u*u))


def last_pair(kind, rotation):
    dim = len(rotation)
    b, d = np.eye(dim, dtype=complex), np.eye(dim, dtype=complex)
    if kind == 'scalar':
        k = 0
    elif kind == 'commuting':
        b[-1, -1] = -1
        d[0, 0] = -1
        k = 0
    else:
        k = dim//2 if kind == 'full_blocks' else 2 if kind == 'two_blocks' else 1
        for j in range(k):
            sl = slice(2*j, 2*j+2)
            b[sl, sl], d[sl, sl] = block(math.pi/2 if j % 2 == 0 else .39)
        if kind == 'one_mixed':
            d[-1, -1] = -1
    return rotation@b@rotation.conj().T, rotation@d@rotation.conj().T, k


def insertion(coefficient):
    dim = len(coefficient)
    e = np.zeros((2*dim*dim, 2), dtype=complex)
    for refs in range(dim):
        for last in range(2):
            row = (2*refs+last)*dim
            e[row:row+dim, last] = coefficient[refs]
    return e


def factor_family(name, angles, kind, rotation, last_rotation):
    q = len(angles)
    dim, total = 2**q, 2**(2*q+1)
    refs = query_refs(q+1)
    local = [bell_top(angle) for angle in angles]
    pairs = []
    for j, angle in enumerate(angles):
        b, d = block(angle)
        bq = kron(b if i == j else I for i in range(q))
        dq = kron(d if i == j else I for i in range(q))
        pairs.append((rotation@bq@rotation.conj().T, rotation@dq@rotation.conj().T))
    blast, dlast, k = last_pair(kind, last_rotation)
    pairs.append((blast, dlast))
    hs = [np.kron(refs[2*j], b)+np.kron(refs[2*j+1], d)
          for j, (b, d) in enumerate(pairs)]
    coefficient = kron(p[0] for p in local)@rotation.T
    e = insertion(coefficient)
    p = e@e.conj().T
    u = min(p[1] for p in local)
    v = max(p[2] for p in local)
    c = u-v
    m = sum(p[1] for p in local)-c
    t = 2*q+R-m
    t0 = 2+R-v
    h0 = sum(hs[:-1])
    cross = [norm(a@b-b@a) for i in range(q) for j in range(i+1, q)
             for a in pairs[i] for b in pairs[j]]
    residuals = {
        'reflection_identities': max(norm(a@a-np.eye(dim)) for pair in pairs for a in pair),
        'cross_commutators': max(cross, default=0.),
        'product_Bell_isometry': norm(e.conj().T@e-I),
        'product_Bell_marginal': norm(coefficient.conj().T@coefficient-np.eye(dim)/dim),
        'dedicated_query_spectral_cap': top(h0-m*np.eye(total)-c*p),
        'physical_converse': norm(sum(hs))-(2*q+R),
    }
    recorded = {'name': name, 'q': q, 'angles': list(angles), 'last_kind': kind,
                'Hamiltonian_dimension': total, 'm': m, 'c': c, 't': t, 't0': t0,
                'physical_hamiltonian_norm': norm(sum(hs))}
    if c > 1e-12:
        small_h = np.kron(X, blast)+np.kron(Z, dlast)
        small_resolvent = np.linalg.inv(t0*np.eye(2*dim)-small_h)
        partial = np.trace(small_resolvent.reshape(2, dim, 2, dim), axis1=1, axis2=3)/dim
        compression = e.conj().T@np.linalg.inv(t0*np.eye(total)-hs[-1])@e
        active = c/2*(t0/(t0*t0-4)+1/t0)
        scalar = c/(t0-R)
        weight = 2*k/dim
        bound = weight*active+(1-weight)*scalar
        residuals.update({
            'resolvent_compression_relative_error': norm(compression-partial)/max(1., norm(partial)),
            'Jordan_resolvent_cap': c*top(partial)-bound,
            'active_scalar_inequality': active-5*(4-R)/14,
            'scalar_block_inequality': scalar-1,
            'rank_update_criterion': c*top(partial)-1,
            'positive_rank_update': top(c*p+hs[-1])-t0,
        })
        recorded.update({'active_bracket': active, 'scalar_bracket': scalar,
                         'resolvent_compression_norm': c*top(partial)})
    else:
        residuals['zero_c_triangle'] = sum(p[1] for p in local)+2-(2*q+R)
    if kind == 'scalar' and all(abs(angle-math.pi/2) < 1e-12 for angle in angles):
        residuals['scalar_attainment'] = abs(recorded['physical_hamiltonian_norm']-(2*q+R))
    for key, value in residuals.items():
        require(value, name+' '+key)
    recorded['residuals'] = residuals
    return recorded


def extra_ququart_cases(rng):
    refs = query_refs(3)
    cases = []
    for direct in (True, False):
        for orientation in range(2):
            rotation = np.eye(4) if orientation == 0 else unitary(rng, 4)
            b1, d1 = np.eye(4, dtype=complex), np.eye(4, dtype=complex)
            b2, d2 = np.eye(4, dtype=complex), np.eye(4, dtype=complex)
            if direct:
                b1[:2, :2], d1[:2, :2] = block(.83)
                b2[2:, 2:], d2[2:, 2:] = block(1.22)
            else:
                b1 = np.diag([1., 1., -1., -1.]).astype(complex)
                d1 = np.diag([1., -1., 1., -1.]).astype(complex)
                b2, d2, _ = last_pair('full_blocks', unitary(rng, 4))
            pairs = [(rotation@b@rotation.conj().T, rotation@d@rotation.conj().T)
                     for b, d in ((b1, d1), (b2, d2))]
            b3, d3, _ = last_pair('full_blocks', unitary(rng, 4))
            pairs.append((b3, d3))
            hs = [np.kron(refs[2*j], b)+np.kron(refs[2*j+1], d)
                  for j, (b, d) in enumerate(pairs)]
            residuals = {'physical_converse': norm(sum(hs))-(4+R)}
            if direct:
                residuals['cross_commutators'] = max(norm(a@b-b@a) for a in pairs[0] for b in pairs[1])
            else:
                residuals['internally_commuting_pair'] = norm(pairs[0][0]@pairs[0][1]-pairs[0][1]@pairs[0][0])
                residuals['commuting_local_norm'] = norm(hs[0])-R
            for key, value in residuals.items():
                require(value, 'extra '+key)
            cases.append({'kind': 'direct_sum' if direct else 'internally_commuting',
                          'orientation': orientation, 'physical_hamiltonian_norm': norm(sum(hs)),
                          'residuals': residuals})
    return cases


def cap_obstruction():
    refs = query_refs(3)
    e = insertion(np.eye(4)/2)
    h12 = (np.kron(refs[0], np.kron(X, I))+np.kron(refs[1], np.kron(Z, I))
           +np.kron(refs[2], np.kron(I, X))+np.kron(refs[3], np.kron(I, Z)))
    third_bell = np.zeros(8, dtype=complex)
    third_bell[0] = third_bell[5] = 1/R
    pi = np.kron(np.eye(4), np.outer(third_bell, third_bell.conj()))
    compression = e.conj().T@pi@e
    expected = 4+DELTA/8
    require(norm(compression-I/8), 'cap obstruction compression')
    require(norm(e.conj().T@h12@e-4*I), 'cap obstruction Bell energy')
    require(expected-top(h12+DELTA*pi), 'cap obstruction Rayleigh lower bound')
    return {'delta': DELTA, 'Rayleigh_lower_bound': expected,
            'actual_capped_eigenvalue': top(h12+DELTA*pi),
            'compression_residual': norm(compression-I/8)}


def run():
    rng = np.random.default_rng(SEED)
    cases = []
    for q in (1, 2, 3):
        angle_sets = [[0.]*q, [math.pi/2]*q, [.3+.2*j for j in range(q)],
                      [1e-4]+[1.1]*(q-1), [math.pi/2]*(q-1)+[0.]]
        kinds = ['scalar', 'commuting', 'full_blocks']
        if q >= 2:
            kinds += ['one_plus', 'one_mixed']
        if q == 3:
            kinds += ['two_blocks']
        for ai, angles in enumerate(angle_sets):
            for kind in kinds:
                for orientation in range(2):
                    rotations = ([np.eye(2**q, dtype=complex)]*2 if orientation == 0
                                 else [unitary(rng, 2**q), unitary(rng, 2**q)])
                    name = f'q{q}_angles_{ai}_{kind}_rotation_{orientation}'
                    cases.append(factor_family(name, angles, kind, *rotations))
    return {'reviewed_main': BASE, 'seed': SEED, 'tolerance': TOL,
            'python': platform.python_version(), 'numpy': np.__version__,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'factor_case_count': len(cases), 'factor_cases': cases,
            'extra_ququart_cases': extra_ququart_cases(rng),
            'cap_obstruction': cap_obstruction(), 'status': 'PASS'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(payload)
        print(f'PASS: {result["factor_case_count"]} factor cases, four extra cases, and cap obstruction')
    else:
        print(payload, end='')


if __name__ == '__main__':
    main()
