#!/usr/bin/env python3
"""Small deterministic matrix regressions; the written arguments are the proofs.

Tensor order is R1,R2,R3,A,B. No variational optimization or large simulation.
The script reconstructs every physical matrix independently from Pauli matrices.
"""
from __future__ import annotations

import argparse
import hashlib
import platform
import itertools
import json
from pathlib import Path

import numpy as np

SEED = 2026092409
TOL = 2e-9
RNG = np.random.default_rng(SEED)
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
R = np.sqrt(2.0)
TARGET = 4 + R
RES: dict[str, float] = {}
COUNTS: dict[str, int] = {}


def check(name, value):
    value = float(np.real(value))
    if not np.isfinite(value):
        raise ArithmeticError((name, value))
    RES[name] = max(RES.get(name, 0.0), max(0.0, value))
    if value > TOL:
        raise ArithmeticError((name, value))


def count(name):
    COUNTS[name] = COUNTS.get(name, 0) + 1


def embed(matrix, sites, n=5):
    """Direct computational-basis embedding; sites retain their listed order."""
    sites = tuple(sites)
    out = np.zeros((2**n, 2**n), dtype=complex)
    for col in range(2**n):
        bits = [(col >> (n - 1 - j)) & 1 for j in range(n)]
        subcol = sum(bits[j] << (len(sites) - 1 - k) for k, j in enumerate(sites))
        for subrow in range(2**len(sites)):
            rowbits = bits.copy()
            for k, j in enumerate(sites):
                rowbits[j] = (subrow >> (len(sites) - 1 - k)) & 1
            row = sum(bit << (n - 1 - j) for j, bit in enumerate(rowbits))
            out[row, col] = matrix[subrow, subcol]
    return out


def haar(d):
    raw = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
    q, rr = np.linalg.qr(raw)
    phases = np.diag(rr) / np.abs(np.diag(rr))
    return q @ np.diag(phases)


def reflection(rank):
    u = haar(4)
    return u @ np.diag([-1] * rank + [1] * (4 - rank)) @ u.conj().T


def contraction():
    u = haar(4)
    return u @ np.diag(RNG.uniform(-1, 1, size=4)) @ u.conj().T


def query(i, b, d, n=5):
    return embed(X, [i], n) @ embed(b, [n - 2, n - 1], n) + embed(Z, [i], n) @ embed(d, [n - 2, n - 1], n)


def lmax(a):
    check("hermiticity", np.linalg.norm(a - a.conj().T, ord=2))
    return float(np.linalg.eigvalsh(a)[-1])


def norm(a):
    ev = np.linalg.eigvalsh(a)
    return float(max(abs(ev[0]), abs(ev[-1])))


XA, ZA, XB, ZB, ZAYB = (np.kron(X, I2), np.kron(Z, I2), np.kron(I2, X), np.kron(I2, Z), np.kron(Z, Y))
SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
SINGLET = np.array([0, 1, -1, 0], dtype=complex) / R
SINGLET_P = np.outer(SINGLET, SINGLET.conj())


def two_cross_checks():
    angles = [
        (0., 0.), (np.pi/7, np.pi/9), (-np.pi/5, np.pi/6),
        (np.pi/4, np.pi/4), (-np.pi/4, np.pi/4),
        (np.pi/4, np.pi/12), (np.pi/12, -np.pi/4),
        (0., np.pi/7), (-np.pi/9, 0.),
        (.41, -.23), (-.11, -.32), (np.pi/4, 0.),
    ]
    third_types = list(itertools.product(range(3), repeat=2))
    xx, zz = np.kron(X, X), np.kron(Z, Z)
    for alpha, gamma in angles:
        u = (np.cos(alpha)*np.eye(4)+1j*np.sin(alpha)*xx) @ (np.cos(gamma)*np.eye(4)+1j*np.sin(gamma)*zz)
        half_u = (np.cos(alpha/2)*np.eye(4)+1j*np.sin(alpha/2)*xx) @ (np.cos(gamma/2)*np.eye(4)+1j*np.sin(gamma/2)*zz)
        pairs = [(XA, ZA), (u @ XB @ u.conj().T, u @ ZB @ u.conj().T)]
        common = haar(4)
        pairs = [(common @ b @ common.conj().T, common @ d @ common.conj().T) for b, d in pairs]
        for b, d in pairs:
            check("two_cross_sharp_pairs", max(np.linalg.norm(b @ b-np.eye(4)), np.linalg.norm(d @ d-np.eye(4)), np.linalg.norm(b @ d+d @ b)))
        check("two_cross_mixed_commutators", max(np.linalg.norm(pairs[0][0] @ pairs[1][1]-pairs[1][1] @ pairs[0][0]), np.linalg.norm(pairs[0][1] @ pairs[1][0]-pairs[1][0] @ pairs[0][1])))
        yy = common @ np.kron(Y, Y) @ common.conj().T
        check("two_cross_corresponding_commutators", max(np.linalg.norm(pairs[0][0] @ pairs[1][0]-pairs[1][0] @ pairs[0][0]-2j*np.sin(2*gamma)*yy), np.linalg.norm(pairs[0][1] @ pairs[1][1]-pairs[1][1] @ pairs[0][1]-2j*np.sin(2*alpha)*yy)))
        if abs(np.sin(2*alpha)*np.sin(2*gamma)) > 1e-7:
            count("two_cross_both_corresponding_commutators_nonzero")
        h0 = query(0, *pairs[0], n=4) + query(1, *pairs[1], n=4)
        expected = sorted(x+y for x in [2*np.cos(alpha), -2*np.cos(alpha), 2*np.sin(alpha), -2*np.sin(alpha)] for y in [2*np.cos(gamma), -2*np.cos(gamma), 2*np.sin(gamma), -2*np.sin(gamma)])
        ev = np.linalg.eigvalsh(h0)
        check("two_cross_full_spectrum", np.max(np.abs(ev-expected)))
        u1, v1 = 2*np.cos(alpha), 2*abs(np.sin(alpha))
        u2, v2 = 2*np.cos(gamma), 2*abs(np.sin(gamma))
        upper, c = u1+u2, min(u1-v1, u2-v2)
        second = upper-c
        omega = (common @ half_u).T.reshape(16)/2
        coefficient = omega.reshape(4, 4)
        check("two_cross_top_memory_flatness", np.linalg.norm(coefficient.conj().T @ coefficient-np.eye(4)/4, ord=2))
        check("two_cross_explicit_top_vector", np.linalg.norm(h0 @ omega-upper*omega))
        cap = second*np.eye(16)+c*np.outer(omega, omega.conj())
        check("two_cross_full_spectral_cap", lmax(h0-cap))
        if c > 1e-7:
            little_u = min(u1, u2)
            little_v = np.sqrt(max(0., 4-little_u**2))
            t = 2+R-little_v
            check("two_cross_second_eigenvalue", abs(ev[-2]-second))
            check("two_cross_scalar_resolvent_1", c/(t-R)-1)
            check("two_cross_scalar_resolvent_2", c*(t/(t*t-4)+1/t)-2)
            count("two_cross_simple_top")
        else:
            check("two_cross_degenerate_triangle", upper+2-TARGET)
            count("two_cross_degenerate_top")
        for rb, rd in third_types:
            b3, d3 = reflection(rb), reflection(rd)
            h = query(0, *pairs[0])+query(1, *pairs[1])+query(2, b3, d3)
            check("two_cross_physical_norm", norm(h)-TARGET)
            if c > 1e-7:
                h3 = np.kron(X, b3)+np.kron(Z, d3)
                inverse = np.linalg.inv(t*np.eye(8)-h3)
                traced = np.einsum("abcb->ac", inverse.reshape(2, 4, 2, 4))
                check("two_cross_full_third_resolvent", lmax(c*traced/4-np.eye(2)))
                count("two_cross_full_third_resolvent_cases")
            count("two_cross_reflection_third_cases")
        factors = RNG.uniform(-1, 1, size=4)
        h = sum(query(i, factors[2*i]*pair[0], factors[2*i+1]*pair[1]) for i, pair in enumerate(pairs))
        h += query(2, contraction(), contraction())
        check("two_cross_attenuated_contraction_norm", norm(h)-TARGET)
        count("two_cross_attenuated_contraction_cases")
    # a=c=0: all joint sign patterns of the commuting reflections e,f.
    for esigns, fsigns in itertools.product(list(itertools.product([-1, 1], repeat=2)), repeat=2):
        common = haar(4)
        e, f = np.diag(esigns), np.diag(fsigns)
        pairs = [(XA, ZA), (-np.kron(Z, e), np.kron(X, f))]
        pairs = [(common @ b @ common.conj().T, common @ d @ common.conj().T) for b, d in pairs]
        for b, d in pairs:
            check("exceptional_sharp_pairs", max(np.linalg.norm(b @ b-np.eye(4)), np.linalg.norm(d @ d-np.eye(4)), np.linalg.norm(b @ d+d @ b)))
        h0 = query(0, *pairs[0], n=4)+query(1, *pairs[1], n=4)
        check("exceptional_exact_norm", abs(norm(h0)-2*R))
        for rb, rd in third_types:
            h = query(0, *pairs[0])+query(1, *pairs[1])+query(2, reflection(rb), reflection(rd))
            check("exceptional_physical_norm", norm(h)-TARGET)
            count("exceptional_reflection_third_cases")
        count("exceptional_joint_sign_cases")
    h = query(0, XA, ZA)+query(1, XB, ZB)+query(2, np.eye(4), np.eye(4))
    check("benchmark_attainment", abs(norm(h)-TARGET))


def basis_vector(bits):
    v = np.zeros(2**len(bits), dtype=complex)
    v[int(bits, 2)] = 1
    return v


def spin_bases():
    t3 = basis_vector("000")
    t1 = (basis_vector("001") + basis_vector("010") + basis_vector("100")) / np.sqrt(3)
    tm1 = (basis_vector("011") + basis_vector("101") + basis_vector("110")) / np.sqrt(3)
    ap = (basis_vector("010") - basis_vector("100")) / R
    am = (basis_vector("011") - basis_vector("101")) / R
    bp = (2*basis_vector("001") - basis_vector("010") - basis_vector("100")) / np.sqrt(6)
    bm = (basis_vector("011") + basis_vector("101") - 2*basis_vector("110")) / np.sqrt(6)
    wp, wm = basis_vector("00"), basis_vector("11")
    w0 = (basis_vector("01") + basis_vector("10")) / R
    ws = SINGLET
    tensor = np.kron
    half = np.column_stack([
        tensor(t3, wm)/R - tensor(t1, w0)/np.sqrt(3) + tensor(tm1, wp)/np.sqrt(6),
        np.sqrt(2/3)*tensor(am, wp) - tensor(ap, w0)/np.sqrt(3),
        np.sqrt(2/3)*tensor(bm, wp) - tensor(bp, w0)/np.sqrt(3),
        tensor(ap, ws), tensor(bp, ws),
    ])
    threehalf = np.column_stack([
        np.sqrt(3/5)*tensor(t3, w0) - np.sqrt(2/5)*tensor(t1, wp),
        tensor(ap, wp), tensor(bp, wp), tensor(t3, ws),
    ])
    check("spin_half_orthonormality", np.linalg.norm(half.conj().T @ half - np.eye(5)))
    check("spin_threehalf_orthonormality", np.linalg.norm(threehalf.conj().T @ threehalf - np.eye(4)))
    return half, threehalf


def reduced_matrices(z):
    z1, z2, z3 = z
    m = np.array([-np.sqrt(5/48)*(z1+z2+z3), (-z1+z2)/4, (-z1-z2+2*z3)/(4*np.sqrt(3))])
    n = np.array([
        [(z1-z2)/(2*R), (z1+z2-2*z3)/(2*np.sqrt(6))],
        [np.sqrt(3)*z3/4, (-z1+z2)/4],
        [(-z1+z2)/4, (2*z1+2*z2-z3)/(4*np.sqrt(3))],
    ])
    half = np.block([[np.diag([2, 5/4, 5/4]), n], [n.conj().T, .75*np.eye(2)]])
    threehalf = np.block([[np.diag([5/4, .5, .5]), m[:, None]], [m.conj()[None, :], np.array([[.75]])]])
    return half, threehalf, n


def partial_swap_checks():
    half_basis, threehalf_basis = spin_bases()
    cases = [
        (0, 0, 0), (0, 0, np.pi/2), (0, np.pi/2, 0),
        (np.pi/2, 0, 0), (0, np.pi/3, 2*np.pi/3),
        (.17, -.42, 1.1), (-2.0, .73, 2.7),
        (np.pi/8, np.pi/4, -np.pi/8), (4.2, -3.8, .29),
        (0, np.pi/2, np.pi/4), (np.pi/7, np.pi/7, -np.pi/5),
        (.01, .02, .03),
    ]
    phis = [
        (np.pi/4, np.pi/4, np.pi/4),
        (0, np.pi/4, np.pi/8),
        (np.pi/13, np.pi/7, np.pi/5),
        (np.pi/4, np.pi/4, 0),
    ]
    # Sends X to (X+Z)/sqrt(2), Z to (X-Z)/sqrt(2).
    reference_rotation = np.cos(np.pi/8)*X + np.sin(np.pi/8)*Z
    full_reference_rotation = embed(np.kron(np.kron(reference_rotation, reference_rotation), reference_rotation), [0, 1, 2])
    for angles in cases:
        us = [np.cos(angle)*np.eye(4) + 1j*np.sin(angle)*SWAP for angle in angles]
        projectors = []
        for i, u in enumerate(us):
            big_u = embed(u, [3, 4])
            p = big_u @ embed(SINGLET_P, [i, 3]) @ big_u.conj().T
            projectors.append(p)
            check("partial_swap_projection", np.linalg.norm(p @ p - p))
            check("partial_swap_rank", abs(np.trace(p) - 8))
        k = sum(projectors)
        check("partial_swap_projector_bound", lmax(k) - 2.5)
        half, threehalf, n = reduced_matrices(np.exp(2j*np.array(angles)))
        check("spin_half_reconstruction", np.linalg.norm(half_basis.conj().T @ k @ half_basis - half))
        check("spin_threehalf_reconstruction", np.linalg.norm(threehalf_basis.conj().T @ k @ threehalf_basis - threehalf))
        check("spin_half_invariance", np.linalg.norm(k @ half_basis - half_basis @ half))
        check("spin_threehalf_invariance", np.linalg.norm(k @ threehalf_basis - threehalf_basis @ threehalf))
        spectrum = sorted([0.0]*6 + list(np.repeat(np.linalg.eigvalsh(threehalf), 4)) + list(np.repeat(np.linalg.eigvalsh(half), 2)))
        check("spin_full_spectrum", np.max(np.abs(np.linalg.eigvalsh(k) - spectrum)))
        check("spin_threehalf_bound", lmax(threehalf) - 2)
        schur = 1.75*np.eye(2) - n.conj().T @ np.diag([2, .8, .8]) @ n
        check("spin_half_schur", lmax(-schur))
        phases = np.angle(np.exp(2j*(np.array(angles[:2])-angles[2])))
        alpha, beta = (phases[0]+phases[1])/2, (phases[0]-phases[1])/2
        c, x = np.cos(beta), np.cos(alpha)
        f = 9*(1-c*c)*x*x + 2*c*(7+9*c*c)*x + c*c*(41-9*c*c)
        check("spin_half_determinant_identity", abs(np.linalg.det(schur) - f/25))
        common = haar(4)
        local_refs = np.kron(np.kron(haar(2), haar(2)), haar(2))
        joint = np.kron(local_refs, common)
        check("partial_swap_complex_conjugation", np.max(np.abs(np.linalg.eigvalsh(joint @ k @ joint.conj().T) - np.linalg.eigvalsh(k))))
        count("partial_swap_angle_cases")
        for triple in phis:
            h = np.zeros((32, 32), dtype=complex)
            upper, middle = [], []
            for i, (u, phi, p) in enumerate(zip(us, triple, projectors)):
                memory_x = common @ u @ XA @ u.conj().T @ common.conj().T
                memory_z = common @ u @ ZA @ u.conj().T @ common.conj().T
                b = -np.cos(phi)*memory_x - np.sin(phi)*memory_z
                d = -np.cos(phi)*memory_x + np.sin(phi)*memory_z
                hi = query(i, b, d)
                ui, vi = R*(np.cos(phi)+np.sin(phi)), R*(np.cos(phi)-np.sin(phi))
                common_big = embed(common, [3, 4])
                pi = common_big @ full_reference_rotation @ p @ full_reference_rotation.conj().T @ common_big.conj().T
                check("partial_swap_top_subspace", np.linalg.norm(hi @ pi - ui*pi))
                check("partial_swap_local_spectral_cap", lmax(hi - vi*np.eye(32) - (ui-vi)*pi))
                h += hi
                upper.append(ui)
                middle.append(vi)
            excess = np.array(upper) - np.array(middle)
            order = np.argsort(excess)[::-1]
            cap = sum(middle) + excess[order[0]] + excess[order[1]] + .5*excess[order[2]]
            check("partial_swap_physical_cap", norm(h) - cap)
            check("partial_swap_scalar_target", cap - TARGET)
            check("partial_swap_physical_norm", norm(h) - TARGET)
            count("partial_swap_physical_cases")
    # Scalar boundary and interior cases test the published polynomial identity.
    for c, x in itertools.product([0., 1/7, 2/3, np.sqrt(5)/3, .91, 1.], [-1., -.37, 0., .61, 1.]):
        f = 9*(1-c*c)*x*x + 2*c*(7+9*c*c)*x + c*c*(41-9*c*c)
        check("spin_polynomial_nonnegative", -f)
        if c <= 2/3:
            square = 9*(1-c*c)*(x+c*(7+9*c*c)/(9*(1-c*c)))**2 + 64*c*c*(5-9*c*c)/(9*(1-c*c))
            check("spin_polynomial_square_identity", abs(f-square))
        else:
            endpoint = (1-c)*(9*c**3+27*c*c-5*c+9)
            fminus = 9*(1-c*c)-2*c*(7+9*c*c)+c*c*(41-9*c*c)
            check("spin_polynomial_endpoint_identity", abs(fminus-endpoint))
        count("spin_polynomial_cases")
    # An exact rational-angle saturator of the projector theorem.
    p0 = embed(SINGLET_P, [0, 3])
    p1 = embed(SINGLET_P, [1, 3])
    p2 = embed(SINGLET_P, [2, 4])
    check("partial_swap_projector_attainment", abs(lmax(p0+p1+p2)-2.5))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results/noncommuting_families.json"))
    args = parser.parse_args()
    if args.output.resolve() == Path(__file__).resolve():
        parser.error("The output must differ from the source.")
    two_cross_checks()
    partial_swap_checks()
    result = {
        "description": "Finite matrix regressions, not proof or priority certification",
        "seed": SEED,
        "tolerance": TOL,
        "numpy_version": np.__version__,
        "python_version": platform.python_version(),
        "maximum_matrix_dimension": 32,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "counts": COUNTS,
        "maximum_positive_residuals": RES,
        "maximum_positive_residual": max(RES.values()),
        "all_finite_and_within_tolerance": True,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: finite noncommuting-family checks; wrote {args.output}")


if __name__ == "__main__":
    main()
