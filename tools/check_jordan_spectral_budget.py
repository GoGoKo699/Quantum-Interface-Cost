#!/usr/bin/env python3
"""Deterministic small checks of the all-Jordan-block spectral budget.

No optimizer, global optimality certificate, or literature claim.

    python tools/check_jordan_spectral_budget.py --output results/jordan_spectral_budget.json
"""
import argparse
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path
import numpy as np

BASE = '780605b723919defd382d88c8adb09ed1fd8d204'
SEED = 2026092406
TOL = 1e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
DELTA = 2-math.sqrt(2)
WEIGHTS = {'uniform': [1.]*6,
           'unequal': [.3, 1.1, .5, 1.7, 1.4, .8],
           'with_zero': [0., 1.1, .8, .3, 1.2, 0.]}


def kron(items):
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


QUERIES = [kron(p if j == i else I for j in range(3))
           for i in range(3) for p in (X, Z)]
YS = [np.kron(kron(Y if j == i else I for j in range(3)), np.eye(4))
      for i in range(3)]


def require(residual, description):
    if residual > TOL:
        raise AssertionError(f'{description}: residual {residual}')


def opnorm(a):
    return float(np.linalg.norm(a, 2))


def dense_unitary(rng):
    q, r = np.linalg.qr(rng.normal(size=(4, 4))+1j*rng.normal(size=(4, 4)))
    d = np.diag(r)
    return q@np.diag(d/np.abs(d))


def insert(phi, site):
    out = np.zeros((32, 4), dtype=complex)
    coefficients = phi.reshape(2, 4)
    others = [j for j in range(3) if j != site]
    for column in range(4):
        bits = [0, 0, 0]
        bits[others[0]], bits[others[1]] = column//2, column % 2
        for bit in range(2):
            bits[site] = bit
            index = 4*bits[0]+2*bits[1]+bits[2]
            out[4*index:4*index+4, column] = coefficients[bit]
    return out


def comparison(excesses, sites):
    g = np.diag(excesses).astype(float)
    for j in range(len(sites)):
        for k in range(j+1, len(sites)):
            if sites[j] != sites[k]:
                g[j, k] = g[k, j] = math.sqrt(excesses[j]*excesses[k])/2
    return g


def budget(excesses, sites, threshold):
    if threshold <= max(excesses, default=0.):
        raise ValueError('Budget formula requires threshold > every excess')
    cs = [sum(a/(threshold-a) for a, s in zip(excesses, sites) if s == i)
          for i in range(3)]
    return sum(c/(2+c) for c in cs)


def canonical_pair(angles, site):
    b, d = np.eye(4, dtype=complex), np.eye(4, dtype=complex)
    # With one active block, alternate scalar complement signatures (11)/(12).
    if len(angles) == 1 and site % 2:
        d[3, 3] = -1
    for k, angle in enumerate(angles):
        sl = slice(2*k, 2*k+2)
        b[sl, sl] = Z
        d[sl, sl] = math.cos(angle)*Z+math.sin(angle)*X
    return b, d


def check_family(name, angles, rotations, weights):
    readouts, es, excesses, sites, radii, tops = [], [], [], [], [], []
    marginal_error = cap_error = eigenvector_error = reflection_error = 0.
    for i in range(3):
        a, b = weights[2*i:2*i+2]
        r = math.hypot(a, b)
        radii.append(r)
        canonical_b, canonical_d = canonical_pair(angles[i], i)
        unitary = rotations[i]
        bi = unitary@canonical_b@unitary.conj().T
        di = unitary@canonical_d@unitary.conj().T
        readouts.extend([bi, di])
        reflection_error = max(reflection_error, opnorm(bi@bi-np.eye(4)),
                               opnorm(di@di-np.eye(4)))
        h = a*np.kron(X, bi)+b*np.kron(Z, di)
        cap = r*np.eye(8, dtype=complex)
        local_tops = [r]
        for k, angle in enumerate(angles[i]):
            u = math.sqrt(r*r+2*a*b*abs(math.sin(angle)))
            alpha = max(0., u-r)
            local_tops.append(u)
            # Only diagonalize when the top eigenvalue is provably simple.
            # At zero weights alpha is zero; an arbitrary Bell vector suffices.
            if alpha > 0:
                block = a*np.kron(X, Z)+b*np.kron(Z, math.cos(angle)*Z+math.sin(angle)*X)
                ev, vectors = np.linalg.eigh(block)
                small_phi = vectors[:, -1].reshape(2, 2)
                eigenvector_error = max(eigenvector_error, abs(float(ev[-1])-u))
            else:
                small_phi = np.eye(2, dtype=complex)/math.sqrt(2)
            coefficient = np.zeros((2, 4), dtype=complex)
            coefficient[:, 2*k:2*k+2] = small_phi
            coefficient = coefficient@unitary.T
            phi = coefficient.reshape(8)
            marginal_error = max(marginal_error, opnorm(coefficient@coefficient.conj().T-I/2))
            cap += alpha*np.outer(phi, phi.conj())
            es.append(insert(phi, i)); excesses.append(alpha); sites.append(i)
        tops.append(max(local_tops))
        cap_error = max(cap_error, -float(np.linalg.eigvalsh(cap-h)[0]))
    same_overlap = cross_overlap = 0.
    for j in range(len(es)):
        for k in range(j+1, len(es)):
            overlap = opnorm(es[j].conj().T@es[k])
            if sites[j] == sites[k]:
                same_overlap = max(same_overlap, overlap)
            else:
                cross_overlap = max(cross_overlap, overlap)
    g = comparison(excesses, sites)
    glambda = float(np.linalg.eigvalsh(g)[-1])
    q = sum(alpha*(e@e.conj().T) for alpha, e in zip(excesses, es))
    qnorm = float(np.linalg.eigvalsh(q)[-1])
    h = sum(w*np.kron(p, b) for w, p, b in zip(weights, QUERIES, readouts))
    hnorm = opnorm(h)
    certified_threshold = glambda+1e-7
    scalar_budget = budget(excesses, sites, certified_threshold)
    for residual, description in [
        (reflection_error, 'reflection identity'),
        (eigenvector_error, 'analytical top eigenvalue'),
        (marginal_error, 'Bell marginal'), (cap_error, 'local cap'),
        (same_overlap, 'same-site orthogonality'),
        (cross_overlap-.5, 'cross-site Bell overlap'),
        (qnorm-glambda, 'comparison matrix majorant'),
        (hnorm-sum(radii)-glambda, 'Hamiltonian bound'),
        (scalar_budget-1, 'scalar certificate at safe threshold')]:
        require(residual, name+' '+description)
    threshold_check = None
    if np.array_equal(weights, np.ones(6)):
        target_budget = budget(excesses, sites, 2*DELTA)
        gap = glambda-2*DELTA
        if abs(gap) > 1e-8 and abs(target_budget-1) > 1e-8:
            if (gap > 0) != (target_budget > 1):
                raise AssertionError(name+' threshold sign mismatch')
        threshold_check = {'threshold': 2*DELTA, 'budget': target_budget,
                           'comparison_gap': gap,
                           'certifies_interface_benchmark': target_budget <= 1+TOL}
    return {'name': name, 'weights': list(weights), 'active_block_counts': list(map(len, angles)),
            'excesses': excesses, 'reflection_error': reflection_error,
            'max_top_eigenvalue_error': eigenvector_error,
            'max_Bell_marginal_error': marginal_error, 'max_local_cap_violation': cap_error,
            'max_same_site_overlap': same_overlap, 'max_cross_site_overlap': cross_overlap,
            'weighted_projector_norm': qnorm, 'comparison_largest_eigenvalue': glambda,
            'hamiltonian_norm': hnorm, 'certified_operator_upper_bound': sum(radii)+glambda,
            'triangle_upper_bound': sum(tops), 'safe_threshold_budget': scalar_budget,
            'interface_threshold_check': threshold_check}


def angle_for_excess(coefficient):
    u = math.sqrt(2)+DELTA*coefficient
    sine = min(1., max(0., (u*u-2)/2))
    return math.asin(sine)


def signed_counterexamples():
    plus = []
    p1 = np.zeros((32, 32), dtype=complex)
    for b in range(2):
        phi = np.zeros(8, dtype=complex)
        for a in range(2):
            phi[4*a+2*a+b] = 1/math.sqrt(2)
        e = insert(phi, 0)
        p1 += e@e.conj().T
    plus.append(p1)
    phi = np.zeros(8, dtype=complex)
    phi[0] = phi[5] = 1/math.sqrt(2)
    plus.extend(insert(phi, i)@insert(phi, i).conj().T for i in (1, 2))
    minus = [y@p@y for p, y in zip(plus, YS)]
    rows = []
    for kappa in (1., 2+2*math.sqrt(2), 10., 100.):
        signed = sum(p-kappa*m for p, m in zip(plus, minus))
        actual = float(np.linalg.eigvalsh(signed)[-1])
        t = (3*(1-kappa)+math.sqrt((1-kappa)**2+8*(1+kappa)**2))/4
        exact = (t+1+math.sqrt(t*t+1))/2
        require(abs(actual-exact), 'signed counterexample exact spectrum')
        if actual <= 2:
            raise AssertionError('Expected signed-projector failure absent')
        rows.append({'kappa': kappa, 'computed_largest_eigenvalue': actual,
                     'exact_largest_eigenvalue': exact, 'excess_above_two': actual-2})
    p0 = np.diag([1., 0.]); p1 = I-p0
    cx = np.kron(p0, X)+np.kron(p1, I)
    cz = np.kron(p0, Z)+np.kron(p1, I)
    readouts = [np.kron(X, I), np.kron(Z, I), cx, cz, cx, cz]
    h = sum(np.kron(p, b) for p, b in zip(QUERIES, readouts))
    norm = opnorm(h)
    require(norm-(2+2*math.sqrt(2)), 'physical example analytical upper bound')
    return {'signed_cases': rows, 'physical_hamiltonian_norm': norm,
            'physical_hamiltonian_upper_bound': 2+2*math.sqrt(2)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path('results/jordan_spectral_budget.json'))
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    families = []
    for pattern in itertools.product((1, 2), repeat=3):
        angles = [[.23+.17*i]+([.79+.13*i] if m == 2 else [])
                  for i, m in enumerate(pattern)]
        for kind in ('canonical', 'dense_complex'):
            rotations = [np.eye(4) for _ in range(3)] if kind == 'canonical' else [dense_unitary(rng) for _ in range(3)]
            for wn, w in WEIGHTS.items():
                families.append(check_family(''.join(map(str, pattern))+'_'+kind+'_'+wn,
                                             angles, rotations, w))
    explicit = []
    examples = {'one_double_half_excess': [[.5, .5], [1.], [1.]],
                'three_double_uneven_excess': [[.9, .2]]*3}
    for name, coefficients in examples.items():
        angles = [[angle_for_excess(c) for c in row] for row in coefficients]
        row = check_family(name, angles, [dense_unitary(rng) for _ in range(3)], [1.]*6)
        if not row['interface_threshold_check']['certifies_interface_benchmark']:
            raise AssertionError(name+' must satisfy interface budget')
        if row['triangle_upper_bound'] <= 4+math.sqrt(2):
            raise AssertionError(name+' must improve on the triangle comparison')
        if name == 'one_double_half_excess':
            require(abs(row['comparison_largest_eigenvalue']/DELTA-(1+math.sqrt(3)/2)),
                    'one-double exact comparison eigenvalue')
        else:
            require(abs(row['comparison_largest_eigenvalue']/DELTA-(11+math.sqrt(67))/10),
                    'three-double exact comparison eigenvalue')
            require(abs(row['interface_threshold_check']['budget']-138/145),
                    'three-double exact scalar budget')
            if sum(row['excesses']) <= 3*DELTA:
                raise AssertionError(name+' must exceed the coarse total-excess certificate')
        explicit.append(row)
    report = {'status': 'PASS', 'research_base': BASE, 'random_seed': SEED,
              'tolerance': TOL, 'scope': 'Finite deterministic construction checks; no optimizer, unrestricted proof, or priority certificate.',
              'environment': {'python': platform.python_version(), 'numpy': np.__version__},
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'family_count': len(families), 'explicit_example_count': len(explicit),
              'maximum_hamiltonian_dimension': 32, 'families': families,
              'explicit_examples': explicit, 'signed_obstruction': signed_counterexamples()}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': 'PASS', 'family_count': len(families),
                      'explicit_example_count': len(explicit), 'output': str(args.output)}))


if __name__ == '__main__':
    main()
