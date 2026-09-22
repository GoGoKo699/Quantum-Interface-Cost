#!/usr/bin/env python3
"""Finite diagnostics for the exact one-retained-qubit tradeoff.

Checks explicit optimizers, the scalar-decoder identity, the CHSH bridge,
and deterministic complex seeds. The D=4 negative control documents why
central-qubit monogamy cannot be used for arbitrary output dimension.
No optimization is performed. These checks do not prove a global bound,
classify optimizers, or establish novelty; the analytic argument is separate.

Run from the repository root:
    python tools/check_one_qubit_tradeoff.py --output results/one_qubit_tradeoff.json
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
SEED = 20260923


def tensor(items):
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


def local_paulis(n):
    return [tensor(p if k == i else I for k in range(n))
            for i in range(n) for p in (X, Z)]


def trace_norm_hermitian(a):
    return float(np.sum(np.abs(np.linalg.eigvalsh(a))))


def extreme_sign(a):
    values, vectors = np.linalg.eigh(a)
    # Either sign is dual-optimal on a zero eigenspace. Choosing +1 keeps
    # the decoder an extreme Hermitian contraction (a reflection).
    return (vectors * np.where(values >= 0, 1., -1.)) @ vectors.conj().T


def check_seed(l, n, tolerance):
    ps = local_paulis(n)
    matrices = [l @ p @ l.conj().T for p in ps]
    bs = [extreme_sign(a) for a in matrices]
    scores = [trace_norm_hermitian(a) for a in matrices]
    f = [scores[2*i]+scores[2*i+1] for i in range(n)]
    # Input-then-output vectorization agrees with P^T tensor B.
    vector = l.T.reshape(-1)
    h = sum(np.kron(p.T, b) for p, b in zip(ps, bs))
    dual_score = float(np.vdot(vector, h @ vector).real)
    norm_error = abs(float(np.vdot(l, l).real)-1)
    dual_error = abs(sum(scores)-dual_score)
    reflection_error = max(float(np.max(np.abs(b @ b-I))) for b in bs)
    traceless = [abs(np.trace(b)) < tolerance for b in bs]
    scalar = [abs(abs(np.trace(b))-2) < tolerance for b in bs]
    if any(not (a or b) for a, b in zip(traceless, scalar)):
        raise AssertionError('An extreme qubit decoder was neither scalar nor traceless.')
    active = [i for i in range(n) if traceless[2*i] and traceless[2*i+1]]
    pair_values = [f[i]**2+f[j]**2 for pos, i in enumerate(active)
                   for j in active[pos+1:]]
    if pair_values and max(pair_values) > 4+tolerance:
        raise AssertionError('Complex-seed qubit CHSH diagnostic failed.')
    upper = 2+math.sqrt(2)*(n-1)
    branch_upper = n*math.sqrt(2) if len(active) >= 2 else upper
    if sum(scores) > branch_upper+tolerance:
        raise AssertionError('Seed exceeded the applicable analytic bound.')
    error = max(norm_error, dual_error, reflection_error)
    if error > tolerance:
        raise AssertionError('Seed normalization or trace-norm duality failed.')
    return {'n':n, 'output_dimension':2, 'score':sum(scores),
            'one_qubit_bound':upper, 'site_scores':f, 'active_sites':active,
            'active_pair_squared_scores':pair_values,
            'normalization_error':norm_error, 'duality_error':dual_error,
            'reflection_error':reflection_error, 'max_identity_error':error}


def random_pauli(rng):
    direction = rng.normal(size=3)
    direction /= np.linalg.norm(direction)
    return sum(c*p for c, p in zip(direction, (X, Y, Z)))


def check_decoder_identities(rng, tolerance):
    cases = []
    for mode in ('scalar_scalar', 'scalar_traceless', 'traceless_scalar',
                 'traceless_traceless'):
        for signs in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            types = mode.split('_')
            bs = [s*(I if kind == 'scalar' else random_pauli(rng))
                  for s, kind in zip(signs, types)]
            h = np.kron(X, bs[0])+np.kron(Z, bs[1])
            a0, a1 = (X+Z)/math.sqrt(2), (X-Z)/math.sqrt(2)
            chsh = np.kron(a0+a1, bs[0])+np.kron(a0-a1, bs[1])
            bridge_error = float(np.max(np.abs(chsh-math.sqrt(2)*h)))
            operator_norm = float(np.max(np.abs(np.linalg.eigvalsh(h))))
            square_error = None
            if 'scalar' in types:
                square_error = float(np.max(np.abs(h @ h-2*np.eye(4))))
                norm_error = abs(operator_norm-math.sqrt(2))
                if max(square_error, norm_error) > tolerance:
                    raise AssertionError('Scalar-decoder identity failed.')
            elif operator_norm > 2+tolerance:
                raise AssertionError('Two-decoder operator norm exceeded two.')
            if bridge_error > tolerance:
                raise AssertionError('CHSH normalization failed.')
            cases.append({'decoder_types':mode, 'signs':list(signs),
                          'operator_norm':operator_norm,
                          'scalar_square_error':square_error,
                          'chsh_bridge_error':bridge_error})
    return cases


def check_large_memory_negative_control(tolerance):
    # vec(I_4/2) contains two Bell pairs: each queried site is perfectly
    # correlated with its own output qubit. The shared output has D=4.
    l = np.eye(4, dtype=complex)/2
    scores = [trace_norm_hermitian(l @ p @ l.conj().T)
              for p in local_paulis(2)]
    f = [sum(scores[:2]), sum(scores[2:])]
    pair_value = sum(value**2 for value in f)
    if abs(pair_value-8) > tolerance or pair_value <= 4+tolerance:
        raise AssertionError('D=4 negative control did not violate the qubit-only bound.')
    return {'n':2, 'output_dimension':4, 'seed':'I_4/2 (two Bell pairs)',
            'site_scores':f, 'pair_squared_score':pair_value,
            'qubit_only_pair_bound':4,
            'scope':'Expected violation: central-qubit monogamy requires D=2.'}


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Tolerance must be finite and positive.')
    rng = np.random.default_rng(SEED)
    cases = []
    row = np.array([[math.cos(math.pi/8), math.sin(math.pi/8)]], dtype=complex)
    for n in range(1, 5):
        for kept in range(n):
            l = tensor(I/math.sqrt(2) if i == kept else row for i in range(n))
            result = check_seed(l, n, tolerance)
            result.update({'seed_type':'explicit_optimizer', 'kept_site':kept})
            if abs(result['score']-result['one_qubit_bound']) > tolerance:
                raise AssertionError('Explicit optimizer missed its claimed value.')
            cases.append(result)
        for index in range(4):
            l = rng.normal(size=(2, 2**n))+1j*rng.normal(size=(2, 2**n))
            l /= np.linalg.norm(l)
            result = check_seed(l, n, tolerance)
            result.update({'seed_type':'dense_complex', 'sample':index})
            cases.append(result)
    identities = check_decoder_identities(rng, tolerance)
    negative_control = check_large_memory_negative_control(tolerance)
    identity_errors = [c['max_identity_error'] for c in cases]
    identity_errors += [c['chsh_bridge_error'] for c in identities]
    identity_errors += [c['scalar_square_error'] for c in identities
                        if c['scalar_square_error'] is not None]
    return {'status':'PASS', 'python':platform.python_version(),
            'numpy':np.__version__, 'seed':SEED, 'tolerance':tolerance,
            'counts':{'explicit_optimizers':10, 'dense_complex_seeds':16,
                      'decoder_identity_cases':len(identities),
                      'large_memory_negative_controls':1},
            'max_identity_error':max(identity_errors),
            'seed_cases':cases, 'decoder_identities':identities,
            'large_memory_negative_control':negative_control,
            'scope':'Finite constructive and algebraic diagnostics only. No numerical optimality, proof, or novelty certification.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--tolerance', type=float, default=1e-10)
    args = parser.parse_args()
    report = run(args.tolerance)
    text = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
