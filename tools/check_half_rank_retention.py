#!/usr/bin/env python3
"""Exact constants and fixed constructions for the half-rank affinity proof.

This is a bounded diagnostic supplement to the analytical proof. It performs
no optimization, random sampling, or parameter grid.
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


BASE = "3aad8227ed448eadfaa5ebc4d33bfc9845dd4f8c"
NOTE = "HALF_RANK_RETENTION_CONVERSE.md"
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


def exact_checks():
    checks = {}

    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness

    check("sqrt2_lower", F(707, 500)**2 < 2, "707/500<sqrt2")
    check("sqrt2_upper", 2 < F(3, 2)**2, "sqrt2<3/2")
    check("sqrt7_upper", 7 < F(1323, 500)**2, "sqrt7<1323/500")
    check("nondominant_linear_margin", 2*F(707, 500)-F(3, 2)-F(1323, 1000) == F(1, 200),
          "2sqrt2-3/2-sqrt7/2>1/200")
    check("nondominant_original_witness", 24**2*2 < 37**2, "24sqrt2<37 from 1152<1369")
    check("unified_nondominant_gap", 63 < 64, "4sqrt2>3+sqrt7 from 6sqrt7<16")
    check("unified_nondominant_alternative_gap", 289 > 288,
          "34>24sqrt2 from 289>288")
    check("four_sign_middle_coefficient_norm", (F(3, 4)**2+3*F(1, 4)**2) == F(3, 4),
          "||(3,1,1,1)/4||_2^2=3/4")
    check("four_sign_last_coefficient_norm", 3*F(1, 2)**2 == F(3, 4),
          "||(1,1,1,0)/2||_2^2=3/4")
    check("nondominant_matrix_trace", F(11, 4)+F(1, 4) == 3, "trace=3")
    check("nondominant_matrix_determinant", F(11, 16)-F(3, 16) == F(1, 2),
          "det=1/2; eigenvalues (3+-sqrt7)/2")
    check("dominant_quadratic_determinant", 10**2 > 7**2*2, "10-7sqrt2>0 from 100>98")
    check("dominant_quadratic_second_diagonal", 3**2 > 2**2*2,
          "1-2(sqrt2-1)=3-2sqrt2>0")
    check("low_trace_strict_margin", F(3, 2)-2*(2-F(707, 500)) == F(41, 125),
          "3/2-2(2-sqrt2)>41/125>0")
    for n in [2, 3, 4]:
        rank = 2**(n-1)
        check(f"rank_half_normalization_n{n}", 2*rank == 2**n,
              f"dimension={2**n}, half-rank={rank}")
        check(f"nondominant_squared_margin_n{n}", 2*n*F(1, 200) > 0,
              f"target square minus relaxed square > {F(2*n, 200)}+(2-sqrt2)^2")
    return checks


def normalize(matrix):
    return matrix/np.linalg.norm(matrix)


def equality_seed(n, direction=None):
    if direction is None:
        direction = (X+Z)/ROOT2
    return kron((I+direction)/2, np.eye(2**(n-1)))/np.sqrt(2**(n-1))


def nonflat_product(n):
    weights = np.ones(2**(n-1))
    weights[0] = 2
    return normalize(kron((I+(X+Z)/ROOT2)/2, np.diag(weights)))


def majority_seed(n):
    # Four positive weights on the three-bit majority subspace, then an
    # unused maximally mixed factor for n=4. Every spectrum is fixed.
    weights = np.zeros(8)
    weights[0] = 2
    weights[[1, 2, 4]] = 1
    rotation = np.cos(np.pi/8)*I-1j*np.sin(np.pi/8)*Y
    change = kron(rotation, rotation, rotation)
    result = change @ np.diag(weights) @ change.conj().T
    if n == 4:
        result = kron(result, I)
    return normalize(result)


def constructions():
    cases = []
    for n in [2, 3, 4]:
        cases.append((f"n{n}_bisector_equality", n, equality_seed(n), "equality"))
        cases.append((f"n{n}_nonflat_dominant", n, nonflat_product(n), "nonflat"))
    for n in [3, 4]:
        cases.append((f"n{n}_majority_nondominant", n, majority_seed(n), "nondominant"))
    cases.append(("n2_rank_one_complex", 2,
                  kron((I+Y)/2, (I+(X+Z)/ROOT2)/2), "rank_deficient"))
    cases.append(("n3_rank_three", 3, normalize(np.diag([3, 2, 1, 0, 0, 0, 0, 0])), "rank_deficient"))
    cases.append(("n3_zero_singleton_mass", 3, equality_seed(3, Y), "zero_singleton"))
    seed = nonflat_product(4)
    unitary = (3*np.eye(16)+4j*word("ZXIX"))/5
    cases.append(("n4_complex_entangled", 4, unitary @ seed @ unitary.conj().T, "complex"))
    # A fixed tie resolution among the zero-energy majority configurations
    # gives eight positive eigenvalues and four active singleton sites.
    labels = list(itertools.product([1, -1], repeat=4))
    ordering = sorted(range(16), key=lambda index: (-sum(labels[index]), index))
    weights = np.zeros(16)
    for index in ordering[:8]:
        weights[index] = 1+sum(labels[index])
    cases.append(("n4_four_active_singletons", 4, normalize(np.diag(weights)), "four_active"))
    return cases


def check_construction(name, n, matrix, kind):
    errors, margins = {}, {}
    dimension, half_rank = 2**n, 2**(n-1)
    compare(errors, "Hermitian_seed_root", matrix, matrix.conj().T)
    eigenvalues = np.linalg.eigvalsh(matrix)
    nonnegative(margins, "seed_root_positive", eigenvalues[0])
    rank = int(np.count_nonzero(eigenvalues > TOL))
    require(1 <= rank <= half_rank, "admissible rank")
    compare(errors, "Hilbert_Schmidt_normalization", np.trace(matrix @ matrix), 1)
    trace = float(np.trace(matrix).real)
    raw_u = trace/np.sqrt(half_rank)
    nonnegative(margins, "rank_trace_cap", 1-raw_u*raw_u)
    u = min(1., raw_u)
    v = float(np.sqrt(max(0, 1-u*u)))
    coefficients = {}
    for letters in itertools.product("IXYZ", repeat=n):
        label = "".join(letters)
        coefficient = np.trace(matrix @ word(label))/np.sqrt(dimension)
        require(abs(coefficient.imag) < TOL, "Hermitian Pauli coefficients real")
        coefficients[label] = float(coefficient.real)
    compare(errors, "Pauli_Parseval", sum(value*value for value in coefficients.values()), 1)
    compare(errors, "identity_coefficient", coefficients["I"*n], trace/np.sqrt(dimension))
    singleton = np.zeros_like(matrix, dtype=complex)
    b = []
    queries, affinities, trace_scores = [], [], []
    for site in range(n):
        mass = 0.
        for axis in "XZ":
            letters = ["I"]*n
            letters[site] = axis
            label = "".join(letters)
            coefficient = coefficients[label]
            mass += coefficient*coefficient
            query = word(label)
            singleton += coefficient*query/np.sqrt(dimension)
            affinity = float(np.trace(matrix @ query @ matrix @ query).real)
            score = float(np.sum(np.linalg.svd(matrix @ query @ matrix, compute_uv=False)))
            nonnegative(margins, label+"_affinity_positive", affinity)
            nonnegative(margins, label+"_affinity_at_most_one", 1-affinity)
            nonnegative(margins, label+"_squared_fidelity_affinity", affinity-score*score)
            anticommute_mass = sum(value*value for key, value in coefficients.items()
                                   if key[site] not in ["I", axis])
            compare(errors, label+"_anticommuting_deficit", 1-affinity, 2*anticommute_mass)
            queries.append(label)
            affinities.append(affinity)
            trace_scores.append(score)
        b.append(np.sqrt(mass))
    b = np.array(b)
    singleton_mass = float(b @ b)
    y = min(1., 2*singleton_mass)
    compare(errors, "singleton_norm", np.trace(singleton @ singleton), singleton_mass)
    compare(errors, "singleton_self_pairing", np.trace(matrix @ singleton), singleton_mass)
    spectrum = np.linalg.eigvalsh(singleton)
    compare(errors, "singleton_spectral_symmetry", spectrum, -spectrum[::-1])
    compare(errors, "positive_singleton_squared_norm", np.sum(np.maximum(spectrum, 0)**2), singleton_mass/2)
    nonnegative(margins, "positive_singleton_Cauchy", np.sqrt(singleton_mass/2)-singleton_mass)
    nonnegative(margins, "singleton_mass_at_most_half", .5-singleton_mass)
    signed_average = float(np.mean([abs(np.dot(signs, b)) for signs in itertools.product([1, -1], repeat=n)]))
    ordered = sorted(b, reverse=True)+[0.]*(4-n)
    a, bb, cc, dd = ordered
    candidates = [a, (3*a+bb+cc+dd)/4, (a+bb+cc)/2]
    maximum = max(candidates)
    compare(errors, "four_sign_absolute_mean", signed_average, maximum)
    top = spectrum[-half_rank:][::-1]
    mu = maximum/np.sqrt(dimension)
    compare(errors, "top_half_mean", np.mean(top), mu)
    compare(errors, "top_half_centered_norm", np.sum((top-mu)**2), (singleton_mass-maximum*maximum)/2)
    lambdas = eigenvalues[-half_rank:][::-1]
    compare(errors, "padded_seed_centered_norm", np.sum((lambdas-trace/half_rank)**2), 1-trace*trace/half_rank)
    nonnegative(margins, "rank_half_von_Neumann", np.dot(lambdas, top)-singleton_mass)
    centered_bound = trace*mu+v*np.sqrt(max(0, (singleton_mass-maximum*maximum)/2))
    nonnegative(margins, "rank_half_centered_Cauchy", centered_bound-np.dot(lambdas, top))
    total_affinity = float(sum(affinities))
    conjugation_sum = sum(value*value*sum(2 if letter == "I" else -2 if letter == "Y" else 0
                                            for letter in key) for key, value in coefficients.items())
    compare(errors, "Pauli_conjugation_sum", total_affinity, conjugation_sum)
    budget = 2*n-4+2*u*u+y
    nonnegative(margins, "Pauli_affinity_budget", budget-total_affinity)
    affinity_score = float(sum(np.sqrt(np.maximum(affinities, 0))))
    original_score = float(sum(trace_scores))
    target = 2*n-2+ROOT2
    nonnegative(margins, "affinity_retention_bound", target-affinity_score)
    nonnegative(margins, "original_retention_bound", target-original_score)
    nonnegative(margins, "original_below_affinity", affinity_score-original_score)
    if singleton_mass < TOL:
        branch = "zero_singleton"
    else:
        c = min(1., maximum/np.sqrt(singleton_mass))
        nonnegative(margins, "rank_half_unit_circle", u*c+v*np.sqrt(max(0, 1-c*c))-np.sqrt(y))
        if u <= np.sqrt(3)/2+TOL:
            branch = "low_trace"
            nonnegative(margins, "low_trace_budget", 2*n-1.5-total_affinity)
        elif max(candidates[1:]) >= candidates[0]-TOL:
            branch = "nondominant"
            nonnegative(margins, "nondominant_direction_cap", np.sqrt(3)/2-c)
            nonnegative(margins, "nondominant_circle_bound", (np.sqrt(3)*u+v)**2/4-y)
            nonnegative(margins, "nondominant_eigenvalue_bound", (3+np.sqrt(7))/2-2*u*u-y)
            nonnegative(margins, "nondominant_strict_target", target-np.sqrt(2*n*(2*n-4+(3+np.sqrt(7))/2)))
        elif u*u+y < 1:
            branch = "dominant_low_mass"
            nonnegative(margins, "dominant_low_mass_budget", 2*n-2-total_affinity)
        else:
            branch = "dominant"
            site = int(np.argmax(b))
            deficits = 1-np.array(affinities)
            chosen = float(sum(deficits[2*site:2*site+2]))
            total = float(sum(deficits))
            e = 4-2*u*u-y
            z = np.sqrt(max(0, 1-y))
            circle_lower = u*np.sqrt(y)-v*z
            w = y*circle_lower*circle_lower
            nonnegative(margins, "dominant_circle_lower_positive", circle_lower)
            nonnegative(margins, "dominant_circle_inversion", c-circle_lower)
            nonnegative(margins, "chosen_query_singleton_deficit", chosen-y*c*c)
            nonnegative(margins, "chosen_query_geometric_deficit", chosen-w)
            nonnegative(margins, "total_query_deficit", total-e)
            group_bound = np.sqrt(max(0, 2*(2-chosen)))+np.sqrt(max(0, (2*n-2)*(2*n-2-total+chosen)))
            tangent = target+((ROOT2-1)*(1-chosen)-(total-1))/2
            nonnegative(margins, "group_Cauchy", group_bound-affinity_score)
            nonnegative(margins, "concave_tangents", tangent-group_bound)
            nonnegative(margins, "sine_upper_bound", v*v+2*v*z+2*z*z-(1-w))
            r = ROOT2-1
            quadratic = (2-r)*v*v-2*r*v*z+(1-2*r)*z*z
            nonnegative(margins, "dominant_positive_quadratic", quadratic)
            nonnegative(margins, "dominant_quadratic_comparison", (e-1)-r*(1-w)-quadratic)
            nonnegative(margins, "tangent_below_target", target-tangent)
    if kind == "equality":
        compare(errors, "affinity_equality", affinity_score, target)
        compare(errors, "original_equality", original_score, target)
    if kind == "nondominant":
        require(branch == "nondominant", "majority construction exercises nondominant branch")
    if kind == "four_active":
        require(np.all(b > TOL), "all four singleton sites active")
    if kind in ["complex", "rank_deficient"] and "complex" in name:
        require(np.linalg.norm(matrix.imag) > .01, "construction genuinely complex")
    return {"name": name, "qubits": n, "matrix_dimension": dimension, "rank": rank,
            "proof_branch": branch, "u": u, "y": y, "singleton_site_lengths": b.tolist(),
            "original_trace_norm_score": original_score, "affinity_score": affinity_score,
            "retention_target": target, "relative_identity_residuals": errors, "inequality_margins": margins}


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
              "scope": "Thirteen fixed positive seed roots on two, three, or four qubits. Checks include bisector equality, nonflat dominant seeds, majority nondominant seeds, rank-deficient and complex seeds, zero singleton mass, and four active singleton sites. The universal theorem and equality classification are analytical; finite floating-point identities and inequalities are diagnostics, not interval certificates or an optimization proof. No random sampling, parameter grid, optimizer, or publication-priority claim."}
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
