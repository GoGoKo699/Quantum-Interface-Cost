#!/usr/bin/env python3
"""Deterministic matrix checks for the Q1 delayed local-readout benchmark.

These verify an explicit construction at small sizes. They are not an
optimization, a proof of lower bounds, or a novelty check.
Dependency: numpy. Run: python checks.py --max-n 4 --output checks.json
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from pathlib import Path
from typing import Iterable

import numpy as np
from numpy.typing import NDArray

Matrix = NDArray[np.complex128]
I: Matrix = np.eye(2, dtype=complex)
X: Matrix = np.array([[0, 1], [1, 0]], dtype=complex)
Z: Matrix = np.diag([1, -1]).astype(complex)
ETA0 = 1 / math.sqrt(2)
SIGNS = tuple(itertools.product((-1, 1), repeat=2))


def kron_all(matrices: Iterable[Matrix]) -> Matrix:
    result = np.ones((1, 1), dtype=complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def local_pauli(n: int, site: int, basis: int) -> Matrix:
    return kron_all((X if basis == 0 else Z) if k == site else I
                    for k in range(n))


def permutation_matrix(n: int, order: tuple[int, ...]) -> Matrix:
    """Map computational basis from original order to the requested order."""
    result = np.zeros((2**n, 2**n), dtype=complex)
    for old in range(2**n):
        bits = tuple((old >> (n - 1 - k)) & 1 for k in range(n))
        new = 0
        for k in order:
            new = 2 * new + bits[k]
        result[new, old] = 1
    return result


def binary_entropy(p: float) -> float:
    if not 0 <= p <= 1:
        raise ValueError('Probability must be in [0,1].')
    if p in (0, 1):
        return 0.0
    return -p * math.log2(p) - (1-p) * math.log2(1-p)


def run_checks(max_n: int, tolerance: float) -> dict:
    parents = {(a, b): (I + ETA0 * (a*X + b*Z)) / 4 for a, b in SIGNS}
    rows: dict[tuple[int, int], Matrix] = {}
    rank_one_error = 0.0
    for label, effect in parents.items():
        eigenvalues, eigenvectors = np.linalg.eigh(effect)
        row = math.sqrt(max(0.0, float(eigenvalues[-1]))) * eigenvectors[:, -1].conj()[None, :]
        rows[label] = row
        rank_one_error = max(rank_one_error, float(np.max(np.abs(row.conj().T @ row - effect))))
    parent_errors = {
        'normalization': float(np.max(np.abs(sum(parents.values()) - I))),
        'x_marginal': float(np.max(np.abs(sum(a*g for (a,b),g in parents.items()) - ETA0*X))),
        'z_marginal': float(np.max(np.abs(sum(b*g for (a,b),g in parents.items()) - ETA0*Z))),
        'x_estimator_mean': float(np.max(np.abs(sum(math.sqrt(2)*a*g for (a,b),g in parents.items()) - X))),
        'z_estimator_mean': float(np.max(np.abs(sum(math.sqrt(2)*b*g for (a,b),g in parents.items()) - Z))),
        'estimator_second_moment': float(np.max(np.abs(sum(2*g for g in parents.values()) - 2*I))),
        'rank_one_factorization': rank_one_error,
    }
    minimum_eigenvalue = min(float(np.min(np.linalg.eigvalsh(g))) for g in parents.values())
    results = []
    for n in range(1, max_n + 1):
        targets = {(i,b): local_pauli(n,i,b) for i in range(n) for b in (0,1)}
        for q in range(n + 1):
            identity_q = np.eye(2**q, dtype=complex)
            completeness = np.zeros((2**n, 2**n), dtype=complex)
            effective = {j: np.zeros_like(p) for j,p in targets.items()}
            branches = 0
            for kept in itertools.combinations(range(n), q):
                discarded = tuple(k for k in range(n) if k not in kept)
                perm = permutation_matrix(n, kept + discarded)
                kept_observables = {(i,b): local_pauli(q, kept.index(i), b)
                                    for i in kept for b in (0,1)}
                for labels in itertools.product(SIGNS, repeat=n-q):
                    row = kron_all(rows[label] for label in labels)
                    kraus = (np.kron(identity_q, row) @ perm) / math.sqrt(math.comb(n,q))
                    adjoint = kraus.conj().T
                    completeness += adjoint @ kraus
                    for i,b in targets:
                        if i in kept:
                            decoder = kept_observables[i,b]
                        else:
                            decoder = labels[discarded.index(i)][b] * identity_q
                        effective[i,b] += adjoint @ decoder @ kraus
                    branches += 1
            eta = ETA0 + (q/n)*(1-ETA0)
            normalization_error = float(np.max(np.abs(completeness - np.eye(2**n))))
            observable_error = max(float(np.max(np.abs(effective[j]-eta*p))) for j,p in targets.items())
            results.append({'n':n, 'q':q, 'kraus_branches':branches, 'eta':eta,
                            'normalization_max_abs_error':normalization_error,
                            'observable_max_abs_error':observable_error})
    table = []
    for epsilon in (0.0, 0.01, 0.05, 0.10, 0.14, (1-ETA0)/2):
        eta = 1-2*epsilon
        sq = max(0.0, eta-ETA0)**2/(16*math.log(2))
        entropic = max(0.0, 1-2*binary_entropy(epsilon))
        upper = max(0.0, (eta-ETA0)/(1-ETA0))
        table.append({'epsilon':epsilon, 'eta':eta, 'lower_rate':max(sq,entropic),
                      'entropy_lower_rate':entropic, 'squashed_lower_rate':sq,
                      'achievable_rate_upper':upper})
    errors = list(parent_errors.values())
    errors += [r[key] for r in results for key in ('normalization_max_abs_error', 'observable_max_abs_error')]
    passed = max(errors) < tolerance and minimum_eigenvalue >= -tolerance
    report = {'status':'PASS' if passed else 'FAIL', 'python':platform.python_version(),
              'numpy':np.__version__, 'max_n':max_n, 'tolerance':tolerance,
              'max_matrix_entry_error':max(errors),
              'parent_min_eigenvalue':minimum_eigenvalue,
              'parent_errors':parent_errors, 'cases':results, 'rate_table':table,
              'scope':'Checks an explicit construction and estimator identities only; not optimality or novelty.'}
    if not passed:
        raise AssertionError(json.dumps(report, indent=2))
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n', type=int, default=4, choices=range(1,5))
    parser.add_argument('--tolerance', type=float, default=1e-10)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.tolerance <= 0:
        parser.error('--tolerance must be positive.')
    report = run_checks(args.max_n, args.tolerance)
    text = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text+'\n', encoding='utf-8')
    print(text)


if __name__ == '__main__':
    main()
