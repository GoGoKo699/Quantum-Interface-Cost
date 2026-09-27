#!/usr/bin/env python3
"""Exact scalar algebra and fixed matrix diagnostics for balanced spectra.

The all-dimension result is proved analytically in the accompanying note.
No parameter grid, random sampling, optimizer, or large matrix is used.
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

BASE = "18550b3b9ab5617a788b3b5d43d575dbf6e5a39e"
NOTE = "docs/audits/BALANCED_SPECTRUM_OPTIMALITY.md"
TOL = 3e-9
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
R2 = np.sqrt(2.)


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def compare(errors, label, actual, expected):
    residual = float(np.linalg.norm(np.asarray(actual)-np.asarray(expected)) /
                     max(1., np.linalg.norm(expected)))
    errors[label] = residual
    require(residual <= TOL, label)


def nonnegative(margins, label, value):
    margins[label] = float(value)
    require(value >= -TOL, label)


def polynomial_product(a, b):
    result = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def exact_checks():
    checks = {}

    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness

    a, b = Q(3, 4), Q(2)
    s, p = a+b, a*b
    alpha, beta, gamma = 3*p-2*s*s, s**4-s*s*p+3*p*p, p*p*(s*s+p)
    denominator = 2*s**3*p
    numerator = [gamma, -denominator, beta, Q(0), alpha, Q(0), Q(1)]
    factorized = polynomial_product(polynomial_product([a*a, -2*a, Q(1)],
                                                       [b*b, -2*b, Q(1)]),
                                    [s*s+p, 2*s, Q(1)])
    check("degree_six_majorant_factorization", numerator == factorized,
          "P(x)-x=(x-3/4)^2(x-2)^2(x^2+(11/2)x+145/16)/(3993/64)")
    check("majorant_fourth_coefficient", alpha == -Q(85, 8), "alpha=-85/8")
    check("majorant_second_coefficient", beta == Q(13465, 256), "beta=13465/256")
    check("majorant_constant", gamma == Q(1305, 64), "gamma=1305/64")
    check("majorant_denominator", denominator == Q(3993, 64), "denominator=3993/64")
    baseline = (15+3*alpha+beta+gamma)/denominator
    check("majorant_moment_baseline", baseline == Q(14365, 15972), "baseline=14365/15972")
    check("majorant_K_coefficient", -30-2*alpha == -Q(35, 4), "K coefficient is 16A-35/4")
    check("low_max_half_coefficient", 16*Q(1, 2)-Q(35, 4) == -Q(3, 4), "A<=1/2 makes the K correction nonpositive")
    check("low_max_strict_nine_tenths", baseline < Q(9, 10), "14365/15972<9/10")
    check("second_tail_factorization", polynomial_product([-2, 1], [-2, 1]) == [4, -4, 1],
          "x^2-4(x-1)=(x-2)^2")
    fourth_factor = polynomial_product([16, -24, 9], [16, 8, 3])
    check("fourth_tail_factorization", fourth_factor == [256, -256, 0, 0, 27],
          "27x^4-256(x-1)=(3x-4)^2(3x^2+8x+16)")
    check("second_tail_left_endpoint", Q(25, 32) < Q(81, 100), "(5sqrt2/8)^2<(.9)^2")
    check("second_tail_right_endpoint", Q(43, 48) < Q(9, 10), "43/48<9/10")
    check("fourth_tail_left_endpoint", Q(915, 1024) < Q(9, 10), "915/1024<9/10")
    check("fourth_tail_right_endpoint", 100*3*265**2 < 81*512**2,
          "265sqrt3/512<9/10 by positive squaring")
    # H4(A)=(337A^2-162A+81)/(256A^(3/2)); differentiate its numerator.
    h4_numerator = [Q(81), -Q(162), Q(337)]
    derivative_numerator = [(2*j-3)*value for j, value in enumerate(h4_numerator)]
    check("fourth_tail_derivative", derivative_numerator == [-243, 162, 337],
          "H4 derivative has numerator 337A^2+162A-243")
    check("diffuse_threshold", 281**2 < 2*200**2, "81/100<2(sqrt2-1)")
    check("dominant_fourth_constant", Q(81, 256) < Q(1, 3), "81/256<1/3")
    check("dominant_tail_ratio", (1-Q(3, 4))/Q(3, 4) == Q(1, 3), "(1-A)/A<=1/3")
    check("dominant_radical_lower", Q(7, 5)**2 < 2, "sqrt2-1>2/5")
    dominant_slack = Q(7, 10)*(Q(2, 3)*Q(1, 3)+Q(1, 9)*Q(1, 27))
    check("dominant_slack_value", dominant_slack == Q(77, 486), "slack bound=77/486")
    check("dominant_slack_comparison", Q(77, 486) < Q(4, 25), "77/486<4/25<(sqrt2-1)^2")
    # Exact fourth and sixth moments for a rational normalized sign vector.
    coefficients = [Q(2, 3), Q(2, 3), Q(1, 3)]
    samples = [sum(a*e for a, e in zip(coefficients, signs)) for signs in product([-1, 1], repeat=3)]
    K, L = sum(a**4 for a in coefficients), sum(a**6 for a in coefficients)
    check("Rademacher_variance_identity", sum(x*x for x in samples)/8 == 1, "sum a_i^2=1")
    check("Rademacher_fourth_identity", sum(x**4 for x in samples)/8 == 3-2*K, "E X^4=3-2K")
    check("Rademacher_sixth_identity", sum(x**6 for x in samples)/8 == 15-30*K+16*L,
          "E X^6=15-30K+16L")
    return checks


def local_query(n, site, local):
    U = np.ones((1, 1), complex)
    for j in range(n):
        U = np.kron(U, local if site == j else I)
    return U


def norm1_hermitian(matrix):
    return float(np.sum(np.abs(np.linalg.eigvalsh(matrix))))


def trace_root(matrix):
    values = np.linalg.eigvalsh(matrix)
    require(min(values) >= -TOL, "matrix under square root is positive")
    return float(np.sum(np.sqrt(np.maximum(values, 0))))


def binary_entropy(p):
    return float(-sum(x*np.log2(x) for x in [p, 1-p] if x > 0))


def fixtures():
    B = (X+Z)/R2
    n = 3
    v = np.array([1, 2j, -2, 1+1j, 3-1j, -1j, 2+3j, -2j], complex)
    v /= np.linalg.norm(v)
    V = np.eye(8)-2*np.outer(v, v.conj())
    householder = V@local_query(n, 0, Z)@V.conj().T
    indices = np.arange(16)
    fourier = np.exp(2j*np.pi*np.outer(indices, indices)/16)/4
    phases = np.exp(1j*np.array([0, .2, -.5, .7, 1.1, -.8, .4, -.3,
                               .6, -.9, .1, .8, -.2, .3, -1., .5]))
    V4 = phases[:, None]*fourier
    fourier_reflection = V4@np.diag([1]*8+[-1]*8)@V4.conj().T
    majority = np.diag([1 if sum(signs) > 0 else -1
                        for signs in product([1, -1], repeat=3)])
    majority4 = np.kron(majority, I)
    entangling = (np.kron(Z, I)+np.kron(X, X))/R2
    return [("one_qubit_bisector_mixed", B, 1, 3/5, "equality"),
            ("one_qubit_Y_mixed", Y, 1, 4/5, "strict"),
            ("two_qubit_entangling_half_rank", entangling, 2, 1., "strict"),
            ("three_qubit_complex_Householder", householder, 3, 5/13, "complex"),
            ("four_qubit_complex_Fourier", fourier_reflection, 4, 4/5, "complex"),
            ("five_qubit_retention_half_rank", local_query(5, 2, B), 5, 1., "equality"),
            ("five_qubit_retention_mixed", local_query(5, 4, (X-Z)/R2), 5, 3/5, "equality"),
            ("three_qubit_zero_bias_endpoint", householder, 3, 0., "zero"),
            ("four_qubit_classical_majority", majority4, 4, 12/13, "diffuse"),
            ("two_qubit_single_X_mixed", local_query(2, 0, X), 2, 4/5, "strict")]


def reflection_case(name, R, n, t, kind):
    errors, margins = {}, {}
    dimension = len(R)
    identity = np.eye(dimension, dtype=complex)
    tau = lambda matrix: np.trace(matrix)/dimension
    compare(errors, "Hermitian_reflection", R, R.conj().T)
    compare(errors, "reflection_square", R@R, identity)
    compare(errors, "reflection_balanced", tau(R), 0)
    reflection_values, reflection_vectors = np.linalg.eigh(R)
    reflection_signs = np.where(reflection_values >= 0, 1., -1.)
    spectral_probabilities = (1+t*reflection_signs)/dimension
    rho = (identity+t*R)/dimension
    root = ((np.sqrt(1+t)+np.sqrt(1-t))*identity +
            (np.sqrt(1+t)-np.sqrt(1-t))*R)/(2*np.sqrt(dimension))
    compare(errors, "state_root_square", root@root, rho)
    compare(errors, "state_trace", np.trace(rho), 1)
    eigenvalues = np.linalg.eigvalsh(rho)
    nonnegative(margins, "state_positive", min(eigenvalues))
    entropy = -sum(value*np.log2(value) for value in eigenvalues if value > TOL)
    entropy_formula = n-1+binary_entropy((1+t)/2)
    compare(errors, "balanced_entropy_formula", entropy, entropy_formula)
    z_original, z_affinity = t*t, 1-np.sqrt(1-t*t)
    rows, coefficients = [], []
    for site in range(n):
        pair = []
        for axis, local in [("X", X), ("Z", Z)]:
            U = local_query(n, site, local)
            label = f"site{site}_{axis}"
            coefficient = float(tau(R@U).real)
            pair.append(coefficient)
            commutator = R@U-U@R
            C = commutator.conj().T@commutator/4
            q = float(tau(C).real)
            compare(errors, label+"_C_Hermitian", C, C.conj().T)
            compare(errors, label+"_C_commutes_R", C@R, R@C)
            compare(errors, label+"_C_commutes_U", C@U, U@C)
            compare(errors, label+"_energy_trace_formula", q, (1-float(tau(R@U@R@U).real))/2)
            c_values = np.linalg.eigvalsh(C)
            nonnegative(margins, label+"_C_positive", min(c_values))
            nonnegative(margins, label+"_C_contraction", 1-max(c_values))
            F = norm1_hermitian(root@U@root)
            affinity = float(np.trace(root@U@root@U).real)
            exact_F = trace_root(identity-z_original*C)/dimension
            spectral_U = reflection_vectors.conj().T@U@reflection_vectors
            sums = spectral_probabilities[:, None]+spectral_probabilities[None, :]
            differences = spectral_probabilities[:, None]-spectral_probabilities[None, :]
            sld_weights = np.divide(differences*differences, sums,
                                    out=np.zeros_like(sums), where=sums > 0)
            sld = float(np.sum(sld_weights*abs(spectral_U)**2)/2)
            compare(errors, label+"_SLD_two_level_identity", sld, t*t*q)
            compare(errors, label+"_exact_two_reflection_score", F, exact_F)
            compare(errors, label+"_exact_affinity_formula", affinity, 1-z_affinity*q)
            nonnegative(margins, label+"_original_Jensen", np.sqrt(max(0., 1-z_original*q))-F)
            nonnegative(margins, label+"_SLD_score_bound", 1-sld-F*F)
            nonnegative(margins, label+"_fidelity_affinity", affinity-F*F)
            rows.append(dict(site=site, axis=axis, singleton_coefficient=coefficient,
                             energy=q, original_score=F, affinity=affinity))
        coefficients.append(pair)
    coefficients = np.array(coefficients)
    site_weights = np.sum(coefficients**2, axis=1)
    W, b = float(sum(site_weights)), float(max(site_weights))
    energy = sum(row["energy"] for row in rows)
    nonnegative(margins, "singleton_weight_cap", 1-W)
    nonnegative(margins, "energy_Pauli_bound", energy-(2-W))
    if W > TOL:
        amplitudes = np.sqrt(site_weights/W)
        m = float(np.mean([abs(np.dot(amplitudes, signs))
                           for signs in product([-1, 1], repeat=n)]))
        A = b/W
        H = sum(coefficients[site, j]*local_query(n, site, local)
                for site in range(n) for j, local in enumerate([X, Z]))
        compare(errors, "singleton_duality_identity", tau(R@H), W)
        compare(errors, "singleton_Rademacher_spectrum", norm1_hermitian(H)/dimension, np.sqrt(W)*m)
        nonnegative(margins, "singleton_duality_bound", m*m-W)
        if A <= 3/4+TOL:
            nonnegative(margins, "diffuse_nine_tenths_gate", .9-m)
        else:
            nonnegative(margins, "dominant_Rademacher_gate", (2-R2)-m*m*(1-(R2-1)*A))
    else:
        A, m = 0., 0.
    selected = int(np.argmax(site_weights))
    for j, axis in enumerate(["X", "Z"]):
        row = rows[2*selected+j]
        nonnegative(margins, f"selected_{axis}_opposite_singleton", row["energy"]-coefficients[selected, 1-j]**2)
    responses = []
    for label, z in [("original", z_original), ("affinity", z_affinity)]:
        response = float(sum(np.sqrt(max(0., 1-z*row["energy"])) for row in rows))
        target = 2*n-2+2*np.sqrt(1-z/2)
        deficit = 2*n-response
        grouped = z*(2-W-b)/2+2*(1-np.sqrt(1-z*b/2))
        nonnegative(margins, label+"_response_bound", target-response)
        nonnegative(margins, label+"_grouped_response_bound", deficit-grouped)
        if W <= 2*(R2-1)+TOL:
            nonnegative(margins, label+"_diffuse_linear_bound", deficit-z*(2-W)/2)
        if W-(R2-1)*b <= (2-R2)+TOL:
            nonnegative(margins, label+"_dominant_grouped_gate", grouped-(2-2*np.sqrt(1-z/2)))
        if kind in ("equality", "zero"):
            compare(errors, label+"_attains_response_curve", response, target)
        responses.append(dict(kind=label, z=z, response=response, sharp_upper_bound=target))
    g = sum(row["original_score"] for row in rows)
    G = sum(np.sqrt(max(0., row["affinity"])) for row in rows)
    g_target = 2*n-2+np.sqrt(4-2*t*t)
    G_target = 2*n-2+np.sqrt(2+2*np.sqrt(1-t*t))
    compare(errors, "affinity_equals_abstract_response", G, responses[1]["response"])
    nonnegative(margins, "original_balanced_spectrum_bound", g_target-g)
    nonnegative(margins, "affinity_balanced_spectrum_bound", G_target-G)
    nonnegative(margins, "balanced_curve_below_entropy_line", R2*n+(2-R2)*entropy-g_target)
    if kind in ("equality", "zero"):
        compare(errors, "attains_original_spectrum_curve", g, g_target)
        compare(errors, "attains_affinity_spectrum_curve", G, G_target)
    return dict(name=name, ambient_qubits=n, matrix_dimension=dimension, bias=t,
                state_rank=int(sum(eigenvalues > TOL)), entropy_bits=float(entropy),
                singleton_weight=W, maximum_site_weight=b, normalized_maximum_site_weight=A,
                Rademacher_first_moment=m, total_query_energy=energy,
                original_score=g, affinity_score=G, original_sharp_bound=g_target,
                affinity_sharp_bound=G_target, query_data=rows, response_data=responses,
                relative_identity_residuals=errors, inequality_margins=margins)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source = Path(__file__).resolve()
    repository = source.parents[1]
    note = repository/NOTE
    if args.output:
        destination = args.output.resolve()
        if destination in [source, note.resolve()] or destination.suffix != ".json":
            raise ValueError("Output must be JSON and cannot overwrite source or proof note")
    exact = exact_checks()
    rows = [reflection_case(*case) for case in fixtures()]
    residuals = [value for row in rows for value in row["relative_identity_residuals"].values()]
    margins = [value for row in rows for value in row["inequality_margins"].values()]
    report = dict(status="exact scalar comparisons and fixed constructions passed", research_base=BASE,
                  python=platform.python_version(), numpy=np.__version__, tolerance=TOL,
                  source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  proof_note_sha256={NOTE: hashlib.sha256(note.read_bytes()).hexdigest()},
                  exact_comparisons=exact, constructions=rows, maximum_matrix_dimension=32,
                  exact_comparison_count=len(exact), fixed_construction_count=len(rows),
                  query_count=sum(len(row["query_data"]) for row in rows),
                  matrix_identity_count=len(residuals), inequality_count=len(margins),
                  maximum_relative_identity_residual=max(residuals), minimum_inequality_margin=min(margins),
                  scope="Exact Fraction algebra checks the degree-six Rademacher majorant, moment identities, three diffuse intervals and dominant-tail rational comparisons. Ten fixed balanced reflections on one through five qubits check original-query commutators, singleton/Rademacher duality, grouped response bounds, exact balanced-spectrum trace norms and affinities, entropy, and bisector attainment. Each reflection uses one deliberate bias; these fixtures form no parameter grid. Matrices have dimension at most 32. The all-dimension theorem and equality classification are analytical in the proof note; finite floating-point checks do not establish those quantified claims or publication novelty. No random sampling or optimization.")
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
