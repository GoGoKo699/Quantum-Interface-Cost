# An entropy characterization of the asymptotic interface rate

Date: 2026-09-22. Research base:
`df45e2eaceb5669cfff9ac063d3da845d622dac3`.
Status: derived with the proof below and independently checked by another
agent in this workspace. This is not external peer review, a certification
of publication novelty, or a closed-form evaluation of the rate.

The [normalized-seed reduction](COLLECTIVE_ENCODING_REDUCTION.md) expresses
finite-block memory through a rank constraint. Asymptotically, that rank
constraint has an exact regularized entropy formulation. The result also
identifies a universal entropy inequality that is equivalent to optimality
of the random-subset rate.

## 1. Model and statement

Use exactly [RESEARCH_NOTE.md](../RESEARCH_NOTE.md), Section 2. An encoder
receives one arbitrary unknown state on n qubits. Before learning a single
query $(i,b)$, where $b\in\{X,Z\}$, it retains a quantum system of dimension
at most $2^q$ and an unrestricted finite classical record. The encoder may
act collectively on all n input qubits. After the query, its binary output
must have effects

$$
\frac{I\pm\eta P_{i,b}}2
$$

on the original input, for every input state and every query. Thus the
contrast condition is an operator identity, including on inputs entangled
across sites. The quantum dimension bound holds on every branch. No source
reaccess, additional copies of the specimen, preshared entanglement, or
postselected success is available.

Write $q_{\min}(n,\eta)$ for the minimum integer q. The block-product
argument in the research note gives

$$
R(\eta)=\lim_{n\to\infty}\frac{q_{\min}(n,\eta)}n
=\inf_{n\ge1}\frac{q_{\min}(n,\eta)}n.
$$

All logarithms and entropies below use base two. For an n-qubit density
matrix $\rho$, define

$$
f_n(\rho)=\frac1{2n}\sum_{i=1}^n\sum_{b=X,Z}
\left\|\sqrt\rho\,P_{i,b}\sqrt\rho\right\|_1,
$$

$$
e_n(\eta)=\min_{\rho:\,f_n(\rho)\ge\eta}S(\rho),
\qquad
E(\eta)=\inf_{n\ge1}\frac{e_n(\eta)}n.
$$

There is no rank constraint in $e_n$. Each minimum exists: density matrices
form a compact set, entropy and $f_n$ are continuous, and the maximally
mixed state is feasible for every $0\le\eta\le1$. Each trace norm in
$f_n$ is the root fidelity between $\rho$ and $P_{i,b}\rho P_{i,b}$;
the fidelity is not squared in this convention.

**Theorem.** For every $0\le\eta\le1$,

$$
\boxed{R(\eta)=E(\eta)
=\lim_{n\to\infty}\frac{e_n(\eta)}n.}
\tag{1}
$$

The function E is nondecreasing, convex, and continuous on $(0,1)$.
With $\eta_0=1/\sqrt2$,

$$
E(\eta)=R(\eta)=0\quad(0\le\eta\le\eta_0),
\qquad E(1)=R(1)=1.
$$

Equation (1) is a regularized variational characterization. It does not
determine the unknown values between $\eta_0$ and 1.

## 2. Rank gives the entropy converse

For a normalized seed L, let $\rho=L^\dagger L$. Polar decomposition
$L=V\sqrt\rho$ preserves the nonzero singular values of the sandwiched
operators, so

$$
g(L)=\sum_{i,b}\|LP_{i,b}L^\dagger\|_1=2n f_n(\rho).
$$

If L has output dimension $D\le2^q$, then

$$
S(\rho)\le\log_2\operatorname{rank}\rho\le q.
$$

The exact seed reduction implies that any admissible q-qubit protocol at
contrast $\eta$ has an admissible seed with $f_n(\rho)\ge\eta$ and rank
at most $2^q$. Consequently

$$
e_n(\eta)\le q_{\min}(n,\eta),\qquad E(\eta)\le R(\eta).
\tag{2}
$$

This uses the worst-case dimension of the physical interface. It does not
replace that resource by an average over classical branches.

## 3. Tensor products, convexity, and contrast slack

For states $\rho$ on n sites and $\sigma$ on m sites, trace-norm
multiplicativity and $\operatorname{Tr}\rho=\operatorname{Tr}\sigma=1$
give

$$
(n+m)f_{n+m}(\rho\otimes\sigma)
=nf_n(\rho)+mf_m(\sigma),
\qquad S(\rho\otimes\sigma)=S(\rho)+S(\sigma).
\tag{3}
$$

At fixed contrast, $e_{n+m}\le e_n+e_m$. Fekete's lemma therefore proves
the limit assertion for E in (1). Also $0\le E\le1$, and E is
nondecreasing because increasing the contrast shrinks the feasible set.

For convexity, take an n-site state feasible at a and an m-site state
feasible at b. The state $\rho^{\otimes m}\otimes\sigma^{\otimes n}$
has $2nm$ sites, contrast at least $(a+b)/2$, and entropy per site
$S(\rho)/(2n)+S(\sigma)/(2m)$. Taking the two independent infima yields

$$
E\!\left(\frac{a+b}{2}\right)\le\frac{E(a)+E(b)}2.
\tag{4}
$$

A locally bounded midpoint-convex function is continuous and convex on
the interior of its interval. Here the bound $0\le E\le1$ supplies the
needed hypothesis.

The right continuity needed below can also be seen directly. Iterating
(4), for $t=2^{-k}$ and $\eta<1$,

$$
E(\eta)\le E((1-t)\eta+t)
\le(1-t)E(\eta)+tE(1).
$$

Monotonicity then gives $E(\eta+)=E(\eta)$. This scalar-contrast
argument does not assume continuity of a general assemblage entanglement
measure or of the finite-block minimizers.

## 4. Entropy gives a fixed-dimension encoder

Fix $\eta<\eta'\le1$, a block size n, and a state $\rho$ with
$f_n(\rho)\ge\eta'$. Let $L=\sqrt\rho$ and let $|\psi\rangle$ be its
normalized vectorization, in input-reference-then-output order. Its Schmidt
coefficients squared are the nonzero eigenvalues of $\rho$.

Choose an entropy tolerance $\tau>0$. In $|\psi\rangle^{\otimes M}$,
retain the output Schmidt eigenvectors whose product eigenvalues are at
least $2^{-M(S(\rho)+\tau)}$. If $D_M$ is their number, then

$$
D_M\le2^{M(S(\rho)+\tau)}.
\tag{5}
$$

Let $p_M$ be the discarded probability. The law of large numbers applied
to the nonzero eigenvalues gives $p_M\to0$. For sufficiently large M the
retained subspace is nonempty. Normalize the truncated vector to obtain
$|\psi'_M\rangle$. The pure-state trace distance is exactly

$$
\left\|
|\psi\rangle\langle\psi|^{\otimes M}
-|\psi'_M\rangle\langle\psi'_M|
\right\|_1=2\sqrt{p_M}.
\tag{6}
$$

For each original local query choose a trace-norm-optimal Hermitian
decoder contraction B on its output block, tensored with the identity on
the other output blocks. Its correlation observable $P^T\otimes B$ has
operator norm at most one. Equation (6) bounds the loss of each correlation
by $2\sqrt{p_M}$, and therefore bounds the loss of their average by the
same number, with no factor depending on nM.

Compress the retained output subspace isometrically to dimension $D_M$.
The compressed B remain Hermitian contractions. The resulting vector is
a normalized seed $L_M$ with

$$
f_{nM}(L_M^\dagger L_M)
\ge f_n(\rho)-2\sqrt{p_M}
\ge\eta'-2\sqrt{p_M}.
\tag{7}
$$

For all sufficiently large M this score is at least $\eta$. Apply the
Pauli-orbit completion and query-symmetry equalization from the
[seed reduction](COLLECTIVE_ENCODING_REDUCTION.md), Section 3. They
produce a trace-preserving instrument, including every branch, whose
common contrast is the seed score. Independent output flips reduce that
contrast to exactly $\eta$. Every branch has quantum output dimension
at most $D_M$, and hence uses at most

$$
q_M=\lceil\log_2 D_M\rceil
\le\lceil M(S(\rho)+\tau)\rceil
\tag{8}
$$

qubits. The classical orbit and randomization labels are finite for each
block and are free in the specified model.

The Schmidt projection is used to define a new mathematical seed. The
physical protocol is the complete trace-preserving orbit instrument; it
does not condition success on a typical outcome. Likewise the tensor
powers above are virtual seed vectors used to build one encoder on one
arbitrary nM-qubit specimen. They do not supply repeated copies of the
unknown input. After the twirl the effect identities hold uniformly on
all input states, including states entangled across the M blocks.

Equations (7)–(8) and the definition of R imply

$$
R(\eta)\le\frac{S(\rho)+\tau}{n}.
$$

Send $\tau\downarrow0$, minimize over $\rho$ and n feasible at $\eta'$,
and obtain $R(\eta)\le E(\eta')$. Right continuity from Section 3 allows
$\eta'\downarrow\eta$. Together with (2), this proves (1) for $\eta<1$.

## 5. Endpoints

A pure product of local eigenstates of $(X+Z)/\sqrt2$ has
$f_n=\eta_0$ and zero entropy. Thus $E=0$ for $0\le\eta\le\eta_0$,
matching the classical interface and covering $\eta=0$ explicitly.

At $\eta=1$, every one of the $2n$ root fidelities in $f_n$ must equal
one. Equality of fidelity to one forces
$\rho=P_{i,b}\rho P_{i,b}$ for every local X and Z. Their algebra is the
full matrix algebra, whose commutant consists only of scalars. Therefore
$\rho=I/2^n$, $e_n(1)=n$, and $E(1)=1$. Equation (2) and the full-memory
encoder give $R(1)=1$. No continuity assumption at this endpoint is needed.

## 6. Exact equivalence to the universal entropy inequality

Define the hybrid rate

$$
H(\eta)=\frac{\eta-\eta_0}{1-\eta_0}
\qquad(\eta_0\le\eta\le1).
$$

The random-subset construction proves $R(\eta)\le H(\eta)$.

**Corollary.** The following two statements are equivalent:

1. $R(\eta)=H(\eta)$ for every $\eta_0<\eta\le1$.
2. For every n and every n-qubit density matrix $\rho$,

   $$
   \boxed{
   g(\sqrt\rho)\le\sqrt2\,n+(2-\sqrt2)S(\rho).
   }
   \tag{9}
   $$

To prove the implication from (9), divide by $2n$. For every state feasible
at $\eta>\eta_0$,

$$
\frac{S(\rho)}n\ge
\frac{f_n(\rho)-\eta_0}{1-\eta_0}
\ge H(\eta).
$$

Taking the regularized infimum in (1) proves $R\ge H$, and the hybrid
construction proves equality.

Conversely, suppose statement 1 holds. If $f_n(\rho)>\eta_0$, then (1)
gives

$$
H(f_n(\rho))=R(f_n(\rho))
\le\frac{S(\rho)}n,
$$

which is (9). If $f_n(\rho)\le\eta_0$, (9) follows directly from
$S(\rho)\ge0$.

In particular, any violation of (9) would have $\eta_0<f_n(\rho)<1$
and would imply the strict, operational asymptotic improvement

$$
R(f_n(\rho))\le\frac{S(\rho)}n<H(f_n(\rho)).
$$

The [product-diagonal theorem](COMMUTING_SEED_BOUND.md) proves (9) for
Gram matrices diagonal in any fixed tensor product of local qubit bases,
allowing correlated spectra and arbitrary local axes. Such states cannot
witness a strict rate improvement, even after their entropy is converted
to asymptotic rank by Section 4. The subsequent
[boundary results](ENTROPY_INEQUALITY_BOUNDARIES.md) also exclude all
rank-two states, stabilizer-basis spectra, flat rank-three two-input states,
and a scoped family of flat half-rank projectors. A two-input, nonuniform
rank-three state is the smallest possible entropy witness; general full-rank
two-input states also remain open. The
[logarithmic-Sobolev converse](STRONG_ENTROPIC_CONVERSE.md) bounds this same
unrestricted entropy minimum from below but does not evaluate it.
Inequality (9) for unrestricted states remains unresolved.
The false local conditional-entropy argument in that
note is an obstruction to one proposed proof, not a counterexample to (9).
Subsequent exclusions also cover [local classical flags](CLASSICAL_FLAG_ENTROPY_BOUND.md),
[locally maximally mixed two-input states](LOCALLY_MIXED_TWO_QUBIT_BOUND.md),
and arbitrary full-rank states with [bounded spectral condition number](SPECTRAL_CONDITION_ENTROPY_BOUND.md).
The [flat half-rank result](FLAT_HALF_RANK_OPTIMALITY.md) settles that
family through four input qubits. These results narrow possible witnesses
without evaluating the unrestricted regularized entropy minimum.

## 7. Prior ingredients and novelty boundary

Schmidt typicality and the conversion of asymptotic rank to entropy are
established ingredients. The supplied deduction combines them with the
exact seed twirl and a scalar-contrast continuity argument; publication
novelty of this specialization is not certified.

Cope–Uola, *Quantifying the high-dimensionality of quantum devices*,
[arXiv:2207.05722v4](https://arxiv.org/pdf/2207.05722v4), Eq. (7), already
formulates worst-case measurement compression dimension; their average
cost is a distinct resource. Section VI.1, Eqs. (20)–(22), printed
pp. 11–12, relates assemblage entanglement of formation to asymptotically
smoothed Schmidt measure for complete tensor-product assemblages. Those
objects require all setting tuples and outcome tuples, whereas this
workload asks one delayed local query. The discussion after Eq. (22)
identifies a continuity obstacle, and the section leaves asymptotic
measurement compression for future work. Its methods are close prior
ingredients; its statements do not directly establish (1).

Cope, *Entanglement cost for steering assemblages*,
[arXiv:2102.02333v2](https://arxiv.org/pdf/2102.02333v2), Eqs. (5)–(6),
defines asymptotic entanglement cost for complete tensor-product
assemblages under LOCC. That full-tuple target is stronger than one
delayed query. It is relevant prior theory, not a directly interchangeable
operational characterization.

The [commit-pinned audit](audits/PROOF_AND_NOVELTY_AUDIT.md) contains the
broader framework and reconstruction comparisons. Neither the formula
(1), the corollary, nor passing finite matrix diagnostics establishes a
sharp intermediate rate or absence of an earlier equivalent theorem.
