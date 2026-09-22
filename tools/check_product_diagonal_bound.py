#!/usr/bin/env python3
"""Small matrix diagnostics for docs/COMMUTING_SEED_BOUND.md.

Compare full-matrix trace norms with the exact edge formula for ten
product-diagonal states, including correlated spectra, zero probabilities,
and local axes with Y components. No optimization is performed. These checks
verify formulas at finite examples, not the unrestricted conjecture or novelty.

Run from the repository root:
    python tools/check_product_diagonal_bound.py --output results/product_diagonal_bound.json
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


def tensor(items):
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


def entropy(probabilities):
    positive = np.asarray(probabilities)[np.asarray(probabilities) > 0]
    return float(-np.dot(positive, np.log2(positive)))


def axes(n, mode):
    directions = ([[1., 0., 1.]] * n if mode == 'bisector'
                  else [[1., 1., 1.], [1., 2., -.5], [.2, -.7, 1.]][:n])
    directions = np.asarray(directions)
    return directions / np.linalg.norm(directions, axis=1, keepdims=True)


def check_case(label, probabilities, mode, tolerance):
    p = np.asarray(probabilities, dtype=float)
    p /= p.sum()
    n = int(round(math.log2(len(p))))
    if len(p) != 2**n or np.min(p) < 0:
        raise ValueError('Expected a nonnegative spectrum on n qubits.')
    directions = axes(n, mode)
    rotations = []
    for direction in directions:
        _, vectors = np.linalg.eigh(sum(a*b for a, b in zip(direction, (X, Y, Z))))
        rotations.append(vectors[:, ::-1])  # label 0 is the +1 eigenstate
    u = tensor(rotations)
    sqrt_rho = (u*np.sqrt(p)) @ u.conj().T
    rho = sqrt_rho @ sqrt_rho
    matrix_scores, edge_scores, bisector_scores = [], [], []
    conditional_entropies, conditional_entropy_residuals = [], []
    for i in range(n):
        edges = np.moveaxis(p.reshape((2,)*n), i, 0).reshape(2, -1)
        left, right = edges
        weight = left+right
        mask = weight > 0
        conditional_entropy = sum(
            float(w)*entropy(np.array([a, b])/w)
            for a, b, w in zip(left[mask], right[mask], weight[mask]))
        conditional_entropies.append(conditional_entropy)
        conditional_entropy_residuals.append(
            abs(conditional_entropy-(entropy(p)-entropy(weight))))
        bisector_scores.append(float(math.sqrt(2)*np.sqrt(weight**2+4*left*right).sum()))
        for pauli, coordinate in ((X, 0), (Z, 2)):
            global_pauli = tensor(pauli if j == i else I for j in range(n))
            matrix = sqrt_rho @ global_pauli @ sqrt_rho
            matrix_scores.append(float(np.abs(np.linalg.eigvalsh(matrix)).sum()))
            a = directions[i, coordinate]
            edge_scores.append(float(np.sqrt(4*left*right+(left-right)**2*a*a).sum()))
    matrix_entropy = entropy(np.maximum(np.linalg.eigvalsh(rho), 0))
    h = entropy(p)
    score = sum(matrix_scores)
    entropy_bound = math.sqrt(2)*n+(2-math.sqrt(2))*h
    rank = int(np.count_nonzero(p))
    rank_bound = math.sqrt(2)*n+(2-math.sqrt(2))*math.log2(rank)
    formula_error = max(abs(a-b) for a, b in zip(matrix_scores, edge_scores))
    normalization_error = abs(float(np.trace(rho).real)-1)
    entropy_error = abs(matrix_entropy-h)
    residual = max(formula_error, normalization_error, entropy_error,
                   *conditional_entropy_residuals)
    if residual > tolerance:
        raise AssertionError(f'{label}: a matrix or entropy identity failed.')
    if score > sum(bisector_scores)+tolerance:
        raise AssertionError(f'{label}: local-basis upper bound failed.')
    if sum(conditional_entropies) > h+tolerance:
        raise AssertionError(f'{label}: classical entropy-chain bound failed.')
    if score > entropy_bound+tolerance or score > rank_bound+tolerance:
        raise AssertionError(f'{label}: product-diagonal bound failed.')
    for i, conditional_entropy in enumerate(conditional_entropies):
        if bisector_scores[i] > math.sqrt(2)+(2-math.sqrt(2))*conditional_entropy+tolerance:
            raise AssertionError(f'{label}: conditional single-bit bound failed.')
    if mode == 'bisector' and abs(score-sum(bisector_scores)) > tolerance:
        raise AssertionError(f'{label}: bisector edge equality failed.')
    return {'label':label, 'n':n, 'basis':mode, 'axes':directions.tolist(),
            'probabilities':p.tolist(), 'rank':rank,
            'matrix_pauli_scores':matrix_scores, 'edge_pauli_scores':edge_scores,
            'score':score, 'bisector_score_upper_bound':sum(bisector_scores),
            'entropy':h, 'conditional_entropies':conditional_entropies,
            'entropy_bound':entropy_bound, 'rank_bound':rank_bound,
            'max_formula_error':formula_error, 'max_identity_error':residual}


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Tolerance must be finite and positive.')
    specifications = [
        ('n2_pure_bisector', [1, 0, 0, 0], 'bisector'),
        ('n2_subset_bisector', [1, 1, 0, 0], 'bisector'),
        ('n2_correlated_bisector', [1, 2, 3, 7], 'bisector'),
        ('n2_sparse_correlated_complex_basis', [7, 0, 0, 13], 'general'),
        ('n2_correlated_complex_basis', [1, 2, 3, 7], 'general'),
        ('n3_subset_bisector', [1, 1, 1, 1, 0, 0, 0, 0], 'bisector'),
        ('n3_correlated_bisector', [1, 3, 2, 7, 9, 4, 5, 11], 'bisector'),
        ('n3_sparse_correlated_bisector', [2, 0, 0, 5, 0, 3, 7, 0], 'bisector'),
        ('n3_correlated_complex_basis', [1, 3, 2, 7, 9, 4, 5, 11], 'general'),
        ('n3_sparse_correlated_complex_basis', [2, 0, 0, 5, 0, 3, 7, 0], 'general'),
    ]
    cases = [check_case(*specification, tolerance) for specification in specifications]
    return {'status':'PASS', 'python':platform.python_version(),
            'numpy':np.__version__, 'tolerance':tolerance, 'case_count':len(cases),
            'max_identity_error':max(case['max_identity_error'] for case in cases),
            'cases':cases,
            'scope':'Ten finite matrix diagnostics. No optimization, unrestricted bound, or novelty certification.'}


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
