#!/usr/bin/env python3
"""Fixed construction diagnostics for quarter-rank affinity geometry.

Exact rational comparisons and eight small matrices supplement the analytical
proof. No optimization, random sampling, or parameter grid is performed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import platform

import numpy as np


BASE = "ecdfc7d6ad3ee16e66ba6f6de8802974bb558ee2"
NOTE = "QUARTER_RANK_GEOMETRY.md"
TOL = 3e-9
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = dict(I=I, X=X, Y=Y, Z=Z)
ROOT2 = float(np.sqrt(2))


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


def nonnegative(margins, label, value):
    value = float(value)
    margins[label] = value
    require(value >= -TOL, label)


def normalize(matrix):
    return matrix/np.linalg.norm(matrix)


def exact_checks():
    checks = {}

    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness

    check("first_local_axis", F(3, 5)**2+F(4, 5)**2 == 1, "3^2+4^2=5^2")
    check("second_local_axis", F(5, 13)**2+F(12, 13)**2 == 1, "5^2+12^2=13^2")
    check("complex_rotation", F(3, 5)**2+F(4, 5)**2 == 1, "(3I+4iG)/5 unitary for G^2=I")
    check("quarter_rank_factor", F(16, 4) == 4, "d/r=4 at d=16,r=4")
    check("affinity_budget_endpoint", F(9, 2)+F(3, 2) == 6, "9/2+3u^2/2=6 at u=1")
    check("flat_branch_A_sign", 2*2**2 < 3**2, "2sqrt2-3<0 from 8<9")
    check("flat_branch_B_crossing", 3-F(4, 5) == 4*F(4, 5)-1 == F(11, 5),
          "max(3-y,4y-1)>=11/5, meeting at y=4/5")
    check("flat_branch_B_Cauchy", 8*(8-F(11, 5)) == F(232, 5), "8(8-11/5)=232/5")
    check("flat_branch_B_radical_gap", F(7, 5)**2 < 2, "sqrt2>7/5 gives 24+16sqrt2>232/5")
    check("rank_three_affinity_budget", F(9, 2)+3*F(3, 8) == F(45, 8), "rank3 flat budget=45/8")
    check("rank_three_target_gap", F(21, 16)**2 < 2, "sqrt45<4+2sqrt2 since 21/16<sqrt2")
    check("retention_singleton_data", 2*F(1, 2)**2 == F(1, 2), "a=b=1/2,c=d=0 gives T=1/2")
    check("trace_gate_polynomial_identity", 36-12 == 4**2+2**2*2 and 12*F(4, 3) == 2*4*2,
          "36+12(4sqrt2-3)/3=(4+2sqrt2)^2")
    return checks


def constructions():
    bisector = (X+Z)/ROOT2
    p = (I+bisector)/2
    equality = kron(p, p, np.eye(4))/2
    unbalanced = kron((I+(3*X+4*Z)/5)/2, (I+(5*X+12*Z)/13)/2, np.eye(4))/2
    rotation = np.cos(np.pi/8)*I-1j*np.sin(np.pi/8)*Y
    local_change = kron(rotation, rotation, rotation, rotation)
    angle_change = np.cos(np.pi/8)*np.eye(16)+1j*np.sin(np.pi/8)*word("XIXI")
    flat_branch_a = angle_change @ equality @ angle_change.conj().T
    majority = np.zeros(16)
    majority[[0, 1, 2, 4]] = 1
    flat_branch_b = local_change @ np.diag(majority/2) @ local_change.conj().T
    rank_three = np.zeros(16)
    rank_three[[0, 1, 2]] = 1/np.sqrt(3)
    rank_three = local_change @ np.diag(rank_three) @ local_change.conj().T
    nonflat = normalize(kron(p, p, np.diag([2, 1, 1, 1])))
    nonflat_rank_three = normalize(kron(p, p, np.diag([2, 1, 1, 0])))
    star = np.zeros(16)
    star[0] = 1/np.sqrt(2)
    star[[2, 4, 8]] = 1/np.sqrt(6)
    star = local_change @ np.diag(star) @ local_change.conj().T
    complex_change = (3*np.eye(16)+4j*word("ZXXI"))/5
    complex_nonflat = complex_change @ nonflat @ complex_change.conj().T
    return [("flat_bisector_equality", equality, "equality_bisector"),
            ("flat_arbitrary_axis_squared_equality", unbalanced, "equality_axes"),
            ("flat_complex_branch_A", flat_branch_a, "flat_A"),
            ("flat_majority_branch_B", flat_branch_b, "flat_B"),
            ("flat_rank_three", rank_three, "flat_lower_rank"),
            ("nonflat_cube_rank_three", nonflat_rank_three, "nonflat_lower_rank"),
            ("nonflat_Hamming_star", star, "nonflat"),
            ("nonflat_complex_entangled", complex_nonflat, "nonflat_complex")]


def local_blocks(matrix, site, sx, sz):
    angle = np.arctan2(sx, sz) if np.hypot(sx, sz) > TOL else 0.
    rotation = np.cos(angle/2)*I-1j*np.sin(angle/2)*Y
    factors = [I]*4
    factors[site] = rotation
    change = kron(*factors)
    rotated = change.conj().T @ matrix @ change
    remaining = [index for index in range(4) if index != site]
    order = [site]+remaining+[site+4]+[index+4 for index in remaining]
    blocks = rotated.reshape([2]*8).transpose(order).reshape(2, 8, 2, 8)
    return blocks[0, :, 0, :], blocks[0, :, 1, :], blocks[1, :, 1, :]


def check_construction(name, matrix, kind):
    errors, margins = {}, {}
    compare(errors, "Hermitian_seed_root", matrix, matrix.conj().T)
    values = np.linalg.eigvalsh(matrix)
    nonnegative(margins, "positive_seed_root", values[0])
    rank = int(np.count_nonzero(values > TOL))
    require(1 <= rank <= 4, "admissible quarter rank")
    compare(errors, "HS_normalization", np.trace(matrix @ matrix), 1)
    trace = float(np.trace(matrix).real)
    raw_u = trace/2
    nonnegative(margins, "rank_trace_cap", 1-raw_u*raw_u)
    u = min(1., raw_u)
    v = float(np.sqrt(max(0, 1-u*u)))
    kappa = float(values[-1])
    coefficients = {"".join(letters): float((np.trace(matrix @ word(letters))/4).real)
                    for letters in itertools.product("IXYZ", repeat=4)}
    compare(errors, "Pauli_Parseval", sum(coefficient**2 for coefficient in coefficients.values()), 1)
    compare(errors, "identity_coefficient", coefficients["IIII"], u/2)
    singleton = np.zeros((16, 16), dtype=complex)
    b, affinities, scores = [], [], []
    for site in range(4):
        local_coefficients = []
        for axis in "XZ":
            label = "I"*site+axis+"I"*(3-site)
            query = word(label)
            coefficient = coefficients[label]
            local_coefficients.append(coefficient)
            singleton += coefficient*query/4
            affinity = float(np.trace(matrix @ query @ matrix @ query).real)
            score = float(np.sum(np.linalg.svd(matrix @ query @ matrix, compute_uv=False)))
            nonnegative(margins, label+"_affinity_positive", affinity)
            nonnegative(margins, label+"_affinity_upper", 1-affinity)
            nonnegative(margins, label+"_squared_fidelity_affinity", affinity-score*score)
            anticommute_mass = sum(coefficient**2 for key, coefficient in coefficients.items()
                                   if key[site] not in ["I", axis])
            compare(errors, label+"_Pauli_deficit", 1-affinity, 2*anticommute_mass)
            affinities.append(affinity)
            scores.append(score)
        local_length = float(np.linalg.norm(local_coefficients))
        b.append(local_length)
        a, c, d = local_blocks(matrix, site, *local_coefficients)
        local_deficit = 2-affinities[-1]-affinities[-2]
        c_norm = float(np.linalg.norm(c)**2)
        c_square = float(np.trace(c @ c).real)
        difference_norm = float(np.linalg.norm(a-d)**2)
        compare(errors, f"site{site}_oriented_trace", np.trace(a-d), 4*local_length)
        compare(errors, f"site{site}_block_deficit", local_deficit, difference_norm+6*c_norm-2*c_square)
        compare(errors, f"site{site}_block_second_formula", local_deficit,
                1-2*np.trace(a @ d).real+4*c_norm-2*c_square)
        nonnegative(margins, f"site{site}_off_diagonal_remainder", 2*c_norm-2*c_square)
        nonnegative(margins, f"site{site}_rank_sensitive_deficit", local_deficit-(16/rank)*local_length**2)
        nonnegative(margins, f"site{site}_operator_norm_block_deficit", local_deficit-(1-2*kappa*(u-2*local_length)))
        nonnegative(margins, f"site{site}_block_positive_A", np.linalg.eigvalsh(a)[0])
        nonnegative(margins, f"site{site}_block_positive_D", np.linalg.eigvalsh(d)[0])
        nonnegative(margins, f"site{site}_A_operator_norm", kappa-np.linalg.eigvalsh(a)[-1])
        require(np.count_nonzero(np.linalg.eigvalsh(a) > TOL) <= rank, "principal block rank bound")
        require(np.count_nonzero(np.linalg.eigvalsh(a-d) > TOL) <= rank, "positive inertia bound")
        if kind.startswith("equality"):
            compare(errors, f"site{site}_local_rank_bound_equality", local_deficit, (16/rank)*local_length**2)
            if local_length > TOL:
                compare(errors, f"site{site}_positive_bias_D_zero", d, np.zeros((8, 8)))
                compare(errors, f"site{site}_positive_bias_C_zero", c, np.zeros((8, 8)))
                compare(errors, f"site{site}_positive_bias_flat_A", a @ a, a/np.sqrt(rank))
            else:
                compare(errors, f"site{site}_zero_bias_equal_blocks", a, d)
                compare(errors, f"site{site}_zero_bias_C_zero", c, np.zeros((8, 8)))
    b = np.array(b)
    ordering = np.argsort(-b)
    a, bb, cc, dd = b[ordering]
    local_mass = float(b @ b)
    y = 2*local_mass
    r_tail = max(bb, (bb+cc+dd)/2)
    compare(errors, "singleton_self_pairing", np.trace(matrix @ singleton), local_mass)
    compare(errors, "singleton_HS_norm", np.trace(singleton @ singleton), local_mass)
    top = np.linalg.eigvalsh(singleton)[-4:][::-1]
    formula = np.array([a+bb+cc+dd, a+bb+cc-dd, a+bb-cc+dd, a+abs(bb-cc-dd)])/4
    compare(errors, "exact_top_four_singleton_eigenvalues", top, formula)
    mean = (a+r_tail)/4
    variance = (local_mass-a*a-r_tail*r_tail)/4
    compare(errors, "top_quarter_mean", np.mean(top), mean)
    compare(errors, "top_quarter_variance", np.sum((top-mean)**2), variance)
    nonnegative(margins, "top_quarter_variance_positive", variance)
    lambdas = values[-4:][::-1]
    compare(errors, "padded_seed_centered_variance", np.sum((lambdas-trace/4)**2), 1-trace*trace/4)
    nonnegative(margins, "rank_four_rearrangement", np.dot(lambdas, top)-local_mass)
    nonnegative(margins, "centered_rank_constraint", u*(a+r_tail)+v*np.sqrt(max(0, 4*variance))-2*local_mass)
    nonnegative(margins, "singleton_mass_cap", (1+u*u)/4-local_mass)
    total_affinity = float(sum(affinities))
    squared_original = float(sum(score*score for score in scores))
    nonnegative(margins, "Pauli_affinity_budget", 4+u*u+2*local_mass-total_affinity)
    nonnegative(margins, "trace_dependent_affinity_budget", 4.5+1.5*u*u-total_affinity)
    nonnegative(margins, "sharp_affinity_bound", 6-total_affinity)
    nonnegative(margins, "sharp_squared_original_bound", 6-squared_original)
    nonnegative(margins, "squared_original_below_affinity", total_affinity-squared_original)
    affinity_score = float(sum(np.sqrt(np.maximum(affinities, 0))))
    original_score = float(sum(scores))
    target = 4+2*ROOT2
    trace_gate = (4*ROOT2-3)/3
    nonnegative(margins, "trace_dependent_root_bound", np.sqrt(36+12*u*u)-affinity_score)
    if rank <= 3:
        nonnegative(margins, "arbitrary_lower_rank_affinity_bound", np.sqrt(45)-affinity_score)
        nonnegative(margins, "arbitrary_lower_rank_original_bound", np.sqrt(45)-original_score)
    if u*u <= trace_gate:
        nonnegative(margins, "trace_gate_affinity_converse", target-affinity_score)
        nonnegative(margins, "trace_gate_original_converse", target-original_score)
    flat = kind.startswith("flat") or kind.startswith("equality")
    branch = "nonflat_not_claimed"
    if flat:
        compare(errors, "flat_projector_root", matrix @ matrix, matrix/np.sqrt(rank))
        nonnegative(margins, "flat_affinity_converse", target-affinity_score)
        nonnegative(margins, "flat_original_converse", target-original_score)
        if rank < 4:
            branch = "flat_rank_at_most_three"
            nonnegative(margins, "lower_flat_rank_affinity_budget", 4.5+3*rank/8-total_affinity)
            nonnegative(margins, "lower_flat_rank_root_budget", np.sqrt(36+3*rank)-affinity_score)
        else:
            compare(errors, "flat_rank_four_u", u, 1)
            compare(errors, "flat_rank_four_operator_norm", kappa, .5)
            deficits = 2-np.array(affinities).reshape(4, 2).sum(axis=1)
            for site in range(4):
                nonnegative(margins, f"site{site}_flat_linear_deficit", deficits[site]-2*b[site])
                nonnegative(margins, f"site{site}_flat_singleton_upper", .5-b[site])
            total_deficit = float(sum(deficits))
            nonnegative(margins, "flat_total_Pauli_deficit", total_deficit-(3-y))
            if bb >= cc+dd-TOL:
                branch = "flat_A"
                pair_mass = a+bb
                chosen = float(sum(deficits[ordering[:2]]))
                nonnegative(margins, "flat_A_rank_constraint", pair_mass-y)
                nonnegative(margins, "flat_A_pair_mass_upper", 1-pair_mass)
                nonnegative(margins, "flat_A_chosen_deficit", chosen-2*pair_mass)
                group_bound = np.sqrt(max(0, 4*(4-chosen)))+np.sqrt(max(0, 4*(4-total_deficit+chosen)))
                tangent = target+((ROOT2-1)*(2-chosen)-(total_deficit-2))/2
                nonnegative(margins, "flat_A_group_Cauchy", group_bound-affinity_score)
                nonnegative(margins, "flat_A_tangent", tangent-group_bound)
                nonnegative(margins, "flat_A_tangent_target", target-tangent)
            else:
                branch = "flat_B"
                mass_sum = float(sum(b))
                nonnegative(margins, "flat_B_rank_constraint", (a+mass_sum)/2-y)
                nonnegative(margins, "flat_B_local_deficit_sum", total_deficit-2*mass_sum)
                nonnegative(margins, "flat_B_increasing_deficit", total_deficit-(4*y-1))
                nonnegative(margins, "flat_B_deficit_floor", total_deficit-11/5)
                nonnegative(margins, "flat_B_strict_affinity_bound", np.sqrt(232/5)-affinity_score)
    if kind == "flat_A":
        require(branch == "flat_A", "fixed construction exercises flat branch A")
    if kind == "flat_B":
        require(branch == "flat_B", "fixed construction exercises flat branch B")
    if kind.startswith("equality"):
        compare(errors, "sharp_affinity_sum_equality", total_affinity, 6)
        compare(errors, "sharp_original_squared_sum_equality", squared_original, 6)
        compare(errors, "termwise_original_squared_equality", np.array(scores)**2, affinities)
        compare(errors, "equality_singleton_lengths", b[ordering], [.5, .5, 0, 0])
    if kind == "equality_bisector":
        compare(errors, "flat_affinity_root_equality", affinity_score, target)
        compare(errors, "flat_original_root_equality", original_score, target)
    if "complex" in name:
        require(np.linalg.norm(matrix.imag) > .01, "genuinely complex construction")
    return {"name": name, "rank": rank, "flat_proof_branch": branch, "u": u, "operator_norm": kappa,
            "singleton_mass": local_mass, "singleton_lengths": b.tolist(),
            "affinity_sum": total_affinity, "original_squared_score_sum": squared_original,
            "affinity_root_score": affinity_score, "original_root_score": original_score,
            "relative_identity_residuals": errors, "inequality_margins": margins}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    source = Path(__file__).resolve()
    repository = source.parents[1]
    note = repository/"docs/audits"/NOTE
    if arguments.output:
        destination = arguments.output.resolve()
        if destination in [source, note.resolve()] or destination.suffix != ".json":
            raise ValueError("Output must be JSON and must not overwrite source or proof note")
    records = [check_construction(*case) for case in constructions()]
    report = {"status": "exact constants and fixed constructions passed", "research_base": BASE,
              "python": platform.python_version(), "numpy": np.__version__, "tolerance": TOL,
              "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
              "proof_note_sha256": {str(note.relative_to(repository)): hashlib.sha256(note.read_bytes()).hexdigest()},
              "exact_constants": exact_checks(), "constructions": records, "maximum_matrix_dimension": 16,
              "scope": "Eight deterministic positive seed roots on four qubits. Checks cover sharp affinity and squared-original-score budgets, equality on arbitrary X/Z axes, top-quarter geometry, local rank and operator-norm deficits, both flat rank-four branches, flat and nonflat rank-three seeds, and the trace gate. Nonflat rank-four root scores are reported as diagnostics; their unrestricted retention bound remains unproved here. Universal statements and equality classifications are analytical. Floating-point identities and inequalities are not interval certificates. No random sampling, grid, optimizer, or novelty claim."}
    residuals = [value for row in records for value in row["relative_identity_residuals"].values()]
    margins = [value for row in records for value in row["inequality_margins"].values()]
    report["exact_scalar_count"] = len(report["exact_constants"])
    report["fixed_construction_count"] = len(records)
    report["matrix_identity_count"] = len(residuals)
    report["inequality_count"] = len(margins)
    report["maximum_relative_identity_residual"] = max(residuals)
    report["minimum_inequality_margin"] = min(margins)
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
