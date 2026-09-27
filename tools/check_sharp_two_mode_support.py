#!/usr/bin/env python3
"""Targeted algebra and construction checks for sharp two-mode support.

The all-state inequalities and equality classification are proved in the
accompanying note. This script checks their algebra, canonical attainer,
weighted frontier constructions, and exact radical boundary constant.
There is no parameter scan or numerical claim of universal optimality.
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
TOLERANCE = 4e-11
RESEARCH_BASE = "5a9d0ae04ba0c3a8a782e39c9e853d934d30ed6b"


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def kron(*matrices):
    result = np.array([[1]], dtype=complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def field(*coefficients):
    """Coefficients in the exact basis 1, sqrt(3), sqrt(5), sqrt(15)."""
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
            rational = (3 if common & 1 else 1) * (5 if common & 2 else 1)
            result[i ^ j] += a * b * rational
    return tuple(result)


def exact_algebra_checks():
    reference_paulis = [kron(X, I2), kron(Z, I2), kron(I2, X), kron(I2, Z)]
    paulis = {"I": I2, "X": X, "Y": Y, "Z": Z}
    local_eigenvalue = {"I": 2, "X": 0, "Y": -2, "Z": 0}
    laplacian_values = {}
    for first, first_matrix in paulis.items():
        for second, second_matrix in paulis.items():
            matrix = kron(first_matrix, second_matrix)
            value = local_eigenvalue[first] + local_eigenvalue[second]
            image = sum(a @ matrix @ a for a in reference_paulis)
            # These entries are exactly representable Gaussian integers.
            require(np.array_equal(image, value * matrix), "Pauli superoperator identity")
            laplacian_values[first + second] = value
    require(laplacian_values["II"] == 4
            and max(value for word, value in laplacian_values.items() if word != "II") == 2,
            "sharp identity-versus-complement superoperator bound")

    generators = [kron(X, I2, Z), kron(Z, I2, Z),
                  kron(I2, X, X), kron(I2, Z, X)]
    opposite = (1, 0, 3, 2)
    for index, generator in enumerate(generators):
        require(np.array_equal(generator @ generator, np.eye(8)), "Clifford generator square")
        for other in range(index):
            require(np.array_equal(generator @ generators[other] + generators[other] @ generator,
                                   np.zeros((8, 8))), "Clifford anticommutator")
        for axis, reference in enumerate(reference_paulis):
            sign = -1 if index == opposite[axis] else 1
            lifted = kron(reference, I2)
            require(np.array_equal(lifted @ generator @ lifted, sign * generator),
                    "opposite-axis compression identity")

    one = field(1, 0, 0, 0)
    tail = field(0, Fraction(2, 3), 0, 0)
    gap = field(0, Fraction(4, 3), 0, 0)
    t_star = field(0, Fraction(2, 3), 0, Fraction(2, 3))
    bound = field_add(tail, t_star)
    root_candidate = field_add(t_star, field_scale(Fraction(1, 2), gap))
    require(all(coefficient >= 0 for coefficient in root_candidate)
            and any(coefficient > 0 for coefficient in root_candidate),
            "positive branch of the exact radical")
    require(field_multiply(root_candidate, root_candidate)
            == field_add(field_scale(2, field_multiply(t_star, t_star)), field_scale(-4, one)),
            "sqrt(2t_star^2-4)=t_star+g/2 after positive squaring")
    require(field_scale(2, field_add(root_candidate, field_scale(-1, t_star))) == gap,
            "exact g F(t_star)=1")
    require(field_multiply(t_star, t_star) == field(8, 0, Fraction(8, 3), 0),
            "exact t_star square")
    require(field_multiply(bound, bound) == field(12, 0, Fraction(16, 3), 0),
            "exact boundary norm square")
    require(Fraction(5) < Fraction(15, 4)**2, "t_star<3sqrt(2)")
    require(Fraction(8) > 4, "t_star>2")
    require(5 * 16**2 < 39**2, "boundary norm strictly below 5")
    require(1 < 2, "5<4+sqrt(2)")
    return {
        "reference_Pauli_superoperator_eigenvalues": laplacian_values,
        "Clifford_generator_squares_checked": 4,
        "Clifford_anticommutators_checked": 6,
        "opposite_axis_conjugations_checked": 16,
        "radical_field_basis": ["1", "sqrt(3)", "sqrt(5)", "sqrt(15)"],
        "boundary_constant": "(4+2sqrt(5))/sqrt(3)",
        "resolvent_parameter": "(2+2sqrt(5))/sqrt(3)",
        "positive_radical_identity": "sqrt(2t_star^2-4)=t_star+2/sqrt(3)",
        "resolvent_certificate": "g/[2(sqrt(2t_star^2-4)-t_star)]=1",
        "strict_range_and_gap_witnesses": ["8>4", "80<225", "1280<1521", "1<2"],
        "radical_identities_and_strict_signs_use_floating_point": False,
    }


def partial_references(matrix):
    return np.einsum("rqrs->qs", matrix.reshape(4, 4, 4, 4))


def trace_norm(matrix):
    return float(np.sum(np.linalg.svd(matrix, compute_uv=False)))


def correlation(sigma, reference):
    return partial_references(kron(reference, I4) @ sigma)


def sign_reflection(matrix):
    if np.linalg.norm(matrix) < TOLERANCE:
        return I4.copy()
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.where(values >= 0, 1, -1)) @ vectors.conj().T


def compare(residuals, name, actual, expected):
    residual = float(np.linalg.norm(actual - expected) / max(1, np.linalg.norm(expected)))
    residuals[name] = residual
    require(residual < TOLERANCE, name)


def equality_construction_checks():
    residuals = {}
    c = np.sqrt((1 + 1 / np.sqrt(2)) / 2)
    s = np.sqrt((1 - 1 / np.sqrt(2)) / 2)
    conditionals = [np.array([c, s]), np.array([c, -s]),
                    np.array([s, c]), np.array([s, -c])]
    # Tensor order R1,R2,Q,E; Q uses the same two-bit computational labels as R.
    purification = np.zeros((4, 4, 2), dtype=complex)
    for label, vector in enumerate(conditionals):
        purification[label, label, :] = vector / 2
    sigma = np.einsum("rqe,sve->rqsv", purification, purification.conj()).reshape(16, 16)
    rho = np.einsum("rqe,sqf->resf", purification, purification.conj()).reshape(8, 8)
    isometry = np.sqrt(2) * purification.reshape(16, 2)
    involution = (kron(Z, I2, Z) + kron(I2, Z, X)) / np.sqrt(2)
    complement_projector = (np.eye(8) + involution) / 2
    compare(residuals, "flat_complement", rho, complement_projector / 4)
    compare(residuals, "head_isometry", isometry.conj().T @ isometry, I2)
    compare(residuals, "flat_rank_two_support", sigma, isometry @ isometry.conj().T / 2)
    compare(residuals, "memory_marginal", partial_references(sigma), I4 / 4)
    compare(residuals, "purifying_qubit_marginal",
            np.einsum("rers->es", rho.reshape(4, 2, 4, 2)), I2 / 2)

    new_references = [kron(Z, I2), kron(X, I2), kron(I2, Z), kron(I2, X)]
    new_correlations = [correlation(sigma, reference) for reference in new_references]
    expected_correlations = [kron(Z, I2) / 4, kron(X, I2) / (4 * np.sqrt(2)),
                             kron(I2, Z) / 4, kron(Z, X) / (4 * np.sqrt(2))]
    for index, (actual, expected) in enumerate(zip(new_correlations, expected_correlations)):
        compare(residuals, f"bisector_correlation_{index}", actual, expected)
    old_references, old_correlations = [], []
    for site in range(2):
        for sign in (1, -1):
            old_references.append((new_references[2 * site] + sign * new_references[2 * site + 1])
                                  / np.sqrt(2))
            old_correlations.append((new_correlations[2 * site] + sign * new_correlations[2 * site + 1])
                                    / np.sqrt(2))
    expected_readouts = [np.sqrt(2 / 3) * kron(Z, I2) + kron(X, I2) / np.sqrt(3),
                         np.sqrt(2 / 3) * kron(Z, I2) - kron(X, I2) / np.sqrt(3),
                         np.sqrt(2 / 3) * kron(I2, Z) + kron(Z, X) / np.sqrt(3),
                         np.sqrt(2 / 3) * kron(I2, Z) - kron(Z, X) / np.sqrt(3)]
    for index, (matrix, readout) in enumerate(zip(old_correlations, expected_readouts)):
        compare(residuals, f"full_rank_correlation_spectrum_{index}", np.linalg.eigvalsh(matrix),
                np.array([-1, -1, 1, 1]) * np.sqrt(3) / 8)
        compare(residuals, f"unique_sign_readout_{index}", sign_reflection(matrix), readout)
        compare(residuals, f"reflection_{index}", readout @ readout, I4)
    profile = np.array([trace_norm(matrix) for matrix in old_correlations])
    compare(residuals, "sharp_squared_support_sum", np.dot(profile, profile), 3)
    operator = sum(kron(reference, readout) for reference, readout in zip(old_references, expected_readouts))
    a, b = 2 / np.sqrt(3), np.sqrt(2 / 3)
    expected_operator = (a * kron(Z, I2, Z, I2) + b * kron(X, I2, X, I2)
                         + a * kron(I2, Z, I2, Z) + b * kron(I2, X, Z, X))
    compare(residuals, "canonical_balanced_operator", operator, expected_operator)
    top, tail = 2 * np.sqrt(3), 2 / np.sqrt(3)
    expected_spectrum = np.array([-top] * 2 + [-tail] * 6 + [tail] * 6 + [top] * 2)
    compare(residuals, "complete_equality_spectrum", np.linalg.eigvalsh(operator), expected_spectrum)
    compare(residuals, "degenerate_leading_eigenvectors", operator @ isometry, top * isometry)
    for row in range(2):
        for column in range(2):
            matrix_unit = np.zeros((2, 2), dtype=complex)
            matrix_unit[row, column] = 1
            actual = partial_references(isometry @ matrix_unit @ isometry.conj().T)
            expected = np.diag([vector.conj() @ matrix_unit @ vector / 2 for vector in conditionals])
            compare(residuals, f"square_POVM_channel_{row}{column}", actual, expected)
    return {
        "correlation_trace_norms": profile.tolist(),
        "squared_support_sum": float(np.dot(profile, profile)),
        "leading_eigenvalues": [float(top), float(top)],
        "third_eigenvalue": float(tail),
        "correlation_eigenvalues_exact": ["-sqrt(3)/8 twice", "+sqrt(3)/8 twice"],
        "boundary_norm_upper_bound_display": float((4 + 2 * np.sqrt(5)) / np.sqrt(3)),
        "boundary_norm_attainment_claimed": False,
        "relative_identity_residuals": residuals,
    }


def weighted_frontier_checks():
    # Each squared profile is rational. The three weighted support certificates
    # with positive multiplier satisfy w=lambda*t+mu, mu>=0 on saturated axes.
    cases = [
        ("balanced", [Fraction(3, 4)] * 4, [1.0] * 4, 2 / np.sqrt(3)),
        ("rational_interior", [Fraction(121, 169)] * 3 + [Fraction(144, 169)],
         [11 / 13, 11 / 13, 11 / 13, 12 / 13], 1.0),
        ("one_saturated_axis", [Fraction(1)] + [Fraction(2, 3)] * 3,
         [3.0, 1.0, 1.0, 1.0], np.sqrt(3 / 2)),
        ("zero_weight_and_zero_correlation", [Fraction(1)] * 3 + [Fraction(0)],
         [2.0, 1.0, 1.0, 0.0], 0.0),
        ("single_nonzero_weight", [Fraction(1)] * 3 + [Fraction(0)],
         [1.0, 0.0, 0.0, 0.0], 0.0),
        ("all_zero_weights", [Fraction(1)] * 3 + [Fraction(0)],
         [0.0] * 4, 0.0),
    ]
    require(3 * 121 + 144 == 3 * 169, "exact rational interior sphere point")
    require(Fraction(9) > Fraction(3, 2), "positive saturated-axis multiplier")
    generators = [kron(X, I2, Z), kron(Z, I2, Z), kron(I2, X, X), kron(I2, Z, X)]
    reference_paulis = [kron(X, I2), kron(Z, I2), kron(I2, X), kron(I2, Z)]
    opposite = (1, 0, 3, 2)
    records = []
    for name, squared_profile, raw_weights, multiplier in cases:
        require(sum(squared_profile) == 3 and all(0 <= value <= 1 for value in squared_profile),
                "exact capped sphere profile")
        if name == "balanced":
            require(all(Fraction(4, 3) * value == 1 for value in squared_profile),
                    "exact balanced support dual coefficient")
        elif name == "rational_interior":
            rational_weights = [Fraction(11, 13)] * 3 + [Fraction(12, 13)]
            require([weight**2 for weight in rational_weights] == squared_profile,
                    "exact rational support dual coefficient")
        elif name == "one_saturated_axis":
            require(squared_profile[0] == 1
                    and all(Fraction(3, 2) * value == 1 for value in squared_profile[1:]),
                    "exact saturated support dual coefficients")
        else:
            require(all(weight == 0 or value == 1
                        for weight, value in zip(raw_weights, squared_profile)),
                    "zero-multiplier support dual certificate")
        squared_coefficients = [1 - squared_profile[opposite[j]] for j in range(4)]
        require(sum(squared_coefficients) == 1, "exact Clifford coefficient normalization")
        coefficients = np.sqrt(np.array([float(value) for value in squared_coefficients]))
        profile = np.sqrt(np.array([float(value) for value in squared_profile]))
        weights = np.array(raw_weights)
        residuals = {}
        slack = weights - multiplier * profile
        require(np.min(slack) >= -TOLERANCE
                and np.linalg.norm(slack * (1 - profile)) < TOLERANCE,
                "finite weighted support dual certificate")
        support_value = float(np.dot(weights, profile))
        compare(residuals, "weighted_support_duality", support_value, 3 * multiplier + np.sum(slack))
        involution = sum(coefficient * generator for coefficient, generator in zip(coefficients, generators))
        projector = (np.eye(8) + involution) / 2
        compare(residuals, "involution", involution @ involution, np.eye(8))
        compare(residuals, "rank_four_projection", projector @ projector, projector)
        rho = projector / 4
        compare(residuals, "maximally_mixed_purifying_qubit",
                np.einsum("rers->es", rho.reshape(4, 2, 4, 2)), I2 / 2)
        values, vectors = np.linalg.eigh(involution)
        positive_basis = vectors[:, values > 0]
        require(positive_basis.shape == (8, 4), "four-dimensional complement support")
        # Purification order R,E,Q, then reorder to R,Q,E.
        purification = (positive_basis / 2).reshape(4, 2, 4).transpose(0, 2, 1)
        sigma = np.einsum("rqe,sve->rqsv", purification, purification.conj()).reshape(16, 16)
        head = np.sqrt(2) * purification.reshape(16, 2)
        compare(residuals, "flat_rank_two_support", sigma, head @ head.conj().T / 2)
        compare(residuals, "head_isometry", head.conj().T @ head, I2)
        correlations = [correlation(sigma, reference) for reference in reference_paulis]
        actual_profile = np.array([trace_norm(matrix) for matrix in correlations])
        compare(residuals, "attained_profile", actual_profile, profile)
        for axis, reference in enumerate(reference_paulis):
            compressed = projector @ kron(reference, I2) @ projector
            compare(residuals, f"compression_square_{axis}", compressed @ compressed,
                    float(squared_profile[axis]) * projector)
        readouts = [sign_reflection(matrix) for matrix in correlations]
        operator = sum(weight * kron(reference, readout)
                       for weight, reference, readout in zip(weights, reference_paulis, readouts))
        energy = float(np.trace(operator @ sigma).real)
        compare(residuals, "attained_weighted_energy", energy, support_value)
        leading_sum = float(np.sum(np.linalg.eigvalsh(operator)[-2:]))
        compare(residuals, "attained_weighted_Ky_Fan_sum", leading_sum, 2 * support_value)
        records.append({
            "case": name,
            "squared_profile_exact": [str(value) for value in squared_profile],
            "squared_Clifford_coefficients_exact": [str(value) for value in squared_coefficients],
            "weights": weights.tolist(),
            "weighted_support_value": support_value,
            "sum_of_two_leading_eigenvalues": leading_sum,
            "relative_identity_residuals": residuals,
        })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    source = Path(__file__).resolve()
    note = source.parents[1] / "docs/audits/SHARP_TWO_MODE_SUPPORT.md"
    report = {
        "status": "targeted algebra and construction checks passed",
        "research_base": RESEARCH_BASE,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "proof_note_sha256": hashlib.sha256(note.read_bytes()).hexdigest(),
        "tolerance": TOLERANCE,
        "exact_algebra": exact_algebra_checks(),
        "canonical_equality_construction": equality_construction_checks(),
        "weighted_frontier_constructions": weighted_frontier_checks(),
        "maximum_matrix_dimension": 16,
        "scope": "finite checks of supplied proofs; no parameter scan or unrestricted converse claim",
    }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        if arguments.output.resolve() in (source, note.resolve()):
            raise ValueError("The output must not overwrite the verifier or proof note")
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
