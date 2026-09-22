#!/usr/bin/env python3
"""Small deterministic diagnostics for the entropy converses and seed families.

No optimization is performed. These finite examples check matrix identities
and theorem inequalities; they do not certify unrestricted optimality or
publication novelty. Run from the repository root:

    python tools/check_entropy_bounds.py --output results/entropy_bounds.json
"""
from __future__ import annotations

import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = (X + Z) / math.sqrt(2)
BISECTOR = np.array([math.cos(math.pi / 8), math.sin(math.pi / 8)], complex)
SPECTRAL_ZERO_THRESHOLD = 1e-14
RANDOM_SEED = 20260924


def tensor(items):
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


def pure(vector):
    vector = np.asarray(vector, complex)
    vector = vector / np.linalg.norm(vector)
    return np.outer(vector, vector.conj())


def entropy(probabilities):
    positive = np.asarray(probabilities)[np.asarray(probabilities) > 0]
    return float(-np.dot(positive, np.log2(positive)))


def h2(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def h2_inverse(s):
    if s <= 0:
        return 0.0
    if s >= 1:
        return 0.5
    low, high = 0.0, 0.5
    for _ in range(90):
        middle = (low + high) / 2
        if h2(middle) < s:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def local_pauli(n, site, pauli):
    return tensor(pauli if k == site else I for k in range(n))


def partial_trace_site(matrix, n, site):
    array = matrix.reshape((2,) * (2 * n))
    return np.trace(array, axis1=site, axis2=n + site).reshape(2 ** (n - 1), -1)


def state_from_spectrum(unitary, probabilities):
    p = np.asarray(probabilities, float)
    p /= p.sum()
    return (unitary * p) @ unitary.conj().T, p


def bell_clifford():
    cnot = np.zeros((4, 4), complex)
    for x in range(4):
        cnot[x ^ ((x >> 1) & 1), x] = 1
    return cnot @ np.kron(H, I)


def graph_clifford():
    phases = []
    for x in range(8):
        bits = [(x >> (2 - k)) & 1 for k in range(3)]
        phases.append((-1) ** (bits[0] * bits[1] + bits[1] * bits[2]))
    return np.diag(phases) @ tensor([H, H, H])


def cases():
    rng = np.random.default_rng(RANDOM_SEED)
    result = []

    def add(label, rho, **extra):
        result.append(dict(label=label, rho=rho, **extra))

    add('n1_pure_bisector', pure(BISECTOR), rank_two=True, rank_two_attainer=True)
    add('n1_maximally_mixed', I / 2, rank_two=True, rank_two_attainer=True)
    add('n3_maximally_mixed', np.eye(8) / 8)
    plus, minus = BISECTOR, np.array([-BISECTOR[1], BISECTOR[0]])
    for n in (2, 3):
        for lam in (.1, .3, .5):
            first = lam * pure(plus) + (1 - lam) * pure(minus)
            rho = tensor([first] + [pure(BISECTOR)] * (n - 1))
            add(f'n{n}_rank_two_attainer_{lam}', rho,
                rank_two=True, rank_two_attainer=True)
    for n, lam in ((2, .2), (3, .37)):
        raw = rng.normal(size=(2**n, 2)) + 1j * rng.normal(size=(2**n, 2))
        basis, _ = np.linalg.qr(raw)
        rho = (basis * [lam, 1 - lam]) @ basis.conj().T
        add(f'n{n}_rank_two_complex_isometry', rho, rank_two=True)
    complement_vectors = [
        ('product_bisectors', np.kron(BISECTOR, BISECTOR)),
        ('bell', np.array([1, 0, 0, 1], complex) / math.sqrt(2)),
        ('complex', np.array([1, 2j, -1 + 1j, 3], complex)),
    ]
    for label, vector in complement_vectors:
        projector = pure(vector)
        add(f'n2_flat_rank_three_{label}', (np.eye(4) - projector) / 3,
            rank_three_complement=projector)
    specifications = [
        ('n2_bell_nonflat', bell_clifford(), [1, 2, 3, 4]),
        ('n2_bell_zero_spectrum', bell_clifford(), [7, 0, 3, 0]),
        ('n3_graph_nonflat', graph_clifford(), [1, 2, 3, 4, 5, 6, 7, 8]),
        ('n3_graph_zero_spectrum', graph_clifford(), [2, 0, 1, 0, 0, 3, 0, 4]),
    ]
    for label, unitary, spectrum in specifications:
        rho, probabilities = state_from_spectrum(unitary, spectrum)
        add(label, rho, stabilizer_unitary=unitary, probabilities=probabilities)
    zero = np.array([1, 0], complex)
    one = np.array([0, 1], complex)
    xplus = np.array([1, 1], complex) / math.sqrt(2)
    conditional = np.kron(pure(zero), pure(zero)) + np.kron(pure(xplus), pure(one))
    add('n3_balanced_non_product_diagonal', np.kron(conditional, I) / 4,
        balanced_site=0)
    phi = pure(np.array([1, 0, 0, 1], complex))
    entangled = np.kron(pure(zero), phi) + np.kron(pure(xplus), np.eye(4) - phi)
    add('n3_balanced_entangled_rest', entangled / 4, balanced_site=0)
    for n in (2, 3):
        raw = rng.normal(size=(2**n, 2**n)) + 1j * rng.normal(size=(2**n, 2**n))
        rho = raw @ raw.conj().T
        rho /= np.trace(rho)
        add(f'n{n}_general_complex_full_rank', rho)
    return result


def check_case(case, tolerance):
    rho, label = case['rho'], case['label']
    d = len(rho)
    n = int(round(math.log2(d)))
    eigenvalues, basis = np.linalg.eigh(rho)
    identity_errors = [abs(float(np.trace(rho).real) - 1),
                       float(np.max(np.abs(rho - rho.conj().T)))]
    if min(eigenvalues) < -tolerance:
        raise AssertionError(f'{label}: state is not positive.')
    # Exact-zero spectra acquire tiny signed eigenvalues in floating point.
    eigenvalues = np.where(eigenvalues > SPECTRAL_ZERO_THRESHOLD, eigenvalues, 0)
    w = ((basis * np.sqrt(eigenvalues)) @ basis.conj().T).astype(complex)
    identity_errors.append(float(np.max(np.abs(w @ w - rho))))
    s = entropy(eigenvalues)
    p = h2_inverse(min(1.0, max(0.0, s / n)))
    identity_errors.append(abs(h2(p) - s / n))
    queries = [local_pauli(n, i, pauli) for i in range(n) for pauli in (X, Z)]
    fidelities, affinities = [], []
    for pauli in queries:
        fidelities.append(float(np.abs(np.linalg.eigvalsh(w @ pauli @ w)).sum()))
        affinities.append(float(np.trace(w @ pauli @ w @ pauli).real))
    energy_partial_trace = 0.0
    energy_pauli_twirl = 0.0
    for i in range(n):
        marginal = partial_trace_site(w, n, i)
        energy_partial_trace += float(np.trace(rho).real - .5 * np.trace(marginal @ marginal).real)
        expectation = w.copy()
        for pauli in (X, Y, Z):
            global_pauli = local_pauli(n, i, pauli)
            expectation += global_pauli @ w @ global_pauli
        expectation /= 4
        energy_pauli_twirl += float(np.trace(w @ (w - expectation)).real)
    identity_errors.append(abs(energy_partial_trace - energy_pauli_twirl))
    score = sum(fidelities)
    f = score / (2 * n)
    average_squared_fidelity = sum(value**2 for value in fidelities) / (2 * n)
    average_affinity = sum(affinities) / (2 * n)
    energy_ceiling = 1 - energy_partial_trace / n
    entropy_ceiling = .5 + math.sqrt(max(0.0, p * (1 - p)))
    violations = [max(0.0, left**2 - right) for left, right in zip(fidelities, affinities)]
    chain = [f**2, average_squared_fidelity, average_affinity, energy_ceiling, entropy_ceiling]
    violations += [max(0.0, left - right) for left, right in zip(chain, chain[1:])]
    violations += [max(0.0, -min(affinities)), max(0.0, max(fidelities) - 1)]
    family_checks = {}
    if case.get('rank_two'):
        nonzero = eigenvalues[eigenvalues > 0]
        if len(nonzero) > 2:
            raise AssertionError(f'{label}: rank-two flag has the wrong rank.')
        lam = float(nonzero[0]) if len(nonzero) == 2 else 0.0
        bound = math.sqrt(2) * (n - 1) + math.sqrt(2 + 8 * lam * (1 - lam))
        violations.append(max(0.0, score - bound))
        family_checks['rank_two_fixed_spectrum_bound'] = bound
        family_checks['rank_two_attainer'] = bool(case.get('rank_two_attainer'))
        if case.get('rank_two_attainer'):
            identity_errors.append(abs(score - bound))
    if 'rank_three_complement' in case:
        complement = case['rank_three_complement']
        formula = (8 + sum(abs(float(np.trace(complement @ pauli).real)) for pauli in queries)) / 3
        family_checks['flat_rank_three_exact_score'] = formula
        family_checks['flat_rank_three_bound'] = (8 + 2 * math.sqrt(2)) / 3
        identity_errors.append(abs(score - formula))
        violations.append(max(0.0, score - family_checks['flat_rank_three_bound']))
    if 'stabilizer_unitary' in case:
        unitary, probabilities = case['stabilizer_unitary'], case['probabilities']
        translation_fidelities = []
        for pauli in queries:
            monomial = unitary.conj().T @ pauli @ unitary
            targets = np.argmax(abs(monomial), axis=0)
            identity_errors.append(float(np.max(abs(abs(monomial).sum(axis=0) - 1))))
            translation_fidelities.append(float(np.sqrt(probabilities * probabilities[targets]).sum()))
        identity_errors.append(max(abs(a - b) for a, b in zip(fidelities, translation_fidelities)))
        bound = 2 * n - math.log(2) * (n - s)
        family_checks['stabilizer_entropy_bound'] = bound
        family_checks['translation_fidelities'] = translation_fidelities
        violations.append(max(0.0, score - bound))
    if 'balanced_site' in case:
        site = case['balanced_site']
        rank = 2 ** (n - 1)
        projector = rho * rank
        identity_errors.append(float(np.max(abs(projector @ projector - projector))))
        identity_errors.append(float(np.max(abs(partial_trace_site(projector, n, site) - np.eye(rank)))))
        site_score = sum(fidelities[2 * site:2 * site + 2])
        bound = 2 * (n - 1) + math.sqrt(2)
        family_checks['balanced_site'] = site
        family_checks['balanced_site_score'] = site_score
        family_checks['balanced_rank_half_bound'] = bound
        violations += [max(0.0, site_score - math.sqrt(2)), max(0.0, score - bound)]
    max_identity_error = max(identity_errors)
    max_inequality_violation = max(violations)
    if max_identity_error > tolerance or max_inequality_violation > tolerance:
        raise AssertionError(f'{label}: identity error {max_identity_error}, inequality violation {max_inequality_violation}.')
    return dict(label=label, n=n, rank=int(np.count_nonzero(eigenvalues)),
                entropy=s, score=score, contrast=f, fidelities=fidelities,
                affinities=affinities, depolarizing_energy_partial_trace=energy_partial_trace,
                depolarizing_energy_pauli_twirl=energy_pauli_twirl,
                inverse_entropy_probability=p,
                converse_chain=dict(contrast_squared=f**2,
                                    average_fidelity_squared=average_squared_fidelity,
                                    average_affinity=average_affinity,
                                    one_minus_energy_per_site=energy_ceiling,
                                    entropy_ceiling=entropy_ceiling),
                family_checks=family_checks, max_identity_error=max_identity_error,
                max_inequality_violation=max_inequality_violation)


def rate_table():
    eta0 = 1 / math.sqrt(2)
    rows = []
    for eta in (eta0, .72, .8, .9, .98, 1.0):
        u = max(0.0, 2 * eta**2 - 1)
        probability = (1 - math.sqrt(max(0.0, 1 - u**2))) / 2
        new_bound = h2(probability) if eta > eta0 else 0.0
        old_entropic = max(0.0, 1 - 2 * h2((1 - eta) / 2))
        old_squashed = max(0.0, eta - eta0)**2 / (16 * math.log(2))
        rows.append(dict(contrast=eta, strong_entropic_lower_bound=new_bound,
                         old_entropic_lower_bound=old_entropic,
                         old_squashed_lower_bound=old_squashed,
                         old_combined_lower_bound=max(old_entropic, old_squashed),
                         subset_upper_bound=(eta - eta0) / (1 - eta0)))
    return rows


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Tolerance must be finite and positive.')
    results = [check_case(case, tolerance) for case in cases()]
    return dict(status='PASS', research_base='f9a5fc72d15e9d314f6deae65096605e955a2051',
                python=platform.python_version(), numpy=np.__version__, tolerance=tolerance,
                spectral_zero_threshold=SPECTRAL_ZERO_THRESHOLD, random_seed=RANDOM_SEED,
                case_count=len(results), maximum_matrix_dimension=8,
                max_identity_error=max(case['max_identity_error'] for case in results),
                max_inequality_violation=max(case['max_inequality_violation'] for case in results),
                cases=results, analytical_rate_table=rate_table(),
                scope='Finite matrix diagnostics and arithmetic values of proved bounds. No optimization, unrestricted subset-optimality certificate, or novelty certification.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--tolerance', type=float, default=1e-10)
    args = parser.parse_args()
    report = run(args.tolerance)
    text = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
