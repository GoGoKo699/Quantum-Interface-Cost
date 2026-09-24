#!/usr/bin/env python3
"""Check the partial-SWAP theorem's finite spin matrices using exact arithmetic.

The proof reduces a five-qubit operator to its total-spin multiplicity
matrices. This script independently builds the displayed highest-weight
vectors in the computational basis and checks their matrix coefficients.
All coefficients are rational combinations of square roots of integers;
there are no floating-point tolerances or third-party dependencies.

This checks the finite representation and phase convention. It does not
replace the analytical Schur-complement positivity proof, certify arbitrary
U(4) subsystem embeddings, or certify publication originality.

Example:
    python tools/check_partial_swap_basis.py --output results/partial_swap_basis.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path
from typing import TypeAlias


def squarefree_parts(number: int) -> tuple[int, int]:
    """Return (outside, inside) with sqrt(number) = outside * sqrt(inside)."""
    if number <= 0:
        raise ValueError("The radicand must be positive.")
    outside = 1
    inside = 1
    divisor = 2
    remaining = number
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            remaining //= divisor
            exponent += 1
        outside *= divisor ** (exponent // 2)
        if exponent % 2:
            inside *= divisor
        divisor += 1
    inside *= remaining
    return outside, inside


class Radical:
    """A finite exact sum of rational multiples of squarefree square roots."""

    def __init__(self, value: int | Fraction = 0) -> None:
        coefficient = Fraction(value)
        self.terms: dict[int, Fraction] = {1: coefficient} if coefficient else {}

    @classmethod
    def root(cls, number: int) -> Radical:
        outside, inside = squarefree_parts(number)
        result = cls()
        result.terms = {inside: Fraction(outside)}
        return result

    @staticmethod
    def coerce(value: Radical | int | Fraction) -> Radical:
        return value if isinstance(value, Radical) else Radical(value)

    def __add__(self, other: Radical | int | Fraction) -> Radical:
        other = self.coerce(other)
        result = Radical()
        result.terms = self.terms.copy()
        for radicand, coefficient in other.terms.items():
            result.terms[radicand] = result.terms.get(radicand, Fraction(0)) + coefficient
        result.terms = {key: value for key, value in result.terms.items() if value}
        return result

    def __radd__(self, other: int | Fraction) -> Radical:
        return self + other

    def __neg__(self) -> Radical:
        return self * -1

    def __sub__(self, other: Radical | int | Fraction) -> Radical:
        return self + -self.coerce(other)

    def __mul__(self, other: Radical | int | Fraction) -> Radical:
        other = self.coerce(other)
        result = Radical()
        for left_root, left_coefficient in self.terms.items():
            for right_root, right_coefficient in other.terms.items():
                outside, inside = squarefree_parts(left_root * right_root)
                product = left_coefficient * right_coefficient * outside
                result.terms[inside] = result.terms.get(inside, Fraction(0)) + product
        result.terms = {key: value for key, value in result.terms.items() if value}
        return result

    def __rmul__(self, other: int | Fraction) -> Radical:
        return self * other

    def __truediv__(self, other: int) -> Radical:
        return self * Fraction(1, other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (int, Fraction)):
            other = Radical(other)
        if not isinstance(other, Radical):
            return NotImplemented
        return self.terms == other.terms

    def __repr__(self) -> str:
        return f"Radical({self.terms!r})"


Vector: TypeAlias = dict[str, Radical]


def ket(bits: str) -> Vector:
    return {bits: Radical(1)}


def add_vectors(*vectors: Vector) -> Vector:
    result: Vector = {}
    for vector in vectors:
        for bits, coefficient in vector.items():
            result[bits] = result.get(bits, Radical()) + coefficient
    return {bits: coefficient for bits, coefficient in result.items() if coefficient != 0}


def scale(vector: Vector, factor: Radical | int | Fraction) -> Vector:
    result = {bits: coefficient * factor for bits, coefficient in vector.items()}
    return {bits: coefficient for bits, coefficient in result.items() if coefficient != 0}


def tensor(left: Vector, right: Vector) -> Vector:
    return {
        left_bits + right_bits: left_coefficient * right_coefficient
        for left_bits, left_coefficient in left.items()
        for right_bits, right_coefficient in right.items()
    }


def inner(left: Vector, right: Vector) -> Radical:
    # These highest-weight basis vectors have real coefficients.
    return sum(
        (coefficient * right.get(bits, Radical()) for bits, coefficient in left.items()),
        Radical(),
    )


def swap(vector: Vector, first: int, second: int) -> Vector:
    result: Vector = {}
    for bits, coefficient in vector.items():
        reordered = list(bits)
        reordered[first], reordered[second] = reordered[second], reordered[first]
        result["".join(reordered)] = coefficient
    return result


def singlet_projector(vector: Vector, reference: int) -> Vector:
    # Computational order is R1, R2, R3, A, B.
    return scale(add_vectors(vector, scale(swap(vector, reference, 3), -1)), Fraction(1, 2))


def total_raising(vector: Vector) -> Vector:
    result: Vector = {}
    for bits, coefficient in vector.items():
        for position in range(5):
            if bits[position] == "1":
                raised = bits[:position] + "0" + bits[position + 1 :]
                result[raised] = result.get(raised, Radical()) + coefficient
    return {bits: coefficient for bits, coefficient in result.items() if coefficient != 0}


def highest_weight_bases() -> tuple[list[Vector], list[Vector]]:
    root = Radical.root
    t_three = ket("000")
    t_one = scale(add_vectors(ket("001"), ket("010"), ket("100")), root(3) / 3)
    t_minus_one = scale(add_vectors(ket("011"), ket("101"), ket("110")), root(3) / 3)
    a_plus = scale(add_vectors(ket("010"), scale(ket("100"), -1)), root(2) / 2)
    a_minus = scale(add_vectors(ket("011"), scale(ket("101"), -1)), root(2) / 2)
    b_plus = scale(
        add_vectors(scale(ket("001"), 2), scale(ket("010"), -1), scale(ket("100"), -1)),
        root(6) / 6,
    )
    b_minus = scale(
        add_vectors(ket("011"), ket("101"), scale(ket("110"), -2)), root(6) / 6
    )
    triplet_plus = ket("00")
    triplet_minus = ket("11")
    triplet_zero = scale(add_vectors(ket("01"), ket("10")), root(2) / 2)
    memory_singlet = scale(add_vectors(ket("01"), scale(ket("10"), -1)), root(2) / 2)

    spin_half = [
        add_vectors(
            scale(tensor(t_three, triplet_minus), root(2) / 2),
            scale(tensor(t_one, triplet_zero), -root(3) / 3),
            scale(tensor(t_minus_one, triplet_plus), root(6) / 6),
        )
    ]
    for plus, minus in [(a_plus, a_minus), (b_plus, b_minus)]:
        spin_half.append(
            add_vectors(
                scale(tensor(minus, triplet_plus), root(6) / 3),
                scale(tensor(plus, triplet_zero), -root(3) / 3),
            )
        )
    spin_half.extend([tensor(a_plus, memory_singlet), tensor(b_plus, memory_singlet)])
    spin_three_half = [
        add_vectors(
            scale(tensor(t_three, triplet_zero), root(15) / 5),
            scale(tensor(t_one, triplet_plus), -root(10) / 5),
        ),
        tensor(a_plus, triplet_plus),
        tensor(b_plus, triplet_plus),
        tensor(t_three, memory_singlet),
    ]
    return spin_half, spin_three_half


def require(condition: bool, description: str) -> None:
    # Deliberately not an assert: python -O must not disable verification.
    if not condition:
        raise ArithmeticError(description)


def verify() -> dict[str, int | str]:
    spin_half, spin_three_half = highest_weight_bases()
    root = Radical.root
    zero = Radical()
    one = Radical(1)
    expected_half = [
        [[root(2) / 4, root(6) / 12], [zero, -one / 4], [-one / 4, root(3) / 6]],
        [[-root(2) / 4, root(6) / 12], [zero, one / 4], [one / 4, root(3) / 6]],
        [[zero, -root(6) / 6], [root(3) / 4, zero], [zero, -root(3) / 12]],
    ]
    expected_three_half = [
        [-root(15) / 12, -one / 4, -root(3) / 12],
        [-root(15) / 12, one / 4, -root(3) / 12],
        [-root(15) / 12, zero, root(3) / 6],
    ]
    counts = {
        "highest_weight_vectors": 0,
        "orthonormality_entries": 0,
        "memory_swap_eigenvectors": 0,
        "projector_invariant_vectors": 0,
        "off_diagonal_coefficients": 0,
        "diagonal_sum_coefficients": 0,
        "symmetric_projector_actions": 0,
    }

    for basis, down_spins in [(spin_half, 2), (spin_three_half, 1)]:
        for row, vector in enumerate(basis):
            require(all(bits.count("1") == down_spins for bits in vector), "Wrong J_z eigenvalue")
            require(not total_raising(vector), "The vector is not highest weight")
            counts["highest_weight_vectors"] += 1
            sign = 1 if row < 3 else -1
            require(swap(vector, 3, 4) == scale(vector, sign), "Wrong memory SWAP sign")
            counts["memory_swap_eigenvectors"] += 1
            for column, other in enumerate(basis):
                require(inner(vector, other) == int(row == column), "Nonorthonormal basis")
                counts["orthonormality_entries"] += 1
            for reference in range(3):
                projected = singlet_projector(vector, reference)
                expanded = add_vectors(*(scale(other, inner(other, projected)) for other in basis))
                require(projected == expanded, "The projector leaves the stated spin multiplicity space")
                counts["projector_invariant_vectors"] += 1

    for reference in range(3):
        for row in range(3):
            for column in range(2):
                actual = inner(spin_half[row], singlet_projector(spin_half[3 + column], reference))
                require(actual == expected_half[reference][row][column], "Incorrect spin-1/2 coefficient")
                counts["off_diagonal_coefficients"] += 1
            actual = inner(spin_three_half[row], singlet_projector(spin_three_half[3], reference))
            require(actual == expected_three_half[reference][row], "Incorrect spin-3/2 coefficient")
            counts["off_diagonal_coefficients"] += 1

    diagonal_cases = [
        (spin_half, [Fraction(2), Fraction(5, 4), Fraction(5, 4), Fraction(3, 4), Fraction(3, 4)]),
        (spin_three_half, [Fraction(5, 4), Fraction(1, 2), Fraction(1, 2), Fraction(3, 4)]),
    ]
    for basis, diagonal in diagonal_cases:
        for row, left in enumerate(basis):
            for column, right in enumerate(basis):
                if (row < 3) != (column < 3):
                    continue
                actual = sum(
                    (inner(left, singlet_projector(right, reference)) for reference in range(3)),
                    zero,
                )
                expected = diagonal[row] if row == column else 0
                require(actual == expected, "Incorrect triplet/singlet diagonal sum")
                counts["diagonal_sum_coefficients"] += 1

    for reference in range(3):
        require(not singlet_projector(ket("00000"), reference), "Nonzero fully symmetric block")
        counts["symmetric_projector_actions"] += 1
    require(6 * 1 + 4 * len(spin_three_half) + 2 * len(spin_half) == 32, "Wrong dimension count")
    return {"status": "pass", **counts}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=Path("results/partial_swap_basis.json"), help="Result JSON path"
    )
    args = parser.parse_args()
    source_path = Path(__file__).resolve()
    if args.output.resolve() == source_path:
        parser.error("The output path must differ from the verifier source.")
    checks = verify()
    result = {
        "schema_version": 1,
        "verifier": source_path.name,
        "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        "python_version": platform.python_version(),
        "arithmetic": "exact rational combinations of squarefree integer square roots",
        "checks": checks,
        "scope": "finite SU(2) multiplicity matrices and the memory-SWAP phase convention",
        "limitations": (
            "does not replace the continuous Schur-complement proof "
            "or establish the arbitrary-U(4) case"
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: exact partial-SWAP spin matrices; wrote {args.output}")


if __name__ == "__main__":
    main()
