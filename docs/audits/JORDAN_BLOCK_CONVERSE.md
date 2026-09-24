# A converse from one noncommuting Jordan block per query pair

Date: 24 September 2026. Reviewed main:
`012bafa1895a66e22eac676ba1702a2bde531881`.

**Verdict.** Every three-input normalized seed of rank at most three
obeys the two-retained-qubit benchmark:

$$
\boxed{\Gamma(3,3)\le4+\sqrt2.}
\tag{1}
$$

This covers arbitrary complex eigenvectors and nonuniform spectra, with
no common antiunitary assumption. The same proof excludes four of the
ten nonscalar ququart readout-signature patterns. Six patterns remain;
unrestricted `Gamma(3,4)`, the equal-accuracy rate, and publication
originality are not settled. Equation (1) is an upper bound, not an
evaluation of the qutrit optimum or of the sharper balanced quadratic
conjecture.

The short argument is that each local qutrit Hamiltonian has at most
one eigenvalue above its classical bound. Its eigenvector is maximally
entangled. The resulting projectors for different reference qubits have
overlap at most one half, even when their memory planes differ. Their
sum has norm at most two. This directly controls the original linear
score without solving the stronger quadratic conjecture.

## 1. Weighted statement

Consider n reference qubits and a finite-dimensional memory Q. For
nonnegative weights a_i,b_i and Hermitian reflections B_i,D_i on Q set

$$
H=\sum_i h_i,\qquad h_i=a_iX_i\otimes B_i+b_iZ_i\otimes D_i,
$$

$$
r_i=\sqrt{a_i^2+b_i^2},\qquad
\delta_i=a_i+b_i-r_i,\qquad v_i=\sqrt{\delta_i},\qquad
G_\delta=\frac{\operatorname{diag}(\delta)+vv^T}{2}.
\tag{2}
$$

Suppose each pair `(B_i,D_i)` admits a simultaneous Jordan decomposition
with at most one noncommuting two-dimensional block. All other blocks
can be taken one-dimensional. Different sites may have completely
different decompositions and memory planes.

**Theorem.** Under this readout condition,

$$
\boxed{\|H\|_\infty\le\sum_i r_i+\lambda_{\max}(G_\delta)
\le\sum_i r_i+\frac{\sum_i\delta_i+\max_i\delta_i}{2}.}
\tag{3}
$$

Every pair of qutrit reflections satisfies the condition. In dimension
at most three, (3) consequently holds for all Hermitian contractions
as well, by separate convexity and extremal reflection reduction.
This contraction extension asserts no Jordan decomposition for a pair
of general contractions in larger memory dimension.

For n=3, order the deficits as `delta_(1)>=delta_(2)>=delta_(3)`. Then

$$
\frac{\sum_i\delta_i+\max_i\delta_i}{2}
=\delta_{(1)}+\frac{\delta_{(2)}+\delta_{(3)}}2
\le\delta_{(1)}+\delta_{(2)}.
\tag{4}
$$

The last bound is exactly the weighted support of retaining the two
original sites with largest deficits. Thus all qutrit protocols obey
that comparison-class support bound for every nonnegative query
weighting. No equality or optimal qutrit accuracy region is claimed.
For unit weights (3) gives `3sqrt(2)+2(2-sqrt(2))=4+sqrt(2)`.

## 2. One local pair needs only one Bell projector

Jordan's lemma decomposes two reflections into common invariant spaces
of dimension at most two. On each one-dimensional space their values
are scalar signs, so the reference Hamiltonian has eigenvalues `+/-r_i`.
On a noncommuting two-dimensional space both reflections are traceless
qubit observables.

Independent local rotations on the reference and this memory plane put
their bilinear Hamiltonian into

$$
s_1 X\otimes X+s_2 Z\otimes Z,\qquad
s_1,s_2\ge0,\qquad s_1^2+s_2^2=r_i^2.
\tag{5}
$$

This follows by singular-value decomposition of its real correlation
matrix, whose rank is at most two. Its eigenvalues are
`+/-(s_1+s_2)` and `+/-(s_1-s_2)`. The largest is
`u_i=s_1+s_2<=a_i+b_i`, while all the others are at most r_i.
If `u_i>r_i`, the top eigenvector is unique and maximally entangled
between the reference qubit and that memory plane. Denote its projector
by Pi_i, with identity on all other references suppressed. Therefore

$$
h_i\le r_i I+(u_i-r_i)\Pi_i
\le r_i I+\delta_i\Pi_i.
\tag{6}
$$

If no positive excess exists, `h_i<=r_i I`; one can use any Bell
projector in a memory plane in the weaker last bound. Dimension-one
memory is entirely scalar and satisfies (3) directly. Zero weights and
commuting pairs need no positive correction. The rotations in (5)
are an algebraic diagonalization, not extra operations in the protocol.

The condition of at most one noncommuting block is what makes the
positive correction a single rank-one projector on `R_i tensor Q`.
It does not require a common block for different i.

## 3. Different memory planes still have overlap at most one half

Write the normalized vector defining Pi_i as

$$
|\phi_i\rangle=\frac1{\sqrt2}\sum_{a=0}^1
|a\rangle_{R_i}V_i|a\rangle_Q,
\qquad V_i^\dagger V_i=I_2.
\tag{7}
$$

A reference-basis rotation can be absorbed into the isometry V_i.
Let E_i insert phi_i and leave all other reference qubits unchanged,
so `Pi_i=E_i E_i^dagger`. For i different from j, contraction of the
memory index leaves, up to transposition and spectator identities,
`V_i^dagger V_j/2`. Consequently

$$
\|E_i^\dagger E_j\|_\infty\le\frac12,
\qquad \|\Pi_i\Pi_j\|_\infty\le\frac12.
\tag{8}
$$

The estimate holds in any ambient memory dimension. Equal planes,
real vectors, and simultaneous readout execution are unnecessary.

For arbitrary vectors x_i in the insertion domains put `y_i=||x_i||`.
The Gram matrix of the column map with blocks `sqrt(delta_i) E_i`
satisfies

$$
\begin{aligned}
\left\|\sum_i\sqrt{\delta_i}E_i x_i\right\|^2
&\le\sum_i\delta_i y_i^2+
\sum_{i<j}\sqrt{\delta_i\delta_j}\,y_i y_j\\
&=y^T G_\delta y.
\end{aligned}
\tag{9}
$$

The nonzero spectra of the two Gram products agree. Hence

$$
\left\|\sum_i\delta_i\Pi_i\right\|_\infty
\le\lambda_{\max}(G_\delta)
\le\frac{\max_i\delta_i+\sum_i\delta_i}{2}.
\tag{10}
$$

The final step bounds the diagonal and rank-one terms of G separately.
Summing (6) proves the upper spectral bound in (3). Conjugating all
reference qubits by Y sends H to -H, so it is also an operator-norm
bound. Signs of real query weights can alternatively be absorbed into
the reflections.

## 4. Every rank-three seed and four ququart sectors are excluded

The normalized-seed reduction gives

$$
g(L)=\sum_{i=1}^3\sum_{U=X_i,Z_i}\|LUL^\dagger\|_1,
\qquad \|L\|_F=1.
\tag{11}
$$

If L has rank at most three, choose an output isometry onto its image.
The six compressed operators then live on a memory of dimension at
most three. Their trace norms admit arbitrary Hermitian contraction
dual readouts; maximization is attained at reflections. Applying (3)
proves (1) for every such seed, without a condition on its spectrum,
eigenvectors, or sign pattern. These are full trace norms, not the
balanced-readout scores of the preceding continuation.

For a complete instrument, omit zero Kraus branches and set
`L_a=K_a/||K_a||_F`, `p_a=||K_a||_F^2/8`. The p_a sum to one.
The normalized-Kraus converse gives `6 eta<=sum_a p_a g(L_a)`.
Thus any protocol all of whose refined branch maps have rank at most
three obeys the benchmark, with arbitrary collective encoding and
unlimited finite classical records. A protocol improving the benchmark
must contain a rank-four branch. No branch is postselected.

The readout proof covers additional rank-four seeds. A ququart
reflection with minority eigenspace rank one permits at most one
noncommuting Jordan block with any other reflection: every such block
uses a direction of that minority eigenspace. Consequently the four
unordered nonscalar patterns containing only pair types `(1,1)` and
`(1,2)` obey (3):

$$
(11)^3,\qquad(11)^2(12),\qquad(11)(12)^2,\qquad(12)^3.
\tag{12}
$$

Here the digits are the two minority ranks, as in the earlier
[ten-sector reduction](DECODER_ALGEBRA_AND_THREE_INPUT.md), Section 6.
A balanced `(2,2)` pair is also covered when its actual decomposition
has at most one noncommuting block. A scalar readout already bounds its
site by r_i; adding `a_i+b_i` for the other two sites gives the
two-retained-site support directly.

Exactly six full continuous signature patterns therefore remain in
the reduction for `Gamma(3,4)`. Each contains at least one `(2,2)` site.
Together with the earlier [flat-seed theorem](../FLAT_HALF_RANK_OPTIMALITY.md),
any strict improvement in the `(n,q)=(3,2)` block requires a nonflat rank-four seed
and an optimal readout family with a pair having two noncommuting
Jordan blocks. This is a necessary condition, not a proposed encoder
restriction. Neither the unrestricted entropy inequality nor the
asymptotic equal-accuracy rate follows from (1).

## 5. Why one double block defeats the immediate extension

The tempting extension `||Pi_1+Pi_2+Pi_3||<=2` becomes false when even
one local correction includes two Bell projectors. Let the memory be
`Q=A tensor B`, with both factors qubits, and put

$$
\Pi_1=\Phi_{R_1A}\otimes I_B,\qquad
\Pi_2=|0\rangle\langle0|_A\otimes\Phi_{R_2B},\qquad
\Pi_3=|0\rangle\langle0|_A\otimes\Phi_{R_3B},
\tag{13}
$$

where Phi is a Bell projector and unused reference identities are
suppressed. The first edge projector has rank two on `R_1 tensor Q`.
For `T=Phi_(R_2B)+Phi_(R_3B)`, the maximum eigenvalue is 3/2, by the
same two-projector overlap calculation. On a T-eigenspace with value t,
the sum in (13) has the following block on `|00>,|11>` of `R_1A`:

$$
\begin{pmatrix}t+1/2&1/2\\1/2&1/2\end{pmatrix}.
$$

The other two eigenvalues on `R_1A` are 0 and t. The largest eigenvalue
of the displayed block dominates both and increases with t. Its maximum
occurs at t=3/2, giving exactly

$$
\boxed{\|\Pi_1+\Pi_2+\Pi_3\|_\infty
=\frac{5+\sqrt{13}}4>2.}
\tag{14}
$$

This is a counterexample to an intermediate projector bound, not to
the interface conjecture. For example, realize Pi_1 with X_A,Z_A and
realize the other pairs with X_B,Z_B conditioned on A=0, using scalar
readouts when A=1. The last two site Hamiltonians together have norm
at most `2sqrt(2)` by the qubit monogamy bound in the first condition
and directly in the scalar condition. The full actual Hamiltonian is
therefore at most `2+2sqrt(2)`. The projector replacement discarded
negative spectral information needed to control this extension.

## 6. Primary-source comparison and evidence

Jordan reduction and singular-value diagonalization are established
ingredients. The Bell-projector overlap mechanism is also prior:
Kay–Kaszlikowski–Ramanathan, *Optimal Cloning and Singlet Monogamy*,
PRL 103, 050501 (2009), [arXiv:0901.3626v3](https://arxiv.org/pdf/0901.3626),
Eqs. (3)–(6), pp. 2–3, studies weighted Bell projectors with overlap
factor 1/d. That version explicitly leaves the fully general asymmetric
ansatz unproved, while identifying proved small cases. Our elementary
upper bound uses no unproved part of that ansatz.

Jorquera et al., *Monogamy of Entanglement Bounds and Improved
Approximation Algorithms for Qudit Hamiltonians*, Quantum 10, 2088
(2026), [arXiv:2410.15544v4](https://arxiv.org/pdf/2410.15544),
Lemma 3.4/Eq. (8), printed p. 7, and Proposition 3.6/Eq. (18),
printed p. 8, give the star bound for equal-dimensional, independently
rotated maximally entangled edge projectors. Theorem 3.7, p. 9, gives
unweighted attainment. Equation numbers here follow the PDF, whose
title page identifies v4, 20 April 2026. Their d=2, three-edge constant
is already two. The present varying memory planes do not match their
equal-dimension hypothesis literally; (7)–(10) supply the required
ordinary-operator upper bound. No extension of their pseudo-density
or sum-of-squares theorem is asserted.

The supplied deduction is the local spectral majorant applied to this
interface task, including arbitrary qutrit spectra and the four ququart
sectors. It is not a new singlet-monogamy principle. A scoped comparison
does not certify exhaustive originality or PRL-level significance.

Independent internal reconstructions checked the local Bell eigenvector,
degenerate and zero-weight cases, arbitrary complex memory planes,
weighted Gram comparison, full trace-norm and Kraus transfer, sector
count, and exact failure (14). The small construction checks are in
[`check_jordan_block_converse.py`](../../tools/check_jordan_block_converse.py)
and [`jordan_block_converse.json`](../../results/jordan_block_converse.json).
They supplement the symbolic proof and establish no general optimum
or priority claim. The stronger balanced quadratic conjecture remains
unproved and is not used in (1).

All 84 weighted construction cases passed: eight dense complex qutrit
families, four scalar qutrit controls, and sixteen ququart families across
the four excluded signatures, each with three weight choices. A parent
workspace rerun reproduced the result JSON byte-for-byte with Python
3.12.14 and NumPy 2.3.5. These deterministic diagnostics also check (14)
and its actual Hamiltonian, whose norm is approximately 4.7396401073.
No optimizer or large simulation is used. See the
[reproducibility record](../REPRODUCIBILITY.md#jordan-block-converse).
