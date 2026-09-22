#!/usr/bin/env python3
"""Small constructive checks of the seed-to-interface reduction.

No optimization is performed. A passing test does not prove a converse or
establish optimality or novelty. NumPy only; n is deliberately capped at two.
Run from the repository root:
    python tools/check_seed_twirl.py --output results/seed_twirl.json
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

Matrix = NDArray[np.complex128]
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = (X + Z) / math.sqrt(2)


def tensor(items) -> Matrix:
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


def sign_matrix(a: Matrix) -> Matrix:
    values, vectors = np.linalg.eigh((a + a.conj().T) / 2)
    return (vectors * np.sign(values)) @ vectors.conj().T


def local_paulis(n: int) -> list[Matrix]:
    return [tensor(p if k == i else I for k in range(n))
            for i in range(n) for p in (X, Z)]


def permutations(n: int) -> list[Matrix]:
    out = []
    d = 2**n
    for order in itertools.permutations(range(n)):
        mat = np.zeros((d, d), dtype=complex)
        for old in range(d):
            bits = [(old >> (n - 1 - k)) & 1 for k in range(n)]
            new = sum(bits[order[k]] << (n - 1 - k) for k in range(n))
            mat[new, old] = 1
        out.append(mat)
    return out


def verify_seed(l: Matrix, n: int, tolerance: float) -> dict:
    d = 2**n
    if n not in (1, 2) or l.shape[1] != d:
        raise ValueError('Use n=1 or n=2 and a D-by-2**n seed.')
    if abs(float(np.vdot(l, l).real) - 1) > tolerance:
        raise ValueError('The seed must have Frobenius norm one.')
    ps = local_paulis(n)
    compressed = [l @ p @ l.conj().T for p in ps]
    decoders = [sign_matrix(a) for a in compressed]
    scores = [float(np.trace(a @ b).real) for a, b in zip(compressed, decoders)]
    eta = sum(scores) / (2*n)
    paulis = [tensor(t) for t in itertools.product((I, X, Y, Z), repeat=n)]
    symmetries = [perm @ tensor(t) for perm in permutations(n)
                  for t in itertools.product((I, H), repeat=n)]
    completeness = np.zeros((d, d), dtype=complex)
    effective = [np.zeros((d, d), dtype=complex) for _ in ps]
    factor = math.sqrt(d / (len(paulis)*len(symmetries)))
    for v in symmetries:
        mapping = []
        for p in ps:
            rotated = v @ p @ v.conj().T
            matches = [k for k, target in enumerate(ps)
                       if np.max(np.abs(rotated-target)) < tolerance]
            if len(matches) != 1:
                raise AssertionError('Symmetry failed to permute local queries.')
            mapping.append(matches[0])
        for u in paulis:
            kraus = factor * l @ u @ v
            adjoint = kraus.conj().T
            completeness += adjoint @ kraus
            for j, k in enumerate(mapping):
                character = float(np.trace(ps[k] @ u @ ps[k] @ u.conj().T).real / d)
                if abs(abs(character)-1) > tolerance:
                    raise AssertionError('Invalid Pauli character.')
                effective[j] += adjoint @ (character*decoders[k]) @ kraus
    tp_error = float(np.max(np.abs(completeness-np.eye(d))))
    effect_error = max(float(np.max(np.abs(a-eta*p))) for a,p in zip(effective,ps))
    max_decoder_norm = max(float(np.max(np.abs(np.linalg.eigvalsh(b)))) for b in decoders)
    if tp_error > tolerance or effect_error > tolerance or max_decoder_norm > 1+tolerance:
        raise AssertionError((tp_error,effect_error,max_decoder_norm))
    return {'n':n, 'output_dimension':l.shape[0], 'eta':eta,
            'seed_score':sum(scores), 'kraus_branches':len(paulis)*len(symmetries),
            'trace_preservation_error':tp_error, 'observable_error':effect_error}


def run(tolerance: float) -> dict:
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Tolerance must be finite and positive.')
    rng = np.random.default_rng(20260922)
    cases = []
    row = np.array([[math.cos(math.pi/8),math.sin(math.pi/8)]], dtype=complex)
    for n in (1,2):
        for q in range(n+1):
            # A kept-qubit factor and pure bisector factors reproduce the subset score.
            l = np.kron(np.eye(2**q),tensor([row]*(n-q))) / math.sqrt(2**q)
            result = verify_seed(l,n,tolerance)
            expected = 1/math.sqrt(2) + (q/n)*(1-1/math.sqrt(2))
            if abs(result['eta']-expected) > tolerance:
                raise AssertionError('Subset-score identity failed.')
            result.update({'seed_type':'subset', 'q':q, 'expected_eta':expected})
            cases.append(result)
            l = rng.normal(size=(2**q,2**n)) + 1j*rng.normal(size=(2**q,2**n))
            l = l/np.linalg.norm(l)
            result = verify_seed(l,n,tolerance)
            result.update({'seed_type':'dense_complex', 'q':q})
            cases.append(result)
    return {'status':'PASS', 'python':platform.python_version(), 'numpy':np.__version__,
            'seed':20260922, 'tolerance':tolerance, 'cases':cases,
            'max_error':max(max(c['trace_preservation_error'],c['observable_error']) for c in cases),
            'scope':'Constructive twirl identities only; no optimization, converse, or novelty certification.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--tolerance', type=float, default=1e-10)
    args = parser.parse_args()
    report = run(args.tolerance)
    text = json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    print(text,end='')


if __name__ == '__main__':
    main()
