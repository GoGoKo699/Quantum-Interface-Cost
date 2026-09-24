#!/usr/bin/env python3
"""Finite construction checks for common antiunitary-odd ququart readouts.

These tests verify the stated examples and sampled operator inequalities.
They are not an optimization, a global-bound certificate, or a novelty audit.

    python tools/check_antiunitary_readouts.py --output results/antiunitary_readouts.json
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

BASE = "0730608b9daa9ba09a27843d57b47134a5852fd4"
RANDOM_SEED = 2026092404
TOLERANCE = 1e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
I4 = np.eye(4, dtype=complex)


def tensor(items):
    result = np.ones((1, 1), dtype=complex)
    for item in items:
        result = np.kron(result, item)
    return result


QUERIES = [tensor(p if position == site else I for position in range(3))
           for site in range(3) for p in (X, Z)]
LEFT = np.array([tensor((X, Y)), tensor((Y, I)), tensor((Z, Y))])
RIGHT = np.array([tensor((Y, X)), tensor((I, Y)), tensor((Y, Z))])
WEIGHTS = {
    "uniform": np.ones(6),
    "unequal": np.array([.2, .5, 1., 1.3, .7, 1.8]),
    "signed": np.array([-.2, .5, -1., 1.3, -.7, 1.8]),
}


def max_entry(matrix):
    return float(np.max(np.abs(matrix)))


def require_small(value, description):
    if value > TOLERANCE:
        raise AssertionError(f"{description}: residual {value}")


def readout_checks(readouts, antiunitary_matrix):
    """Theta=M K; conjugation is M B* M†, and Theta²=M M*."""
    values = {
        "unitarity": max_entry(antiunitary_matrix @ antiunitary_matrix.conj().T - I4),
        "hermiticity": max(max_entry(b-b.conj().T) for b in readouts),
        "reflection": max(max_entry(b@b-I4) for b in readouts),
        "trace_zero": max(float(abs(np.trace(b))) for b in readouts),
        "oddness": max(max_entry(antiunitary_matrix @ b.conj()
                                @ antiunitary_matrix.conj().T+b) for b in readouts),
    }
    for name, error in values.items():
        require_small(error, name)
    return values


def operator_checks(readouts):
    result = {}
    for name, weights in WEIGHTS.items():
        # The six input Pauli matrices are real, so either vectorization
        # convention gives the same displayed operator spectrum here.
        hamiltonian = sum(w*np.kron(u, b)
                          for w, u, b in zip(weights, QUERIES, readouts))
        eigenvalues = np.linalg.eigvalsh(hamiltonian)
        norm = float(np.max(np.abs(eigenvalues)))
        upper = 2*float(np.linalg.norm(weights))
        if norm-upper > TOLERANCE:
            raise AssertionError(f"Weighted norm exceeded proposed bound: {name}")
        result[name] = {"norm": norm, "upper_bound": upper,
                        "norm_minus_bound": norm-upper}
    return result


def real_structure_sweep(rng):
    algebra_errors = []
    for sphere in (LEFT, RIGHT):
        for index, op in enumerate(sphere):
            algebra_errors.extend([max_entry(op@op-I4), max_entry(op+op.conj())])
            algebra_errors.append(max_entry(
                sphere[index]@sphere[(index+1) % 3]-1j*sphere[(index+2) % 3]))
    algebra_errors.extend(max_entry(a@b-b@a) for a in LEFT for b in RIGHT)
    algebra_error = max(algebra_errors)
    require_small(algebra_error, "Two commuting imaginary Pauli triples")
    rows = []
    errors = []
    for assignment in itertools.product((0, 1), repeat=6):
        directions = rng.normal(size=(6, 3))
        directions /= np.linalg.norm(directions, axis=1)[:, None]
        readouts = np.array([sum(c*p for c, p in zip(v, (LEFT, RIGHT)[side]))
                             for side, v in zip(assignment, directions)])
        checks = readout_checks(readouts, I4)
        errors.extend(checks.values())
        rows.append({"assignment_left_0_right_1": list(assignment),
                     "operator_checks": operator_checks(readouts)})
    return {"class": "Theta=K, square +I", "assignments": 64,
            "weights_per_assignment": 3, "operator_eigensystems": 192,
            "algebra_max_error": algebra_error,
            "readout_max_error": max(errors), "rows": rows}


def positive_square_attainer():
    # Build the common tensor-factor identification from commuting Z operators.
    projector = (I4+LEFT[2])@(I4+RIGHT[2])/4
    vector = projector[:, int(np.argmax(np.real(np.diag(projector))))]
    vector /= np.linalg.norm(vector)
    basis = np.column_stack((vector, RIGHT[0]@vector, LEFT[0]@vector,
                             LEFT[0]@RIGHT[0]@vector))
    errors = [max_entry(basis.conj().T@basis-I4)]
    for op, pauli in zip(LEFT, (X, Y, Z)):
        errors.append(max_entry(basis.conj().T@op@basis-np.kron(pauli, I)))
    for op, pauli in zip(RIGHT, (X, Y, Z)):
        errors.append(max_entry(basis.conj().T@op@basis-np.kron(I, pauli)))
    require_small(max(errors), "Logical factor identification")
    bisector = np.array([math.cos(math.pi/8), math.sin(math.pi/8)])
    seed = np.zeros((4, 8), dtype=complex)
    for q1, r1, r2, r3 in itertools.product((0, 1), repeat=4):
        if q1 == r1:
            seed[2*q1, 4*r1+2*r2+r3] = bisector[r2]*bisector[r3]/math.sqrt(2)
    seed = basis@seed
    readouts = [LEFT[0], LEFT[2], RIGHT[2], RIGHT[2], RIGHT[2], RIGHT[2]]
    checks = readout_checks(readouts, I4)
    scores = np.array([float(np.trace(b@seed@u@seed.conj().T).real)
                       for u, b in zip(QUERIES, readouts)])
    expected = np.array([1., 1.]+[1/math.sqrt(2)]*4)
    require_small(max_entry(scores-expected), "Square-positive equality profile")
    require_small(abs(float(scores@scores)-4), "Quadratic equality")
    require_small(abs(float(np.vdot(seed, seed).real)-1), "Seed normalization")
    return {"factor_identification_max_error": max(errors),
            "readout_checks": checks, "profile": scores.tolist(),
            "squared_sum": float(scores@scores), "linear_sum": float(scores.sum()),
            "exact_squared_sum": "4", "exact_linear_sum": "2+2sqrt(2)"}


def negative_square_attainer():
    # Flat cyclic support, independently constructed rather than importing a
    # previous diagnostic's data or eigenbasis.
    cyclic = (tensor((X, Z, I))+tensor((I, X, Z))+tensor((Z, I, X)))/math.sqrt(3)
    eigenvalues, vectors = np.linalg.eigh(cyclic)
    basis = vectors[:, eigenvalues > 0]
    spin = tensor((Y, Y, Y))
    antiunitary_matrix = basis.conj().T@spin@basis.conj()
    readouts = [basis.conj().T@u@basis/math.sqrt(2/3) for u in QUERIES]
    checks = readout_checks(readouts, antiunitary_matrix)
    square_error = max_entry(antiunitary_matrix@antiunitary_matrix.conj()+I4)
    require_small(square_error, "Kramers square -I")
    operators = operator_checks(readouts)
    require_small(abs(operators["uniform"]["norm"]-2*math.sqrt(6)),
                  "Kramers uniform equality")
    return {"class": "Theta²=-I, flat cyclic support", "readout_checks": checks,
            "square_error": square_error, "operator_checks": operators,
            "exact_uniform_norm": "2sqrt(6)"}


def nonscalar_square_example():
    phase = math.pi/3
    zero = np.zeros((2, 2), dtype=complex)
    antiunitary_matrix = np.block([[zero, np.exp(1j*phase)*I], [I, zero]])
    readouts = [np.block([[a, zero], [zero, -a.conj()]])
                for a in (X, Z, I, I, I, I)]
    checks = readout_checks(readouts, antiunitary_matrix)
    square = antiunitary_matrix@antiunitary_matrix.conj()
    expected_square = np.diag([np.exp(1j*phase)]*2+[np.exp(-1j*phase)]*2)
    require_small(max_entry(square-expected_square), "Nonscalar square formula")
    distance_from_scalar = float(np.linalg.norm(square-np.trace(square)*I4/4))
    if distance_from_scalar < .1:
        raise AssertionError("The intended nonscalar square became scalar")
    operators = operator_checks(readouts)
    analytic_errors = []
    for name, weights in WEIGHTS.items():
        exact = abs(weights[0])+abs(weights[1])+np.linalg.norm(weights[2:4])+np.linalg.norm(weights[4:6])
        analytic_errors.append(abs(operators[name]["norm"]-float(exact)))
    require_small(max(analytic_errors), "Paired-sector exact norm")
    return {"class": "nonreal conjugate eigenspaces of Theta²", "phase": phase,
            "readout_checks": checks, "square_formula_error": max_entry(square-expected_square),
            "square_distance_from_scalar_frobenius": distance_from_scalar,
            "operator_checks": operators, "analytic_norm_max_error": max(analytic_errors),
            "exact_uniform_norm": "2+2sqrt(2)"}


def missing_symmetry_control():
    # M B* + B M=0 is complex-linear in M. Column-major vectorization gives
    # (B*.T tensor I + I tensor B) vec(M)=0.
    readouts = [tensor(pair) for pair in ((X, I), (Z, I), (Y, I),
                                         (I, X), (I, Z), (X, X))]
    equations = np.vstack([np.kron(b.conj().T, I4)+np.kron(I4, b) for b in readouts])
    singular_values = np.linalg.svd(equations, compute_uv=False)
    rank = int(np.count_nonzero(singular_values > TOLERANCE))
    if rank != 16:
        raise AssertionError("Negative control unexpectedly has an intertwiner")
    return {"description": "Balanced sextuple with no common odd antiunitary",
            "readouts": ["XI", "ZI", "YI", "IX", "IZ", "XX"],
            "linear_system_shape": list(equations.shape), "complex_rank": rank,
            "smallest_singular_value": float(singular_values[-1]),
            "exact_reason": "Oddness for real XI and IX makes M commute with their product XX; oddness for XX also makes M anticommute with it. Since XX is invertible, M=0.",
            "scope": "Excludes common symmetry only; no bound violation is claimed."}


def run():
    rng = np.random.default_rng(RANDOM_SEED)
    return {
        "status": "PASS; finite construction checks, not a global proof or optimization",
        "base_commit": BASE,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(), "numpy": np.__version__,
        "rng_seed": RANDOM_SEED, "tolerance": TOLERANCE,
        "max_operator_dimension": 32,
        "weights": {name: weights.tolist() for name, weights in WEIGHTS.items()},
        "positive_square_sweep": real_structure_sweep(rng),
        "positive_square_attainer": positive_square_attainer(),
        "negative_square_attainer": negative_square_attainer(),
        "nonscalar_square_example": nonscalar_square_example(),
        "missing_symmetry_control": missing_symmetry_control(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("results/antiunitary_readouts.json"))
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": report["status"], "output": str(args.output),
                      "assignment_count": 64, "weighted_operator_checks": 198,
                      "negative_square_uniform_norm": report["negative_square_attainer"]["operator_checks"]["uniform"]["norm"]}, indent=2))


if __name__ == "__main__":
    main()
