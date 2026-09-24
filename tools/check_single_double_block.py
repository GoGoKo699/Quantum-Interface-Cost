#!/usr/bin/env python3
"""Small deterministic diagnostics for the one-double-Jordan-block converse.

These construction checks supplement the proof; no optimizer or global
optimality/priority certificate is used.
"""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import numpy as np

BASE = 'ac5863e1e026a8a9432a27385e6ee9491b423e92'
SEED = 2026092407
TOL = 1e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
R = math.sqrt(2)
DELTA = 2-R
TARGET = 4-R


def kron(items):
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


QUERIES = [kron(p if j == i else I for j in range(3))
           for i in range(3) for p in (X, Z)]


def top(a):
    return float(np.linalg.eigvalsh((a+a.conj().T)/2)[-1])


def norm(a):
    return float(np.linalg.norm(a, 2))


def require(residual, label):
    if residual > TOL:
        raise AssertionError(f'{label}: residual {residual}')


def unitary(rng):
    q, r = np.linalg.qr(rng.normal(size=(4, 4))+1j*rng.normal(size=(4, 4)))
    d = np.diag(r)
    return q@np.diag(d/np.abs(d))


def insert(phi, site):
    e = np.zeros((32, 4), dtype=complex)
    coefficients = phi.reshape(2, 4)
    others = [j for j in range(3) if j != site]
    for c in range(4):
        bits = [0, 0, 0]
        bits[others[0]], bits[others[1]] = c//2, c % 2
        for bit in range(2):
            bits[site] = bit
            row = 4*bits[0]+2*bits[1]+bits[2]
            e[4*row:4*row+4, c] = coefficients[bit]
    return e


def bell_top(angle):
    h = np.kron(X, Z)+np.kron(Z, math.cos(angle)*Z+math.sin(angle)*X)
    u = math.sqrt(2+2*abs(math.sin(angle)))
    if abs(math.sin(angle)) < 1e-12:
        # Top eigenspace is degenerate. Select a Bell vector analytically.
        ev, ref = np.linalg.eigh(X+math.cos(angle)*Z)
        coefficient = np.column_stack((ref[:, -1], ref[:, 0]))/R
        phi = coefficient.reshape(4)
    else:
        ev, vectors = np.linalg.eigh(h)
        phi = vectors[:, -1]
    require(norm(h@phi-u*phi), 'local Bell eigenvector')
    m = phi.reshape(2, 2)
    require(norm(m@m.conj().T-I/2), 'local Bell marginal')
    return phi.reshape(2, 2), u


def pair(angles, signature, rotation, site):
    b = np.eye(4, dtype=complex)
    d = np.eye(4, dtype=complex)
    if signature == '12':
        d[3, 3] = -1
    es, us = [], []
    for k, angle in enumerate(angles):
        sl = slice(2*k, 2*k+2)
        b[sl, sl] = Z
        d[sl, sl] = math.cos(angle)*Z+math.sin(angle)*X
        small, u = bell_top(angle)
        coefficient = np.zeros((2, 4), dtype=complex)
        coefficient[:, sl] = small
        coefficient = coefficient@rotation.T
        es.append(insert(coefficient.reshape(8), site))
        us.append(u)
    b = rotation@b@rotation.conj().T
    d = rotation@d@rotation.conj().T
    require(norm(b@b-np.eye(4)), 'reflection B')
    require(norm(d@d-np.eye(4)), 'reflection D')
    return b, d, es, us


def family(name, angles, signatures, rotations):
    hs, projectors, tops, maps = [], [], [], []
    for site in range(3):
        b, d, es, us = pair(angles[site], signatures[site], rotations[site], site)
        hs.append(np.kron(QUERIES[2*site], b)+np.kron(QUERIES[2*site+1], d))
        projectors.append([e@e.conj().T for e in es])
        tops.append(us)
        maps.append(es)
    order = np.argsort(tops[0])[::-1]
    u0, u = [tops[0][j] for j in order]
    p0, p1 = [projectors[0][j] for j in order]
    e = np.column_stack([maps[0][j] for j in order])
    v = math.sqrt(max(0., 4-u*u))
    k = projectors[1][0]+projectors[2][0]
    kp = e.conj().T@k@e
    c = (u0-v)*p0+(u-v)*p1
    z = TARGET-v
    resolvent = np.linalg.inv(z*np.eye(32)-DELTA*k)
    chord = np.eye(32)/z+DELTA*k/(z*(z-1.5*DELTA))
    d0, d1 = (u0-v)/(TARGET-u0), (u-v)/(TARGET-u)
    sd = np.diag(np.sqrt(np.repeat([d0, d1], 4)))
    weighted_norm = top(sd@kp@sd)
    comparison = .5*d0+.25*d1
    residuals = {
        'h1_positive_spectrum_cap': top(hs[0]-v*np.eye(32)-c),
        'other_local_caps': max(top(hs[j]-R*np.eye(32)-DELTA*projectors[j][0]) for j in (1, 2)),
        'K_norm': top(k)-1.5,
        'rank_one_compression': max(top(p@k@p)-.5 for p in (p0, p1)),
        'rank_two_compression': top(kp)-.75,
        'resolvent_chord': top(resolvent-chord),
        'weighted_compression': weighted_norm-comparison,
        'scalar_conclusion': DELTA*comparison-(z-1.5*DELTA),
        'asymmetric_converse': top(hs[0]+DELTA*k)-TARGET,
        'physical_converse': norm(sum(hs))-(4+R),
    }
    for key, value in residuals.items():
        require(value, name+' '+key)
    return {'name': name, 'signatures': list(signatures),
            'angles': [list(x) for x in angles], 'u0': u0, 'u1': u,
            'v': v, 'd0': d0, 'd1': d1,
            'weighted_compression_norm': weighted_norm,
            'weighted_comparison': comparison,
            'asymmetric_largest_eigenvalue': top(hs[0]+DELTA*k),
            'physical_hamiltonian_norm': norm(sum(hs)),
            'residuals': residuals}


def choi_factor(rng, central_dim, env_dim, site):
    rows = central_dim*env_dim
    v, _ = np.linalg.qr(rng.normal(size=(rows, 2))+1j*rng.normal(size=(rows, 2)))
    f = np.zeros((4*central_dim, 2*env_dim), dtype=complex)
    rho = np.zeros((2*central_dim, 2*central_dim), dtype=complex)
    for a in range(env_dim):
        kraus = v[a*central_dim:(a+1)*central_dim]
        phi = kraus.T.reshape(2*central_dim)/R
        rho += np.outer(phi, phi.conj())
        for other in range(2):
            for leaf in range(2):
                bits = [other, other]
                bits[site] = leaf
                row = 2*bits[0]+bits[1]
                f[row*central_dim:(row+1)*central_dim, 2*a+other] = kraus[:, leaf]/R
    marginal = np.trace(rho.reshape(2, central_dim, 2, central_dim), axis1=1, axis2=3)
    require(norm(marginal-I/2), 'mixed Choi leaf marginal')
    return f


def mixed_choi_cases(rng):
    cases = []
    for dim, env in ((2, 2), (2, 3), (3, 2), (3, 3)):
        f = choi_factor(rng, dim, env, 0)
        g = choi_factor(rng, dim, env+1, 1)
        cross = norm(f.conj().T@g)
        star = top(f@f.conj().T+g@g.conj().T)
        require(cross-.5, 'mixed Choi cross Gram')
        require(star-1.5, 'mixed Choi star')
        cases.append({'central_dimension': dim, 'environment_dimensions': [env, env+1],
                      'cross_Gram_norm': cross, 'star_norm': star})
    return cases


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    cases = []
    angle_sets = ((math.pi/2, 0.), (math.pi/2, math.pi/2), (.31, 1.11), (2.41, .72))
    for others in (('11', '11'), ('11', '12'), ('12', '12')):
        for a, first in enumerate(angle_sets):
            tail = (math.pi/2, math.pi/2) if a % 2 == 0 else (.63, 1.07)
            angles = (first, (tail[0],), (tail[1],))
            for rotation_index in range(4):
                rotations = [np.eye(4, dtype=complex)]*3 if rotation_index == 0 else [unitary(rng) for _ in range(3)]
                label = '-'.join(others)+f'-angles{a}-rotation{rotation_index}'
                cases.append(family(label, angles, ('22',)+others, rotations))
    choi = mixed_choi_cases(rng)
    maxima = {key: max(case['residuals'][key] for case in cases) for key in cases[0]['residuals']}
    result = {'reviewed_main': BASE, 'seed': SEED, 'tolerance': TOL,
              'python': platform.python_version(), 'numpy': np.__version__,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'family_count': len(cases), 'mixed_Choi_count': len(choi),
              'maximum_hamiltonian_dimension': 32,
              'max_residuals': maxima, 'construction_cases': cases,
              'mixed_Choi_cases': choi, 'status': 'PASS',
              'scope': 'Finite construction diagnostics supplement the supplied proof; no optimizer, unrestricted optimum, or priority certification.'}
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({'status': result['status'], 'families': len(cases), 'mixed_Choi': len(choi), 'max_residuals': maxima}, sort_keys=True))


if __name__ == '__main__':
    main()
