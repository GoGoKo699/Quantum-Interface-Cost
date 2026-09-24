# Separate qubit readouts with one arbitrary additional query

Date: 24 September 2026. Reviewed main:
`a383214b357ccbd83a62ae0c94660083cb8b090e`, the merge of PR #37.

**Verdict.** For `n=q+1`, the retention benchmark is optimal whenever
q original query pairs address separate memory qubits; the remaining
query pair may act arbitrarily on the entire memory. The encoder is
unrestricted and all binary POVMs are allowed.

For three inputs and two retained qubits there is a simpler consequence:
**if any two original query algebras commute, no collective advantage
is possible.** A violating optimal family must therefore make all three
query algebras pairwise noncommuting.

The three complete signature patterns left by the previous report
remain unresolved. This theorem excludes further families within them,
not another complete pattern. Publication originality remains open.

## 1. The sharp conditional theorem at every size

Let `q>=1`, `n=q+1`, and `Q=A_1 tensor ... tensor A_q` with each A_i
a qubit. Let B_i,D_i be Hermitian contractions. For `i<=q` assume
they act only on A_i. The last pair B_n,D_n is arbitrary on Q.
On the n reference qubits and Q set

$$
H=\sum_{i=1}^{n}h_i,\qquad
h_i=X_i\otimes B_i+Z_i\otimes D_i.
\tag{1}
$$

**Theorem.**

$$
\boxed{\|H\|_\infty\le2q+\sqrt2.}
\tag{2}
$$

The memory factorization can be any unitary identification with q
qubits; it need not coincide with the encoder's circuit or input
subsystems. No commutation or Pauli assumption is imposed on the last
pair relative to the first q pairs. Their internal angles are arbitrary.
General contractions represent arbitrary binary POVMs.

The constant is attained: use X/Z on each dedicated memory qubit,
a Bell pair between it and its reference, scalar identity readouts
for the last query pair, and a top eigenvector of `X_n+Z_n`.
The physical uniform-error attainment is given in Section 5.
The case q=1 is also covered by the earlier unrestricted one-memory-qubit
theorem; the present argument handles every q with the stated structure.

## 2. One product-Bell eigenvector controls the first q terms

Separate convexity reduces the contractions to reflections while
preserving each dedicated factor. Any Hermitian contraction is a
convex combination of reflections in its own spectral algebra; no
dimension-increasing dilation is used.

Put `r=sqrt(2)`. If any of the first q reflection pairs commutes
internally, its term has norm at most r and the other q terms have
norm at most two. The triangle inequality proves (2).
Otherwise all the first q pairs are traceless qubit reflections.
On reference i and memory qubit A_i their spectra are

$$
\{\pm u_i,\pm v_i\},\qquad
2\ge u_i\ge r\ge v_i\ge0,\qquad u_i^2+v_i^2=4.
\tag{3}
$$

Their top vectors are Bell vectors, by the two-Pauli singular-value
decomposition used in the [one-block proof](JORDAN_BLOCK_CONVERSE.md).
Let

$$
U=\sum_{i=1}^q u_i,\qquad
u=\min_i u_i,\qquad v=\sqrt{4-u^2},\qquad
c=u-v,\qquad m=U-c.
\tag{4}
$$

The gap `u_i-v_i` increases with u_i. Since the first q terms act on
disjoint reference-memory pairs, their sum H_0 has top eigenvalue U,
with product-Bell vector Omega, and every other eigenvalue is at most m.
Therefore

$$
H_0\le mI+cP,\qquad P=|\Omega\rangle\langle\Omega|\otimes I_{R_n}.
\tag{5}
$$

Omega is maximally entangled between `R_1...R_q` and Q, each of
dimension `D=2^q`. P has rank one before the last reference spectator
and rank two after it.

If c=0, one local u_i equals r and the triangle argument again
suffices. For c>0 define

$$
t_0=2+r-v>2,\qquad
2q+r-m\ge t_0,
\tag{6}
$$

where the inequality follows from `U-u<=2(q-1)`.
It is enough to prove `cP+h_n<=t_0 I`. Positivity of `t_0 I-h_n`
and the positive rank-update criterion give the equivalence

$$
cP+h_n\le t_0 I
\quad\Longleftrightarrow\quad
\frac cD\operatorname{Tr}_Q(t_0 I-h_n)^{-1}\le I_{R_n}.
\tag{7}
$$

Indeed, compressing an operator on `R_n tensor Q` to the
product-Bell vector gives its normalized partial trace over Q.
This retains the entire last-query spectrum.

## 3. The last-query resolvent has a dimension-independent bound

Apply Jordan's lemma to B_n,D_n. Suppose there are k traceless
two-dimensional blocks and `D-2k` scalar blocks.
On a two-dimensional block the local spectrum is `{+/-a,+/-b}`,
where `a^2+b^2=4` and `2>=a>=r>=b>=0`. For t>2,

$$
\operatorname{Tr}_{\mathrm{block}}(tI-h_n)^{-1}
=\left(\frac{t}{t^2-a^2}+\frac{t}{t^2-b^2}\right)I_{R_n}
\le A(t)I_{R_n},
\quad A(t)=\frac{t}{t^2-4}+\frac1t.
\tag{8}
$$

For the equality, expand the resolvent as
`(tI+h_n)(t^2I-h_n^2)^(-1)`. The square has the form
`2I+Y tensor C`, with C proportional to the cross product of the
two memory Bloch directions. C is traceless and orthogonal to both
directions, so all odd partial-trace terms vanish. The remaining
coefficient is the one displayed in (8). This includes arbitrary
complex orientations; commuting traceless endpoints follow directly
or by continuity.

The inequality follows from convexity of `x -> 1/(t^2-x)`:
with `a^2+b^2=4` its sum is maximized at `(a^2,b^2)=(4,0)`.
On a scalar block, `h_n=+/-X_n+/-Z_n` and hence
`(tI-h_n)^(-1)<=I/(t-r)`.
Thus at `t=t_0` the norm of the left side of (7) is at most

$$
\frac{2k}{D}\left[\frac{cA(t)}2\right]
+\left(1-\frac{2k}{D}\right)\left[\frac{c}{t-r}\right].
\tag{9}
$$

This is a convex combination of two quantities at most one.
First, `c=u-v<=2-v=t-r`. Second, `u+v<=2r` gives
`c<=2(r-v)=2(t-2)`. Applying these two bounds separately to
the two terms of A yields

$$
cA(t)\le\frac{2t}{t+2}+1-\frac rt.
\tag{10}
$$

The right side increases with t>0, and `t=2+r-v<=2+r`. Therefore

$$
cA(t)\le
\frac{2(2+r)}{4+r}+1-\frac r{2+r}
=\frac{5(4-r)}7<2.
\tag{11}
$$

Equations (9)–(11) prove (7), so `H<=(2q+r)I`. Conjugating
every reference by Y sends H to -H, proving (2).
No singular inverse is used: the inverse step is only needed at c>0,
where t_0>2. The c=0 case was treated before that step.

## 4. Three inputs: two commuting query algebras suffice

For `n=3,D=4` there is no need to assume a memory tensor
factorization in advance.

**Corollary.** For Hermitian contractions, if any two original query
pairs commute crosswise,

$$
[B_i,B_j]=[B_i,D_j]=[D_i,B_j]=[D_i,D_j]=0
\quad (i\ne j),
\tag{12}
$$

then `||H||<=4+sqrt(2)`, with the third pair arbitrary.
Internal commutation within either pair is not required.

To reduce contractions to reflections, take their spectral convex
decompositions inside their respective generated algebras. This
preserves all four cross-commutation relations. Separate convexity
therefore reduces the corollary to reflections.

Relabel the two commuting algebras as
`A=C*(B_1,D_1)` and `B=C*(B_2,D_2)`. If either pair commutes
internally, the triangle inequality proves the claim. Otherwise,
Jordan's lemma and the standard isotypic decomposition give

$$
Q=\bigoplus_\alpha
\left(\mathbb C^{d_\alpha}\otimes\mathbb C^{m_\alpha}\right),
\quad
\mathcal A=\bigoplus_\alpha(M_{d_\alpha}\otimes I_{m_\alpha}),
\quad
\mathcal A'=\bigoplus_\alpha(I_{d_\alpha}\otimes M_{m_\alpha}),
\quad d_\alpha\in\{1,2\}.
\tag{13}
$$

Equivalent irreducible representations, including equal scalar
characters, are grouped into the multiplicity spaces.
B lies in A'. Noncommutativity of A requires some `d_alpha=2`;
noncommutativity of B requires some `m_beta>=2`.

If one summand has both `d=2` and `m>=2`, dimension four forces
a single `d=m=2` summand. The pairs act on complementary qubit
factors, and (2) with q=2 applies.

Otherwise the `d=2,m=1` summand uses two dimensions, and the other
pair's noncommutativity must lie in a separate `d=1,m=2` summand.
Both original pairs then have at most one noncommuting Jordan block;
the third has at most two. The
[one-double-block theorem](SINGLE_DOUBLE_BLOCK_CONVERSE.md) applies.
These alternatives exhaust dimension four.

Consequently a strict improvement requires all three original query
algebras to be pairwise noncommuting in every score-attaining
reflection family. A single nonzero cross commutator for each pair
of algebras is only a necessary condition; it is not evidence of
an advantage.

## 5. Operational transfer and exact conditional optimum

For the original task, a refined branch has arbitrary Kraus map K_a
and branch-dependent binary readouts. Put

$$
p_a=\frac{\|K_a\|_F^2}{2^n},\qquad
L_a=\frac{K_a}{\|K_a\|_F},\qquad \sum_a p_a=1.
\tag{14}
$$

Zero branches are omitted. The p_a are normalization weights, not
asserted input-independent outcome probabilities.
The decoded branch score is
`s_a=sum_j Tr(B_(a,j) L_a P_j L_a^dagger)`.
Vectorization and (2) bound s_a for any normalized seed whenever
that branch's readouts satisfy the factor condition. Standard Pauli
coefficient averaging gives

$$
2n\eta\le\sum_a p_a s_a\le2q+\sqrt2,\qquad
\boxed{\eta\le\frac{q+1/\sqrt2}{q+1}.}
\tag{15}
$$

For each branch, the q dedicated queried sites, memory factorization,
and readouts may differ. The encoder itself is unrestricted.
This statement concerns a specified decoder class. Separately,
the full trace-norm seed score is bounded whenever it admits even
one score-attaining family in that class. A violating unrestricted
seed must evade it in every optimal family.

Uniform random retention attains (15) inside the class. Select which
one of the n=q+1 sites to discard, uniformly. On that site use the
four-outcome POVM

$$
F_{ab}=\frac14\left[I+\frac{aX+bZ}{\sqrt2}\right],
\qquad a,b\in\{+1,-1\}.
\tag{16}
$$

Retain the other q input qubits. Record the discarded site and a,b
classically; answer its delayed X or Z query by a or b. All retained
queries are measured only when requested. The resulting effective
observables are exactly `eta X_i,eta Z_i` with eta in (15), for
every input state, including entangled inputs.

This uses one unknown specimen and exactly one delayed query.
It preserves unlimited finite classical records, worst-case quantum
dimension `2^q`, and uniform binary total-variation error
`epsilon=(1-eta)/2`. No extra copies, quantum bypass, preshared
entanglement, input description, or postselected success is introduced.

## 6. Why the simpler positive-projector extension fails

The previous positive cap for the last pair cannot replace its
resolvent in this proof. At q=2 let the first two terms be exact
Pauli readouts on complementary memory qubits. Their product-Bell
top vector Omega has eigenvalue four and memory marginal I_4/4.
For any rank-one Bell projector Pi between the third reference
and a memory plane,

$$
P\Pi P=\tfrac18P,\qquad
\lambda_{\max}(h_1+h_2+\delta\Pi)\ge4+\delta/8>4,
\quad \delta=2-\sqrt2.
\tag{17}
$$

Even when the third pair has at most one noncommuting Jordan block,
its valid local cap `h_3<=sqrt(2)I+delta Pi` gives an upper-bound
operator already above the target, with two perfectly separate
stored qubits. This is a counterexample to that proof
extension, not to the physical interface bound. Retaining the full
last-query resolvent repairs exactly this loss.

## 7. Established ingredients, supplied deductions, and remaining work

Jordan's lemma, extremal binary measurements, finite-dimensional
commutant decomposition, product spectra, and the positive rank-update
criterion are established ingredients. Their uses are proved or
spelled out above. The supplied deductions are (2), its conditional
operational optimum, and the ququart corollary (12).

The closest inspected overlapping-measurement comparison is Bermejo
Morán–Pozas-Kerstjens–Huber, PRL 131, 080201 (2023),
[2303.02127v3](https://arxiv.org/pdf/2303.02127), Eq. (2), p. 2;
Table I, p. 3; Appendix C, p. 7. Its K_2 relaxation allows reuse of
Alice's query pair and attains six. Here the trusted pairs
belong to distinct reference qubits. See the explicit assumption map in
[LITERATURE_COMPARISON.md](../LITERATURE_COMPARISON.md).

This theorem is distinct from the earlier
[all-pair commutation/anticommutation theorem](WEIGHTED_DECODER_ALLOCATION.md):
the additional pair here can be an arbitrary joint-memory binary
measurement. Neither decoder hypothesis can be silently imposed on
the unrestricted optimization.

At `(n,q)=(3,2)` all three full patterns
`(22)^2(11)`, `(22)^2(12)`, and `(22)^3` retain unresolved regions.
Combining current results, a strict improvement needs a nonflat
rank-four seed, at least two double-block optimal pairs, pairwise
noncommuting original query algebras, and failure of the existing
all-block scalar certificate. These are necessary conditions only.
The next target is the interaction of genuinely different,
noncommuting memory-subsystem embeddings.

No general equal-accuracy optimum, entropy inequality, rate evaluation,
full accuracy region, or publication-priority certificate follows.
The prior nonlinear-CHSH subsumption remains in force. Originality
of the explicit two-parameter evaluation is not settled by this result.

## 8. Verification and provenance

The complementary-factor proof, general-q extension and commuting-algebra
classification received independent internal reconstructions, including
all endpoint cases, normalized partial-trace factors, arbitrary complex
orientations, contraction reductions and operational quantifiers.
These are workspace checks, not external peer review.

[The diagnostic](../../tools/check_commuting_query_algebras.py) and
[its recorded output](../../results/commuting_query_algebras.json)
check small explicit constructions, normalized resolvent compression,
spectral caps, scalar inequalities, and the positive-cap obstruction.
The environment, actual counts, residuals, source hash and rerun record
are in [REPRODUCIBILITY.md](../REPRODUCIBILITY.md#commuting-query-algebras).
There is no optimizer or large simulation in this verification.
Numerical checks supplement the supplied proof and certify no originality.

LICENSE and the historical `PROOF_AND_NOVELTY_AUDIT.md` are unchanged.
Earlier commit-pinned reports remain historical records; the current
claim ledger records this additional converse and its limits.
