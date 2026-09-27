#!/usr/bin/env python3
"""Exact constants and fixed small constructions for three head-structure proofs.

No optimization or parameter scan is performed. The universal conclusions
come from the analytical proof notes, not these finite matrix diagnostics.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


RESEARCH_BASE = "eb88f82db5bfd4acd7b687ca209fc094fc5df2ea"
TOLERANCE = 4e-10
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = dict(I=I, X=X, Y=Y, Z=Z)
REFERENCE = ["XI", "ZI", "IX", "IZ"]
NOTE_NAMES = ["CONSERVED_SYMMETRY_CONVERSE.md", "HIGH_SECOND_MODE_ONE_BLOCK.md",
              "ZERO_PAULI_GAP_DICHOTOMY.md"]


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


def compare(residuals, label, actual, expected):
    error = float(np.linalg.norm(np.asarray(actual)-np.asarray(expected)) /
                  max(1, np.linalg.norm(expected)))
    residuals[label] = error
    require(error <= TOLERANCE, label)


def partial_reference(matrix, memory_dimension=4):
    return np.einsum("rqrs->qs", matrix.reshape(4, memory_dimension, 4, memory_dimension))


def channel(v, matrix):
    return partial_reference(v @ matrix @ v.conj().T)


def dual(v, matrix):
    return v.conj().T @ kron(np.eye(4), matrix) @ v


def amplified_dual(v, matrix):
    blocks = matrix.reshape(2, 4, 2, 4)
    result = np.empty((2, 2, 2, 2), dtype=complex)
    for row in range(2):
        for column in range(2):
            result[row, :, column, :] = dual(v, blocks[row, :, column, :])
    return result.reshape(4, 4)


def normalized_choi(v):
    images = [channel(v, a) for a in (I, X, Y, Z)]
    return (kron(I, images[0])+kron(X, images[1])-kron(Y, images[2])+
            kron(Z, images[3]))/4, images


def hamiltonian(readouts):
    return sum(kron(word(a), b) for a, b in zip(REFERENCE, readouts))


def full_hamiltonian(readouts, last_pair):
    refs = ["XII", "ZII", "IXI", "IZI", "IIX", "IIZ"]
    return sum(kron(word(a), b) for a, b in zip(refs, [*readouts, *last_pair]))


def exact_checks():
    checks = {}

    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness

    check("symmetry_tail_radicals", 7 < F(8, 3)**2 and 7 > 4,
          "2<sqrt7<8/3")
    check("symmetry_high_resolvent_branch", 12 < F(7, 2)**2 and 2 < F(3, 2)**2,
          "2sqrt3<7/2 and sqrt2<3/2")
    check("symmetry_endpoint_zero", 40**2*3 < 72**2, "4800<5184")
    check("symmetry_endpoint_ellipse", 16**2*3 < 28**2, "768<784")
    check("symmetry_derivative_first", 20-6*F(8, 3)-2*F(10, 3)/2 == F(2, 3),
          "20-16-10/3=2/3")
    check("symmetry_derivative_second", 20-6*F(8, 3) == 4, "20-16=4")
    check("symmetry_top_multiplicity", 4*3**2 > 32, "36>32")
    # Coefficients of ell^0, ell^1, ell^2 after positive squaring.
    check("symmetry_squared_quadratic", 100-4*46 == -84 and -60+4*20 == 20
          and 9-4*2 == 1,
          "(U+10-3ell)^2-4(46-20ell+2ell^2)=U^2+20U-84+(20-6U)ell+ell^2")
    low2, high2 = F(141421, 100000), F(99, 70)
    low3, high3 = F(433, 250), F(1732051, 1000000)
    check("one_block_radical_bounds", low2**2 < 2 < high2**2 and low3**2 < 3 < high3**2,
          "141421/100000<sqrt2<99/70;433/250<sqrt3<1732051/1000000")
    check("one_block_U_bounds", 4*low3-2-high2 > F(351, 100)
          and 4*high3-2-low2 < F(1757, 500), "351/100<u_star<1757/500")
    check("one_block_k_bounds", 2+low2 > F(1707, 500) and 2+high2 < F(683, 200),
          "1707/500<k<683/200")
    check("one_block_C_bounds", 40-28*high2 >= F(2, 5)
          and 40-28*low2 < F(403, 1000), "2/5<C<403/1000")
    # Multiplication in Q(sqrt2): (40-28r)(6+4r)=16-8r.
    check("one_block_C_identity", 40*6-28*4*2 == 16 and 40*4-28*6 == -8,
          "(40-28sqrt2)(6+4sqrt2)=8(2-sqrt2)")
    upper_e = F(57, 20)**2-(32-F(351, 100)**2-F(341, 100)**2)
    lower_e = 32-F(1757, 500)**2-F(683, 200)**2-F(14, 5)**2
    check("one_block_tail_upper", upper_e == F(707, 10000) > 0, str(upper_e))
    check("one_block_tail_lower", lower_e == F(149579, 1000000) > 0, str(lower_e))
    check("one_block_tail_below_three", 32-2*F(17, 5)**2 < 9, "32-2(17/5)^2<9")
    check("one_block_coefficient_bounds", 4-F(1757, 500)-F(403, 1000) == F(83, 1000)
          and 4-F(17, 5)-F(2, 5) == F(1, 5), "83/1000<4-U-C<1/5")
    check("one_block_decreasing_scalar", -F(4, 5)+F(1, 5)*F(18, 5)/F(14, 5)
          == -F(19, 35), "-4/5+(1/5)(18/5)/(14/5)=-19/35")
    margin = (4-F(1757, 500))*(F(1707, 500)-F(57, 20))
    margin -= F(403, 1000)*(F(1757, 500)-F(57, 20))
    check("one_block_endpoint_margin", margin == F(407, 62500) > 0, str(margin))
    check("zero_gap_support_scalar", F(3, 5)**2+F(4, 5)**2 == 1
          and F(17, 5) < 2+low2, "3-4-5 unit vectors give support17/5<2+sqrt2")
    check("split_EB_head_high_m", F(173, 100)**2 < 3 and F(283, 200)**2 > 2
          and F(999, 1000)*2*F(173, 100)-F(1, 1000) > 2+F(283, 200),
          "(999/1000)2sqrt3-1/1000>2+sqrt2")
    return {"count": len(checks), "witnesses": checks, "uses_floating_point": False}


def symmetry_readouts(rows, scales=None):
    basis = [[word("ZI"), word("XI"), word("YY")],
             [word("IZ"), word("ZX"), word("XX")]]
    if scales is None:
        scales = [1.0]*4
    result = []
    for index, row in enumerate(rows):
        coefficients = np.asarray(row, dtype=float)
        if np.linalg.norm(coefficients):
            coefficients = coefficients/np.linalg.norm(coefficients)
        result.append(scales[index]*sum(c*p for c, p in zip(coefficients, basis[index//2])))
    return result


def canonical_readouts():
    return symmetry_readouts([[np.sqrt(2), 1, 0], [np.sqrt(2), -1, 0],
                              [np.sqrt(2), 1, 0], [np.sqrt(2), -1, 0]])


def third_pairs():
    active_b, active_d = np.zeros((4, 4), complex), np.zeros((4, 4), complex)
    active_b[:2, :2], active_d[:2, :2] = Z, (3*Z+4*X)/5
    active_b[2:, 2:], active_d[2:, 2:] = I, Z
    angle = 0.31
    rotation = np.cos(angle)*np.eye(4)+1j*np.sin(angle)*word("YX")
    complex_b = rotation @ word("ZI") @ rotation.conj().T
    return [("commuting_scalar", np.eye(4), word("IZ")),
            ("one_active_block", active_b, active_d),
            ("complex_full_pair", complex_b, (3*word("XI")+4*word("YZ"))/5)]


def aligned_real_head(h, residuals):
    values, vectors = np.linalg.eigh(h.real)
    p = vectors[:, -2:] @ vectors[:, -2:].T
    s1, s2 = word("YIYZ").real, word("IYIY").real
    plus = p @ (np.eye(16)+s2)/2
    column = int(np.argmax(np.linalg.norm(plus, axis=0)))
    v0 = plus[:, column]/np.linalg.norm(plus[:, column])
    v = np.column_stack([v0, s1 @ v0])
    compare(residuals, "aligned_head_isometry", v.T @ v, I)
    compare(residuals, "aligned_head_projector", v @ v.T, p)
    compare(residuals, "S1_head_X", s1 @ v, v @ X)
    compare(residuals, "S2_head_Z", s2 @ v, v @ Z)
    return values, v


def symmetry_checks():
    cases = [("balanced", canonical_readouts()),
             ("three_generator_reflections", symmetry_readouts([[4, 3, 1], [4, -3, 2],
                                                                [4, 3, 2], [4, -3, -1]])),
             ("three_generator_interior", symmetry_readouts([[4, 3, 1], [4, -3, 2],
                                                             [4, 3, 2], [4, -3, -1]],
                                                            [.98, .97, .99, .98])),
             ("degenerate_commuting_endpoint", symmetry_readouts([[1, 0, 0]]*4)),
             ("zero_endpoint", [np.zeros((4, 4))]*4)]
    records = []
    for name, readouts in cases:
        residuals = {}
        h = hamiltonian(readouts)
        s1, s2, chirality = word("YIYZ"), word("IYIY"), word("YYII")
        compare(residuals, "real_H0", h.imag, np.zeros((16, 16)))
        compare(residuals, "S1_commutes", s1 @ h, h @ s1)
        compare(residuals, "S2_commutes", s2 @ h, h @ s2)
        compare(residuals, "symmetries_anticommute", s1 @ s2, -s2 @ s1)
        compare(residuals, "chirality", chirality @ h, -h @ chirality)
        values = np.linalg.eigvalsh(h)
        compare(residuals, "even_eigenvalue_multiplicity", values[::2], values[1::2])
        u, ell = float(values[-1]), float(values[-3])
        require(u <= 2*np.sqrt(3)+TOLERANCE, "sharp support cap")
        require(u*u+ell*ell <= 16+TOLERANCE, "symmetry spectral ellipse")
        for b in readouts:
            require(np.linalg.norm(b, 2) <= 1+TOLERANCE, "earlier contraction")
        record = {"case": name, "U_equals_m": u, "third_eigenvalue": ell}
        if u > 3:
            require(values[-1]-values[-3] > 1e-6, "isolated top doublet")
            values, v = aligned_real_head(h, residuals)
            choi, images = normalized_choi(v)
            q1, q2 = word("YZ"), word("IY")
            for label, sigma, memory in [("X", X, q1), ("Z", Z, q2)]:
                for index, a in enumerate((I, X, Y, Z)):
                    compare(residuals, f"covariance_{label}_{index}", channel(v, sigma @ a @ sigma),
                            memory @ channel(v, a) @ memory)
            compare(residuals, "flat_average_output", images[0], np.eye(4)/2)
            compare(residuals, "zero_head_Y", images[2], np.zeros((4, 4)))
            compare(residuals, "commuting_head_outputs", images[1] @ images[3], images[3] @ images[1])
            compare(residuals, "head_output_square", images[1] @ images[1]+images[3] @ images[3], np.eye(4)/4)
            compare(residuals, "Choi_flat_spectrum", np.linalg.eigvalsh(choi), [0]*4+[.25]*4)
            compare(residuals, "Choi_projection_identity", choi @ choi, choi/4)
            compare(residuals, "Choi_Y_pairing", kron(Y, np.eye(4)) @ choi @ kron(Y, np.eye(4)),
                    np.eye(8)/4-choi)
            # The rectangular classification requires reality as well as covariance.
            alpha2 = float(np.trace(images[1] @ images[1]).real/4)
            beta2 = float(np.trace(images[3] @ images[3]).real/4)
            compare(residuals, "rectangular_X_square", images[1] @ images[1], alpha2*np.eye(4))
            compare(residuals, "rectangular_Z_square", images[3] @ images[3], beta2*np.eye(4))
            record["rectangular_POVM_axis_magnitudes"] = [float(2*np.sqrt(max(0, alpha2))),
                                                         float(2*np.sqrt(max(0, beta2)))]
        full = []
        for pair_name, b, d in third_pairs():
            h3 = kron(X, b)+kron(Z, d)
            value = float(np.linalg.norm(full_hamiltonian(readouts, (b, d)), 2))
            require(value <= 5+TOLERANCE, "symmetry-family norm five")
            item = {"last_pair": pair_name, "full_norm": value}
            if u > 3:
                test = (u-ell)*amplified_dual(v, np.linalg.inv((5-ell)*np.eye(8)-h3))
                item["norm_five_envelope_maximum"] = float(np.linalg.eigvalsh(test)[-1])
                require(item["norm_five_envelope_maximum"] < 1+TOLERANCE, "norm-five head test")
            full.append(item)
        record["third_pair_checks"] = full
        record["relative_identity_residuals"] = residuals
        records.append(record)
    require(sum(record["U_equals_m"] > 3 for record in records) >= 3,
            "all three selected positive doublets exercised")
    return records


def one_block_checks():
    c, s = F(99, 100), np.sqrt(1-float(F(99, 100))**2)
    a, b = np.sqrt(1.5), 1/np.sqrt(2)
    npt = [(a*word("ZI")+b*word("XI"))/np.sqrt(2),
           (a*word("ZI")-b*word("XI"))/np.sqrt(2),
           float(c)*word("IZ")+s*word("YY"), float(c)*word("ZX")-s*word("XI")]
    tau = .001
    split = [(1-tau)*r for r in canonical_readouts()]
    split[0] += tau*word("XZ")/np.sqrt(2)
    split[1] -= tau*word("XZ")/np.sqrt(2)
    last_b, last_d = third_pairs()[1][1:]
    # A complex common memory unitary tests a different Bell plane and basis.
    angle = .23
    rotation = np.cos(angle)*np.eye(4)+1j*np.sin(angle)*word("XX")
    last_b, last_d = rotation @ last_b @ rotation.conj().T, rotation @ last_d @ rotation.conj().T
    h3 = kron(X, last_b)+kron(Z, last_d)
    last_values, last_vectors = np.linalg.eigh(h3)
    bell = np.outer(last_vectors[:, -1], last_vectors[:, -1].conj())
    r, delta, bound = np.sqrt(2), 2-np.sqrt(2), 4+np.sqrt(2)
    require(np.linalg.eigvalsh(r*np.eye(8)+delta*bell-h3)[0] >= -TOLERANCE,
            "one-block Bell spectral majorant")
    records = []
    for name, readouts in [("balanced", canonical_readouts()), ("non_EB_head", npt),
                           ("split_EB_head", split)]:
        residuals = {}
        h = hamiltonian(readouts)
        values, vectors = np.linalg.eigh(h)
        u, m, ell = map(float, [values[-1], values[-2], values[-3]])
        require(m >= 2+np.sqrt(2), "chosen one-block head in high-m regime")
        v = vectors[:, [-1, -2]]
        moment = channel(v, np.diag([u*u, m*m]))
        moment_gap = float(np.linalg.eigvalsh(8*np.eye(4)-moment)[0])
        require(moment_gap >= -TOLERANCE, "actual weighted channel moment")
        compression = amplified_dual(v, bell)
        bell_cap = float(np.linalg.eigvalsh(compression)[-1])
        require(bell_cap <= 8/(m*m)+TOLERANCE, "positive Bell compression bound")
        weights = kron(I, np.diag(np.sqrt([u-ell, m-ell])))
        t = bound-ell
        resolvent = np.linalg.inv(t*np.eye(8)-h3)
        majorant = np.eye(8)/(t-r)+delta*bell/((t-r)*(t-2))
        require(np.linalg.eigvalsh(majorant-resolvent)[0] >= -TOLERANCE,
                "one-block resolvent comparison")
        test = weights @ amplified_dual(v, resolvent) @ weights
        scalar = (u-ell)/(t-r)*(1+8*delta/(m*m*(t-2)))
        require(scalar < 1, "one-block scalar certificate")
        test_value = float(np.linalg.eigvalsh(test)[-1])
        require(test_value <= scalar+TOLERANCE, "one-block scalar majorizes full head test")
        full_norm = float(np.linalg.norm(full_hamiltonian(readouts, (last_b, last_d)), 2))
        require(full_norm < bound, "one-block full norm")
        choi, _ = normalized_choi(v)
        ppt = choi.reshape(2, 4, 2, 4).transpose(2, 1, 0, 3).reshape(8, 8)
        ppt_min = float(np.linalg.eigvalsh(ppt)[0])
        if name == "non_EB_head":
            require(ppt_min < -1e-4, "non-EB head genuinely exercised")
        if name == "split_EB_head":
            compare(residuals, "split_top_gap", u-m, 2*tau)
            require(ppt_min >= -TOLERANCE, "split head PPT consistency")
        compare(residuals, "head_isometry", v.conj().T @ v, I)
        compare(residuals, "Bell_projector", bell @ bell, bell)
        compare(residuals, "Bell_reference_marginal",
                np.einsum("rqsq->rs", bell.reshape(2, 4, 2, 4)), I/2)
        records.append({"case": name, "U": u, "m": m, "ell": ell,
                        "channel_moment_minimum_gap": moment_gap, "Bell_compression_maximum": bell_cap,
                        "Bell_compression_cap": float(8/(m*m)), "scalar_certificate": float(scalar),
                        "full_head_test_maximum": test_value, "full_norm": full_norm,
                        "Choi_partial_transpose_minimum": ppt_min,
                        "relative_identity_residuals": residuals})
    return records


def zero_gap_checks():
    plus, minus = (I+Z)/2, (I-Z)/2
    cases = [("traceless_two_site", (word("XIZ")+2*word("ZIZ")+
                                    word("IXX")+2*word("IZX"))/np.sqrt(10),
              [np.sqrt(.6), np.sqrt(.9), np.sqrt(.6), np.sqrt(.9)], True),
             ("one_site_distinct_axes", kron((3*word("XI")+4*word("ZI"))/5, plus)+
              kron((4*word("XI")-3*word("ZI"))/5, minus), [.7, .7, 1, 1], False),
             ("flagged_disjoint_axes", kron((3*word("XI")+4*word("ZI"))/5, plus)+
              kron((4*word("IX")-3*word("IZ"))/5, minus), [.8, .9, .9, .8], False)]
    records = []
    for name, reflection, expected_profile, is_eb in cases:
        residuals = {}
        projection = (np.eye(8)+reflection)/2
        rho, root = projection/4, projection/2
        compare(residuals, "complement_reflection", reflection @ reflection, np.eye(8))
        compare(residuals, "complement_projector", projection @ projection, projection)
        compare(residuals, "complement_flat_marginal", partial_reference(rho, 2), I/2)
        compare(residuals, "root_square", root @ root, rho)
        t = partial_reference(root, 2)
        compare(residuals, "root_marginal", t, I)
        affinity_sum, profile = 0.0, []
        for query in REFERENCE:
            a = kron(word(query), I)
            profile.append(float(np.sum(np.linalg.svd(root @ a @ root, compute_uv=False))))
            affinity_sum += float(np.trace(root @ a @ root @ a).real)
        compare(residuals, "zero_Pauli_gap", affinity_sum, 2+float(np.trace(t @ t).real)/2)
        compare(residuals, "classified_support_profile", profile, expected_profile)
        values, vectors = np.linalg.eigh(rho)
        purification = vectors[:, -4:]/2
        v = np.sqrt(2)*purification.reshape(4, 2, 4).transpose(0, 2, 1).reshape(16, 2)
        compare(residuals, "purified_head_isometry", v.conj().T @ v, I)
        choi, images = normalized_choi(v)
        ppt = choi.reshape(2, 4, 2, 4).transpose(2, 1, 0, 3).reshape(8, 8)
        ppt_min = float(np.linalg.eigvalsh(ppt)[0])
        if is_eb:
            require(ppt_min >= -TOLERANCE, "traceless channel PPT consistency")
            for j in range(1, 4):
                for k in range(j+1, 4):
                    compare(residuals, f"EB_commuting_outputs_{j}_{k}", images[j] @ images[k], images[k] @ images[j])
        else:
            require(sum(profile) <= 2+np.sqrt(2)+TOLERANCE, "zero-gap low-support branch")
        records.append({"case": name, "support_profile": profile, "support_sum": float(sum(profile)),
                        "squared_support_deficit": float(3-np.dot(profile, profile)),
                        "Choi_partial_transpose_minimum": ppt_min,
                        "relative_identity_residuals": residuals})
    return records


def weighted_polar_check():
    """One unequal-weight purification checks the four correlation formulas."""
    residuals = {}
    a, b, c, d = np.arange(1, 5)/np.sqrt(30)
    r, s = np.sqrt(a*a+b*b), np.sqrt(c*c+d*d)

    def real_frame(first, second):
        z_axis = (first*X+second*Z)/np.sqrt(first*first+second*second)
        x_axis = (second*X-first*Z)/np.sqrt(first*first+second*second)
        _, vectors = np.linalg.eigh(z_axis.real)
        frame = vectors[:, [1, 0]]
        if (frame.T @ x_axis @ frame)[0, 1].real < 0:
            frame[:, 1] *= -1
        return frame

    reference_frame = kron(real_frame(a, b), real_frame(c, d))
    purification = np.zeros((4, 4, 2), dtype=complex)
    for first_bit in range(2):
        for second_bit in range(2):
            label = 2*first_bit+second_bit
            first_sign, second_sign = 1-2*first_bit, 1-2*second_bit
            chi = np.array([np.sqrt((1+first_sign*r)/2),
                            second_sign*np.sqrt((1-first_sign*r)/2)])
            purification[:, label, :] = reference_frame[:, label, None]*chi[None, :]/2
    v = np.sqrt(2)*purification.reshape(16, 2)
    compare(residuals, "weighted_head_isometry", v.conj().T @ v, I)
    sigma = v @ v.conj().T/2
    expected = [(a*word("ZI")+b*s*word("XI"))/(4*r),
                (b*word("ZI")-a*s*word("XI"))/(4*r),
                (c*word("IZ")+d*r*word("ZX"))/(4*s),
                (d*word("IZ")-c*r*word("ZX"))/(4*s)]
    readouts, profile = [], []
    for index, (query, target) in enumerate(zip(REFERENCE, expected)):
        correlation = partial_reference(kron(word(query), np.eye(4)) @ sigma)
        compare(residuals, f"weighted_correlation_{index}", correlation, target)
        values, vectors = np.linalg.eigh(correlation)
        require(np.min(np.abs(values)) > 1e-3, "weighted correlation invertible")
        readouts.append((vectors*np.sign(values)) @ vectors.conj().T)
        profile.append(float(np.sum(np.abs(values))))
    compare(residuals, "weighted_profile", profile,
            [np.sqrt(1-b*b), np.sqrt(1-a*a), np.sqrt(1-d*d), np.sqrt(1-c*c)])
    compare(residuals, "weighted_squared_budget", np.dot(profile, profile), 3)
    full_norms = []
    for pair_name, last_b, last_d in third_pairs():
        value = float(np.linalg.norm(full_hamiltonian(readouts, (last_b, last_d)), 2))
        require(value <= 5+TOLERANCE, "weighted polar readout converse")
        full_norms.append({"last_pair": pair_name, "full_norm": value})
    return [{"case": "weights_1_2_3_4_over_sqrt30", "support_profile": profile,
             "third_pair_checks": full_norms, "relative_identity_residuals": residuals}]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    source = Path(__file__).resolve()
    repository = source.parents[1]
    notes = [repository/"docs/audits"/name for name in NOTE_NAMES]
    if arguments.output:
        destination = arguments.output.resolve()
        if destination in [source, *(note.resolve() for note in notes)] or destination.suffix != ".json":
            raise ValueError("Output must be JSON and must not overwrite source or proof notes")
    report = {"status": "exact scalar and fixed matrix checks passed", "research_base": RESEARCH_BASE,
              "python": platform.python_version(), "numpy": np.__version__, "tolerance": TOLERANCE,
              "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
              "proof_note_sha256": {str(note.relative_to(repository)): hashlib.sha256(note.read_bytes()).hexdigest()
                                     for note in notes},
              "exact_constants": exact_checks(), "symmetry_constructions": symmetry_checks(),
              "one_block_constructions": one_block_checks(), "zero_gap_constructions": zero_gap_checks(),
              "weighted_polar_construction": weighted_polar_check(),
              "maximum_matrix_dimension": 32,
              "scope": "Exact rational constants and twelve fixed constructions; no scan, optimization, universal numerical proof, or publication-priority claim."}
    residuals = [value for group in ["symmetry_constructions", "one_block_constructions", "zero_gap_constructions",
                                   "weighted_polar_construction"]
                 for record in report[group] for value in record["relative_identity_residuals"].values()]
    report["matrix_identity_count"] = len(residuals)
    report["maximum_relative_identity_residual"] = max(residuals)
    encoded = json.dumps(report, indent=2, sort_keys=True)+"\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
