#!/usr/bin/env python3
"""Small deterministic diagnostics for allocation and spectral converses.

No optimizer, random search, numerical rank inference, or eigenvalue clipping
is used. Supplied orthonormal eigenbases define all state square roots.

    python tools/check_allocation_and_kernels.py --output results/allocation_and_kernels.json
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np

BASE = '358d887058eb9fa2fe8bb899d0261ec811d42fa6'
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = (I, X, Y, Z)
SQRT2 = math.sqrt(2)
C = 2 - SQRT2
BETA = np.array([math.cos(math.pi / 8), math.sin(math.pi / 8)], complex)


def tensor(items):
    out = np.ones((1, 1), complex)
    for item in items:
        out = np.kron(out, item)
    return out


def queries(n, axes=(X, Z)):
    return [tensor(p if j == i else I for j in range(n))
            for i in range(n) for p in axes]


def entropy(p):
    return math.fsum(-float(x) * math.log2(float(x)) for x in p if x > 0)


def trace_norm(a):
    return float(np.linalg.svd(a, compute_uv=False).sum())


def fourier(d):
    j = np.arange(d)
    return np.exp(2j * math.pi * np.outer(j, j) / d) / math.sqrt(d)


def rotate(p, theta):
    return math.cos(theta) * np.eye(len(p)) + 1j * math.sin(theta) * p


def generic_basis(n):
    if n == 2:
        return (rotate(np.kron(X, Y), .31) @ rotate(np.kron(Z, X), .23)
                @ rotate(np.kron(Y, I), .41) @ rotate(np.kron(I, Z), .17)
                @ fourier(4))
    d = 2 ** n
    v = np.array([complex(1 + j % 3, (-1) ** j * (j + 1) / 3)
                  for j in range(d)])
    return basis_from_vector(v)


def basis_from_vector(v):
    v = np.asarray(v, complex).reshape(-1)
    v /= np.linalg.norm(v)
    # All vectors supplied below have a nonzero last component.
    return np.linalg.qr(np.column_stack((v, np.eye(len(v))[:, :-1])))[0]


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


def spectral_state(u, p, test):
    p = np.asarray(p, float)
    test.require(bool(np.all(p >= 0)), 'supplied spectrum must be nonnegative')
    test.equal(u.conj().T @ u, np.eye(len(p)))
    test.equal(p.sum(), 1)
    rho = (u * p) @ u.conj().T
    root = (u * np.sqrt(p)) @ u.conj().T
    test.equal(root @ root, rho)
    test.data.update(matrix_dimension=len(rho), supplied_spectrum=p.tolist(),
                     rank=int(np.count_nonzero(p)), entropy=entropy(p))
    return rho, root


def score(root):
    q = queries(int(round(math.log2(len(root)))))
    values = [trace_norm(root @ p @ root) for p in q]
    return math.fsum(values), values


def allocation_cost(x, z):
    return max(0.0, x + z - 1 - math.sqrt(2 * (1 - x) * (1 - z)))


def check_instrument(tolerance):
    test = Diagnostic('n3_complete_anisotropic_allocation_instrument', tolerance)
    probabilities = np.array([.5, .3, .2])
    classical = np.array([[.6, .8], [.8, .6], [1 / SQRT2, 1 / SQRT2]])
    targets = probabilities[:, None] + (1 - probabilities[:, None]) * classical
    costs = [allocation_cost(*pair) for pair in targets]
    test.equal(costs, probabilities)
    test.equal(sum(costs), 1)
    tp = np.zeros((8, 8), complex)
    effective = [np.zeros((8, 8), complex) for _ in range(6)]
    records = []
    max_output_dimension = 0
    for keep in range(3):
        discarded = [i for i in range(3) if i != keep]
        for raw in itertools.product((-1, 1), repeat=4):
            signs = {i: raw[2 * j:2 * j + 2] for j, i in enumerate(discarded)}
            bras = {}
            for i in discarded:
                s, t = signs[i]
                cx, cz = classical[i]
                theta = math.atan2(s * cx, t * cz)
                v = np.array([math.cos(theta / 2), math.sin(theta / 2)])
                bras[i] = v / SQRT2
                parent = (I + s * cx * X + t * cz * Z) / 4
                test.equal(np.outer(bras[i], bras[i]), parent)
                test.equal(np.linalg.eigvalsh(parent), [0, .5])
            kraus = np.zeros((2, 8), complex)
            for column in range(8):
                bits = [(column >> (2 - i)) & 1 for i in range(3)]
                kraus[bits[keep], column] = math.sqrt(probabilities[keep]) * math.prod(
                    bras[i][bits[i]] for i in discarded)
            max_output_dimension = max(max_output_dimension, kraus.shape[0])
            tp += kraus.conj().T @ kraus
            for i in range(3):
                for b, pauli in enumerate((X, Z)):
                    decoder = pauli if i == keep else signs[i][b] * I
                    effective[2 * i + b] += kraus.conj().T @ decoder @ kraus
            records.append(dict(retained_site=keep,
                                discarded_signs={str(i): list(signs[i]) for i in discarded},
                                normalized_kraus_weight=float(np.linalg.norm(kraus, 'fro') ** 2 / 8)))
    test.equal(tp, np.eye(8))
    for j, p in enumerate(queries(3)):
        test.equal(effective[j], targets.reshape(-1)[j] * p)
    test.equal(sum(record['normalized_kraus_weight'] for record in records), 1)
    test.require(max_output_dimension == 2 and len(records) == 48,
                 'every branch must retain at most one qubit')
    test.data.update(matrix_dimension=8, branch_count=len(records),
                     maximum_quantum_output_dimension=max_output_dimension,
                     retention_probabilities=probabilities.tolist(),
                     discarded_contrasts=classical.tolist(), target_contrasts=targets.tolist(),
                     exact_allocation_costs=costs, classical_records=records)
    return test.finish()


def check_weighted_attainer(tolerance):
    test = Diagnostic('n3_unequal_query_weight_attainer', tolerance)
    weights = np.array([[3, .2], [1.3, 1.1], [.4, 2]])
    radii = np.linalg.norm(weights, axis=1)
    increments = weights.sum(axis=1) - radii
    keep = int(np.argmax(increments))
    test.require(keep == 1, 'the maximum increment, not maximum raw weight, selects the site')
    target = weights / radii[:, None]
    target[keep] = 1
    factors = []
    for i in range(3):
        if i == keep:
            factors.append(I / SQRT2)
        else:
            theta = math.atan2(target[i, 0], target[i, 1])
            factors.append(np.array([[math.cos(theta / 2), math.sin(theta / 2)]]))
    seed = tensor(factors)
    test.equal(np.linalg.norm(seed, 'fro'), 1)
    values = np.array([trace_norm(seed @ p @ seed.conj().T) for p in queries(3)])
    optimum = float(radii.sum() + increments.max())
    actual = float(weights.reshape(-1) @ values)
    test.equal(values, target.reshape(-1))
    test.equal(actual, optimum)
    test.equal(sum(allocation_cost(*pair) for pair in target), 1)
    test.data.update(matrix_dimension=8, quantum_output_dimension=2,
                     weights=weights.tolist(), increments=increments.tolist(), retained_site=keep,
                     contrasts=target.tolist(), weighted_score=actual, exact_optimum=optimum)
    return test.finish()


def sld_comparison(u, p, test):
    p = np.asarray(p, float)
    denominator = p[:, None] + p[None, :]
    kernel = np.divide((p[:, None] - p[None, :]) ** 2, 2 * denominator,
                       out=np.zeros_like(denominator), where=denominator > 0)
    harmonic = np.divide(p[:, None] * p[None, :], denominator,
                         out=np.zeros_like(denominator), where=denominator > 0)
    n = int(round(math.log2(len(p))))
    values = [float(np.sum(kernel * abs(u.conj().T @ a @ u) ** 2))
              for a in queries(n, (X, Y, Z))]
    site_remainders = [values[3 * i] + values[3 * i + 2] - values[3 * i + 1]
                       for i in range(n)]
    for value in site_remainders:
        test.le(0, value)
    remainder = sum(site_remainders) / 2
    # Independent finite evaluation of the positive Laplace/Fourier remainder:
    # ∫ f_w(t)^2 dt = d^(-2) Σ_ab λa λb/(λa+λb) <a|w|a><b|w|b>.
    integral_remainder = 0.0
    for word in itertools.product(range(4), repeat=n):
        y_count = word.count(2)
        if y_count:
            a = tensor(PAULIS[j] for j in word)
            diagonal = np.diag(u.conj().T @ a @ u).real
            integral_remainder += 4 * y_count / len(p) * float(diagonal @ harmonic @ diagonal)
    test.equal(remainder, integral_remainder)
    test.data['sld'] = dict(local_xyz_values=values, site_triangle_remainders=site_remainders,
                            xz_minus_half_xyz=remainder,
                            laplace_fourier_remainder=integral_remainder)


def triplet_basis():
    return np.column_stack(([1, 0, 0, 0], [0, 0, 0, 1],
                            np.array([0, 1, 1, 0]) / SQRT2,
                            np.array([0, 1, -1, 0]) / SQRT2)).astype(complex)


def check_kernel(kind, tolerance):
    test = Diagnostic('n2_rank_three_kernel_' + kind, tolerance)
    if kind in ('generic_complex', 'universal_spectrum'):
        u = generic_basis(2)
        p = [.65, .25, .1, 0] if kind == 'generic_complex' else [.5, .25, .25, 0]
    else:
        u = triplet_basis()
        p = [.55, .3, .15, 0]
        if kind == 'rotated_bell':
            u = np.kron(rotate(Y, .23) @ rotate(Z, .19), rotate(X, .37)) @ u
            p = [.7, .2, .1, 0]
    rho, root = spectral_state(u, p, test)
    support, v = u[:, :3], u[:, 3]
    lam = np.array(p[:3])
    adjugate = (support * (np.prod(lam) / lam)) @ support.conj().T
    tv = np.zeros((4, 4), complex)
    details, q_values, f_values, m_values = [], [], [], []
    for pauli in queries(2):
        signed_m = float(np.vdot(v, pauli @ v).real)
        m = abs(signed_m)
        chosen = pauli if signed_m >= 0 else -pauli
        q = float((2 * np.trace(rho @ pauli @ rho @ pauli)
                   - np.trace(rho @ pauli) ** 2).real)
        f = trace_norm(root @ pauli @ root)
        compressed = support.conj().T @ chosen @ support
        test.equal(np.linalg.eigvalsh(compressed), [-1, -m, 1])
        signed = np.linalg.eigvalsh(support.conj().T @ root @ chosen @ root @ support)
        a, b, small = float(signed[2]), -float(signed[0]), -float(signed[1])
        test.le(0, small)
        test.equal(a * b * small, np.prod(lam) * m)
        test.equal(f * f, q + 4 * b * small)
        test.le(lam[-1], a)
        test.le(f * f, q + 4 * lam[0] * lam[1] * m)
        plus = (np.eye(4) + chosen) / 2
        ev = plus @ v
        intersection = plus - np.outer(ev, ev.conj()) / ((1 + m) / 2)
        test.equal(intersection @ intersection, intersection)
        test.equal(np.trace(intersection), 1)
        test.equal(intersection @ v, 0)
        adjugate_charge = m * float(np.trace(adjugate @ intersection).real)
        test.le(b * small, adjugate_charge)
        tv += m * intersection
        q_values.append(q)
        f_values.append(f)
        m_values.append(m)
        details.append(dict(kernel_expectation=signed_m, inertia_values=[a, -b, -small],
                            q=q, fidelity=f, same_sign_product=b * small,
                            adjugate_charge=adjugate_charge))
    correlations = np.array([[np.trace(rho @ np.kron(a, b)).real
                              for b in (X, Y, Z)] for a in (X, Y, Z)])
    chi = float(correlations[0, 1] ** 2 + correlations[2, 1] ** 2
                + correlations[1, 0] ** 2 + correlations[1, 2] ** 2
                + 2 * correlations[1, 1] ** 2)
    test.equal(sum(q_values), 2 - chi)
    m_total = sum(m_values)
    test.equal(np.trace(tv), m_total)
    t_values = np.linalg.eigvalsh(support.conj().T @ tv @ support)[::-1]
    test.le(0, float(t_values[-1]))
    direct = float(np.trace(adjugate @ tv).real)
    rearranged = float(np.array([lam[0] * lam[1], lam[0] * lam[2], lam[1] * lam[2]]) @ t_values)
    scalar = lam[0] * lam[1] * m_total
    test.le(direct, rearranged)
    test.le(rearranged, scalar)
    actual = sum(f_values)
    direct_bound = 8 - 4 * chi + 16 * direct
    test.le(actual ** 2, direct_bound)
    line = 2 * SQRT2 + C * entropy(p)
    scalar_certificate = 8 + 16 * scalar <= line ** 2
    refined_certificate = 8 + 16 * rearranged <= line ** 2
    if scalar_certificate or refined_certificate:
        test.le(actual, line)
    marginal_norms = [float(np.linalg.norm([np.trace(rho @ a).real
                                           for a in queries(2, (X, Y, Z))[3 * i:3 * i + 3]]))
                      for i in range(2)]
    if kind in ('singlet', 'rotated_bell'):
        test.equal(m_total, 0)
        test.le(actual, 2 * SQRT2)
        test.require(max(marginal_norms) > .1, 'the example must not have both marginals maximally mixed')
    if kind == 'universal_spectrum':
        test.require(scalar_certificate, 'the stated spectrum must have a valid uniform certificate')
        test.le(actual, math.sqrt(8 + 4 * SQRT2))
    sld_comparison(u, p, test)
    test.data.update(score=actual, entropy_line=line, chi_y=chi, kernel_m=m_total,
                     marginal_bloch_lengths=marginal_norms, kernel_operator_eigenvalues=t_values.tolist(),
                     scalar_squared_bound=8 - 4 * chi + 16 * scalar,
                     adjugate_squared_bound=direct_bound,
                     rearranged_squared_bound=8 - 4 * chi + 16 * rearranged,
                     scalar_entropy_certificate=bool(scalar_certificate),
                     refined_entropy_certificate=bool(refined_certificate), query_details=details)
    return test.finish()


def check_one_outlier(n, t, attainer, tolerance):
    test = Diagnostic(f'n{n}_one_outlier_' + ('attainer' if attainer else 'complex_vector'), tolerance)
    d = 2 ** n
    u = basis_from_vector(tensor([BETA] * n).reshape(-1)) if attainer else generic_basis(n)
    b = (1 - t) / (d - 1)
    p = [t] + [b] * (d - 1)
    rho, root = spectral_state(u, p, test)
    v = u[:, 0]
    actual, values = score(root)
    means = [float(np.vdot(v, a @ v).real) for a in queries(n)]
    formulas = [(d - 2) * b + math.sqrt(4 * t * b + (t - b) ** 2 * m * m)
                for m in means]
    bound = 2 * n * ((d - 2) * b + math.sqrt(4 * t * b + (t - b) ** 2 / 2))
    test.equal(values, formulas)
    test.le(actual, bound)
    if attainer:
        test.equal(actual, bound)
    sld_comparison(u, p, test)
    test.data.update(outlier=t, background=b, query_means=means, query_scores=values,
                     exact_query_formulas=formulas, score=actual, exact_spectrum_optimum=bound)
    return test.finish()


def check_graph(tolerance):
    test = Diagnostic('d8_nonphysical_spectral_graph_relaxation', tolerance)
    w = np.full((8, 8), .25)
    np.fill_diagonal(w, 3)
    for i in range(8):
        w[i, i ^ 1] = 1.5
    p = np.array([.5, .5, 0, 0, 0, 0, 0, 0])
    denominator = p[:, None] + p[None, :]
    kernel = np.divide((p[:, None] - p[None, :]) ** 2, denominator,
                       out=np.zeros_like(denominator), where=denominator > 0)
    energy = float(np.sum(w * kernel) / 2)
    laplacian_spectrum = np.linalg.eigvalsh(6 * np.eye(8) - w)
    test.equal(w, w.T)
    test.equal(w.sum(axis=1), 6)
    test.equal(laplacian_spectrum, [0, 2, 2, 2, 4.5, 4.5, 4.5, 4.5])
    test.equal(energy, 1.5)
    deficit = 3 - entropy(p)
    test.equal(deficit, 2)
    test.require(deficit > energy, 'the generic graph relaxation must fail')
    test.data.update(matrix_dimension=8, graph_matrix=w.tolist(),
                     laplacian_eigenvalues=laplacian_spectrum.tolist(),
                     rational_energy=energy, entropy_deficit=deficit,
                     false_relaxation_gap=deficit - energy,
                     physical_state_counterexample=False,
                     nonphysical_reason='Saturated diagonal 3 forces product X/Z-plane eigenvectors and off-diagonal entries at most 1, whereas paired entries are 1.5.')
    return test.finish()


def check_entanglement_calibration(tolerance):
    test = Diagnostic('near_bell_false_linear_entanglement_charge', tolerance)
    eps = 1 / 1024
    v = np.array([1, 0, 0, 1], complex) / SQRT2
    # A Bell basis gives the supplied spectrum exactly, including degeneracy.
    u = np.column_stack((v, np.array([1, 0, 0, -1]) / SQRT2,
                         np.array([0, 1, 1, 0]) / SQRT2,
                         np.array([0, 1, -1, 0]) / SQRT2))
    p = [1 - 3 * eps, eps, eps, eps]
    rho, _ = spectral_state(u, p, test)
    test.equal(rho, (1 - 4 * eps) * np.outer(v, v.conj()) + eps * np.eye(4))
    witness = float(np.trace(rho @ (np.kron(X, X) + np.kron(Z, Z))).real)
    test.equal(witness, 2 - 8 * eps)
    for local in queries(2, (X, Y, Z)):
        test.equal(np.trace(rho @ local), 0)
    upper = 1 - entropy(p) / 2
    false_charge = (witness - SQRT2) / C
    test.require(false_charge > upper, 'the proposed charge must exceed a valid entanglement upper bound')
    test.data.update(epsilon=eps, witness=witness, half_mutual_information=upper,
                     proposed_linear_charge=false_charge, obstruction_gap=false_charge - upper,
                     squashed_entanglement_evaluated=False)
    return test.finish()


def check_doublet(tolerance):
    test = Diagnostic('n2_doublet_spectrum_generic_and_attainer', tolerance)
    delta = .6
    p = [(1 + delta) / 4] * 2 + [(1 - delta) / 4] * 2
    bound = 2 + math.sqrt(4 - 2 * delta * delta)
    generic = generic_basis(2)
    beta_basis = np.column_stack((BETA, [-BETA[1], BETA[0]]))
    attainer = np.kron(beta_basis, I)
    values = []
    for label, u in [('generic', generic), ('attainer', attainer)]:
        _, root = spectral_state(u, p, test)
        actual, per_query = score(root)
        test.le(actual, bound)
        if label == 'attainer':
            test.equal(actual, bound)
        values.append(dict(kind=label, score=actual, query_scores=per_query))
    test.data.update(delta=delta, exact_spectrum_optimum=bound, states=values)
    return test.finish()


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Tolerance must be finite and positive.')
    cases = [check_instrument(tolerance), check_weighted_attainer(tolerance)]
    cases += [check_kernel(kind, tolerance)
              for kind in ('generic_complex', 'universal_spectrum', 'singlet', 'rotated_bell')]
    cases += [check_one_outlier(n, t, attainer, tolerance)
              for n, t, attainer in [(1, .81, False), (2, .03, False), (2, 0, True),
                                     (3, .91, False), (3, .67, True)]]
    cases += [check_graph(tolerance), check_entanglement_calibration(tolerance), check_doublet(tolerance)]
    return dict(status='PASS', research_base=BASE, python=platform.python_version(),
                numpy=np.__version__, tolerance=tolerance, case_count=len(cases),
                maximum_matrix_dimension=8,
                spectral_policy='Use supplied orthonormal eigenbases and all nonnegative eigenvalues directly; no eigenvalue clipping or inferred numerical rank.',
                max_identity_error=max(case['max_identity_error'] for case in cases),
                max_inequality_violation=max(case['max_inequality_violation'] for case in cases),
                cases=cases,
                scope='Finite deterministic checks of complete-instrument identities, exact spectral formulas, stated inequalities and explicit obstructions. No optimization, unrestricted theorem certificate, entanglement evaluation or novelty certification.')


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
