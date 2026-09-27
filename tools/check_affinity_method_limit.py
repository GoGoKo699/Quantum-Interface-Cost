#!/usr/bin/env python3
"""Exact finite comparisons and small matrices for the affinity method limit.

The asymptotic conclusion belongs to the analytical proof, not this checker.
No random sampling, parameter grid, optimizer, or large matrix is used.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
from math import isqrt
import json
from pathlib import Path
import platform
import numpy as np

BASE = "ced383d1a4ad8d9c13fbd4ebe1befd3c6284519a"
NOTE = "docs/audits/AFFINITY_METHOD_LIMIT.md"
TOL = 3e-9
I = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]])
Z = np.diag([1.,-1.]).astype(complex)
R2 = np.sqrt(2.)


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def compare(errors, label, actual, expected):
    residual = float(np.linalg.norm(np.asarray(actual)-np.asarray(expected))/max(1.,np.linalg.norm(expected)))
    errors[label] = residual
    require(residual <= TOL, label)


def nonnegative(margins, label, value):
    margins[label] = float(value)
    require(value >= -TOL, label)


def sqrt_interval(value, digits=14):
    """Rational enclosure, checked exactly; uses no floating-point arithmetic."""
    value = F(value)
    require(value >= 0, "nonnegative exact radicand")
    scale = 10**digits
    integer = isqrt(value.numerator*scale*scale//value.denominator)
    lo = F(integer, scale)
    hi = lo if lo*lo == value else F(integer+1, scale)
    require(lo*lo <= value <= hi*hi, "integer square-root enclosure")
    return lo, hi


def exact_checks():
    checks = {}
    def check(label, condition, witness):
        require(condition, label)
        checks[label] = witness
    n=15
    check("star_rank", n+1 == 2**4, "rank16=2^4")
    check("star_normalization", F(1,2)+n*F(1,2*n) == 1, "1/2+15/30=1")
    check("star_G_square_constant", 2*n*n-(8**2+2*11**2) == 144, "G^2-K^2=144+30sqrt15-176sqrt2")
    check("star_G_square_coefficients", 2*n == 30 and 2*8*11 == 176, "radical coefficients30 and176")
    check("sqrt15_lower", 15*25-19**2 == 14, "sqrt15>19/5")
    check("sqrt2_upper", 10**2-2*7**2 == 2, "sqrt2<10/7")
    check("surrogate_strict_gap", 144+30*F(19,5)-176*F(10,7) == F(46,7), "G^2-K^2>46/7")
    check("star_original_radicand", n*n+6*n+1 == 4*79, "15^2+6*15+1=4*79")
    check("sqrt79_upper", 79 < 9**2, "g=sqrt2(7+sqrt79)<16sqrt2")
    check("original_strict_gap", 2*5**2 < 8**2, "16sqrt2<8+11sqrt2")
    t=F(3,5); a=(1+t)/2; fsq=(1+t*t)/2; b=(1+t**3)/(1+t*t)
    check("mixed_t", 4*F(1,10)*F(9,10) == t*t, "t=2sqrt(lambda(1-lambda))=3/5")
    check("mixed_affinity", a == F(4,5), "a=4/5")
    check("mixed_original_square", fsq == F(17,25), "F^2=17/25")
    check("mixed_decoder_affinity", b == F(76,85), "b=76/85")
    check("mixed_full_gap", a-fsq == F(3,25), "a-F^2=3/25")
    check("mixed_commutator_gap", a*(1-b) == F(36,425), "a(1-b)=36/425")
    check("mixed_Cauchy_gap", a*b-fsq == F(3,85), "ab-F^2=3/85")
    check("mixed_gap_decomposition", F(36,425)+F(3,85) == F(3,25), "36/425+3/85=3/25")
    check("mixed_gap_fraction", F(36,425)/F(3,25) == F(12,17), "commutator accounts for12/17 of squared gap")
    r2lo,r2hi=sqrt_interval(2); r15lo,r15hi=sqrt_interval(15); r79lo,r79hi=sqrt_interval(79)
    Glo=sqrt_interval(450+30*r15lo)[0]; Ghi=sqrt_interval(450+30*r15hi)[1]
    Klo,Khi=8+11*r2lo,8+11*r2hi
    glo,ghi=r2lo*(7+r79lo),r2hi*(7+r79hi)
    check("exact_G_minus_benchmark_interval", Glo-Khi > 0, "rational interval has strictly positive lower endpoint")
    check("exact_g_minus_benchmark_interval", ghi-Klo < 0, "rational interval has strictly negative upper endpoint")
    intervals={"surrogate_minus_benchmark":[str(Glo-Khi),str(Ghi-Klo)],
               "original_minus_benchmark":[str(glo-Khi),str(ghi-Klo)]}
    return checks, intervals


def positive_root(matrix):
    values,vectors=np.linalg.eigh(matrix)
    require(values[0] >= -TOL,"positive root input")
    return (vectors*np.sqrt(np.maximum(values,0))) @ vectors.conj().T


def query_gap(S, B, label, errors, margins):
    dimension=len(S)
    compare(errors,label+"_compressed_Hermitian",B,B.conj().T)
    nonnegative(margins,label+"_compressed_contraction",1-np.max(np.abs(np.linalg.eigvalsh(B))))
    M=S@B@S
    values,vectors=np.linalg.eigh(M)
    # A zero singular direction receives +1, so J is unitary on the support.
    signs=np.where(values < -TOL,-1.,1.)
    J=(vectors*signs)@vectors.conj().T
    Fscore=float(np.sum(np.abs(values)))
    a=float(np.trace(S@B@S@B).real)
    b=float(np.trace(S@J@S@J).real)
    commutator=float(np.linalg.norm(S@J-J@S)**2)
    sqrtS=positive_root(S)
    residual=float(b*np.linalg.norm(sqrtS@(B-(Fscore/b)*J)@sqrtS)**2)
    first=a*(1-b); second=a*b-Fscore*Fscore
    compare(errors,label+"_unitary_zero_extension",J@J,np.eye(dimension))
    compare(errors,label+"_polar_attainment",np.trace(M@J),Fscore)
    compare(errors,label+"_decoder_commutator",b,1-commutator/2)
    compare(errors,label+"_weighted_Cauchy_residual",second,residual)
    compare(errors,label+"_gap_decomposition",a-Fscore*Fscore,first+second)
    nonnegative(margins,label+"_affinity",a)
    nonnegative(margins,label+"_decoder_affinity",b)
    nonnegative(margins,label+"_decoder_affinity_cap",1-b)
    nonnegative(margins,label+"_commutator_gap",first)
    nonnegative(margins,label+"_Cauchy_gap",second)
    nonnegative(margins,label+"_fidelity_affinity_gap",a-Fscore*Fscore)
    return dict(F=Fscore,a=a,b=b,commutator_gap=first,Cauchy_gap=second,
                zero_extension_dimension=int(np.count_nonzero(np.abs(values)<=TOL)))


def star_case():
    errors,margins={},{}
    n=15
    S=np.diag([1/R2]+[1/np.sqrt(2*n)]*n).astype(complex)
    compare(errors,"star_HS_normalization",np.trace(S@S),1)
    require(np.linalg.matrix_rank(S)==16,"star_support_rank16")
    records=[]
    for site in range(1,n+1):
        for axis,sign in [("X",1),("Z",-1)]:
            B=np.eye(n+1,dtype=complex)/R2
            B[site,site]=-1/R2
            B[0,site]=B[site,0]=sign/R2
            # Exact compression of the original query in the bisector star basis.
            squared=np.eye(n+1)/2
            squared[0,0]=squared[site,site]=1
            compare(errors,f"site{site}_{axis}_compression_square",B@B,squared)
            record=query_gap(S,B,f"site{site}_{axis}",errors,margins)
            compare(errors,f"site{site}_{axis}_affinity_formula",record["a"],(1+1/np.sqrt(n))/2)
            compare(errors,f"site{site}_{axis}_original_formula",record["F"],(np.sqrt(n*n+6*n+1)+n-1)/(2*n*R2))
            records.append(record)
    G=float(sum(np.sqrt(record["a"]) for record in records))
    g=float(sum(record["F"] for record in records))
    benchmark=8+11*R2
    compare(errors,"star_surrogate_closed_form",G,n*np.sqrt(2+2/np.sqrt(n)))
    compare(errors,"star_original_closed_form",g,R2*(7+np.sqrt(79)))
    nonnegative(margins,"star_surrogate_exceeds_benchmark",G-benchmark)
    nonnegative(margins,"star_original_below_benchmark",benchmark-g)
    return dict(name="fifteen_input_star",ambient_qubits=15,compressed_dimension=16,rank=16,
                original_score=g,root_affinity_score=G,retention_benchmark=benchmark,
                query_data=records,relative_identity_residuals=errors,inequality_margins=margins)


def fixtures():
    rotation=np.cos(np.pi/8)*I-1j*np.sin(np.pi/8)*Y
    mixed=rotation@np.diag(np.sqrt([.9,.1]))@rotation.conj().T
    plus=rotation[:,0]; minus=rotation[:,1]
    vectors=np.column_stack([np.kron(plus,plus),np.kron(minus,minus)])
    equality=(vectors*np.sqrt([.9,.1]))@vectors.conj().T
    singular_vectors=np.zeros((4,2),complex)
    singular_vectors[0,0]=1
    singular_vectors[1,1]=1/R2; singular_vectors[2,1]=1j/R2
    singular=(singular_vectors*np.sqrt([.75,.25]))@singular_vectors.conj().T
    pure=np.array([1,1j])/R2
    zero=np.outer(pure,pure.conj())
    return [("mixed_bisector_lambda_one_tenth",mixed,1,"mixed"),
            ("nonflat_spectral_blocks_same_profile",equality,2,"equality"),
            ("complex_singular_seed_with_zero_extension",singular,2,"singular"),
            ("pure_Y_zero_compressed_queries",zero,1,"zero")]


def fixture_case(name,root,n,kind):
    errors,margins={},{}
    compare(errors,"Hermitian_root",root,root.conj().T)
    compare(errors,"normalized_root",np.trace(root@root),1)
    eigenvalues,eigenvectors=np.linalg.eigh(root)
    nonnegative(margins,"positive_root",eigenvalues[0])
    keep=eigenvalues>TOL
    V=eigenvectors[:,keep]
    S=np.diag(eigenvalues[keep]).astype(complex)
    rank=int(sum(keep))
    records=[]
    for site in range(n):
        for axis,Ulocal in [("X",X),("Z",Z)]:
            U=np.ones((1,1),complex)
            for j in range(n):
                U=np.kron(U,Ulocal if site==j else I)
            B=V.conj().T@U@V
            label=f"site{site}_{axis}"
            record=query_gap(S,B,label,errors,margins)
            compare(errors,label+"_ambient_affinity",record["a"],np.trace(root@U@root@U))
            compare(errors,label+"_ambient_original",record["F"],sum(np.linalg.svd(root@U@root,compute_uv=False)))
            if kind=="mixed":
                for key,expected in [("a",4/5),("b",76/85),("commutator_gap",36/425),("Cauchy_gap",3/85)]:
                    compare(errors,label+"_exact_"+key,record[key],expected)
                compare(errors,label+"_original_squared",record["F"]**2,17/25)
            if kind in ["equality","zero"]:
                compare(errors,label+"_gap_zero",record["a"],record["F"]**2)
                compare(errors,label+"_compressed_constant_modulus",B@B,record["F"]**2*np.eye(rank))
                compare(errors,label+"_spectral_commutation",B@(S@S)-(S@S)@B,np.zeros((rank,rank)))
            if kind=="equality":
                # Both positive eigenvalues are simple; every flat spectral block
                # is a pure state with exactly the same query profile.
                for index in range(rank):
                    compare(errors,label+f"_block{index}_same_profile",abs(B[index,index]),record["F"])
            if kind=="zero":
                compare(errors,label+"_zero_query",B,np.zeros((rank,rank)))
                require(record["zero_extension_dimension"]==rank,"zero query extension covers support")
            records.append(record)
    if kind=="singular":
        require(rank==2 and len(root)==4,"complex singular rank")
        require(np.linalg.norm(root.imag)>.01,"genuinely complex singular fixture")
        require(any(record["zero_extension_dimension"]>0 for record in records),"singular optimal query exercises unitary extension")
    g=float(sum(record["F"] for record in records)); G=float(sum(np.sqrt(max(0.,record["a"])) for record in records))
    if kind=="equality":
        compare(errors,"all_queries_pure_spectral_block_bound",g,n*R2)
    return dict(name=name,ambient_qubits=n,ambient_dimension=len(root),compressed_dimension=rank,rank=rank,
                original_score=g,root_affinity_score=G,query_data=records,
                relative_identity_residuals=errors,inequality_margins=margins)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    source=Path(__file__).resolve(); repository=source.parents[1]; note=repository/NOTE
    if args.output:
        destination=args.output.resolve()
        if destination in [source,note.resolve()] or destination.suffix!=".json":
            raise ValueError("Output must be JSON and cannot overwrite source or proof note")
    exact,intervals=exact_checks()
    records=[star_case()]+[fixture_case(*case) for case in fixtures()]
    report=dict(status="exact finite comparisons and fixed constructions passed",research_base=BASE,
                python=platform.python_version(),numpy=np.__version__,tolerance=TOL,
                source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                proof_note_sha256={NOTE:hashlib.sha256(note.read_bytes()).hexdigest()},
                exact_comparisons=exact,exact_score_gap_intervals=intervals,constructions=records,
                maximum_matrix_dimension=16,
                scope="Exact stdlib Fraction/isqrt comparisons certify only the finite fifteen-input rank-16 star's surrogate violation and original-score nonviolation, plus rational mixed-bisector gap identities. Thirty original star queries are represented by their 16-by-16 support compressions; no 32768-by-32768 matrix is constructed. Four fixed 2-by-2 and 4-by-4 fixtures check the optimal-decoder gap, unitary zero extensions, compressed equality conditions and identical spectral-block query profiles. The asymptotic method limit is analytical in the proof note; no asymptotic numerical claim is tested here. Floating-point construction checks are not interval certificates. No random sampling, grid, optimization or novelty claim.")
    residuals=[value for row in records for value in row["relative_identity_residuals"].values()]
    margins=[value for row in records for value in row["inequality_margins"].values()]
    report.update(exact_comparison_count=len(exact),fixed_construction_count=len(records),
                  query_count=sum(len(row["query_data"]) for row in records),matrix_identity_count=len(residuals),
                  inequality_count=len(margins),maximum_relative_identity_residual=max(residuals),
                  minimum_inequality_margin=min(margins))
    encoded=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(encoded)
    print(encoded,end="")


if __name__=="__main__":
    main()
