#!/usr/bin/env python3
"""Bounded fixed-matrix diagnostics for the nonflat quarter-rank converse.

No optimizer, random sampling, or parameter grid. Analytical proofs and the
separate exact polynomial certificate establish universal assertions.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import numpy as np

BASE = "c8b2e88d6721cb9208c797788f334d7f8b1e1848"
NOTE = "docs/audits/NONFLAT_QUARTER_RANK_CONVERSE.md"
TOL = 3e-9
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1., -1.]).astype(complex)
PAULIS = dict(I=I, X=X, Y=Y, Z=Z)
R2, R3 = np.sqrt(2.), np.sqrt(3.)
TARGET = 4+2*R2


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def kron(*matrices):
    result = np.ones((1, 1), complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def word(letters):
    return kron(*(PAULIS[letter] for letter in letters))


def normalize(matrix):
    return matrix/np.linalg.norm(matrix)


def compare(errors, label, actual, expected):
    residual = float(np.linalg.norm(np.asarray(actual)-np.asarray(expected))/max(1., np.linalg.norm(expected)))
    errors[label] = residual
    require(residual <= TOL, label)


def nonnegative(margins, label, value):
    margins[label] = float(value)
    require(value >= -TOL, label)


def exact_checks():
    checks = {}
    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness
    check("A_low_trace_affinity", F(9, 2)+F(3, 2)*F(15, 16)**2 == F(2979, 512), "9/2+(3/2)(15/16)^2=2979/512")
    check("A_low_trace_radical_gap", 2*1024**2-1443**2 == 14903, "sqrt2>1443/1024")
    check("A_r_squared_lower", 17**2-2*12**2 == 1, "sqrt2<17/12 implies (sqrt2-1)^2>1/6")
    check("A_r_squared_upper", 2*32**2-45**2 == 23, "sqrt2>45/32 implies (sqrt2-1)^2<3/16")
    check("A_w_rectangle", F(9, 8)*F(3, 16)/F(15, 16) == F(9, 40), "w<9/40")
    check("A_group_monotonicity_gap", 2-F(9, 10)-(2+F(3, 16))/2 == F(1, 160), "W_min-D_min/2>1/160")
    check("A_curvature_numerator", F(7, 5)**2 < 2, "1+sqrt2>12/5")
    check("A_curvature_denominator", F(5, 2)**2 > 6, "5+2sqrt6<10")
    check("A_curvature_coefficient", F(12, 5)/10 == F(6, 25), "curvature>6/25")
    check("A_SOS_v_squared", F(3, 2) == F(3, 2), "v^2 coefficient=3/2")
    check("A_SOS_v_h_squared", -3*F(8, 15) == -F(8, 5), "v*h^2 coefficient=-8/5")
    check("A_SOS_h_squared", F(1, 12)+F(1, 15)+F(1, 60) == F(1, 6), "h^2 coefficient=1/6")
    check("A_SOS_h_cubed_cancellation", F(8, 15)-F(8, 15) == 0, "h^3/sqrt2 coefficients cancel")
    check("A_SOS_h_fourth", F(3, 2)*F(8, 15)**2+F(8, 15) == F(24, 25), "h^4 coefficient=24/25")
    check("T1_spectral_normalization", 3*3**2+2**2 == 31, "spectrum (3,3,3,2)/sqrt31 has HS norm1")
    check("T1_negative_gap", 2*259**2 > 346**2, "346-259sqrt2<0")
    check("T1_necessary_strip", 1061**2-8*372**2 == 18649, "55/372<3-2sqrt2")
    check("T1_delta_identity", F(3, 124)+1-F(163, 186) == F(55, 372), "delta=v^2+1-y=55/372")
    check("T1_constant_coefficient", F(3, 124)+3*F(23, 186)+F(2, 248)+4*F(121, 2232) == F(346, 558), "T1 constant coefficient=346/558")
    check("T1_radical_coefficient", -2*F(23, 186)-4*F(121, 2232) == -F(259, 558), "T1 sqrt2 coefficient=-259/558")
    check("complex_unitary", 399**2+40**2 == 401**2, "(399I+40iG)/401 is unitary when G^2=I")
    check("B_tau_box", 2*2824**2-3993**2 == 5903, "sqrt2>3993/2824 gives tau<9/25")
    check("B_mu_box", 2*625**2-881**2 == 5089, "sqrt2-1>256/625 gives mu/u<9/25")
    check("B_x_rectangle", 2*F(3,8)*(F(1,2)+F(3,8)) == F(21,32), "x<21/32")
    check("B_H_threshold", 2*14**2 > 19**2, "sqrt2>19/14 gives (7sqrt2-8)/3>1/2")
    check("B_large_x_domain", 2*21**2 < 32**2, "21/32<1/sqrt2")
    return checks


def constructions():
    local = np.cos(np.pi/8)*I-1j*np.sin(np.pi/8)*Y
    change = kron(local, local, local, local)
    rotate = lambda matrix: change @ matrix @ change.conj().T
    diag = lambda indices, weights: np.diag([dict(zip(indices, weights)).get(j, 0.) for j in range(16)]).astype(complex)
    equality = rotate(diag([0, 1, 2, 3], [.5]*4))
    psi = np.zeros(16, complex)
    psi[4], psi[3] = np.sqrt(2/3), np.sqrt(1/3)
    obstruction = rotate((diag([0, 1, 2], [3, 3, 3])+2*np.outer(psi, psi.conj()))/np.sqrt(31))
    nonflat_a = rotate(normalize(diag([0, 1, 2, 3], [6, 5, 5, 4])))
    majority = rotate(normalize(diag([0, 1, 2, 4], [11, 10, 10, 9])))
    unitary = (399*np.eye(16)+40j*word("ZXXI"))/401
    complex_majority = unitary @ majority @ unitary.conj().T
    rank_three = rotate(normalize(diag([0, 1, 2], [2, 1, 1])))
    ghz = np.zeros(16, complex)
    ghz[0], ghz[15] = 1/np.sqrt(2), 1j/np.sqrt(2)
    pure = np.outer(ghz, ghz.conj())
    attained = rotate(normalize(diag([0, 1, 2, 8], [5, 3, 3, 2])))
    return [("bisector_equality", equality, "equality"),
            ("physical_old_T1_obstruction", obstruction, "obstruction"),
            ("nonflat_pair_branch", nonflat_a, "A"),
            ("nonflat_majority_branch", majority, "B"),
            ("complex_nonflat_majority", complex_majority, "complex_B"),
            ("nonflat_rank_three", rank_three, "rank_three"),
            ("complex_GHZ_rank_one", pure, "pure"),
            ("attained_middle_spectral_envelope", attained, "attained")]


def local_blocks(matrix, site, sx, sz):
    angle = np.arctan2(sx, sz) if np.hypot(sx, sz) > TOL else 0.
    local = np.cos(angle/2)*I-1j*np.sin(angle/2)*Y
    factors = [I]*4
    factors[site] = local
    change = kron(*factors)
    rotated = change.conj().T @ matrix @ change
    other = [j for j in range(4) if j != site]
    blocks = rotated.reshape([2]*8).transpose([site]+other+[site+4]+[j+4 for j in other]).reshape(2, 8, 2, 8)
    return blocks[0, :, 0, :], blocks[0, :, 1, :], blocks[1, :, 1, :]


def spectral_envelope(u, v, mu):
    first, second = (u-R2*v)/2, (u-v/R3)/2
    if mu <= first:
        return mu+R2*v
    if mu <= second:
        radicand = 2*(3*(1-mu*mu)-(2*u-mu)**2)
        require(radicand >= -TOL, "middle spectral radicand")
        return (2*u-mu+np.sqrt(max(0., radicand)))/3
    return (u+R3*v)/2


def check_construction(name, matrix, kind):
    errors, margins = {}, {}
    compare(errors, "Hermitian", matrix, matrix.conj().T)
    eigenvalues = np.linalg.eigvalsh(matrix)
    nonnegative(margins, "positive", eigenvalues[0])
    rank = int(np.count_nonzero(eigenvalues > TOL))
    require(1 <= rank <= 4, "rank cap")
    compare(errors, "HS_normalized", np.trace(matrix @ matrix), 1)
    u = min(1., float(np.trace(matrix).real)/2)
    v = np.sqrt(max(0., 1-u*u))
    kappa, minimum = float(eigenvalues[-1]), float(eigenvalues[-rank])
    k = u+R3*v
    padded = eigenvalues[-4:]
    compare(errors, "four_eigenvalue_centering", np.sum((padded-u/2)**2), v*v)
    nonnegative(margins, "spectral_spread", R2*v-(kappa-minimum))
    nonnegative(margins, "spectral_maximum", k/2-kappa)
    singleton, affinities, scores, deficits, lengths = np.zeros((16, 16), complex), [], [], [], []
    local_records = []
    for site in range(4):
        coefficients, pair = [], []
        for axis in "XZ":
            query = word("I"*site+axis+"I"*(3-site))
            coefficient = float(np.trace(matrix @ query).real)/4
            coefficients.append(coefficient)
            singleton += coefficient*query/4
            affinity = float(np.trace(matrix @ query @ matrix @ query).real)
            score = float(np.sum(np.linalg.svd(matrix @ query @ matrix, compute_uv=False)))
            nonnegative(margins, f"site{site}_{axis}_affinity", affinity)
            nonnegative(margins, f"site{site}_{axis}_affinity_cap", 1-affinity)
            nonnegative(margins, f"site{site}_{axis}_fidelity_affinity", affinity-score*score)
            affinities.append(affinity); scores.append(score); pair.append(affinity)
        length = float(np.linalg.norm(coefficients)); lengths.append(length)
        mu = u-2*length
        W = 2-sum(pair); deficits.append(W)
        A, C, D = local_blocks(matrix, site, *coefficients)
        normC = float(np.linalg.norm(C)**2)
        compare(errors, f"site{site}_oriented_mu", np.trace(D), mu)
        compare(errors, f"site{site}_exact_block_W", W, 1-2*np.trace(A@D).real+4*normC-2*np.trace(C@C).real)
        nonnegative(margins, f"site{site}_mu", mu)
        nonnegative(margins, f"site{site}_coherence_mass", normC-minimum*mu+mu*mu)
        nonnegative(margins, f"site{site}_spectral_block_inequality", np.linalg.eigvalsh(D@D+C.conj().T@C-minimum*D)[0])
        nonnegative(margins, f"site{site}_rank_deficit", W-(16/rank)*length*length)
        nonnegative(margins, f"site{site}_kappa_deficit", W-(1-2*kappa*mu))
        nonnegative(margins, f"site{site}_exact_spread_deficit", W-(1-2*mu*(kappa-minimum+mu)))
        nonnegative(margins, f"site{site}_universal_spread_deficit", W-(1-2*mu*(R2*v+mu)))
        record = dict(singleton_length=length, mu=mu, deficit=W)
        if u > np.sqrt(3)/2:
            envelope = spectral_envelope(u, v, mu)
            nonnegative(margins, f"site{site}_joint_spectral_envelope", envelope-min(kappa,kappa-minimum+mu))
            nonnegative(margins, f"site{site}_joint_envelope_deficit", W-(1-2*mu*envelope))
            record["joint_spectral_envelope"] = envelope
            if kind == "attained" and site == 0:
                nonnegative(margins, "attained_middle_left", mu-(u-R2*v)/2)
                nonnegative(margins, "attained_middle_right", (u-v/R3)/2-mu)
                compare(errors, "attained_middle_W", W, 1-2*mu*envelope)
                compare(errors, "attained_middle_coherent_block_zero", C, np.zeros((8,8)))
        local_records.append(record)
    order = np.argsort(-np.array(lengths))
    a,b,c,d = np.array(lengths)[order]
    T = float(sum(value*value for value in lengths)); y=2*T
    R = max(b,(b+c+d)/2)
    variance = max(0.,T-a*a-R*R)
    top = np.linalg.eigvalsh(singleton)[-4:]
    compare(errors, "top_quarter_mean", np.mean(top), (a+R)/4)
    compare(errors, "top_quarter_variance", sum((top-np.mean(top))**2), variance/4)
    nonnegative(margins, "centered_circle", u*(a+R)+v*np.sqrt(variance)-y)
    nonnegative(margins, "singleton_mass_cap", (1+u*u)/2-y)
    nonnegative(margins, "first_singleton_trace_cap", u/2-a)
    Dtotal=float(sum(deficits)); delta=v*v+1-y
    nonnegative(margins, "Pauli_deficit", Dtotal-(4-u*u-y))
    nonnegative(margins, "local_deficit_sum", Dtotal-(4-4*k*u+2*k*(a+b+c+d)))
    affinity_score=float(sum(np.sqrt(np.maximum(affinities,0))))
    original_score=float(sum(scores))
    nonnegative(margins, "final_affinity_converse", TARGET-affinity_score)
    nonnegative(margins, "final_original_converse", TARGET-original_score)
    nonnegative(margins, "original_below_affinity", affinity_score-original_score)
    branch="A" if b >= c+d-TOL else "B"
    active = u*u >= (4*R2-3)/3-TOL and delta <= (R2-1)**2+TOL
    if kind in ["A","obstruction"]:
        require(branch=="A", "fixed A construction")
    if kind in ["B","complex_B"]:
        require(branch=="B", "fixed B construction")
        require(active, "fixed B construction enters difficult scalar strip")
    if active and branch=="A":
        p=a+b; Q=c*c+d*d; w=u-p; h=np.sqrt(max(0.,u*w)); x=2*k*w
        W=float(sum(np.array(deficits)[order[:2]]))
        nonnegative(margins,"A_tail_rank_circle", y*(1-y)-Q)
        nonnegative(margins,"A_pair_lower", W-(2-x))
        nonnegative(margins,"A_small_rectangle", .9-x)
        nonnegative(margins,"A_group_monotonicity", 2-x-(2+delta)/2)
        coupled=7*v*v/4+u*w-v*np.sqrt(max(0.,v*v+8*u*w-8*w*w))/4
        lower=1.5*v*v+h*h-v*h/R2
        nonnegative(margins,"A_coupled_root",delta-coupled)
        nonnegative(margins,"A_simple_lower",delta-lower)
        polynomial=1.5*v*v-v*h/R2+h*h/6-8*v*h*h/5+24*h**4/25
        sos=1.5*(v-h/(3*R2)-8*h*h/15)**2+8*h*h*(h-1/(2*R2))**2/15+h*h/60
        compare(errors,"A_SOS_identity",polynomial,sos)
        nonnegative(margins,"A_SOS_transfer",delta-(R2-1)*x+6*x*x/25-polynomial)
        threshold=2*(2+R2)*(np.sqrt(2+x)-R2)-2*x
        nonnegative(margins,"A_curvature",(R2-1)*x-6*x*x/25-threshold)
        group=2*np.sqrt(2+x)+2*np.sqrt(4-delta-x)
        nonnegative(margins,"A_group_dominates",group-affinity_score)
        nonnegative(margins,"A_group_target",TARGET-group)
    if branch=="B":
        q=b+c+d; mu=u-2*a; e=np.sqrt(variance); x=2*mu*(R2*v+mu)
        compare(errors,"B_circle_variance", e*e,y/2-a*a-q*q/4)
        nonnegative(margins,"B_tail_spread_lower", T-a*a-q*q/3)
        nonnegative(margins,"B_tail_spread_upper", q*q/2-(T-a*a))
        W1=deficits[int(order[0])]
        nonnegative(margins,"B_combined_remaining_deficit",Dtotal-(4-3*k*u+2*k*q-x))
        group=np.sqrt(max(0.,4-2*W1))+np.sqrt(max(0.,36-6*Dtotal+6*W1))
        nonnegative(margins,"B_actual_group",group-affinity_score)
        if active:
            lam=2*(R2-1)/3; baseline=4-4*R2/3
            Dstar=baseline+lam*x*(1-x); threshold_y=4-u*u-Dstar
            q0=(3*u+mu)/2-(u*u+threshold_y)/(2*k)
            H0=2*threshold_y-u*(u-mu); J0=2*threshold_y-(u-mu)**2
            C0=u*H0-q0; F0=C0*C0-v*v*(J0-H0*H0)
            tau=v/u; m=mu/u; d0=1+tau*tau; h0=1+R3*tau
            t=2*m*(R2*tau+m)
            Zpoly=(4*R2*d0/3-1)*d0-lam*t*(d0-t)
            Qpoly=h0*(3+m)*d0-d0-Zpoly
            Apoly=2*h0*(2*Zpoly-(1-m)*d0)-Qpoly
            Cpoly=2*h0*(2*Zpoly-(1-m)*d0)-d0*Qpoly
            Ppoly=Apoly*Apoly-tau*tau*(4*h0*h0*(2*Zpoly*d0-(1-m)**2*d0*d0)-Qpoly*Qpoly)
            compare(errors,"B_Y_polynomial_bridge",threshold_y,Zpoly/(d0*d0))
            compare(errors,"B_C_polynomial_bridge",C0,Cpoly/(2*h0*d0**2.5))
            compare(errors,"B_P_polynomial_bridge",F0,Ppoly/(4*h0*h0*d0**4))
            compare(errors,"B_equivalent_circle_residual",F0,(H0-u*q0)**2-v*v*(J0-q0*q0))
            nonnegative(margins,"B_tau_box",9/25-tau)
            nonnegative(margins,"B_normalized_mu_box",9/25-m)
            nonnegative(margins,"B_x_box",21/32-x)
            nonnegative(margins,"B_H_threshold",H0-.5)
            nonnegative(margins,"B_C_certificate_at_fixed_point",Cpoly-4/25)
            nonnegative(margins,"B_P_certificate_at_fixed_point",Ppoly-1/10000)
            nonnegative(margins,"B_strict_total_threshold",Dtotal-Dstar)
            if J0-H0*H0 >= 0:
                nonnegative(margins,"B_threshold_below_lower_circle_root",u*H0-v*np.sqrt(J0-H0*H0)-q0)
            if x < 1-1/R2:
                critical=baseline+lam*x-2*(1+R2)*x*x/(3*(np.sqrt(1+x)+1)**2)
                nonnegative(margins,"B_exact_group_curvature",Dstar-critical)
                nonnegative(margins,"B_group_monotonicity",1-x-Dstar/4)
                upper=np.sqrt(2+2*x)+np.sqrt(42-6*Dstar-6*x)
                nonnegative(margins,"B_threshold_group_target",TARGET-upper)
                nonnegative(margins,"B_threshold_group_dominates",upper-affinity_score)
            else:
                nonnegative(margins,"B_Cauchy_threshold",Dstar-(5-2*R2))
    if kind=="obstruction":
        compare(errors,"T1_singletons",[a,b,c,d],np.array([33,25,11,11])/(12*np.sqrt(31)))
        compare(errors,"T1_u",u,11/(2*np.sqrt(31)))
        compare(errors,"T1_y",y,163/186)
        compare(errors,"T1_rotated_affinities",affinities,[.5,.5,319/558,319/558,445/558,445/558,445/558,445/558])
        w=u-a-b; forced=max(0.,c-w)**2+max(0.,d-w)**2
        old=v*v+(1-2*(R2-1))*(1-y)+2*forced-4*(R2-1)*(c*c+d*d)
        compare(errors,"T1_exact_failure",old,(346-259*R2)/558)
        nonnegative(margins,"T1_strict_obstruction",-old)
    if kind=="equality":
        compare(errors,"affinity_retention_equality",affinity_score,TARGET)
        compare(errors,"original_retention_equality",original_score,TARGET)
    if "complex" in name:
        require(np.linalg.norm(matrix.imag)>.01,"complex seed")
    return dict(name=name,rank=rank,branch=branch,enters_difficult_strip=bool(active),u=u,v=v,y=y,delta=delta,
                affinity_root_score=affinity_score,original_trace_norm_score=original_score,query_affinities=affinities,
                query_trace_norm_scores=scores,local_data=local_records,relative_identity_residuals=errors,inequality_margins=margins)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    source=Path(__file__).resolve(); repo=source.parents[1]; note=repo/NOTE
    if args.output:
        destination=args.output.resolve()
        if destination in [source,note.resolve()] or destination.suffix!=".json":
            raise ValueError("Output must be JSON and cannot overwrite source or proof note")
    records=[check_construction(*case) for case in constructions()]
    report=dict(status="exact constants and fixed constructions passed",research_base=BASE,
                python=platform.python_version(),numpy=np.__version__,tolerance=TOL,
                source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                proof_note_sha256={NOTE:hashlib.sha256(note.read_bytes()).hexdigest()},
                exact_constants=exact_checks(),constructions=records,maximum_matrix_dimension=16,
                scope="Eight deterministic positive seed roots on four qubits, including a physical failure of the former T1 tangent, both nonflat branches, complex seeds, singular seeds, retention equality and an attained local spectral envelope. The final affinity and original trace-norm scores, local spread inequalities and branch identities are fixed-construction diagnostics. Universal inequalities are established by the analytical proof and its separate exact polynomial certificate. Floating-point identities and margins are not interval certificates. No random sampling, grid, optimizer, or novelty claim.")
    residuals=[value for row in records for value in row["relative_identity_residuals"].values()]
    margins=[value for row in records for value in row["inequality_margins"].values()]
    report.update(exact_scalar_count=len(report["exact_constants"]),fixed_construction_count=len(records),
                  matrix_identity_count=len(residuals),inequality_count=len(margins),
                  maximum_relative_identity_residual=max(residuals),minimum_inequality_margin=min(margins))
    encoded=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(encoded)
    print(encoded,end="")


if __name__=="__main__":
    main()
