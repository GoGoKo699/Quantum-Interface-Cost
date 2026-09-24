#!/usr/bin/env python3
"""Exact rational interval certificate for the remaining sharp scalar bound.

The physical/operator reduction is separate. Every arithmetic enclosure here
uses Fraction and integer isqrt. No floating-point result certifies a claim.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform


SQRT_DENOMINATOR = 10**35
CELL_COUNT = 400
UNIFORM_CEILING = Fraction(999, 1000)


@dataclass(frozen=True)
class Interval:
    """Closed rational interval with exact outward arithmetic."""

    lo: Fraction
    hi: Fraction

    def __init__(self, lo, hi=None):
        object.__setattr__(self, "lo", Fraction(lo))
        object.__setattr__(self, "hi", Fraction(lo if hi is None else hi))
        assert self.lo <= self.hi

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __rsub__(self, other):
        return as_interval(other) + (-self)

    def __mul__(self, other):
        other = as_interval(other)
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_interval(other)
        assert other.lo > 0
        return self * Interval(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return as_interval(other) / self

    def square(self):
        if self.lo >= 0:
            return Interval(self.lo * self.lo, self.hi * self.hi)
        if self.hi <= 0:
            return Interval(self.hi * self.hi, self.lo * self.lo)
        return Interval(0, max(self.lo * self.lo, self.hi * self.hi))

    def sqrt(self):
        assert self.lo >= 0

        def floor_scaled_root(value):
            scaled_square = (
                value.numerator * SQRT_DENOMINATOR * SQRT_DENOMINATOR
            ) // value.denominator
            return isqrt(scaled_square)

        # floor(sqrt(q) * D) equals isqrt(floor(q * D**2)). Adding
        # one to the upper integer endpoint gives an outward enclosure,
        # including when the endpoint happens to be a perfect square.
        return Interval(
            Fraction(floor_scaled_root(self.lo), SQRT_DENOMINATOR),
            Fraction(floor_scaled_root(self.hi) + 1, SQRT_DENOMINATOR),
        )


def as_interval(value):
    return value if isinstance(value, Interval) else Interval(value)


SQRT_TWO = Interval(2).sqrt()


def certify_cell(index, count):
    """Enclose the two nonscalar branches on one entire closed cell."""
    x = Interval(Fraction(index, count), Fraction(index + 1, count))
    z = (SQRT_TWO - 1) * x
    z_squared = z.square()
    denominator = 1 + z_squared
    top = 4 / denominator
    second = 2 + 4 * z / denominator
    t = 2 + SQRT_TWO - 4 * z / denominator

    # c has a removable zero at z=sqrt(2)-1. This identity uses only
    # nonnegative factors throughout x in [0,1]:
    # 1-2z-z**2=(sqrt(2)-1-z)(sqrt(2)+1+z),
    # sqrt(2)-1-z=(sqrt(2)-1)(1-x).
    c = (
        2 * (SQRT_TWO - 1) * (1 - x) * (SQRT_TWO + 1 + z)
        / denominator
    )
    ratio = SQRT_TWO * (SQRT_TWO + 1 + z) / (SQRT_TWO + 1 - z)

    # Scaled resolvent coefficients A=cF, B=cG, S=cs. The first
    # formula uses c/(t-2)=ratio, so it remains finite at x=1.
    upper_pole = ratio * ((2 * t.square() - 4).sqrt() + t) / (2 * (t + 2))
    lower_pole = c * (t + 1) / (t * (t + 2))
    scalar = c / (t - SQRT_TWO)

    # E=(4-U)(3U+4)/8. Since 4-U=4z**2/(1+z**2), this expression
    # stays nonnegative without cancellation at the endpoint U=4.
    sld_cap = (4 * z_squared / denominator) * (3 * top + 4) / 8
    tail_from_rank = (top - 3) / (top + second)
    tail_from_sld = (1 - sld_cap.sqrt()) / 2
    tail_lower = max(Fraction(0), tail_from_rank.lo, tail_from_sld.lo)
    assert 0 <= tail_lower <= Fraction(1, 2)

    # The exact two-block expression A(1-tau)+B*tau decreases with
    # tau, since F>=G. The corresponding interval upper endpoints
    # have the same order, verified rather than assumed here.
    assert upper_pole.hi >= lower_pole.hi
    two_block = (
        upper_pole.hi * (1 - tail_lower) + lower_pole.hi * tail_lower
    )

    largest_cap = (2 + second) / (top + second)
    largest_upper = min(Fraction(1), largest_cap.hi)
    assert 0 <= largest_upper <= 1
    assert upper_pole.hi >= scalar.hi
    # Write S+(A-S)*kappa as a convex combination to reduce interval
    # dependence. The preceding ordering justifies using kappa's upper
    # endpoint after separately enclosing A and S.
    rank_one_bound = (
        upper_pole.hi * largest_upper
        + scalar.hi * (1 - largest_upper)
    )

    alpha_upper = max(Fraction(0), upper_pole.hi - scalar.lo)
    beta_upper = max(Fraction(0), scalar.hi - lower_pole.lo)
    # For centered coefficient vector (alpha,0,0,-beta), its squared
    # norm is alpha**2+beta**2-(alpha-beta)**2/4, equivalently the
    # following sum of nonnegative terms. The SLD inequality bounds
    # ||lambda-(1/4,...,1/4)|| by sqrt(E/2).
    centered_norm_squared = (
        Fraction(3, 4) * (alpha_upper**2 + beta_upper**2)
        + alpha_upper * beta_upper / 2
    )
    moment_bound = (
        (upper_pole.hi + 2 * scalar.hi + lower_pole.hi) / 4
        + (sld_cap / 2).sqrt().hi
        * Interval(centered_norm_squared).sqrt().hi
    )
    mixed = min(rank_one_bound, moment_bound)
    return two_block, mixed, rank_one_bound, moment_bound


def rational_ceiling(value, denominator=10**9):
    """Compact rational upper bound, with no floating-point rounding."""
    scaled = value * denominator
    numerator = -((-scaled.numerator) // scaled.denominator)
    return str(Fraction(numerator, denominator))


def main(output):
    if not __debug__:
        raise RuntimeError("Run this certificate without -O or -OO")
    source = Path(__file__).resolve()
    if output.resolve() == source:
        raise ValueError("The output must not overwrite the verifier source")

    # These closed cells cover the entire normalized parameter domain,
    # including both removable endpoints. No sampling or optimization occurs.
    worst_two_block = (Fraction(0), 0)
    worst_mixed = (Fraction(0), 0)
    selections = {"cap": 0, "moment": 0}
    for index in range(CELL_COUNT):
        two_block, mixed, rank_one_bound, moment_bound = certify_cell(
            index, CELL_COUNT
        )
        assert two_block <= UNIFORM_CEILING, ("two-block branch", index)
        assert mixed <= UNIFORM_CEILING, ("mixed branch", index)
        if two_block > worst_two_block[0]:
            worst_two_block = (two_block, index)
        if mixed > worst_mixed[0]:
            worst_mixed = (mixed, index)
        selections["cap" if rank_one_bound <= moment_bound else "moment"] += 1
    assert sum(selections.values()) == CELL_COUNT

    report = {
        "status": "exact rational interval certificate passed",
        "scope": "scalar reduction for two sharp anticommuting ququart pairs and one arbitrary final pair",
        "not_claimed": "unrestricted three-input optimum or arbitrary earlier Jordan angles",
        "parameter": "x=z/(sqrt(2)-1), 0<=x<=1",
        "closed_cells": CELL_COUNT,
        "sqrt_denominator": str(SQRT_DENOMINATOR),
        "sqrt_method": "integer isqrt on exact Fraction endpoints, outward enclosure",
        "two_block_uniform_upper_bound": str(UNIFORM_CEILING),
        "mixed_uniform_upper_bound": str(UNIFORM_CEILING),
        "scalar_branch": "bounded analytically by one from U<=4",
        "worst_two_block_cell_zero_based": worst_two_block[1],
        "worst_two_block_rational_upper_ceiling": rational_ceiling(worst_two_block[0]),
        "worst_mixed_cell_zero_based": worst_mixed[1],
        "worst_mixed_rational_upper_ceiling": rational_ceiling(worst_mixed[0]),
        "mixed_bound_selection_counts": selections,
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "python": platform.python_version(),
        "arithmetic": "Fraction and integer isqrt only; no floating-point certificate arithmetic",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).resolve().parents[1] / "results" / "two_sharp_pair_converse.json",
    )
    main(parser.parse_args().output)
