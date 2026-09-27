#!/usr/bin/env python3
"""Fixed construction checks for block-budget resolvents and envelope failure.

Scalar supports are evaluated by bisection using the proved convex-quartic
decision and its unique clipped cubic root. There is no angle grid or
matrix optimizer. Finite checks supplement the analytical proof notes.
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


BASE = "556df48950c2de3162171dd1d85c3df9e5937fc2"
TOL = 3e-9
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
ROOT2 = float(np.sqrt(2))
PAULIS = dict(I=I, X=X, Y=Y, Z=Z)
NOTES = ["JORDAN_BLOCK_BUDGET_RESOLVENT.md", "REFLECTION_ENVELOPE_OBSTRUCTION.md"]


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
    value = float(np.linalg.norm(np.asarray(actual)-np.asarray(expected)) /
                  max(1, np.linalg.norm(expected)))
    errors[label] = value
    require(value <= TOL, label)


def polynomial(t, x, y, bound, a):
    total, difference = x+y, x-y
    return (4*bound*a**4+2*difference*a**3-8*bound*a*a-
            difference*(t*t+2)*a+bound*(t*t-2)**2-total*t*(t*t-2))


def clipped_cubic(t, x, y, bound):
    require(bound > 0, "positive scalar threshold")
    difference = x-y
    if difference == 0:
        return polynomial(t, x, y, bound, 1.0), 1.0

    def derivative(a):
        return 16*bound*a**3+6*difference*a*a-16*bound*a-difference*(t*t+2)

    if derivative(ROOT2) <= 0:
        return polynomial(t, x, y, bound, ROOT2), ROOT2
    lower, upper = 1.0, ROOT2
    for _ in range(70):
        center = (lower+upper)/2
        if derivative(center) <= 0:
            lower = center
        else:
            upper = center
    point = (lower+upper)/2
    return polynomial(t, x, y, bound, point), point


def fg(t, a):
    b2 = max(0.0, 2-a*a)
    return (t-a)/((t-a)**2-b2), (t+a)/((t+a)**2-b2)


def psi_support(t, x, y):
    x, y = max(x, y), min(x, y)
    if x+y == 0:
        return 0.0, 1.0
    lower, upper = 0.0, (x+y)/(t-2)
    for _ in range(75):
        center = (lower+upper)/2
        if clipped_cubic(t, x, y, center)[0] >= 0:
            upper = center
        else:
            lower = center
    _, angle = clipped_cubic(t, x, y, upper)
    f, g = fg(t, angle)
    attained = x*f+y*g
    require(abs(attained-upper) <= TOL, "scalar cubic value and attainer agree")
    return float(attained), float(angle)


def weighted_resolvent(t, rho, b, d):
    dimension = len(rho)
    resolvent = np.linalg.inv(t*np.eye(2*dimension)-kron(X, b)-kron(Z, d))
    return np.einsum("qp,rpsq->rs", rho, resolvent.reshape(2, dimension, 2, dimension))


def exact_checks():
    checks = {}

    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness

    c, s = F(399, 401), F(40, 401)
    check("reflection_angle", c*c+s*s == 1, "399^2+40^2=401^2")
    check("sqrt3_bracket", F(1732, 1000)**2 < 3 < F(1733, 1000)**2,
          "1732/1000<sqrt3<1733/1000")
    check("top_radical_bracket", 380**2 < 144841 < 381**2,
          "380<sqrt144841<381")
    check("second_radical_bracket", 420**2 < 176761 < F(841, 2)**2,
          "420<sqrt176761<841/2")
    check("second_lower", F(2360000, 694933)-F(679, 200) == F(140493, 138986600) > 0,
          "140493/138986600")
    check("second_upper", F(2361000, 694532)-F(17, 5) == -F(511, 868165) < 0,
          "-511/868165")
    check("top_gap", F(79000, 694933)-F(11, 100) == F(255737, 69493300) > 0,
          "255737/69493300")
    check("top_upper", F(2442000, 694532) < F(18, 5), "2442000/694532<18/5")
    check("small_pole_gap", F(7, 5)**2 < 2 < F(283, 200)**2
          and 2+F(283, 200)-F(679, 200) == F(1, 50),
          "7/5<sqrt2<283/200;2+283/200-679/200=1/50")
    check("excluded_sector_bounds", F(4, 3) < F(6, 5)**2 and 1-c+s < F(1, 8)
          and 1+(c+s)**2 < F(3, 2)**2 and F(4, 5)**2 < F(2, 3)
          and F(6, 5)*F(21, 10)-F(4, 5) == F(43, 25) < 2,
          "all excluded sector eigenvalues<2")
    check("noncommuting_blocks", F(3, 2)*s < c and 2 < F(3, 2)**2,
          "sqrt2*S<C from60<399")
    check("top_marginal_bias", 3*359**2 > 401**2, "q>1/2 from3*359^2>401^2")
    check("envelope_failure_margin", F(11, 100)*F(3, 2)/(8*F(1, 50)) == F(33, 32) > 1,
          "33/32")
    check("actual_norm_perturbation", 2*(1-c+s) == F(84, 401) < F(1, 4)
          and F(5, 4)**2 < 2, "84/401<1/4;21/4<4+sqrt2")
    check("two_mode_radical_comparison", (60*F(7, 5)-46)/25 == F(38, 25) > 0,
          "(8+8sqrt2)-(14/5+sqrt2)^2=(60sqrt2-46)/25>38/25")
    check("two_mode_product", (F(18, 5)-2)*F(5, 8) == 1,
          "(18/5-2)(5/8)=1 with both actual factors strict")
    for index, (t, x, y, bound, a) in enumerate([
            (F(21, 10), F(3, 5), F(1, 10), F(4), F(6, 5)),
            (F(13, 5), F(1, 4), F(1, 4), F(1), F(1)),
            (F(9, 2), F(3, 5), F(0), F(1, 3), F(7, 5))]):
        b2 = 2-a*a
        left, right = (t-a)**2-b2, (t+a)**2-b2
        f, g = (t-a)/left, (t+a)/right
        check(f"quartic_identity_{index}", polynomial(t, x, y, bound, a) == left*right*(bound-x*f-y*g),
              "P_K=positive_denominators*(K-x f_a-y g_a)")
    return {"count": len(checks), "uses_floating_point": False, "witnesses": checks}


def partial_matchings(indices):
    """Enumerate finite partial matchings, including unmatched vertices."""
    if not indices:
        yield ()
        return
    first, rest = indices[0], indices[1:]
    yield from partial_matchings(rest)
    for offset, second in enumerate(rest):
        remaining = rest[:offset]+rest[offset+1:]
        for tail in partial_matchings(remaining):
            yield ((first, second),)+tail


def block_budget_checks():
    cases = [("odd_three", [F(3, 5), F(3, 10), F(1, 10)], F(23, 10)),
             ("flat_four", [F(1, 4)]*4, F(21, 10)),
             ("scalar_branch_four", [F(9, 20), F(1, 4), F(3, 20), F(3, 20)], F(5)),
             ("odd_five", [F(1, 2), F(1, 4), F(3, 20), F(2, 25), F(1, 50)], F(14, 5)),
             ("even_six", [F(3, 5), F(1, 5), F(1, 10), F(3, 50), F(1, 25), F(0)], F(5, 2))]
    chi = np.linalg.eigh((X+Z)/ROOT2)[1][:, -1]
    records = []
    for name, exact_spectrum, exact_t in cases:
        require(sum(exact_spectrum) == 1, "normalized rational spectrum")
        lam, t = np.array(list(map(float, exact_spectrum))), float(exact_t)
        dimension, scalar = len(lam), 1/(t-ROOT2)
        errors, values, angles, gains = {}, {}, {}, {}
        for first, second in itertools.combinations(range(dimension), 2):
            value, angle = psi_support(t, lam[first], lam[second])
            values[first, second], angles[first, second] = value, angle
            gains[first, second] = max(0.0, value-scalar*(lam[first]+lam[second]))
        outer = [(j, dimension-1-j) for j in range(dimension//2)]
        require(all(gains[outer[j]]+TOL >= gains[outer[j+1]] for j in range(len(outer)-1)),
                "decreasing outer-pair gains")
        all_matchings = list(partial_matchings(tuple(range(dimension))))
        budgets = []
        for budget in range(dimension//2+1):
            formula = scalar+sum(gains[pair] for pair in outer[:budget])
            exhaustive = scalar+max(sum(gains[pair] for pair in matching)
                                    for matching in all_matchings if len(matching) <= budget)
            compare(errors, f"finite_matching_budget_{budget}", formula, exhaustive)
            b, d = np.eye(dimension, dtype=complex), np.eye(dimension, dtype=complex)
            active = 0
            for pair in outer[:budget]:
                if gains[pair] <= 1e-12:
                    continue
                active += 1
                a = angles[pair]
                bb = np.sqrt(max(0.0, 2-a*a))
                b[np.ix_(pair, pair)] = (a*Z+bb*X)/ROOT2
                d[np.ix_(pair, pair)] = (a*Z-bb*X)/ROOT2
            compare(errors, f"B_reflection_budget_{budget}", b @ b, np.eye(dimension))
            compare(errors, f"D_reflection_budget_{budget}", d @ d, np.eye(dimension))
            # A fixed Fourier basis also checks arbitrary complex eigenvectors.
            labels = np.arange(dimension)
            unitary = np.exp(2j*np.pi*np.outer(labels, labels)/dimension)/np.sqrt(dimension)
            rho = (unitary*lam) @ unitary.conj().T
            compressed = weighted_resolvent(t, rho, unitary @ b @ unitary.conj().T,
                                           unitary @ d @ unitary.conj().T)
            compare(errors, f"attained_norm_budget_{budget}", np.linalg.eigvalsh(compressed)[-1], formula)
            compare(errors, f"common_reference_budget_{budget}", np.vdot(chi, compressed @ chi), formula)
            budgets.append({"budget": budget, "active_blocks": active, "value": float(formula)})
        first_pair, second_pair = (0, dimension-1), (dimension-2, dimension-1)
        fixed_candidates = [(1-lam[p]-lam[q])*scalar+values[p, q]
                            for p, q in (first_pair, second_pair)]
        fixed_formula = max(fixed_candidates)
        all_plane_values = [(1-lam[p]-lam[q])*scalar+values[p, q] for p, q in values]
        compare(errors, "fixed_rank11_finite_plane_choices", fixed_formula, max(all_plane_values))
        selected = (first_pair, second_pair)[int(np.argmax(fixed_candidates))]
        a = angles[selected]
        bb = np.sqrt(max(0.0, 2-a*a))
        b, d = np.eye(dimension, dtype=complex), np.eye(dimension, dtype=complex)
        b[np.ix_(selected, selected)], d[np.ix_(selected, selected)] = (a*Z+bb*X)/ROOT2, (a*Z-bb*X)/ROOT2
        require(np.count_nonzero(np.linalg.eigvalsh(b) < 0) == 1 and
                np.count_nonzero(np.linalg.eigvalsh(d) < 0) == 1, "fixed minority ranks one")
        fixed_compressed = weighted_resolvent(t, np.diag(lam), b, d)
        compare(errors, "fixed_rank11_attainment", np.linalg.eigvalsh(fixed_compressed)[-1], fixed_formula)
        if name == "flat_four":
            flat_formula = scalar/2+(t*t-2)/(2*t*(t*t-4))
            compare(errors, "fixed_rank11_flat_formula", fixed_formula, flat_formula)
        if name == "scalar_branch_four":
            require(all(value <= 1e-12 for value in gains.values()), "all-scalar gain branch exercised")
            require(fixed_formula < scalar-1e-3, "fixed-signature loss differs from union")
            require(fixed_candidates[1] > fixed_candidates[0]+1e-4,
                    "second fixed-signature branch genuinely needed")
        records.append({"case": name, "dimension": dimension, "spectrum_exact": list(map(str, exact_spectrum)),
                        "t_exact": str(exact_t), "partial_matchings_checked": len(all_matchings),
                        "budget_values": budgets, "fixed_minority_rank11_value": float(fixed_formula),
                        "fixed_minority_rank11_candidates": list(map(float, fixed_candidates)),
                        "outer_pair_gains": [float(gains[pair]) for pair in outer],
                        "relative_identity_residuals": errors})
    return records


def partial_reference(matrix):
    return np.einsum("rqrs->qs", matrix.reshape(4, 4, 4, 4))


def amplified_dual(v, matrix):
    blocks = matrix.reshape(2, 4, 2, 4)
    result = np.empty((2, 2, 2, 2), dtype=complex)
    for row in range(2):
        for column in range(2):
            result[row, :, column, :] = v.conj().T @ kron(np.eye(4), blocks[row, :, column, :]) @ v
    return result.reshape(4, 4)


def lift_earlier(matrix):
    return kron(matrix, I).reshape(4, 4, 2, 4, 4, 2).transpose(0, 2, 1, 3, 5, 4).reshape(32, 32)


def reflection_obstruction_checks():
    errors = {}
    a, b = 2/np.sqrt(3), np.sqrt(2/3)
    cosine, sine = 399/401, 40/401
    first_z, first_x = a*word("ZI"), b*word("XI")
    second_z = a*cosine*word("IZ")-b*sine*word("ZZ")
    second_x = b*cosine*word("ZX")+a*sine*word("IX")
    readouts = [(first_z+first_x)/ROOT2, (first_z-first_x)/ROOT2,
                (second_z+second_x)/ROOT2, (second_z-second_x)/ROOT2]
    for index, matrix in enumerate(readouts):
        compare(errors, f"earlier_reflection_{index}", matrix @ matrix, np.eye(4))
        compare(errors, f"earlier_balanced_trace_{index}", np.trace(matrix), 0)
    earlier = sum(kron(word(ref), matrix) for ref, matrix in zip(["XI", "ZI", "IX", "IZ"], readouts))
    bisector = a*word("ZIZI")+b*word("XIXI")+a*cosine*word("IZIZ")-b*sine*word("IZZZ")
    bisector += b*cosine*word("IXZX")+a*sine*word("IXIX")
    rotation = np.cos(np.pi/8)*I-1j*np.sin(np.pi/8)*Y
    change = kron(rotation, rotation, np.eye(4))
    compare(errors, "original_vs_bisector_coordinates", earlier, change @ bisector @ change.conj().T)
    spectrum = sorted(a*alpha+a*cosine*beta+a*sine*r+sign*b*np.sqrt(1+(r*cosine-beta*sine)**2)
                      for alpha, beta, r, sign in itertools.product([-1, 1], repeat=4))
    eigenvalues, eigenvectors = np.linalg.eigh(earlier)
    compare(errors, "complete_sector_spectrum", eigenvalues, spectrum)
    upper = (1680+2*np.sqrt(144841))/(401*np.sqrt(3))
    second = (1520+2*np.sqrt(176761))/(401*np.sqrt(3))
    compare(errors, "leading_eigenvalues", eigenvalues[-2:], [second, upper])
    require(eigenvalues[-3] < 2 and upper > second, "actual leading ordering and tail cap")
    d = cosine-sine
    q = d/np.sqrt(1+d*d)
    phi = np.diag([np.sqrt((1+q)/2), np.sqrt((1-q)/2)])
    bell = np.eye(2)/ROOT2
    omega = np.einsum("ra,sb->rsab", phi, bell).reshape(16)
    omega = change @ omega
    gamma = word("YYII")
    negative = gamma @ omega
    p_plus = np.outer(omega, omega.conj())
    p_minus = np.outer(negative, negative.conj())
    rho = partial_reference(p_plus)
    cross = partial_reference(np.outer(omega, negative.conj()))
    compare(errors, "top_eigenvector", earlier @ omega, upper*omega)
    compare(errors, "negative_eigenvector", earlier @ negative, -upper*negative)
    compare(errors, "top_memory_marginal", rho, (np.eye(4)+q*word("ZI"))/4)
    compare(errors, "chiral_cross_marginal", cross, word("YY")/(4*np.sqrt(1+d*d)))
    p0, p1 = (I+Z)/2, (I-Z)/2
    last_b, last_d = kron(p0, Z)+kron(p1, I), kron(p0, X)+kron(p1, I)
    for name, matrix in [("B", last_b), ("D", last_d)]:
        compare(errors, f"last_reflection_{name}", matrix @ matrix, np.eye(4))
        require(np.count_nonzero(np.linalg.eigvalsh(matrix) < 0) == 1, "last minority rank one")
    h3 = kron(X, last_b)+kron(Z, last_d)
    target, gap = 4+ROOT2, upper-second
    t = target-second
    positive_test = gap*weighted_resolvent(t, rho, last_b, last_d)
    cross_block = weighted_resolvent(t, cross, last_b, last_d)
    compare(errors, "signed_cross_block_zero", cross_block, np.zeros((2, 2)))
    a_matrix = positive_test/gap
    signed_test = gap*(a_matrix-(upper+second)*cross_block @
                      np.linalg.inv(I+(upper+second)*a_matrix) @ cross_block)
    compare(errors, "signed_equals_unsigned_test", signed_test, positive_test)
    minimum_test = float(np.linalg.eigvalsh(positive_test)[0])
    require(minimum_test > 33/32, "both envelopes fail above exact margin")
    unsigned_envelope = second*np.eye(16)+gap*p_plus
    signed_envelope = unsigned_envelope-(upper+second)*p_minus
    unsigned_max = float(np.linalg.eigvalsh(lift_earlier(unsigned_envelope)+kron(np.eye(4), h3))[-1])
    signed_max = float(np.linalg.eigvalsh(lift_earlier(signed_envelope)+kron(np.eye(4), h3))[-1])
    require(unsigned_max > target and signed_max > target, "full signed and unsigned envelopes fail")
    require(np.linalg.eigvalsh(unsigned_envelope-earlier)[0] >= -TOL and
            np.linalg.eigvalsh(signed_envelope-earlier)[0] >= -TOL, "both are valid spectral envelopes")
    head = eigenvectors[:, [-1, -2]]
    images = [partial_reference(head @ p @ head.conj().T) for p in [I, X, Y, Z]]
    for index, image in enumerate(images):
        compare(errors, f"copying_head_diagonal_output_{index}", image, np.diag(np.diag(image)))
    baseline_two = 2*np.eye(16)+head @ np.diag([upper-2, second-2]) @ head.conj().T
    require(np.linalg.eigvalsh(baseline_two-earlier)[0] >= -TOL, "two-mode baseline two valid")
    third_cases = [("one_block_failure_pair", last_b, last_d),
                   ("one_block_rank12_pair", last_b, kron(p0, X)+kron(p1, Z)),
                   ("complex_full_pair", (word("XI")+word("YZ"))/ROOT2,
                    (word("ZI")+word("YX"))/ROOT2)]
    final_records = []
    for name, third_b, third_d in third_cases:
        last = kron(X, third_b)+kron(Z, third_d)
        full_norm = float(np.linalg.norm(lift_earlier(earlier)+kron(np.eye(4), last), 2))
        require(full_norm < 21/4, "actual full norm safely bounded")
        weights = kron(I, np.diag(np.sqrt([upper-2, second-2])))
        two_test = weights @ amplified_dual(head, np.linalg.inv((2+ROOT2)*np.eye(8)-last)) @ weights
        two_max = float(np.linalg.eigvalsh(two_test)[-1])
        require(two_max < 1, "two-positive-mode envelope succeeds")
        record = {"last_pair": name, "actual_full_norm": full_norm,
                  "two_mode_test_maximum": two_max}
        if name == "one_block_rank12_pair":
            compare(errors, "rank12_B_reflection", third_b @ third_b, np.eye(4))
            compare(errors, "rank12_D_reflection", third_d @ third_d, np.eye(4))
            require(np.count_nonzero(np.linalg.eigvalsh(third_b) < 0) == 1 and
                    np.count_nonzero(np.linalg.eigvalsh(third_d) < 0) == 2,
                    "rank12 last minority ranks")
            rank12_test = gap*weighted_resolvent(t, rho, third_b, third_d)
            compare(errors, "rank12_signed_cross_zero", weighted_resolvent(t, cross, third_b, third_d),
                    np.zeros((2, 2)))
            record["one_mode_test_minimum"] = float(np.linalg.eigvalsh(rank12_test)[0])
            require(record["one_mode_test_minimum"] > 33/32, "rank12 signed and unsigned failure")
        final_records.append(record)
    return {"U": float(upper), "m": float(second), "third_eigenvalue": float(eigenvalues[-3]),
            "pole_distance": float(t-2), "top_marginal_bias": float(q),
            "one_mode_test_minimum": minimum_test, "one_mode_test_maximum": float(np.linalg.eigvalsh(positive_test)[-1]),
            "unsigned_envelope_maximum": unsigned_max, "signed_envelope_maximum": signed_max,
            "actual_and_two_mode_checks": final_records, "relative_identity_residuals": errors}


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
              "exact_constants": exact_checks(), "block_budget_constructions": block_budget_checks(),
              "reflection_envelope_obstruction": reflection_obstruction_checks(),
              "maximum_matrix_dimension": 32,
              "scope": "Five fixed spectra, finite partial matchings and explicit attainment; one exact physical reflection example with three third-pair diagnostics, including minority ranks (11) and (12). Scalar cubic-root and support bisections use floating-point approximations, not rigorous interval certificates. Universal proofs are analytical. No angle grid, matrix optimizer, unrestricted converse, or priority claim."}
    residuals = [value for record in report["block_budget_constructions"]
                 for value in record["relative_identity_residuals"].values()]
    residuals += list(report["reflection_envelope_obstruction"]["relative_identity_residuals"].values())
    report["matrix_and_matching_identity_count"] = len(residuals)
    report["maximum_relative_identity_residual"] = max(residuals)
    report["block_budget_attainment_count"] = sum(len(row["budget_values"]) for row in report["block_budget_constructions"])
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
