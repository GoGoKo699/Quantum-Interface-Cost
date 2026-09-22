#!/usr/bin/env python3
"""Finite diagnostics for small flat seeds and entropy-family exclusions.

The twenty deterministic examples have dimension at most sixteen. No optimizer
is used, and passing examples do not prove the theorems or establish novelty.

    python tools/check_entropy_structure.py --output results/entropy_structure.json
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
from pathlib import Path

import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
B = (X + Z) / math.sqrt(2)
PAULIS = (I, X, Y, Z)
RANDOM_SEED = 20260925
ZERO_THRESHOLD = 1e-14
BASE = '87b6432cdd1f29bc4981f24bd6732bb933741193'


def tensor(items):
    out = np.ones((1, 1), complex)
    for item in items:
        out = np.kron(out, item)
    return out


def local(n, site, operator):
    return tensor(operator if k == site else I for k in range(n))


def pure(vector):
    vector = np.asarray(vector, complex)
    vector /= np.linalg.norm(vector)
    return np.outer(vector, vector.conj())


def root_and_entropy(rho):
    values, vectors = np.linalg.eigh(rho)
    if min(values) < -1e-10:
        raise AssertionError('Nonpositive state.')
    values = np.where(values > ZERO_THRESHOLD, values, 0)
    positive = values[values > 0]
    return ((vectors * np.sqrt(values)) @ vectors.conj().T,
            float(-sum(positive * np.log2(positive))), int(len(positive)))


def trace_norm_hermitian(matrix):
    return float(sum(abs(np.linalg.eigvalsh(matrix))))


def norm(matrix):
    return float(np.max(abs(matrix)))


def scores(rho):
    root, entropy, rank = root_and_entropy(rho)
    n = int(round(math.log2(len(rho))))
    values = [trace_norm_hermitian(root @ local(n, i, p) @ root)
              for i in range(n) for p in (X, Z)]
    return values, entropy, rank, norm(root @ root - rho)


def unitary_from_hermitian(matrix, angle):
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.exp(1j * angle * values)) @ vectors.conj().T


def binary_entropy(p):
    return -sum(q * math.log2(q) for q in (p, 1-p) if q > 0)


def leaf(rho):
    return dict(rho=rho)


def flagged(probability, flag_basis, zero, one):
    projectors = [pure(flag_basis[:, b]) for b in (0, 1)]
    rho = sum(weight * np.kron(projector, child['rho'])
              for weight, projector, child in
              zip((probability, 1-probability), projectors, (zero, one)))
    return dict(rho=rho, probability=probability, projectors=projectors,
                children=(zero, one))


def examples():
    rng = np.random.default_rng(RANDOM_SEED)
    result = []
    base = tensor([B, I, I])

    def add_flat(label, reflection, attainer=False):
        d = len(reflection)
        result.append(dict(label=label, family='flat_half_rank',
                           rho=(np.eye(d) + reflection) / d,
                           reflection=reflection, attainer=attainer))

    add_flat('flat_bisector_site_zero', base, True)
    add_flat('flat_negative_bisector_site_two', -tensor([I, I, B]), True)
    for label, angle in (('flat_near_attainer', .02),
                         ('flat_controlled_rotation', .63)):
        unitary = unitary_from_hermitian(tensor([Z, X, I]), angle)
        add_flat(label, unitary @ base @ unitary.conj().T)
    majority = sum(local(3, i, X) for i in range(3))
    values, vectors = np.linalg.eigh(majority)
    add_flat('flat_majority_singleton_threshold',
             (vectors * np.sign(values)) @ vectors.conj().T)
    for index in range(2):
        raw = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
        unitary, _ = np.linalg.qr(raw)
        add_flat(f'flat_complex_reflection_{index}',
                 unitary @ np.diag([1]*4 + [-1]*4) @ unitary.conj().T)
    rank_three_projector = unitary[:, :3]@unitary[:, :3].conj().T
    result.append(dict(label='flat_three_qubit_rank_three',
                       family='flat_general_rank', rho=rank_three_projector/3))
    add_flat('flat_four_qubit_bisector_attainer', tensor([I, B, I, I]), True)
    raw = rng.normal(size=(16, 16))+1j*rng.normal(size=(16, 16))
    unitary, _ = np.linalg.qr(raw)
    add_flat('flat_four_qubit_complex_reflection',
             unitary@np.diag([1]*8+[-1]*8)@unitary.conj().T)
    rank_seven_projector = unitary[:, :7]@unitary[:, :7].conj().T
    result.append(dict(label='flat_four_qubit_rank_seven',
                       family='flat_general_rank', rho=rank_seven_projector/7))

    basis_a = unitary_from_hermitian(Y, .31)
    basis_b = unitary_from_hermitian(X+Z, .43)
    sigma = [(I+.7*Z)/2, (I+.5*X+.3*Y)/2]
    rank_three = flagged(.38, basis_b, leaf(pure([1, 0])), leaf(sigma[1]))
    full_rank = flagged(.61, basis_a, leaf(sigma[0]), leaf(sigma[1]))
    first = flagged(.32, basis_a, leaf((I+.6*X)/2), leaf((I+.4*Z)/2))
    second = flagged(.71, basis_b, leaf((I+.5*Y)/2), leaf((I+.3*B)/2))
    recursive = flagged(.44, basis_b, first, second)
    bisector = (I+B)/2
    equality = flagged(.5, basis_a, leaf(bisector), leaf(bisector))
    for label, tree in (('flag_noncommuting_rank_three', rank_three),
                        ('flag_noncommuting_full_rank', full_rank),
                        ('flag_recursive_conditional_bases', recursive),
                        ('flag_entropy_line_attainer', equality)):
        result.append(dict(label=label, family='classical_flag',
                           rho=tree['rho'], tree=tree,
                           attainer=label.endswith('attainer')))
    p = .9
    counter = flagged(.5, I, leaf(pure([math.sqrt(p), math.sqrt(1-p)])),
                      leaf(pure([math.sqrt(p), -math.sqrt(1-p)])))
    result.append(dict(label='failed_local_conditional_bound',
                       family='conditional_counterexample',
                       rho=counter['rho']))
    threshold_alpha = 2*(2-math.sqrt(2))/math.log(2)
    t = threshold_alpha-1
    kappa_threshold = ((1+math.sqrt(1-t*t))/t)**2
    raw = rng.normal(size=(4, 4))+1j*rng.normal(size=(4, 4))
    unitary, _ = np.linalg.qr(raw)
    for label, factor in (('below', 1-1e-6), ('above', 1+1e-6)):
        kappa = kappa_threshold*factor
        spectrum = np.array([1, 1.7, 2.9, kappa])
        spectrum /= sum(spectrum)
        result.append(dict(label=f'spectral_condition_{label}_threshold',
                           family='spectral_condition',
                           rho=(unitary*spectrum)@unitary.conj().T,
                           target_kappa=kappa, kappa_threshold=kappa_threshold))
    bell_basis = np.array([[1, 1, 0, 0], [0, 0, 1, 1],
                           [0, 0, 1, -1], [1, -1, 0, 0]], complex)/math.sqrt(2)
    rotations = (unitary_from_hermitian(X+.5*Y+.7*Z, .37),
                 unitary_from_hermitian(.2*X+Y-.4*Z, .29))
    product_rotation = np.kron(*rotations)
    for label, probabilities in (('rank_three', [.51, .31, .18, 0]),
                                 ('full_rank', [.46, .28, .17, .09])):
        probabilities = np.array(probabilities)
        bell = (bell_basis*probabilities)@bell_basis.conj().T
        result.append(dict(label=f'locally_mixed_rotated_bell_{label}',
                           family='locally_mixed',
                           rho=product_rotation@bell@product_rotation.conj().T,
                           bell_rho=bell, bell_basis=bell_basis,
                           probabilities=probabilities, local_rotations=rotations))
    return result


def check_flag(tree, identities, violations):
    values, entropy, _, reconstruction = scores(tree['rho'])
    identities.append(reconstruction)
    n = len(values)//2
    coefficient = 2-math.sqrt(2)
    if 'children' not in tree:
        if n != 1:
            raise AssertionError('This diagnostic uses only one-qubit leaves.')
        violations.append(sum(values) - math.sqrt(2) - coefficient*entropy)
        return dict(n=1, entropy=entropy, score=sum(values))
    p = tree['probability']
    weights = (p, 1-p)
    children = tree['children']
    child_reports = [check_flag(child, identities, violations) for child in children]
    marginal = sum(weight*projector for weight, projector
                   in zip(weights, tree['projectors']))
    marginal_values, _, _, reconstruction = scores(marginal)
    identities.append(reconstruction)
    for actual, upper in zip(values[:2], marginal_values):
        violations.append(actual-upper)
    for k, value in enumerate(values[2:]):
        conditional = sum(weight*scores(child['rho'])[0][k]
                          for weight, child in zip(weights, children))
        identities.append(abs(value-conditional))
    conditional_entropy = sum(weight*report['entropy']
                              for weight, report in zip(weights, child_reports))
    identities.append(abs(entropy-binary_entropy(p)-conditional_entropy))
    flag_envelope = math.sqrt(2+8*p*(1-p))
    violations.extend((sum(marginal_values)-flag_envelope,
                       flag_envelope-math.sqrt(2)-coefficient*binary_entropy(p),
                       sum(values)-math.sqrt(2)*n-coefficient*entropy))
    if p in (0, 1):
        commutator = 0.0
    else:
        commutator = norm(children[0]['rho']@children[1]['rho']
                          - children[1]['rho']@children[0]['rho'])
    return dict(n=n, entropy=entropy, score=sum(values),
                flag_probability=p, flag_score=sum(values[:2]),
                marginal_flag_score=sum(marginal_values),
                flag_spectral_envelope=flag_envelope,
                conditional_states_commutator_norm=commutator,
                conditional_entropy=conditional_entropy, children=child_reports)


def check_flat(case, values, identities, violations):
    reflection = case['reflection']
    d = len(reflection)
    n = int(round(math.log2(d)))
    identities += [norm(reflection@reflection-np.eye(d)),
                   abs(float(np.trace(reflection).real)),
                   norm(reflection-reflection.conj().T)]
    coefficients = {}
    for word in itertools.product(range(4), repeat=n):
        pauli = tensor(PAULIS[k] for k in word)
        coefficients[word] = float(np.trace(reflection@pauli).real/d)
    identities.append(abs(sum(c*c for c in coefficients.values())-1))
    singleton = np.zeros((d, d), complex)
    beta = []
    for i in range(n):
        length_squared = 0.0
        for a in (1, 3):
            word = tuple(a if j == i else 0 for j in range(n))
            c = coefficients[word]
            singleton += c*local(n, i, PAULIS[a])
            length_squared += c*c
        beta.append(math.sqrt(length_squared))
    total = sum(b*b for b in beta)
    expected_absolute = sum(abs(sum(sign*b for sign, b in zip(signs, beta)))
                            for signs in itertools.product((-1, 1), repeat=n))/d
    spectral_absolute = trace_norm_hermitian(singleton)/d
    ordered = sorted(beta, reverse=True)
    if n == 3:
        closed_expression = max(ordered[0], sum(ordered)/2)
    elif n == 4:
        a, b, c, e = ordered
        closed_expression = max(a, (3*a+b+c+e)/4, (a+b+c)/2)
    else:
        raise AssertionError('The singleton norm diagnostic covers n=3,4.')
    identities.extend((abs(expected_absolute-spectral_absolute),
                       abs(expected_absolute-closed_expression),
                       abs(float(np.trace(reflection@singleton).real/d)-total)))
    violations.append(total-expected_absolute)
    weights = []
    projector = (np.eye(d)+reflection)/2
    for i in range(n):
        for a in (1, 3):
            pauli = local(n, i, PAULIS[a])
            anticommute_weight = sum(c*c for word, c in coefficients.items()
                                    if word[i] not in (0, a))
            weights.append(anticommute_weight)
            fidelity = values[2*i+(a == 3)]
            compression = trace_norm_hermitian(projector@pauli@projector)/(d/2)
            anticommutator = trace_norm_hermitian(reflection@pauli+pauli@reflection)/(2*d)
            identities.extend((abs(fidelity-compression),
                               abs(fidelity-anticommutator)))
            violations.append(fidelity-math.sqrt(max(0, 1-anticommute_weight)))
    deficits = [sum(weights[2*i:2*i+2]) for i in range(n)]
    violations += [b*b-deficit for b, deficit in zip(beta, deficits)]
    violations.append(2-total-sum(deficits))
    low_bound = math.sqrt(2*n*(2*n-2+total))
    if total <= .75:
        region, region_bound = 'T <= 3/4', low_bound
    else:
        region = 'T > 3/4'
        violations.append(total-max(beta))
        region_bound = math.sqrt(max(0, 4-2*total**2)) + math.sqrt((2*n-2)*(2*n-4+total+total**2))
    global_bound = 2*(n-1)+math.sqrt(2)
    violations += [sum(values)-region_bound, sum(values)-global_bound]
    if case['attainer']:
        identities.extend((abs(total-1), abs(sum(values)-global_bound)))
    return dict(singleton_lengths=beta, singleton_squared_mass=total,
                expected_absolute_singleton_sum=expected_absolute,
                singleton_trace_norm_over_dimension=spectral_absolute,
                query_anticommuting_weights=weights, site_deficits=deficits,
                region=region, region_score_bound=region_bound,
                singleton_closed_expression=closed_expression,
                global_flat_score_bound=global_bound,
                expected_exact_attainer=case['attainer'])


def check_case(case, tolerance):
    rho = case['rho']
    values, entropy, rank, reconstruction = scores(rho)
    n = len(values)//2
    identities = [norm(rho-rho.conj().T), abs(float(np.trace(rho).real)-1), reconstruction]
    # The general-rank projector statement below is a finite-budget bound;
    # it does not establish the conjectured entropy line for that family.
    violations = [] if case['family'] == 'flat_general_rank' else [
        sum(values)-math.sqrt(2)*n-(2-math.sqrt(2))*entropy]
    if case['family'] == 'flat_half_rank':
        family = check_flat(case, values, identities, violations)
    elif case['family'] == 'flat_general_rank':
        d = len(rho)
        projector = rank*rho
        reflection = 2*projector-np.eye(d)
        identities.append(norm(projector@projector-projector))
        coefficients = {}
        for word in itertools.product(range(4), repeat=n):
            coefficients[word] = float(np.trace(reflection@tensor(PAULIS[k] for k in word)).real/d)
        identities.extend((abs(sum(c*c for c in coefficients.values())-1),
                           abs(coefficients[(0,)*n]-(2*rank/d-1))))
        weights, compressions = [], []
        for i in range(n):
            for a in (1, 3):
                query = local(n, i, PAULIS[a])
                w = sum(c*c for word, c in coefficients.items() if word[i] not in (0, a))
                weights.append(w)
                compression_square = float(np.trace(projector@query@projector@query).real/rank)
                compressions.append(compression_square)
                identities.append(abs(compression_square-(1-d*w/(2*rank))))
                violations.append(values[2*i+(a == 3)]**2-compression_square)
        violations.append(1-(2*rank/d-1)**2-sum(weights))
        bound = math.sqrt(2*n*(2*n-2+2*rank/d))
        violations.append(sum(values)-bound)
        family = dict(query_anticommuting_weights=weights,
                      normalized_compression_squares=compressions,
                      general_flat_rank_score_bound=bound,
                      finite_memory_subset_score=2*(n-1)+math.sqrt(2),
                      scope='Finite-budget score bound only; no entropy-line claim for this family.')
        if n == 4 and rank == 7:
            beta = []
            for site in range(n):
                squared = sum(coefficients[tuple(a if i == site else 0 for i in range(n))]**2
                              for a in (1, 3))
                beta.append(math.sqrt(squared))
            total = sum(b*b for b in beta)
            nonidentity_mass = 1-(2*rank/d-1)**2
            expected_absolute = sum(abs(sum(sign*b for sign, b in zip(signs, beta)))
                                    for signs in itertools.product((-1, 1), repeat=n))/d
            a, b, c, e = sorted(beta, reverse=True)
            identities.append(abs(expected_absolute-max(a, (3*a+b+c+e)/4, (a+b+c)/2)))
            bias_cap = 2*rank/d
            violations.extend((max(beta)-bias_cap, total-expected_absolute,
                               total-bias_cap, 2*nonidentity_mass-total-sum(weights),
                               35/32-sum(weights)))
            refined_bound = math.sqrt(54)
            violations.extend((sum(values)-refined_bound,
                               refined_bound-(6+math.sqrt(2))))
            family.update(singleton_lengths=beta, singleton_squared_mass=total,
                          singleton_bias_cap=bias_cap, nonidentity_squared_mass=nonidentity_mass,
                          expected_absolute_singleton_sum=expected_absolute,
                          refined_anticommuting_weight_lower_bound=35/32,
                          refined_flat_rank_score_bound=refined_bound)
        else:
            violations.append(bound-(2*(n-1)+math.sqrt(2)))
    elif case['family'] == 'classical_flag':
        family = check_flag(case['tree'], identities, violations)
        if case['attainer']:
            identities.append(abs(violations[0]))
    elif case['family'] == 'conditional_counterexample':
        marginal = np.trace(rho.reshape(2, 2, 2, 2), axis1=0, axis2=2)
        _, marginal_entropy, _, _ = scores(marginal)
        conditional_entropy = entropy-marginal_entropy
        local_witness = sum(values[:2])
        claimed_upper = math.sqrt(2)+(2-math.sqrt(2))*conditional_entropy
        gap = local_witness-claimed_upper
        if gap <= .07:
            raise AssertionError('The intended strict local counterexample is missing.')
        identities.extend(abs(a-b) for a, b in zip(values, (.8, 1, .6, .8)))
        identities.extend((abs(entropy-1), abs(conditional_entropy-(1-binary_entropy(.9)))))
        family = dict(conditional_entropy=conditional_entropy,
                      local_witness=local_witness, false_local_upper_bound=claimed_upper,
                      strict_local_violation=gap,
                      global_entropy_bound=math.sqrt(2)*n+(2-math.sqrt(2))*entropy)
    elif case['family'] == 'spectral_condition':
        spectrum, basis = np.linalg.eigh(rho)
        root = (basis*np.sqrt(spectrum))@basis.conj().T
        kappa = float(max(spectrum)/min(spectrum))
        identities.append(abs(kappa-case['target_kappa']))
        alpha = 1+2*math.sqrt(kappa)/(1+kappa)
        coefficient = alpha*math.log(2)/2
        symmetric_information, affinities = [], []
        for i in range(n):
            for pauli in (X, Z):
                query = local(n, i, pauli)
                query_basis = basis.conj().T@query@basis
                difference = spectrum[:, None]-spectrum[None, :]
                pair_sum = spectrum[:, None]+spectrum[None, :]
                information = float(.5*np.sum(difference**2/pair_sum*abs(query_basis)**2))
                affinity = float(np.trace(root@query@root@query).real)
                symmetric_information.append(information)
                affinities.append(affinity)
        for score, information, affinity in zip(values, symmetric_information, affinities):
            violations.extend((score*score-1+information,
                               alpha*(1-affinity)-information))
        energy = 0.0
        for i in range(n):
            marginal = np.trace(root.reshape((2,)*(2*n)), axis1=i, axis2=n+i).reshape(2**(n-1), -1)
            energy += 1-.5*float(np.trace(marginal@marginal).real)
        bound = 2*n-coefficient*(n-entropy)
        violations.extend((2*energy-sum(1-a for a in affinities),
                           math.log(2)/2*(n-entropy)-energy,
                           sum(values)-(2*n-.5*sum(symmetric_information)),
                           sum(values)-bound))
        below = kappa <= case['kappa_threshold']
        if below:
            violations.append((2-math.sqrt(2))-coefficient)
        elif coefficient >= 2-math.sqrt(2):
            raise AssertionError('The above-threshold diagnostic is on the wrong side.')
        family = dict(condition_number=kappa, threshold=case['kappa_threshold'],
                      below_threshold=below, spectral_coefficient=alpha,
                      entropy_deficit_coefficient=coefficient,
                      symmetric_information=symmetric_information,
                      affinities=affinities, depolarizing_energy=energy,
                      spectral_entropy_score_bound=bound)
    else:
        bell = case['bell_rho']
        # The exact Bell spectrum is available, including a deliberate zero.
        root = (case['bell_basis']*np.sqrt(case['probabilities']))@case['bell_basis'].conj().T
        identities.append(norm(root@root-bell))
        for site in (0, 1):
            marginal = np.trace(rho.reshape(2, 2, 2, 2), axis1=site, axis2=2+site)
            identities.append(norm(marginal-I/2))
        axes = [trace_norm_hermitian(root@np.kron(p, I)@root) for p in (X, Y, Z)]
        for p, axial in zip((X, Y, Z), axes):
            identities.append(abs(trace_norm_hermitian(root@np.kron(I, p)@root)-axial))
            permutation = case['bell_basis'].conj().T@np.kron(p, I)@case['bell_basis']
            targets = np.argmax(abs(permutation), axis=0)
            translated = float(sum(np.sqrt(case['probabilities']*case['probabilities'][targets])))
            identities.append(abs(axial-translated))
        directions = []
        determinant = float(np.prod(case['probabilities']))
        for site, rotation in enumerate(case['local_rotations']):
            for index, query in enumerate((X, Z)):
                rotated_query = rotation.conj().T@query@rotation
                direction = [float(np.trace(rotated_query@p).real/2) for p in (X, Y, Z)]
                directions.append(direction)
                actual = values[2*site+index]
                formula = sum(component**2*axis**2 for component, axis in zip(direction, axes))
                identities.append(abs(actual**2-formula))
                sandwich = root@local(2, site, rotated_query)@root
                determinant_formula = 2*float(np.trace(sandwich@sandwich).real)+8*math.sqrt(determinant)
                identities.append(abs(actual**2-determinant_formula))
                paired_eigenvalues = np.linalg.eigvalsh(sandwich)
                identities.append(float(np.max(abs(paired_eigenvalues+paired_eigenvalues[::-1]))))
        top = sorted(axes, reverse=True)[:2]
        rotated_score_bound = 2*math.sqrt(2)*math.sqrt(sum(a*a for a in top))
        coefficient = 2*(2-math.sqrt(2))*math.log(2)
        strong_bound = 4-coefficient*(2-entropy)
        violations.extend((sum(values)-rotated_score_bound,
                           math.log(2)*(2-entropy)-(2-sum(top)),
                           rotated_score_bound-(4-2*(2-math.sqrt(2))*(2-sum(top))),
                           sum(values)-strong_bound))
        family = dict(bell_spectrum=case['probabilities'].tolist(),
                      axial_fidelities=axes, rotated_query_directions=directions,
                      rotated_score_bound=rotated_score_bound,
                      entropy_deficit_coefficient=coefficient,
                      locally_mixed_entropy_bound=strong_bound)
    maximum_identity = max(identities)
    maximum_violation = max(0.0, *violations)
    if maximum_identity > tolerance or maximum_violation > tolerance:
        raise AssertionError(f"{case['label']}: identity {maximum_identity}, violation {maximum_violation}")
    return dict(label=case['label'], family=case['family'], n=n, rank=rank,
                entropy=entropy, score=sum(values), query_scores=values,
                family_checks=family, max_identity_error=maximum_identity,
                max_inequality_violation=maximum_violation)


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Tolerance must be positive and finite.')
    reports = [check_case(case, tolerance) for case in examples()]
    return dict(status='PASS', research_base=BASE, python=platform.python_version(),
                numpy=np.__version__, random_seed=RANDOM_SEED,
                tolerance=tolerance, spectral_zero_threshold=ZERO_THRESHOLD,
                case_count=len(reports), maximum_matrix_dimension=16,
                max_identity_error=max(r['max_identity_error'] for r in reports),
                max_inequality_violation=max(r['max_inequality_violation'] for r in reports),
                cases=reports,
                scope='Finite diagnostics of proved identities, family inequalities, and a false local bound. No optimizer, unrestricted optimality certificate, or novelty certification.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--tolerance', type=float, default=1e-10)
    arguments = parser.parse_args()
    text = json.dumps(run(arguments.tolerance), indent=2)+'\n'
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
