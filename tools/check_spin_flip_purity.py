#!/usr/bin/env python3
"""Small deterministic constructions for the three-qubit spin-flip theorem.

The objective is the sum of squared unrestricted root-fidelity scores,
not the balanced-decoder objective. These calculations check identities
on specified constructions; they are not a proof or an optimization.

    python tools/check_spin_flip_purity.py --output results/spin_flip_purity.json
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

BASE = 'e97d0d4a164c73c8ce1d945febadc1d267c0b6d5'
RANDOM_SEED = 2026092403
ZERO_THRESHOLD = 1e-14
IMBALANCES = (-1.0, -.37, 0.0, .4, 1.0)
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = (I, X, Y, Z)


def tensor(items):
    answer = np.ones((1, 1), complex)
    for item in items:
        answer = np.kron(answer, item)
    return answer


SPIN = tensor([Y, Y, Y])
QUERIES = [tensor(p if j == i else I for j in range(3))
           for i in range(3) for p in (X, Z)]
WORDS = [(word, tensor(PAULIS[j] for j in word))
         for word in itertools.product(range(4), repeat=3)]


def maximum_entry(matrix):
    return float(np.max(abs(matrix)))


def spin_flip(matrix):
    return SPIN@matrix.conj()@SPIN.conj().T


def theta(vector):
    return SPIN@vector.conj()


def root(matrix):
    eigenvalues, vectors = np.linalg.eigh(matrix)
    if min(eigenvalues) < -1e-10:
        raise AssertionError('Nonpositive density matrix.')
    eigenvalues = np.where(eigenvalues > ZERO_THRESHOLD, eigenvalues, 0.0)
    return (vectors*np.sqrt(eigenvalues))@vectors.conj().T


def fidelity_scores(rho):
    square_root = root(rho)
    scores = [float(sum(abs(np.linalg.eigvalsh(square_root@u@square_root))))
              for u in QUERIES]
    return scores, square_root


def kramers_frame(rng, projector=None):
    """Symplectic Gram--Schmidt: columns u, Theta u, v, Theta v."""
    basis = []
    for _ in range(2):
        vector = rng.normal(size=8)+1j*rng.normal(size=8)
        if projector is not None:
            vector = projector@vector
        for _ in range(2):
            if basis:
                previous = np.column_stack(basis)
                vector -= previous@(previous.conj().T@vector)
        length = np.linalg.norm(vector)
        if length < 1e-12:
            raise AssertionError('Degenerate fixed-seed Gram--Schmidt input.')
        vector /= length
        basis.extend((vector, theta(vector)))
    return np.column_stack(basis)


def analytic_equality_frame(projector, direction):
    columns = []
    for pair_projector in ((projector+direction)/2, (projector-direction)/2):
        index = int(np.argmax(np.real(np.diag(pair_projector))))
        vector = pair_projector[:, index]
        vector /= np.linalg.norm(vector)
        columns.extend((vector, theta(vector)))
    return np.column_stack(columns)


def support_data(label, frame):
    projector = frame@frame.conj().T
    support_direction = np.diag([1, 1, -1, -1])
    direction = frame@support_direction@frame.conj().T
    reflection = 2*projector-np.eye(8)
    identities = [maximum_entry(frame.conj().T@frame-np.eye(4)),
                  maximum_entry(projector@projector-projector),
                  maximum_entry(direction@direction-projector),
                  maximum_entry(projector@direction-direction),
                  maximum_entry(spin_flip(projector)-projector),
                  maximum_entry(spin_flip(direction)-direction),
                  abs(float(np.trace(projector).real)-4),
                  abs(float(np.trace(direction).real))]
    rw, sw, multiplicities = [], [], []
    vr = np.zeros((8, 8), complex)
    vs = np.zeros((8, 8), complex)
    for word, pauli in WORDS:
        a = np.trace(reflection@pauli)/8
        z = np.trace(direction@pauli)/8
        identities.extend((abs(float(a.imag)), abs(float(z.imag))))
        if sum(index != 0 for index in word) != 2:
            identities.extend((abs(float(a.real)), abs(float(z.real))))
            continue
        multiplicity = word.count(2)
        rw.append(float(a.real))
        sw.append(float(z.real))
        multiplicities.append(multiplicity)
        vr += multiplicity*a.real*pauli
        vs += multiplicity*z.real*pauli
    rw, sw, multiplicities = map(np.asarray, (rw, sw, multiplicities))
    y0 = float(sum(multiplicities*rw**2))
    z0 = float(sum(multiplicities*sw**2))
    cross = float(sum(multiplicities*rw*sw))
    identities.extend((abs(float(sum(rw**2))-1), abs(float(sum(sw**2))-.5),
                       maximum_entry(sum(u@reflection@u for u in QUERIES)-2*reflection+2*vr),
                       maximum_entry(sum(u@direction@u for u in QUERIES)-2*direction+2*vs)))
    compressed = [frame.conj().T@u@frame for u in QUERIES]
    determinant_roots = []
    for matrix in compressed:
        spectrum = np.linalg.eigvalsh(matrix)
        identities.append(float(max(abs(spectrum+spectrum[::-1]))))
        determinant = float(np.prod(spectrum))
        if determinant < -1e-12:
            raise AssertionError('Paired compression has negative determinant.')
        determinant_roots.append(math.sqrt(max(0.0, determinant)))
    determinant_sum = sum(determinant_roots)
    squared_sum = sum(matrix@matrix for matrix in compressed)
    identities.append(maximum_entry(squared_sum-4*np.eye(4)+frame.conj().T@vr@frame))
    identities.append(abs(float(np.trace(squared_sum).real)-(16-4*y0)))
    f0 = sum(float(sum(abs(np.linalg.eigvalsh(matrix))))**2/16 for matrix in compressed)
    linear = sum(float(np.trace(support_direction@matrix@matrix).real)/4 for matrix in compressed)
    quadratic = sum(float(np.trace(support_direction@matrix@support_direction@matrix).real)/8
                    for matrix in compressed)-determinant_sum/2
    identities.extend((abs(f0-(2-y0/2+determinant_sum/2)),
                       abs(linear+2*cross),
                       abs(quadratic-(1-2*z0-determinant_sum/2)),
                       abs(quadratic-(3-f0-y0/2-2*z0))))
    delta = 4-f0
    return dict(label=label, frame=frame, projector=projector, direction=direction,
                support_direction=support_direction, compressed=compressed,
                determinant_roots=determinant_roots, determinant_sum=determinant_sum,
                rw=rw, sw=sw, multiplicities=multiplicities, y0=y0, z0=z0,
                f0=f0, linear=linear, quadratic=quadratic, delta=delta,
                identity_errors=identities, violations=[y0-delta])


def check_state(support, imbalance, tolerance, equality=False):
    p, s, frame = (support[key] for key in ('projector', 'direction', 'frame'))
    rho = (p+imbalance*s)/4
    scores, square_root = fidelity_scores(rho)
    identities = list(support['identity_errors'])
    violations = list(support['violations'])
    spectrum = np.linalg.eigvalsh(rho)
    expected = sorted([0]*4+[(1+imbalance)/4]*2+[(1-imbalance)/4]*2)
    identities.extend((float(max(abs(spectrum-expected))),
                       maximum_entry(spin_flip(rho)-rho),
                       maximum_entry(square_root@square_root-rho),
                       maximum_entry(spin_flip(square_root)-square_root),
                       abs(float(np.trace(rho).real)-1)))
    per_query_quadratic = []
    support_s = support['support_direction']
    for u, k, det_root, score in zip(QUERIES, support['compressed'], support['determinant_roots'], scores):
        compressed = frame.conj().T@square_root@u@square_root@frame
        paired = np.linalg.eigvalsh(compressed)
        identities.append(float(max(abs(paired+paired[::-1]))))
        expression = float(np.trace(k@k + 2*imbalance*support_s@k@k
                                   + imbalance**2*support_s@k@support_s@k).real)/8
        expression += (1-imbalance**2)*det_root/2
        per_query_quadratic.append(expression)
        identities.append(abs(score**2-expression))
    objective = sum(value**2 for value in scores)
    polynomial = support['f0']+support['linear']*imbalance+support['quadratic']*imbalance**2
    sos = ((support['delta']-support['y0']/2)*(1-imbalance**2)
           + 2*float(sum(support['multiplicities']
                         *(imbalance*support['sw']+support['rw']/2)**2)))
    purity = float(np.trace(rho@rho).real)
    bound = 5-4*purity
    identities.extend((abs(objective-polynomial), abs(4-imbalance**2-objective-sos),
                       abs(purity-(1+imbalance**2)/4), abs(bound-(4-imbalance**2))))
    violations.extend((objective-bound, -sos))
    if equality:
        target_scores = [1, 0, 0, 1, 1, math.sqrt(max(0, 1-imbalance**2))]
        identities.extend(abs(a-b) for a, b in zip(scores, target_scores))
        identities.append(abs(objective-bound))
    max_identity = max(identities)
    max_violation = max(0.0, *violations)
    if max_identity > tolerance or max_violation > tolerance:
        raise AssertionError(f"{support['label']} r={imbalance}: residuals {max_identity}, {max_violation}")
    return dict(label=f"{support['label']}_r_{imbalance}", imbalance=imbalance,
                rank=2 if abs(imbalance) == 1 else 4, spectrum=spectrum.tolist(),
                query_root_fidelities=scores, per_query_quadratic_values=per_query_quadratic,
                squared_fidelity_sum=objective, polynomial_value=polynomial,
                polynomial_coefficients=[support['f0'], support['linear'], support['quadratic']],
                y_penalty=support['y0'], spectral_direction_y_penalty=support['z0'],
                flat_deficit=support['delta'], determinant_root_sum=support['determinant_sum'],
                sos_value=sos, purity=purity, purity_bound=bound,
                exact_equality_family=equality, max_identity_error=max_identity,
                max_inequality_violation=max_violation)


def special_controls(rng, tolerance):
    cyclic = (tensor([X, Z, I])+tensor([I, X, Z])+tensor([Z, I, X]))/math.sqrt(3)
    projector = (np.eye(8)+cyclic)/2
    rho = projector/4
    scores, square_root = fidelity_scores(rho)
    frame = kramers_frame(rng, projector)
    memory_spin = frame.conj().T@SPIN@frame.conj()
    errors = [maximum_entry(projector@projector-projector),
              maximum_entry(spin_flip(rho)-rho),
              maximum_entry(square_root@square_root-rho),
              maximum_entry(frame.conj().T@frame-np.eye(4)),
              maximum_entry(memory_spin@memory_spin.conj()+np.eye(4)),
              abs(sum(scores)-2*math.sqrt(6)), abs(sum(v*v for v in scores)-4)]
    for query, score in zip(QUERIES, scores):
        decoder = (frame.conj().T@query@frame)/math.sqrt(2/3)
        errors.extend((abs(score-math.sqrt(2/3)),
                       maximum_entry(decoder@decoder-np.eye(4)),
                       abs(float(np.trace(decoder).real)),
                       maximum_entry(memory_spin@decoder.conj()@memory_spin.conj().T+decoder)))
    bisector = np.array([math.cos(math.pi/8), math.sin(math.pi/8)])
    negative = np.kron(np.eye(4)/4, np.outer(bisector, bisector))
    negative_scores, negative_root = fidelity_scores(negative)
    negative_objective = sum(v*v for v in negative_scores)
    negative_purity = float(np.trace(negative@negative).real)
    negative_bound = 5-4*negative_purity
    spin_defect = maximum_entry(spin_flip(negative)-negative)
    errors.extend((maximum_entry(negative_root@negative_root-negative),
                   abs(negative_objective-5), abs(negative_bound-4)))
    if spin_defect <= .1 or negative_objective-negative_bound <= .9:
        raise AssertionError('The intended out-of-class negative control is missing.')
    if max(errors) > tolerance:
        raise AssertionError(f'Control identity residual {max(errors)}')
    return dict(cyclic_flat=dict(query_root_fidelities=scores,
                                fidelity_sum=sum(scores), squared_fidelity_sum=sum(v*v for v in scores),
                                purity=float(np.trace(rho@rho).real),
                                shared_memory_antiunitary_checked=True),
                negative_control=dict(label='nonsymmetric_subset_seed',
                                      query_root_fidelities=negative_scores,
                                      squared_fidelity_sum=negative_objective,
                                      purity=negative_purity, inapplicable_purity_bound=negative_bound,
                                      intentional_violation=negative_objective-negative_bound,
                                      spin_flip_maximum_entry_defect=spin_defect,
                                      scope='Outside spin-flip hypothesis; unrestricted root-fidelity scores, not balanced-decoder scores.'),
                max_identity_error=max(errors))


def run(tolerance):
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError('Tolerance must be positive and finite.')
    rng = np.random.default_rng(RANDOM_SEED)
    supports = [support_data(f'complex_kramers_support_{i}', kramers_frame(rng)) for i in range(8)]
    a, b = tensor([X, Z, I]), tensor([X, I, X])
    p, s = (np.eye(8)+a)/2, (b+a@b)/2
    equality = support_data('all_purity_pauli_attainer', analytic_equality_frame(p, s))
    states = [check_state(support, imbalance, tolerance) for support in supports for imbalance in IMBALANCES]
    states += [check_state(equality, imbalance, tolerance, equality=True) for imbalance in IMBALANCES]
    controls = special_controls(rng, tolerance)
    return dict(status='PASS: finite construction diagnostics; no proof or novelty certificate',
                research_base_main_sha=BASE,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                python_version=platform.python_version(), numpy_version=np.__version__,
                objective='F(rho)=sum_(i,b=X,Z) ||sqrt(rho) P_(i,b) sqrt(rho)||_1^2',
                query_order=['X1', 'Z1', 'X2', 'Z2', 'X3', 'Z3'],
                configuration=dict(random_seed=RANDOM_SEED, complex_kramers_supports=8,
                                   spectral_imbalances=IMBALANCES, tolerance=tolerance,
                                   spectral_zero_threshold=ZERO_THRESHOLD, maximum_matrix_dimension=8),
                invariant_state_count=len(states)+1, negative_control_count=1,
                total_state_constructions=len(states)+2,
                max_identity_error=max(controls['max_identity_error'], max(c['max_identity_error'] for c in states)),
                max_inequality_violation=max(c['max_inequality_violation'] for c in states),
                states=states, controls=controls,
                interpretation=['No optimization or broad search is performed.',
                                'Eigenvalues below the stated zero threshold are clipped only when constructing square roots; reconstruction is checked.',
                                'The intentional negative-control violation is recorded separately and excluded from the theorem residual.',
                                'Passing finite constructions do not prove unrestricted optimality, the symbolic theorem, or publication novelty.'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--tolerance', type=float, default=1e-10)
    arguments = parser.parse_args()
    report = run(arguments.tolerance)
    encoded = json.dumps(report, indent=2)+'\n'
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded, encoding='utf-8')
    print(encoded, end='')


if __name__ == '__main__':
    main()
