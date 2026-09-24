#!/usr/bin/env python3
"""Small construction checks for the one-active-Jordan-block converse.

This is a deterministic, non-optimizing diagnostic. It verifies the sampled
local spectral majorants, maximally entangled top eigenvectors, projector
overlaps, and weighted global bounds. It does not prove a universal bound
or establish publication novelty.

    python tools/check_jordan_block_converse.py --output results/jordan_block_converse.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import numpy as np

BASE = "012bafa1895a66e22eac676ba1702a2bde531881"
RANDOM_SEED = 2026092405
TOLERANCE = 1e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
WEIGHTS = {
    "uniform": np.ones(6),
    "unequal": np.array([.2, .5, 1., 1.3, .7, 1.8]),
    "with_zero": np.array([0., 1.1, .8, .3, 0., 0.]),
}


def tensor(items):
    result = np.ones((1, 1), dtype=complex)
    for item in items:
        result = np.kron(result, item)
    return result


QUERIES = [tensor(p if position == site else I for position in range(3))
           for site in range(3) for p in (X, Z)]


def require(value, description):
    if value > TOLERANCE:
        raise AssertionError(f"{description}: residual {value}")


def opnorm(matrix):
    return float(np.linalg.norm(matrix, 2))


def dense_reflection(rng, dimension, negative_rank):
    gaussian = rng.normal(size=(dimension, dimension))
    gaussian = gaussian + 1j*rng.normal(size=(dimension, dimension))
    unitary, triangular = np.linalg.qr(gaussian)
    phases = np.diag(triangular)
    unitary = unitary @ np.diag(phases/np.abs(phases))
    signs = np.ones(dimension)
    signs[:negative_rank] = -1
    reflection = (unitary*signs) @ unitary.conj().T
    # Independent sign choices leave the Jordan-block count unchanged.
    return (-1 if rng.integers(2) else 1)*reflection


def insertion(phi, site, dimension):
    """Insert a reference-memory vector, preserving the other two references."""
    result = np.zeros((8*dimension, 4), dtype=complex)
    others = [j for j in range(3) if j != site]
    coefficients = phi.reshape(2, dimension)
    for column in range(4):
        bits = [0, 0, 0]
        bits[others[0]], bits[others[1]] = column//2, column % 2
        for local in range(2):
            bits[site] = local
            reference = 4*bits[0]+2*bits[1]+bits[2]
            result[reference*dimension:(reference+1)*dimension, column] = coefficients[local]
    return result


def bounds(weights):
    pairs = weights.reshape(3, 2)
    radii = np.linalg.norm(pairs, axis=1)
    deltas = np.sum(pairs, axis=1)-radii
    gram = (np.diag(deltas)+np.outer(np.sqrt(deltas), np.sqrt(deltas)))/2
    return radii, deltas, {
        "gram_bound": float(np.sum(radii)+np.linalg.eigvalsh(gram)[-1]),
        "coarse_gram_bound": float(np.sum(radii)+(np.sum(deltas)+max(deltas))/2),
        "two_largest_deltas_bound": float(np.sum(radii)+sum(sorted(deltas)[-2:])),
    }


def check_family(name, readouts):
    dimension = readouts[0].shape[0]
    identity = np.eye(dimension)
    reflection_error = max(max(opnorm(b-b.conj().T), opnorm(b@b-identity))
                           for b in readouts)
    require(reflection_error, name+" reflection identity")
    negative_ranks = [int(np.sum(np.linalg.eigvalsh(b) < 0)) for b in readouts]
    rows = {}
    for weight_name, weights in WEIGHTS.items():
        radii, deltas, upper = bounds(weights)
        insertions = []
        marginal_errors = []
        local_violations = []
        excess_ranks = []
        for site in range(3):
            h = weights[2*site]*np.kron(X, readouts[2*site])
            h += weights[2*site+1]*np.kron(Z, readouts[2*site+1])
            eigenvalues, eigenvectors = np.linalg.eigh(h)
            excess_rank = int(np.sum(eigenvalues > radii[site]+TOLERANCE))
            if excess_rank > 1:
                raise AssertionError(name+" has more than one positive excess direction")
            excess_ranks.append(excess_rank)
            if excess_rank:
                phi = eigenvectors[:, -1]
                coefficient = phi.reshape(2, dimension)
                marginal_error = opnorm(coefficient@coefficient.conj().T-I/2)
                require(marginal_error, name+" maximally entangled local top vector")
                marginal_errors.append(marginal_error)
                p = np.outer(phi, phi.conj())
                insertions.append(insertion(phi, site, dimension))
            else:
                p = np.zeros_like(h)
                insertions.append(np.zeros((8*dimension, 4), dtype=complex))
            cap = radii[site]*np.eye(2*dimension)+deltas[site]*p-h
            violation = -float(np.linalg.eigvalsh(cap)[0])
            require(violation, name+" local spectral majorant")
            local_violations.append(violation)
        overlaps = [opnorm(insertions[i].conj().T@insertions[j])
                    for i in range(3) for j in range(i+1, 3)]
        require(max(overlaps)-.5, name+" rank-one projector overlap")
        hamiltonian = sum(w*np.kron(u, b)
                          for w, u, b in zip(weights, QUERIES, readouts))
        norm = float(max(abs(np.linalg.eigvalsh(hamiltonian))))
        for bound_name, upper_bound in upper.items():
            require(norm-upper_bound, name+" "+bound_name)
        projectors = [e@e.conj().T for e in insertions]
        weighted_projector_sum = sum(d*p for d, p in zip(deltas, projectors))
        projector_norm = float(np.linalg.eigvalsh(weighted_projector_sum)[-1])
        require(projector_norm-(upper["gram_bound"]-sum(radii)), name+" weighted Gram estimate")
        rows[weight_name] = {
            "operator_norm": norm,
            "norm_minus_gram_bound": norm-upper["gram_bound"],
            "local_excess_ranks": excess_ranks,
            "max_local_majorant_violation": max(local_violations),
            "max_top_marginal_error": max(marginal_errors, default=0.),
            "max_projector_overlap": max(overlaps),
            "weighted_projector_norm": projector_norm,
        }
    return {"name": name, "memory_dimension": dimension,
            "negative_ranks": negative_ranks,
            "reflection_error": reflection_error, "weights": rows}


def mixed_projector_negative_control():
    dimension = 4
    first = np.zeros((32, 32), dtype=complex)
    for memory_b in range(2):
        phi = np.zeros(8, dtype=complex)
        for memory_a in range(2):
            phi[4*memory_a+2*memory_a+memory_b] = 1/math.sqrt(2)
        e = insertion(phi, 0, dimension)
        first += e@e.conj().T
    phi = np.zeros(8, dtype=complex)
    phi[0] = phi[5] = 1/math.sqrt(2)  # A=0, reference entangled with B.
    e2, e3 = insertion(phi, 1, dimension), insertion(phi, 2, dimension)
    total = first+e2@e2.conj().T+e3@e3.conj().T
    norm = float(np.linalg.eigvalsh(total)[-1])
    exact = (5+math.sqrt(13))/4
    require(abs(norm-exact), "Mixed-rank projector counterexample value")
    if norm <= 2:
        raise AssertionError("Expected mixed-projector relaxation violation absent")
    p0 = np.diag([1., 0.])
    p1 = I-p0
    conditional_x = np.kron(p0, X)+np.kron(p1, I)
    conditional_z = np.kron(p0, Z)+np.kron(p1, I)
    readouts = [np.kron(X, I), np.kron(Z, I), conditional_x,
                conditional_z, conditional_x, conditional_z]
    hamiltonian = sum(np.kron(u, b) for u, b in zip(QUERIES, readouts))
    actual = float(max(abs(np.linalg.eigvalsh(hamiltonian))))
    actual_upper = 2+2*math.sqrt(2)
    require(actual-actual_upper, "Actual mixed construction analytical bound")
    return {
        "projector_sum_norm": norm, "exact_projector_sum_norm": exact,
        "projector_sum_norm_minus_two": norm-2,
        "actual_hamiltonian_norm": actual,
        "actual_hamiltonian_analytic_upper_bound": actual_upper,
        "explanation": "Only the mixed-rank projector shortcut fails. Conditional on Q1, the last two sites obey either the two-active-site qubit bound or the scalar bound 2 sqrt(2); adding the first site gives 2+2 sqrt(2).",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results/jordan_block_converse.json"))
    args = parser.parse_args()
    rng = np.random.default_rng(RANDOM_SEED)
    families = []
    for sample in range(8):
        readouts = [dense_reflection(rng, 3, 1) for _ in range(6)]
        families.append(check_family(f"qutrit_dense_{sample}", readouts))
    for scalar_count in (1, 2, 4, 6):
        readouts = [dense_reflection(rng, 3, 0 if j < scalar_count else 1)
                    for j in range(6)]
        families.append(check_family(f"qutrit_{scalar_count}_scalar_readouts", readouts))
    # Up to site permutations, these are all four three-site patterns whose
    # local pairs never have signature (2,2): k pairs (1,2), 3-k pairs (1,1).
    for mixed_pairs in range(4):
        for sample in range(4):
            readouts = []
            for site in range(3):
                readouts.extend([dense_reflection(rng, 4, 1),
                                 dense_reflection(rng, 4, 2 if site < mixed_pairs else 1)])
            families.append(check_family(f"ququart_{mixed_pairs}_mixed_pairs_{sample}", readouts))
    report = {
        "status": "PASS", "research_base": BASE,
        "scope": "Finite construction diagnostics, not an optimizer, universal proof, or novelty certificate.",
        "random_seed": RANDOM_SEED, "tolerance": TOLERANCE,
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "family_count": len(families), "weighted_case_count": len(families)*len(WEIGHTS),
        "maximum_hamiltonian_dimension": 32,
        "weight_data": {name: {"weights": weights.tolist(), **bounds(weights)[2]}
                        for name, weights in WEIGHTS.items()},
        "families": families,
        "mixed_projector_negative_control": mixed_projector_negative_control(),
    }
    rows = [entry for family in families for entry in family["weights"].values()]
    report["maximum_top_marginal_error"] = max(row["max_top_marginal_error"] for row in rows)
    report["maximum_local_majorant_violation"] = max(row["max_local_majorant_violation"] for row in rows)
    report["maximum_projector_overlap"] = max(row["max_projector_overlap"] for row in rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "families": report["family_count"],
                      "weighted_cases": report["weighted_case_count"],
                      "output": str(args.output), "source_sha256": report["source_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
