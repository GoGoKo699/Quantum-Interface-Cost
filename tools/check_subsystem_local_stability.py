#!/usr/bin/env python3
"""Verify the local Bell-subsystem stability calculation.

The exact part reconstructs five-qubit singlet projectors and verifies the
reduced resolvent and rational second-order coefficients. The continuous
theorem also requires the symmetry and coordinate arguments in the report;
these finite checks are not a substitute for those arguments.

Eight small floating-point constructions check the actual perturbed operators.
There is no optimizer, random search for violations, or large simulation.

Example:
    python tools/check_subsystem_local_stability.py --output results/subsystem_local_stability.json
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


F = Fraction


def require(condition: bool, message: str) -> None:
    """Keep checks active under python -O as well as ordinary execution."""
    if not condition:
        raise RuntimeError(message)


def kron_all(matrices: list[np.ndarray]) -> np.ndarray:
    result = np.ones((1, 1), dtype=matrices[0].dtype)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def on_qubit(index: int, matrix: np.ndarray, identity: np.ndarray) -> np.ndarray:
    return kron_all([matrix if j == index else identity for j in range(5)])


def commutator(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return left @ right - right @ left


def fraction_text(value: F) -> str:
    return str(value)


def exact_checks() -> tuple[dict, tuple[np.ndarray, ...]]:
    """Use rational real matrices; Y_i Y_j is represented as -J_i J_j."""
    identity2 = np.eye(2, dtype=object)
    x = np.array([[0, 1], [1, 0]], dtype=object)
    j = np.array([[0, -1], [1, 0]], dtype=object)  # Y=i J
    z = np.diag([1, -1]).astype(object)
    identity = np.eye(32, dtype=object)
    zero = np.zeros((32, 32), dtype=object)

    def at(index: int, matrix: np.ndarray) -> np.ndarray:
        return on_qubit(index, matrix, identity2)

    def singlet(first: int, second: int) -> np.ndarray:
        return F(1, 4) * (
            identity
            - at(first, x) @ at(second, x)
            + at(first, j) @ at(second, j)
            - at(first, z) @ at(second, z)
        )

    p1, p2, p3 = singlet(0, 3), singlet(1, 3), singlet(2, 4)
    k12 = p1 + p2
    base = k12 + p3
    e15 = F(2, 3) * (k12 @ k12) - F(1, 3) * k12
    e05 = -2 * (k12 @ k12) + 3 * k12
    e0 = identity - e15 - e05
    top = e15 @ p3
    resolvent = (
        e0 @ (F(2, 5) * (identity - p3) + F(2, 3) * p3)
        + e05 @ (F(1, 2) * (identity - p3) + p3)
        + e15 @ (identity - p3)
    )

    identities_checked = 0

    def matrix_equal(left: np.ndarray, right: np.ndarray, name: str) -> None:
        nonlocal identities_checked
        require(np.array_equal(left, right), f"Exact identity failed: {name}")
        identities_checked += 1

    for number, projector in enumerate((p1, p2, p3), 1):
        matrix_equal(projector @ projector, projector, f"P{number} is a projector")
        require(np.trace(projector) == 8, f"Unexpected rank for P{number}")
    matrix_equal(top @ top, top, "top projector")
    matrix_equal(base @ top, F(5, 2) * top, "top eigenvalue")
    matrix_equal(resolvent @ top, zero, "reduced resolvent annihilates top")
    matrix_equal(
        (F(5, 2) * identity - base) @ resolvent,
        identity - top,
        "reduced resolvent inverse on complement",
    )
    require(np.trace(top) == 2, "The top eigenspace must have dimension two")

    gx = at(3, x) @ at(4, x)
    gz = at(3, z) @ at(4, x)
    cases = [
        ("G_only", gx, zero, F(-2, 3), F(11, 30), F(-3, 10)),
        ("H_only", zero, gx, F(-1), F(7, 15), F(-8, 15)),
        ("same_direction", gx, gx, F(-5, 3), F(41, 30), F(-3, 10)),
        ("orthogonal_directions", gx, gz, F(-5, 3), F(5, 6), F(-5, 6)),
        ("H_half_G", gx, F(1, 2) * gx, F(-11, 12), F(3, 4), F(-1, 6)),
    ]
    coefficients = []
    for name, generator_g, generator_h, direct_expected, response_expected, total_expected in cases:
        # The physical first derivative is i times this real antisymmetric matrix.
        derivative_without_i = commutator(generator_g, p2) + commutator(generator_h, p3)
        second = -F(1, 2) * (
            commutator(generator_g, commutator(generator_g, p2))
            + commutator(generator_h, commutator(generator_h, p3))
        )
        direct = top @ second @ top
        response = -top @ derivative_without_i @ resolvent @ derivative_without_i @ top
        effective = direct + response
        matrix_equal(top @ derivative_without_i @ top, zero, f"{name}: first derivative")
        matrix_equal(direct, direct_expected * top, f"{name}: direct Taylor term")
        matrix_equal(response, response_expected * top, f"{name}: resolvent response")
        matrix_equal(effective, total_expected * top, f"{name}: effective curvature")
        coefficients.append({
            "case": name,
            "direct": fraction_text(direct_expected),
            "response": fraction_text(response_expected),
            "total": fraction_text(total_expected),
        })

    # Positivity of the curvature coefficient matrix minus I/8.
    first_minor = F(3, 10) - F(1, 8)
    determinant = first_minor * (F(8, 15) - F(1, 8)) - F(4, 15) ** 2
    require(first_minor == F(7, 40) and determinant == F(1, 2880), "Curvature certificate changed")
    require(first_minor > 0 and determinant > 0, "Curvature does not exceed I/8")

    radius = F(1, 1024)
    # Rational constants from the continuous remainder proof, valid for epsilon<=1/100.
    remainder_constant = F(75, 4) + F(341, 20) + F(10571, 100000) + F(7, 2)
    require(remainder_constant < 40, "The remainder constant is not below forty")
    require(radius <= F(1, 100), "Radius exceeds the preliminary inverse-estimate range")
    require(40 * radius < F(1, 16), "The remainder can consume the claimed gap")

    result = {
        "status": "pass",
        "arithmetic": "exact rational Fraction matrix arithmetic",
        "matrix_dimension": 32,
        "matrix_identities_checked": identities_checked,
        "coefficient_cases": coefficients,
        "curvature_matrix": [["3/10", "-4/15"], ["-4/15", "8/15"]],
        "curvature_minus_I_over_8_first_minor": fraction_text(first_minor),
        "curvature_minus_I_over_8_determinant": fraction_text(determinant),
        "radius": fraction_text(radius),
        "norm_gap_coefficient": "1/16",
        "continuous_remainder_constant_upper_bound": 40,
        "rational_remainder_constant": fraction_text(remainder_constant),
    }
    return result, tuple(np.asarray(matrix, dtype=complex) for matrix in (p1, p2, p3, top))


def floating_checks(projectors: tuple[np.ndarray, ...]) -> dict:
    """Evaluate eight prescribed perturbations, including complex memory matrices."""
    p1, p2, p3, top = projectors
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    words = [np.kron(a, b) for a in (x, y, z) for b in (x, y, z)]

    def generator(coefficients: np.ndarray) -> np.ndarray:
        return sum((weight * word for weight, word in zip(coefficients.flat, words)), np.zeros((4, 4), complex))

    def unitary(hermitian: np.ndarray) -> np.ndarray:
        eigenvalues, eigenvectors = np.linalg.eigh(hermitian)
        return (eigenvectors * np.exp(1j * eigenvalues)) @ eigenvectors.conj().T

    seed = np.random.default_rng(20260924)
    basis = np.zeros((3, 3))
    basis[0, 0] = 1
    raw_cases = [
        ("G_only", basis, np.zeros((3, 3))),
        ("H_only", np.zeros((3, 3)), basis),
        ("same_direction", basis, basis),
        ("H_half_G", basis, basis / 2),
    ]
    raw_cases.extend((f"dense_complex_{index}", seed.normal(size=(3, 3)), seed.normal(size=(3, 3))) for index in range(4))
    tolerance = 2e-12
    records = []
    for index, (name, raw_g, raw_h) in enumerate(raw_cases):
        epsilon = 2.0 ** (-10 if index % 2 == 0 else -11)
        normalization = np.sqrt(np.sum(raw_g ** 2) + np.sum(raw_h ** 2))
        g, h = raw_g * epsilon / normalization, raw_h * epsilon / normalization
        ug, uh = unitary(generator(g)), unitary(generator(h))
        full_g, full_h = np.kron(np.eye(8), ug), np.kron(np.eye(8), uh)
        operator = p1 + full_g @ p2 @ full_g.conj().T + full_h @ p3 @ full_h.conj().T
        eigenvalues = np.linalg.eigvalsh(operator)
        curvature = np.sum(g ** 2) / 6 + (8 / 15) * np.sum((h - g / 2) ** 2)
        predicted_top = 2.5 - curvature
        actual_top = float(eigenvalues[-1])
        required_upper = 2.5 - epsilon ** 2 / 16
        require(actual_top <= required_upper + tolerance, f"Floating gap check failed: {name}")
        require(abs(actual_top - predicted_top) <= 40 * epsilon ** 3 + tolerance, f"Floating Taylor check failed: {name}")
        require(np.linalg.norm(operator - operator.conj().T) < tolerance, f"Non-Hermitian construction: {name}")
        records.append({
            "case": name,
            "epsilon": epsilon,
            "lambda_max": actual_top,
            "certified_upper": required_upper,
            "second_order_prediction": float(predicted_top),
            "prediction_residual": float(abs(actual_top - predicted_top)),
            "top_doublet_splitting": float(eigenvalues[-1] - eigenvalues[-2]),
            "margin_below_claimed_upper": float(required_upper - actual_top),
        })
    return {
        "status": "pass",
        "construction_count": len(records),
        "random_seed_for_fixed_dense_constructions": 20260924,
        "tolerance": tolerance,
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results/subsystem_local_stability.json"))
    args = parser.parse_args()
    source = Path(__file__).resolve()
    if args.output.resolve() == source:
        parser.error("The output must differ from the verifier source.")
    exact, projectors = exact_checks()
    numerical = floating_checks(projectors)
    result = {
        "schema_version": 1,
        "verifier": source.name,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "scope": "exact local curvature and prescribed nearby subsystem constructions",
        "limitations": "requires the report's continuous symmetry, gauge-chart and remainder arguments; does not prove the arbitrary-U(4) bound or classify remote equality cases",
        "exact": exact,
        "floating": numerical,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: exact local subsystem curvature and eight finite constructions; wrote {args.output}")


if __name__ == "__main__":
    main()
