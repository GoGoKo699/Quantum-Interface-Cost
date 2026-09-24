#!/usr/bin/env python3
"""Small deterministic identity checks; supplied proofs establish the bounds.

No optimizer is used. Scalar endpoint identities and synthetic tuples are
checked with exact rational arithmetic, including Q(sqrt(2)) arithmetic.
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
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
TOL = 3e-10


def require(test, message):
    if not test:
        raise AssertionError(message)


def q2(a=0, b=0):
    return F(a), F(b)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0]


def div(x, y):
    den = y[0]**2 - 2*y[1]**2
    require(den != 0, "zero quadratic-field denominator")
    return mul(x, (y[0]/den, -y[1]/den))


def positive(x):
    a, b = x
    if not b:
        return a > 0
    if a >= 0 and b > 0:
        return True
    if a <= 0 and b < 0:
        return False
    return a*a > 2*b*b if a > 0 else 2*b*b > a*a


def exact_checks():
    count = 0
    for i in range(21):
        y = F(i, 20)
        endpoint = (1-y)**2 + 2*y/(1+y)
        require(endpoint == 1-y*y*(1-y)/(1+y), "scalar endpoint identity")
        for j in range(i, 21):
            x = F(j, 20)
            value = (x-y)**2 + 4*x*y/((1+x)*(1+y))
            require(value <= endpoint <= 1, "scalar monotonic upper bound")
            count += 1
    require(F(7, 2)*(1-2*F(1, 30)) == F(49, 15) > 3,
            "old synthetic tuple must violate the weaker tail bound")
    old_U, old_m = q2(F(7, 2)), q2(F(1, 2), 2)
    old_circle_excess = sub(add(mul(sub(old_U, q2(2)), sub(old_U, q2(2))),
                                mul(sub(old_m, q2(2)), sub(old_m, q2(2)))), q2(4))
    require(old_circle_excess == q2(F(17, 2), -6) and positive(old_circle_excess),
            "old synthetic tuple violates spectral circle")

    U, m, r = q2(F(37, 10)), q2(F(3, 10), 2), q2(0, 1)
    tau, lam = q2(F(13, 100)), q2(F(87, 200))
    tail_gap = sub(mul(add(U, m), tau), sub(U, q2(3)))
    require(tail_gap == q2(F(-9, 50), F(13, 50)) and positive(tail_gap),
            "new synthetic rank-two tail constraint")
    rank_one_gap = sub(add(q2(2), m), mul(add(U, m), lam))
    require(rank_one_gap == q2(F(14, 25), F(113, 100))
            and positive(rank_one_gap), "new synthetic rank-one constraint")
    E = F(37, 50)**2
    require(E == F(1369, 2500), "new spectrum SLD minimum")
    require(F(453, 800)-E == F(373, 20000) > 0, "six-Pauli gap")
    require(F(3631, 1250)-F(17, 10)**2 == F(37, 2500) > 0,
            "exact fixed-spectrum score gap")
    t = sub(U, r)
    c = sub(U, m)
    require(c == mul(q2(2), sub(t, q2(2))) and positive(sub(t, q2(2))),
            "positive resolvent parameters")
    f = div(sub(t, q2(1)), mul(t, sub(t, q2(2))))
    g = div(add(t, q2(1)), mul(t, add(t, q2(2))))
    excess = sub(mul(c, add(mul(q2(F(87, 100)), f),
                                  mul(q2(F(13, 100)), g))), q2(1))
    claimed = div(q2(4883, -3440), mul(q2(500), mul(t, add(t, q2(2)))))
    require(excess == claimed and positive(excess), "exact resolvent witness")
    require(4883**2-2*3440**2 == 176489, "integer positivity witness")
    circle_excess = sub(add(mul(sub(U, q2(2)), sub(U, q2(2))),
                            mul(sub(m, q2(2)), sub(m, q2(2)))), q2(4))
    require(circle_excess == q2(F(489, 50), F(-34, 5))
            and positive(circle_excess), "new synthetic tuple violates spectral circle")
    return {"scalar_rational_pairs": count,
            "old_tuple_weak_tail_score": "49/15 > 3",
            "old_tuple_spectral_circle_excess_exact_coefficients":
                [str(old_circle_excess[0]), str(old_circle_excess[1])],
            "new_tuple_tail_sld_and_fixed_spectrum_constraints_pass": True,
            "new_tuple_spectral_circle_excess_exact_coefficients":
                [str(circle_excess[0]), str(circle_excess[1])],
            "new_tuple_resolvent_excess_exact_coefficients":
                [str(excess[0]), str(excess[1])],
            "new_tuple_resolvent_lower_witness":
                1+float(excess[0])+float(excess[1])*np.sqrt(2)}


def haar(rng, n):
    A = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    d = np.diag(R)
    return Q * (d/np.abs(d)).conj()


def partial_leaf(E):
    return np.einsum("aiaj->ij", E.reshape(2, 2, 2, 2))


def random_center_operator(rng, rank):
    A = rng.normal(size=(4, rank)) + 1j*rng.normal(size=(4, rank))
    E = A @ A.conj().T
    vals, vecs = np.linalg.eigh(partial_leaf(E))
    filt = (vecs / np.sqrt(2*vals)) @ vecs.conj().T
    K = np.kron(I, filt)
    return K @ E @ K.conj().T


def insert(E, which, memory_dim=2):
    """Insert E on reference `which` and the shared memory, with spectators."""
    if which == 1:
        return np.kron(I, E)
    ans = np.zeros((4*memory_dim, 4*memory_dim), dtype=complex)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    if b == d:
                        ans[(2*a+b)*memory_dim:(2*a+b+1)*memory_dim,
                            (2*c+d)*memory_dim:(2*c+d+1)*memory_dim] = \
                            E[a*memory_dim:(a+1)*memory_dim,
                              c*memory_dim:(c+1)*memory_dim]
    return ans


def choi_checks(rng):
    max_sum = 0.0
    residual = 0.0
    min_envelope_gap = 2.0
    count = 0
    for j in range(48):
        E = random_center_operator(rng, (1, 2, 4)[j % 3])
        Fm = random_center_operator(rng, (1, 4, 2)[(j // 3) % 3])
        residual = max(residual, np.linalg.norm(partial_leaf(E)-I/2),
                       np.linalg.norm(partial_leaf(Fm)-I/2))
        ev, U = np.linalg.eigh(E)
        fv, V = np.linalg.eigh(Fm)
        p, q = float(ev[-1]), float(fv[-1])
        top = float(np.linalg.eigvalsh(insert(E, 0)+insert(Fm, 1))[-1])
        require(top <= 1.5+TOL, "fixed-center sum bound")
        if min(p, q) > 0.5+TOL:
            P = np.outer(U[:, -1], U[:, -1].conj())
            R = np.outer(V[:, -1], V[:, -1].conj())
            overlap = np.linalg.norm(insert(P, 0) @ insert(R, 1), 2)
            require(overlap <= 1/(2*np.sqrt(p*q))+TOL, "Schmidt overlap cap")
            bound = 1+0.5*np.sqrt(4*(p-q)**2+(2-1/p)*(2-1/q))
            require(top <= bound+TOL and bound <= 1.5+TOL,
                    "spectral-envelope sum bound")
            min_envelope_gap = min(min_envelope_gap, bound-top)
        max_sum = max(max_sum, top)
        count += 1
    bell = np.array([1, 0, 0, 1], dtype=complex)/np.sqrt(2)
    phi = np.outer(bell, bell.conj())
    product = np.kron(np.diag([1, 0]), I/2)
    for E, Fm in [(phi, phi), (phi, product)]:
        require(abs(np.linalg.eigvalsh(insert(E, 0)+insert(Fm, 1))[-1]-1.5)<TOL,
                "fixed-center exact attainer")
    return {"random_positive_pairs": count, "explicit_attainers": 2,
            "max_sum_eigenvalue": max_sum,
            "max_center_marginal_residual": float(residual),
            "min_spectral_envelope_gap": float(min_envelope_gap)}


def sharp_checks(rng):
    XA, ZA = np.kron(X, I), np.kron(Z, I)
    swap = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                     [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
    gamma = np.kron(np.kron(Y, Y), np.eye(4))
    max_rank_two = 0.0
    min_tail_gap = 10.0
    min_rank_one_gap = 10.0
    max_chiral_residual = 0.0
    max_circle_value = 0.0
    max_remainder_norm_excess = 0.0
    min_compression_test_gap = 10.0
    cases = [np.eye(4), swap] + [haar(rng, 4) for _ in range(38)]
    for V in cases:
        B2, D2 = V @ XA @ V.conj().T, V @ ZA @ V.conj().T
        h1 = np.kron(X, XA)+np.kron(Z, ZA)
        h2 = np.kron(X, B2)+np.kron(Z, D2)
        H = insert(h1, 0, 4)+insert(h2, 1, 4)
        residual = np.linalg.norm(gamma @ H @ gamma+H)
        max_chiral_residual = max(max_chiral_residual, residual)
        eig, vec = np.linalg.eigh(H)
        U, m = float(eig[-1]), float(eig[-2])
        require(U <= 4+TOL and m >= 2-TOL, "earlier sharp spectrum bounds")
        circle_value = (U-2)**2+(m-2)**2
        require(circle_value <= 4+TOL, "sharp spectrum circle")
        max_circle_value = max(max_circle_value, circle_value)
        omega = vec[:, -1]
        u = (omega+gamma @ omega)/np.sqrt(2)
        v = (omega-gamma @ omega)/np.sqrt(2)
        plus, minus = (np.eye(16)+gamma)/2, (np.eye(16)-gamma)/2
        C = plus @ H @ minus
        Cprime = C-U*np.outer(u, v.conj())
        rem_excess = np.linalg.norm(Cprime, 2)-m
        max_remainder_norm_excess = max(max_remainder_norm_excess, rem_excess)
        require(rem_excess <= TOL, "singular remainder norm")
        A = omega.reshape(4, 4)
        rho = np.einsum("rq,rt->qt", A, A.conj())
        vals, basis = np.linalg.eigh(rho)
        tau = float(vals[0]+vals[1])
        tail_gap = 3-U+(U+m)*tau
        rank_one_gap = 2+m-(U+m)*float(vals[-1])
        min_tail_gap = min(min_tail_gap, tail_gap)
        min_rank_one_gap = min(min_rank_one_gap, rank_one_gap)
        require(tail_gap >= -TOL and rank_one_gap >= -TOL,
                "actual top-state Schmidt constraints")
        for W in [haar(rng, 4)[:, :2], basis[:, 2:]]:
            K = np.kron(np.eye(4), W)
            compressed = K.conj().T @ H @ K
            norm = float(np.max(np.abs(np.linalg.eigvalsh(compressed))))
            max_rank_two = max(max_rank_two, norm)
            require(norm <= 3+TOL, "rank-two compression norm")
            projected_u, projected_v = K @ (K.conj().T @ u), K @ (K.conj().T @ v)
            a, b = np.vdot(projected_u, projected_u).real, np.vdot(projected_v, projected_v).real
            if min(a, b) > TOL:
                test_lower = U*np.sqrt(a*b)-m*np.sqrt(max(0, (1-a)*(1-b)))
                min_compression_test_gap = min(min_compression_test_gap, norm-test_lower)
                require(test_lower <= norm+TOL, "normalized singular-vector compression test")
            for h in [h1, h2]:
                pi = (h @ h+2*h)/8
                L = np.kron(I, W)
                E = L.conj().T @ pi @ L
                require(np.linalg.norm(partial_leaf(E)-I/2)<TOL,
                        "sharp Bell compression has the center marginal")
        for q in [basis[:, -1], haar(rng, 4)[:, 0]]:
            K = np.kron(np.eye(4), q[:, None])
            require(np.max(np.abs(np.linalg.eigvalsh(K.conj().T @ H @ K)))
                    <= 2+TOL, "rank-one compression norm")

    # Complementary memories, one Bell pair and one product pair: score 3.
    H = (insert(np.kron(X, XA)+np.kron(Z, ZA), 0, 4)
         + insert(np.kron(X, np.kron(I, X))+np.kron(Z, np.kron(I, Z)), 1, 4))
    psi = np.zeros(16, dtype=complex)
    psi[0], psi[10] = 1/np.sqrt(2), 1/np.sqrt(2)
    require(abs(np.vdot(psi, H @ psi).real-3)<TOL, "rank-two score attainer")
    require(np.linalg.matrix_rank(psi.reshape(4, 4), tol=1e-9)==2,
            "attainer Schmidt rank")
    return {"sharp_pair_families": len(cases),
            "rank_two_compressions": 2*len(cases),
            "rank_one_compressions": 2*len(cases),
            "max_rank_two_compression_norm": max_rank_two,
            "min_top_tail_gap": min_tail_gap,
            "min_top_rank_one_gap": min_rank_one_gap,
            "max_chiral_residual": float(max_chiral_residual),
            "max_spectral_circle_value": max_circle_value,
            "max_singular_remainder_norm_excess": float(max_remainder_norm_excess),
            "min_singular_compression_test_gap": float(min_compression_test_gap),
            "rank_two_attaining_score": 3}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rng = np.random.default_rng(2026092407)
    report = {"status": "all checks passed; symbolic proof is separate",
              "python": platform.python_version(), "numpy": np.__version__,
              "seed": 2026092407, "tolerance": TOL,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "exact_scalar_checks": exact_checks(),
              "fixed_center_checks": choi_checks(rng),
              "sharp_pair_checks": sharp_checks(rng)}
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
