#!/usr/bin/env python3
"""Small deterministic diagnostics for the entropy/geometry continuation.

Thirteen cases check explicit translation instruments, a 32-vertex support
graph, two-qubit SLD identities, and one-qubit-memory stability certificates.
No optimizer, random search, eigenvalue clipping, or numerical rank inference
is used. Passing finite examples is not proof of a theorem or of novelty.

    python tools/check_entropy_geometry.py --output results/entropy_geometry.json
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np

BASE = "f761bbca3ba3c1b263a1914175e3bdab94be70a7"
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
HADAMARD = (X + Z) / math.sqrt(2)


def tensor(items):
    result = np.ones((1, 1), complex)
    for item in items:
        result = np.kron(result, item)
    return result


def local(n, site, operator):
    return tensor(operator if k == site else I for k in range(n))


def entropy(probabilities):
    return math.fsum(-float(p) * math.log2(float(p))
                     for p in probabilities if p > 0)


def trace_norm(matrix):
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


class Diagnostic:
    def __init__(self, label, tolerance):
        self.data = {"label": label}
        self.tolerance = tolerance
        self.identities = []
        self.violations = []

    def require(self, condition, message):
        if not condition:
            raise RuntimeError(f"{self.data['label']}: {message}")

    def equal(self, actual, expected):
        residual = float(np.max(np.abs(np.asarray(actual) - expected)))
        self.require(math.isfinite(residual), "nonfinite identity residual")
        self.identities.append(residual)

    def le(self, actual, bound):
        residual = float(actual - bound)
        self.require(math.isfinite(residual), "nonfinite inequality residual")
        self.violations.append(max(0.0, residual))

    def finish(self):
        identity = max(self.identities, default=0.0)
        violation = max(self.violations, default=0.0)
        self.require(max(identity, violation) <= self.tolerance,
                     f"residual exceeds tolerance: {identity}, {violation}")
        self.data.update(max_identity_error=identity,
                         max_inequality_violation=violation,
                         identity_checks=len(self.identities),
                         inequality_checks=len(self.violations))
        return self.data


def shifted_vertex(vertex, n, shift):
    bits = [(vertex >> (n - 1 - k)) & 1 for k in range(n)]
    return sum(bits[(k - shift) % n] << (n - 1 - k) for k in range(n))


def check_translation_instrument(label, support, probabilities, shifts, tolerance):
    test = Diagnostic(label, tolerance)
    n = 3
    dimension = 2 ** n
    output_dimension = len(support)
    probabilities = np.asarray(probabilities, float)
    test.require(bool(np.all(probabilities > 0)), "support probabilities must be positive")
    test.equal(probabilities.sum(), 1)
    basis = tensor([HADAMARD] * n)
    queries = [local(n, i, p) for i in range(n) for p in (X, Z)]
    tp = np.zeros((dimension, dimension), complex)
    effective = [np.zeros_like(tp) for _ in queries]
    contrasts = np.zeros(n)
    branch_count = 0
    weights = []
    for shift in shifts:
        vertices = [shifted_vertex(v, n, shift) for v in support]
        test.require(len(set(vertices)) == output_dimension, "duplicate support vertex")
        seed_x = np.zeros((output_dimension, dimension), complex)
        for row, (vertex, probability) in enumerate(zip(vertices, probabilities)):
            seed_x[row, vertex] = math.sqrt(probability)
        seed = seed_x @ basis
        test.equal(np.vdot(seed, seed).real, 1)
        diagonal_decoders = []
        matching_decoders = []
        for site in range(n):
            mask = 1 << (n - 1 - site)
            diagonal_decoders.append(np.diag([1 if not v & mask else -1
                                             for v in vertices]))
            matching = np.array([[int(a ^ b == mask) for b in vertices]
                                 for a in vertices], complex)
            matching_decoders.append(matching)
            test.le(float(np.linalg.norm(matching, 2)), 1)
            contrast = float(np.sqrt(probabilities) @ matching.real @ np.sqrt(probabilities))
            contrasts[site] += contrast / len(shifts)
            test.equal(trace_norm(seed @ queries[2 * site + 1] @ seed.conj().T), contrast)
        for translation in range(dimension):
            unitary = tensor(Z if translation & (1 << (n - 1 - k)) else I
                             for k in range(n))
            kraus = seed @ unitary / math.sqrt(len(shifts))
            adjoint = kraus.conj().T
            tp += adjoint @ kraus
            weights.append(float(np.vdot(kraus, kraus).real / dimension))
            for site in range(n):
                sign = -1 if translation & (1 << (n - 1 - site)) else 1
                decoder_x = sign * diagonal_decoders[site]
                decoder_z = matching_decoders[site]
                test.equal(decoder_x @ kraus, kraus @ queries[2 * site])
                effective[2 * site] += adjoint @ decoder_x @ kraus
                effective[2 * site + 1] += adjoint @ decoder_z @ kraus
            branch_count += 1
    test.equal(tp, np.eye(dimension))
    test.equal(sum(weights), 1)
    for site in range(n):
        test.equal(effective[2 * site], queries[2 * site])
        test.equal(effective[2 * site + 1], contrasts[site] * queries[2 * site + 1])
    test.equal(contrasts, np.full(n, contrasts.mean()))
    test.require(branch_count == dimension * len(shifts), "incomplete translation orbit")
    test.data.update(matrix_dimension=dimension, input_qubits=n,
                     maximum_quantum_output_dimension=output_dimension,
                     branch_count=branch_count, original_support=support,
                     supplied_probabilities=probabilities.tolist(), cyclic_shifts=shifts,
                     x_contrasts=[1.0] * n, z_contrasts=contrasts.tolist(),
                     normalized_kraus_weights=weights,
                     scope="Complete instrument, exact-X intertwining, and all six operator identities.")
    return test.finish()


def check_star(tolerance):
    test = Diagnostic("n31_star_support_and_interior_separation", tolerance)
    n, q = 31, 5
    probabilities = np.array([.5] + [1 / (2 * n)] * n)
    vector = np.sqrt(probabilities)
    adjacency = np.zeros((n + 1, n + 1))
    adjacency[0, 1:] = 1
    adjacency[1:, 0] = 1
    radius = math.sqrt(n)
    z = 1 / radius
    x = 9999 / 10000
    radical = math.sqrt(2 * (1 - x) * (1 - z))
    weight = x + z - 1 - radical
    test.equal(probabilities.sum(), 1)
    test.equal(adjacency @ vector, radius * vector)
    test.equal(np.linalg.eigvalsh(adjacency)[-1], radius)
    test.equal(2 * vector[0] * vector[1:], np.full(n, z))
    test.equal(float(vector @ adjacency @ vector), n * z)
    test.require(n + 1 == 2 ** q, "worst-case dimension budget mismatch")
    test.require(radius > q and n * weight > q, "collective separation is not strict")
    test.require(z > 1796 / 10000 and radical < 13 / 1000,
                 "elementary analytic interior estimates failed")
    test.require(n * (1665 / 10000) > q, "rational interior certificate failed")
    test.data.update(matrix_dimension=n + 1, input_qubits=n, quantum_qubits=q,
                     support_size=n + 1, spectral_radius=radius,
                     exact_axis_contrast=z, interior_x_contrast=x,
                     interior_z_contrast=z, interior_local_allocation_weight=weight,
                     total_interior_allocation_weight=n * weight,
                     original_site_retention_cap=q,
                     full_input_space_dimension=2 ** n,
                     full_input_matrix_constructed=False,
                     complete_instrument_enumerated=False,
                     scope="Only a 32-vertex graph and scalar arithmetic; no optimality claim at n=31,D=32.")
    return test.finish()


def complex_basis():
    def rotate(pauli, angle):
        return math.cos(angle) * np.eye(4) + 1j * math.sin(angle) * pauli
    indices = np.arange(4)
    fourier = np.exp(2j * math.pi * np.outer(indices, indices) / 4) / 2
    return (rotate(np.kron(X, Y), .31) @ rotate(np.kron(Z, X), .23)
            @ rotate(np.kron(Y, I), .41) @ rotate(np.kron(I, Z), .17) @ fourier)


def check_sld(label, supplied_spectrum, tolerance):
    test = Diagnostic(label, tolerance)
    p = np.asarray(supplied_spectrum, float)
    test.require(bool(np.all(p >= 0) and np.all(p[:-1] >= p[1:])),
                 "spectrum must be supplied in nonincreasing order")
    test.equal(p.sum(), 1)
    denominator = p[:, None] + p[None, :]
    kernel = np.divide((p[:, None] - p[None, :]) ** 2, denominator,
                       out=np.zeros_like(denominator), where=denominator > 0)
    exact_minimum = float(kernel[0, 1] + kernel[0, 2] + kernel[1, 3] + kernel[2, 3])
    reverse_cost = float(2 * (kernel[0, 3] + kernel[1, 2]))
    assignment_costs = [float(sum(kernel[i, perm[i]] for i in range(4)))
                        for perm in itertools.permutations(range(4))]
    for cost in assignment_costs:
        test.le(cost, reverse_cost)
    test.equal(max(assignment_costs), reverse_cost)
    test.le(2 - entropy(p), exact_minimum)
    paulis = [local(2, site, pauli) for site in range(2) for pauli in (X, Y, Z)]
    spin_flip = np.kron(Y, Y)
    basis_reports = []
    for basis_label, unitary in (("fixed_complex_basis", complex_basis()),
                                ("product_basis_attainer", np.eye(4, dtype=complex))):
        test.equal(unitary.conj().T @ unitary, np.eye(4))
        rho = (unitary * p) @ unitary.conj().T
        root = (unitary * np.sqrt(p)) @ unitary.conj().T
        test.equal(root @ root, rho)
        transformed = [unitary.conj().T @ pauli @ unitary for pauli in paulis]
        information = [.5 * float(np.sum(kernel * np.abs(pauli) ** 2))
                       for pauli in transformed]
        j = .5 * math.fsum(information)
        xz = math.fsum(information[k] for k in (0, 2, 3, 5))
        k_matrix = unitary.conj().T @ spin_flip @ unitary.conj()
        bistochastic = abs(k_matrix) ** 2
        test.equal(k_matrix.T, k_matrix)
        test.equal(k_matrix.conj().T @ k_matrix, np.eye(4))
        test.equal(bistochastic.sum(axis=0), np.ones(4))
        test.equal(bistochastic.sum(axis=1), np.ones(4))
        transition_sum = sum(abs(pauli) ** 2 for pauli in transformed)
        test.equal(transition_sum, 2 * (np.ones((4, 4)) - bistochastic))
        assignment_average = float(np.sum(kernel * bistochastic))
        test.equal(j, float(np.triu(kernel, 1).sum()) - .5 * assignment_average)
        test.le(assignment_average, reverse_cost)
        test.le(exact_minimum, j)
        test.le(j, xz)
        test.le(2 - entropy(p), xz)
        fidelity_values = [trace_norm(root @ paulis[k] @ root) for k in (0, 2, 3, 5)]
        for value, k in zip(fidelity_values, (0, 2, 3, 5)):
            test.le(value * value, 1 - information[k])
        score = math.fsum(fidelity_values)
        test.le(score, 2 * math.sqrt(4 - exact_minimum))
        if basis_label == "product_basis_attainer":
            test.equal(j, exact_minimum)
            test.equal(xz, exact_minimum)
        basis_reports.append(dict(basis=basis_label, xyz_sld_values=information,
                                  half_xyz_sum=j, xz_sum=xz,
                                  bistochastic_assignment_average=assignment_average,
                                  trace_norm_score=score))
    test.data.update(matrix_dimension=4, supplied_spectrum=p.tolist(),
                     supplied_nonzero_entries=int(np.count_nonzero(p)),
                     entropy_bits=entropy(p), exact_orbit_minimum=exact_minimum,
                     reverse_assignment_cost=reverse_cost,
                     enumerated_assignment_count=len(assignment_costs),
                     basis_checks=basis_reports,
                     scope="Two explicit eigenbases, all 24 assignments, and exact product-basis attainment.")
    return test.finish()


def subset_seed(n, retained_site, output_unitary):
    beta = np.array([math.cos(math.pi / 8), math.sin(math.pi / 8)])
    seed = np.zeros((2, 2 ** n), complex)
    for column in range(2 ** n):
        bits = [(column >> (n - 1 - site)) & 1 for site in range(n)]
        seed[bits[retained_site], column] = math.prod(
            beta[bits[site]] for site in range(n) if site != retained_site) / math.sqrt(2)
    return output_unitary @ seed


def check_stability(label, n, retained_site, epsilon, angle, tolerance):
    test = Diagnostic(label, tolerance)
    output_unitary = math.cos(angle) * I + 1j * math.sin(angle) * (X + Y + Z) / math.sqrt(3)
    exact = subset_seed(n, retained_site, output_unitary)
    omega = exact.T.reshape(-1)
    direction = np.array([complex(1 + k % 3, (-1) ** k * (k + 1) / 7)
                          for k in range(len(omega))])
    direction -= omega * np.vdot(omega, direction)
    direction /= np.linalg.norm(direction)
    vector = math.sqrt(1 - epsilon) * omega + math.sqrt(epsilon) * direction
    seed = vector.reshape(2 ** n, 2).T
    test.equal(np.vdot(seed, seed).real, 1)
    paulis = [local(n, site, pauli) for site in range(n) for pauli in (X, Z)]
    decoders = []
    compressed_eigenvalues = []
    active_sites = []
    score_terms = []
    for pauli in paulis:
        compressed = seed @ pauli @ seed.conj().T
        test.equal(compressed, compressed.conj().T)
        eigenvalues, eigenvectors = np.linalg.eigh(compressed)
        test.require(float(np.min(np.abs(eigenvalues))) > 1e-4,
                     "example requires sign eigenvalues safely away from zero")
        signs = np.sign(eigenvalues)
        decoder = (eigenvectors * signs) @ eigenvectors.conj().T
        test.equal(decoder @ decoder, I)
        score = trace_norm(compressed)
        test.equal(np.trace(compressed @ decoder).real, score)
        decoders.append(decoder)
        compressed_eigenvalues.append(eigenvalues.tolist())
        score_terms.append(score)
    for site in range(n):
        if all(abs(np.trace(decoders[2 * site + axis])) < tolerance for axis in (0, 1)):
            active_sites.append(site)
    test.require(active_sites == [retained_site], "example must have one active site")
    for site in range(n):
        if site != retained_site:
            for axis in (0, 1):
                test.equal(decoders[2 * site + axis], I)
    hamiltonian = sum(np.kron(pauli.T, decoder) for pauli, decoder in zip(paulis, decoders))
    test.equal(hamiltonian, hamiltonian.conj().T)
    score = math.fsum(score_terms)
    test.equal(np.vdot(vector, hamiltonian @ vector).real, score)
    optimum = 2 + (n - 1) * math.sqrt(2)
    delta = optimum - score
    test.require(0 <= delta <= 1 / 48, "example lies outside the small-deficit theorem")
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    certificate_vector = eigenvectors[:, -1]
    certificate = certificate_vector.reshape(2 ** n, 2).T
    gap = float(eigenvalues[-1] - eigenvalues[-2])
    test.require(gap > 1.5, "dual-Hamiltonian spectral gap certificate failed")
    # The actual Hamiltonian's top vector is an exact subset seed: its Gram
    # matrix is I/2 at the retained site times the positive bisector elsewhere.
    beta = np.array([math.cos(math.pi / 8), math.sin(math.pi / 8)])
    gram_target = tensor(I / 2 if site == retained_site else np.outer(beta, beta)
                         for site in range(n))
    test.equal(certificate.conj().T @ certificate, gram_target)
    test.equal(certificate @ certificate.conj().T, I / 2)
    certificate_score = math.fsum(trace_norm(certificate @ p @ certificate.conj().T)
                                  for p in paulis)
    test.equal(certificate_score, optimum)
    overlap = abs(np.vdot(certificate_vector, vector)) ** 2
    distance_squared = float(2 - 2 * abs(np.vdot(certificate_vector, vector)))
    test.le(1 - overlap, 2 * delta / 3)
    test.le(distance_squared, 4 * delta / 3)
    test.le(distance_squared, 96 * delta)
    test.le(float(eigenvalues[-1]), optimum)
    test.data.update(matrix_dimension=2 ** (n + 1), input_qubits=n,
                     retained_site=retained_site, supplied_perturbation_weight=epsilon,
                     output_rotation_angle=angle, seed_score=score, exact_optimum=optimum,
                     deficit=delta, active_sites=active_sites,
                     compressed_eigenvalues=compressed_eigenvalues,
                     actual_dual_hamiltonian_top_eigenvalue=float(eigenvalues[-1]),
                     actual_dual_hamiltonian_gap=gap,
                     exact_subset_certificate_score=certificate_score,
                     certificate_overlap_squared=float(overlap),
                     phase_optimized_frobenius_distance_squared=distance_squared,
                     overlap_loss_bound=2 * delta / 3, distance_bound=4 * delta / 3,
                     scope="Actual sign decoders and Hamiltonian; an explicit exact-subset certificate, not a closest-seed optimization.")
    return test.finish()


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("Tolerance must be finite and positive.")
    cases = [check_translation_instrument("n3_star_complete_translation_instrument",
                                          [0, 4, 2, 1], [.5, 1 / 6, 1 / 6, 1 / 6], [0], tolerance),
             check_translation_instrument("n3_asymmetric_complete_flagged_instrument",
                                          [0, 1, 3], [.5, .3, .2], [0, 1, 2], tolerance),
             check_star(tolerance)]
    spectra = [("pure", [1, 0, 0, 0]), ("rank_two", [.75, .25, 0, 0]),
               ("rank_three_unequal", [.5, .3, .2, 0]),
               ("rank_three_repeated", [.5, .25, .25, 0]),
               ("full_rank_unequal", [.55, .25, .15, .05]),
               ("maximally_mixed", [.25, .25, .25, .25])]
    cases.extend(check_sld("two_qubit_sld_" + label, spectrum, tolerance)
                 for label, spectrum in spectra)
    for index, (n, site, epsilon, angle) in enumerate(((1, 0, .0003, .17),
                                                     (3, 0, .001, .29),
                                                     (4, 2, .002, .41),
                                                     (3, 1, .004, .63))):
        cases.append(check_stability(f"one_qubit_stability_{index + 1}",
                                     n, site, epsilon, angle, tolerance))
    if len(cases) != 13:
        raise RuntimeError("The documented diagnostic case count changed.")
    return dict(status="PASS", research_base=BASE, python=platform.python_version(),
                numpy=np.__version__, tolerance=tolerance, case_count=len(cases),
                maximum_matrix_dimension=max(case["matrix_dimension"] for case in cases),
                max_identity_error=max(case["max_identity_error"] for case in cases),
                max_inequality_violation=max(case["max_inequality_violation"] for case in cases),
                cases=cases,
                scope="Finite deterministic identities only; no optimizer, random search, spectral clipping, numerical rank inference, proof certification, or novelty certification. The n=31 case constructs only its 32-vertex support graph.")


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
