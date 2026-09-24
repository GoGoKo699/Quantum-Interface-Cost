# A simpler decoder proof and an extended small-tail theorem

Date: 2026-09-24. Reviewed main:
`449984f346ed396f515c885cb0c5921cb7739735` (PR #25).
Reviewed tree: `9ee1a7d345d3fc574791cbf36cba90481dce1407`.

**Status:** supplied analytical deduction, independently reconstructed
within this workspace, with an optional exact one-variable certificate.
Not external peer review, unrestricted optimality, or publication originality.
This continues the historical [proof audit](PROOF_AND_NOVELTY_AUDIT.md)
without rewriting it.

## 1. Result and its limits

For a complex two-qubit density matrix define

$$
g(\rho)=\sum_{U=X_A,Z_A,X_B,Z_B}\|\sqrt\rho U\sqrt\rho\|_1,
\qquad \Delta(\rho)=2\sqrt2+(2-\sqrt2)S(\rho)-g(\rho).
$$

Entropy is in bits. Let
`rho=(1-epsilon)sigma direct-sum epsilon tau`, where the normalized
core and tail have orthogonal supports of dimension at most two.

**Theorem.** If `g(sigma)>13/4` and `0<epsilon<=1/99`, then
`Delta(rho)>0`. A wholly elementary proof gives the same conclusion
through `epsilon<=1/201`; the improvement to `1/99` uses a 97-leaf exact
scalar certificate, not a simulation of density matrices.

For the spectral application take sigma to be the normalized top-two
eigenspace restriction and epsilon the bottom-two eigenvalue sum. This
adds a genuine exclusion when `13/4<g(sigma)<=10/3`. It does **not**
replace the earlier [high-score theorem](TWO_QUBIT_CORE_STABILITY.md)
on its entire interval `epsilon<=1/29`. That theorem still applies
through `1/29` when `g(sigma)>10/3`.

Thus, in addition to all earlier necessary conditions, a remaining
two-qubit entropy witness must satisfy

$$
\epsilon\le1/99\quad\Longrightarrow\quad g(\sigma)\le13/4.
$$

Neither the full two-qubit inequality nor its all-n analogue is proved.
The original task still has one unknown specimen, one delayed local
query, unrestricted collective encoding, unlimited finite classical
records, worst-case quantum dimension, and error uniform in input and
query. Core/tail decomposition is a virtual-seed proof device. It adds
no input promise, copies, postselection, average-memory convention,
joint-decoder requirement, quantum bypass, or preshared entanglement.

## 2. The decoder threshold needs only three anticommuting sets

This gives a shorter, weaker alternative to the existing
[sharp operator envelope](MIXED_DECODER_PATTERN_BOUND.md). For a mixed
scalar/traceless inactive site, its canonical Hamiltonian is

$$
H=aX_AX_M+bZ_AZ_M+X_B+Z_B(xX_M+yY_M+zZ_M),
\quad 0\le a\le b,\quad a^2+b^2=2,\quad x^2+y^2+z^2=1.
$$

Set `B_1=X_A X_B X_M`, `B_2=Z_A X_B Z_M`, `D=X_A Z_B`,
`E=Z_A Z_B`, and `R=B_1 B_2=-Y_A Y_M`. Direct multiplication gives

$$
H^2=4I+2K,\qquad K=abR+aB_1+bB_2+axD+bzE.
$$

In any state write the five expectations as `u,v,r,s,t`, respectively
for `B_1,B_2,R,D,E`. Each of
`{B_1,D}`, `{B_2,E}`, `{R,D,E}` anticommutes internally. The established
expectation bound gives

$$
u^2+s^2\le1,\quad v^2+t^2\le1,\quad r^2+s^2+t^2\le1,
\quad u^2+v^2+r^2+2s^2+2t^2\le3.
$$

Apply `2pq<=p^2+q^2` to the vectors
`(u,v,r,sqrt(2)s,sqrt(2)t)` and
`(a,b,ab,ax/sqrt(2),bz/sqrt(2))`. Since `x^2+z^2<=1` and `a<=b`,

$$
\begin{aligned}
\langle K\rangle
&\le\tfrac12[3+a^2+b^2+a^2b^2+(a^2x^2+b^2z^2)/2]\\
&\le3+\tfrac34a^2-\tfrac12a^4
=\tfrac{105}{32}-\tfrac12(a^2-\tfrac34)^2\le\tfrac{105}{32}.
\end{aligned}
$$

Therefore `H^2<=169I/16` and `||H||<=13/4`. Arbitrary complex decoder
directions remain included: no planar assumption was made. The zero-
and two-active-site cases have the prior rank-two bound `2sqrt(2)`.
Consequently a core above `13/4` has exactly one active site A and two
scalar decoders at B.

**Prior ingredient, not a new uncertainty principle.** Kurzyński et al.,
*Correlation complementarity yields Bell monogamy relations*,
[arXiv:1010.2012v2](https://arxiv.org/html/1010.2012v2), 19 May 2011,
Eq. (1), printed p. 2, supplies the squared-expectation inequality;
pp. 2–3 supply its use by grouping Pauli correlations. All our operators
are Hermitian Pauli involutions, traceless and trace-orthogonal. Apply
the source inequality separately to each set and add: overlap between
sets is harmless. The particular rational bound above is a supplied
corollary. The earlier sharp envelope's priority is not established.

## 3. Keep the stronger angle inequality

Use `s=sqrt(2)`, `c=2-s`, core spectrum `p=1-m>=m>0`, and

$$
G_{\rm act}=\sqrt{4-2(1-2m)^2},\quad G=s+G_{\rm act},\quad
d=G-g(\sigma),\quad \delta=2s+c h_2(m)-G,\quad \kappa=p/m.
$$

The prior [rank-two spectrum theorem](../ENTROPY_INEQUALITY_BOUNDARIES.md)
gives `d,delta>=0` and `Delta(tau)>=0`. A rank-one core cannot have the
required score. Let `P=supp(sigma)` and let `P_*` be A tensored with the
positive signed-bisector state at B. Let `u>=v` now denote the squared
principal-angle sines between P and P_*; the expectations from Section 2
are no longer in use. Put `xi=s-f_B`, `L=G_act-f_A`. The earlier
[core proof](TWO_QUBIT_CORE_STABILITY.md), Section 4, gives

$$
d=\xi+L,\quad \xi\ge2s(mu+pv),\quad
L\ge m(1-q^2),\qquad q=\cos(\alpha-\beta),
$$

where `alpha=arcsin(sqrt(u))`, `beta=arcsin(sqrt(v))`. Its prior
Cheng–Hall input, 1610.09302v3 Eqs. (10), (14), applies to the **core's**
pure three-qubit purification, not to a purification of the full rho.

For `0<=beta<=alpha<=pi/2`,
`sin(alpha-beta)>=sin(alpha)-sin(beta)`: the common factor is
`2sin((alpha-beta)/2)`, and
`cos((alpha-beta)/2)>=cos((alpha+beta)/2)`. Therefore

$$
\boxed{L\ge m(\sqrt u-\sqrt v)^2.}
$$

The earlier extra factor `1-u` was unnecessary. Minimize the resulting
quadratic over all real sqrt(v), a safe relaxation, to obtain

$$
d\ge mu B(m),\qquad B(m)=2s+\frac{2s\kappa}{2s\kappa+1}>7/2.
\tag{1}
$$

The last comparison follows from `kappa>=1` and `17>12sqrt(2)`.

## 4. An elementary angle cutoff protects every inverse

High score implies `m>7/32`, because G increases on `[0,1/2]` and
`G(7/32)=s+sqrt(431/128)<13/4`. The comparison follows from
`s<1177/832`, certified by `1177^2-2*832^2=881>0`. Hence `kappa<25/7`.

Write `R(m)=G(m)-13/4`, `U(m)=R(m)/(mB(m))`, and `r=1-2m`.
Since `d<R`, (1) gives `u<U`. Concavity gives
`R<=s-5/4-r^2/2`. For `D=2s(1+r)+1-r>0`, direct expansion of
`20D[mB(m)/10-(s-5/4-r^2/2)]` gives

$$
P(r)=(34s-47)+(66s-105)r+(20s+2)r^2+(20s-10)r^3.
$$

Using `s>140/99` and `r>=0`, bound its coefficients below by those of

$$
\begin{aligned}
Q(r)&=27/25-(35/3)r+30r^2+18r^3\\
&=18(r-1/6)^2(r+1/3)+30(r-61/360)^2+1123/21600>0.
\end{aligned}
$$

The coefficient gaps at `s=140/99` are
`2/2475,0,28/99,28/99`. Thus `U<1/10` and **u<1/10**.
Active compressions have least singular value at least
`sqrt(1-4u)>sqrt(3/5)`. Scalar-site compressions are definite because
`1-2u>2sqrt(u(1-u))`; at `u=1/10` these sides are `4/5` and `3/5`.

## 5. Transfer the core deficit to the full seed

With `Q=I-P`, define on P

$$
C_U=\sqrt\sigma\,|\sqrt\sigma PUP\sqrt\sigma|^{-1}\sqrt\sigma,
\qquad K=\sum_U\operatorname{Tr}(\tau QUP C_U PUQ).
$$

All inverses exist by Section 4. The block Schur estimate and exact
orthogonal-support entropy identity from the earlier proof give

$$
\Delta(\rho)\ge(1-\epsilon)(\delta+d)+c h_2(\epsilon)-2\epsilon K.
\tag{2}
$$

Here the tail's entropy and score remain paired via `Delta(tau)>=0`.
Section 5 of that proof gives the finite-angle bounds

$$
K_A\le\frac{8\sqrt\kappa\,u}{\sqrt{1-4u}},\qquad
K_B\le A(u)=s(1-2u)\left[\frac2{1-8u+8u^2}-1\right].
\tag{3}
$$

Their derivations require only `u<1/4` and the scalar definiteness
condition, respectively, not the earlier final cutoff `u<1/20`.
In particular the scalar inverse sum retains its cancellation before
being bounded; no Taylor remainder is dropped.

Set, continuously at zero,

$$
J(u)=\frac{A(u)-s}{u}=
\frac{s(14-32u+16u^2)}{1-8u+8u^2}.
$$

Its derivative has positive numerator `16s(5-12u+8u^2)` on `[0,1/10]`.
Thus `J(u)<=J(1/10)=274s/7<56`. Also
`8sqrt(kappa)/sqrt(1-4u)<40sqrt(5/21)<20`. Equations (1), (3) imply

$$
K-s\le76u\le\frac{4864}{49}d\le100d,
\qquad
\Delta(\rho)\ge c h_2(\epsilon)-2s\epsilon+(1-201\epsilon)d.
$$

Keep weak inequalities: `d=u=0` permits `K=s`. For
`epsilon<=1/201`, the d coefficient is nonnegative, while
`h_2(epsilon)/epsilon>log_2(201)>7` and `7c-2s=14-9s>0`.
This proves the elementary theorem.

## 6. Optional exact one-variable sharpening

Retaining the m dependence instead gives

$$
K-s\le C(m)d,\qquad
C(m)=\frac{J(U(m))+8\sqrt\kappa/\sqrt{1-4U(m)}}{mB(m)}.
$$

Where `R<0`, the high-score hypothesis is impossible. The
[checker](../../tools/certify_extended_core.py) safely replaces R by
its positive part and encloses the entire larger interval
`m in [7/32,1/2]`. It certifies `U<1/10` and `C(m)<49`.
Monotonicity justifies evaluating J and the active denominator at an
upper endpoint for U. Every arithmetic endpoint is an integer divided
by `2^80`, rounded outward; unresolved intervals raise an exception.

The [record](../../results/extended_core_certificate.json) has 97 accepted
leaves, maximum depth 8, minimum angle-margin numerator
`22610467235550810200`, and minimum C-margin numerator
`14480460893618248359602`, with denominator
`1208925819614629174706176`. Normal and optimized Python runs agree.
This certifies the scalar inequality conditional on the analytical
reduction, not unrestricted optimality or novelty.

Consequently `K-s<=49d` and (2) gives

$$
\boxed{\Delta(\rho)\ge c h_2(\epsilon)-2s\epsilon
 +(1-99\epsilon)d>0,\qquad 0<\epsilon\le1/99.}
$$

Strict positivity follows from
`h_2(epsilon)/epsilon>log_2(99)>6` and `6c-2s=12-8s>0`.

## 7. What remains open

The larger-tail strip for newly admitted cores is not handled. The last
relaxed scalar lower bound is already negative at
`m=1/2,d=1/8,epsilon=1/29`: dropping or retaining delta is identical
there, and `h_2(1/29)<1/2` bounds it above by
`(81-66sqrt(2))/116<0`. For the entropy comparison, monotonicity gives
`h_2(1/29)<h_2(1/16)<3/8`, using `ln(16/15)<1/15` and `ln(2)>1/2`.
This is a limitation of the estimate, **not** a
physical entropy counterexample; flat-core states are separately covered.
One cannot substitute `13/4` for `10/3` in the older certificate.

The prospective global coherent-transfer inequality still lacks a proof:
the four core decoder compressions are contractions, and replacing them
by extreme reflections discards the cross-block budget. A sharp finite-
tail argument must control that shared geometry. Even closure for n=2
would not establish the required all-n entropy inequality.

The short anticommutation method is an established prior ingredient;
the improved angular estimate and the stated finite-tail exclusion are
supplied deductions. Neither certifies priority of the full two-parameter
formation evaluation. The unresolved source comparisons in the
[literature ledger](../LITERATURE_COMPARISON.md) remain open. No new
entropic or squashed-entanglement converse is claimed in this continuation.
