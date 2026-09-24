#!/usr/bin/env python3
"""Bounded complex seesaws for the three-input, dimension-four seed problem.

Finite numerical evidence only: this is not a global upper-bound certificate.
Random initializations sample general complex supports and spectra; they do
not exhaust them. The ten decoder-signature manifolds remain continuous
nonconvex optimization problems after their discrete enumeration.

Run from the repository root (single BLAS threads keep this small):
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
        tools/check_three_input_decoders.py --output results/three_input_decoders.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np

RESEARCH_BASE = "f46ed69785ace49d6f3f52645fefbb9dbdc99f1f"
FREE_SEED = 20260924
SECTOR_SEED = 2026092401
STOP_TOLERANCE = 2e-13
RANK_TOLERANCE = 1e-8
WITNESS_TOLERANCE = 1e-9
BENCHMARK = 4 + math.sqrt(2)
FREE_LIMIT = 600
SECTOR_LIMIT = 1500


def local_paulis() -> list[np.ndarray]:
    identity = np.eye(2)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    result = []
    for site in range(3):
        for query in (x, z):
            product = np.ones((1, 1), dtype=complex)
            for position in range(3):
                product = np.kron(product, query if site == position else identity)
            result.append(product)
    return result


PAULIS = local_paulis()


def compressed_eigensystem(seed: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    compressed = np.array([seed @ p @ seed.conj().T for p in PAULIS])
    compressed = (compressed + compressed.conj().transpose(0, 2, 1)) / 2
    return np.linalg.eigh(compressed)


def decoder_data(seed: np.ndarray, signature: tuple[int, ...] | None = None):
    eigenvalues, eigenvectors = compressed_eigensystem(seed)
    if signature is None:
        # Both choices at zero are extreme trace-norm-optimal contractions.
        signs = np.where(eigenvalues >= 0, 1., -1.)
    else:
        dimension = seed.shape[0]
        signs = np.array([[-1.] * (dimension-k) + [1.] * k for k in signature])
    reflections = np.einsum(
        "bik,bk,bjk->bij", eigenvectors, signs, eigenvectors.conj())
    return float(np.sum(signs * eigenvalues)), reflections


def climb(seed: np.ndarray, signature: tuple[int, ...] | None = None):
    """Alternate optimal reflections of the chosen signature and seed vector."""
    seed = seed / np.linalg.norm(seed)
    limit = FREE_LIMIT if signature is None else SECTOR_LIMIT
    previous = None
    updates = 0
    converged = False
    minimum_step = 0.
    for _ in range(limit):
        score, reflections = decoder_data(seed, signature)
        if previous is not None:
            step = score - previous
            minimum_step = min(minimum_step, step)
            if step < -1e-10:
                raise ArithmeticError(f"Seesaw score decreased by {step}")
            if step < STOP_TOLERANCE:
                converged = True
                break
        previous = score
        bell = sum(np.kron(p.T, b) for p, b in zip(PAULIS, reflections))
        _, vectors = np.linalg.eigh(bell)
        # Input-first/output-second vectorization: Tr(B L P L†).
        seed = vectors[:, -1].reshape(8, seed.shape[0]).T
        updates += 1
    # Always recompute after the final update, including at the iteration cap.
    final_score, _ = decoder_data(seed, signature)
    if previous is not None:
        minimum_step = min(minimum_step, final_score - previous)
        if final_score - previous < -1e-10:
            raise ArithmeticError("Final update decreased the score")
    return seed, {
        "score": final_score,
        "eigenvector_updates": updates,
        "converged_by_step_tolerance": converged,
        "minimum_score_step": minimum_step,
    }


def describe_seed(seed: np.ndarray) -> dict:
    values, _ = compressed_eigensystem(seed)
    spectrum = np.linalg.eigvalsh(seed @ seed.conj().T)
    inertias = [[int(np.sum(v > RANK_TOLERANCE)),
                 int(np.sum(v < -RANK_TOLERANCE)),
                 int(np.sum(np.abs(v) <= RANK_TOLERANCE))] for v in values]
    score = float(np.abs(values).sum())
    return {
        "score": score,
        "score_minus_benchmark": score - BENCHMARK,
        "frobenius_norm_squared": float(np.vdot(seed, seed).real),
        "output_dimension": seed.shape[0],
        "numerical_gram_rank": int(np.sum(spectrum > RANK_TOLERANCE)),
        "gram_eigenvalues_ascending": spectrum.tolist(),
        "compression_inertias_positive_negative_zero": inertias,
        "all_six_compressions_indefinite": all(p > 0 and n > 0 for p, n, _ in inertias),
    }


def iteration_summary(records: list[dict]) -> dict:
    return {
        "runs": len(records),
        "converged": sum(r["converged_by_step_tolerance"] for r in records),
        "hit_iteration_cap": sum(not r["converged_by_step_tolerance"] for r in records),
        "minimum_eigenvector_updates": min(r["eigenvector_updates"] for r in records),
        "maximum_eigenvector_updates": max(r["eigenvector_updates"] for r in records),
        "minimum_score_step": min(r["minimum_score_step"] for r in records),
    }


def controls() -> dict:
    angle = math.pi / 8
    rotation = np.array([[math.cos(angle), -math.sin(angle)],
                         [math.sin(angle), math.cos(angle)]])
    bisector = rotation[:, 0]
    subset = np.kron(np.eye(4)/2, bisector[None, :])
    star = np.zeros((4, 8))
    star[np.arange(4), [0, 1, 2, 4]] = np.sqrt(
        [1-math.sqrt(6)/4] + [math.sqrt(6)/12]*3)
    star = star @ np.kron(np.kron(rotation, rotation), rotation).T
    rank_three = np.zeros((3, 4))
    rank_three[np.arange(3), [0, 1, 2]] = np.sqrt([3/7, 2/7, 2/7])
    rank_three = rank_three @ np.kron(rotation, rotation).T
    rank_three = np.kron(rank_three, bisector[None, :])
    output = {}
    for name, seed, exact, expression in [
        ("subset", subset, BENCHMARK, "4+sqrt(2)"),
        ("nonuniform_bisector_star", star, 3*math.sqrt(3), "3*sqrt(3)"),
        ("rank_three_product", rank_three, 25*math.sqrt(2)/7, "25*sqrt(2)/7"),
    ]:
        data = describe_seed(seed)
        error = abs(data["score"] - exact)
        if error > 1e-12:
            raise ArithmeticError(f"Known control {name} failed: {error}")
        data.update(known_exact_expression=expression, numerical_error=error)
        output[name] = data
    return output


def run() -> dict:
    free_rng = np.random.default_rng(FREE_SEED)
    sector_rng = np.random.default_rng(SECTOR_SEED)
    free_records = []
    free_groups = []
    all_descriptions = []

    def free_group(name: str, seeds: list[np.ndarray]):
        records = []
        descriptions = []
        for seed in seeds:
            seed, record = climb(seed)
            records.append(record)
            descriptions.append(describe_seed(seed))
        free_records.extend(records)
        all_descriptions.extend(descriptions)
        free_groups.append({"name": name, "iterations": iteration_summary(records),
                            "best": max(descriptions, key=lambda d: d["score"])})

    for dimension in (3, 4):
        free_group(f"dense_complex_dimension_{dimension}", [
            free_rng.normal(size=(dimension, 8))
            + 1j*free_rng.normal(size=(dimension, 8)) for _ in range(48)])
    bisector = np.array([math.cos(math.pi/8), math.sin(math.pi/8)])
    subset = np.kron(np.eye(4)/2, bisector[None, :])
    free_group("perturbed_subset", [
        subset + scale*(free_rng.normal(size=(4, 8))
                        + 1j*free_rng.normal(size=(4, 8)))
        for scale in (.03, .1, .3, 1.) for _ in range(8)])

    sector_records = []
    release_records = []
    sector_rows = []
    site_types = [(1, 1), (1, 2), (2, 2)]
    for types in itertools.combinations_with_replacement(range(3), 3):
        signature = sum((site_types[i] for i in types), ())
        fixed_records = []
        releases = []
        before_scores = []
        for _ in range(12):
            seed = sector_rng.normal(size=(4, 8)) + 1j*sector_rng.normal(size=(4, 8))
            seed, fixed = climb(seed, signature)
            fixed_records.append(fixed)
            before_scores.append(describe_seed(seed)["score"])
            seed, released = climb(seed)
            releases.append(released)
            all_descriptions.append(describe_seed(seed))
        sector_records.extend(fixed_records)
        release_records.extend(releases)
        sector_rows.append({
            "positive_eigenspace_ranks": list(signature),
            "best_fixed_sector_score": max(r["score"] for r in fixed_records),
            "largest_actual_trace_norm_before_release": max(before_scores),
            "best_trace_norm_after_unrestricted_release": max(r["score"] for r in releases),
            "fixed_sector_iterations": iteration_summary(fixed_records),
            "release_iterations": iteration_summary(releases),
        })
    best = max(all_descriptions, key=lambda d: d["score"])
    active = [d for d in all_descriptions if d["all_six_compressions_indefinite"]]
    return {
        "status": "finite numerical evidence only; no global upper-bound or novelty certificate",
        "research_base_main_sha": RESEARCH_BASE,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_version": platform.python_version(),
        "numpy_version": np.__version__,
        "objective": "sum_j ||L P_j L^dagger||_1, Frobenius norm(L)=1, six local X/Z queries",
        "query_order": ["X1", "Z1", "X2", "Z2", "X3", "Z3"],
        "benchmark": BENCHMARK,
        "configuration": {
            "free_random_seed": FREE_SEED, "sector_random_seed": SECTOR_SEED,
            "dense_starts_per_output_dimension": 48,
            "subset_perturbation_scales": [.03, .1, .3, 1.], "starts_per_scale": 8,
            "starts_per_signature": 12, "free_iteration_limit": FREE_LIMIT,
            "sector_iteration_limit": SECTOR_LIMIT,
            "score_step_stopping_tolerance": STOP_TOLERANCE,
            "numerical_rank_and_inertia_tolerance": RANK_TOLERANCE,
            "candidate_margin_tolerance": WITNESS_TOLERANCE,
        },
        "known_controls": controls(),
        "free_search": {"iterations": iteration_summary(free_records), "groups": free_groups},
        "signature_search": {
            "fixed_iterations": iteration_summary(sector_records),
            "release_iterations": iteration_summary(release_records), "patterns": sector_rows},
        "total_initializations": len(all_descriptions),
        "unrestricted_best": best,
        "all_six_indefinite_best_found": max(active, key=lambda d: d["score"]),
        "candidates_above_benchmark_plus_tolerance": sum(
            d["score"] > BENCHMARK + WITNESS_TOLERANCE for d in all_descriptions),
        "interpretation": [
            "Values are attained local-search scores, not certified signature-sector maxima.",
            "No found violation does not establish optimality or rule out other basins.",
            "A strict seed witness requires the complete orbit instrument for operational use.",
            "Roundoff and numerical rank classifications may vary across linear algebra libraries.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output),
                      "initializations": result["total_initializations"],
                      "best_score": result["unrestricted_best"]["score"],
                      "candidate_count": result["candidates_above_benchmark_plus_tolerance"],
                      "status": result["status"]}, indent=2))


if __name__ == "__main__":
    main()
