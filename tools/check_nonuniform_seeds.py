#!/usr/bin/env python3
"""Deterministic small-matrix diagnostics for nonuniform seed deductions.

No optimization or search is performed. Known spectral decompositions are
used directly: every supplied positive tail eigenvalue is retained, even
below machine epsilon. These examples do not prove unrestricted optimality,
the existential rank-two neighborhood, or publication novelty.

    python tools/check_nonuniform_seeds.py --output results/nonuniform_seeds.json
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np

BASE = '6ddc97a549316ed9edb7a14a110ceee70b87bdf9'
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
SQRT2 = math.sqrt(2)
C = 2 - SQRT2
BETA = np.array([math.cos(math.pi / 8), math.sin(math.pi / 8)])
ROT = np.column_stack((BETA, [-BETA[1], BETA[0]])).astype(complex)


def tensor(items):
    out = np.ones((1, 1), complex)
    for item in items:
        out = np.kron(out, item)
    return out


def queries(n):
    return [tensor(p if j == i else I for j in range(n))
            for i in range(n) for p in (X, Z)]


def h2(p):
    if p == 0 or p == 1:
        return 0.0
    return (-p * math.log(p) - (1 - p) * math.log1p(-p)) / math.log(2)


def entropy(p):
    return math.fsum(-float(x) * math.log2(float(x)) for x in p if x > 0)


def trace_norm(a):
    return float(np.linalg.svd(a, compute_uv=False).sum())


def fourier(d):
    j = np.arange(d)
    return np.exp(2j * math.pi * np.outer(j, j) / d) / math.sqrt(d)


class Diagnostic:
    def __init__(self, label, tolerance):
        self.data = {'label': label}
        self.tolerance = tolerance
        self.identities = []
        self.violations = []

    def equal(self, actual, expected):
        self.identities.append(float(np.max(np.abs(np.asarray(actual) - expected))))

    def le(self, actual, bound):
        self.violations.append(max(0.0, float(actual - bound)))

    def require(self, condition, message):
        if not condition:
            raise AssertionError(f"{self.data['label']}: {message}")

    def finish(self):
        self.data['max_identity_error'] = max(self.identities, default=0.0)
        self.data['max_inequality_violation'] = max(self.violations, default=0.0)
        self.require(max(self.data['max_identity_error'],
                         self.data['max_inequality_violation']) <= self.tolerance,
                     'a numerical residual exceeded the tolerance')
        return self.data


def spectral_state(basis, probabilities, diagnostic):
    """Use the supplied nonzero spectrum, without numerical rank truncation."""
    p = np.asarray(probabilities, float)
    diagnostic.require(bool(np.all(p > 0)), 'supplied spectrum must be positive')
    diagnostic.equal(basis.conj().T @ basis, np.eye(len(p)))
    diagnostic.equal(float(p.sum()), 1.0)
    rho = (basis * p) @ basis.conj().T
    root = (basis * np.sqrt(p)) @ basis.conj().T
    diagnostic.equal(root @ root, rho)
    diagnostic.equal(rho, rho.conj().T)
    diagnostic.data.update(n=int(round(math.log2(len(rho)))), rank=len(p),
                           supplied_positive_spectrum=p.tolist(),
                           entropy=entropy(p))
    return rho, root


def score(root):
    n = int(round(math.log2(len(root))))
    values = [trace_norm(root @ p @ root) for p in queries(n)]
    return math.fsum(values), values


def check_star(n, flat, tolerance):
    label = f'n{n}_star_' + ('flat' if flat else 'nonuniform_optimum')
    test = Diagnostic(label, tolerance)
    basis = tensor([ROT] * n)[:, [0] + [2 ** (n - 1 - j) for j in range(n)]]
    a = 1 / (n + 1) if flat else (3 / 7 if n == 2 else 1 - math.sqrt(6) / 4)
    b = (1 - a) / n
    _, root = spectral_state(basis, [a] + [b] * n, test)
    actual, values = score(root)
    formula = n * SQRT2 * (math.sqrt(a * a + 6 * a * b + b * b) + (n - 1) * b)
    optimum = 18 * SQRT2 / 7 if n == 2 else 3 * math.sqrt(3)
    flat_score = (8 + 2 * SQRT2) / 3 if n == 2 else 3 + 1.5 * SQRT2
    test.equal(actual, formula)
    test.equal(actual, flat_score if flat else optimum)
    test.require(optimum > flat_score, 'nonuniform score must exceed flat comparison')
    test.le(actual, SQRT2 * n + C * test.data['entropy'])
    if n == 3:
        test.le(actual, 4 + SQRT2)
        if not flat:
            test.equal(values, math.sqrt(3) / 2)
    test.data.update(score=actual, query_scores=values, exact_formula=formula,
                     support_optimum=optimum, flat_comparison=flat_score,
                     strict_nonuniform_gain=optimum - flat_score)
    return test.finish()


def check_coherent_star(tolerance):
    test = Diagnostic('n3_coherent_star_twirl', tolerance)
    support = tensor([ROT] * 3)[:, [0, 4, 2, 1]]
    eigenbasis = support @ fourier(4)
    rho, root = spectral_state(eigenbasis, [.55, .25, .15, .05], test)
    actual, _ = score(root)
    in_basis = support.conj().T @ rho @ support
    diagonal = np.diag(in_basis).real
    twirled = (support * diagonal) @ support.conj().T
    twirled_root = (support * np.sqrt(diagonal)) @ support.conj().T
    # Construct the local-B group average independently of diagonal extraction.
    average = np.zeros((8, 8), complex)
    bisector_pauli = (X + Z) / SQRT2
    for mask in range(8):
        u = tensor(bisector_pauli if mask & (1 << j) else I for j in range(3))
        average += u @ rho @ u.conj().T / 8
    test.equal(average, twirled)
    after, _ = score(twirled_root)
    test.le(actual, after)
    test.le(after, 3 * math.sqrt(3))
    test.require(np.max(abs(in_basis - np.diag(diagonal))) > .01,
                 'the starting state must have actual coherences')
    test.data.update(score=actual, score_after_local_bisector_twirl=after,
                     twirled_probabilities=diagonal.tolist(),
                     off_diagonal_max=float(np.max(abs(in_basis - np.diag(diagonal)))))
    return test.finish()


def inertia(basis, n, tolerance):
    spectra = [np.linalg.eigvalsh(basis.conj().T @ p @ basis) for p in queries(n)]
    indefinite = [bool(w[0] < -tolerance and w[-1] > tolerance) for w in spectra]
    active = sum(indefinite[2 * i] and indefinite[2 * i + 1] for i in range(n))
    return active, [w.tolist() for w in spectra]


def check_subset(flat, tolerance):
    test = Diagnostic('n3_subset_' + ('equality' if flat else 'nonuniform_strict'), tolerance)
    support = np.kron(np.eye(4), BETA[:, None])
    basis = support if flat else support @ fourier(4)
    p = [.25] * 4 if flat else [.5, .25, .15, .1]
    _, root = spectral_state(basis, p, test)
    actual, _ = score(root)
    active, spectra = inertia(support, 3, tolerance)
    bound = 3 * SQRT2 + C * active
    test.require(active == 2, 'subset support has exactly two active sites')
    test.le(actual, bound)
    if flat:
        test.equal(actual, 4 + SQRT2)
    else:
        test.require(bound - actual > 1e-3, 'nonflat spectrum must be strict')
    test.data.update(score=actual, active_sites=active, support_bound=bound,
                     subset_gap=4 + SQRT2 - actual, compression_spectra=spectra)
    return test.finish()


def check_radius(position, tolerance):
    theta = {'below': math.pi / 16, 'equal': math.pi / 8,
             'above': math.pi / 8 + .03}[position]
    test = Diagnostic(f'n2_support_radius_{position}', tolerance)
    beta = lambda t: np.array([math.cos(t), math.sin(t)])
    support = np.column_stack((np.kron([1, 0], beta(math.pi / 8 + theta)),
                               np.kron([0, 1], beta(math.pi / 8 - theta))))
    reference = np.kron(I, np.outer(BETA, BETA))
    projector = support @ support.conj().T
    distance = float(np.linalg.norm(projector - reference, ord=2))
    test.equal(distance, math.sin(theta))
    _, root = spectral_state(support @ fourier(2), [.73, .27], test)
    actual, _ = score(root)
    active, spectra = inertia(support, 2, tolerance)
    test.require(active == (2 if position == 'above' else 1), 'wrong active-site count')
    test.le(actual, 2 * SQRT2 + C * active)
    test.le(actual, 2 + SQRT2)  # Separate established rank-two theorem.
    xdiag = [math.sin(math.pi / 4 + 2 * theta), math.sin(math.pi / 4 - 2 * theta)]
    zdiag = [math.cos(math.pi / 4 + 2 * theta), math.cos(math.pi / 4 - 2 * theta)]
    test.equal(support.conj().T @ queries(2)[2] @ support, np.diag(xdiag))
    test.equal(support.conj().T @ queries(2)[3] @ support, np.diag(zdiag))
    test.data.update(theta=theta, distance=distance, radius=math.sin(math.pi / 8),
                     active_sites=active, compression_spectra=spectra, score=actual,
                     support_bound=2 * SQRT2 + C * active)
    return test.finish()


def check_block(tolerance):
    test = Diagnostic('complex_indefinite_block_trace_norm', tolerance)
    a = np.diag([.3, -.2]).astype(complex)
    b = np.array([[.03 + .02j, -.04j], [.01, -.02 + .01j]])
    c = np.array([[.1, .015j], [-.015j, -.04]])
    matrix = np.block([[a, b], [b.conj().T, c]])
    mu = .2
    actual = trace_norm(matrix)
    bound = trace_norm(a) + trace_norm(c) + 2 * np.linalg.norm(b, 'fro') ** 2 / mu
    test.equal(matrix, matrix.conj().T)
    test.le(actual, bound)
    test.data.update(matrix_dimension=4, trace_norm=actual, block_bound=float(bound),
                     compression_gap=mu, cross_block_hilbert_schmidt=float(np.linalg.norm(b, 'fro')))
    return test.finish()


def check_tail(rank, epsilon, tolerance, label):
    test = Diagnostic(label, tolerance)
    theta = .01
    rotation = math.cos(theta) * np.eye(4) + 1j * math.sin(theta) * np.kron(X, X)
    # The entangling unitary is applied in the local bisector coordinates.
    basis = tensor([ROT, ROT]) @ rotation
    support_indices = [0] if rank == 1 else [0, 2]
    sigma_basis = basis[:, support_indices]
    tau_basis = basis[:, [1]]
    sigma_p = np.ones(rank) / rank
    sigma_root = (sigma_basis * np.sqrt(sigma_p)) @ sigma_basis.conj().T
    tau_root = tau_basis @ tau_basis.conj().T
    full_basis = np.column_stack((sigma_basis, tau_basis))
    p = [(1 - epsilon) / rank] * rank + [epsilon]
    _, root = spectral_state(full_basis, p, test)
    sigma_score, _ = score(sigma_root)
    actual, _ = score(root)
    gaps = []
    block_violations = []
    for pauli in queries(2):
        compressed = sigma_basis.conj().T @ sigma_root @ pauli @ sigma_root @ sigma_basis
        mu = float(min(abs(np.linalg.eigvalsh(compressed))))
        gaps.append(mu)
        a = (1 - epsilon) * compressed
        b = math.sqrt(epsilon * (1 - epsilon)) * sigma_basis.conj().T @ sigma_root @ pauli @ tau_basis
        c = epsilon * tau_basis.conj().T @ pauli @ tau_basis
        matrix = np.block([[a, b], [b.conj().T, c]])
        bound = trace_norm(a) + trace_norm(c) + 2 * np.linalg.norm(b, 'fro') ** 2 / ((1 - epsilon) * mu)
        block_violations.append(max(0.0, trace_norm(matrix) - bound))
        test.le(trace_norm(matrix), bound)
        test.equal(trace_norm(matrix), trace_norm(root @ pauli @ root))
    k = math.fsum(1 + 2 / (rank * mu) for mu in gaps)
    score_bound = (1 - epsilon) * sigma_score + epsilon * k
    sigma_gap = 2 * SQRT2 + C * math.log2(rank) - sigma_score
    exact_entropy = h2(epsilon) + (1 - epsilon) * math.log2(rank)
    test.equal(test.data['entropy'], exact_entropy)
    entropy_gap = 2 * SQRT2 + C * exact_entropy - actual
    gap_bound = (1 - epsilon) * sigma_gap + C * h2(epsilon) - (k - 2 * SQRT2) * epsilon
    threshold = 2 ** (-(k - 2 * SQRT2) / C)
    test.require(epsilon < threshold, 'tail must meet the proved sufficient criterion')
    test.require(min(gaps) > .3 / rank, 'supported compression gaps must stay positive')
    test.le(actual, score_bound)
    test.le(gap_bound, entropy_gap)
    test.le(0.0, sigma_gap)
    test.le(0.0, entropy_gap)
    test.data.update(epsilon=epsilon, epsilon_below_machine_epsilon=bool(epsilon < np.finfo(float).eps),
                     retained_positive_tail=float(p[-1]), supplied_tail_rank=1,
                     supported_compression_gaps=gaps, K=k, sufficient_tail_threshold=threshold,
                     score=actual, score_bound=score_bound, sigma_score=sigma_score,
                     sigma_entropy_gap=sigma_gap, entropy_gap=entropy_gap,
                     entropy_gap_lower_bound=gap_bound, exact_orthogonal_mixture_entropy=exact_entropy,
                     maximum_block_inequality_violation=max(block_violations))
    return test.finish()


def sld(pure_basis, probabilities, pauli):
    # Complete the supplied orthonormal eigenbasis without altering eigenvalues.
    complete, _ = np.linalg.qr(pure_basis, mode='complete')
    lambdas = np.r_[probabilities, np.zeros(len(complete) - len(probabilities))]
    transformed = complete.conj().T @ pauli @ complete
    denominator = lambdas[:, None] + lambdas[None, :]
    ratio = np.divide((lambdas[:, None] - lambdas[None, :]) ** 2, denominator,
                      out=np.zeros_like(denominator), where=denominator > 0)
    return float(.5 * np.sum(ratio * abs(transformed) ** 2))


def check_sld(conditional, tolerance):
    label = 'sld_false_local_conditional_step' if conditional else 'sld_false_binary_pinching_step'
    test = Diagnostic(label, tolerance)
    vector = np.array([math.sqrt(.9), 0, 0, math.sqrt(.1)]) if conditional else np.sqrt([.9, .1])
    basis = vector[:, None].astype(complex)
    rho, _ = spectral_state(basis, [1.0], test)
    if conditional:
        values = [sld(basis, [1.0], p) for p in queries(2)]
        local = sum(values[:2])
        false_rhs = 1 + h2(.1)
        test.equal(values, [1, 9 / 25, 1, 9 / 25])
        test.equal(local, 34 / 25)
        test.le(2, sum(values))  # The actual global proposal is not refuted.
        test.data.update(local_sld_sum=local, false_conditional_rhs=false_rhs,
                         global_sld_sum=sum(values), global_entropy_deficit=2)
    else:
        local = sld(basis, [1.0], Z)
        pinched = (rho + Z @ rho @ Z) / 2
        false_rhs = h2(.1)
        test.equal(pinched, np.diag([.9, .1]))
        test.equal(local, 9 / 25)
        test.data.update(sld_information=local, pinching_entropy_gain=false_rhs)
    test.require(false_rhs - local > .1, 'the proposed local step must fail strictly')
    test.data['false_step_excess'] = false_rhs - local
    return test.finish()


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Tolerance must be finite and positive.')
    cases = [check_star(n, flat, tolerance) for n in (2, 3) for flat in (False, True)]
    cases += [check_coherent_star(tolerance)]
    cases += [check_subset(flat, tolerance) for flat in (True, False)]
    cases += [check_radius(position, tolerance) for position in ('below', 'equal', 'above')]
    cases += [check_block(tolerance)]
    cases += [check_tail(2, 1e-7, tolerance, 'n2_rank_two_rotated_support_tail'),
              check_tail(1, 1e-9, tolerance, 'n2_pure_rotated_support_tail'),
              check_tail(2, 2 ** -55, tolerance, 'n2_positive_tail_below_machine_epsilon')]
    cases += [check_sld(conditional, tolerance) for conditional in (True, False)]
    return dict(status='PASS', research_base=BASE, python=platform.python_version(),
                numpy=np.__version__, tolerance=tolerance, case_count=len(cases),
                maximum_matrix_dimension=8,
                spectral_policy='Use supplied orthonormal eigenvectors and every positive supplied eigenvalue; no spectral clipping or inferred numerical rank.',
                max_identity_error=max(case['max_identity_error'] for case in cases),
                max_inequality_violation=max(case['max_inequality_violation'] for case in cases),
                cases=cases,
                scope='Finite deterministic identity and inequality diagnostics. No optimization, search, unrestricted optimality certificate, quantitative value for the existential neighborhood, or novelty certification.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--tolerance', type=float, default=1e-10)
    args = parser.parse_args()
    report = run(args.tolerance)
    text = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
