#!/usr/bin/env python3
"""Identity checks for the sharp-pair normal form, not an optimum certificate.

The relaxation obstruction uses exact rational arithmetic in Q(sqrt(2)).
The normal-form diagnostics use fixed, small matrices and no optimizer.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import numpy as np

I = np.eye(2, dtype=complex)
P = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]], dtype=complex)
I4 = np.eye(4, dtype=complex)
TOL = 2e-10


def require(condition, message):
    if not condition:
        raise AssertionError(message)


class Q2:
    """Exact a+b sqrt(2), sufficient for the algebraic obstruction."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def cast(value):
        return value if isinstance(value, Q2) else Q2(value)

    def __add__(self, other):
        o = self.cast(other)
        return Q2(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) + -self

    def __mul__(self, other):
        o = self.cast(other)
        return Q2(self.a * o.a + 2 * self.b * o.b,
                  self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self.cast(other)
        den = o.a * o.a - 2 * o.b * o.b
        if not den:
            raise ZeroDivisionError
        return self * Q2(o.a / den, -o.b / den)

    def __eq__(self, other):
        o = self.cast(other)
        return self.a == o.a and self.b == o.b

    def positive(self):
        if self.b == 0:
            return self.a > 0
        if self.a >= 0 and self.b > 0:
            return True
        if self.a <= 0 and self.b < 0:
            return False
        if self.a > 0:
            return self.a * self.a > 2 * self.b * self.b
        return 2 * self.b * self.b > self.a * self.a

    def approximate(self):
        return float(self.a) + float(self.b) * np.sqrt(2)


def exact_obstruction():
    r = Q2(0, 1)
    u, m = Q2(F(7, 2)), Q2(F(1, 2), 2)
    t, c = 4 + r - m, u - m
    require((m - 2).positive() and c.positive() and (4 - u).positive(), "Spectral range")
    require(u + m == 4 + 2 * r and c == 2 * (t - 2), "Spectral identities")
    require((t - 2).positive(), "Positive resolvent denominator")
    lam = [F(29, 60), F(29, 60), F(1, 60), F(1, 60)]
    k = lambda x, y: (x-y)**2/(x+y) if x+y else F(0)
    e = k(lam[0], lam[1])+k(lam[0], lam[2])+k(lam[1], lam[3])+k(lam[2], lam[3])
    require(sum(lam) == 1 and min(lam) > 0 and e == F(196, 225), "Full-rank SLD data")
    require(e < F(15, 16) and e < F(29, 32), "Both necessary SLD constraints")
    require(F(4*127, 225) > F(9, 4), "Exact fixed-spectrum score bound admits U=7/2")
    f, g = (t-1)/(t*(t-2)), (t+1)/(t*(t+2))
    witness = c * (2 * lam[0] * f + 2 * lam[3] * g)
    excess = (Q2(587, -412))/(60*t*(t+2))
    require(witness - 1 == excess and excess.positive(), "Exact failing resolvent witness")
    require(587**2 - 2*412**2 == 5081, "Strict surd comparison")
    return {"e_star": str(e), "spectrum": [str(x) for x in lam],
            "exact_excess": "(587-412*sqrt(2))/(60*t*(t+2)); t=7/2-sqrt(2)",
            "witness_approximation": witness.approximate(),
            "status": "synthetic relaxation data; no Hamiltonian realization supplied"}


def kron(*args):
    out = np.array([[1]], dtype=complex)
    for a in args:
        out = np.kron(out, a)
    return out


def su2(rng):
    x = rng.normal(size=4)
    x /= np.linalg.norm(x)
    return x[0]*I + 1j*np.einsum("a,aij->ij", x[1:], P)


def cartan(angles):
    d = I4.copy()
    for theta, p in zip(angles, P):
        d = d @ (np.cos(theta)*I4 + 1j*np.sin(theta)*kron(p, p))
    return d


def bloch(matrix):
    return np.array([np.trace(p@matrix).real/2 for p in P])


def memory_marginal(vector):
    v = vector.reshape(4, 4)
    return v.T @ v.conj()


def normal_form(angles, n1, n2):
    d = cartan(angles)
    h = np.zeros((16, 16), dtype=complex)
    for i, n in enumerate([n1, n2]):
        coeff = np.eye(3) - np.outer(n, n)
        for a in range(3):
            for b in range(3):
                memory = kron(P[b], I)
                if i:
                    memory = d @ memory @ d.conj().T
                reference = kron(P[a], I) if i == 0 else kron(I, P[a])
                h += coeff[a, b] * kron(reference, memory)
    return h


def pauli_expansion(angles):
    co, si = np.cos(2*angles), np.sin(2*angles)
    out = []
    for j, k, l in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        out.append(co[k]*co[l]*kron(P[j], I) + si[k]*si[l]*kron(I, P[j])
                   + si[k]*co[l]*kron(P[l], P[k]) - co[k]*si[l]*kron(P[k], P[l]))
    return out


def run_checks():
    rng = np.random.default_rng(20260924)
    residuals = {}

    def check(label, a, b):
        err = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
        residuals[label] = max(residuals.get(label, 0), err)
        require(err < TOL, f"{label}: {err}")

    # Include commuting, SWAP, identity, and angle-boundary cases.
    angle_cases = [np.zeros(3), np.full(3, np.pi/4), np.array([np.pi/2, 0, -np.pi/2]),
                   np.array([0, np.pi/4, 0])]
    angle_cases += [rng.uniform(-np.pi/2, np.pi/2, 3) for _ in range(36)]
    marginal_cases = 0
    for angles in angle_cases:
        a, b, c, e = [su2(rng) for _ in range(4)]
        d = cartan(angles)
        left, right = kron(a, b), kron(c, e)
        unitary = left @ d @ right
        h0 = sum(kron(p, I, p, I) + kron(I, p, unitary@kron(p, I)@unitary.conj().T)
                 for p in [P[0], P[2]])
        n1, n2 = bloch(a.conj().T@P[1]@a), bloch(c@P[1]@c.conj().T)
        h = normal_form(angles, n1, n2)
        transform = kron(a.conj().T, c, left.conj().T)
        check("normal_form_unitary_equivalence", h, transform@h0@transform.conj().T)
        for j, expansion in enumerate(pauli_expansion(angles)):
            check("cartan_pauli_expansion", expansion, d@kron(P[j], I)@d.conj().T)
        for j in range(3):
            shifted = angles.copy()
            shifted[j] += np.pi
            check("angle_periodicity", normal_form(shifted, n1, n2), h)
        y1, y2 = [np.einsum("a,aij->ij", n, P) for n in [n1, n2]]
        gamma = kron(y1, y2, I4)
        check("chiral_anticommutator", gamma@h+h@gamma, 0)
        _, v1 = np.linalg.eigh(y1)
        _, v2 = np.linalg.eigh(y2)
        plus_r = np.column_stack([kron(v1[:, 0:1], v2[:, 0:1]).ravel(),
                                  kron(v1[:, 1:2], v2[:, 1:2]).ravel()])
        minus_r = np.column_stack([kron(v1[:, 0:1], v2[:, 1:2]).ravel(),
                                   kron(v1[:, 1:2], v2[:, 0:1]).ravel()])
        ep, em = kron(plus_r, I4), kron(minus_r, I4)
        fmat = ep.conj().T@h@em
        lu, singular, rvh = np.linalg.svd(fmat)
        values, vectors = np.linalg.eigh(h)
        check("full_spectrum_from_singular_values", values, np.sort(np.r_[-singular, singular]))
        u, v = ep@lu[:, 0], em@rvh.conj().T[:, 0]
        omega = (u+v)/np.sqrt(2)
        check("reconstructed_eigenvector", h@omega, singular[0]*omega)
        cross = u.reshape(4, 4).T@v.reshape(4, 4).conj()
        check("cross_partial_trace", cross, 0)
        rho = (memory_marginal(u)+memory_marginal(v))/2
        check("marginal_reconstruction", rho, memory_marginal(omega))
        if singular[0]-singular[1] > 1e-8:
            marginal_cases += 1
            check("top_marginal_direct_diagonalization", rho, memory_marginal(vectors[:, -1]))
            _, orig_vectors = np.linalg.eigh(h0)
            check("original_marginal_spectrum", np.linalg.eigvalsh(rho),
                  np.linalg.eigvalsh(memory_marginal(orig_vectors[:, -1])))
    # An exact Pauli construction saturates the known U+m spectral bound.
    h = (kron(P[0], I, P[0], I) + kron(P[2], I, P[2], I)
         + kron(I, P[0], I, P[2]) + kron(I, P[2], P[0], P[0]))
    target = sorted([a+b+c*np.sqrt(2) for a in [-1, 1] for b in [-1, 1]
                     for c in [-1, 1] for _ in range(2)])
    check("physical_spectral_sum_saturation", np.linalg.eigvalsh(h), target)
    return {"normal_form_cases": len(angle_cases), "simple_top_marginal_cases": marginal_cases,
            "max_residuals": residuals, "tolerance": TOL,
            "status": "finite identity diagnostics; no global inequality certificate"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "environment": {"python": platform.python_version(), "numpy": np.__version__},
              "exact_obstruction": exact_obstruction(), "identities": run_checks()}
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
