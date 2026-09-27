#!/usr/bin/env python3
"""Exact Bernstein certificate for the nonflat quarter-rank converse.

Uses only integer/rational arithmetic. Radical intervals enclose polynomial
coefficients; no sampled values, optimizer, or floating-point sign test is used.
See docs/audits/NONFLAT_QUARTER_RANK_CONVERSE.md for the analytical reduction.
"""

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, isqrt
from pathlib import Path


RESEARCH_BASE = "c8b2e88d6721cb9208c797788f334d7f8b1e1848"
PROOF_RELATIVE_PATH = "docs/audits/NONFLAT_QUARTER_RANK_CONVERSE.md"
SOURCE_PATH = Path(__file__).resolve()
PROOF_PATH = SOURCE_PATH.parents[1] / PROOF_RELATIVE_PATH


class Interval:
    """Closed rational interval, with outward bounds exact by construction."""

    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = as_interval(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-as_interval(other))

    def __mul__(self, other):
        other = as_interval(other)
        products = [a * b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return Interval(min(products), max(products))

    __rmul__ = __mul__


def as_interval(value):
    return value if isinstance(value, Interval) else Interval(value)


class Polynomial:
    """Sparse polynomials in (w,m), with rational interval coefficients."""

    def __init__(self, coefficients):
        self.coefficients = {power: as_interval(value)
                             for power, value in coefficients.items()}

    def __add__(self, other):
        other = as_polynomial(other)
        result = dict(self.coefficients)
        for power, value in other.coefficients.items():
            result[power] = result.get(power, Interval(0)) + value
        return Polynomial(result)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({p: -v for p, v in self.coefficients.items()})

    def __sub__(self, other):
        return self + (-as_polynomial(other))

    def __rsub__(self, other):
        return as_polynomial(other) - self

    def __mul__(self, other):
        other = as_polynomial(other)
        result = {}
        for (i, j), value in self.coefficients.items():
            for (k, ell), factor in other.coefficients.items():
                power = (i + k, j + ell)
                result[power] = result.get(power, Interval(0)) + value * factor
        return Polynomial(result)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        result = as_polynomial(1)
        for _ in range(exponent):
            result = result * self
        return result


def as_polynomial(value):
    return value if isinstance(value, Polynomial) else Polynomial({(0, 0): value})


def radical_interval(integer):
    denominator = 10 ** 18
    numerator = isqrt(integer * denominator ** 2)
    assert numerator ** 2 < integer * denominator ** 2 < (numerator + 1) ** 2
    return Interval(F(numerator, denominator), F(numerator + 1, denominator))


def bernstein_certificate(polynomial, degree, threshold):
    """Convert power coefficients to tensor Bernstein coefficients on the box.

    b_ij = sum_{k<=i,l<=j} c_kl (9/25)^(k+l)
           * binom(i,k)/binom(n,k) * binom(j,l)/binom(p,l).
    Bernstein basis functions are nonnegative and sum to one.
    """
    n, p = degree
    width = F(9, 25)
    assert all(k <= n and ell <= p for k, ell in polynomial.coefficients)
    coefficients = []
    lower_bound_numerators = []
    for i in range(n + 1):
        row = []
        for j in range(p + 1):
            value = Interval(0)
            for (k, ell), coefficient in polynomial.coefficients.items():
                if k <= i and ell <= j:
                    weight = (width ** (k + ell) * F(comb(i, k), comb(n, k))
                              * F(comb(j, ell), comb(p, ell)))
                    value = value + coefficient * weight
            assert value.lo > threshold, (degree, i, j, value.lo, threshold)
            coefficients.append((value.lo, i, j))
            scaled = value.lo * 10 ** 6
            row.append(scaled.numerator // scaled.denominator)
        lower_bound_numerators.append(row)
    _, i, j = min(coefficients)
    return {"degree": list(degree), "coefficient_count": len(coefficients),
            "strict_lower_bound": str(threshold), "minimum_index": [i, j],
            "coefficient_lower_bound_denominator": 10 ** 6,
            "coefficient_lower_bound_numerators": lower_bound_numerators}


def run():
    w = Polynomial({(1, 0): 1})
    m = Polynomial({(0, 1): 1})
    r2 = as_polynomial(radical_interval(2))
    r3 = as_polynomial(radical_interval(3))
    d = 1 + w ** 2
    h = 1 + r3 * w
    lam = F(2, 3) * (r2 - 1)
    t = 2 * m * (r2 * w + m)
    z = (F(4, 3) * r2 * d - 1) * d - lam * t * (d - t)
    q = h * (3 + m) * d - d - z
    a = 2 * h * (2 * z - (1 - m) * d) - q
    c = 2 * h * (2 * z - (1 - m) * d) - d * q
    p = a ** 2 - w ** 2 * (4 * h ** 2 *
                           (2 * z * d - (1 - m) ** 2 * d ** 2) - q ** 2)
    checks = {
        "C": bernstein_certificate(c, (6, 4), F(4, 25)),
        "P": bernstein_certificate(p, (10, 8), F(1, 10000)),
    }
    # Exact witnesses for the two enlarged-box comparisons.
    assert 2 * 2824 ** 2 - 3993 ** 2 == 5903
    assert 2 * 625 ** 2 - 881 ** 2 == 5089
    return {"status": "passed", "arithmetic": "exact rational intervals",
            "research_base": RESEARCH_BASE,
            "proof_note": PROOF_RELATIVE_PATH,
            "proof_note_sha256": hashlib.sha256(PROOF_PATH.read_bytes()).hexdigest(),
            "box": {"w": ["0", "9/25"], "m": ["0", "9/25"]},
            "subdivisions": 0, "radical_denominator": 10 ** 18,
            "radical_enclosures": {str(n): [str(radical_interval(n).lo),
                                            str(radical_interval(n).hi)]
                                     for n in (2, 3)},
            "total_bernstein_coefficients": sum(v["coefficient_count"]
                                                for v in checks.values()),
            "certificates": checks,
            "source_sha256": hashlib.sha256(SOURCE_PATH.read_bytes()).hexdigest(),
            "scope": "Exact scalar positivity certificate; analytical reduction is in the proof note."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        if args.output.suffix.lower() != ".json":
            parser.error("--output must have a .json suffix")
        if args.output.resolve() in (SOURCE_PATH, PROOF_PATH.resolve()):
            parser.error("--output must not overwrite the checker or proof note")
    output = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
