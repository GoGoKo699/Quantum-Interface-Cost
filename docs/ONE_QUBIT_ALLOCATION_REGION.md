# Exact allocation region for one retained qubit

Date: 22 September 2026. Research base:
`358d887058eb9fa2fe8bb899d0261ec811d42fa6`.

**Status:** supplied deduction, independently reconstructed within this
workspace. The converse uses the established Cheng–Hall monogamy theorem
already used in the [one-qubit optimum](ONE_QUBIT_OPTIMALITY.md).
Publication novelty remains unresolved; no new general incompatibility
measure or monogamy theorem is claimed.

This note allows separate contrasts for the existing local X/Z queries.
The original uniform target remains a slice of the exact region below;
the specimen, encoder, query timing, and resources are unchanged.

## 1. Explicit feasible region and weighted theorem

The encoder receives one arbitrary unknown n-qubit specimen before one
delayed query `(i,b)`, with `b=X,Z`. It may be collective, its finite
classical record is unrestricted, and every branch retains a quantum
system of dimension at most two. Require effective observables

$$
A_{i,X}=\eta_{i,X}X_i,\qquad A_{i,Z}=\eta_{i,Z}Z_i,
\qquad 0\le\eta_{i,b}\le1,
$$

uniformly for every input state, including internally entangled states.
Define the following function on the unit square:

$$
w(x,y)=\max\{0,\ x+y-1-\sqrt{2(1-x)(1-y)}\}.
\tag{1}
$$

**Theorem.** A contrast profile is feasible if and only if

$$
\boxed{\sum_{i=1}^n w(\eta_{i,X},\eta_{i,Z})\le1.}
\tag{2}
$$

Equivalently, for arbitrary nonnegative weights a_i,b_i, put
`r_i=sqrt(a_i^2+b_i^2)` and `delta_i=a_i+b_i-r_i`. The exact support
function is

$$
\boxed{\max_{\text{feasible }\eta}
\sum_i(a_i\eta_{i,X}+b_i\eta_{i,Z})
=\sum_i r_i+\max_i\delta_i.}
\tag{3}
$$

Define the quarter disk `D={(x,y) in [0,1]^2:x^2+y^2<=1}` and the
square `S=[0,1]^2`. A third equivalent description is

$$
\boxed{\mathcal K_n=\operatorname{conv}
\left(\bigcup_{k=1}^n
\mathcal D^{k-1}\times\mathcal S\times\mathcal D^{n-k}\right).}
\tag{4}
$$

The all-classical region `D^n` is already included. The full region
need not be a polytope; its equal-pair slice in Section 6 is one.

## 2. Weighted seed bound from three-qubit monogamy

For a complex `2 by 2^n` matrix L with `||L||_F=1`, define

$$
f_i=a_i\|LX_iL^\dagger\|_1+b_i\|LZ_iL^\dagger\|_1.
$$

Choose extreme Hermitian contraction decoders attaining these norms.
In dimension two, an extreme is a scalar sign or a traceless Pauli
direction. On the normalized vectorized seed, `f_i=<h_i>` with

$$
h_i=a_iX_i\otimes B_{i,X}+b_iZ_i\otimes B_{i,Z}.
$$

Call a site active when both decoders are traceless. At an inactive site,
one decoder is scalar and `h_i^2=r_i^2 I`, so `f_i<=r_i`.
Ignore sites with `r_i=0`. At an active site the reference observables

$$
C_{i,0}=\frac{a_iX_i+b_iZ_i}{r_i},\qquad
C_{i,1}=\frac{a_iX_i-b_iZ_i}{r_i}
$$

are unit Pauli directions. They need not be orthogonal: CHSH permits
arbitrary unit directions. Their CHSH operator with memory settings
`B_{i,X},B_{i,Z}` is exactly `2h_i/r_i`. For two active sites,
Cheng–Hall's independently optimized common-qubit bound gives

$$
\left(\frac{f_i}{r_i}\right)^2+
\left(\frac{f_k}{r_k}\right)^2\le2.
\tag{5}
$$

The common system is the retained qubit. The three-qubit marginal may
be mixed, and different tests may use different settings on that qubit.
Both qualifications are permitted by the prior theorem; precise source
locators appear in [the earlier proof](ONE_QUBIT_OPTIMALITY.md), Section 2.

Thus at most one site exceeds r_i. Every site also has `f_i<=a_i+b_i`,
because each trace norm is at most one. Consequently every seed obeys

$$
\sum_i f_i\le\sum_i r_i+\max_i\delta_i.
\tag{6}
$$

## 3. Converse for arbitrary physical branches

Refine the instrument into Kraus matrices K_a, retaining the original
decoder if desired. Omit zero matrices and embed smaller outputs into
dimension two. With `d=2^n`, put
`p_a=||K_a||_F^2/d` and `L_a=K_a/||K_a||_F`.
Trace preservation gives `sum_a p_a=1`. The actual branch decoders
`D_{a,i,b}` are Hermitian contractions. Taking the Hilbert–Schmidt
inner products of the effective observables with the target Paulis gives

$$
\sum_i(a_i\eta_{i,X}+b_i\eta_{i,Z})
=\sum_a p_a\sum_i h_{a,i},
$$

where
`h_{a,i}=a_i Tr(D_{a,i,X}L_aX_iL_a^dagger)`
`+b_i Tr(D_{a,i,Z}L_aZ_iL_a^dagger)`.
Actual branch alignments may be negative. Trace-norm duality still gives
`h_{a,i}<=f_i(L_a)`. Applying (6) to every seed proves the upper bound
in (3). The p_a are proof weights, not an assumption that physical
outcome probabilities are input independent. The argument uses the
worst-case branch dimension and the complete trace-preserving instrument.

## 4. Achievability and completeness of the convex description

For any `(u,v)` in D, the four-outcome parent POVM

$$
G_{s,t}=\tfrac14(I+s u X+t v Z),\qquad s,t\in\{+1,-1\},
\tag{7}
$$

is positive and sums to I. Reporting s for an X query or t for a Z
query implements exactly the two noisy Pauli observables. Measuring a
single biased axis without the required randomization would instead
leave cross terms. These local POVMs are valid on entangled input states.

Retain site k. On it, independent output noise for each query realizes
every pair in S. On all other sites use (7), realizing every point in
the kth product set in (4). Finite classical randomization realizes its
convex hull; finite-dimensional convexity needs at most `2n+1` component
points. Hence classical records remain finite.

To attain (3), retain a site maximizing delta_i at contrasts `(1,1)`.
At each other nonzero-weight site use
`(u_i,v_i)=(a_i/r_i,b_i/r_i)`; zero-weight sites may use any disk point.
The value is `sum_i r_i+max_i delta_i`.

Finally, K_n is compact and downward closed in the nonnegative orthant,
and has support function (3). Nonnegative support directions suffice:
for every real w, downward closure gives `h_K(w)=h_K(w_+)`.
A nonnegative point separated by w is therefore also separated by w_+.
The converse excludes all profiles outside K_n, proving (4).

## 5. Derivation and implementation of the explicit criterion

For a single pair `(x,y)`, the minimum fraction p for which

$$
(x,y)=p\,s+(1-p)d,\qquad s\in\mathcal S,\ d\in\mathcal D,
\tag{8}
$$

is possible is w(x,y). Indeed, necessity follows from

$$
\|((x,y)-p(1,1))_+\|_2\le1-p,
\tag{9}
$$

using `s<= (1,1)` coordinatewise. If `(x,y)` lies in D, p=0 suffices.
Otherwise the smaller quadratic root of
`(x-p)^2+(y-p)^2=(1-p)^2` is

$$
p_*=x+y-1-\sqrt{2(1-x)(1-y)}>0.
$$

It obeys `p_*<=min(x,y)`. For `p<p_*`, the positive part in (9)
does not change either coordinate and the quadratic inequality fails.
At p=p_* it holds with equality, so the minimum is exactly (1).
For `p_*<1`, one may take `s=(1,1)` and
`d=((x,y)-p_*(1,1))/(1-p_*)` on the disk boundary.

Any convex decomposition in (4) has total retained-site probabilities
p_i summing to one. Aggregating the components at site i gives (8),
with its retained average in S and its discarded average in D.
Thus `w(eta_{i,X},eta_{i,Z})<=p_i`, proving necessity of (2).

Conversely, set `p_i=w(eta_{i,X},eta_{i,Z})` when (2) holds. Retain
site i with probability p_i and use an all-classical branch with the
remaining probability. At every discarded site with `p_i<1`, use (7)
with the common classical pair

$$
(u_i,v_i)=\frac{(\eta_{i,X},\eta_{i,Z})-p_i(1,1)}{1-p_i}.
$$

It lies in D by the calculation above, including the p_i=0 case.
If p_i=1, both target contrasts are one and this site is always retained;
its classical pair is never needed. Averaging gives exactly the target
profile, proving sufficiency. The complete protocol is trace preserving,
with memory dimension at most two in every branch and no postselection.

## 6. Equal contrasts within each site and the original target

Write `eta_{i,X}=eta_{i,Z}=eta_i`, `eta_0=1/sqrt(2)`.
Direct substitution in (1) gives

$$
w(\eta_i,\eta_i)=\frac{(\eta_i-\eta_0)_+}{1-\eta_0},
\qquad
\boxed{\sum_i(\eta_i-\eta_0)_+\le1-\eta_0.}
\tag{10}
$$

This slice is a polytope, with nonnegative support function
`eta_0 sum_i w_i+(1-eta_0)max_i w_i`. Its converse also follows
directly at branch level: the unweighted seed obeys
`sum_i(f_i-sqrt(2))_+<=2-sqrt(2)`. The inequalities
`2eta_i<=sum_a p_af_i(L_a)` and convexity of the positive part give
(10), even with negative actual branch alignments.

An alternative simple construction retains site i with probability
`t_i=(eta_i-eta_0)_+/(1-eta_0)`, using the classical pair
`(eta_0,eta_0)` elsewhere and an all-classical residual branch.
It produces `tilde_eta_i=max(eta_i,eta_0)`; flip a delayed output sign
with probability `(1-eta_i/tilde_eta_i)/2` to reach eta_i exactly.
When every eta_i equals eta, (10) reproduces the original theorem
`eta<=eta_0+(1-eta_0)/n`.

No general boundary-rigidity claim is made. For example,
`(eta_1,eta_2,eta_3)=(1,0,0)` permits retaining site 1 and measuring
sites 2,3 in an entangled basis before returning random signs for their
queries. The original single-specimen, single-query model, collective
encoders, unlimited finite classical records, worst-case quantum dimension,
and uniform arbitrary-input statistics remain unchanged. Higher-memory
allocation and `Gamma(3,4)` remain open in general. The later
[exact-axis reduction](EXACT_AXIS_SPECTRAL_REDUCTION.md) evaluates the
boundary with exact X queries in graph-spectral terms and shows that
`sum_i w<=q` describes the complete original-site-retention class at any q,
but fails as a converse for unrestricted collective encoders at q=5.
The dimension-two theorem here is unchanged. Publication novelty remains open.

## 7. Established local weight and the global deduction

The function w is the standard incompatibility weight evaluated for this
noisy orthogonal pair, not a newly defined resource measure. In the usual
definition a measurement family is written as `p F+(1-p)G`, where G is
jointly measurable and F is arbitrary, and p is minimized. Conjugating
by the qubit Paulis with compensating outcome relabelings preserves the
target and compatibility and makes both components unbiased and aligned
with the specified axes. The compatible component lies in the unit disk;
the arbitrary component lies in `[-1,1]^2`. For a nonnegative target, the
same coordinatewise argument (9) and the attaining corner `(1,1)` give
exactly (1), even if negative component coordinates were initially allowed.

The following primary statements fix the provenance and comparison scope:

| Source and exact locator | Established ingredient or distinction |
|---|---|
| Yu–Liu–Li–Oh, [0805.1538v2](https://arxiv.org/pdf/0805.1538v2), 17 September 2008, Theorem 1 / Eq. (5), p. 1; unbiased specialization, p. 2 | The joint-measurability criterion gives the unit disk for orthogonal unbiased qubit observables. The source attributes that special case to Busch (1986). |
| Pusey, [1502.03010v2](https://arxiv.org/pdf/1502.03010v2), 24 March 2015, Section III / Eq. (15), p. 4; Eq. (9), p. 3 | Defines incompatibility weight and supplies the equally weighted two-Pauli witness, up to normalization and an axis rotation. |
| Cope–Uola, [2207.05722v4](https://arxiv.org/pdf/2207.05722v4), 21 June 2023, Section IV.C / Eqs. (13)–(14), pp. 7–8; Fig. 5 | Relates average compression dimension to incompatibility weight and evaluates noisy Pauli examples. The average cost is distinct from the dimension-two cap on every branch used here. Section IV.A's tensor-product subadditivity concerns full product measurements and does not supply this local-query-union converse. |
| Ioannou et al., [2202.12980v1](https://arxiv.org/pdf/2202.12980v1), 25 February 2022, Eq. (1), p. 2; Claim 3 / Eq. (13), p. 4 | Its simulability model contains this task exactly upon setting input dimension `2^n`, output dimension two, and query label `(i,b)`. The inspected evaluated claim concerns all noisy rank-one projective measurements with common noise, rather than this finite binary accuracy region. |
| Alves–Gigena–Kaniewski, [2302.08494v3](https://arxiv.org/pdf/2302.08494v3), 12 October 2023, Section II / Eq. (7), p. 3; Lemma 4 / Eq. (30), p. 9 | The biased random-access code receives a classical string and prepares a qubit. A free input-dependent classical channel would trivialize that task, so its weighted values cannot be imported as an unknown-specimen converse. |

Cheng–Hall's theorem, cited in Section 2, is the decisive prior correlation
inequality. The supplied deduction combines it with normalized Kraus
refinement and convex geometry to evaluate the complete global region:
the sum of these established local weights is at most one. This is an
exact refinement of the previous uniform one-qubit theorem, not a new
general monogamy result or a substitution of average memory for worst-case
memory. The inspected statements do not establish subsumption of the
evaluated region; that scoped comparison does not certify publication
novelty or absence from the wider literature.
