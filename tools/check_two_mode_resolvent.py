#!/usr/bin/env python3
"""Small deterministic checks of the supplied two-mode resolvent reduction.

These constructions check identities and an exact example. They do not
certify the unresolved universal four-by-four head inequality by sampling.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
SQRT2 = np.sqrt(2)
TARGET = 4 + SQRT2
TAIL_CAP = np.sqrt(32 / 3)
TOLERANCE = 4e-10
SEED = 2026092604


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def kron(*matrices):
    result = np.array([[1]], dtype=complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def haar(rng, dimension):
    raw = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
        size=(dimension, dimension)
    )
    unitary, triangular = np.linalg.qr(raw)
    diagonal = np.diag(triangular)
    return unitary * (diagonal / np.abs(diagonal)).conj()


def memory_operator(rng, reflection):
    unitary = haar(rng, 4)
    if reflection:
        positive = int(rng.integers(0, 5))
        diagonal = np.array([1] * positive + [-1] * (4 - positive))
    else:
        diagonal = rng.uniform(-1, 1, size=4)
    return (unitary * diagonal) @ unitary.conj().T


def hamiltonian(readouts):
    b1, d1, b2, d2 = readouts
    return (
        kron(X, I2, b1) + kron(Z, I2, d1)
        + kron(I2, X, b2) + kron(I2, Z, d2)
    )


def partial_references(matrix):
    return np.einsum("rqrs->qs", matrix.reshape(4, 4, 4, 4))


def head_dual(isometry, memory_matrix):
    blocks = isometry.reshape(4, 4, 2)
    return np.einsum("rqa,qs,rsb->ab", blocks.conj(), memory_matrix, blocks)


def head_forward(isometry, head_matrix):
    blocks = isometry.reshape(4, 4, 2)
    return np.einsum("rqa,ab,rsb->qs", blocks, head_matrix, blocks.conj())


def head_choi(isometry):
    blocks = isometry.reshape(4, 4, 2)
    return np.einsum("rqa,rsb->aqbs", blocks, blocks.conj()).reshape(8, 8)


def insertion(isometry):
    """Map R3 x head to R1 x R2 x R3 x Q."""
    result = np.zeros((32, 4), dtype=complex)
    for reference in range(4):
        for last in range(2):
            result[(2 * reference + last) * 4:(2 * reference + last + 1) * 4,
                   last * 2:(last + 1) * 2] = isometry[reference * 4:(reference + 1) * 4]
    return result


def compressed_resolvent(isometry, weights, t, b, d):
    resolvent = np.linalg.inv(t * np.eye(8) - kron(X, b) - kron(Z, d))
    square_root = np.diag(np.sqrt(np.maximum(weights, 0)))
    compressed = np.zeros((4, 4), dtype=complex)
    for row in range(2):
        for column in range(2):
            memory_block = resolvent[row * 4:(row + 1) * 4,
                                      column * 4:(column + 1) * 4]
            compressed[row * 2:(row + 1) * 2,
                       column * 2:(column + 1) * 2] = (
                square_root @ head_dual(isometry, memory_block) @ square_root
            )
    return compressed, resolvent


def exact_scalar_checks():
    # kappa < 2+sqrt(2) reduces to 6sqrt(2)>7.
    require(72 > 49, "uniform tail gap integer comparison")
    # 2sqrt(3)>2+sqrt(2) follows from sqrt(2)<3/2.
    require(Fraction(2) < Fraction(9, 4), "rank-one obstruction comparison")
    # The physical example's t>3sqrt(2) reduces to 17>12sqrt(2).
    require(17**2 > 2 * 12**2, "example large-t comparison")
    require(3**2 < 4 * 3, "example head criterion strictly below one")
    require(Fraction(32, 3) > Fraction(13, 4)**2,
            "fixed kappa is larger than the failing rational baseline")
    require(2 * 12**2 < 23**2, "fixed baseline negative secular numerator")
    c, s = Fraction(39999, 40001), Fraction(400, 40001)
    require(c*c + s*s == 1, "exact NPT example angle")
    require(c > Fraction(999, 1000) and Fraction(61, 25)**2 < 6,
            "NPT example energy lower estimates")
    require(7 + 2 * Fraction(61, 25) * Fraction(999, 1000)
            > Fraction(86, 25)**2 and Fraction(36, 25)**2 > 2,
            "NPT example high two-mode energy")
    return {
        "uniform_tail_gap_integer_witness": "72 > 49",
        "rank_one_obstruction_integer_witness": "8 < 9",
        "example_large_t_integer_witness": "289 > 288",
        "example_strict_head_bound_integer_witness": "9 < 12",
        "fixed_kappa_comparison_integer_witness": "512 > 507",
        "fixed_baseline_negative_secular_integer_witness": "288 < 529",
        "npt_example_rational_angle": "39999^2 + 400^2 = 40001^2",
        "npt_example_energy_chain": "U > 86/25 > 2+sqrt(2)",
    }


def general_checks(rng):
    xa, za = kron(X, I2), kron(Z, I2)
    xb, zb = kron(I2, X), kron(I2, Z)
    readout_cases = [
        (np.zeros((4, 4)),) * 4,
        (I4,) * 4,
        (xa, za, xb, zb),
    ]
    for index in range(25):
        readout_cases.append(tuple(
            memory_operator(rng, reflection=index % 2 == 0) for _ in range(4)
        ))

    gamma = kron(Y, Y, I4)
    y_basis = np.array([[1, 1j], [1j, 1]], dtype=complex) / SQRT2
    y_change = kron(y_basis, I4)
    maxima = {
        "chiral_residual": 0.0,
        "trace_moment_residual": 0.0,
        "partial_trace_moment_residual": 0.0,
        "head_unital_residual": 0.0,
        "head_choi_trace_residual": 0.0,
        "schur_compression_residual": 0.0,
        "reflection_block_resolvent_residual": 0.0,
    }
    minimum_tail_gap = 10.0
    maximum_third_eigenvalue = 0.0
    minimum_channel_moment_gap = 10.0
    schur_inertia_comparisons = 0
    reflection_block_checks = 0
    convexity_checks = 0

    for index, readouts in enumerate(readout_cases):
        h0 = hamiltonian(readouts)
        square = h0 @ h0
        trace_sum = sum(operator @ operator for operator in readouts)
        expected_trace = 4 * np.trace(trace_sum).real
        maxima["trace_moment_residual"] = max(
            maxima["trace_moment_residual"], abs(np.trace(square).real - expected_trace)
        )
        partial_square = partial_references(square)
        maxima["partial_trace_moment_residual"] = max(
            maxima["partial_trace_moment_residual"],
            np.linalg.norm(partial_square - 4 * trace_sum)
        )
        require(expected_trace <= 64 + TOLERANCE, "second moment bound")
        maxima["chiral_residual"] = max(
            maxima["chiral_residual"], np.linalg.norm(gamma @ h0 @ gamma + h0)
        )
        values, vectors = np.linalg.eigh(h0)
        top, second, tail = values[-1], values[-2], values[-3]
        require(tail >= -TOLERANCE and tail <= TAIL_CAP + TOLERANCE,
                "third eigenvalue bound")
        maximum_third_eigenvalue = max(maximum_third_eigenvalue, float(tail))
        isometry = vectors[:, [-1, -2]]
        weights = np.array([top - tail, second - tail])
        envelope = tail * np.eye(16) + (isometry * weights) @ isometry.conj().T
        require(np.linalg.eigvalsh(envelope - h0)[0] >= -TOLERANCE,
                "two-mode spectral majorant")
        t = TARGET - tail
        minimum_tail_gap = min(minimum_tail_gap, float(t - 2))
        require(t > 2, "uniformly positive last-query inverse")

        maxima["head_unital_residual"] = max(
            maxima["head_unital_residual"], np.linalg.norm(head_dual(isometry, I4) - I2)
        )
        choi = head_choi(isometry)
        require(np.linalg.eigvalsh(choi)[0] >= -TOLERANCE, "positive head Choi matrix")
        choi_trace = np.einsum("aqbq->ab", choi.reshape(2, 4, 2, 4))
        maxima["head_choi_trace_residual"] = max(
            maxima["head_choi_trace_residual"], np.linalg.norm(choi_trace - I2)
        )
        channel_moment = head_forward(isometry, np.diag([top**2, second**2]))
        channel_gap = np.linalg.eigvalsh(8 * I4 - channel_moment)[0]
        minimum_channel_moment_gap = min(minimum_channel_moment_gap, float(channel_gap))
        require(channel_gap >= -TOLERANCE, "actual channel matrix moment")

        b = memory_operator(rng, reflection=True)
        d = memory_operator(rng, reflection=index % 2 == 0)
        small, resolvent = compressed_resolvent(isometry, weights, t, b, d)
        inserted = insertion(isometry)
        weighted = inserted @ kron(I2, np.diag(np.sqrt(np.maximum(weights, 0))))
        direct = weighted.conj().T @ kron(I4, resolvent) @ weighted
        maxima["schur_compression_residual"] = max(
            maxima["schur_compression_residual"], np.linalg.norm(small - direct)
        )
        base = kron(I4, t * np.eye(8) - kron(X, b) - kron(Z, d))
        # Scaling the positive update checks both positive and negative
        # Schur outcomes, without asserting universal success at scale one.
        for scale in (0.5, 1.0, 2.0, 4.0):
            full_values = np.linalg.eigvalsh(base - scale * weighted @ weighted.conj().T)
            small_values = np.linalg.eigvalsh(np.eye(4) - scale * small)
            full_negative = int(np.count_nonzero(full_values < -TOLERANCE))
            small_negative = int(np.count_nonzero(small_values < -TOLERANCE))
            require(full_negative == small_negative, "Schur inertia equality")
            schur_inertia_comparisons += 1

        if index % 2 == 0:
            transition = b + 1j * d
            first = np.linalg.inv(t * t * I4 - transition @ transition.conj().T)
            second_inverse = np.linalg.inv(t * t * I4 - transition.conj().T @ transition)
            block = np.block([
                [t * first, transition @ second_inverse],
                [transition.conj().T @ first, t * second_inverse],
            ])
            maxima["reflection_block_resolvent_residual"] = max(
                maxima["reflection_block_resolvent_residual"],
                np.linalg.norm(y_change.conj().T @ resolvent @ y_change - block)
            )
            require(np.linalg.norm(transition @ transition.conj().T
                                   - (2 * I4 - 1j * (b @ d - d @ b))) < TOLERANCE,
                    "reflection commutator identity")
            reflection_block_checks += 1

        if index < 8:
            b_other = memory_operator(rng, reflection=True)
            proportion = Fraction(2, 5)
            mixture = float(proportion) * b + float(1 - proportion) * b_other
            k_first = compressed_resolvent(isometry, weights, t, b, d)[0]
            k_second = compressed_resolvent(isometry, weights, t, b_other, d)[0]
            k_mixture = compressed_resolvent(isometry, weights, t, mixture, d)[0]
            gap = float(proportion) * k_first + float(1 - proportion) * k_second - k_mixture
            require(np.linalg.eigvalsh(gap)[0] >= -TOLERANCE,
                    "operator convexity in the final readout")
            convexity_checks += 1

    require(max(maxima.values()) < TOLERANCE, "construction residual tolerance")
    return {
        "earlier_pair_constructions": len(readout_cases),
        "schur_inertia_comparisons": schur_inertia_comparisons,
        "reflection_block_checks": reflection_block_checks,
        "operator_convexity_checks": convexity_checks,
        "maximum_third_eigenvalue_observed": maximum_third_eigenvalue,
        "minimum_resolvent_gap_observed": minimum_tail_gap,
        "minimum_channel_moment_gap": minimum_channel_moment_gap,
        "maximum_residuals": maxima,
    }


def exact_example_checks():
    xa, za = kron(X, I2), kron(Z, I2)
    xb, zb = kron(I2, X), kron(I2, Z)
    cross = kron(Z, X)
    a = 2 / np.sqrt(3)
    b = np.sqrt(2 / 3)
    physical = ((a * za + b * xa) / SQRT2, (a * za - b * xa) / SQRT2,
                (a * zb + b * cross) / SQRT2, (a * zb - b * cross) / SQRT2)
    for operator in physical:
        require(np.linalg.norm(operator @ operator - I4) < TOLERANCE,
                "example physical readout is a reflection")
        require(np.count_nonzero(np.linalg.eigvalsh(operator) > 0) == 2,
                "example reflection is balanced")
    h0 = (a * kron(Z, I2, za) + b * kron(X, I2, xa)
          + a * kron(I2, Z, zb) + b * kron(I2, X, cross))
    expected = np.array([-2 * np.sqrt(3)] * 2 + [-a] * 6 + [a] * 6
                        + [2 * np.sqrt(3)] * 2)
    spectrum_residual = np.linalg.norm(np.linalg.eigvalsh(h0) - expected)
    require(spectrum_residual < TOLERANCE, "full physical example spectrum")
    require(np.linalg.norm(np.linalg.eigvalsh(hamiltonian(physical)) - expected)
            < TOLERANCE, "trusted-frame spectrum agrees")

    plus = np.array([1, 1], dtype=complex) / SQRT2
    rotation = np.cos(np.pi / 8) * I4 + 1j * np.sin(np.pi / 8) * kron(Y, X)
    encoded = rotation @ np.kron(plus[:, None], I2)
    copying = np.zeros((16, 4), dtype=complex)
    for index in range(4):
        copying[5 * index, index] = 1
    isometry = copying @ encoded
    top = 2 * np.sqrt(3)
    require(np.linalg.norm(h0 @ isometry - top * isometry) < TOLERANCE,
            "explicit isometry spans the leading eigenspace")
    require(np.linalg.norm(isometry.conj().T @ isometry - I2) < TOLERANCE,
            "explicit head isometry")
    effects = [
        (I2 + ((-1)**first * X + (-1)**second * Z) / SQRT2) / 4
        for first in range(2) for second in range(2)
    ]
    require(np.linalg.norm(sum(effects) - I2) < TOLERANCE, "head POVM normalization")
    channel_residual = 0.0
    for first in range(2):
        for second in range(2):
            matrix = np.zeros((2, 2), dtype=complex)
            matrix[first, second] = 1
            expected_output = np.diag([np.trace(effect @ matrix) for effect in effects])
            channel_residual = max(channel_residual,
                                   np.linalg.norm(head_forward(isometry, matrix) - expected_output))
    require(channel_residual < TOLERANCE, "full head channel including cross terms")
    for sign in (1, -1):
        y_vector = np.array([1, sign * 1j]) / SQRT2
        marginal = head_forward(isometry, np.outer(y_vector, y_vector.conj()))
        require(np.linalg.norm(marginal - I4 / 4) < TOLERANCE,
                "flat diagonal marginals in the head Y basis")

    weight = 4 / np.sqrt(3)
    t = TARGET - a
    compressed, _ = compressed_resolvent(isometry, np.array([weight, weight]), t, za, zb)
    formula = weight * (t * np.eye(4) + (kron(X, X) + kron(Z, Z)) / SQRT2) / (t*t - 2)
    require(np.linalg.norm(compressed - formula) < TOLERANCE,
            "coherent head resolvent formula")
    head_y = kron(I2, Y)
    dephased = (compressed + head_y @ compressed @ head_y) / 2
    coherent_norm = float(np.linalg.eigvalsh(compressed)[-1])
    dephased_norm = float(np.linalg.eigvalsh(dephased)[-1])
    exact_value = 2 / (2 * np.sqrt(3) - 1)
    require(abs(coherent_norm - exact_value) < TOLERANCE,
            "example attaining last pair")
    require(abs(dephased_norm - weight*t/(t*t - 2)) < TOLERANCE,
            "dephased head resolvent")
    require(coherent_norm > dephased_norm and exact_value < 1,
            "strict coherence loss and successful example cap")
    difference = np.linalg.eigvalsh(compressed - dephased)
    require(difference[0] < -TOLERANCE and difference[-1] > TOLERANCE,
            "dephasing has no one-sided operator order")
    return {
        "top_eigenvalue": float(top),
        "top_multiplicity": 2,
        "third_eigenvalue": float(a),
        "spectrum_residual": float(spectrum_residual),
        "full_channel_residual": float(channel_residual),
        "rank_one_baseline_above_safe_threshold": bool(top > TARGET - 2),
        "resolvent_parameter_above_three_sqrt_two": bool(t > 3 * SQRT2),
        "coherent_head_norm": coherent_norm,
        "dephased_head_norm": dephased_norm,
        "all_third_pair_head_supremum_exact": "2/(2sqrt(3)-1) < 1",
    }


def fixed_tail_warning_checks():
    xa, za = kron(X, I2), kron(Z, I2)
    xb, zb = kron(I2, X), kron(I2, Z)
    h0 = hamiltonian((xa, za, xb, zb))
    values, vectors = np.linalg.eigh(h0)
    isometry = vectors[:, [-1, -2]]
    require(abs(values[-1] - 4) < TOLERANCE
            and abs(values[-2] - 2) < TOLERANCE
            and abs(values[-3] - 2) < TOLERANCE,
            "retention head eigenvalues")
    test_values = []
    for baseline in (13 / 4, TAIL_CAP):
        t = TARGET - baseline
        require(t > 2, "fixed tail diagnostic retains positive inverse")
        weights = np.array([4 - baseline, 0])
        compressed, _ = compressed_resolvent(isometry, weights, t, xa, za)
        actual = float(np.linalg.eigvalsh(compressed)[-1])
        formula = (4 - baseline) * (t*t - 2) / (t * (t*t - 4))
        require(abs(actual - formula) < TOLERANCE and actual > 1,
                "fixed baseline envelope fails the exact head test")
        test_values.append(actual)
    t = TARGET - 13 / 4
    weight = 3 / 4
    secular = t**3 - weight*t*t - 4*t + 2*weight
    require(abs(secular - SQRT2 * (12*SQRT2 - 23) / 16) < TOLERANCE,
            "fixed baseline secular identity")
    physical = (
        kron(X, I2, I2, xa) + kron(Z, I2, I2, za)
        + kron(I2, X, I2, xb) + kron(I2, Z, I2, zb)
        + kron(I2, I2, X, xa) + kron(I2, I2, Z, za)
    )
    physical_norm = float(np.max(np.abs(np.linalg.eigvalsh(physical))))
    require(abs(physical_norm - (2 + 2*SQRT2)) < TOLERANCE,
            "actual Hamiltonian remains below the target")
    return {
        "test_value_at_baseline_13_over_4": test_values[0],
        "test_value_at_fixed_kappa": test_values[1],
        "actual_three_query_norm": physical_norm,
        "scope": "failure of the fixed-baseline positive-head envelope, not the physical bound",
    }


def nonclassical_head_checks():
    a, b = np.sqrt(3 / 2), 1 / SQRT2
    c, s = 39999 / 40001, 400 / 40001
    h0 = (
        a * kron(Z, I2, Z, I2) + b * kron(X, I2, X, I2)
        + c * kron(I2, Z, I2, Z) + s * kron(I2, Z, Y, Y)
        + c * kron(I2, X, Z, X) - s * kron(I2, X, X, I2)
    )
    pair_b = c * kron(I2, Z) + s * kron(Y, Y)
    pair_d = c * kron(Z, X) - s * kron(X, I2)
    require(np.linalg.norm(pair_b @ pair_b - I4) < TOLERANCE
            and np.linalg.norm(pair_d @ pair_d - I4) < TOLERANCE
            and np.linalg.norm(pair_b @ pair_d + pair_d @ pair_b) < TOLERANCE,
            "NPT construction has an actual sharp second pair")
    top = np.sqrt(7 + 4*a*c)
    lower = np.sqrt(7 - 4*a*c)
    expected = np.array([-top] * 2 + [-lower] * 2 + [-1] * 4
                        + [1] * 4 + [lower] * 2 + [top] * 2)
    values, vectors = np.linalg.eigh(h0)
    spectrum_residual = float(np.linalg.norm(values - expected))
    require(spectrum_residual < TOLERANCE, "NPT example exact spectrum")
    isometry = vectors[:, [-1, -2]]
    normalized_choi = head_choi(isometry) / 2
    partial_transpose = normalized_choi.reshape(2, 4, 2, 4).transpose(2, 1, 0, 3).reshape(8, 8)
    epsilon = b*s / (top*top - 1)
    expected_ppt = np.sort(np.array([-epsilon] * 2 + [epsilon] * 2 + [1/4] * 4))
    actual_ppt = np.linalg.eigvalsh(partial_transpose)
    ppt_residual = float(np.linalg.norm(actual_ppt - expected_ppt))
    require(ppt_residual < TOLERANCE and actual_ppt[0] < -TOLERANCE,
            "actual high-energy channel has the stated negative partial transpose")
    require(np.linalg.norm(head_forward(isometry, I2) - I4/2) < TOLERANCE,
            "NPT head channel has the stated maximally mixed aggregate")
    exact_negative_display = -100*SQRT2 / (120003 + 39999*np.sqrt(6))
    require(abs(actual_ppt[0] - exact_negative_display) < TOLERANCE,
            "NPT exact negative eigenvalue formula")
    return {
        "top_eigenvalue": float(top),
        "top_multiplicity": 2,
        "spectrum_residual": spectrum_residual,
        "normalized_choi_partial_transpose_residual": ppt_residual,
        "minimum_partial_transpose_eigenvalue": float(actual_ppt[0]),
        "exact_negative_eigenvalue": "-100sqrt(2)/(120003+39999sqrt(6))",
        "scope": "actual two-mode channel is not entanglement breaking; no physical violation claimed",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    rng = np.random.default_rng(SEED)
    report = {
        "status": "all construction checks passed; universal head inequality unresolved",
        "seed": SEED,
        "tolerance": TOLERANCE,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "exact_scalar_comparisons": exact_scalar_checks(),
        "general_constructions": general_checks(rng),
        "physical_degenerate_head_example": exact_example_checks(),
        "fixed_tail_warning": fixed_tail_warning_checks(),
        "nonclassical_head_example": nonclassical_head_checks(),
        "maximum_matrix_dimension": 32,
        "uniform_resolvent_gap_display": float(2 + SQRT2 - TAIL_CAP),
    }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        if arguments.output.resolve() == Path(__file__).resolve():
            raise ValueError("The output must not overwrite the verifier source")
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
