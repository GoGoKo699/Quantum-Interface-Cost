# Prior comparison for the nonflat half-rank theorem

Date: 27 September 2026. Research base:
`ecdfc7d6ad3ee16e66ba6f6de8802974bb558ee2`.
Status: targeted primary-source comparison, with explicit supplied
deductions. This is not an exhaustive assessment of publication priority.

The [half-rank theorem](HALF_RANK_RETENTION_CONVERSE.md) proves, for
n=2,3,4 and d=2^n,

$$
S\ge0,\quad \operatorname{Tr}S^2=1,\quad
\operatorname{rank}S\le d/2
\quad\Longrightarrow\quad
\sum_{i,b=X,Z}\sqrt{\operatorname{Tr}(S P_{i,b}S P_{i,b})}
\le2n-2+\sqrt2.
$$

This affinity bound gives `Gamma(n,d/2)=2n-2+sqrt(2)` and classifies
every maximizing normalized seed Gram state. It includes nonflat seeds
in the original model: one unknown specimen, one delayed local query,
unlimited finite classical records, and a worst-case quantum dimension
cap. The [flat-seed comparison](../FLAT_SEED_PRIOR_COMPARISON.md) and
[literature ledger](../LITERATURE_COMPARISON.md) record the established
framework and ingredients. The comparisons below address the strengthened
rank theorem directly.

## 1. Poincare gives a nonflat baseline, with a strict gap

Put `tau(T)=Tr(T)/d`, `X=sqrt(d) S`, and expand in normalized Paulis:

$$
X=\sum_w x_w\sigma_w,\qquad \sum_wx_w^2=1,\qquad
x_0=\tau(X),\qquad x_0^2\le\tfrac12.
$$

The last step is rank Cauchy. For the depolarizing generator
`K_n=sum_i(id-E_i)`, where E_i is normalized partial trace at site i
with the local identity reinserted,

$$
\mathscr D(X)=\tau(XK_n(X))=\sum_w|w|x_w^2
\ge1-x_0^2\ge\tfrac12.
$$

This is the elementary Poincare proof. Its Boolean form appears in
Montanaro--Osborne, *Quantum boolean functions*,
[0810.2435v5](https://arxiv.org/pdf/0810.2435v5), Proposition 72,
Eq. (163), printed p. 38. The displayed proof needs no Boolean or
flat-spectrum hypothesis. Writing `a_(i,b)=Tr(S P_(i,b) S P_(i,b))`,
Pauli conjugation gives the query-dependent identity

$$
\sum_{i,b=X,Z}a_{i,b}
=2n-2\sum_w\bigl(|w|+N_Y(w)\bigr)x_w^2\le2n-1.
$$

The established fidelity-affinity comparison and Cauchy therefore give

$$
\Gamma(n,d/2)\le\sqrt{2n(2n-1)}.
$$

Its square exceeds the target square by
`(n-1)(6-4sqrt(2))>0`. In particular it gives sqrt(30) instead of
4+sqrt(2), and sqrt(56) instead of 6+sqrt(2). The new proof retains
additional positivity and rank information through the singleton Pauli
spectrum; aggregate energy alone gives the weaker displayed conclusion.

## 2. Beigi's Faber--Krahn rank substitution

Beigi, *Improved Quantum Hypercontractivity Inequality for the Qubit
Depolarizing Channel*, [2105.00462v2](https://arxiv.org/pdf/2105.00462v2),
9 December 2021, Theorem 4, printed p. 6, gives, when tau(X^2)=1,

$$
\mathscr D(X)\ge n\phi\!\left(\ln2-\frac{\ln R}{n}\right),
\qquad
\phi(\xi)=\frac12-
\sqrt{h^{-1}(\ln2-\xi)\bigl(1-h^{-1}(\ln2-\xi)\bigr)},
$$

where R is the rank and h is binary entropy with natural logarithms.
Lemma 8, printed p. 10, states that phi is increasing and convex.
Since phi(0)=0 and phi(ln2)=1/2, convexity gives

$$
n\phi(\ln2/n)\le\tfrac12.
$$

Thus the uniform half-rank specialization is no stronger than Section 1.
Smaller actual ranks or additional entropy information may strengthen
the source bound; this comparison concerns the uniform class R<=d/2.
The source's Theorem 2 already underlies the
[global entropic converse](../STRONG_ENTROPIC_CONVERSE.md). These direct
rank substitutions do not evaluate the sharp affinity sum or its equality.

## 3. Quantum FKN: conditional rigidity, not the nonflat optimization

Montanaro--Osborne, Proposition 59, printed p. 31, classifies Boolean
functions with no Fourier mass above degree one as single-site operators
or constants. This is established rigidity once the relevant reflection
has been shown to have that Fourier support. It does not show that every
maximizer of the nonflat affinity problem has that form.

Blecher--Gao--Xu, *Geometric influences on quantum Boolean cubes*,
[2409.00224v1](https://arxiv.org/pdf/2409.00224v1), Section 6,
Lemma 6.1 and Theorem 6.2, printed pp. 32--34, supplies the corrected
stability comparison: Boolean reflections with small high-degree tail
are close to single-site Boolean operators. General S above is positive,
not Boolean; replacing it by its support reflection discards the
eigenvalues controlling the objective. For flat seeds, the earlier
comparison already quantifies why the stated stability conclusion does
not by itself give the exact finite-range score.

## 4. Bounded-memory BB84: the finite-size bound is vacuous here

Dupuis--Fawzi--Wehner, *Entanglement sampling and applications*,
[1305.1316v3](https://arxiv.org/pdf/1305.1316v3), Eq. (27), printed p. 18,
combined with `H_2(A^n|QC)>=-q` as used in Theorem 15, gives at q=n-1

$$
2^{-H_2(X^n|QC\Theta^n)}
\le\frac12\sum_{\ell=0}^{\ell_0}\binom n\ell
+2^{-\ell_0-1}\mathbf1_{\ell_0<n}.
$$

Here C is the free classical record. The best displayed cutoff is
ell_0=0, giving exactly one; every ell_0>=1 gives a value greater than
one for n>=2. The direct dimension substitution is therefore vacuous
even before distinguishing whole-string guessing from one delayed
coordinate. Theorem 9, printed p. 16, requires n>d_local^2, with local
dimension d_local=2 here, excluding n=2,3,4. These statements do not supply
the two new constants or the maximizing seeds.

## 5. Exact overlap and remaining scope

The n=2 value and its seed equality deduction were already obtained in
[ONE_QUBIT_OPTIMALITY](../ONE_QUBIT_OPTIMALITY.md) from Cheng--Hall,
*Anisotropic invariance and the distribution of quantum correlations*,
[1610.09302v3](https://arxiv.org/pdf/1610.09302v3), Eq. (1), printed p. 1,
and Eqs. (13)--(14) with the mixed-state extension, printed p. 3.
Its common-memory-qubit hypothesis does not cover memory dimension four
or eight. The n=2 endpoint should not be presented as a new prior gap.

For n=3,4, the specifically compared statements and direct substitutions
above do not yield the exact nonflat half-rank constants or full seed
equality classification. The supplied strengthening is the positive
half-rank affinity theorem and its rigidity. The task, fidelity-affinity
inequality, Pauli calculus, FKN rigidity, and n=2 endpoint have established
antecedents. This scoped comparison does not certify publication novelty;
unsuccessful searches provide no evidence of originality.
