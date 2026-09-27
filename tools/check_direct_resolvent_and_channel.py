#!/usr/bin/env python3
"""Bounded construction checks for three direct converse/channel deductions.

Exact rational witnesses and thirteen fixed small constructions supplement the
analytical proofs. There is no parameter grid, optimization, or interval solver.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


BASE = "7cb964b47b8aa13a604a3ab5df663d4f399fa6f4"
TOL = 3e-9
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
R = float(np.sqrt(2))
PAULIS = dict(I=I, X=X, Y=Y, Z=Z)
NOTES = ["ACTIVE_PLANE_REVERSE_RESOLVENT.md", "ONE_AXIS_EB_REPAIR.md",
         "CONTROLLED_PHASE_PAIR_CONVERSE.md"]


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def kron(*matrices):
    result = np.ones((1, 1), dtype=complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def word(letters):
    return kron(*(PAULIS[letter] for letter in letters))


def compare(errors, label, actual, expected):
    residual = float(np.linalg.norm(np.asarray(actual)-np.asarray(expected)) /
                     max(1, np.linalg.norm(expected)))
    errors[label] = residual
    require(residual <= TOL, label)


def positive(margins, label, matrix):
    require(np.linalg.norm(matrix-matrix.conj().T) <= TOL*max(1, np.linalg.norm(matrix)),
            label+" Hermitian")
    minimum = float(np.linalg.eigvalsh(matrix)[0])
    margins[label] = minimum
    require(minimum >= -TOL, label)


def earlier_hamiltonian(pairs):
    n = len(pairs)
    dimension = len(pairs[0][0])
    result = np.zeros((2**n*dimension, 2**n*dimension), dtype=complex)
    for index, (b, d) in enumerate(pairs):
        for axis, matrix in [(X, b), (Z, d)]:
            factors = [I]*n
            factors[index] = axis
            result += kron(*factors, matrix)
    return result


def lift_earlier(matrix, references, dimension):
    return np.kron(matrix, I).reshape(references, dimension, 2, references, dimension, 2).transpose(
        0, 2, 1, 3, 5, 4).reshape(2*references*dimension, 2*references*dimension)


def memory_trace(matrix, references, dimension):
    return np.einsum("aqap->qp", matrix.reshape(references, dimension, references, dimension))


def plane_trace(matrix, references):
    return np.einsum("aqbq->ab", matrix.reshape(references, 2, references, 2))/2


def f_matrix(matrix, a):
    return matrix @ np.linalg.inv(np.eye(len(matrix))+a*matrix)


def exact_checks():
    checks = {}

    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness

    check("sqrt2_lower", F(141, 100)**2 < 2, "141^2<2*100^2")
    check("sqrt2_upper", 2 < F(3, 2)**2, "2<9/4")
    check("sqrt3_lower", F(1732, 1000)**2 < 3, "1732^2<3*1000^2")
    check("reflection_rotation", F(399, 401)**2+F(40, 401)**2 == 1,
          "399^2+40^2=401^2")
    check("top_radical_upper", 144841 < 381**2, "sqrt144841<381")
    check("reflection_top_upper", F(2442000, 694532) < F(71, 20),
          "2442000/694532<71/20")
    check("plane_zeta_upper", F(4, 3) < F(6, 5)**2, "2/sqrt3<6/5")
    check("last_excess_upper", F(7, 5)**2 < 2, "2-sqrt2<3/5")
    check("repaired_reflection_margin", 16-F(71, 20)**2-F(26, 5)*F(3, 5) == F(111, 400),
          "16-(71/20)^2-(26/5)(3/5)=111/400")
    check("active_angle", F(3, 5)**2+F(4, 5)**2 == 1, "3^2+4^2=5^2")
    check("active_spectral_circle", F(18, 5)+F(2, 5) == 4, "u^2+v^2=18/5+2/5=4")
    check("all_angle_cutoff_n1", 4-2 == 2, "4N^2-2N=2 at N=1")
    check("all_angle_cutoff_n2", 16-4 == 12, "4N^2-2N=12 at N=2")
    check("all_angle_cutoff_n3", 36-6 == 30, "4N^2-2N=30 at N=3")
    check("repair_identity_distance", 2*F(1)/(1+F(1)) == 1, "2n/(1+n)=1 at n=1")
    check("repair_head_distance", 2*F(1, 4)/(1+F(1, 4)) == F(2, 5), "n=1/4 gives 2/5")
    check("repair_stronger_axis_threshold", F(2, 3)/2 == F(1, 3), "axis norm 2/3 gives n=1/3")
    check("amplitude_damping_half_axis", 1-F(3, 4) == F(1, 2)**2, "gamma=3/4 gives n=1/2")
    check("amplitude_damping_quarter_axis", 1-F(15, 16) == F(1, 4)**2, "gamma=15/16 gives n=1/4")
    check("unequal_readout_angle", F(1, 5)**2+F(7, 5)**2 == 2, "(1/5)^2+(7/5)^2=2")
    check("flux_top_cap", 3*80**2 < 139**2, "4sqrt3-3<79/20")
    check("flux_tail_sum", 77 < 9**2, "(3+sqrt77)/2<6")
    check("flux_quadratic_endpoint_zero", F(9121, 400)-F(81, 5)*F(141, 100) == -F(79, 2000),
          "Q(79/20,0)<-79/2000")
    check("flux_quadratic_endpoint_switch", F(561, 50)-8*F(141, 100) == -F(3, 50),
          "Q(79/20,41/20)<-3/50")
    def channel_polynomial(t):
        return t**3-F(43, 7)*t*t+F(1081, 350)*t+F(467, 35)

    check("channel_cubic_left_endpoint", channel_polynomial(F(12, 5)) == -F(703, 875),
          "P(12/5)=-703/875")
    check("channel_cubic_right_endpoint", channel_polynomial(F(17, 4)) == -F(86469, 11200),
          "P(17/4)=-86469/11200")
    check("channel_cubic_convexity", 6*F(12, 5)-F(86, 7) == F(74, 35),
          "P''(12/5)=74/35>0")
    check("channel_sqrt2_upper", 2 < F(99, 70)**2, "sqrt2<99/70")
    check("channel_linear_endpoint", (24*F(99, 70)-34)/5 == -F(2, 175),
          "L(4+sqrt2)=(24sqrt2-34)/5<-2/175")
    return checks


def reflection_pairs():
    a, b, c, s = 2/np.sqrt(3), np.sqrt(2/3), 399/401, 40/401
    return [((a*word("ZI")+b*word("XI"))/R, (a*word("ZI")-b*word("XI"))/R),
            ((a*c*word("IZ")-b*s*word("ZZ")+b*c*word("ZX")+a*s*word("IX"))/R,
             (a*c*word("IZ")-b*s*word("ZZ")-b*c*word("ZX")-a*s*word("IX"))/R)]


def active_plane_checks():
    b1 = np.diag([.3, -.3, .06]).astype(complex)
    d1 = np.array([[0, .4, 0], [.4, 0, 0], [0, 0, .04]], dtype=complex)
    rotation = (4*np.eye(4)+3j*word("XX"))/5
    cases = [("N1_odd_memory", [(b1, d1)], np.eye(3, dtype=complex), 3/5, 4/5),
             ("N2_reflection_obstruction_repaired", reflection_pairs(), np.eye(4, dtype=complex), 0., 1.),
             ("N3_complex_rotated_plane", [(.8*word("XI"), .8*word("ZI")),
                                           (.7*word("IX"), .7*word("IZ")),
                                           (.6*word("XX"), .6*word("ZZ"))], rotation, 3/5, 4/5)]
    records = []
    for name, pairs, rotation, cosine, sine in cases:
        errors, margins = {}, {}
        n, dimension = len(pairs), len(rotation)
        refs = 2**n
        compare(errors, "plane_rotation_unitary", rotation.conj().T @ rotation, np.eye(dimension))
        for index, pair in enumerate(pairs):
            for axis, matrix in zip("BD", pair):
                compare(errors, f"readout_{index}_{axis}_Hermitian", matrix, matrix.conj().T)
                positive(margins, f"readout_{index}_{axis}_contraction", np.eye(dimension)-matrix @ matrix)
        w = rotation[:, :2]
        p = w @ w.conj().T
        b3 = w @ Z @ w.conj().T+np.eye(dimension)-p
        d3 = w @ (cosine*Z+sine*X) @ w.conj().T+np.eye(dimension)-p
        for label, matrix in [("B", b3), ("D", d3)]:
            compare(errors, "last_"+label+"_reflection", matrix @ matrix, np.eye(dimension))
        h0 = earlier_hamiltonian(pairs)
        upper = float(np.linalg.norm(h0, 2))
        zeta = sum(float(np.hypot(np.trace(p @ b).real/2, np.trace(p @ d).real/2)) for b, d in pairs)
        h3 = kron(X, b3)+kron(Z, d3)
        u, v = np.sqrt(2+2*sine), np.sqrt(2-2*sine)
        x, a, b = u-R, R-v, u-v
        root = float((x+np.sqrt(x*x+4*upper*upper+4*zeta*x))/2)
        compare(errors, "quantitative_root_equation", root*root-upper*upper, (root+zeta)*x)
        require(root+R <= upper+u+TOL, "quantitative bound improves triangle")
        # Use the benchmark A=2N to avoid a nearly saturated inverse comparison.
        scalar = 2*n
        c = scalar*scalar-upper*upper
        require(c > 0 and c >= (scalar+zeta)*x-TOL, "active-plane benchmark condition")
        k = scalar*np.eye(len(h0))-h0
        inverse = np.linalg.inv(k)
        positive(margins, "spectral_chord", (scalar*np.eye(len(h0))+h0)/c-inverse)
        insertion = kron(np.eye(refs), w)
        plane = kron(np.eye(refs), p)
        t = insertion.conj().T @ inverse @ insertion
        d = (scalar*np.eye(2*refs)+insertion.conj().T @ h0 @ insertion)/c
        positive(margins, "compressed_chord", d-t)
        compressed = insertion.conj().T @ np.linalg.inv(k+a*plane) @ insertion
        compare(errors, "exact_compressed_Woodbury", compressed, f_matrix(t, a))
        positive(margins, "operator_monotonicity", f_matrix(d, a)-f_matrix(t, a))
        e_d = plane_trace(d, refs)
        positive(margins, "normalized_trace_Jensen", f_matrix(e_d, a)-plane_trace(f_matrix(d, a), refs))
        scalar_bound = (scalar+zeta)/(c+a*(scalar+zeta))
        positive(margins, "scalar_resolvent_bound", scalar_bound*np.eye(refs)-plane_trace(compressed, refs))
        eigenvalues, eigenvectors = np.linalg.eigh(h3)
        top = eigenvectors[:, -1:]
        compare(errors, "active_top_eigenvalue", eigenvalues[-1], u)
        compare(errors, "Bell_active_marginal", memory_trace(top @ top.conj().T, 2, dimension), p/2)
        majorant = R*np.eye(2*dimension)-a*kron(I, p)+b*top @ top.conj().T
        positive(margins, "last_query_Bell_majorant", majorant-h3)
        bell_insertion = kron(np.eye(refs), top)
        bell_compression = bell_insertion.conj().T @ lift_earlier(np.linalg.inv(k+a*plane), refs, dimension) @ bell_insertion
        compare(errors, "Bell_normalized_partial_trace", bell_compression, plane_trace(compressed, refs))
        positive(margins, "reverse_Bell_test", np.eye(refs)-b*bell_compression)
        actual_norm = float(np.linalg.norm(lift_earlier(h0, refs, dimension)+kron(np.eye(refs), h3), 2))
        require(actual_norm <= R+root+TOL, "actual norm below quantitative bound")
        if n == 2:
            compare(errors, "PR49_actual_plane_zeta", zeta, 2/np.sqrt(3))
            require(16-upper*upper-(4+zeta)*(2-R) > 111/400, "PR49 exact positive margin")
            require(upper > 2*np.sqrt(3), "PR49 repair exceeds universal all-plane cutoff")
        records.append({"name": name, "earlier_queries": n, "memory_dimension": dimension,
                        "U": upper, "zeta": zeta, "last_u": float(u), "last_v": float(v),
                        "benchmark_margin": float(c-(scalar+zeta)*x), "actual_norm": actual_norm,
                        "quantitative_bound": R+root, "triangle_bound": upper+float(u),
                        "relative_identity_residuals": errors, "positive_matrix_minima": margins})
    return records


def choi(images):
    return (kron(I, images[0])+kron(X, images[1])-kron(Y, images[2])+kron(Z, images[3]))/4


def partial_transpose(matrix, dimension):
    return matrix.reshape(2, dimension, 2, dimension).transpose(2, 1, 0, 3).reshape(2*dimension, 2*dimension)


def input_marginal(matrix, dimension):
    return np.einsum("aqbq->ab", matrix.reshape(2, dimension, 2, dimension))


def trace_norm(matrix):
    return float(np.sum(np.linalg.svd(matrix, compute_uv=False)))


def amplified_dual(images, matrix):
    dimension = len(images[0])
    result = np.zeros((4, 4), dtype=complex)
    for row in range(2):
        for column in range(2):
            block = matrix[row*dimension:(row+1)*dimension, column*dimension:(column+1)*dimension]
            result[2*row:2*row+2, 2*column:2*column+2] = sum(
                np.trace(image @ block)*axis/2 for image, axis in zip(images, [I, X, Y, Z]))
    return result


def channel_checks():
    w = np.array([[1, 0], [0, 1], [0, 1j], [1j, 0]], dtype=complex)/R

    def damping(gamma, isometry):
        return [isometry @ np.diag([1, np.sqrt(1-gamma)]),
                isometry @ np.array([[0, np.sqrt(gamma)], [0, 0]])]

    cases = [("identity_endpoint", [I], 1.), ("dephasing_zero_axis", [(I+Z)/2, (I-Z)/2], 0.),
             ("amplitude_damping", damping(3/4, I), .5),
             ("D4_complex_embedded_damping", damping(15/16, w), .25)]
    records = []
    for name, kraus, expected_n in cases:
        errors, margins = {}, {}
        dimension = len(kraus[0])
        compare(errors, "Kraus_trace_preserving", sum(k.conj().T @ k for k in kraus), I)
        images = [sum(k @ axis @ k.conj().T for k in kraus) for axis in [I, X, Y, Z]]
        original = choi(images)
        positive(margins, "original_Choi", original)
        compare(errors, "original_input_marginal", input_marginal(original, dimension), I/2)
        m = images[2]
        values, vectors = np.linalg.eigh(m)
        mplus = (vectors*np.maximum(values, 0)) @ vectors.conj().T
        mminus = (vectors*np.maximum(-values, 0)) @ vectors.conj().T
        n = trace_norm(m)/2
        compare(errors, "axis_trace_distance", n, expected_n)
        compare(errors, "axis_traceless", np.trace(m), 0)
        compare(errors, "Jordan_positive_trace", np.trace(mplus), n)
        compare(errors, "Jordan_negative_trace", np.trace(mminus), n)
        correction = (kron(I, mplus+mminus)+kron(Y, m))/4
        compare(errors, "separable_correction_formula", correction,
                (kron((I+Y)/2, mplus)+kron((I-Y)/2, mminus))/2)
        positive(margins, "correction_positive", correction)
        compare(errors, "correction_input_marginal", input_marginal(correction, dimension), n*I/2)
        if n > TOL:
            theta_images = [(np.trace((I-Y) @ axis/2)*mplus+np.trace((I+Y) @ axis/2)*mminus)/n
                            for axis in [I, X, Y, Z]]
            compare(errors, "opposite_labels_kill_axis", theta_images[2], -m/n)
            compare(errors, "Theta_Choi_sign", choi(theta_images), correction/n)
            repaired_images = [(image+n*theta)/(1+n) for image, theta in zip(images, theta_images)]
        else:
            repaired_images = images
        repaired = choi(repaired_images)
        compare(errors, "repaired_Choi_formula", repaired, (original+correction)/(1+n))
        compare(errors, "repaired_axis_zero", repaired_images[2], np.zeros_like(m))
        compare(errors, "repaired_input_marginal", input_marginal(repaired, dimension), I/2)
        compare(errors, "partial_transpose_invariance", partial_transpose(repaired, dimension), repaired)
        positive(margins, "repaired_Choi", repaired)
        positive(margins, "repaired_partial_transpose", partial_transpose(repaired, dimension))
        bound = 2*n/(1+n)
        choi_distance = trace_norm(original-repaired)
        require(choi_distance <= bound+TOL, "Choi distance no larger than analytical diamond upper bound")
        if name == "identity_endpoint":
            compare(errors, "identity_sharp_Choi_distance", choi_distance, 1)
            compare(errors, "identity_repair_Bell_overlap", np.trace(original @ repaired), .5)
        if dimension == 4:
            last_b, last_d = (word("XI")+word("YZ"))/R, (word("ZI")+word("YX"))/R
            t = 3.
            resolvent = np.linalg.inv(t*np.eye(8)-kron(X, last_b)-kron(Z, last_d))
            actual_test = amplified_dual(images, resolvent)
            repaired_test = amplified_dual(repaired_images, resolvent)
            theta_test = amplified_dual(theta_images, resolvent)
            compare(errors, "direct_channel_decomposition", actual_test, (1+n)*repaired_test-n*theta_test)
            positive(margins, "EB_repair_resolvent_upper", pure_support(t)*np.eye(4)-repaired_test)
            positive(margins, "EB_correction_resolvent_lower", theta_test-np.eye(4)/(t+R))
            direct_upper = (1+n)*pure_support(t)-n/(t+R)
            positive(margins, "direct_repair_resolvent_upper", direct_upper*np.eye(4)-actual_test)
        records.append({"name": name, "output_dimension": dimension, "n": n,
                        "analytical_diamond_upper_bound": bound, "Choi_trace_distance": choi_distance,
                        "relative_identity_residuals": errors, "positive_matrix_minima": margins})
    return records


def pure_support(t):
    return 1/(t-R) if t >= 3*R else 1/(2*(np.sqrt(2*t*t-4)-t))


def flat_support(t):
    return max(1/(t-R), (t*t-2)/(t*(t*t-4)))


def copying_isometry(alpha, beta):
    result = np.zeros((16, 4), dtype=complex)
    for a in range(2):
        for b in range(2):
            memory = 2*a+b
            reference = 2*(a ^ (alpha < 0))+(b ^ (beta < 0))
            result[4*reference+memory, memory] = 1
    return result


def controlled_phase_checks():
    balanced_a, balanced_b = 2/np.sqrt(3), np.sqrt(2/3)
    cases = [("sharp_product_equality", 1., 1., 1., 1., 1., 0.),
             ("balanced_degenerate_head", balanced_a, balanced_b, balanced_a, balanced_b, 0., 1.),
             ("unequal_other_sector_second", 1., 1., .2, 1.4, 1., 0.),
             ("same_parity_head", balanced_a, balanced_b, balanced_a, balanced_b, .6, .8),
             ("negative_cosine_and_sine", balanced_a, balanced_b, balanced_a, balanced_b, -.6, -.8),
             ("zero_coefficient_triangle", 0., R, R, 0., .6, .8)]
    records = []
    for name, a, b, c, d, cosine, sine in cases:
        errors, margins = {}, {}
        w = cosine*word("IX")+sine*word("ZY")
        compare(errors, "phase_reflection", w @ w, np.eye(4))
        pairs = [((a*word("ZI")+b*word("XI"))/R, (a*word("ZI")-b*word("XI"))/R),
                 ((c*word("IZ")+d*w)/R, (c*word("IZ")-d*w)/R)]
        for index, pair in enumerate(pairs):
            for label, matrix in zip("BD", pair):
                compare(errors, f"original_{index}_{label}_reflection", matrix @ matrix, np.eye(4))
        h0 = a*word("ZIZI")+b*word("XIXI")+c*word("IZIZ")+d*kron(I, X, w)
        bisector = np.cos(np.pi/8)*I-1j*np.sin(np.pi/8)*Y
        reference_change = kron(bisector, bisector, np.eye(4))
        compare(errors, "original_readouts_bisector_change", earlier_hamiltonian(pairs),
                reference_change @ h0 @ reference_change.conj().T)
        f = b*word("XI")+d*w
        compare(errors, "square_loop_identity", f @ f, (b*b+d*d)*np.eye(4)+2*b*d*cosine*word("XX"))
        q, p = np.sqrt(b*b+d*d+2*b*d*abs(cosine)), np.sqrt(max(0, b*b+d*d-2*b*d*abs(cosine)))
        aa, difference = a+c, abs(a-c)
        expected = []
        for alpha in [-1, 1]:
            for beta in [-1, 1]:
                sector = copying_isometry(alpha, beta)
                compare(errors, f"copying_sector_{alpha}_{beta}", sector.conj().T @ h0 @ sector,
                        (alpha*a+beta*c)*np.eye(4)+f)
                expected.extend(alpha*a+beta*c+value for value in [q, p, -p, -q])
        values, vectors = np.linalg.eigh(h0)
        compare(errors, "complete_spectrum", values, np.sort(expected))
        upper, second, ell = map(float, values[[-1, -2, -3]])
        compare(errors, "top_formula", upper, aa+q)
        compare(errors, "second_formula", second, max(aa+p, difference+q))
        compare(errors, "scalar_energy_identity", aa*aa+difference*difference+p*p+q*q, 8)
        bound_test = None
        if upper <= 2+R+TOL:
            branch = "triangle"
        elif second <= 3+TOL or difference+q >= aa+p-TOL:
            branch = "flat_top_rank_one"
            top = vectors[:, -1:]
            compare(errors, "flat_top_marginal", memory_trace(top @ top.conj().T, 4, 4), np.eye(4)/4)
            bound_test = (upper-second)*flat_support(4+R-second)
            require(bound_test <= 1+TOL, "flat rank-one scalar criterion")
            if second > 3:
                require(2+R-second >= min(a, c)-TOL, "other-sector pole distance")
        else:
            branch = "same_parity_EB_head"
            head = vectors[:, [-1, -2]]
            compare(errors, "actual_third_formula", ell, max(aa-p, difference+q))
            for index, axis in enumerate([I, X, Y, Z]):
                output = memory_trace(head @ axis @ head.conj().T, 4, 4)
                compare(errors, f"copying_channel_diagonal_{index}", output, np.diag(np.diag(output)))
            require(ell < np.sqrt(7) and upper+ell < 6 and upper < 79/20, "same-parity exact coarse caps")
            bound_test = (upper-ell)*pure_support(4+R-ell)
            require(bound_test < 1, "EB actual-tail scalar criterion")
        third_b, third_d = ((np.eye(4), np.eye(4)) if name == "sharp_product_equality" else
                            ((word("XI")+word("YZ"))/R, (word("ZI")+word("YX"))/R))
        for label, matrix in [("B", third_b), ("D", third_d)]:
            compare(errors, "third_"+label+"_reflection", matrix @ matrix, np.eye(4))
        full = lift_earlier(h0, 4, 4)+kron(np.eye(4), kron(X, third_b)+kron(Z, third_d))
        actual_norm = float(np.linalg.norm(full, 2))
        require(actual_norm <= 4+R+TOL, "fixed third-pair converse")
        if name == "sharp_product_equality":
            compare(errors, "sharp_equality", actual_norm, 4+R)
        records.append({"name": name, "proof_branch": branch, "U": upper, "m": second,
                        "third_eigenvalue": ell, "scalar_envelope_test": bound_test,
                        "fixed_third_actual_norm": actual_norm, "relative_identity_residuals": errors,
                        "positive_matrix_minima": margins})
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    source = Path(__file__).resolve()
    repository = source.parents[1]
    notes = [repository/"docs/audits"/name for name in NOTES]
    if arguments.output:
        destination = arguments.output.resolve()
        if destination in [source, *(note.resolve() for note in notes)] or destination.suffix != ".json":
            raise ValueError("Output must be JSON and must not overwrite source or proof notes")
    report = {"status": "exact scalar and fixed construction checks passed", "research_base": BASE,
              "python": platform.python_version(), "numpy": np.__version__, "tolerance": TOL,
              "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
              "proof_note_sha256": {str(note.relative_to(repository)): hashlib.sha256(note.read_bytes()).hexdigest()
                                     for note in notes},
              "exact_constants": exact_checks(), "active_plane_constructions": active_plane_checks(),
              "channel_repair_constructions": channel_checks(), "controlled_phase_constructions": controlled_phase_checks(),
              "maximum_matrix_dimension": 64,
              "scope": "Thirteen fixed constructions: three active-plane examples with N=1,2,3 and memory dimensions 3,4,4; four qubit-input channels; six controlled-phase pairs. Universal assertions and the diamond-norm estimate are analytical, not certified by these finite checks. Numerical eigenvalues and inverses are floating-point diagnostics, not interval certificates. Choi trace distances are not diamond-norm computations. No parameter grid, optimizer, unrestricted converse, or novelty claim."}
    records = report["active_plane_constructions"]+report["channel_repair_constructions"]+report["controlled_phase_constructions"]
    residuals = [value for row in records for value in row["relative_identity_residuals"].values()]
    minima = [value for row in records for value in row["positive_matrix_minima"].values()]
    report["fixed_construction_count"] = len(records)
    report["exact_scalar_count"] = len(report["exact_constants"])
    report["matrix_identity_count"] = len(residuals)
    report["matrix_inequality_count"] = len(minima)
    report["maximum_relative_identity_residual"] = max(residuals)
    report["minimum_positive_matrix_eigenvalue"] = min(minima)
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
