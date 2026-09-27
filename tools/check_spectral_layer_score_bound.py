#!/usr/bin/env python3
"""Fixed small-matrix diagnostics for the spectral-layer score bound.

The quantified result and sharpness limit are analytical in the proof note.
No random sampling, grid, optimizer, or large matrix is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform

import numpy as np

BASE = "26a126a729fb483897c8a2e356dc733089c0d2a0"
NOTE = "docs/audits/SPECTRAL_LAYER_SCORE_BOUND.md"
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
    residual = float(np.linalg.norm(np.asarray(actual) - np.asarray(expected)) /
                     max(1., np.linalg.norm(expected)))
    errors[label] = residual
    require(residual <= TOL, label)


def nonnegative(margins, label, value):
    margins[label] = float(value)
    require(value >= -TOL, label)


def norm1_hermitian(matrix):
    return float(np.sum(np.abs(np.linalg.eigvalsh(matrix))))


def exact_checks():
    checks = {}

    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness

    v = Q(1, 1000)
    bias = 2*v/(1+v*v)  # Twice epsilon in the proof note's sharpness state.
    t = (1-v*v)/(1+v*v)
    delta = t*(1-t)
    defect = t-1+bias
    check("sharpness_normalization", bias*bias+t*t == 1,
          "bias=2v/(1+v^2)=2epsilon_note, t=(1-v^2)/(1+v^2)")
    check("sharpness_layer_weights", bias+(1-bias) == 1,
          "w1=bias, w2=1-bias")
    check("sharpness_gap_positive", delta > 0, "delta=t(1-t)>0")
    check("sharpness_defect_positive", defect > 0, "d=t-1+bias>0")
    check("sharpness_defect_factorization", defect == 2*v*(1-v)/(1+v*v),
          "d=2v(1-v)/(1+v^2)")
    check("sharpness_ratio_identity", defect*defect/(2*delta) == (1-v)/(1+v),
          "d^2/(2delta)=(1-v)/(1+v)")
    check("sharpness_refined_equality", defect*defect == 2*(1-bias)*(1-t),
          "d^2=2c(1-b), with c=1-bias and b=t")
    check("sharpness_fixed_ratio", defect*defect/(2*delta) == Q(999, 1001),
          "at v=1/1000, squared ratio is 999/1001")
    check("sharpness_aggregate_identity", (2*defect)**2/(2*2*(2*delta)) == Q(999, 1001),
          "two original queries give the same aggregate ratio")
    check("rank_three_layer_weights", Q(1, 7)+3*Q(2, 7) == 1,
          "spectrum (3/7,2/7,2/7) gives w1=1/7, w3=6/7")
    check("rank_three_nonuniform_strict_gap", 2*5**2 > 7**2,
          "5sqrt2>7 certifies nonuniform score above every flat rank-three score")
    return checks


def root_from_spectrum(vectors, spectrum):
    return (vectors*np.sqrt(spectrum)) @ vectors.conj().T


def fixtures():
    rotation = np.cos(np.pi/8)*I - 1j*np.sin(np.pi/8)*Y
    plus, minus = rotation[:, 0], rotation[:, 1]
    v = 1/1000
    bias = 2*v/(1+v*v)
    y_vectors = np.column_stack([np.array([1, 1j])/R2,
                                np.array([1, -1j])/R2])
    sharp = root_from_spectrum(y_vectors, [(1+bias)/2, (1-bias)/2])
    equality_vectors = np.column_stack([np.kron(plus, plus), np.kron(minus, minus)])
    equality = root_from_spectrum(equality_vectors, [.9, .1])
    singular_vectors = np.zeros((4, 2), complex)
    singular_vectors[0, 0] = 1
    singular_vectors[1, 1] = 1/R2
    singular_vectors[2, 1] = 1j/R2
    singular = root_from_spectrum(singular_vectors, [.75, .25])
    pure = np.outer(y_vectors[:, 0], y_vectors[:, 0].conj())
    bisector_basis = np.kron(rotation, rotation)
    nonuniform = root_from_spectrum(bisector_basis[:, :3], [3/7, 2/7, 2/7])
    indices = np.arange(8)
    fourier = np.exp(2j*np.pi*np.outer(indices, indices)/8)/np.sqrt(8)
    phases = np.exp(1j*np.array([0., .2, -.5, .7, 1.1, -.8, .4, -.3]))
    complex_vectors = phases[:, None]*fourier
    complex_full = root_from_spectrum(complex_vectors, np.array([16, 9, 7, 5, 4, 3, 2, 1])/47)
    mixed = np.eye(16, dtype=complex)/4
    return [("almost_flat_Y_sharpness", sharp, 1, "sharp"),
            ("nonflat_spectral_blocks_same_profile", equality, 2, "equality"),
            ("complex_rank_two_with_query_zero_mode", singular, 2, "singular"),
            ("pure_Y_zero_compressed_queries", pure, 1, "zero"),
            ("nonuniform_rank_three_bisector_support", nonuniform, 2, "nonuniform"),
            ("fixed_complex_full_rank_three_qubit_seed", complex_full, 3, "complex"),
            ("maximally_mixed_four_qubit_seed", mixed, 4, "flat")]


def fixture_case(name, root, n, kind):
    errors, margins = {}, {}
    compare(errors, "root_Hermitian", root, root.conj().T)
    compare(errors, "root_normalized", np.trace(root@root), 1)
    values, vectors = np.linalg.eigh(root)
    nonnegative(margins, "root_positive", values[0])
    keep = np.flatnonzero(values > TOL)[::-1]
    s = values[keep]
    V = vectors[:, keep]
    S = np.diag(s).astype(complex)
    eigenvalues = s*s
    rank = len(s)
    gaps = eigenvalues - np.append(eigenvalues[1:], 0.)
    weights = np.arange(1, rank+1)*gaps
    projections = [np.diag(np.arange(rank) < k).astype(complex) for k in range(1, rank+1)]
    inverse = np.diag(1/s)
    compare(errors, "layer_weight_sum", sum(weights), 1)
    for k, weight in enumerate(weights, 1):
        nonnegative(margins, f"layer{k}_weight", weight)
        nonnegative(margins, f"layer{k}_rank_cap", rank-k)
    reconstructed = sum((weight/k)*P for k, (weight, P) in enumerate(zip(weights, projections), 1))
    compare(errors, "state_layer_decomposition", reconstructed, S@S)
    instrument = [np.sqrt(max(0., gap))*P@inverse for gap, P in zip(gaps, projections)]
    compare(errors, "layer_instrument_complete", sum(A.conj().T@A for A in instrument), np.eye(rank))
    entropy = float(-np.dot(eigenvalues, np.log2(eigenvalues)))
    layer_entropy = float(np.dot(weights, np.log2(np.arange(1, rank+1))))
    nonnegative(margins, "entropy_dominates_layer_entropy", entropy-layer_entropy)
    nonnegative(margins, "rank_entropy_cap", np.log2(rank)-layer_entropy)
    records = []
    for site in range(n):
        for axis, local in [("X", X), ("Z", Z)]:
            U = np.ones((1, 1), complex)
            for j in range(n):
                U = np.kron(U, local if j == site else I)
            B = V.conj().T@U@V
            label = f"site{site}_{axis}"
            compare(errors, label+"_compressed_Hermitian", B, B.conj().T)
            nonnegative(margins, label+"_compressed_contraction", 1-max(abs(np.linalg.eigvalsh(B))))
            M = S@B@S
            score = norm1_hermitian(M)
            polar_values, polar_vectors = np.linalg.eigh(M)
            signs = np.where(polar_values < -TOL, -1., 1.)
            J = (polar_vectors*signs)@polar_vectors.conj().T
            a = float(np.trace(S@B@S@B).real)
            b = float(np.trace(S@J@S@J).real)
            commutator = float(np.linalg.norm(S@J-J@S)**2)
            delta = a-score*score
            commutator_gap = a*(1-b)
            layer_profiles = [norm1_hermitian(P@B@P)/k for k, P in enumerate(projections, 1)]
            layer_score = float(np.dot(weights, layer_profiles))
            defect = score-layer_score
            layer_operator = sum(gap*P@B@P for gap, P in zip(gaps, projections))
            coefficient_operator = np.minimum.outer(eigenvalues, eigenvalues)*B
            cross = float(np.trace((M-layer_operator)@J).real)
            small_factor = float(np.sum(np.minimum.outer(eigenvalues, eigenvalues)*abs(B)**2))
            layer_affinities = [float(np.trace(P@B@P@B).real)/k for k, P in enumerate(projections, 1)]
            compare(errors, label+"_polar_unitary", J@J, np.eye(rank))
            compare(errors, label+"_polar_attainment", np.trace(M@J), score)
            compare(errors, label+"_ambient_score", score, norm1_hermitian(root@U@root))
            compare(errors, label+"_ambient_affinity", a, np.trace(root@U@root@U))
            compare(errors, label+"_decoder_commutator", b, 1-commutator/2)
            compare(errors, label+"_layer_minimum_coefficient", layer_operator, coefficient_operator)
            compare(errors, label+"_entrywise_remainder", M-layer_operator,
                    np.minimum.outer(s, s)*abs(s[:, None]-s[None, :])*B)
            compare(errors, label+"_layer_affinity_identity", small_factor, np.dot(weights, layer_affinities))
            for k, (A, P, gap) in enumerate(zip(instrument, projections, gaps), 1):
                compare(errors, label+f"_instrument_layer{k}", A@M@A.conj().T, gap*P@B@P)
            nonnegative(margins, label+"_fidelity_affinity_gap", delta)
            nonnegative(margins, label+"_commutator_gap", commutator_gap)
            nonnegative(margins, label+"_gap_dominates_commutator", delta-commutator_gap)
            nonnegative(margins, label+"_layer_concavity", defect)
            nonnegative(margins, label+"_defect_below_cross", cross-defect)
            nonnegative(margins, label+"_entrywise_factor_cap", a-small_factor)
            nonnegative(margins, label+"_cross_Cauchy", np.sqrt(max(0., small_factor*commutator))-abs(cross))
            nonnegative(margins, label+"_refined_layer_affinity_bound", np.sqrt(max(0., 2*small_factor*(1-b)))-defect)
            nonnegative(margins, label+"_sharp_commutator_bound", np.sqrt(max(0., 2*commutator_gap))-defect)
            nonnegative(margins, label+"_gap_bound", np.sqrt(max(0., 2*delta))-defect)
            nonnegative(margins, label+"_squared_gap_bound", 2*delta-defect*defect)
            if kind == "sharp":
                v = 1/1000
                bias = 2*v/(1+v*v)
                t = (1-v*v)/(1+v*v)
                compare(errors, label+"_sharp_score", score, t)
                compare(errors, label+"_sharp_affinity", a, t)
                compare(errors, label+"_sharp_layer_score", layer_score, 1-bias)
                compare(errors, label+"_sharp_refined_equality", defect*defect, 2*small_factor*(1-b))
                compare(errors, label+"_sharp_squared_ratio", defect*defect/(2*delta), 999/1001)
            if kind in ("equality", "zero", "flat"):
                compare(errors, label+"_zero_gap", delta, 0.)
                compare(errors, label+"_zero_layer_defect", defect, 0.)
            records.append(dict(site=site, axis=axis, original=score, affinity=a,
                                decoder_affinity=b, squared_affinity_gap=delta,
                                decoder_commutator_gap=commutator_gap,
                                weighted_layer_affinity=small_factor,
                                flat_layer_scores=layer_profiles, weighted_layer_score=layer_score,
                                layer_defect=defect,
                                zero_extension_dimension=int(np.count_nonzero(abs(polar_values) <= TOL))))
    defects = np.array([row["layer_defect"] for row in records])
    deltas = np.array([row["squared_affinity_gap"] for row in records])
    commutator_gaps = np.array([row["decoder_commutator_gap"] for row in records])
    m = len(records)
    query_weights = np.arange(1, m+1)/m
    original = sum(row["original"] for row in records)
    layer_total = sum(row["weighted_layer_score"] for row in records)
    nonnegative(margins, "aggregate_squared_commutator_bound", 2*sum(commutator_gaps)-np.dot(defects, defects))
    nonnegative(margins, "aggregate_squared_gap_bound", 2*sum(deltas)-np.dot(defects, defects))
    nonnegative(margins, "aggregate_commutator_score_bound", np.sqrt(max(0., 2*m*sum(commutator_gaps)))-sum(defects))
    nonnegative(margins, "aggregate_score_bound", np.sqrt(max(0., 2*m*sum(deltas)))-sum(defects))
    nonnegative(margins, "weighted_termwise_bound", np.dot(query_weights, np.sqrt(np.maximum(0., 2*deltas)))-np.dot(query_weights, defects))
    nonnegative(margins, "weighted_profile_bound", np.sqrt(max(0., 2*sum(query_weights)*np.dot(query_weights, deltas)))-np.dot(query_weights, defects))
    nonnegative(margins, "weighted_Euclidean_profile_bound", np.sqrt(max(0., 2*np.dot(query_weights, query_weights)*sum(deltas)))-np.dot(query_weights, defects))
    flat_totals = np.sum([row["flat_layer_scores"] for row in records], axis=0)
    compare(errors, "common_weighted_profile_sum", layer_total, np.dot(weights, flat_totals))
    nonnegative(margins, "some_flat_layer_near_original", max(flat_totals)+np.sqrt(max(0., 2*m*sum(deltas)))-original)
    if kind == "nonuniform":
        compare(errors, "known_rank_three_score", original, 18*R2/7)
        compare(errors, "known_rank_three_layer_score", layer_total, (16+6*R2)/7)
        nonnegative(margins, "nonuniform_exceeds_all_exact_rank_three_flat_scores", original-(8+2*R2)/3)
    if kind == "singular":
        require(rank == 2, "singular fixture rank")
        require(any(row["zero_extension_dimension"] for row in records), "singular query exercises unitary extension")
    return dict(name=name, ambient_qubits=n, ambient_dimension=len(root), compressed_dimension=rank,
                rank=rank, spectrum=eigenvalues.tolist(), layer_weights=weights.tolist(),
                entropy_bits=entropy, weighted_flat_entropy_bits=layer_entropy,
                original_score=original, weighted_flat_layer_score=layer_total,
                sum_squared_affinity_gaps=float(sum(deltas)), query_weights=query_weights.tolist(),
                query_data=records, relative_identity_residuals=errors, inequality_margins=margins)


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
    records = [fixture_case(*case) for case in fixtures()]
    residuals = [value for row in records for value in row["relative_identity_residuals"].values()]
    margins = [value for row in records for value in row["inequality_margins"].values()]
    report = dict(status="exact finite comparisons and fixed constructions passed", research_base=BASE,
                  python=platform.python_version(), numpy=np.__version__, tolerance=TOL,
                  source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  proof_note_sha256={NOTE: hashlib.sha256(note.read_bytes()).hexdigest()},
                  exact_comparisons=exact, constructions=records, maximum_matrix_dimension=16,
                  exact_comparison_count=len(exact), fixed_construction_count=len(records),
                  query_count=sum(len(row["query_data"]) for row in records),
                  matrix_identity_count=len(residuals), inequality_count=len(margins),
                  maximum_relative_identity_residual=max(residuals), minimum_inequality_margin=min(margins),
                  scope="Exact Fraction identities check one rational sharpness fixture and the prior rank-three example's strict comparison. Seven fixed states of dimension at most 16 check the spectral layer decomposition, one common convex mixture of flat profiles, coordinatewise lower and upper score defects, the optimal-decoder commutator bound, aggregate squared and weighted estimates, entropy, and unchanged rank caps. The almost-flat Y fixture exercises both original X/Z queries and a near-sharp finite ratio. Other fixtures include singular complex support, repeated eigenvalues, zero optimal-query modes, and a prior nonuniform rank-three example. The quantified theorem and sharpness limit are analytical in the proof note. Floating-point checks are not interval certificates. No random sampling, grid, optimization or novelty claim.")
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
