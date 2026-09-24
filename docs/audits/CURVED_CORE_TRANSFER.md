# Curved transfer closes the larger-tail high-score strip

Date: 2026-09-24. Reviewed main:
`3964f9b97766463a2aff65233560c9dcdf60c297` (PR #26).
Reviewed tree: `0bdb23c6045674fc4d0c2b18d5119e095d531196`.

**Status:** supplied analytical deductions and an exact scalar certificate,
independently reconstructed within this workspace. This is not external
peer review, unrestricted optimality, or a publication-originality claim.
The historical [proof audit](PROOF_AND_NOVELTY_AUDIT.md) is unchanged.

## 1. Theorem and operational scope

For an arbitrary complex two-qubit state, let

$$
g(\rho)=\sum_{U=X_A,Z_A,X_B,Z_B}\|\sqrt\rho U\sqrt\rho\|_1,
\qquad D_\rho=2\sqrt2+(2-\sqrt2)S(\rho)-g(\rho).
$$

Entropy is in bits. Order the eigenvalues, put `e=lambda_3+lambda_4`, and
let sigma be the normalized top-two spectral restriction.

**Theorem.** If `g(sigma)>13/4` and `0<e<=1/29`, then `D_rho>0`.

The previous [small-tail theorem](EXTENDED_CORE_TRANSFER.md) covered
this score threshold through `e<=1/99`. The present proof closes the
remaining interval `[1/99,1/29]`. Together with the existing
[spectral-tail gate](TWO_QUBIT_SPECTRAL_TAIL_GATE.md), any two-qubit
entropy counterexample must therefore have `g(sigma)<=13/4`.
The low-score-core case and the all-size inequality remain unresolved.

All decompositions concern virtual normalized seeds. The physical model
still has one arbitrary unknown specimen, one delayed local query,
unrestricted collective encoding, unlimited finite classical records,
worst-case retained quantum dimension, and error uniform over inputs
and queries. No physical projection, postselection, extra specimen,
joint execution of decoders, or average-memory convention is introduced.

## 2. Existing geometric inputs

Write `rho=q sigma direct-sum e tau`, `q=1-e`, and use

$$
s=\sqrt2,\quad c=2-s,\quad p=1-m\ge m>0,\quad\kappa=p/m,
\quad g_a=\sqrt{4-2(1-2m)^2},\quad G=s+g_a.
$$

Define `d=G-g(sigma)>=0`, `delta=2s+c h_2(m)-G>=0`. The
[rank-two theorem](../ENTROPY_INEQUALITY_BOUNDARIES.md) proves these
signs and `D_tau>=0`. The decoder classification in
[EXTENDED_CORE_TRANSFER.md](EXTENDED_CORE_TRANSFER.md) gives one active
site A and two scalar decoders at B. Let `f_A,f_B` denote the two site
scores and set

$$
\xi=s-f_B(\sigma),\quad L=g_a-f_A(\sigma),\quad d=\xi+L.
$$

Let `u` be the larger squared principal-angle sine between
`P=supp(sigma)` and its signed B-bisector subset support. That report
proves `m>7/32`, `u<1/10`, and

$$
\xi\ge2smu,\qquad d\ge mB(m)u,\qquad
B(m)=2s+\frac{2s\kappa}{2s\kappa+1},\qquad d<G-13/4.
\tag{1}
$$

In particular all active compressions are invertible, while the signed
scalar-query compressions are positive on P and negative on Q=I-P.
Set `d_0=max{mB(m)u,2smu+L}`; every actual state has `d>=d_0`.
This is a relaxation, not an assertion that its extremal scalar values
come from a physical state.

## 3. Keep the two scalar-query endpoints together

Put

$$
r_0=1-2u,\quad t_0=2\sqrt{u(1-u)},\quad
\ell=(r_0-t_0)/s,\quad h=(r_0+t_0)/s,
$$
$$
H_t(a,b)=\sqrt{(a-b)^2t^2+4ab}-(a+b)t.
$$

The finite-tail scalar-site gain obeys

$$
\boxed{f_B(\rho)-qf_B(\sigma)-ef_B(\tau)
\le H_\ell(q,e)+H_h(q,e)=:\mathcal B(e,u).}
\tag{2}
$$

**Paired-mode reduction.** For either signed scalar query use its
cosine-sine representation `U=[[T,S],[S,-T]]`, with
`T=diag(t_1,t_2)>0` and `S=sqrt(I-T^2)`. Pinching into its two paired
P/Q modes commutes with U. Root-fidelity monotonicity therefore bounds
the original fidelity above by the pinched one. In mode j put
`a_j=q<j|sigma|j>`, `b_j=e<j|tau|j>`. Its exact contribution is
`sqrt((a_j-b_j)^2t_j^2+4a_jb_j)`. The core and tail contributions are
`a_j t_j` and `b_j t_j`; definiteness makes them linear and unchanged
by pinching. Thus the excess is at most `sum_j H_{t_j}(a_j,b_j)`.
Unequal spectra and complex within-support coherence are retained.

**Endpoints.** For a unit vector in P, expectations r,z of the signed
bisector and its perpendicular satisfy `r>=r_0` and `r^2+z^2<=1`.
Since `r_0>4/5>1/sqrt(2)`, both `(r+z)/s` and `(r-z)/s` belong to
`[ell,h]`: `r-sqrt(1-r^2)` increases, while `r+sqrt(1-r^2)` decreases
on this range. Hence all t_j for both queries belong to that interval.
The Q statement follows with reversed signs.

**Chord and concavity.** The function H is convex in t:

$$
\partial_t^2H_t=\frac{4ab(a-b)^2}{[(a-b)^2t^2+4ab]^{3/2}}\ge0.
$$

It is jointly concave and homogeneous in a,b: with z=(a-b)/(a+b), it
is the perspective of `sqrt(1-(1-t^2)z^2)-t`, a concave function of z.
Apply the endpoint chord in t to all four modes of the two queries;
then homogeneous concavity bounds their sum by

$$
H_\ell(A,B)+H_h(2q-A,2e-B),\quad
A=\frac{q(2h-f_B(\sigma))}{h-\ell},\quad
B=\frac{e(2h-f_B(\tau))}{h-\ell}.
$$

Both site scores lie in `[s r_0,s]`, so `0<=A<=q` and `0<=B<=e`.
The partial derivatives H_a,H_b decrease with t. For completeness,
when a>=b>0 put z=(a-b)/(a+b) and
`x=t(a-b)/sqrt((a-b)^2t^2+4ab)`, so `0<=x<=z<=1`. Directly,

$$
H_{at}=x\left[1+\frac{1-x^2}{1+z}\right]-1
\le z(2-z)-1\le0.
$$

The bracketed product increases in x on `[0,z]`; its derivative is
at least `(2+z-3z^2)/(1+z)>=0`. For a<b the differentiated root term
is negative, giving H_at<0 directly; symmetry handles H_bt.
Concavity's tangent at `(A,B)=(q,e)` thus has nonnegative gradient,
and `(A-q,B-e)` is nonpositive. This proves (2). Boundary cases and
u=0 follow by continuity. No singular tail inverse occurs.

For stable scalar evaluation set `b=4qe`, `W=1-8u+8u^2`. Since
`ell^2+h^2=1`, `ell h=W/2`, equation (2) becomes

$$
\mathcal B(e,u)=\sqrt{1+b+\sqrt{(1-b)^2W^2+4b}}-s(1-2u).
\tag{3}
$$

## 4. Active-site gain and the transfer certificate

For an invertible Hermitian matrix M, put `F=Tr|M|` and
`K=Tr(XX^dagger|M|^{-1})`. Weighted Hilbert--Schmidt Cauchy gives

$$
\operatorname{Tr}\sqrt{M^2+\alpha XX^\dagger}
\le\sqrt{F(F+\alpha K)}.
$$

Apply Cauchy to `Tr[|M|^(1/2)|M|^(-1/2)sqrt(M^2+alpha XX^dagger)]`;
the squared second factor is `F+alpha K`, by cyclicity of trace.
Apply this after the established
[coherent block-row bound](COHERENT_TRANSFER_AUDIT.md), then apply
Cauchy across the two active queries. With `f=g_a-L`, the result is

$$
f_A(\rho)-qf_A(\sigma)-ef_A(\tau)\le\mathcal A,
\quad\mathcal A=q\left[\sqrt{f^2+(4e/q)fK_A}-f\right],
$$
$$
K_A\le\min\left\{
\frac{2\sqrt\kappa(2-g_a+L)}{m\sqrt{1-4u}},
\frac{8\sqrt\kappa u}{\sqrt{1-4u}}\right\}.
\tag{4}
$$

The two K_A bounds are from
[TWO_QUBIT_CORE_STABILITY.md](TWO_QUBIT_CORE_STABILITY.md), Section 5;
their hypotheses hold at `u<1/10`. Use their minimum in (4), whose
right side increases with K_A. The exact orthogonal-mixture entropy
identity and `D_tau>=0` give

$$
-D_\rho\le T:=\mathcal A+\mathcal B-q(\delta+d_0)-c h_2(e).
\tag{5}
$$

The tail's entropy stays paired with its actual score. Thus T<0 is
a strict entropy certificate.

## 5. SLD retains the imbalance between the two sites

Let `a=f_A(rho)`, `b=f_B(rho)` and `S=4-E_*(lambda)`, where E_* is
the proved [exact SLD spectral minimum](../TWO_QUBIT_SLD_SPECTRUM.md).
The fidelity-SLD inequality and two two-term Cauchy inequalities give
`a^2+b^2<=2 sum_U F_U(rho)^2<=2S`. Homogeneous root-fidelity
concavity gives `a>=q f_A(sigma)+e f_A(tau)>=a_*=q(g_a-L)`.
Maximizing a+b on that quarter disk yields

$$
g(\rho)\le\Phi(S,a_*),\qquad
\Phi(S,a)=\begin{cases}2\sqrt S,&a\le\sqrt S,\\
a+\sqrt{2S-a^2},&a\ge\sqrt S.
\end{cases}
\tag{6}
$$

The physical domain has `a^2<=2S`. No joint-decoder assumption enters.

Write the tail spectrum as `((1+z)/2,(1-z)/2)` and y=e z^2. The
spectral relaxation in the earlier core report, Section 8, gives

$$
E_*\ge(1-2e)^2+q(1-2m)^2+y,\quad
S_0=4-(1-2e)^2-q(1-2m)^2.
$$

Also `h_2((1+z)/2)>=1-z^2`. The gap is therefore at most
`Phi(S_0-y,a_*)-2s-c[h_2(e)+q h_2(m)+e-y]`. On either branch,
`partial_S Phi` is at least `1/sqrt(S_0)` for S<=S_0: on the
imbalanced branch `2S-a_*^2<=S`. Integrate from zero to the actual y;
the whole path is feasible because `a_*^2<=2(S_0-y)` at its endpoint.
Then use `y<=e` and the positive part of the derivative upper bound.
The branch boundary is continuously differentiable; the outer disk
boundary is handled by continuity. This gives the tail-independent bound

$$
-D_\rho\le J:=\Phi(S_0,a_*)-2s-c[h_2(e)+q h_2(m)+e]
+e\max\{0,c-1/\sqrt{S_0}\}.
\tag{7}
$$

Thus J<0 is a second strict certificate. This step uses the spectral
ordering of the core and tail, explicitly retained in the theorem.

## 6. Exact scalar coverage

The [checker](../../tools/certify_curved_core.py) verifies `T<0` or
`J<0` throughout the closed relaxation

$$
1/99\le e\le1/29,\quad7/32\le m\le1/2,\quad
0\le u\le1/10,\quad0\le L\le1/6,\quad d_0\le G-13/4.
\tag{8}
$$

Every physical state in the new strip lies here. In particular,
`L<=d<G-13/4<=sqrt(2)-5/4<1/6`. The spectral split is separated:
`qm>(28/29)(7/32)>e`, so the two tail eigenvalues lie below the core.

All endpoints are outward-rounded integers divided by `2^80`; square
roots use integer square root and entropy uses the previously audited
logarithm series. The two gains are rationalized algebraically to avoid
interval cancellation. For (6), the implementation uses monotonicity
in S and the decrease in a above sqrt(S). Closed children cover their
entire parent. Every accepted nonempty leaf has a strictly negative
upper bound for T or J; exhausted budgets and unresolved leaves fail.
The [exact record](../../results/curved_core_certificate.json) has 10,647
visited boxes and 5,324 terminal leaves: 1,868 transfer, 2,898 SLD, and
558 empty. Maximum depth is 20. The minimum transfer and SLD margin
numerators are respectively `416550709650178248` and
`1311935999616578036`, with common denominator `2^80`.
Ordinary and optimized Python runs reproduce the same certificate.
This is a finite proof of the
scalar disjunction conditional on the analytical reductions above;
it does not infer a theorem from sampled states.

Equations (5), (7), (8), together with the already proved interval
`e<=1/99`, establish the stated theorem through `e<=1/29`.

## 7. Ingredients and remaining boundary

Root-fidelity monotonicity and concavity, cosine-sine decomposition,
Cauchy inequalities and the spectral SLD ingredients are established
tools; their source comparisons are in the linked prior reports.
The finite scalar-pair transfer, the imbalanced use of SLD, and their
combination above are supplied deductions, not claims of priority.
The full two-parameter formation-profile novelty comparison remains
open. No new all-size entropic or squashed-entanglement converse is
asserted, and cores with score at most 13/4 remain outside this theorem.
