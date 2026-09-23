#!/usr/bin/env python3
"""Small deterministic checks for the product-diagonal profile benchmark.

The checks use supplied spectra and local bases, with matrices of size at most
8 by 8. Scalar conjugates use the proved monotonicity of f' and floating-point
bisection brackets; they are not formal interval-arithmetic certificates or
optimizer output. No asymptotic coding, unrestricted converse, or novelty
claim is inferred from these diagnostics.

    python tools/check_profile_rate.py --output results/profile_rate.json
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
import platform
from pathlib import Path

import numpy as np

from check_asymmetric_rate import RateDiagnostic, ROUNDOFF_BOUND, entropy, f, h
from check_entropy_geometry import I, X, Y, Z, local, tensor, trace_norm

BASE = "3ebde02b2d9d5dcdcd0dd445e4a16b4f5aaf03b0"
WEIGHTS = ((.7, .25), (1.2, .75), (1.4, 1.0), (1.8, 1.4), (2.0, 1.5))
BRACKET_WIDTH = 2e-14


def f_prime(v):
    if not 0 <= v <= 1:
        raise ValueError("Derivative argument must lie in [0,1].")
    if v == 0:
        return 0.0
    if v == 1:
        return 1 / math.log(2)
    s = math.sqrt(1 - v * v)
    return v * math.atanh(s) / (s * math.log(2))


def support_data(a, b):
    """Return an upper bracket for max(hypot(a,b), a+f*(b)), a>=b.

    Analytically f' is strictly increasing from 0 to 1/ln(2). For an
    interior stationary point, b*v_hi-f(v_lo) bounds b*v-f(v) throughout
    the bracket because b>=0 and f is increasing. All numbers here remain
    floating-point diagnostics, rather than directed-rounding enclosures.
    """
    if not a >= b >= 0:
        raise ValueError("Support weights must satisfy a >= b >= 0.")
    endpoint_derivative = 1 / math.log(2)
    if b == 0:
        lo = hi = 0.0
        conjugate_lower = conjugate_upper = 0.0
        case = "zero_weight_endpoint"
    elif b >= endpoint_derivative:
        lo = hi = 1.0
        conjugate_lower = conjugate_upper = b - 1
        case = "unit_contrast_endpoint"
    else:
        lo, hi = 0.0, 1.0
        for _ in range(60):
            middle = (lo + hi) / 2
            if f_prime(middle) < b:
                lo = middle
            else:
                hi = middle
            if hi - lo <= BRACKET_WIDTH:
                break
        else:
            raise RuntimeError("Stationary-point bracket did not converge.")
        if not f_prime(lo) <= b <= f_prime(hi):
            raise RuntimeError("Floating-point derivative bracket failed.")
        middle = (lo + hi) / 2
        conjugate_lower = b * middle - f(middle)
        conjugate_upper = b * hi - f(lo)
        case = "interior_monotone_derivative_bracket"
    return dict(a=a, b=b, stationary_case=case,
                contrast_bracket=[lo, hi], bracket_width=hi - lo,
                derivative_at_bracket=[f_prime(lo), f_prime(hi)],
                conjugate_lower=conjugate_lower,
                conjugate_upper=conjugate_upper,
                free_disk_support=math.hypot(a, b),
                profile_support_lower=max(math.hypot(a, b), a + conjugate_lower),
                profile_support_upper=max(math.hypot(a, b), a + conjugate_upper),
                bracket_scope="Floating-point check of the analytically monotone derivative; not an interval-arithmetic certificate.")


def profile_entropy_floor(x, z, test, label):
    radial_square = x * x + z * z
    if radial_square <= 1:
        return 0.0
    radicand = test.probability(2 - radial_square, label + "_radicand")
    return h((1 - math.sqrt(radicand)) / 2)


def qubit_root(radius, direction, test):
    direction = np.asarray(direction, float)
    direction /= np.linalg.norm(direction)
    axis = sum(coordinate * pauli for coordinate, pauli in zip(direction, (X, Y, Z)))
    spectrum = np.array([(1 + radius) / 2, (1 - radius) / 2])
    root = (math.sqrt(spectrum[0]) * (I + axis)
            + math.sqrt(spectrum[1]) * (I - axis)) / 2
    rho = (I + radius * axis) / 2
    test.equal(root @ root, rho)
    test.equal(np.trace(rho), 1)
    test.equal(axis @ axis, I)
    return direction, spectrum, root


def check_qubit(label, radius, direction, tolerance):
    test = RateDiagnostic(label, tolerance)
    direction, spectrum, root = qubit_root(radius, direction, test)
    x = test.probability(trace_norm(root @ X @ root), "F_X")
    z = test.probability(trace_norm(root @ Z @ root), "F_Z")
    x_formula = math.sqrt(1 - radius * radius + radius * radius * direction[0] ** 2)
    z_formula = math.sqrt(1 - radius * radius + radius * radius * direction[2] ** 2)
    test.equal(x, x_formula)
    test.equal(z, z_formula)
    seed_entropy = entropy(spectrum)
    gamma = profile_entropy_floor(x, z, test, "profile_gamma")
    test.le(gamma, seed_entropy)
    if direction[1] == 0:
        test.equal(gamma, seed_entropy)
    radial_record = None
    radius_xz = math.hypot(x, z)
    if radius_xz > 1:
        larger, smaller = max(x, z), min(x, z)
        endpoint_contrast = test.probability(smaller / larger, "ray_endpoint_contrast")
        mixture_weight = test.probability((radius_xz - 1) / (radius_xz / larger - 1),
                                         "ray_mixture_weight")
        disk_x, disk_z = x / radius_xz, z / radius_xz
        axis_x, axis_z = ((1.0, endpoint_contrast) if x >= z
                          else (endpoint_contrast, 1.0))
        test.equal((1 - mixture_weight) * disk_x + mixture_weight * axis_x, x)
        test.equal((1 - mixture_weight) * disk_z + mixture_weight * axis_z, z)
        ray_cost = mixture_weight * f(endpoint_contrast)
        test.le(ray_cost, gamma)
        radial_record = dict(free_disk_point=[disk_x, disk_z],
                             exact_axis_point=[axis_x, axis_z],
                             exact_axis_weight=mixture_weight, ray_mixture_cost=ray_cost)
    weighted = []
    for a, b in WEIGHTS:
        support = support_data(a, b)
        for orientation, first, second in (("XZ", x, z), ("ZX", z, x)):
            value = a * first + b * second - seed_entropy
            test.le(value, support["profile_support_upper"])
            weighted.append(dict(orientation=orientation, a=a, b=b,
                                 weighted_score_minus_entropy=value,
                                 profile_support_upper=support["profile_support_upper"]))
    test.data.update(matrix_dimension=2, supplied_bloch_radius=radius,
                     normalized_bloch_direction=direction.tolist(),
                     supplied_spectrum=spectrum.tolist(),
                     trace_norm_scores=[x, z], formula_scores=[x_formula, z_formula],
                     entropy_bits=seed_entropy, minimal_qubit_profile_entropy=gamma,
                     radial_mixture=radial_record, weighted_support_checks=weighted,
                     scope="One supplied qubit state, including possible Y component; exact score and profile-entropy formulas and finite weighted inequalities.")
    return test.finish()


def check_product_diagonal(label, weights, directions, tolerance):
    test = RateDiagnostic(label, tolerance)
    p = np.asarray(weights, float)
    test.require(bool(np.all(p >= 0)), "supplied weights must be nonnegative")
    p = p / p.sum()
    n = len(directions)
    test.require(len(p) == 2 ** n, "supplied spectrum has wrong length")
    test.equal(p.sum(), 1)
    bases = []
    normalized_directions = []
    for direction in directions:
        direction = np.asarray(direction, float)
        direction /= np.linalg.norm(direction)
        normalized_directions.append(direction.tolist())
        axis = sum(coordinate * pauli for coordinate, pauli in zip(direction, (X, Y, Z)))
        _, vectors = np.linalg.eigh(axis)
        basis = vectors[:, ::-1]
        test.equal(basis.conj().T @ axis @ basis, Z)
        test.equal(basis.conj().T @ basis, I)
        bases.append(basis)
    unitary = tensor(bases)
    test.equal(unitary.conj().T @ unitary, np.eye(2 ** n))
    root = (unitary * np.sqrt(p)) @ unitary.conj().T
    test.equal(np.trace(root @ root), 1)
    total_entropy = entropy(p)
    conditional_sum = 0.0
    full_scores = []
    sites = []
    for site in range(n):
        mask = 1 << (n - 1 - site)
        edge_entropy = 0.0
        edge_scores = np.zeros(2)
        marginal_weights = []
        edge_records = []
        for vertex in range(2 ** n):
            if vertex & mask:
                continue
            left, right = p[vertex], p[vertex ^ mask]
            mass = float(left + right)
            marginal_weights.append(mass)
            if mass == 0:
                edge_records.append(dict(vertices=[vertex, vertex ^ mask], mass=0.0,
                                         skipped_zero_mass=True))
                continue
            conditional = np.array([left / mass, right / mass])
            conditional_root = (bases[site] * np.sqrt(conditional)) @ bases[site].conj().T
            scores = np.array([trace_norm(conditional_root @ pauli @ conditional_root)
                               for pauli in (X, Z)])
            formulas = [math.sqrt(4 * left * right + (left - right) ** 2
                                 * normalized_directions[site][coordinate] ** 2)
                        for coordinate in (0, 2)]
            test.equal(mass * scores, formulas)
            local_entropy = entropy(conditional)
            edge_entropy += mass * local_entropy
            edge_scores += mass * scores
            edge_records.append(dict(vertices=[vertex, vertex ^ mask], mass=mass,
                                     conditional_probabilities=conditional.tolist(),
                                     conditional_scores=scores.tolist(),
                                     conditional_entropy_bits=local_entropy))
        full = np.array([trace_norm(root @ local(n, site, pauli) @ root)
                         for pauli in (X, Z)])
        test.equal(full, edge_scores)
        test.equal(edge_entropy, total_entropy - entropy(marginal_weights))
        conditional_sum += edge_entropy
        full_scores.append(full)
        sites.append(dict(site=site, full_matrix_scores=full.tolist(),
                          edge_sum_scores=edge_scores.tolist(),
                          conditional_entropy_bits=edge_entropy, edges=edge_records))
    test.le(conditional_sum, total_entropy)
    weighted = []
    for a, b in WEIGHTS:
        support = support_data(a, b)
        for orientation, coordinates in (("XZ", (0, 1)), ("ZX", (1, 0))):
            entropy_floor = math.fsum(a * scores[coordinates[0]] + b * scores[coordinates[1]]
                                      - support["profile_support_upper"] for scores in full_scores)
            test.le(entropy_floor, conditional_sum)
            test.le(entropy_floor, total_entropy)
            weighted.append(dict(a=a, b=b, orientation=orientation,
                                 sum_weighted_profile_entropy_lower_bound=entropy_floor,
                                 profile_support_upper=support["profile_support_upper"]))
    test.data.update(matrix_dimension=2 ** n, input_qubits=n,
                     supplied_spectrum=p.tolist(), supplied_positive_entries=sum(w > 0 for w in weights),
                     normalized_local_directions=normalized_directions,
                     entropy_bits=total_entropy, sum_conditional_entropies=conditional_sum,
                     sites=sites, weighted_support_checks=weighted,
                     scope="One correlated product-diagonal state with supplied spectrum and local bases; edge trace-norm identities, classical conditional-entropy chain, and profile support inequalities.")
    return test.finish()


def check_conjugate(a, b, tolerance):
    test = RateDiagnostic(f"support_conjugate_a{a}_b{b}", tolerance)
    data = support_data(a, b)
    lo, hi = data["contrast_bracket"]
    test.le(hi - lo, BRACKET_WIDTH)
    test.le(data["conjugate_lower"], data["conjugate_upper"])
    if 0 < b < 1 / math.log(2):
        test.le(f_prime(lo), b)
        test.le(b, f_prime(hi))
    sampled = []
    for v in (0.0, .1, .25, .5, .75, .9, 1.0):
        value = b * v - f(v)
        test.le(value, data["conjugate_upper"])
        # The reversed exact-axis arm is dominated for a>=b because f* is
        # 1-Lipschitz; this is also checked at these fixed arm points.
        test.le(b + a * v - f(v), data["profile_support_upper"])
        sampled.append(dict(contrast=v, conjugate_objective=value))
    test.data.update(matrix_dimension=1, **data, fixed_contrast_checks=sampled,
                     scope="One-dimensional conjugate bracket and selected scalar support checks; analytic convexity carries the all-contrast result.")
    return test.finish()


def retention(x, z):
    if x * x + z * z <= 1:
        return 0.0
    return x + z - 1 - math.sqrt(2 * (1 - x) * (1 - z))


def check_rational_mixture(tolerance):
    test = RateDiagnostic("rational_profile_mixture", tolerance)
    weight = Fraction(87, 100)
    exact_axis = (Fraction(1), Fraction(15, 29))
    free_circle = (Fraction(12, 13), Fraction(5, 13))
    target = tuple(weight * e + (1 - weight) * c for e, c in zip(exact_axis, free_circle))
    test.require(target == (Fraction(99, 100), Fraction(1, 2)), "exact rational mixture mismatch")
    test.require(sum(c * c for c in free_circle) == 1, "free point is not on the unit circle")
    cost = float(weight) * f(float(exact_axis[1]))
    comparison = retention(*map(float, target))
    test.equal(comparison, .39)
    test.require(cost < .326 < comparison, "strict scalar improvement failed")
    test.data.update(matrix_dimension=1, exact_axis_weight=str(weight),
                     exact_axis_point=list(map(str, exact_axis)), free_circle_point=list(map(str, free_circle)),
                     exact_rational_target=list(map(str, target)),
                     mixture_entropy_cost=cost, original_site_retention_rate=comparison,
                     inherited_exact_axis_rate=f(.5), saving_over_retention=comparison - cost,
                     scope="Exact Fraction arithmetic for the profile mixture and a floating-point entropy-cost check; the separate analytical proof establishes asymptotic achievability and the strict gap.")
    return test.finish()


def check_phase_boundary(tolerance):
    test = RateDiagnostic("profile_phase_boundary", tolerance)
    tau = 2 * (1 / math.log(2) - 1) ** 2
    profiles = [(.8, .8), (.95, .9), (.99, .5), (.97, .7), (1 - tau * .4, .6)]
    records = []
    for index, (x, z) in enumerate(profiles):
        test.require(x >= z and x * x + z * z > 1, "profile must be in the stated ordered nonclassical region")
        w = retention(x, z)
        circle_x, circle_z = (x - w) / (1 - w), (z - w) / (1 - w)
        test.equal(circle_x * circle_x + circle_z * circle_z, 1)
        multiplier = 1 / (circle_x + circle_z - 1)
        a, b = multiplier * circle_x, multiplier * circle_z
        test.equal(math.hypot(a, b), a + b - 1)
        test.equal(a * x + b * z - multiplier, w)
        ratio = (1 - x) / (1 - z)
        if index == len(profiles) - 1:
            test.equal(ratio, tau)
            test.equal(b, 1 / math.log(2))
            region = "analytic_boundary"
        elif ratio > tau:
            test.require(b > 1 / math.log(2), "retention side derivative criterion failed")
            support = support_data(a, b)
            test.equal(support["profile_support_upper"], multiplier)
            region = "retention_equality_side"
        else:
            test.require(b < 1 / math.log(2), "strict-improvement side derivative criterion failed")
            support = support_data(a, b)
            test.require(support["profile_support_lower"] > multiplier,
                         "the exact-axis interior did not exceed the retention support")
            region = "strict_improvement_side"
        records.append(dict(x=x, z=z, retention_weight=w,
                            deficit_ratio=ratio, retention_circle_point=[circle_x, circle_z],
                            retention_support_weights=[a, b], region=region))
    test.data.update(matrix_dimension=1, phase_threshold=tau,
                     endpoint_curve_derivative=1 / math.log(2), profiles=records,
                     scope="Five fixed profiles and the analytic boundary parameter; these samples do not prove the whole phase diagram.")
    return test.finish()


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("Tolerance must be finite and positive.")
    qubits = [("maximally_mixed_qubit", 0.0, [1, 0, 0]),
              ("pure_bisector", 1.0, [1, 0, 1]),
              ("pure_qubit_with_Y", 1.0, [2, 2, 1]),
              ("mixed_qubit_with_Y", .7, [1, 2, -.5]),
              ("mixed_XZ_qubit", .8, [3, 0, 4]),
              ("mixture_exact_axis_qubit", math.sqrt(1 - (15 / 29) ** 2), [1, 0, 0]),
              ("mixture_free_circle_qubit", 1.0, [12, 0, 5])]
    cases = [check_qubit(*specification, tolerance) for specification in qubits]
    products = [("n2_correlated_XZ_product_diagonal", [1, 2, 3, 7], [[1, 0, 1], [3, 0, 4]]),
                ("n2_sparse_product_diagonal_with_Y", [7, 0, 0, 13], [[1, 1, 1], [1, 2, -.5]]),
                ("n3_correlated_product_diagonal_with_Y", [1, 3, 2, 7, 9, 4, 5, 11],
                 [[1, 1, 1], [1, 2, -.5], [.2, -.7, 1]]),
                ("n3_sparse_product_diagonal_with_zero_mass_edge", [2, 0, 0, 5, 0, 0, 7, 0],
                 [[1, 0, 1], [3, 0, 4], [1, 2, -.5]])]
    cases.extend(check_product_diagonal(*specification, tolerance) for specification in products)
    cases.extend(check_conjugate(a, b, tolerance) for a, b in WEIGHTS)
    cases.extend((check_rational_mixture(tolerance), check_phase_boundary(tolerance)))
    if len(cases) != 18:
        raise RuntimeError("The documented diagnostic case count changed.")
    return dict(status="PASS", research_base=BASE, python=platform.python_version(), numpy=np.__version__,
                tolerance=tolerance, case_count=len(cases),
                maximum_matrix_dimension=max(case["matrix_dimension"] for case in cases),
                max_identity_error=max(case["max_identity_error"] for case in cases),
                max_inequality_violation=max(case["max_inequality_violation"] for case in cases),
                endpoint_roundoff_bound=ROUNDOFF_BOUND,
                endpoint_adjustment_count=sum(len(case["endpoint_adjustments"]) for case in cases),
                conjugate_bracket_width_target=BRACKET_WIDTH, cases=cases,
                scope="Finite deterministic qubit, product-diagonal, scalar-conjugate, rational-mixture, and phase-boundary checks. No optimizer, random search, numerical rank inference, complete-instrument enumeration, large-block simulation, asymptotic rate certification, unrestricted converse, or novelty certification. Every endpoint adjustment is bounded and listed; conjugate brackets use ordinary floating-point arithmetic.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tolerance", type=float, default=1e-10)
    args = parser.parse_args()
    report = run(args.tolerance)
    text = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
