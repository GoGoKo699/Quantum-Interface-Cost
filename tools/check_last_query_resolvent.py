#!/usr/bin/env python3
"""Small deterministic checks for exact elimination of the last binary readout.

This supplements a supplied proof. It is not a global interface certificate.
No optimizer is used: each scalar support value is approximated by monotone
bisection in its bound K, whose exact decision uses one convex quartic.
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
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
R = float(np.sqrt(2))
TOL = 2e-9


def fg(t: float, a: float) -> tuple[float, float]:
    b2 = max(0.0, 2 - a * a)
    return ((t - a) / ((t - a) ** 2 - b2),
            (t + a) / ((t + a) ** 2 - b2))


def poly(t: float, x: float, y: float, bound: float, a: float) -> float:
    w, delta = x + y, x - y
    return (4 * bound * a**4 + 2 * delta * a**3 - 8 * bound * a*a
            - delta * (t*t + 2) * a + bound * (t*t - 2)**2
            - w * t * (t*t - 2))


def minimum(t: float, x: float, y: float, bound: float) -> tuple[float, float, str]:
    """Evaluate the unique clipped cubic point; zero case is separate."""
    delta = x - y
    if x == y == bound == 0:
        return 0.0, 1.0, "zero"
    if bound <= 0:
        raise ValueError("A positive bound is needed for a nonzero pair")
    if delta == 0:
        return poly(t, x, y, bound, 1.0), 1.0, "left"

    def derivative(a: float) -> float:
        return (16 * bound * a**3 + 6 * delta * a*a - 16 * bound * a
                - delta * (t*t + 2))

    if derivative(R) <= 0:
        return poly(t, x, y, bound, R), R, "right"
    lo, hi = 1.0, R
    for _ in range(70):
        mid = (lo + hi) / 2
        if derivative(mid) <= 0:
            lo = mid
        else:
            hi = mid
    a = (lo + hi) / 2
    return poly(t, x, y, bound, a), a, "interior"


def support(t: float, x: float, y: float) -> tuple[float, float | None, str]:
    if x < y:
        x, y = y, x
    if x + y == 0:
        return 0.0, None, "zero"
    baseline = (x + y) / (t - R)
    p0, _, _ = minimum(t, x, y, baseline)
    if p0 >= -1e-13:
        return baseline, None, "scalar"
    lo, hi = baseline, (x + y) / (t - 2)
    for _ in range(75):
        mid = (lo + hi) / 2
        if minimum(t, x, y, mid)[0] >= 0:
            hi = mid
        else:
            lo = mid
    _, a, _ = minimum(t, x, y, hi)
    f, g = fg(t, a)
    actual = x * f + y * g
    if abs(actual - hi) > TOL:
        raise AssertionError("Support bisection and attaining angle disagree")
    return actual, a, "block"


def complex_unitary(dim: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    return q @ np.diag(phases / np.abs(phases))


def weighted_resolvent(t: float, rho: np.ndarray, b: np.ndarray,
                        d: np.ndarray) -> np.ndarray:
    dim = len(rho)
    h = np.kron(X, b) + np.kron(Z, d)
    resolvent = np.linalg.inv(t * np.eye(2 * dim) - h).reshape(2, dim, 2, dim)
    return np.einsum("qp,rpsq->rs", rho, resolvent)


def main(output: Path) -> None:
    if not __debug__:
        raise RuntimeError("Run this verifier without -O or -OO")
    if output.resolve() == Path(__file__).resolve():
        raise ValueError("--output must not overwrite this verifier source")
    rng = np.random.default_rng(2026092507)
    counts = {"exact_inverse_identity_cases": 0, "exact_quartic_identity_cases": 0,
              "jordan_identity_cases": 0, "quartic_identity_cases": 0,
              "attainment_cases": 0, "pairing_cases": 0,
              "cap_cases": 0, "scalar_pairs": 0, "block_pairs": 0,
              "zero_pairs": 0, "clipped_right_cases": 0,
              "interior_cubic_cases": 0, "contraction_convexity_cases": 0}
    errors = {"jordan_inverse": 0.0, "quartic_identity": 0.0,
              "attainment": 0.0, "hermiticity": 0.0,
              "reflection": 0.0, "cubic_stationarity": 0.0,
              "support_boundary": 0.0}
    margins = {"pairing": float("inf"),
               "contraction_convexity": float("inf")}
    parameters = []
    chi = np.linalg.eigh((X + Z) / R)[1][:, -1]

    # Exact rational identities are separate from all floating diagnostics.
    F = Fraction

    def kron_exact(a, b):
        return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])]
                 for j in range(len(a[0]) * len(b[0]))]
                for i in range(len(a) * len(b))]

    def linear_exact(terms):
        return [[sum(coef * matrix[i][j] for coef, matrix in terms)
                 for j in range(4)] for i in range(4)]

    def multiply_exact(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(4))
                 for j in range(4)] for i in range(4)]

    ie = [[F(int(i == j)) for j in range(4)] for i in range(4)]
    xe, ze = [[F(0), F(1)], [F(1), F(0)]], [[F(1), F(0)], [F(0), F(-1)]]
    je = [[F(0), F(-1)], [F(1), F(0)]]
    xx, zz = kron_exact(xe, xe), kron_exact(ze, ze)
    yy = [[-entry for entry in row] for row in kron_exact(je, je)]
    for te in (F(21, 10), F(13, 5), F(9, 2)):
        for ae, be in ((F(1), F(1)), (F(119, 101), F(79, 101))):
            assert ae*ae+be*be == 2
            se = te*te-2
            determinant = se*se-4*ae*ae*be*be
            denominator = linear_exact([(te, ie), (-ae, zz), (-be, xx)])
            numerator = linear_exact([(te*se, ie), (ae*(se+2*be*be), zz),
                                      (be*(se+2*ae*ae), xx), (-2*te*ae*be, yy)])
            assert multiply_exact(denominator, numerator) == linear_exact([(determinant, ie)])
            counts["exact_inverse_identity_cases"] += 1
            for xw, yw in ((F(7, 10), F(1, 10)), (F(1, 4), F(1, 4)),
                           (F(2, 5), F(0)), (F(0), F(0))):
                ke = xw+yw+F(1, 10)
                fe = (te-ae)/((te-ae)**2-be*be)
                ge = (te+ae)/((te+ae)**2-be*be)
                assert poly(te, xw, yw, ke, ae) == determinant*(ke-xw*fe-yw*ge)
                counts["exact_quartic_identity_cases"] += 1

    # Direct inverse identities, including unequal coefficients and endpoints.
    probe = np.array([np.sqrt(.31), np.exp(.37j) * np.sqrt(.69)])
    bloch = [float(np.vdot(probe, p @ probe).real) for p in (Z, X, Y)]
    for t in (2.05, 2.6, 2 + R, 4.5):
        for a in (1.0, 1.13, 1.31, R):
            b = np.sqrt(max(0.0, 2 - a*a))
            h = a * np.kron(Z, Z) + b * np.kron(X, X)
            inv = np.linalg.inv(t * np.eye(4) - h).reshape(2, 2, 2, 2)
            actual = np.einsum("r,rpsq,s->pq", probe.conj(), inv, probe)
            s, det = t*t - 2, (t*t - 2)**2 - 4 * a*a * b*b
            z, x, y = bloch
            expected = (t*s*I2 + z*a*(s+2*b*b)*Z
                        + x*b*(s+2*a*a)*X - y*2*t*a*b*Y) / det
            errors["jordan_inverse"] = max(errors["jordan_inverse"],
                                           float(np.linalg.norm(actual - expected)))
            counts["jordan_identity_cases"] += 1
            for xw, yw in ((.7, .1), (.25, .25), (.4, 0), (0, 0)):
                k = (xw + yw) / (t - R) + .1
                f, g = fg(t, a)
                error = abs(poly(t, xw, yw, k, a) - det * (k - xw*f - yw*g))
                errors["quartic_identity"] = max(errors["quartic_identity"], error)
                counts["quartic_identity_cases"] += 1

    for dim in (2, 4, 6, 8):
        spectra = [np.ones(dim) / dim,
                   .47 ** np.arange(dim),
                   np.r_[1.0, np.zeros(dim - 1)],
                   np.r_[np.arange(dim, 2, -1, dtype=float), 0.0, 0.0]]
        if dim == 2:
            spectra[-1] = np.array([.83, .17])
        spectra = [s / s.sum() for s in spectra]
        for spectrum_id, lam in enumerate(spectra):
            for t in (2.05, 2.6, 2 + R, 4.5):
                b0, d0 = np.zeros((dim, dim), complex), np.zeros((dim, dim), complex)
                total, local = 0.0, []
                for j in range(dim // 2):
                    indices = (j, dim - 1 - j)
                    x, y = float(lam[indices[0]]), float(lam[indices[1]])
                    value, a, kind = support(t, x, y)
                    total += value
                    counts[kind + "_pairs"] += 1
                    if kind == "block":
                        bb = np.sqrt(max(0.0, 2 - a*a))
                        bp, dp = (a * Z + bb * X) / R, (a * Z - bb * X) / R
                    else:
                        bp = dp = I2
                    b0[np.ix_(indices, indices)] = bp
                    d0[np.ix_(indices, indices)] = dp
                    baseline = (x+y) / (t-R)
                    pmin, amin, where = minimum(t, x, y, baseline) if x+y else (0., 1., "zero")
                    if where == "right":
                        counts["clipped_right_cases"] += 1
                    if where == "interior":
                        counts["interior_cubic_cases"] += 1
                        derivative = (16*baseline*amin**3 + 6*(x-y)*amin*amin
                                      -16*baseline*amin-(x-y)*(t*t+2))
                        errors["cubic_stationarity"] = max(errors["cubic_stationarity"], abs(derivative))
                    if x+y:
                        p_at_bound = minimum(t, x, y, value)[0]
                        errors["support_boundary"] = max(errors["support_boundary"], max(0., -p_at_bound))
                    local.append({"weights": [x, y], "kind": kind, "a": a})
                unitary = complex_unitary(dim, rng)
                rho = (unitary * lam) @ unitary.conj().T
                b, d = unitary @ b0 @ unitary.conj().T, unitary @ d0 @ unitary.conj().T
                resolvent = weighted_resolvent(t, rho, b, d)
                attained = float(np.linalg.eigvalsh(resolvent)[-1])
                chi_value = float(np.vdot(chi, resolvent @ chi).real)
                errors["attainment"] = max(errors["attainment"], abs(attained-total), abs(chi_value-total))
                errors["hermiticity"] = max(errors["hermiticity"], float(np.linalg.norm(resolvent-resolvent.conj().T)))
                errors["reflection"] = max(errors["reflection"], float(np.linalg.norm(b@b-np.eye(dim))), float(np.linalg.norm(d@d-np.eye(dim))))
                counts["attainment_cases"] += 1
                parameters.append({"dimension": dim, "spectrum": spectrum_id, "t": t,
                                   "value": total, "pairs": local})

                # Compare every matching in dimensions at most eight (105 at D=8).
                def matchings(indices):
                    if not indices:
                        yield []
                        return
                    first = indices[0]
                    for n in range(1, len(indices)):
                        second = indices[n]
                        remaining = indices[1:n] + indices[n+1:]
                        for rest in matchings(remaining):
                            yield [(first, second)] + rest
                cache = {(i, j): support(t, float(lam[i]), float(lam[j]))[0]
                         for i in range(dim) for j in range(i+1, dim)}
                for pairs in matchings(list(range(dim))):
                    alternative = sum(cache[(i, j)] for i, j in pairs)
                    margins["pairing"] = min(margins["pairing"], total - alternative)
                    counts["pairing_cases"] += 1

                # Direct convexity check with contractions in the same dimension.
                b_alt = unitary @ np.diag(np.where(np.arange(dim) % 2, -1, 1)) @ unitary.conj().T
                d_alt = unitary @ np.diag(np.where(np.arange(dim) % 3, -1, 1)) @ unitary.conj().T
                fraction = .37
                mixed = weighted_resolvent(t, rho, fraction*b+(1-fraction)*b_alt, d)
                upper = fraction*resolvent+(1-fraction)*weighted_resolvent(t, rho, b_alt, d)
                margins["contraction_convexity"] = min(margins["contraction_convexity"], float(np.linalg.eigvalsh(upper-mixed)[0]))
                # Also change D while holding a genuine contraction B fixed.
                bc = fraction*b+(1-fraction)*b_alt
                dc = fraction*d+(1-fraction)*d_alt
                mixed2 = weighted_resolvent(t, rho, bc, dc)
                upper2 = fraction*weighted_resolvent(t, rho, bc, d)+(1-fraction)*weighted_resolvent(t, rho, bc, d_alt)
                margins["contraction_convexity"] = min(margins["contraction_convexity"], float(np.linalg.eigvalsh(upper2-mixed2)[0]))
                counts["contraction_convexity_cases"] += 2

                # Explicit rank-one update, limited to four tiny cases.
                if dim in (2, 4) and spectrum_id == 1 and t == 2.6:
                    e = np.zeros((2*dim*dim, 2), dtype=complex)
                    for q in range(dim):
                        for rr in range(2):
                            e[(q*2+rr)*dim+q, rr] = np.sqrt(lam[q])
                    p = e @ e.conj().T
                    h = np.kron(X, b0) + np.kron(Z, d0)
                    for factor in (.9, 1.1):
                        c = factor / total
                        residual = t*np.eye(2*dim*dim)-np.kron(np.eye(dim), h)-c*p
                        mineig = float(np.linalg.eigvalsh(residual)[0])
                        if factor < 1 and mineig <= 0:
                            raise AssertionError("Expected passing rank-one cap")
                        if factor > 1 and mineig >= 0:
                            raise AssertionError("Expected failing rank-one cap")
                        counts["cap_cases"] += 1

    if max(errors.values()) > TOL:
        raise AssertionError(f"Identity residual exceeds tolerance: {errors}")
    if min(margins.values()) < -TOL:
        raise AssertionError(f"Comparison failed: {margins}")
    if not all(counts[key] for key in ("scalar_pairs", "block_pairs", "zero_pairs",
                                     "clipped_right_cases", "interior_cubic_cases")):
        raise AssertionError("Missing an intended endpoint/branch check")
    result = {"status": "passed", "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "python_version": platform.python_version(), "numpy_version": np.__version__,
              "seed": 2026092507, "tolerance": TOL, "exact_arithmetic": "fractions.Fraction", "counts": counts,
              "maximum_absolute_errors": errors, "minimum_comparison_margins": margins,
              "scope": "Exact rational identities and finite floating diagnostics supplement the supplied proof; floating bisection is not interval certification and no global interface optimum or novelty is certified.",
              "constructions": parameters}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "output": str(output), "counts": counts,
                      "maximum_error": max(errors.values()), "minimum_margin": min(margins.values())}, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    main(parser.parse_args().output)
