# A sharp global support bound for two leading modes

**Research base:** main `5a9d0ae04ba0c3a8a782e39c9e853d934d30ed6b`.
**Date:** 27 September 2026.

For arbitrary four-dimensional memory readouts, the two greatest
eigenvalues of the earlier-query Hamiltonian satisfy the sharp bound
`U+m<=4sqrt(3)`. The proof uses the four original reference Pauli
operators directly. It also gives the exact support function for
unequally weighted queries and classifies every equal-weight attainer.
That entire equality class obeys a strict three-query norm bound.

**Status:** supplied analytical proofs, independently reconstructed
within this workspace. The fidelity--affinity comparison and Pauli
conjugation gap are established ingredients; the applications and
equality arguments are proved below. No publication-priority claim is
made. The unrestricted three-input converse remains open.

## 1. The squared support budget and sharp spectral bound

Let `R=R1 tensor R2`, let `dim Q<=4`, and write

```math
\mathcal A=\{X_1,Z_1,X_2,Z_2\},\qquad
H_0=X_1B_1+Z_1D_1+X_2B_2+Z_2D_2,
\quad -I\le B_i,D_i\le I.
\qquad\text{(1)}
```

Reference and memory tensor factors are implicit. For any rank-two
projector P on RQ, put `sigma=P/2` and

```math
C_A=\mathrm{Tr}_R[(A\otimes I_Q)\sigma].
```

**Theorem.** Without any marginal, symmetry or readout-algebra assumption,

```math
\boxed{\sum_{A\in\mathcal A}\|C_A\|_1^2\le3.}
\qquad\text{(2)}
```

Consequently the two greatest eigenvalues U,m of (1) obey

```math
\boxed{U+m\le4\sqrt3,\qquad m\le2\sqrt3.}
\qquad\text{(3)}
```

Indeed, trace-norm duality and Cauchy--Schwarz give
`Tr(PH_0)/2<=sum_A||C_A||_1<=2sqrt(3)`. Maximizing over P is the
Ky Fan variational principle. The balanced example reconstructed in
Section 4 has `U=m=2sqrt(3)`, so both constants in (3) are attained.
No reduction to reflection extremes is needed for the upper bounds.

## 2. Proof of the squared support budget

Purify sigma with a qubit E and let rho be the complementary state on
RE. Then

```math
\mathrm{rank}\rho\le4,\qquad
\mathrm{Tr}_R\rho=I_E/2.
\qquad\text{(4)}
```

Schmidt decomposition across `RE:Q` gives

```math
\|C_A\|_1=\|\sqrt\rho(A\otimes I_E)\sqrt\rho\|_1.
\qquad\text{(5)}
```

In Schmidt bases the two supported matrices are transposes, so the
identity includes singular rho. Write `S=sqrt(rho)`. Squared root
fidelity is bounded by affinity:

```math
\|SAS\|_1^2\le\mathrm{Tr}(SASA).
\qquad\text{(6)}
```

This is the established comparison recorded, with primary-source
attribution, in [STRONG_ENTROPIC_CONVERSE, Section 3](../STRONG_ENTROPIC_CONVERSE.md#3-root-fidelity-affinity-and-the-two-pauli-energy).
For completeness, Schatten Holder with exponents 4,2,4 gives

```math
\|\rho^{1/2}\tau^{1/2}\|_1
\le\|\rho^{1/4}\|_4
\|\rho^{1/4}\tau^{1/4}\|_2\|\tau^{1/4}\|_4
=\sqrt{\mathrm{Tr}(\sqrt\rho\sqrt\tau)}.
```

Take `tau=A rho A` to obtain (6).

The map `T(M)=sum_{A in mathcal A} A M A` has eigenvalue four on
the reference identity Pauli word, eigenvalue two on precisely the four
words in mathcal A, and eigenvalues at most zero on every other
reference Pauli word. Its Pauli expansion therefore gives

```math
\sum_A\mathrm{Tr}(SASA)
\le2\mathrm{Tr}S^2+
\frac12\mathrm{Tr}_E[(\mathrm{Tr}_R S)^2]
=2+\frac12\mathrm{Tr}_E[(\mathrm{Tr}_R S)^2].
\qquad\text{(7)}
```

It remains to use the flat marginal in (4). Diagonalize
`rho=sum_{j=1}^s lambda_j|u_j><u_j|` on its support, and put
`sigma_j=Tr_R|u_j><u_j|`. All overlaps `Tr(sigma_i sigma_j)` are
nonnegative, each sigma_j has trace one, and
`sum_j lambda_j sigma_j=I_E/2`. Arithmetic--geometric mean gives

```math
\begin{aligned}
\mathrm{Tr}_E[(\mathrm{Tr}_R S)^2]
&=\sum_{i,j}\sqrt{\lambda_i\lambda_j}
       \mathrm{Tr}(\sigma_i\sigma_j)\\
&\le\sum_{i,j}\frac{\lambda_i+\lambda_j}{2}
       \mathrm{Tr}(\sigma_i\sigma_j)\\
&=\sum_i\mathrm{Tr}(\sigma_i\rho_E)
=s/2\le2.
\end{aligned}
\qquad\text{(8)}
```

Equations (5)--(8) prove (2).

## 3. Exact support for arbitrary query weights

For `dim Q=4` and nonnegative weights `w=(w_1,...,w_4)`, in the order
`A=(X1,Z1,X2,Z2)`, let `H_w=sum_j w_j A_j B_j`. The exact answer is

```math
\boxed{\sup_{-I\le B_j\le I}
[\lambda_1(H_w)+\lambda_2(H_w)]
=2\max_{\substack{0\le t_j\le1\\\sum_jt_j^2\le3}}
\sum_jw_jt_j.}
\qquad\text{(9)}
```

The upper bound follows from (2), `||C_A||_1<=1`, and the same
Ky Fan argument. Here is an attainment construction for every sphere
point `sum_j t_j^2=3`. Choose

```math
\alpha_1^2=1-t_2^2,\quad\alpha_2^2=1-t_1^2,\quad
\alpha_3^2=1-t_4^2,\quad\alpha_4^2=1-t_3^2,
```

and, on RE, define

```math
F=(\alpha_1X_1+\alpha_2Z_1)Z_E
 +(\alpha_3X_2+\alpha_4Z_2)X_E,\qquad
\Pi=(I+F)/2,\qquad \rho=\Pi/4.
\qquad\text{(10)}
```

The four summands of F anticommute, their squared coefficients sum
to one, and F is traceless. Thus Pi has rank four and `rho_E=I_E/2`.
For a query A, let D be the opposite-axis summand of F at that site.
Then `AFA=F-2D`, `D^2=alpha_opp^2 I`, and
`{F,D}=2alpha_opp^2 I`. Hence

```math
(\Pi A\Pi)^2=(1-\alpha_{\rm opp}^2)\Pi=t_A^2\Pi.
\qquad\text{(11)}
```

Purifying rho with Q of dimension four produces a flat rank-two state
sigma on RQ with `||C_A||_1=t_A`. Choosing each `B_A=sign(C_A)`,
with arbitrary reflection completion on its kernel, attains its support.
A maximizer on the right of (9) can always be chosen on the sphere:
if its squared norm is less than three, every positive-weight coordinate
is already one, and zero-weight coordinates can be increased without
changing the objective. This also covers zero weights and zero
correlations. Thus (9) is an attained support formula, not only an
upper bound inferred from a selected family.

## 4. Every equal-weight attainer has the same decoder form

Suppose `U+m=4sqrt(3)` and choose P to span the two leading modes.
Every inequality above is then an equality; in particular

```math
\|C_A\|_1=\sqrt3/2\quad(A\in\mathcal A),\qquad s=4.
\qquad\text{(12)}
```

We first show that the complementary rho is flat. Equality in (8)
requires `Tr(sigma_i sigma_j)=0` whenever `lambda_i!=lambda_j`.
On a qubit this forces such marginals to be orthogonal pure states.
If two distinct eigenvalues occur, there are consequently exactly two
groups, each with a fixed orthogonal pure E marginal. Their multiplicities
must be 1 and 3: a group of size d has eigenvalue `1/(2d)` by (4), and
equal group sizes would give equal eigenvalues. In particular one E
diagonal block of S is proportional to a rank-one reference projector.
But equality in (7) permits only reference words
`I,X1,Z1,X2,Z2`. A positive rank-one two-qubit operator cannot lie in
their span: an operator there has eigenvalues
`a+-||b||+-||c||`, and positivity cannot make exactly three zero
unless the whole operator vanishes. This excludes the nonflat case.
Therefore

```math
\rho=\Pi/4,\qquad \mathrm{rank}\Pi=4,
\qquad\mathrm{Tr}_R\Pi=2I_E.
\qquad\text{(13)}
```

Equality in (7) and (13) imply

```math
F:=2\Pi-I=\sum_{A\in\mathcal A}A\otimes M_A.
\qquad\text{(14)}
```

The involution identity `F^2=I` forces the two M coefficients at each
site to commute, coefficients at different sites to anticommute, and
`sum_A M_A^2=I_E`. Thus the four full summands `F_A=A tensor M_A`
anticommute pairwise, and each `I_R tensor M_A^2` commutes with Pi.

Since rho is flat, equality in (6) is equality in the rank-four
trace-norm/Hilbert--Schmidt Cauchy bound. Equation (12) gives
`(Pi A Pi)^2=3Pi/4`. If F_D is the opposite-axis summand at the same
site, the same calculation as (11) gives

```math
(\Pi A\Pi)^2=\Pi-\Pi F_D\Pi
=\Pi-\Pi(I_R\otimes M_D^2)\Pi.
```

Commutation with Pi and its faithful marginal (13) therefore imply
`M_D^2=I_E/4`. A scalar coefficient `+-I_E/2` is incompatible with
cross-site anticommutation and the other nonzero coefficients. Hence
all M coefficients are traceless half-Paulis, parallel within each site
and orthogonal between sites. Up to signs of the original query axes
and an E unitary, the complementary reflection is exactly

```math
\boxed{F=\frac{(X_1+Z_1)Z_E+(X_2+Z_2)X_E}{2}.}
\qquad\text{(15)}
```

These sign changes can be absorbed into readout outcomes. No arbitrary
reference rotation has been treated as a symmetry of the fixed support
functional.

To reconstruct the physical readouts, now *rewrite coordinates* using
the reference bisectors
`Ztilde_i=(X_i+Z_i)/sqrt(2)` and
`Xtilde_i=(X_i-Z_i)/sqrt(2)`. In these coordinates
`F=(Ztilde_1 Z_E+Ztilde_2 X_E)/sqrt(2)`.
For `a,b in {+1,-1}`, let chi_ab have Bloch vector `(b,0,a)/sqrt(2)`.
Then Pi is the sum of the four projectors
`|ab><ab|_R tensor |chi_ab><chi_ab|_E`. A purification is

```math
|\Psi\rangle=\frac12\sum_{a,b}|ab\rangle_R|ab\rangle_Q
|\chi_{ab}\rangle_E.
\qquad\text{(16)}
```

All other purifications differ by a memory unitary. Choosing real phases
`chi_++=(c,s), chi_+-=(c,-s), chi_-+=(s,c), chi_--=(s,-c)`, with
`c=cos(pi/8),s=sin(pi/8)`, gives, for `Q=A tensor B`,

```math
C_{\widetilde Z_1}=Z_A/4,\quad
C_{\widetilde X_1}=X_A/(4\sqrt2),\quad
C_{\widetilde Z_2}=Z_B/4,\quad
C_{\widetilde X_2}=Z_AX_B/(4\sqrt2).
\qquad\text{(17)}
```

Each original-query correlation consequently has eigenvalues
`+-sqrt(3)/8`, each twice. It is invertible, so equality in trace-norm
duality forces its readout uniquely to be its sign. The original pairs
are therefore, up to the memory unitary and the sign choices above,

```math
\boxed{\begin{aligned}
B_1&=\sqrt{2/3}\,Z_A+X_A/\sqrt3,&
D_1&=\sqrt{2/3}\,Z_A-X_A/\sqrt3,\\
B_2&=\sqrt{2/3}\,Z_B+Z_AX_B/\sqrt3,&
D_2&=\sqrt{2/3}\,Z_B-Z_AX_B/\sqrt3.
\end{aligned}}
\qquad\text{(18)}
```

For an invertible Hermitian C, the optimizer of `Tr(CB)` over
`-I<=B<=I` is uniquely `sign(C)`: its diagonal entries are forced in
an eigenbasis of C, and positivity of `I+-B` then kills off-diagonal
entries. Thus (18) also classifies contraction attainers.

In bisector coordinates this is the previously constructed balanced
Hamiltonian

```math
H_0=\frac2{\sqrt3}(\widetilde Z_1Z_A+\widetilde Z_2Z_B)
+\sqrt{2/3}(\widetilde X_1X_A+\widetilde X_2Z_AX_B).
\qquad\text{(19)}
```

The first two Pauli words commute with each other and with the last
two; the last two anticommute. Their joint sectors give the spectrum

```math
\{+2\sqrt3\ (\times2),\ +2/\sqrt3\ (\times6),
  -2/\sqrt3\ (\times6),\ -2\sqrt3\ (\times2)\}.
\qquad\text{(20)}
```

In particular every attainer has `U=m=2sqrt(3)`, not merely this
average. Its entire head-to-memory channel is

```math
\Phi(\omega)=\sum_{a,b}\mathrm{Tr}(E_{ab}\omega)
|ab\rangle\langle ab|,\qquad
E_{ab}=\frac14\left[I+\frac{aZ_E+bX_E}{\sqrt2}\right].
\qquad\text{(21)}
```

The effects are positive, have rank one, and sum to I. This is the
square-POVM channel already obtained in
[TWO_MODE_RESOLVENT, Section 5](TWO_MODE_RESOLVENT.md#5-why-one-leading-mode-does-not-suffice-uniformly).

## 5. The whole equality boundary obeys a strict full norm bound

For any attainer (18), let `h_3=X_3 B+Z_3 D` with arbitrary Hermitian
contractions B,D on Q. Put

```math
u=2\sqrt3,\qquad \ell=2/\sqrt3,\qquad g=u-\ell=4/\sqrt3.
```

Its actual two-mode envelope is `H_0<=ell I+gP`. The positive-update
criterion in the [two-mode reduction](TWO_MODE_RESOLVENT.md#4-exact-four-by-four-schur-condition)
tests this envelope at `ell+t`, where t>2, by
`g(id tensor E)[(tI-h_3)^(-1)]<=I`; E is dual to (21).

The [exact last-query theorem](EXACT_LAST_QUERY_RESOLVENT.md#1-the-readout-elimination-theorem)
gives, for every pure memory vector v and `2<t<=3sqrt(2)`,

```math
\langle v|(tI-h_3)^{-1}|v\rangle
\le F(t)I_{R_3},\qquad
F(t)=\frac1{2(\sqrt{2t^2-4}-t)}.
\qquad\text{(22)}
```

To verify the range and expression, its pure-state formula is the maximum
of `1/(t-sqrt(2))` and
`f_a=(t-a)/(t^2-2ta+2a^2-2)` for `1<=a<=sqrt(2)`.
On the stated t interval, the maximum occurs at
`a=t-sqrt((t^2-2)/2)`, which lies in that a interval. Substitution
gives F(t); the endpoint `a=sqrt(2)` already includes the scalar branch.

Because (21) prepares orthogonal pure memory states and its positive
effects sum to I, (22) gives the complete matrix bound `K_t<=gF(t)I`.
Choose

```math
t_*=(2+2\sqrt5)/\sqrt3.
```

Here `2<t_*<3sqrt(2)`, since `t_*^2=(24+8sqrt(5))/3` lies strictly
between 4 and 18. Also
`sqrt(2t_*^2-4)-t_*=2/sqrt(3)`, so `gF(t_*)=1`. Therefore

```math
\boxed{\|H_0+h_3\|\le\frac{4+2\sqrt5}{\sqrt3}
<4+\sqrt2.}
\qquad\text{(23)}
```

The strict comparison already follows from this constant being less
than five: positive squaring reduces that assertion to `16sqrt(5)<39`,
certified by `1280<1521`, and `5<4+sqrt(2)`.

The Schur argument first bounds the largest eigenvalue of the envelope.
The original Hamiltonian is odd under `Y_1Y_2Y_3 tensor I_Q`, so its
spectrum is symmetric and the same bound controls its operator norm.
The constant in (23) is an **upper bound**; no attainment or optimality
claim for that constant is made. The intermediate bounds for different
pure memory states need not be simultaneously attainable.

## 6. The synthetic swap head fails in every reference orientation

The [compatibility obstruction](TWO_MODE_COMPATIBILITY_OBSTRUCTION.md)
uses the channel
`Phi_p(omega)=(1-p)I/2 tensor omega+p omega tensor I/2` at `p=1/20`.
Its displayed purification has complementary state

```math
\rho_{RE}=\frac{I+(1-2p)Z_1+
 2\sqrt{p(1-p)}X_1W_{R_2E}}8=\Pi/4,
\qquad\text{(24)}
```

Here `(1-2p)Z_1+2sqrt(p(1-p))X_1W` is a traceless reflection, which
verifies the flat-projector identity in (24). W is the swap. Every other
Stinespring isometry for this same channel with four-dimensional R is
related by a unitary on R. Expanding
`W=(I+X_2X_E+Y_2Y_E+Z_2Z_E)/2`, the three nonidentity E-Pauli
coefficients of `sqrt(rho)` are nonzero multiples of
`X_1X_2,X_1Y_2,X_1Z_2`. They are pairwise anticommuting reflections,
and remain so under any reference unitary.

If its support reached `2sqrt(3)`, equality in (7) would place each of
these conjugated reflections in
`L=span{X1,Z1,X2,Z2}`. But a reflection in L occupies only one site:
writing it as `A_1 tensor I+I tensor A_2`, its square has cross term
`2A_1 tensor A_2`, which forces one A_i to vanish. Anticommuting
reflections in L must occupy the same site, whose X/Z plane contains
at most two mutually orthogonal directions. Thus L cannot contain the
required anticommuting triple. For every `0<p<1` the support is
strictly below `2sqrt(3)` in every reference orientation. This excludes
all such realizations as an energy-`2sqrt(3)` physical head, while making
no assertion that every support-compatible head passes the resolvent.

## 7. Remaining regime and verification scope

The regime in which one leading mode cannot ensure a positive final
resolvent is now confined to

```math
2+\sqrt2\le m\le2\sqrt3,\qquad
m\le U\le4\sqrt3-m.
\qquad\text{(25)}
```

Strictly below `m=2+sqrt(2)`, that inverse is positive; this fact alone
does not prove its scalar test. At `U+m=4sqrt(3)`, Sections 4--5 classify
and control every actual head. They do not supply quantitative stability
away from that boundary or settle the interior two-mode test. All three
complete remaining reflection signatures and the unrestricted
three-input converse remain open.

There is nevertheless a qualitative uniform neighborhood of the equality
boundary: some `delta>0` satisfies

```math
U+m>4\sqrt3-\delta
\quad\Longrightarrow\quad
\|H_0+h_3\|<4+\sqrt2
\quad\text{for every allowed third pair}.
\qquad\text{(26)}
```

Otherwise a sequence of six Hermitian-contraction readouts would have
`U+m` tending to `4sqrt(3)` while its full norm stayed at least
`4+sqrt(2)`. Compactness gives a convergent subsequence. Continuity of
the Ky Fan sum and operator norm produces an equality-boundary
counterexample to (23). This proves existence only; no explicit width
delta is supplied.

The proof and equality arguments were independently reconstructed by
other agents in this workspace; this is internal review, not external
peer review. The accompanying checker uses exact arithmetic for scalar
identities and numerical matrix checks with a reported tolerance.
The universal inequalities are proved above;
finite construction checks do not replace their proofs.

Reproduce the targeted checks with

```sh
python tools/check_sharp_two_mode_support.py --output results/sharp_two_mode_support.json
```

The JSON records `source_sha256` for the checker and `proof_note_sha256`
for this note. Verify that both hashes match the files under review.
The report is byte-identical for the same files and runtime environment;
matrix rounding can differ across environments within the tolerance. Its
fixed weighted examples check the construction, including endpoints,
not an optimization over readout orientations.
