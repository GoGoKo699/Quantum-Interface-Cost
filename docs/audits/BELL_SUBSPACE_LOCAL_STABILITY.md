# Bell-subspace local stability in every subsystem direction

**Reviewed main:** `6612c8fb66eed17be00b4df12b74663236e7a86e`, the merge
of PR #39. **Date:** 2026-09-24.
**Status:** analytic local converse, independently reconstructed inside
the audit workspace; no global optimum or publication-priority claim.
LICENSE and the historical [proof and novelty audit](PROOF_AND_NOVELTY_AUDIT.md)
are preserved.

The known configurations attaining the Bell-projector sum `5/2` are
strict local maxima in **all eighteen subsystem directions**, after
removing exact unitary equivalences. This excludes an actual open
neighborhood around the configurations with two queries on one memory
qubit and the third on its complementary qubit. It goes beyond the
special continuous families in the
[previous report](NONCOMMUTING_QUERY_FAMILIES.md).

The exact second-order loss is

$$
\frac16\|g\|_F^2+\frac8{15}\|h-g/2\|_F^2.
$$

A controlled remainder proves a finite neighborhood, not just a
negative Hessian. The general inequality for three independently
arbitrary subsystem embeddings remains unproved. This report neither
classifies all global maximizers nor says that every nearly optimal
configuration must be near the known configurations.

## 1. The theorem and its coordinates

Let `Q=A tensor B`, where A and B are qubits, and let R1,R2,R3 be three
distinct reference qubits. With spectator identities understood, set

$$
P_1=\Phi^-_{R_1A}\otimes I_B,\qquad
P_2=\Phi^-_{R_2A}\otimes I_B,\qquad
P_3=\Phi^-_{R_3B}\otimes I_A,
\qquad K_0=P_1+P_2+P_3,
$$

where `Phi^-` denotes the singlet projector. For real 3-by-3 matrices
g,h, define memory interaction generators

$$
G=\sum_{a,b=x,y,z}g_{ab}\sigma_a^A\sigma_b^B,\qquad
J=\sum_{a,b=x,y,z}h_{ab}\sigma_a^A\sigma_b^B,
\qquad r^2=\|g\|_F^2+\|h\|_F^2,
$$

and

$$
K(g,h)=P_1+e^{iG}P_2e^{-iG}+e^{iJ}P_3e^{-iJ}.
\tag{1}
$$

The Pauli matrices have eigenvalues `+/-1`; the generator convention
contains no additional factor of one half.

**Theorem.**

$$
\boxed{r\le\frac1{1024}
\quad\Longrightarrow\quad
\lambda_{\max}K(g,h)\le\frac52-\frac{r^2}{16}.}
\tag{2}
$$

The same statement holds after a common memory unitary, independent
reference unitaries, and a permutation of the queries. These operations
generate the **known attainer orbit** from the displayed configuration.
They need not be physical operations performed by the protocol.
Section 5 proves that (1) includes every sufficiently nearby
configuration modulo these exact spectral equivalences. The radius
is conservative; no optimal robustness constant is asserted.

## 2. The top doublet and exact reduced resolvent

On R1,R2,A, the operator `A0=P1+P2` has eigenvalues 0, 1/2, 3/2 with
multiplicities four, two, two. Its spectral projectors are

$$
E_{3/2}=\frac23A_0^2-\frac13A_0,\qquad
E_{1/2}=-2A_0^2+3A_0,\qquad
E_0=I-E_{3/2}-E_{1/2}.
$$

P3 commutes with A0. The top eigenvalue of K0 is 5/2, its projector is
`P=E_(3/2)P3`, and its multiplicity is two. The next eigenvalue is 3/2,
so the spectral gap is one. A basis of the top doublet is the R3:B
singlet tensored with

$$
\begin{aligned}
\tau_+&=\sqrt{2/3}|00\rangle|1\rangle
       -( |01\rangle+|10\rangle)|0\rangle/\sqrt6,\\
\tau_-&=\sqrt{2/3}|11\rangle|0\rangle
       -( |01\rangle+|10\rangle)|1\rangle/\sqrt6.
\end{aligned}
$$

The first two tensor factors here are R1,R2 and the last is A.
The reduced resolvent at the top eigenvalue is

$$
R=E_0\left[\frac25(I-P_3)+\frac23P_3\right]
 +E_{1/2}\left[\frac12(I-P_3)+P_3\right]
 +E_{3/2}(I-P_3).
\tag{3}
$$

It satisfies `RP=0`, `||R||=1`, and `(5I/2-K0)R=I-P`.

## 3. Exact curvature in all eighteen directions

Expand along `K(tg,th)=K0+tD+t^2E+O(t^3)`, with

$$
D=i[G,P_2]+i[J,P_3],\qquad
E=-\frac12\bigl([G,[G,P_2]]+[J,[J,P_3]]\bigr).
$$

The first-order compression is zero. For the G term,
`[G,P2]=sum_ab g_ab [sigma_a^A,P2] sigma_b^B` and
`P3 sigma_b^B P3=0`. For the J term,
`P[J,P3]P=0` because `P3P=P`. Thus `PDP=0`.

The second-order effective operator on the top doublet is

$$
C=P(E+DRD)P.
\tag{4}
$$

This operator is scalar. Indeed, ordinary five-qubit spin reversal
`T=(iY)^(tensor 5) conjugation` preserves the initial singlet projectors
and has `T^2=-I`. Every interaction Pauli product on A,B is T-even;
antiunitarity consequently sends `K(tg,th)` to `K(-tg,-th)`.
Therefore C is a T-even Hermitian operator on a two-dimensional
Kramers space, where every such operator is scalar. This is an
algebraic symmetry of the base-point expansion, not an assumed common
antiunitary symmetry of arbitrary readouts.

Simultaneous rotations of R1,R2,A and independently of R3,B preserve
K0. The matrices g,h transform as two copies of the real `(3,3)`
representation of `SO(3) times SO(3)`. Its scalar quadratic invariants
are exactly `||g||_F^2`, `||h||_F^2`, and `<g,h>`: each pair of A
indices and each pair of B indices must be contracted with its
invariant rank-two tensor. Hence three coefficients determine (4).

For the representative interaction `Z_A Z_B`, direct Pauli algebra gives
the following scalar compressions:

| G,J | Direct term PEP | Resolvent term PDRDP | Total C |
|---|---:|---:|---:|
| Z_A Z_B, 0 | -2/3 | 11/30 | -3/10 |
| 0, Z_A Z_B | -1 | 7/15 | -8/15 |
| Z_A Z_B, Z_A Z_B | -5/3 | 41/30 | -3/10 |

Here each entry multiplies P. The coefficients can be obtained by hand
in a three-dimensional space. On R1,R2,A, use

$$
\tau=(2|001\rangle-|010\rangle-|100\rangle)/\sqrt6,\quad
s=(|010\rangle-|100\rangle)/\sqrt2,\quad
q=(|001\rangle+|010\rangle+|100\rangle)/\sqrt3.
$$

Their A0 eigenvalues are 3/2, 1/2, 0. Since `Z_B` sends the R3:B singlet
to a triplet, the resolvent denominators for the first-order vectors
are 1, 2, 5/2. Before their common factor i, those vectors are

$$
\begin{aligned}
a&=[Z_A,P_2]\tau
 =(-|001\rangle-2|010\rangle)/\sqrt6
 \quad\leftrightarrow\quad(0,-1/\sqrt3,-1/\sqrt2),\\
b&=Z_A\tau
 =(-2|001\rangle-|010\rangle-|100\rangle)/\sqrt6
 \quad\leftrightarrow\quad(-1/3,0,-2\sqrt2/3).
\end{aligned}
$$

Consequently

$$
\langle a,Ra\rangle=\frac{1/3}{2}+\frac{1/2}{5/2}
=\frac{11}{30},\qquad
\langle b,Rb\rangle=\frac19+\frac{8/9}{5/2}=\frac7{15},
\qquad \operatorname{Re}\langle a,Rb\rangle=\frac{2/3}{5/2}=\frac4{15}.
$$

For the direct terms, `PP2P=(3/4)P` and
`sum_a sigma_a^A P2 sigma_a^A=I-P2`. Rotational covariance and the
same doublet symmetry give each corresponding compression as `P/12`.
Thus the G contribution is `1/12-3/4=-2/3`. The J contribution is
`-1`, since `P3 J P=0` and `J^2=I` in this representative case.
This independently derives the table without numerical fitting.

Combining the coefficients yields

$$
\boxed{
C=-\left[\frac3{10}\|g\|_F^2+\frac8{15}\|h\|_F^2
-\frac8{15}\langle g,h\rangle\right]P
=-\left[\frac16\|g\|_F^2+\frac8{15}\|h-g/2\|_F^2\right]P.}
\tag{5}
$$

In each of the nine component pairs the coefficient matrix is
`(1/30)[[9,-8],[-8,16]]`. Subtracting `I/8` gives first principal
minor `7/40` and determinant `1/2880`, both positive. In particular,

$$
C\le-\frac{r^2}{8}P.
\tag{6}
$$

## 4. A finite radius from a controlled remainder

Write `Delta=K(g,h)-K0=D+E+F`. For an interaction generator, a signed
singular-value decomposition of its real coefficient matrix is
implemented by local qubit rotations. Thus
`||G||<=sqrt(3)||g||_F`, and likewise for J.
For a Hermitian generator L and an orthogonal projector V,
`||[L,V]||<=||L||`. Successive commutators and the integral Taylor
remainder therefore give

$$
\|\Delta\|,\|D\|\le\sqrt6\,r,\qquad
\|E\|\le3r^2,\qquad \|F\|\le2\sqrt3\,r^3.
$$

For example the third-derivative norm for one conjugated projector
is at most `4||L||^3`, and its remainder coefficient is `1/6`.
Unitary conjugation requires no exponential prefactor.

For `r<=1/100`, convenient rational consequences are

$$
\|\Delta\|,\|D\|\le\frac52r,\qquad
\|F\|\le\frac72r^3,\qquad
\|\Delta-D\|\le\frac{31}{10}r^2.
$$

Put `Q0=I-P` and `t=5/2-r^2/16`. On Q0, the operator
`tQ0-Q0KQ0` is strictly positive: its gap is at least
`1-(5/2)r-r^2/16`. Its inverse S, extended by zero on P, obeys

$$
\|S\|\le\frac{11}{10},\qquad \|S-R\|\le3r.
$$

The latter follows from the resolvent identity. These conservative
constants follow immediately from `r<=1/100` and the preceding gap.
Also `PKQ0=PDQ0+W`, with `||W||<=(31/10)r^2`. The error in replacing
the exact Schur response by `PDRDP`, including the top-block remainder
PFP, is at most

$$
\begin{aligned}
&\|D\|^2\|S-R\|+2\|D\|\|S\|\|W\|
 +\|S\|\|W\|^2+\|F\|\\
&\quad\le
\left(\frac{75}{4}+\frac{341}{20}
+\frac{10571}{100000}+\frac72\right)r^3
=\frac{3940571}{100000}r^3<40r^3.
\end{aligned}
$$

Using (6), the exact upper Schur block is bounded by

$$
PKP+PKQ_0SQ_0KP
\le\left(\frac52-\frac{r^2}{8}+40r^3\right)P.
$$

At `r<=1/1024`, `40r<=5/128<1/16`. The last expression is at most
tP, so the positive Schur-complement criterion proves (2). All
inverses are on a strictly positive complement; `r=0` is simply the
known equality configuration.

## 5. Why the theorem includes every nearby subsystem direction

First fix P1 by a common memory unitary. Near the displayed configuration,
the other two projectors are arbitrary memory-unitary images of an A
factor and a B factor, respectively. The real Lie algebra su(4) is the
direct sum of the six local Pauli generators and the nine interactions
`sigma_a^A sigma_b^B`. The inverse function theorem applied at the
identity gives the local analytic factorization

$$
U=e^{iG}(L_A\otimes L_B).
$$

The right local factor on the unused auxiliary qubit commutes with the
projector. Its other right local factor transfers to that projector's
own reference qubit. The references are distinct, so these transfers
are independent and preserve the spectrum of the sum. Every sufficiently
nearby triple is therefore equivalent to (1).

For a dimension check, a single memory-rotated Bell-subspace projector
has 12 real parameters: SU(4) modulo its three-dimensional auxiliary
SU(2). Three such projectors have 36. The known attainer orbit under
common SU(4) and three independent reference SU(2)'s has dimension
`15+9-6=18`; its six-dimensional stabilizer is simultaneous local A,B
rotation compensated on the references. The eighteen coefficients in
g,h are exactly transverse directions. Residual rotations act on those
coordinates as isotropy, rather than six additional directions to remove.

Thus the theorem excludes an open neighborhood of the known attainer
orbit. It does not infer closeness to that orbit from a measured score,
and it does not exclude a larger maximum elsewhere.

## 6. Physical readout consequence and operational quantifiers

Let `H=sum_i h_i`, where `h_i=X_i B_i+Z_i D_i` on three different
reference qubits and a four-dimensional memory. Assume each reflection
pair has two traceless Jordan blocks with the same nonnegative spectra
u_i,v_i, where

$$
u_i^2+v_i^2=4,\qquad 2\ge u_i\ge\sqrt2\ge v_i\ge0.
$$

Suppose its combined top Bell projectors are a triple covered by (2),
allowing the unitary and permutation freedoms stated there. Set
`w_i=u_i-v_i` and `w_min=min_i w_i`. The exact local caps are
`h_i<=v_i I+w_i P_i`. For any unit test vector, put `p_i=<P_i>`.
Then `p_i<=1` and `sum_i p_i<=5/2-r^2/16`. Subtracting the smallest
coefficient before applying these bounds gives

$$
\begin{aligned}
\langle H\rangle
&\le\sum_i v_i+\sum_i(w_i-w_{\min})
+w_{\min}\left(\frac52-\frac{r^2}{16}\right)\\
&\le4+\sqrt2-\frac{r^2}{16}w_{\min}.
\end{aligned}
$$

For the second line, the zero coefficient identifies the site contributing
`(u_i+v_i)/2<=sqrt(2)`; the other two contribute at most two each.
Conjugating all references by Y sends H to -H. Therefore

$$
\boxed{\|H\|\le4+\sqrt2-
\frac{r^2}{16}\min_i(u_i-v_i).}
\tag{7}
$$

The loss is strictly positive when `r>0` and every `u_i>v_i`.
Unequal spectra between sites are allowed. Equal spectra within each
site's two blocks and the local geometric hypothesis are real restrictions;
they cannot be imposed on an unrestricted optimum.

For any normalized complex seed L, vectorization gives its actual decoder
score as `s(L)=<<L|H|L>>`, with `||L||_F=1`. Thus (7) bounds the actual
score for every seed in the stated decoder class. The full trace-norm
score is bounded by this argument only when a score-attaining family of
optimal readouts satisfies those hypotheses.

For an arbitrary collective instrument, refine the classical record to a
Kraus index a, omit zero maps, and put

$$
p_a=\frac{\|K_a\|_F^2}{8},\qquad
L_a=\frac{K_a}{\|K_a\|_F},\qquad \sum_a p_a=1.
$$

These p_a are normalization weights, not asserted input-independent
outcome probabilities. If every branch's actual readouts satisfy the
theorem, branch-dependent coordinates and spectra are permitted, and
uniform contrast eta obeys

$$
6\eta\le\sum_a p_a s(L_a)
\le4+\sqrt2-\sum_a p_a\frac{r_a^2}{16}
\min_i(u_{a,i}-v_{a,i}).
$$

The task still uses one arbitrary unknown quantum specimen, exactly one
delayed original-site X/Z query, unrestricted collective encoding,
unlimited finite classical records, worst-case branch dimension four,
and uniform binary total-variation error `(1-eta)/2`. No postselected
success, additional copies, average-memory substitution or quantum
bypass is introduced. A seed alone remains insufficient for achievability;
a complete instrument is required.

## 7. An exact obstruction to an entropy shortcut

Allowing all CPTP ququart-to-qubit decoders defines optimized Bell-test
probabilities `F_i^CPTP`. The established conditional min-entropy identity
is

$$
2F_i^{\mathrm{CPTP}}=2^{-H_{\min}(R_i|Q)}.
$$

It relaxes the unitary-plus-discard decoder class. The desired relaxed
sum inequality would be `sum_i 2^(-H_min(R_i|Q))<=5`; the identity itself
does not prove that joint constraint.

In particular the plausible additive budget
`sum_i H_min(R_i|Q)>=-log_2(dim Q)` is false. On R1,R2,A set

$$
|\psi\rangle=(2|000\rangle+|101\rangle+|011\rangle)/\sqrt6,
\qquad
|\omega\rangle=|\psi\rangle_{R_1R_2A}\otimes|\Phi\rangle_{R_3B}.
$$

Recovering A for queries 1 and 2 gives Bell probabilities 3/4 each;
recovering B for query 3 gives one. The min-entropy identity consequently
implies

$$
\prod_i2^{-H_{\min}(R_i|Q)}\ge(3/2)^2\,2=9/2>4.
$$

No claim that these particular recoveries maximize every CPTP objective
is needed. Their sum is exactly 5/2: the example refutes the proposed
additive entropy budget, not the sought Bell-projector inequality.
Min/max-entropy duality leaves an additional rank-constrained joint
fidelity inequality to prove; replacing the objective by that entropy
notation does not settle unrestricted optimality.

## 8. Established ingredients and focused novelty comparison

**Individual recovery objective.** Zhao, *Maximally entangled states and
fully entangled fraction*, [PRA 91, 012310 (2015)](https://doi.org/10.1103/PhysRevA.91.012310),
[arXiv:1610.08147v1](https://arxiv.org/pdf/1610.08147v1), Eq. (17), p. 3,
already defines the relevant unequal-dimension fully entangled fraction.
At dimensions 4 and 2 its sum of two orthogonal Bell projectors is
`Phi tensor I_aux`, optimized by one memory unitary. It is exactly the
individual subsystem-recovery objective used here. That functional is
established; Eq. (17) supplies no joint three-reference stability bound.

**Subspace normal form.** Gour–Wallach, *Entanglement of Subspaces and
Error Correcting Codes*, PRA 76, 042309 (2007),
[arXiv:0704.0251v2](https://arxiv.org/pdf/0704.0251v2), Proposition 3 and
Corollary 4, pp. 3–4, provide the maximally entangled subspace normal
form and dimension bound. At `C^4 tensor C^2`, a maximal such subspace
has dimension two and is a Bell pair tensored with an auxiliary qubit
after a memory unitary. The geometric object is therefore prior work;
the present calculation concerns simultaneous perturbations of three
such objects sharing the same memory.

**Operational entropy identity.** König–Renner–Schaffner,
*The operational meaning of min- and max-entropy*,
[arXiv:0807.1338v2](https://arxiv.org/pdf/0807.1338v2), Theorem 2,
Eq. (32), p. 9, gives the identity used in Section 7. Its squared
Uhlmann fidelity is the Bell-test probability, and its optimization
allows all CPTP decoders. It supplies a relaxation of subsystem
decoding, not equality between those decoder classes or an additive
dimension budget. The counterexample in Section 7 is a supplied
deduction using this established identity.

**Local decay versus global rigidity.** Broadbent–Culf, *Rigidity for
Monogamy-Of-Entanglement Games*, ITCS 2023,
[Theorems 15–16](https://drops.dagstuhl.de/storage/00lipics/lipics-vol251-itcs2023/LIPIcs.ITCS.2023.28/LIPIcs.ITCS.2023.28.pdf),
pp. 13–15, establish exact and robust rigidity for a different game with
two separated players guessing one referee's basis outcome. Here we
prove quadratic decay in a known neighborhood. We do not infer that
every nearly optimal configuration is close to it. Those different
payoffs and quantifiers preclude a direct substitution; this comparison
does not establish priority for the local theorem.

Pauli algebra, spin addition, Kramers pairing, reduced-resolvent
perturbation, Schur complements and local Lie-group coordinates are
established ingredients. The supplied deductions are the full
eighteen-direction curvature (5), the controlled-radius converse (2),
its conditional physical consequence (7), and the false entropy-budget
counterexample. The source check is bounded and does not certify
exhaustive originality or PRL-level significance.

## 9. Verification, provenance and remaining scope

An independent internal reconstruction checked the exact coefficients,
Kramers argument, local coordinate coverage and controlled remainder,
including the three-dimensional hand calculation above. The coordinating
review checked the integrated argument and operational transfer. These
are workspace checks, not external peer review.

[The verifier](../../tools/check_subsystem_local_stability.py) checks
27 exact rational matrix identities on 32-dimensional operators,
five coefficient cases, and rational curvature/radius certificates.
Eight prescribed small constructions additionally evaluate the actual
perturbed operators, including complex memory interactions and the
possible cubic splitting of the top doublet. No optimizer is used.
[The recorded output](../../results/subsystem_local_stability.json)
includes Python 3.12.14, NumPy 2.3.5 and source SHA-256
`90650b9814d37964d3b89f969ea588677b5397bbd9dfae08711f57a885144d38`.
The continuous proof is Sections 2–5; finite construction checks
supplement it. See [REPRODUCIBILITY](../REPRODUCIBILITY.md) for the
coordinating rerun record.

The global independent-subsystem conjecture remains

$$
\sum_{i=1}^3U_i(\Phi_{R_iA}\otimes I_B)U_i^\dagger
\stackrel{?}{\le}\frac52I,
\qquad U_i\in U(4)\text{ independently arbitrary}.
$$

A remote violation or different equality configuration is not excluded.
Even a proof of this global projector statement would leave unequal
Jordan-block spectra outside the physical deduction of Section 6.
The three full signatures `(22)^2(11)`, `(22)^2(12)`, `(22)^3` remain
unresolved, as do unrestricted equal-accuracy optimality and publication
originality. The normalized-seed reduction and earlier entropic and
squashed-entanglement bounds are unchanged.
