# Roof provenance and the local-to-joint entropy obstruction

Date: 2026-09-23. Reviewed main:
`b1f93ac69e4007f9d21df16ab16aa5bbecf94332` (PR #15 merge).
Reviewed tree: `c07394866c16f1a7cf3f0f8216e5adc437964900`.
This continues the historical audit; it is internal mathematical review,
not external peer review or an exhaustive originality certificate.

## 1. Findings and scope

| Claim | Verdict |
|---|---|
| Symmetry reduction and abstract fixed-block roof dichotomy are new principles | No. Vollbrecht–Werner Eqs. (38)–(42) directly supply these principles. The preceding report's proofs remain valid; their specific prior provenance is strengthened here. |
| Cope–Uola's average-rank measurement cost evaluates the full entropy profile C | No. On the whole noisy X/Z square that prior cost equals the incompatibility weight w. The already proved phase boundary states exactly where C<w. |
| Tensor repetition can eliminate a seed's local-versus-joint score gap | Incorrect. The joint score is additive on product seeds even with collective readout, by an established minimum-cost measurement theorem. An exact positive gap below persists under every tensor power. |
| The all-state two-qubit joint entropy bound is established | Unresolved. An exact one-effect reduction is supplied; the entropy optimization is not solved. |
| These comparisons certify publication originality or unrestricted optimality | No. The candidate remains the evaluated two-parameter formation profile and its proved product-diagonal operational rate. |

The physical problem is unchanged: one arbitrary unknown n-qubit specimen,
one delayed local binary X/Z query, unrestricted collective encoding,
unlimited finite classical records, a quantum dimension cap on every
branch, and uniform effects on every input and query. Joint tuple decoding
is a separately labeled comparison problem. Tensor powers below are
auxiliary Gram states on a larger single input block; they do not grant
additional copies of the unknown physical input. Flagged average entropy
is an auxiliary variational cost, not a replacement for worst-case memory.

## 2. Actual prior subsumption of the convex-roof method

Vollbrecht–Werner, *Entanglement Measures under Symmetry*,
[quant-ph/0010095v2](https://arxiv.org/abs/quant-ph/0010095v2), version stamp
1 March 2001, Section IV.A, Eqs. (38)–(41), printed pp. 10–11, proves a
compact-group reduction of a convex roof to the convexification of a
single-orbit minimum. Section IV.B, Eq. (42), p. 11, proves affinity on the
convex hull of the atoms in an optimal positive-weight decomposition.
These results apply directly here, not merely by analogy.

For the first application, take the compact convex set of normalized
qubit assemblages with two binary settings, and the function
`h(Gamma)=S(sum_s Gamma_(s|b))`. Its convex roof is Cope's established
E_FA: refinement to extremal assemblages cannot increase average marginal
entropy. Use Pauli conjugation with the matching outcome relabeling.
The invariant assemblages are

$$
\sigma_{s|X}^{x,z}=(I+sxX)/4,\qquad
\sigma_{s|Z}^{x,z}=(I+szZ)/4.
\tag{1}
$$

Use the full signed square for the group-invariant set and then restrict
to x,z>=0. Here is the orbit minimum, reconstructed for this task. For a
qubit marginal with Bloch vector r, the available X/Z correlations are
bounded by

$$
F_X=\sqrt{1-r_y^2-r_z^2},\qquad
F_Z=\sqrt{1-r_x^2-r_y^2}.
$$

Thus a seed whose orbit gives (x,z) has
`|r|^2<=2-x^2-z^2`. Outside the unit disk this is attained by
`r=(sqrt(1-z^2),0,sqrt(1-x^2))`, with trace-norm-optimal decoders.
Inside the disk a pure vector `r=(x,sqrt(1-x^2-z^2),z)` attains the profile
at zero entropy. Writing

$$
f(v)=h_2\!\left(\frac{1-\sqrt{1-v^2}}2\right),
$$

the exact orbit minimum is therefore

$$
\varepsilon(x,z)=
\begin{cases}
0,&x^2+z^2\le1,\\
f(\sqrt{x^2+z^2-1}),&x^2+z^2>1.
\end{cases}
\qquad C=\operatorname{co}\varepsilon.
\tag{2}
$$

The last identity is a specialization of the prior roof theorem. The
[profile note](../PRODUCT_DIAGONAL_PROFILE_RATE.md) performs the additional
family-specific convexification, support optimization and phase evaluation.
Neither the resource definition nor the general reduction is a novelty.

For the second application, use the full-tuple moment vectors and product
atoms v_j of [the preceding report](TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md),
Section 3. Their costs are j, j=0,...,n. Their moment vectors are affinely
independent, and every interior target u_k=eta^k has strictly positive
binomial weights on all n+1 atoms. If this decomposition attains B_n at one
interior eta, prior Eq. (42) makes the roof affine on the whole product
simplex. It consequently attains the product cost at every eta. Its affine
plane `L(w)=n(w_1-t)/(1-t)`, t=1/sqrt(2), is globally supporting: otherwise
an off-plane cheaper seed could be inserted with small positive weight and
compensated inside this full-dimensional simplex. This also gives the
universal joint-decoder entropy inequality in that report.

The specific moments, affine independence and physical orbit completion
are supplied applications. The affinity/compensation principle is prior.
This corrects attribution, not the theorem or its original-model scope.

The same prior paper evaluates portions of a two-parameter family of
orthogonally invariant bipartite states (Section IV.E, Fig. 7, p. 13;
separable region in Section II.D, Example 3). It does not automatically
evaluate (2). Indeed no affine map from the entire profile square into a
fixed-dimensional OO-invariant-state family can satisfy `E_F(F(x,z))=C(x,z)`:
the inverse image of its separable polygon is polyhedral, whereas the zero
set of C is the quarter disk. This excludes even a non-surjective affine
identification. It does not exclude arbitrary nonlinear reductions. The
natural Werner substitution through `sqrt([x^2+z^2-1]_+)` returns the raw
orbit cost epsilon, not its convexification in (x,z); nonlinear substitution
cannot silently be interchanged with that operation.

## 3. Exact comparison with Cope–Uola's average-rank measure

Cope–Uola, *Quantifying the high-dimensionality of quantum devices*,
[2207.05722v4](https://arxiv.org/abs/2207.05722v4), 21 June 2023, Eq. (8),
p. 5, defines D_M by minimizing the worst-input expected log Kraus rank.
Section IV.B uses Pauli symmetry; Section IV.C, Eqs. (12)–(14), pp. 7–8,
gives the qubit D_M and incompatibility-weight SDPs. They are not equal for
all measurement families. For (1), however, the exact specialization is

$$
D_M(M^{x,z})=W(M^{x,z})=
 w(x,z)=\left[x+z-1-\sqrt{2(1-x)(1-z)}\right]_+,
\quad M^{x,z}=2\sigma^{x,z}.
\tag{3}
$$

**Proof preserving the worst-input maximization.** In the D_M SDP let
`B_0=sum_lambda G_lambda` be the total jointly measurable component.
Its constraints include positive G_lambda, each measurement marginal
bounded above by M, and `(alpha-1)I+B_0>=0`. Pauli conjugation with outcome
relabeling preserves feasibility and alpha for every independent pair x,z.
Averaging makes B_0=beta I. Then gamma=1-beta<=alpha is feasible for the
weight SDP, whose last constraint is `(gamma-1)I+B_0=0`. Hence W<=D_M;
every weight solution is also D_M-feasible, giving the reverse inequality.
The remaining rank-two effect is `(1-beta)I`, so every input has the same
average log-rank cost. No maximization over inputs was dropped.

For completeness the weight formula also follows geometrically. Twirl a
weight decomposition `M=pN+(1-p)G`. The compatible G has contrast in the
unit disk and N in the signed square. For p<min(x,z), feasibility requires

$$
(x-p)^2+(z-p)^2\le(1-p)^2.
$$

Outside the disk its first nonnegative solution is the w in (3), which is
at most min(x,z). It is attained by N=(1,1) and
`G=((x-w)/(1-w),(z-w)/(1-w))`; handle (1,1) separately with w=1.
Inside the disk take w=0. Larger p cannot improve the minimum.

Thus the profile note's existing phase theorem already gives the complete
comparison with this prior resource. For 0<z<=x<1 outside the disk,

$$
C(x,z)<D_M(M^{x,z})
\quad\Longleftrightarrow\quad
\frac{1-x}{1-z}<2(1/\ln2-1)^2.
\tag{4}
$$

There is equality in the complementary central region and on the disk.
On x=1, C(1,z)=f(z)<z=D_M for 0<z<1; use symmetry for the other half of
the square. The equal-accuracy slices coincide. The phase calculation is
already in PR #13; (3) supplies its precise prior-resource interpretation.
It neither proves an unrestricted entropy converse nor replaces the
maximum quantum dimension by this prior average-rank cost.

## 4. Joint scores tensorize: a prior Bayesian decision theorem

Define the independently optimized local score

$$
f_n(\rho)=\frac1{2n}\sum_{i,b\in\{X,Z\}}
\|\sqrt\rho P_{i,b}\sqrt\rho\|_1.
$$

For a full setting tuple b let

$$
J_b(\rho)=\max_{\substack{\Gamma_{s|b}\ge0\\
                      \sum_s\Gamma_{s|b}=\rho}}
 \frac1n\sum_{s,i}s_i\operatorname{Tr}(P_{i,b_i}\Gamma_{s|b}),
\qquad j_n=2^{-n}\sum_b J_b.
\tag{5}
$$

Each context may use an arbitrary joint POVM on a purification; no
no-signalling condition between its internal output sites is imposed.
Always j_n<=f_n. For the filtered ensemble
`v_x=sqrt(rho)|x_b>`, with priors `p_x=||v_x||^2`, the payoff in (5) is
`1-2 d_H(x,s)/n`. Therefore J_b is one minus twice the minimum Bayesian
Hamming risk divided by n.

Wallden–Dunjko–Andersson, *Minimum-cost quantum measurements for quantum
information*, [1312.5205v1](https://arxiv.org/abs/1312.5205v1), 18 December
2013, Theorem 3 / Eq. (74), p. 14, and Lemma 7, p. 15, establish product
optimality for product ensembles with independent priors and additive loss,
allowing collective measurements. Our product-seed specialization is

$$
(n+m)j_{n+m}(\rho\otimes\tau)
 =n j_n(\rho)+m j_m(\tau).
\tag{6}
$$

A direct proof checks every quantifier. For fixed contexts b,c, marginalize
any collective tuple assemblage over the second output block and trace its
reference subsystem. The result sums to rho and is legal for context b.
Its first-block score is at most n J_b(rho), even if the marginal decoder
depends on c. The other block gives m J_c(tau). Averaging proves the upper
bound; product assemblages attain it. The filtered states and priors factor
for product seeds, exactly the prior theorem's hypotheses. They need not
factor for correlated rho, so (6) is no all-state entropy theorem.

Put delta=1-t and define

$$
D_f(\rho)=n(f_n(\rho)-t)-\delta S(\rho),\qquad
D_j(\rho)=n(j_n(\rho)-t)-\delta S(\rho).
\tag{7}
$$

Both excesses are additive on products. Tensor powers scale them; pure
bisector or maximally mixed one-qubit padding contributes zero. Keeping
classical flags averages the branch excesses. These operations with only
D_j<=0 supplementary seeds cannot turn a hypothetical D_f>0, D_j<=0 seed
into a joint violation. This is a precise limitation, not a claim that such
a local entropy violator exists, and not a prohibition on other collective
states or transformations. Forgetting flags and mixing density matrices
is a different operation and is not covered by the averaging assertion.

### Exact score gap with primal and dual certificates

Let c=cos(pi/8), s=sin(pi/8), and take the normalized two-input seed

$$
L=\frac12\begin{pmatrix}c&s&c&s\\s&c&-s&-c\end{pmatrix},
\qquad \rho=L^\dagger L=\frac{I+t(IX+XZ)}4.
\tag{8}
$$

IX and XZ anticommute. Hence rho has spectrum (1/2,1/2,0,0) and S=1.
Direct multiplication gives

$$
LX_1L^\dagger=Z/2,\quad LZ_1L^\dagger=tX/2,\quad
LX_2L^\dagger=tI/2,\quad LZ_2L^\dagger=tZ/2.
$$

For compressed observables A,B, maximize
`sum_(r,u) Tr[(rA+uB)N_(r,u)]`. A dual Y satisfying Y>=rA+uB for all
signs bounds the unnormalized sum by Tr Y. The following feasible duals
and attaining POVMs prove exact optimality in every context.

| Context | A, B | Dual Y | Optimum sum | Attaining readout |
|---|---|---|---|---|
| XX | Z/2, tI/2 | (1+t)I/2 | 1+t | Measure Z; second sign always + |
| XZ | Z/2, tZ/2 | (1+t)I/2 | 1+t | Measure Z; give both bits its sign |
| ZX | tX/2, tI/2 | tI | 2t | Measure X; second sign always + |
| ZZ | tX/2, tZ/2 | I/2 | 1 | N_(r,u)=[I+(rX+uZ)/sqrt(2)]/4 |

Consequently

$$
f_2=\frac{1+3t}4,\qquad j_2=\frac{3+4t}8,\qquad
f_2-j_2=\frac{\sqrt2-1}8>0.
\tag{9}
$$

Equation (6) proves that this normalized gap persists for every tensor
power even under collective tuple readout. Nevertheless
`D_f=-delta/2` and `D_j=-1/4`: both entropy inequalities hold here.
This is neither a counterexample to subset optimality nor a proof of
strict optimized formation costs A_n<B_n.

## 5. Exact two-qubit reduction and the remaining analytic obstruction

For n=2, use the product b eigenbasis 00,01,10,11 and put
`D_s=(s_1P_1+s_2P_2)/2=Pi_s-Pi_(-s)`. The primal is (5).
Its support-compressed dual is the attained minimum
`Tr(rho Y)` subject to `Y>=P D_s P`, where P projects onto supp rho and
Y acts there. On the full space the exact dual is an **infimum**, not
necessarily a minimum when rho is singular. For example, in the ZZ
context rho=|++><++| has J_b=0, but an attaining full-space Y>=±D_0
would require both `Y|++>=D_0|++>` and `Y|++>=-D_0|++>`, impossible.

Group the even guesses into `F=Gamma_00+Gamma_11` and the odd guesses
into rho-F. Each binary optimization is a trace norm. Thus, for arbitrary
complex or singular rho,

$$
\begin{split}
J_b(\rho)=\max_{0\le F\le\rho}\bigg\{&
 \sqrt{(F_{00,00}+F_{11,11})^2-4|F_{00,11}|^2}\\
 &+\sqrt{((\rho-F)_{01,01}+(\rho-F)_{10,10})^2
                        -4|(\rho-F)_{01,10}|^2}\bigg\}.
\end{split}
\tag{10}
$$

Indeed for H>=0 the only potentially nonzero eigenvalues of
`sqrt(H)(|a><a|-|c><c|)sqrt(H)` have sum H_aa-H_cc and product
`-(H_aa H_cc-|H_ac|^2)<=0`. Their absolute sum is
`sqrt((H_aa+H_cc)^2-4|H_ac|^2)`. This proves (10) without invertibility
or a real-matrix restriction. The condition 0<=F<=rho still couples the
parity sectors through all off-diagonal blocks; discarding that coupling
is a relaxation. The outer entropy optimization has not been evaluated.

A second exact description exposes a failed shortcut. J_b is the concave
roof of `u_b(psi)=(|<P_1>|+|<P_2>|)/2`, by refining each Gamma_s into pure
vectors and assigning each its optimal signs. The four contexts can use
four different decompositions. At rho=I/4, their individual eigenbasis
decompositions give j_2=1. But every pure psi has `average_b u_b(psi)<=t`
by the local Bloch bound. No common decomposition can attain those four
roofs. Context averaging and concave-roof optimization cannot be swapped.

Changing f to j also does not repair the earlier false deficit
superadditivity route. For opposite X/Z bisectors beta_±, set
`rho_e=(1-e)|beta_+ beta_+><beta_+ beta_+|+e|beta_- beta_-><beta_- beta_-|`.
Its four optimal local decoders are one common logical Z, so j_2=f_2=t.
Both marginals have `j_1=sqrt(t^2+2e-2e^2)` and entropy h_2(e), as does
the joint state. With `Delta_n=S-n(j_n-t)/delta`,

$$
\Delta_2-\Delta_1-\Delta_1
=-h_2(e)+2[\sqrt{t^2+2e-2e^2}-t]/\delta<0
\quad(e=1/1024).
$$

For this explicit value use `h_2(e)>=10e` and the square-root increment
`<=sqrt(2)e`; the expression is at most `(4sqrt(2)-6)e<0`.
This extends the already documented proof-step obstruction to joint scores;
it is not a failure of either global entropy conjecture.

## 6. Verification, novelty boundary and stopping criterion

Current main, existing reports, issues #1–#2 and the open PR list were
checked before editing; no competing PR was open. Two independent internal
reviews reconstructed the exact gap and all primal/dual certificates,
product rule, one-effect formula and both failed shortcuts. One review
caught the singular-state dual-attainment caveat, which is incorporated
above. No new numerical search, large simulation or solver certificate was
used. Unchanged construction checks were not rerun. LICENSE and the
historical initial audit are preserved.

The prior methodological subsumption in Section 2 is an affirmative finding.
The specific OO-family obstruction and average-rank comparison rule out
specified identifications, not all possible literature reductions. The
candidate contribution remains the complete analytic two-parameter profile
with optimizer and phase boundary, together with its product-diagonal
fixed-cap operational theorem. Its originality remains unverified.

For unrestricted equal-accuracy optimality the required all-state bound is
still

$$
\sum_{i,b}\|\sqrt\rho P_{i,b}\sqrt\rho\|_1
\le\sqrt2\,n+(2-\sqrt2)S(\rho).
\tag{11}
$$

The weaker joint-query target is
`j_n<=t+delta S(rho)/n`; (10) does not prove it even for all two-qubit
states. Neither product repetition nor the two failed tensorization
shortcuts settles that gap. A complete all-state proof or certified
violating seed is the mathematical gate. Additional failed searches or
isolated entropy-valid families would not establish unrestricted optimality
or publication novelty.
