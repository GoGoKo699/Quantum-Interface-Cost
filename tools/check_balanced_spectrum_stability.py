#!/usr/bin/env python3
"""Exact scalar comparisons and fixed diagnostics for balanced-score stability.

The quantified results are proved in the accompanying note. This checker
uses ten prescribed constructions, no grid, sampling, or optimization.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path
import platform

import numpy as np

BASE = "8e38f704b1d8e74344c87ee83748d1f4dc45fcaf"
NOTE = "docs/audits/BALANCED_SPECTRUM_STABILITY.md"
TOL = 3e-9
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
SQRT2 = np.sqrt(2.)


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def identity(out, label, actual, expected):
    residual = float(np.linalg.norm(np.asarray(actual)-np.asarray(expected)) /
                     max(1., np.linalg.norm(expected)))
    out[label] = residual
    require(residual <= TOL, label)


def inequality(out, label, margin):
    out[label] = float(margin)
    require(margin >= -TOL, label)


def exact_comparisons():
    rows = {}

    def check(name, condition, witness):
        require(condition, name)
        rows[name] = witness

    k = Q(81, 256)
    c0 = 1-2*k/3-k*k/27
    check("dominant_concentration_constant", c0 == Q(51469, 65536),
          "1-2(81/256)/3-(81/256)^2/27=51469/65536")
    check("concentration_lower_bound", c0 >= Q(25, 32), "c0>=25/32")
    check("concentration_upper_bound", c0 <= 1, "1+c0<=2")
    check("diffuse_radical_lower_bound", Q(1413, 1000)**2 < 2,
          "sqrt(2)>1413/1000")
    check("diffuse_gap_constant", Q(1413, 1000)-Q(281, 200) == Q(1, 125),
          "1413/1000-281/200=1/125")
    check("diffuse_gap_comparison", Q(1, 125) > Q(1, 128), "1/125>1/128")
    check("dominant_radical_upper_bound", Q(17, 12)**2 > 2,
          "sqrt(2)-1<5/12 and 2-sqrt(2)>7/12")
    check("dominant_slack_constant", Q(7, 12)*Q(25, 32)-Q(5, 12) == Q(5, 128),
          "(7/12)(25/32)-5/12=5/128")
    check("dominant_deficit_constant", Q(5, 512) > Q(1, 128), "5/512>1/128")
    check("imbalance_to_distance_constant", 2*128+2*16 == 288,
          "2(1-b)+2(u^2-v^2)^2<=288 epsilon/z^2")
    check("low_b_distance_constant", 2*256 == 512, "b<1/2 yields constant512")
    check("nonflat_tail_quadratic_coefficient", 2*k/Q(3, 4) == Q(27, 32),
          "2k/A<=27/32 for A>=3/4")
    check("nonflat_tail_quartic_coefficient", k*k/Q(3, 4)**3 == Q(243, 1024),
          "k^2/A^3<=243/1024 for A>=3/4")
    check("nonflat_endpoint_radical_upper", Q(99, 70)**2 > 2, "sqrt(2)<99/70")
    check("nonflat_concavity_zero_endpoint", Q(3, 2)**2 > 2, "3/2-sqrt(2)>0")
    check("nonflat_concavity_right_rational_bound",
          (34*Q(99, 70)-24)/31 == Q(843, 1085),
          "(34sqrt(2)-24)/31<843/1085")
    check("nonflat_concavity_right_positive", 51469*1085-843*65536 == 597017,
          "51469*1085-843*65536=597017>0")
    check("nearflat_singleton_weight", 1-128*Q(1, 1024) == Q(7, 8),
          "flat gap<=1/1024 implies b_R>=7/8")
    check("nearflat_selected_coefficient", Q(66, 25)**2 < 7,
          "sqrt(7)/4>66/100")
    check("nearflat_root_radius", Q(1, 4096) < Q(1, 100), "eta<=1/(4096n)<1/100")
    check("nearflat_total_coefficient", Q(1, 2) < Q(71, 100)**2,
          "1/sqrt(2)<71/100")
    check("nearflat_dominant_ratio", Q(65, 72)**2 > Q(3, 4),
          "(.65/.72)^2>3/4")
    check("nearflat_continuity_budget", 4*Q(1, 4096) == Q(1, 1024),
          "4n/[4096n]=1/1024")
    check("rotation_rational_unit_circle", Q(24, 25)**2+Q(7, 25)**2 == 1,
          "(24/25)^2+(7/25)^2=1")
    check("rotation_positive_bisector_signs", Q(24, 25) > Q(7, 25),
          "theta<pi/4 for the fixed sharpness rotation")
    check("bias_rational_unit_circle", Q(3, 5)**2+Q(4, 5)**2 == 1,
          "t=3/5 and v=4/5 satisfy t^2+v^2=1")
    v = Q(4, 5)
    check("bias_gap_rationalization", 2*(1+v*v)-(1+v)**2 == (1-v)**2,
          "[2sqrt((1+v^2)/2)]^2-(1+v)^2=(1-v)^2")
    return rows


def local(n, site, op):
    out = np.ones((1, 1), complex)
    for j in range(n):
        out = np.kron(out, op if j == site else I)
    return out


def trace_norm(H):
    return float(np.sum(np.abs(np.linalg.eigvalsh((H+H.conj().T)/2))))


def query_data(S, n):
    rows, coefficients = [], []
    d = 2**n
    for site in range(n):
        pair = []
        for axis, op in [("X", X), ("Z", Z)]:
            U = local(n, site, op)
            F = trace_norm(S@U@S)
            a = float(np.trace(S@U@S@U).real)
            value = float(np.trace(S@U).real/np.sqrt(d))
            pair.append(value)
            rows.append(dict(site=site, axis=axis, original_score=F,
                             affinity=a, root_singleton_coefficient=value))
        coefficients.append(pair)
    return rows, np.array(coefficients)


def householder(d):
    j = np.arange(1, d+1)
    vector = (j % 5-2)+1j*(j % 7-3)
    vector = vector/np.linalg.norm(vector)
    return np.eye(d)-2*np.outer(vector, vector.conj())


def reflection_fixtures():
    B, C = (X+Z)/SQRT2, (X-Z)/SQRT2
    V = householder(8)
    return [
        ("one_qubit_bisector_equality", B, 1, 3/5, "equality"),
        ("one_qubit_Y_diffuse", Y, 1, 4/5, "diffuse"),
        ("one_qubit_rotated_bisector_sharpness", (24*B+7*C)/25, 1, 1., "rotation"),
        ("one_qubit_X_bias_scaling", X, 1, 3/5, "bias"),
        ("two_qubit_entangling_reflection", (np.kron(Z, I)+np.kron(X, X))/SQRT2,
         2, 4/5, "entangled"),
        ("three_qubit_complex_Householder", V@local(3, 0, Z)@V.conj().T,
         3, 5/13, "complex"),
    ]


def reflection_case(name, R, n, t, kind):
    errors, margins = {}, {}
    d = 2**n
    Id = np.eye(d, dtype=complex)
    tau = lambda M: float(np.trace(M).real/d)
    identity(errors, "reflection_Hermitian", R, R.conj().T)
    identity(errors, "reflection_square", R@R, Id)
    identity(errors, "reflection_balanced", tau(R), 0)
    rho = (Id+t*R)/d
    S = ((np.sqrt(1+t)+np.sqrt(1-t))*Id+
         (np.sqrt(1+t)-np.sqrt(1-t))*R)/(2*np.sqrt(d))
    identity(errors, "state_root", S@S, rho)
    rows, _ = query_data(S, n)
    coefficients = np.array([[tau(R@local(n, i, op)) for op in [X, Z]] for i in range(n)])
    site_mass = np.sum(coefficients**2, axis=1)
    W, b = float(np.sum(site_mass)), float(np.max(site_mass))
    site = int(np.argmax(site_mass))
    u, v = coefficients[site]
    B = local(n, site, ((1 if u >= 0 else -1)*X+(1 if v >= 0 else -1)*Z)/SQRT2)
    squared_distance = tau((R-B)@(R-B))
    identity(errors, "aligned_bisector_overlap", squared_distance,
             2-SQRT2*(abs(u)+abs(v)))
    energies = []
    for row in rows:
        U = local(n, row["site"], X if row["axis"] == "X" else Z)
        comm = R@U-U@R
        q = tau(comm.conj().T@comm)/4
        energies.append(q)
        inequality(margins, f"q{row['site']}{row['axis']}_lower", q)
        inequality(margins, f"q{row['site']}{row['axis']}_upper", 1-q)
    g = sum(row["original_score"] for row in rows)
    affinity = sum(np.sqrt(max(0., row["affinity"])) for row in rows)
    g_target = 2*n-2+2*np.sqrt(1-t*t/2)
    affinity_target = 2*n-2+np.sqrt(2+2*np.sqrt(1-t*t))
    eg, ea = g_target-g, affinity_target-affinity
    responses = []
    for label, z in [("original", t*t), ("affinity", 1-np.sqrt(1-t*t))]:
        response = sum(np.sqrt(max(0., 1-z*q)) for q in energies)
        target = 2*n-2+2*np.sqrt(1-z/2)
        gap = target-response
        inequality(margins, label+"_nonnegative_response_gap", gap)
        inequality(margins, label+"_mass_rigidity", gap-z*(1-b)/128)
        inequality(margins, label+"_imbalance_rigidity", gap-z*z*(u*u-v*v)**2/16)
        inequality(margins, label+"_reflection_distance", 512*max(0., gap)/z**2-squared_distance)
        responses.append(dict(kind=label, z=z, response=response, gap=gap))
    inequality(margins, "original_gap_dominates_response_gap", eg-responses[0]["gap"])
    identity(errors, "affinity_gap_equals_response_gap", ea, responses[1]["gap"])
    target_rho = (Id+t*B)/d
    distance = trace_norm(rho-target_rho)
    inequality(margins, "original_trace_norm_transfer", 16*SQRT2*np.sqrt(max(0., eg))/t-distance)
    inequality(margins, "affinity_trace_norm_transfer",
               16*SQRT2*(1+np.sqrt(1-t*t))*np.sqrt(max(0., ea))/t-distance)
    if kind == "equality":
        identity(errors, "bisector_zero_gap", eg, 0)
        identity(errors, "bisector_zero_distance", distance, 0)
    if kind == "rotation":
        identity(errors, "square_root_sharpness_gap", eg, SQRT2*(1-24/25))
        identity(errors, "square_root_sharpness_distance", distance**2, SQRT2*eg)
    if kind == "bias":
        v0 = np.sqrt(1-t*t)
        exact_gap = (1-v0)**2/(2*np.sqrt((1+v0*v0)/2)+1+v0)
        identity(errors, "bias_gap_rationalization", eg, exact_gap)
        identity(errors, "bias_trace_norm_formula", distance, t*np.sqrt(2-SQRT2))
    return dict(name=name, family="balanced reflection", ambient_qubits=n,
                matrix_dimension=d, bias=t, original_score=g, affinity_score=affinity,
                original_gap=eg, affinity_gap=ea, singleton_mass=W,
                maximum_site_mass=b, selected_site=site,
                selected_squared_imbalance=float((u*u-v*v)**2),
                normalized_reflection_squared_distance=squared_distance,
                state_trace_norm_distance=distance, response_data=responses,
                query_data=rows, relative_identity_residuals=errors,
                inequality_margins=margins)


def retention_basis(n):
    B = (X+Z)/SQRT2
    values, vectors = np.linalg.eigh(B)
    beta = vectors[:, int(np.argmax(values))]
    return np.kron(beta[:, None], np.eye(2**(n-1)))


def nonflat_fixtures():
    n = 5
    Q0 = retention_basis(n)
    generator = local(n, 0, (X-Z)/SQRT2)@local(n, 1, X)
    angle = 1/256
    V = np.cos(angle)*np.eye(2**n)+1j*np.sin(angle)*generator
    delta = 1/(16384*n)
    probabilities = (1+delta*np.array([1]*8+[-1]*8))/16
    near = ("five_qubit_nonflat_complex_near_retention", n, V@Q0, probabilities,
            V@Q0, "near", True)
    n = 4
    _, eigenvectors = np.linalg.eigh((X+Z)/SQRT2)
    columns = []
    for signs in product([-1, 1], repeat=3):
        if sum(signs) > 0:
            for spectator in [0, 1]:
                column = np.ones(1, complex)
                for sign in signs:
                    column = np.kron(column, eigenvectors[:, (sign+1)//2])
                columns.append(np.kron(column, I[:, spectator]))
    majority_basis = np.column_stack(columns)
    generator = local(n, 0, Z)@local(n, 1, Z)
    V = np.cos(1/10)*np.eye(16)+1j*np.sin(1/10)*generator
    Qfar = V@majority_basis
    delta = 1/(16384*n)
    probabilities = (1+delta*np.array([1]*4+[-1]*4))/8
    far = ("four_qubit_nonflat_complex_majority_support", n, Qfar, probabilities,
           Qfar, "far", True)
    n = 3
    Qdom = retention_basis(n)
    dominant = ("three_qubit_nonflat_dominant_outside_radius", n, Qdom,
                np.array([.45, .45, .05, .05]), Qdom, "dominant", False)
    n = 5
    Qfull = retention_basis(n)
    deficient = ("five_qubit_rank_fifteen_dominant", n, Qfull[:, :15],
                 np.ones(15)/15, Qfull, "dominant", False)
    return [near, far, dominant, deficient]


def nonflat_case(name, n, basis, probabilities, flat_basis, branch, nearflat):
    errors, margins = {}, {}
    d, k = 2**n, 2**(n-1)
    identity(errors, "support_isometry", basis.conj().T@basis, np.eye(basis.shape[1]))
    identity(errors, "flat_isometry", flat_basis.conj().T@flat_basis, np.eye(k))
    identity(errors, "state_probabilities_sum", np.sum(probabilities), 1)
    inequality(margins, "state_probability_nonnegative", float(np.min(probabilities)))
    S = (basis*np.sqrt(probabilities))@basis.conj().T
    rho = (basis*probabilities)@basis.conj().T
    P = flat_basis@flat_basis.conj().T
    Sflat = P/np.sqrt(k)
    identity(errors, "state_root_square", S@S, rho)
    identity(errors, "state_trace", np.trace(rho), 1)
    identity(errors, "flat_support_contains_state", P@S, S)
    eta = float(np.linalg.norm(S-Sflat))
    identity(errors, "spectral_root_distance", eta*eta,
             2*(1-float(np.trace(S).real)/np.sqrt(k)))
    rows, coefficients = query_data(S, n)
    flat_rows, _ = query_data(Sflat, n)
    g = sum(row["original_score"] for row in rows)
    affinity = sum(np.sqrt(max(0., row["affinity"])) for row in rows)
    gflat = sum(row["original_score"] for row in flat_rows)
    target = 2*n-2+SQRT2
    flat_gap = target-gflat
    inequality(margins, "score_continuity", 4*n*eta-abs(g-gflat))
    site_mass = np.sum(coefficients**2, axis=1)
    T = float(np.sum(site_mass))
    A = float(np.max(site_mass)/T)
    inequality(margins, "positive_root_singleton_cap", .5-T)
    amplitudes = np.sqrt(site_mass/T)
    mean = float(np.mean([abs(np.dot(amplitudes, signs))
                          for signs in product([-1, 1], repeat=n)]))
    u = float(np.trace(S).real/np.sqrt(k))
    v = np.sqrt(max(0., 1-u*u))
    y = 2*T
    inequality(margins, "half_rank_centered_circle",
               (u*mean+v*np.sqrt(max(0., 1-mean*mean)))**2-y)
    if A >= .75-TOL:
        r = SQRT2-1
        psi = (1-r)*(2-r+r*A)/(2*(1-r*A))
        inequality(margins, "dominant_Rademacher_gate", psi-mean*mean)
        inequality(margins, "dominant_affinity_converse", target-affinity)
        inequality(margins, "dominant_original_converse", target-g)
    if nearflat:
        inequality(margins, "nearflat_radius", 1/(4096*n)-eta)
        inequality(margins, "nearflat_original_converse", target-g)
        inequality(margins, "complex_support_imaginary_norm", float(np.linalg.norm(P.imag))-1e-6)
        if branch == "near":
            inequality(margins, "near_flat_score_branch", 1/1024-flat_gap)
            R = 2*P-np.eye(d)
            rcoeff = np.array([[float(np.trace(R@local(n, i, op)).real/d)
                               for op in [X, Z]] for i in range(n)])
            site = int(np.argmax(np.sum(rcoeff**2, axis=1)))
            b = float(np.sum(rcoeff[site]**2))
            inequality(margins, "nearflat_reflection_site_mass", b-7/8)
            inequality(margins, "nearflat_selected_root_mass", np.linalg.norm(coefficients[site])-.65)
            inequality(margins, "nearflat_total_root_mass", .72-np.sqrt(T))
            inequality(margins, "nearflat_dominant_direction", A-.75)
        else:
            inequality(margins, "far_flat_score_branch", flat_gap-1/1024)
            inequality(margins, "far_branch_continuity_margin", flat_gap-4*n*eta)
            inequality(margins, "far_branch_outside_dominant_direction", .75-A)
    else:
        inequality(margins, "dominant_outside_radius", eta-1/(4096*n))
        inequality(margins, "dominant_direction_hypothesis", A-.75)
    return dict(name=name, family="arbitrary spectrum at half-rank cap",
                ambient_qubits=n, matrix_dimension=d, state_rank=len(probabilities),
                rank_cap=k, original_score=g, affinity_score=affinity,
                retention_bound=target, flat_comparison_score=gflat,
                flat_comparison_gap=flat_gap, root_distance=eta,
                support_imaginary_frobenius_norm=float(np.linalg.norm(P.imag)),
                nearflat_radius=1/(4096*n), nearflat_hypothesis=nearflat,
                proof_branch=branch, singleton_mass=T,
                normalized_maximum_site_mass=A, Rademacher_first_moment=mean,
                trace_root_over_sqrt_rank_cap=u, query_data=rows,
                relative_identity_residuals=errors, inequality_margins=margins)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source = Path(__file__).resolve()
    repository = source.parents[1]
    note = repository/NOTE
    require(note.is_file(), "Proof note must exist before producing a hash-pinned report")
    if args.output:
        destination = args.output.resolve()
        require(destination.suffix == ".json" and destination not in [source, note.resolve()],
                "Output must be JSON and cannot overwrite source or proof note")
    exact = exact_comparisons()
    cases = [reflection_case(*row) for row in reflection_fixtures()]
    cases += [nonflat_case(*row) for row in nonflat_fixtures()]
    residuals = [value for row in cases for value in row["relative_identity_residuals"].values()]
    margins = [value for row in cases for value in row["inequality_margins"].values()]
    report = dict(status="exact scalar comparisons and fixed constructions passed",
                  research_base=BASE, python=platform.python_version(), numpy=np.__version__,
                  tolerance=TOL, source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  proof_note_sha256={NOTE: hashlib.sha256(note.read_bytes()).hexdigest()},
                  exact_comparisons=exact, constructions=cases,
                  exact_comparison_count=len(exact), fixed_construction_count=len(cases),
                  query_count=sum(len(row["query_data"]) for row in cases),
                  matrix_identity_count=len(residuals), inequality_count=len(margins),
                  maximum_relative_identity_residual=max(residuals),
                  minimum_inequality_margin=min(margins),
                  maximum_matrix_dimension=max(row["matrix_dimension"] for row in cases),
                  scope="Exact Fraction comparisons verify the displayed rigidity, dominant-direction and near-flat constants. Six balanced reflections and four nonflat/rank-deficient seeds check original-query scores, affinity and response gaps, bisector distances, sharpness identities, the centered half-rank circle, and both branches of the near-flat argument. The five-qubit near-flat seed has a complex support and genuinely nonuniform eigenvalues; the complex majority-support fixture exercises the continuity branch outside the dominant-direction hypothesis. Matrices have dimension at most 32; no grid, random sampling or optimization is used. These bounded diagnostics do not prove the quantified all-dimension results or publication novelty.")
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
