#!/usr/bin/env python3
"""Verify one exact obstruction to the relaxed two-mode envelope test.

Strict signs and the resolvent numerator use exact rational arithmetic.
Small matrix checks diagnose the supplied construction, not the universal
physical converse or the all-support compression bounds proved in the note.
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
I16 = np.eye(16, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
TOLERANCE = 3e-11


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def kron(*matrices):
    result = np.array([[1]], dtype=complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def field(*coefficients):
    """Coefficients in the basis 1, sqrt(2), sqrt(3), sqrt(6)."""
    return tuple(Fraction(value) for value in coefficients)


def field_add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def field_scale(scalar, value):
    return tuple(Fraction(scalar) * coefficient for coefficient in value)


def field_multiply(left, right):
    result = [Fraction(0)] * 4
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            common = i & j
            rational = (2 if common & 1 else 1) * (3 if common & 2 else 1)
            result[i ^ j] += a * b * rational
    return tuple(result)


def exact_scalar_checks():
    one = field(1, 0, 0, 0)
    t = field(4, 1, Fraction(-2, 3), 0)
    g = field(0, 0, Fraction(4, 3), 0)
    square = field_multiply(t, t)
    # N = g[t^2 - 2 + 2q(t+1)] - t(t^2-4).
    numerator = field_add(
        field_multiply(g, field_add(
            field_add(square, field_scale(-2, one)),
            field_scale(Fraction(19, 10), field_add(t, one)),
        )),
        field_scale(-1, field_multiply(t, field_add(square, field_scale(-4, one)))),
    )
    require(field_scale(15, numerator) == field(-1716, -830, 1050, 438),
            "exact resolvent numerator in Q(sqrt(2),sqrt(3))")
    root3_lower = Fraction(1732, 1000)
    root6_lower = Fraction(2449, 1000)
    root2_upper = Fraction(1415, 1000)
    require(root3_lower**2 < 3 and root6_lower**2 < 6 and root2_upper**2 > 2,
            "exact rational radical enclosures")
    margin = 1050 * root3_lower + 438 * root6_lower - 830 * root2_upper - 1716
    require(margin == Fraction(812, 1000) and margin > 0,
            "strict positive resolvent numerator")
    require(16 < 24, "full rank-one compression cap")
    cap_gap = 2 * 1200**2 - 1681**2
    require(cap_gap == 54239 and cap_gap > 0, "full rank-two compression cap")
    require(19 < 25 and 1089 < 1200, "local-Pauli energy incompatibility")
    require(Fraction(1, 2) + Fraction(19, 40) == Fraction(39, 40),
            "pure-output top-two mass")
    return {
        "field_basis": ["1", "sqrt(2)", "sqrt(3)", "sqrt(6)"],
        "15_times_resolvent_numerator_coefficients": [-1716, -830, 1050, 438],
        "strict_lower_bound_for_15_times_numerator": str(margin),
        "radical_integer_witnesses": [
            "1732^2 = 2999824 < 3000000",
            "2449^2 = 5997601 < 6000000",
            "1415^2 = 2002225 > 2000000",
        ],
        "rank_two_cap_integer_gap": cap_gap,
        "physical_head_energy_witness": "14/5+sqrt(19)/10 < 33/10 < 2sqrt(3)",
        "strict_signs_use_floating_point": False,
    }


def partial_references(matrix):
    return np.einsum("rqrs->qs", matrix.reshape(4, 4, 4, 4))


def head_forward(isometry, head_matrix):
    blocks = isometry.reshape(4, 4, 2)
    return np.einsum("rqa,ab,rsb->qs", blocks, head_matrix, blocks.conj())


def head_dual(isometry, memory_matrix):
    blocks = isometry.reshape(4, 4, 2)
    return np.einsum("rqa,qs,rsb->ab", blocks.conj(), memory_matrix, blocks)


def trace_norm(matrix):
    return float(np.sum(np.linalg.svd(matrix, compute_uv=False)))


def construction_checks():
    p, q = 1 / 20, 19 / 20
    top, tail, gap = 2 * np.sqrt(3), 2 / np.sqrt(3), 4 / np.sqrt(3)
    target = 4 + np.sqrt(2)
    t = target - tail
    gamma = kron(Y, Y, I4)
    z1 = kron(Z, I2, I4)
    swap = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                     [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
    transform = np.sqrt(q) * I16 - 1j * np.sqrt(p) * kron(Y, I2, swap)
    original_isometry = np.zeros((16, 2), dtype=complex)
    # Tensor order R1,R2,F,L: R1=0, R2=F, and L carries the head.
    for head in range(2):
        for bell_bit in range(2):
            original_isometry[6 * bell_bit + head, head] = 1 / np.sqrt(2)
    isometry = transform @ original_isometry
    positive = isometry @ isometry.conj().T
    negative = gamma @ positive @ gamma
    involution = transform @ z1 @ transform.conj().T
    base = (3 * z1 + kron(I2, X, X, I2) + kron(I2, Z, Z, I2)
            - kron(Z, Y, Y, I2)) / np.sqrt(3)
    operator = transform @ base @ transform.conj().T
    residuals = {}

    def check(name, actual, expected):
        residual = float(np.linalg.norm(actual - expected) / max(1, np.linalg.norm(expected)))
        residuals[name] = residual
        require(residual < TOLERANCE, name)

    check("unitary", transform.conj().T @ transform, I16)
    check("fixed_chirality_commutation", transform @ gamma, gamma @ transform)
    check("head_isometry", isometry.conj().T @ isometry, I2)
    check("involution_formula", involution,
          (1 - 2 * p) * z1 + 2 * np.sqrt(p * q) * kron(X, I2, swap))
    check("positive_negative_orthogonality", positive @ negative, np.zeros((16, 16)))
    check("spectral_projector_decomposition", operator,
          tail * involution + gap * (positive - negative))
    check("leading_eigenvectors", operator @ isometry, top * isometry)
    check("chiral_operator", gamma @ operator @ gamma, -operator)
    expected_spectrum = np.array([-top] * 2 + [-tail] * 6 + [tail] * 6 + [top] * 2)
    check("entire_spectrum", np.linalg.eigvalsh(operator), expected_spectrum)

    for row in range(2):
        for column in range(2):
            matrix_unit = np.zeros((2, 2), dtype=complex)
            matrix_unit[row, column] = 1
            check(f"coherent_channel_matrix_unit_{row}{column}",
                  head_forward(isometry, matrix_unit),
                  q * kron(I2 / 2, matrix_unit) + p * kron(matrix_unit, I2 / 2))
    check("head_matrix_moment", head_forward(isometry, top**2 * I2), 6 * I4)

    # The balanced physical comparator uses the same order R1,R2,F,L.
    a, b = 2 / np.sqrt(3), np.sqrt(2 / 3)
    physical = (a * kron(Z, I2, Z, I2) + b * kron(X, I2, X, I2)
                + a * kron(I2, Z, I2, Z) + b * kron(I2, X, Z, X))
    check("physical_comparator_spectrum", np.linalg.eigvalsh(physical), expected_spectrum)
    for degree in range(10):
        expected = ((top**degree + 3 * tail**degree) * I4
                    if degree % 2 == 0 else np.zeros((4, 4)))
        # Normalize before subtracting so the test is insensitive to moment scale.
        scale = max(1, top**degree)
        check(f"synthetic_memory_moment_degree_{degree}",
              partial_references(np.linalg.matrix_power(operator, degree)) / scale,
              expected / scale)
        check(f"physical_memory_moment_degree_{degree}",
              partial_references(np.linalg.matrix_power(physical, degree)) / scale,
              expected / scale)

    pure_vectors = [np.array([1, 0]), np.array([1, 1]) / np.sqrt(2),
                    np.array([1, 1j]) / np.sqrt(2)]
    output_spectrum = np.array([0, p / 2, q / 2, 1 / 2])
    for index, vector in enumerate(pure_vectors):
        state = np.outer(vector, vector.conj())
        check(f"pure_output_spectrum_{index}",
              np.linalg.eigvalsh(head_forward(isometry, state)), output_spectrum)

    last_b, last_d = kron(I2, X), kron(I2, Z)
    resolvent = np.linalg.inv(t * np.eye(8) - kron(X, last_b) - kron(Z, last_d))
    small = np.zeros((4, 4), dtype=complex)
    for row in range(2):
        for column in range(2):
            small[2 * row:2 * row + 2, 2 * column:2 * column + 2] = (
                gap * head_dual(isometry, resolvent[4 * row:4 * row + 4,
                                                    4 * column:4 * column + 4]))
    alpha = (t * t - 2) / (t * (t * t - 4))
    expected_small = gap * (q * np.linalg.inv(t * I4 - kron(X, X) - kron(Z, Z))
                            + p * alpha * I4)
    check("four_by_four_resolvent", small, expected_small)
    expected_maximum = gap * (q / (t - 2) + p * alpha)
    check("largest_test_eigenvalue", np.linalg.eigvalsh(small)[-1], expected_maximum)
    require(expected_maximum > 1, "displayed failing envelope value")

    sigma = positive / 2
    reference_paulis = [kron(X, I2, I4), kron(Z, I2, I4),
                        kron(I2, X, I4), kron(I2, Z, I4)]
    expected_correlations = [np.sqrt(p * q) * swap / 2, (q - p) * I4 / 4,
                             (q * kron(X, I2) + p * kron(I2, X)) / 4,
                             (q * kron(Z, I2) + p * kron(I2, Z)) / 4]
    correlation_norms = []
    for label, pauli, expected in zip(("X1", "Z1", "X2", "Z2"),
                                     reference_paulis, expected_correlations):
        actual = partial_references(pauli @ sigma)
        check(f"local_correlation_{label}", actual, expected)
        correlation_norms.append(trace_norm(actual))
    check("local_Pauli_support_score", sum(correlation_norms), 14 / 5 + np.sqrt(19) / 10)
    require(sum(correlation_norms) < top, "fixed leading isometry is physically excluded")
    coefficient = np.trace(kron(Z, Y, Y, I2) @ operator) / 16
    check("forbidden_reference_Pauli_coefficient", coefficient, -q / np.sqrt(3))

    # A nondegenerate physical head checks the matrix ordering in inequality (3).
    retention = (kron(X, I2, X, I2) + kron(Z, I2, Z, I2)
                 + kron(I2, X, I2, X) + kron(I2, Z, I2, Z))
    values, vectors = np.linalg.eigh(retention)
    retained_head = vectors[:, [-1, -2]]
    retained_values = values[[-1, -2]]
    fourier = np.array([[1j ** (row * col) for col in range(4)]
                        for row in range(4)], dtype=complex) / 2
    compression_count = 0
    for rank in (1, 2):
        cap = 2 * np.sqrt(2) if rank == 1 else 2 + np.sqrt(2)
        for basis in (I4, fourier):
            support = basis[:, :rank]
            projector = support @ support.conj().T
            inserted_support = kron(I4, support)
            compression = inserted_support.conj().T @ operator @ inserted_support
            require(np.linalg.norm(compression, 2) <= cap + TOLERANCE,
                    "illustrative full memory compression")
            upper = np.diag((retained_values[0] + cap)
                            / (retained_values + retained_values[0]))
            require(np.linalg.eigvalsh(upper - head_dual(retained_head, projector))[0]
                    >= -TOLERANCE, "matrix compatibility orientation")
            compression_count += 1

    return {
        "tensor_order": ["R1", "R2", "F", "L"],
        "top_eigenvalue": float(top),
        "actual_third_eigenvalue": float(tail),
        "pure_output_spectrum": [0, p / 2, q / 2, 1 / 2],
        "rank_one_all_support_analytic_cap": float(tail + gap / 2),
        "rank_two_all_support_analytic_cap": float(tail + 39 * gap / 40),
        "last_query_test_maximum": float(expected_maximum),
        "local_Pauli_correlation_trace_norms": correlation_norms,
        "maximum_physical_energy_of_fixed_head_mixture": float(sum(correlation_norms)),
        "forbidden_Pauli_coefficient": float(coefficient.real),
        "matrix_moment_degrees_checked": list(range(10)),
        "illustrative_supports_checked": compression_count,
        "all_support_claim_basis": "analytical output-spectrum and chiral compression proof",
        "relative_identity_residuals": residuals,
        "maximum_relative_identity_residual": max(residuals.values()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    report = {
        "status": "exact synthetic envelope obstruction verified; physical converse unresolved",
        "research_base": "5434c44c31f42143d4b1f3d32892744b443d6cd4",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "tolerance": TOLERANCE,
        "exact_scalar_checks": exact_scalar_checks(),
        "construction": construction_checks(),
        "maximum_matrix_dimension": 16,
        "scope": "fails the spectral envelope; no physical Hamiltonian violation or universal proof",
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
