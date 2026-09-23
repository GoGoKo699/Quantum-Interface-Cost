#!/usr/bin/env python3
"""Exact rational certificate for one interior profile optimizer.

Replay with:
    python tools/certify_profile_optimizer.py --output results/profile_optimizer_certificate.json

Every enclosure uses Python integers and Fraction arithmetic. No floating
point, numerical solver, or third-party package is used. The global optimizer
and uniqueness assertions come from the analytical profile theorem; this
script certifies its one-dimensional root and value at (x,z)=(99/100,1/2).
It does not certify unrestricted quantum-memory optimality or novelty.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import json
from math import isqrt
from pathlib import Path


BASE = "65fabd7d870df705193017cc61e7230fc4943a5b"
ARITHMETIC_DIGITS = 75
SQRT_DIGITS = 65
LOG_TERMS = 100
OUTPUT_DIGITS = 18
SCALE = 10 ** ARITHMETIC_DIGITS


def require(condition: bool, message: str) -> None:
    """Checks remain enabled under python -O."""
    if not condition:
        raise ArithmeticError(message)


def floor_scaled(value: Fraction, scale: int) -> int:
    return value.numerator * scale // value.denominator


def ceil_scaled(value: Fraction, scale: int) -> int:
    return -floor_scaled(-value, scale)


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        require(self.lo <= self.hi, "Reversed rational interval.")

    @classmethod
    def point(cls, value: Fraction | int) -> Interval:
        value = Fraction(value)
        return cls(value, value)

    @classmethod
    def outward(cls, lo: Fraction, hi: Fraction) -> Interval:
        return cls(Fraction(floor_scaled(lo, SCALE), SCALE),
                   Fraction(ceil_scaled(hi, SCALE), SCALE))

    @staticmethod
    def cast(value: Interval | Fraction | int) -> Interval:
        return value if isinstance(value, Interval) else Interval.point(value)

    def __add__(self, other: Interval | Fraction | int) -> Interval:
        other = self.cast(other)
        return self.outward(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self) -> Interval:
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: Interval | Fraction | int) -> Interval:
        return self + -self.cast(other)

    def __rsub__(self, other: Interval | Fraction | int) -> Interval:
        return self.cast(other) - self

    def __mul__(self, other: Interval | Fraction | int) -> Interval:
        other = self.cast(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return self.outward(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other: Interval | Fraction | int) -> Interval:
        other = self.cast(other)
        require(other.hi < 0 or other.lo > 0,
                "Interval denominator contains zero.")
        reciprocal = self.outward(1 / other.hi, 1 / other.lo)
        return self * reciprocal

    def __rtruediv__(self, other: Interval | Fraction | int) -> Interval:
        return self.cast(other) / self


def sqrt_interval(value: Interval) -> Interval:
    """Integer square roots enclose both rational endpoints exactly."""
    require(value.lo >= 0, "Square-root interval includes negative values.")
    scale = 10 ** SQRT_DIGITS

    def floor_root(endpoint: Fraction) -> int:
        return isqrt(endpoint.numerator * scale * scale // endpoint.denominator)

    lower = floor_root(value.lo)
    upper = floor_root(value.hi)
    if upper * upper * value.hi.denominator != value.hi.numerator * scale * scale:
        upper += 1
    return Interval(Fraction(lower, scale), Fraction(upper, scale))


def twice_atanh_series(t: Fraction) -> Interval:
    """Enclose 2*atanh(t), 0<=t<=1/3, with an explicit positive tail.

    After N terms the omitted sum is at most
        2*t**(2*N+1)/((2*N+1)*(1-t*t)).
    All intermediate rounding is outward at ARITHMETIC_DIGITS places.
    """
    require(0 <= t <= Fraction(1, 3), "Log series reduction is out of range.")
    argument = Interval.point(t)
    square = argument * argument
    power = argument
    total = Interval.point(0)
    for j in range(LOG_TERMS):
        total += power / (2 * j + 1)
        power *= square
    tail = 2 * power / ((2 * LOG_TERMS + 1) * (1 - square))
    partial = 2 * total
    return Interval.outward(partial.lo, partial.hi + tail.hi)


LN2 = twice_atanh_series(Fraction(1, 3))


@lru_cache(maxsize=None)
def log_rational(value: Fraction) -> Interval:
    """For value=2**m*a, 1<=a<2, use ln(a)+m*ln(2)."""
    require(value > 0, "Logarithm argument must be positive.")
    reduced = value
    exponent = 0
    while reduced < 1:
        reduced *= 2
        exponent -= 1
    while reduced >= 2:
        reduced /= 2
        exponent += 1
    t = (reduced - 1) / (reduced + 1)
    return twice_atanh_series(t) + exponent * LN2


def log_interval(value: Interval) -> Interval:
    require(value.lo > 0, "Logarithm interval includes nonpositive values.")
    return Interval(log_rational(value.lo).lo, log_rational(value.hi).hi)


def binary_entropy(probability: Interval) -> Interval:
    require(0 < probability.lo <= probability.hi < 1,
            "Entropy certificate requires an interior probability.")
    return -(probability * log_interval(probability)
             + (1 - probability) * log_interval(1 - probability)) / LN2


def profile_data(v: Interval, x: Fraction) -> dict[str, Interval]:
    s = sqrt_interval(1 - v * v)
    f = binary_entropy((1 - s) / 2)
    atanh_s = (log_interval(1 + s) - log_interval(1 - s)) / 2
    b = v * atanh_s / (s * LN2)
    k = v - f / b
    u = (1 - k * k) / (1 + k * k)
    w = 2 * k / (1 + k * k)
    p = (x - u) / (1 - u)
    z_x = p * v + (1 - p) * w
    return dict(v=v, f=f, b=b, k=k, u=u, w=w, p=p,
                z_x=z_x, cost=p * f)


def decimal_integer(integer: int, digits: int) -> str:
    sign = "-" if integer < 0 else ""
    absolute = abs(integer)
    scale = 10 ** digits
    return f"{sign}{absolute // scale}.{absolute % scale:0{digits}d}"


def decimal_enclosure(value: Interval, digits: int = OUTPUT_DIGITS) -> list[str]:
    """Decimal strings are rational, outward-rounded endpoints."""
    scale = 10 ** digits
    return [decimal_integer(floor_scaled(value.lo, scale), digits),
            decimal_integer(ceil_scaled(value.hi, scale), digits)]


def certificate() -> dict:
    x, z = Fraction(99, 100), Fraction(1, 2)
    v_lo = Fraction("0.52576013296870")
    v_hi = Fraction("0.52576013296872")
    require(0 < z <= x < 1 and x * x + z * z > 1,
            "Profile must lie outside the compatibility disk.")
    threshold = 2 * (1 / LN2 - 1) * (1 / LN2 - 1)
    require((1 - x) / (1 - z) < threshold.lo,
            "Profile is not certified inside the strict-saving wedge.")

    lower = profile_data(Interval.point(v_lo), x)
    upper = profile_data(Interval.point(v_hi), x)
    all_roots = profile_data(Interval(v_lo, v_hi), x)
    require(lower["z_x"].hi < z, "Lower endpoint does not have z_x(v)<z.")
    require(upper["z_x"].lo > z, "Upper endpoint does not have z_x(v)>z.")
    require(0 < all_roots["v"].lo <= all_roots["v"].hi < 1,
            "Root interval leaves the interior exact-axis branch.")
    require(0 < all_roots["k"].lo <= all_roots["k"].hi < 1,
            "Disk contact parameter is outside its physical domain.")
    require(0 < all_roots["u"].lo <= all_roots["u"].hi < x,
            "Disk contact must have u<x.")
    require(0 < all_roots["p"].lo <= all_roots["p"].hi < 1,
            "Mixture coefficient is not strictly between zero and one.")
    rate = all_roots["cost"]
    require(rate.hi - rate.lo < Fraction(1, 10 ** 11),
            "Certified rate interval is wider than 1e-11.")

    older_v = Interval.point(Fraction(15, 29))
    older_mix = Fraction(87, 100) * binary_entropy(
        (1 - sqrt_interval(1 - older_v * older_v)) / 2)
    require(rate.hi < older_mix.lo, "Optimizer is not certified to improve the earlier mixture.")
    saving = older_mix - rate

    return {
        "research_base": BASE,
        "status": "Exact rational interval certificate for one scalar optimizer, conditional on the analytical profile theorem.",
        "scope": "Product-diagonal profile rate C(99/100,1/2); not an unrestricted quantum-memory converse or novelty certificate.",
        "arithmetic": {
            "backend": "Python standard-library integers and fractions.Fraction; no floating-point arithmetic",
            "operation_rounding": "Outward to a fixed decimal lattice after each arithmetic operation",
            "arithmetic_decimal_places": ARITHMETIC_DIGITS,
            "sqrt_decimal_places": SQRT_DIGITS,
            "sqrt_method": "isqrt(floor(numerator*10**(2*digits)/denominator)), with exact upper endpoint check",
            "log_series_terms": LOG_TERMS,
            "log_method": "ln(r)=m*ln(2)+2*sum(t**(2*j+1)/(2*j+1)), r=2**m*a, 1<=a<2, t=(a-1)/(a+1)",
            "log_remainder_bound": "2*t**(2*N+1)/((2*N+1)*(1-t*t)); 0<=t<=1/3",
            "output_decimal_places": OUTPUT_DIGITS,
            "output_convention": "Every two-element decimal-string list is an outward rational enclosure.",
        },
        "profile": {"x": "99/100", "z": "1/2"},
        "ln2": decimal_enclosure(LN2),
        "strict_saving_phase_threshold": decimal_enclosure(threshold),
        "root": {
            "v": decimal_enclosure(Interval(v_lo, v_hi)),
            "z_x_at_lower_endpoint": decimal_enclosure(lower["z_x"]),
            "z_x_at_upper_endpoint": decimal_enclosure(upper["z_x"]),
            "lower_endpoint_gap": decimal_enclosure(z - lower["z_x"]),
            "upper_endpoint_gap": decimal_enclosure(upper["z_x"] - z),
            "existence_and_uniqueness_basis": "Strict endpoint signs plus continuity and strict monotonicity proved in the accompanying analytical optimizer theorem.",
        },
        "optimizer": {
            "exact_axis_point": {"x": "1", "z": decimal_enclosure(all_roots["v"])},
            "free_disk_point": {"x": decimal_enclosure(all_roots["u"]), "z": decimal_enclosure(all_roots["w"])},
            "exact_axis_weight": decimal_enclosure(all_roots["p"]),
            "rate": decimal_enclosure(rate),
            "rate_interval_width_upper": decimal_enclosure(Interval.point(rate.hi - rate.lo))[1],
        },
        "comparison": {
            "previous_explicit_mixture": "(87/100)*f(15/29)",
            "previous_mixture_rate": decimal_enclosure(older_mix),
            "strict_rate_saving": decimal_enclosure(saving),
        },
        "verified_checks": [
            "Profile is outside the compatibility disk and strictly inside the analytic saving wedge.",
            "z_x(v_lower)<1/2<z_x(v_upper) by disjoint rational intervals.",
            "All enclosed optimizer parameters lie in the physical interior, with 0<p<1 and u<x.",
            "Rate enclosure has width below 1e-11.",
            "Certified optimizer rate is strictly smaller than the previous explicit mixture rate.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = certificate()
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"PASS: wrote {args.output}")


if __name__ == "__main__":
    main()
