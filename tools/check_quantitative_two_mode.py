#!/usr/bin/env python3
"""Exact scalar and fixed matrix checks for quantitative two-mode stability.

The universal statements are supplied analytical proofs in the two notes.
This verifier checks their rational constants and specified constructions;
it performs no optimization, parameter scan, or universal numerical test.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


RESEARCH_BASE = "3d230411930a2ac198cdb7f2ef9ad86701face1a"
TOLERANCE = 3e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = {"I": I, "X": X, "Y": Y, "Z": Z}


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


def norm1(matrix):
    return float(np.sum(np.linalg.svd(matrix, compute_uv=False)))


def partial_references(matrix, memory_dimension=4):
    return np.einsum("rqrs->qs", matrix.reshape(4, memory_dimension, 4, memory_dimension))


def compare(residuals, label, actual, expected):
    residual = float(np.linalg.norm(actual - expected) / max(1, np.linalg.norm(expected)))
    residuals[label] = residual
    require(residual <= TOLERANCE, label)


def exact_constant_checks():
    checks = {}

    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness

    eta = F(9, 100)
    check("flattening_minimum_square", 1 - eta - F(3, 10) == F(61, 100)
          and F(61, 100) > F(9, 16), "1-9/100-3/10=61/100>9/16")
    check("flattening_Young_coefficient", F(1) + F(1, 6) + F(3, 10) + F(9, 200)
          == F(907, 600) < F(49, 32), "907/600<49/32")
    check("flattening_cutoff", eta < F(49, 512), "9/100<49/512")
    check("flattening_final_coefficient", F(1, 2) + F(32, 49) * eta < F(9, 16),
          "1/2+(32/49)(9/100)<9/16")
    check("rational_sqrt_bounds", F(7, 5)**2 < 2 < F(99, 70)**2
          and 3 < F(26, 15)**2 and F(17, 10)**2 < 3
          and 5 < F(9, 4)**2,
          "7/5<sqrt(2)<99/70;17/10<sqrt(3)<26/15;sqrt(5)<9/4")

    q = F(1, 4096)
    check("rounding_projection_9", 2 * F(99, 70) + 6 + F(9, 2) * q < 9,
          "2(99/70)+6+(9/2)/4096<9")
    check("rounding_square_19", 9 * (2 + 9 * q) < 19, "9(2+9/4096)<19")
    check("signed_compression_8", 2 / (F(1, 2) - F(3, 4) * q) + 2 + F(26, 15) < 8,
          "2/(1/2-3/(4*4096))+2+26/15<8")
    check("integrated_signed_compression_8", 2 / (F(1, 2) - F(3, 4) * q)
          + 2*F(26, 15) + 2*q < 8,
          "2/(1/2-3/(4*4096))+2(26/15)+2/4096<8")
    check("coefficient_compression_35", F(19, 2) * F(26, 15) + 18 < 35,
          "(19/2)(26/15)+18<35")
    check("coefficient_commutator_42", 19 * F(26, 15) + 9 < 42,
          "19(26/15)+9<42")
    check("coefficient_square_45", 43**2 + 42**2 < 61**2 < F(19, 10) * 45**2,
          "43^2+42^2<61^2<(19/10)45^2")
    check("faithful_support_marginal", 2 - 9 * q >= F(19, 10), "2-9/4096>19/10")
    check("coefficient_eigenvalue_interval", F(12, 25)**2 < F(1, 4) - 45*q
          and F(1, 4) + 45*q < F(13, 25)**2,
          "(12/25)^2<1/4-45/4096<1/4+45/4096<(13/25)^2")
    check("definite_coefficient_exclusion", 2 * F(12, 25)**2 * F(7, 5) > F(19, 2) * q,
          "2(12/25)^2(7/5)>(19/2)/4096")
    check("sign_rounding_46", 45 / F(49, 50) < 46, "45/(49/50)<46")
    check("Bloch_axes_147", F(99, 70) * (F(19, 2) + F(51, 25) * 46) < 147,
          "(99/70)(19/2+(51/25)46)<147")
    check("axis_alignment_range", 147*q < F(1, 2), "147/4096<1/2")
    check("reflection_and_channel_constants", 9 + 4*(46 + 2*147) == 1369
          and 1369 + 3 == 1372 < 1500, "1369+3=1372<1500")
    check("conditional_radius", F(1500, 4096) < F(2, 5), "1500*5<2*4096")
    check("aligned_root_state_343", F(3, 4) + F(1369, 4) == 343,
          "3/4+1369/4=343")
    check("unconditional_correlation_gap", F(343, 65536) < F(1, 64)
          and F(17, 80)-F(1, 32) > F(1, 8) and F(17, 80) > F(1, 5),
          "343/65536<1/64;17/80-1/32>1/8;17/80>1/5")
    check("sign_divided_difference_13", 4/(F(1, 8)+F(1, 5)) < 13,
          "4/(1/8+1/5)=160/13<13")
    check("actual_decoder_loss_7", 32 < 36 < F(49, 2)*F(17, 10),
          "sqrt(32 epsilon)<6sqrt(epsilon)<7q")
    check("actual_decoder_18000", 52*343+7 == 17843 < 18000,
          "52*343+7=17843<18000")
    check("unconditional_radius", F(18000, 65536) < F(1, 3), "18000*3<65536")
    check("boundary_norm_gap", F(17, 2) / F(17, 10) == 5
          and F(4, 3)**2 < 2, "C_star<5;16/3<4+sqrt(2)")

    def low(t):
        return t*t/2 - F(77, 20)*t + F(629, 100)

    def high(t):
        return F(4, 5)*(t-F(19, 10))*(t-F(10, 7)) - (F(19, 10)-F(10, 7))*(t*t-4)

    low_values = [low(F(12, 5)), low(F(17, 4))]
    high_values = [high(F(4)), high(F(11, 2))]
    check("low_quadratic_endpoints", low_values == [F(-7, 100), F(-833, 800)],
          [str(value) for value in low_values])
    check("high_quadratic_endpoints", high_values == [F(-234, 175), F(-909, 1400)],
          [str(value) for value in high_values])
    check("convex_quadratic_leading_coefficients", F(4, 5) - F(19, 10) + F(10, 7)
          == F(23, 70) > 0, "q_low leading1/2;q_high leading23/70")
    # Equality of the quadratic coefficients checks the radical majorant
    # (3t/2-7/10)^2-(2t^2-4)=(t-21/5)^2/4+2/25.
    check("resolvent_radical_majorant", F(9, 4)-2 == F(1, 4)
          and -3*F(7, 10) == -F(21, 10)
          and F(49, 100)+4 == F(441, 100)+F(2, 25),
          "(3t/2-7/10)^2-(2t^2-4)=(t-21/5)^2/4+2/25")
    check("strip_gap_integer", 6*1600**2 - 3919**2 == 1439 > 0,
          "6*1600^2-3919^2=1439")
    check("strip_tail_and_rectangle", 121 < 128 and 18 < F(17, 4)**2
          and 2 < F(10, 7)**2, "11<8sqrt(2);3sqrt(2)<17/4;sqrt(2)<10/7")

    check("NPT_parameter_bounds", F(6, 5)**2 < F(3, 2) < F(5, 4)**2
          and F(1, 2) < F(3, 4)**2 and F(3, 4) < F(7, 8)**2,
          "6/5<a<5/4;b<3/4;ab<7/8")
    check("NPT_energy_bounds", 7 + 4*F(6, 5)*F(19, 20) == F(17, 5)**2
          and 6 + 4*F(6, 5)*F(19, 20) > F(21, 2),
          "U>17/5;d>21/2 on c>=19/20")
    alpha_derivative_upper = 2*(3+F(5, 4))/F(17, 5)**3
    gamma_derivative_upper = F(7, 8)*(17+30*F(5, 4)+12*F(5, 4)**2)/(9*F(17, 5)**3)
    check("NPT_derivative_bounds", alpha_derivative_upper < F(1, 4)
          and gamma_derivative_upper < F(1, 4),
          {"alpha_upper": str(alpha_derivative_upper), "gamma_upper": str(gamma_derivative_upper)})
    check("NPT_linear_coefficient_bounds", 1/F(17, 5) < F(3, 10)
          and 2*F(3, 4)/F(21, 2) < F(3, 20)
          and 2*F(7, 8)/(F(17, 5)*F(21, 2)) < F(1, 20),
          "|beta|<3s/10;|eta|<3s/20;|delta|<s/20")
    check("NPT_arc_distance", 1-F(19, 20)**2 < F(5, 16)**2
          and F(5, 16)+F(1, 20) == F(29, 80) < F(2, 5), "29/80<2/5")
    check("NPT_arc_overlap", 567**2-2*400**2 == 1489 > 0 and 81 < 128,
          "567^2-2*400^2=1489;81<128;19/20<c_star<1")
    return {"count": len(checks), "witnesses": checks, "uses_floating_point": False}


def npt_family_checks():
    records = []
    a, b = np.sqrt(1.5), 1/np.sqrt(2)
    logical = [word("IXIX"), word("XXXY"), word("XIXZ")]
    for rational_c in [F(19, 20), F(1), F(39999, 40001)]:
        c = float(rational_c)
        s = np.sqrt(max(0, 1-c*c))
        upper, tail = np.sqrt(7+4*a*c), np.sqrt(7-4*a*c)
        denominator = 6+4*a*c
        h = a*word("ZIZI") + b*word("XIXI") + c*word("IZIZ") + s*word("IZYY")
        h += c*word("IXZX") - s*word("IXXI")
        projection = (np.eye(16)+word("ZZZZ")) @ (h@h-np.eye(16)) @ (np.eye(16)+h/upper)/(4*denominator)
        residuals = {}
        compare(residuals, "projector", projection@projection, projection)
        compare(residuals, "projector_trace", np.trace(projection), 2)
        compare(residuals, "leading_eigenhead", h@projection, upper*projection)
        expected_spectrum = sorted([-upper]*2+[-tail]*2+[-1]*4+[1]*4+[tail]*2+[upper]*2)
        compare(residuals, "full_spectrum", np.linalg.eigvalsh(h), expected_spectrum)
        for index, operator in enumerate(logical):
            compare(residuals, f"logical_commutator_{index}", h@operator, operator@h)
        alpha = (2*a+8*c+4*a*c*c)/(upper*denominator)
        beta = -s/upper
        eta = -2*b*s/denominator
        gamma = (8*b+6*a*b*c)/(upper*denominator)
        delta = 2*a*b*s/(upper*denominator)
        images = [partial_references(projection)] + [partial_references(projection@operator) for operator in logical]
        expected_images = [np.eye(4)/2, alpha*word("ZI")+beta*word("XX"),
                           eta*word("XY"), gamma*word("IZ")+delta*word("YY")]
        for index in range(4):
            compare(residuals, f"channel_image_{index}", images[index], expected_images[index])
        choi = (kron(I, images[0])+kron(X, images[1])-kron(Y, images[2])+kron(Z, images[3]))/4
        ppt = choi.reshape(2, 4, 2, 4).transpose(2, 1, 0, 3).reshape(8, 8)
        negative = b*s/denominator
        compare(residuals, "Choi_partial_transpose_spectrum", np.linalg.eigvalsh(ppt),
                sorted([0.25]*4+[negative]*2+[-negative]*2))
        require(np.linalg.eigvalsh(choi)[0] >= -TOLERANCE, "NPT channel Choi positive")
        compare(residuals, "Choi_trace", np.trace(choi), 1)
        compare(residuals, "coefficient_square_identity", alpha*alpha+beta*beta+gamma*gamma+delta*delta,
                0.25+eta*eta)
        compare(residuals, "coefficient_cross_identity", 2*(alpha*delta+beta*gamma), eta)
        compare(residuals, "simplified_alpha", alpha, (1+2*a*c)/(2*a*upper))
        compare(residuals, "simplified_gamma", gamma, b*(4+3*a*c)/(upper*(3+2*a*c)))
        # Algebraic derivatives, compared with the quotient-rule expressions.
        alpha_numerator = 2*a+8*c+4*a*c*c
        denominator_derivative = 2*a*denominator/upper + 4*a*upper
        alpha_derivative = ((8+8*a*c)*upper*denominator-alpha_numerator*denominator_derivative)/(upper*denominator)**2
        gamma_derivative = (6*a*b*upper*denominator-(8*b+6*a*b*c)*denominator_derivative)/(upper*denominator)**2
        compare(residuals, "alpha_derivative_identity", alpha_derivative, 2*(3+a*c)/upper**3)
        compare(residuals, "gamma_derivative_identity", gamma_derivative,
                -a*b*(17+30*a*c+12*a*a*c*c)/(upper**3*(3+2*a*c)**2))
        records.append({"c_exact": str(rational_c), "U_equals_m": float(upper),
                        "third_eigenvalue": float(tail), "minimum_Choi_PPT_eigenvalue": float(-negative),
                        "diamond_distance_upper_bound": float(s+1-c),
                        "relative_identity_residuals": residuals})
    return records


def balanced_head():
    memory = [np.sqrt(2/3)*word("ZI")+word("XI")/np.sqrt(3),
              np.sqrt(2/3)*word("ZI")-word("XI")/np.sqrt(3),
              np.sqrt(2/3)*word("IZ")+word("ZX")/np.sqrt(3),
              np.sqrt(2/3)*word("IZ")-word("ZX")/np.sqrt(3)]
    reference = [word("XI"), word("ZI"), word("IX"), word("IZ")]
    h = sum(kron(a, decoder) for a, decoder in zip(reference, memory))
    values, vectors = np.linalg.eigh(h)
    require(abs(values[-1]-2*np.sqrt(3)) < TOLERANCE, "canonical top energy")
    return vectors[:, -2:]


def rank_two_head_checks():
    base = balanced_head()
    cases = [("balanced", None, 0.0), ("Pauli_XIYI", "XIYI", 0.01),
             ("Pauli_ZYXZ", "ZYXZ", 0.02), ("Pauli_IXYY", "IXYY", 0.03)]
    reference = [word("XI"), word("ZI"), word("IX"), word("IZ")]
    records = []
    for name, generator, angle in cases:
        v = base if generator is None else (np.cos(angle)*np.eye(16)+1j*np.sin(angle)*word(generator))@base
        residuals = {}
        compare(residuals, "head_isometry", v.conj().T@v, I)
        purification = v.reshape(4, 4, 2)/np.sqrt(2)
        rho = np.einsum("rqe,sqf->resf", purification, purification.conj()).reshape(8, 8)
        compare(residuals, "flat_head_marginal", partial_references(rho, 2), I/2)
        values, vectors = np.linalg.eigh(rho)
        positive = values > 1e-9
        require(np.count_nonzero(positive) == 4, "rank-four complementary state")
        projection = vectors[:, positive]@vectors[:, positive].conj().T
        root = (vectors[:, positive]*np.sqrt(values[positive]))@vectors[:, positive].conj().T
        quarter = (vectors[:, positive]*values[positive]**0.25)@vectors[:, positive].conj().T
        compare(residuals, "square_root", root@root, rho)
        profile, affinities, stabilities = [], [], []
        for index, pauli in enumerate(reference):
            lifted = kron(pauli, I)
            compressed = root@lifted@root
            eigenvalues, eigenvectors = np.linalg.eigh(vectors[:, positive].conj().T@compressed@vectors[:, positive])
            sign = vectors[:, positive]@(eigenvectors*np.where(eigenvalues >= 0, 1, -1))@eigenvectors.conj().T@vectors[:, positive].conj().T
            f = norm1(compressed)
            affinity = float(np.trace(root@lifted@root@lifted).real)
            deficit = max(0.0, affinity-f*f)
            y, z = quarter@lifted@quarter, quarter@sign@quarter
            compare(residuals, f"signed_Cauchy_inner_product_{index}", np.trace(y@z), f)
            signed_error = float(np.linalg.norm(y-f*z)**2)
            compressed_error = float(np.linalg.norm(projection@lifted@projection-f*sign))
            require(signed_error <= deficit+TOLERANCE, "signed affinity stability")
            require(compressed_error**2 * values[positive][0] <= deficit+TOLERANCE,
                    "inverted signed affinity stability")
            require(affinity-f*f >= -TOLERANCE, "fidelity-affinity comparison")
            profile.append(f)
            affinities.append(affinity)
            stabilities.append({"affinity_deficit": deficit, "signed_congruence_error_squared": signed_error,
                                "compressed_sign_error": compressed_error})
        raw_eta = float(3-np.dot(profile, profile))
        require(raw_eta >= -TOLERANCE, "sharp squared support budget")
        eta = max(0.0, raw_eta)
        require(eta <= 0.09, "selected perturbation lies in flattening range")
        flat_error = float(np.linalg.norm(root-projection/2))
        require(flat_error**2 <= F(9, 16)*eta+TOLERANCE, "quantitative flattening bound")
        x_marginal = partial_references(root, 2)
        chirality = word("YYI")
        reflected_root = chirality@root@chirality
        even_remainder = (root+reflected_root)/2-kron(np.eye(4), x_marginal)/4
        overlap = np.trace(root@reflected_root)
        marginal_deficit = 1-np.trace(x_marginal@x_marginal)/2
        compare(residuals, "squared_chirality_identity",
                x_marginal@x_marginal+4*partial_references(even_remainder@even_remainder, 2),
                I+partial_references(root@reflected_root+reflected_root@root, 2))
        compare(residuals, "chirality_overlap_deficit", overlap,
                2*np.linalg.norm(even_remainder)**2-marginal_deficit)
        pauli_gap = 2+float(np.trace(x_marginal@x_marginal).real)/2-sum(affinities)
        require(pauli_gap >= -TOLERANCE, "four-Pauli gap")
        allowed = kron(np.eye(4), x_marginal)/4
        for pauli in reference:
            coefficient = partial_references(kron(pauli, I)@root, 2)/4
            allowed += kron(pauli, coefficient)
        discarded = float(np.linalg.norm(root-allowed))
        require(discarded**2 <= eta/2+TOLERANCE, "Pauli projection residual")
        records.append({"case": name, "rotation_angle": angle, "complement_rank": 4,
                        "correlation_profile": profile, "squared_support_deficit": eta,
                        "flatness_error": flat_error, "Pauli_projection_error": discarded,
                        "affinity_stability": stabilities, "relative_identity_residuals": residuals})
    require(any(record["flatness_error"] > 1e-5 for record in records), "nonflat perturbation exercised")
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    source = Path(__file__).resolve()
    repository = source.parents[1]
    notes = [repository/"docs/audits/QUANTITATIVE_TWO_MODE_STABILITY.md",
             repository/"docs/audits/ROBUST_HEAD_CHANNEL_CONVERSE.md"]
    if arguments.output:
        destination = arguments.output.resolve()
        if destination in [source, *(note.resolve() for note in notes)] or destination.suffix != ".json":
            raise ValueError("Output must be a JSON file and must not overwrite the verifier or proof notes")
    report = {"status": "exact scalar and fixed matrix checks passed", "research_base": RESEARCH_BASE,
              "python": platform.python_version(), "numpy": np.__version__, "tolerance": TOLERANCE,
              "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
              "proof_note_sha256": {str(note.relative_to(repository)): hashlib.sha256(note.read_bytes()).hexdigest()
                                     for note in notes},
              "exact_constants": exact_constant_checks(), "NPT_family_points": npt_family_checks(),
              "rank_two_head_constructions": rank_two_head_checks(), "maximum_matrix_dimension": 16,
              "scope": "Exact rational constant checks and seven fixed matrix constructions; universal proofs are analytical, with no scan, numerical optimality, or unrestricted converse claim."}
    residuals = [value for collection in [report["NPT_family_points"], report["rank_two_head_constructions"]]
                 for record in collection for value in record["relative_identity_residuals"].values()]
    report["maximum_relative_identity_residual"] = max(residuals)
    report["matrix_identity_count"] = len(residuals)
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
