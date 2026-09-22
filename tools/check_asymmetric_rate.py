#!/usr/bin/env python3
"""Finite deterministic checks for the asymmetric entropy/rate deductions.

Fixed seeds and complete small translation instruments are used. There is no
random search, optimizer, numerical rank inference, or large-block simulation.
Roundoff at known probability/positive-semidefinite endpoints is checked
against 1e-12 before adjustment, and every adjustment is reported explicitly.

    python tools/check_asymmetric_rate.py --output results/asymmetric_rate.json
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np

from check_entropy_geometry import (Diagnostic, HADAMARD, I, X, Y, Z,
                                    local, tensor, trace_norm)

BASE = "9697d4d72cc34c52f4680fbf0c588b39af5c0471"
ROUNDOFF_BOUND = 1e-12


class RateDiagnostic(Diagnostic):
    def __init__(self, label, tolerance):
        super().__init__(label, tolerance)
        self.roundoff = []

    def probability(self, value, label):
        value = float(value)
        self.require(math.isfinite(value), f"nonfinite probability: {label}")
        self.require(-ROUNDOFF_BOUND <= value <= 1 + ROUNDOFF_BOUND,
                     f"probability outside checked roundoff range: {label}")
        if value < 0 or value > 1:
            adjusted = 0.0 if value < 0 else 1.0
            self.roundoff.append(dict(quantity=label, original=value,
                                      adjusted=adjusted))
            return adjusted
        return value

    def finish(self):
        self.data.update(roundoff_bound=ROUNDOFF_BOUND,
                         endpoint_adjustments=self.roundoff)
        return super().finish()


def entropy(probabilities):
    return math.fsum(-float(p) * math.log2(float(p))
                     for p in probabilities if p > 0)


def h(p):
    if not 0 <= p <= 1:
        raise ValueError("Binary entropy requires a probability in [0,1].")
    return entropy((p, 1 - p))


def f(c):
    if not 0 <= c <= 1:
        raise ValueError("The contrast must lie in [0,1].")
    # This equivalent form avoids subtractive cancellation near c=0.
    alpha = c * c / (2 * (1 + math.sqrt(1 - c * c)))
    return h(alpha)


def spectral_entropy(matrix, test, label):
    test.equal(matrix, matrix.conj().T)
    raw = np.linalg.eigvalsh(matrix)
    values = [test.probability(v, f"{label}_eigenvalue_{i}")
              for i, v in enumerate(raw)]
    # This is an entropy of a subnormalized positive operator. No renormalizing
    # or numerical rank decision is made after a bounded endpoint adjustment.
    return entropy(values)


def fixed_complex_basis(n):
    dimension = 2 ** n
    indices = np.arange(dimension)
    unitary = np.exp(2j * math.pi * np.outer(indices, indices) / dimension)
    unitary /= math.sqrt(dimension)
    for site in range(n):
        pauli = local(n, site, X if site % 2 else Y)
        angle = .17 + .06 * site
        unitary = (math.cos(angle) * np.eye(dimension)
                   + 1j * math.sin(angle) * pauli) @ unitary
        phase = .11 + .03 * site
        unitary = (math.cos(phase) * np.eye(dimension)
                   + 1j * math.sin(phase) * local(n, site, Z)) @ unitary
    if n >= 2:
        pauli = tensor([Z, Y] + [I] * (n - 2))
        unitary = (math.cos(.31) * np.eye(dimension)
                   + 1j * math.sin(.31) * pauli) @ unitary
    return unitary


def check_seed(label, n, supplied_spectrum, seed_x, tolerance, equality=False):
    """seed_x columns are the seed amplitudes in the product-X input basis."""
    test = RateDiagnostic(label, tolerance)
    spectrum = np.asarray(supplied_spectrum, float)
    test.require(bool(np.all(spectrum > 0)), "supply only positive eigenvalues")
    test.equal(spectrum.sum(), 1)
    test.require(seed_x.shape == (len(spectrum), 2 ** n), "seed shape mismatch")
    test.equal(seed_x @ seed_x.conj().T, np.diag(spectrum))
    seed_entropy = entropy(spectrum)
    p = np.sum(np.abs(seed_x) ** 2, axis=0)
    test.equal(p.sum(), 1)
    classical_entropy = entropy(p)
    quantum_conditional_sum = 0.0
    fano_sum = 0.0
    classical_conditional_sum = 0.0
    lower_classical_sum = 0.0
    lower_quantum_sum = 0.0
    records = []
    for site in range(n):
        mask = 1 << (n - 1 - site)
        fx = test.probability(trace_norm(seed_x @ local(n, site, Z)
                                         @ seed_x.conj().T), f"F_X_{site}")
        fz = test.probability(trace_norm(seed_x @ local(n, site, X)
                                         @ seed_x.conj().T), f"F_Z_{site}")
        groups = [[v for v in range(2 ** n) if bool(v & mask) == bool(bit)]
                  for bit in (0, 1)]
        sigma = [seed_x[:, vertices] @ seed_x[:, vertices].conj().T
                 for vertices in groups]
        test.equal(trace_norm(sigma[0] - sigma[1]), fx)
        quantum_conditional = sum(spectral_entropy(s, test, f"sigma_{site}_{bit}")
                                  for bit, s in enumerate(sigma)) - seed_entropy
        helstrom_error = (1 - fx) / 2
        fano = h(helstrom_error)
        classical_conditional = 0.0
        ci = 0.0
        for vertex in groups[0]:
            a, b = p[vertex], p[vertex ^ mask]
            mass = float(a + b)
            if mass == 0:
                continue
            conditional = test.probability(a / mass, f"conditional_{site}_{vertex}")
            pair_contrast = test.probability(2 * math.sqrt(a * b) / mass,
                                             f"pair_contrast_{site}_{vertex}")
            test.equal(h(conditional), f(pair_contrast))
            classical_conditional += mass * h(conditional)
            ci += 2 * math.sqrt(a * b)
        ci = test.probability(ci, f"classical_flip_{site}")
        test.le(0, quantum_conditional)
        test.le(quantum_conditional, fano)
        test.le(fz, ci)
        test.le(f(fz), f(ci))
        test.le(f(ci), classical_conditional)
        quantum_conditional_sum += quantum_conditional
        fano_sum += fano
        classical_conditional_sum += classical_conditional
        lower_classical_sum += f(ci)
        lower_quantum_sum += f(fz)
        records.append(dict(site=site, F_X=fx, F_Z=fz, classical_flip_overlap=ci,
                            helstrom_error=helstrom_error,
                            conditional_entropy_X_i_given_Q=quantum_conditional,
                            fano_entropy=fano,
                            conditional_entropy_X_i_given_rest=classical_conditional,
                            f_classical_flip=f(ci), f_F_Z=f(fz)))
    test.le(seed_entropy, classical_entropy)
    test.le(classical_entropy - seed_entropy, quantum_conditional_sum)
    test.le(quantum_conditional_sum, fano_sum)
    test.le(classical_conditional_sum, classical_entropy)
    test.le(lower_classical_sum, classical_conditional_sum)
    test.le(lower_quantum_sum - fano_sum, seed_entropy)
    test.le(seed_entropy, math.log2(len(spectrum)))
    if equality:
        test.equal(lower_quantum_sum - fano_sum, seed_entropy)
    test.data.update(matrix_dimension=2 ** n, input_qubits=n,
                     supplied_rank=len(spectrum), supplied_spectrum=spectrum.tolist(),
                     column_probabilities=p.tolist(), seed_entropy_bits=seed_entropy,
                     classical_column_entropy_bits=classical_entropy,
                     full_conditional_entropy_given_Q=classical_entropy - seed_entropy,
                     sum_single_bit_quantum_conditional_entropies=quantum_conditional_sum,
                     sum_fano_entropies=fano_sum,
                     sum_classical_conditional_entropies=classical_conditional_sum,
                     sum_f_classical_flip=lower_classical_sum,
                     asymmetric_entropy_lower_bound=lower_quantum_sum - fano_sum,
                     entropy_equality_asserted=equality,
                     sites=records,
                     scope="Fixed normalized complex seed; full entropy, Helstrom/Fano, conditional-entropy, and flip-overlap chains.")
    return test.finish()


def binomial_cdf(n, threshold, alpha):
    return math.fsum(math.comb(n, k) * alpha ** k * (1 - alpha) ** (n - k)
                     for k in range(min(n, threshold) + 1))


def check_truncated_instrument(n, alpha, cutoff, tolerance):
    test = RateDiagnostic(f"n{n}_bernoulli_cutoff_{cutoff}_complete_instrument", tolerance)
    dimension = 2 ** n
    support = [v for v in range(dimension) if v.bit_count() <= cutoff]
    output_dimension = len(support)
    mass = binomial_cdf(n, cutoff, alpha)
    mass = test.probability(mass, "retained_Bernoulli_mass")
    probabilities = np.array([alpha ** v.bit_count() * (1 - alpha) ** (n - v.bit_count())
                              / mass for v in support])
    test.equal(probabilities.sum(), 1)
    seed_x = np.zeros((output_dimension, dimension), complex)
    for row, (vertex, p) in enumerate(zip(support, probabilities)):
        seed_x[row, vertex] = math.sqrt(p)
    seed = seed_x @ tensor([HADAMARD] * n)
    contrast_formula = (2 * math.sqrt(alpha * (1 - alpha))
                        * binomial_cdf(n - 1, cutoff - 1, alpha) / mass)
    x_decoders = []
    z_decoders = []
    for site in range(n):
        mask = 1 << (n - 1 - site)
        x_decoders.append(np.diag([(-1) ** bool(v & mask) for v in support]))
        matching = np.array([[int(a ^ b == mask) for b in support] for a in support], complex)
        z_decoders.append(matching)
        test.le(float(np.linalg.norm(matching, 2)), 1)
        test.equal(np.sqrt(probabilities) @ matching @ np.sqrt(probabilities), contrast_formula)
    tp = np.zeros((dimension, dimension), complex)
    effective_x = [np.zeros_like(tp) for _ in range(n)]
    effective_z = [np.zeros_like(tp) for _ in range(n)]
    kraus_weights = []
    for translation in range(dimension):
        phase = tensor(Z if translation & (1 << (n - 1 - site)) else I
                       for site in range(n))
        kraus = seed @ phase
        adjoint = kraus.conj().T
        tp += adjoint @ kraus
        kraus_weights.append(float(np.vdot(kraus, kraus).real / dimension))
        for site in range(n):
            sign = (-1) ** bool(translation & (1 << (n - 1 - site)))
            decoder_x = sign * x_decoders[site]
            test.equal(decoder_x @ kraus, kraus @ local(n, site, X))
            effective_x[site] += adjoint @ decoder_x @ kraus
            effective_z[site] += adjoint @ z_decoders[site] @ kraus
    test.equal(tp, np.eye(dimension))
    test.equal(sum(kraus_weights), 1)
    for site in range(n):
        test.equal(effective_x[site], local(n, site, X))
        test.equal(effective_z[site], contrast_formula * local(n, site, Z))
    test.le(n * f(contrast_formula), entropy(probabilities))
    test.le(entropy(probabilities), math.log2(output_dimension))
    original_probabilities = np.array([alpha ** v.bit_count() * (1 - alpha) ** (n - v.bit_count())
                                       for v in range(dimension)])
    test.equal(original_probabilities.sum(), 1)
    original_vector = np.sqrt(original_probabilities)
    truncated_vector = np.zeros(dimension)
    truncated_vector[support] = np.sqrt(probabilities)
    tail_probability = 1 - mass
    pure_state_distance = trace_norm(np.outer(original_vector, original_vector)
                                    - np.outer(truncated_vector, truncated_vector))
    test.equal(pure_state_distance, 2 * math.sqrt(tail_probability))
    test.le(abs(contrast_formula - 2 * math.sqrt(alpha * (1 - alpha))),
            pure_state_distance)
    support_certificate = None
    if cutoff / n <= .5:
        support_log_bound = n * h(cutoff / n)
        hoeffding_tail_bound = math.exp(-2 * n * (cutoff / n - alpha) ** 2)
        test.require(cutoff / n >= alpha, "upper-tail threshold below the mean")
        test.le(math.log2(output_dimension), support_log_bound)
        test.le(tail_probability, hoeffding_tail_bound)
        support_certificate = dict(log2_support_upper_bound=support_log_bound,
                                   hoeffding_tail_upper_bound=hoeffding_tail_bound)
    test.data.update(matrix_dimension=dimension, input_qubits=n, alpha=alpha,
                     hamming_weight_cutoff=cutoff, support=support,
                     support_probability_mass=mass, normalized_probabilities=probabilities.tolist(),
                     branch_count=dimension, maximum_quantum_output_dimension=output_dimension,
                     qubit_cap=math.ceil(math.log2(output_dimension)),
                     x_contrast=1.0, z_contrast=contrast_formula,
                     normalized_kraus_weights=kraus_weights,
                     seed_entropy_bits=entropy(probabilities),
                     log_support_per_input=math.log2(output_dimension) / n,
                     exact_axis_rate_curve_at_achieved_contrast=f(contrast_formula),
                     discarded_probability=tail_probability,
                     original_product_contrast=2 * math.sqrt(alpha * (1 - alpha)),
                     original_to_truncated_pure_state_trace_norm=pure_state_distance,
                     truncation_contrast_loss_bound=2 * math.sqrt(tail_probability),
                     finite_support_certificate=support_certificate,
                     scope="Complete finite translation instrument and all local operator identities; no asymptotic rate attainment claim for this block.")
    return test.finish()


def check_curve(tolerance):
    test = RateDiagnostic("exact_axis_curve_and_strict_interior_rate_gap", tolerance)
    table = []
    for z in (0.0, .1, .25, .5, .75, .9, 1.0):
        alpha = (1 - math.sqrt(1 - z * z)) / 2
        test.equal(2 * math.sqrt(alpha * (1 - alpha)), z)
        test.equal(f(z), h(alpha))
        test.le(f(z), z)
        table.append(dict(z_contrast=z, bernoulli_parameter=alpha,
                          exact_axis_rate=f(z), original_site_retention_rate=z))
    derivatives = []
    step = 1e-4
    derivative_tolerance = 2e-6
    for z in (.125, .25, .5, .75, .875):
        s = math.sqrt(1 - z * z)
        first = z * math.atanh(s) / (s * math.log(2))
        second = (math.atanh(s) - s) / (s ** 3 * math.log(2))
        finite_first = (f(z + step) - f(z - step)) / (2 * step)
        finite_second = (f(z + step) - 2 * f(z) + f(z - step)) / step ** 2
        test.le(abs(finite_first - first), derivative_tolerance)
        test.le(abs(finite_second - second), derivative_tolerance)
        test.require(first > 0 and second > 0, "interior monotonicity/convexity failed")
        derivatives.append(dict(z=z, first_derivative=first, second_derivative=second,
                                centered_difference_first=finite_first,
                                centered_difference_second=finite_second,
                                first_difference_error=abs(finite_first - first),
                                second_difference_error=abs(finite_second - second)))
    x, z = .99, .5
    retention_rate = x + z - 1 - math.sqrt(2 * (1 - x) * (1 - z))
    lower_bound = f(z) - h((1 - x) / 2)
    test.equal(retention_rate, .39)
    test.require(lower_bound < f(z) < retention_rate,
                 "strict interior scalar rate ordering failed")
    x_critical = f(z) + math.sqrt((1 - z) * (1 + z - 2 * f(z)))
    cost_at_critical = x_critical + z - 1 - math.sqrt(2 * (1 - x_critical) * (1 - z))
    test.equal(cost_at_critical, f(z))
    test.require(x > x_critical, "interior X contrast is not beyond the certified threshold")
    test.data.update(matrix_dimension=1, exact_axis_rate_table=table,
                     derivative_step=step, derivative_absolute_tolerance=derivative_tolerance,
                     derivative_checks=derivatives,
                     interior_x=x, interior_z=z,
                     asymmetric_entropic_lower_bound=lower_bound,
                     inherited_exact_axis_achievable_rate=f(z),
                     original_site_retention_rate=retention_rate,
                     interior_separation_x_threshold=x_critical,
                     strict_rate_gap=retention_rate - f(z),
                     scope="Scalar identities and finite-difference diagnostics; these do not prove asymptotic coding or the general derivative formulas.")
    return test.finish()


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("Tolerance must be finite and positive.")
    cases = []
    supplied = [(1, [1]), (1, [.7, .3]), (2, [1]), (2, [.7, .3]),
                (2, [.4, .3, .2, .1]), (3, [.65, .35]),
                (3, [.4, .3, .2, .1]), (4, [.4, .3, .2, .1]),
                (4, [k / 136 for k in range(16, 0, -1)])]
    for n, spectrum in supplied:
        unitary = fixed_complex_basis(n)
        if np.max(abs(unitary.conj().T @ unitary - np.eye(2 ** n))) > tolerance:
            raise RuntimeError("The explicitly constructed basis is not unitary.")
        seed_x = np.sqrt(spectrum)[:, None] * unitary.conj().T[:len(spectrum)]
        cases.append(check_seed(f"n{n}_fixed_complex_rank_{len(spectrum)}", n,
                                spectrum, seed_x, tolerance))
    n = 3
    bisector = np.array([math.cos(math.pi / 8), math.sin(math.pi / 8)])
    seed_x = tensor([bisector] * n) @ tensor([HADAMARD] * n)
    cases.append(check_seed("n3_pure_product_bisector_equality", n, [1], seed_x, tolerance, equality=True))
    alpha = .2
    probabilities = np.array([alpha ** v.bit_count() * (1 - alpha) ** (n - v.bit_count())
                              for v in range(2 ** n)])
    cases.append(check_seed("n3_full_rank_exact_axis_product_equality", n,
                            probabilities, np.diag(np.sqrt(probabilities)), tolerance, equality=True))
    probabilities = np.full(4, .25)
    cases.append(check_seed("n2_maximally_mixed_endpoint", 2, probabilities,
                            np.diag(np.sqrt(probabilities)), tolerance, equality=True))
    cases.extend(check_truncated_instrument(*parameters, tolerance)
                 for parameters in ((2, .15, 1), (3, .2, 1), (4, .25, 2), (3, .2, 3)))
    cases.append(check_curve(tolerance))
    if len(cases) != 17:
        raise RuntimeError("The documented diagnostic case count changed.")
    return dict(status="PASS", research_base=BASE, python=platform.python_version(),
                numpy=np.__version__, tolerance=tolerance, case_count=len(cases),
                maximum_matrix_dimension=max(case["matrix_dimension"] for case in cases),
                max_identity_error=max(case["max_identity_error"] for case in cases),
                max_inequality_violation=max(case["max_inequality_violation"] for case in cases),
                endpoint_roundoff_bound=ROUNDOFF_BOUND,
                endpoint_adjustment_count=sum(len(case["endpoint_adjustments"]) for case in cases),
                cases=cases,
                scope="Finite deterministic seed inequalities, four complete small instruments, and scalar curve diagnostics. No search, optimizer, inferred rank, large-block simulation, proof certification, or novelty certification. Every endpoint roundoff adjustment is bounded and listed.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tolerance", type=float, default=1e-10)
    args = parser.parse_args()
    report = run(args.tolerance)
    text = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
