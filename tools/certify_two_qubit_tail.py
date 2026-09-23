#!/usr/bin/env python3
"""Exact rational certificate for TWO_QUBIT_SPECTRAL_TAIL_GATE.md.

This verifies the finite inequalities in the supplied analytical proof, not
a sample of density matrices. Acceptance uses Fraction and integer arithmetic
only. Decimal margins are diagnostics. Checks remain enabled with python -O.
No external packages, network access, or numerical optimizer are required.
"""

from fractions import Fraction as F
from math import isqrt


SCALE = 10**25
SERIES_TERMS = 40
CELLS = 400
LEFT, RIGHT = F(1, 29), F(9, 25)


def require(condition, label):
    if not condition:
        raise ArithmeticError(f"Certificate failed: {label}")


def sqrt_lower(x):
    """Rational lower enclosure of sqrt(x), for nonnegative Fraction x."""
    require(x >= 0, "square-root domain")
    k = isqrt((x.numerator * SCALE * SCALE) // x.denominator)
    return F(k, SCALE)


def sqrt_upper(x):
    """Rational upper enclosure with the same denominator as sqrt_lower."""
    require(x >= 0, "square-root domain")
    n, d = x.numerator, x.denominator
    k = isqrt((n * SCALE * SCALE) // d)
    if k * k * d < n * SCALE * SCALE:
        k += 1
    return F(k, SCALE)


# ln(2) = 2 atanh(1/3); a finite positive series is a strict lower bound.
LN2_LOWER = 2 * sum(
    (F(1, (2 * j + 1) * 3 ** (2 * j + 1)) for j in range(24)), F(0)
)
C_UPPER = 2 - sqrt_lower(F(2))


def ratio_upper(u):
    """Upper bound for [1-h_2((1+u)/2)]/u^2, continuous at u=0.

    The positive entropy series has total coefficient mass ln(2).
    Replace every omitted power by u^(2N), then use LN2_LOWER on
    the remaining nonnegative sum. See report Eq. (12).
    """
    require(0 <= u <= 1, "entropy-ratio domain")
    tail = u ** (2 * SERIES_TERMS)
    correction = sum(
        (
            (u ** (2 * k - 2) - tail) / (2 * k * (2 * k - 1))
            for k in range(1, SERIES_TERMS + 1)
        ),
        F(0),
    )
    return tail + correction / LN2_LOWER


def main():
    require(0 < LEFT < RIGHT < F(1, 2), "partition domain")
    # c*sqrt(3)>1: its squared inequality is 17>12*sqrt(2).
    require(17**2 > 12**2 * 2, "alpha exceeds one")
    min_det = min_a = min_bk = None
    previous_hi = LEFT
    for j in range(CELLS):
        lo = LEFT + (RIGHT - LEFT) * F(j, CELLS)
        hi = LEFT + (RIGHT - LEFT) * F(j + 1, CELLS)
        require(lo == previous_hi and lo < hi, f"cell {j}: coverage")
        t_max = (1 - 2 * lo) / (1 - lo)
        alpha = C_UPPER * sqrt_upper(3 + 4 * hi - 4 * hi * hi)
        a = (1 - hi) * (1 - alpha * ratio_upper(t_max))
        b = hi * (1 - alpha)
        k = 4 * lo * lo * (1 - lo) * (1 - lo)
        determinant = a * b + k * (a + b)
        require(alpha > 1, f"cell {j}: alpha upper bound")
        require(a >= 0, f"cell {j}: A lower bound")
        require(b + k >= 0, f"cell {j}: second principal minor")
        require(determinant >= 0, f"cell {j}: determinant")
        min_det = determinant if min_det is None else min(min_det, determinant)
        min_a = a if min_a is None else min(min_a, a)
        min_bk = b + k if min_bk is None else min(min_bk, b + k)
        previous_hi = hi
    require(previous_hi == RIGHT, "partition endpoint")

    # The report proves the balanced expression increases with x.
    x = F(27, 29)
    balanced_margin = 2 - C_UPPER * ratio_upper(x) * (
        2 + sqrt_upper(4 - x * x)
    )
    require(balanced_margin > 0, "balanced-spectrum endpoint")

    # For epsilon >= 9/25, ordering bounds both imbalance parameters by 7/9.
    require(3**12 > 2**19, "log_2(3) > 19/12")
    far_margin = 1 - 2 * C_UPPER * F(81, 98)
    require(far_margin > 0, "high-tail entropy ratio")

    # All acceptance decisions above were exact; these floats only aid review.
    print(f"PASS: {CELLS} rational interval certificates on [{LEFT}, {RIGHT}]")
    print(f"minimum determinant (display only): {float(min_det):.17g}")
    print(f"minimum A (display only): {float(min_a):.17g}")
    print(f"minimum B+K (display only): {float(min_bk):.17g}")
    print(f"balanced margin (display only): {float(balanced_margin):.17g}")
    print(f"high-tail margin (display only): {float(far_margin):.17g}")
    print("Certified scope: all ordered spectra with lambda_3+lambda_4 >= 1/29")


if __name__ == "__main__":
    main()
