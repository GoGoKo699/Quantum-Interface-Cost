# Decoder algebra and the three-input memory problem

Date: 24 September 2026. Reviewed main:
`f46ed69785ace49d6f3f52645fefbb9dbdc99f1f`.

**Verdict.** A supplied all-size converse proves that collective encoding
cannot improve the equal-accuracy retention benchmark when the memory
readout reflections pairwise commute or anticommute. The encoder is
unrestricted. This includes Pauli readouts in any common memory basis.
The proof was independently reconstructed within this workspace.

The unrestricted three-input, two-qubit-memory problem is still open.
Its unresolved part is exactly ten compact continuous optimizations over
four-dimensional readout reflections. A bounded numerical investigation
found no violating seed; this is not a global upper bound. The algebraic
ingredients below are prior, and publication originality is not asserted.

## 1. Operational statement

Keep the existing task: one arbitrary unknown n-qubit specimen, including
internally entangled inputs; unrestricted collective encoding before one
delayed local X/Z query; unlimited finite classical records; every branch
has quantum dimension at most `2^q`; error is uniform over all inputs and
queries. There are no additional copies, source reaccess, free entanglement,
uncharged quantum systems, or postselection.

**Theorem.** Let `0 <= q <= n` be an integer. Suppose each classical branch
uses Hermitian unitary readout observables `B_1,...,B_(2n)` such that every
pair either commutes or anticommutes. Then any attainable common contrast
satisfies

$$
\boxed{\eta\le\frac1{\sqrt2}
 +\left(1-\frac1{\sqrt2}\right)\frac qn.}
\tag{1}
$$

Random retention of q original sites attains equality within this decoder
class. More generally, its separate contrasts obey

$$
\sum_{i=1}^n(x_i+z_i)\le2q+\sqrt2(n-q).
\tag{2}
$$

There is no product, stabilizer, flat-spectrum, or eigenbasis restriction
on the encoder. The explicit restriction is on the readout observables.
Classical mixtures of admissible decoder families are also covered:
include the family choice in the free classical record.

The theorem is not a claim about all Clifford circuits with arbitrary
outcome processing, nor about every non-Pauli measurement. It includes
any family simultaneously conjugate to signed q-qubit Pauli observables,
including scalar signs, and allows more general representations of the
same pairwise relations.

## 2. A prior dimension fact

Let M be the binary commutation matrix of the memory reflections:

$$
B_jB_k=(-1)^{M_{jk}}B_kB_j,
\qquad M\in\mathbb F_2^{2n\times2n}.
$$

It is symmetric with zero diagonal, hence alternating over `F_2`.
If its rank is `2r`, a nonzero representation on dimension D requires

$$
2^r\mid D,\qquad \operatorname{rank}_{\mathbb F_2}M\le2q
\quad\text{when }D\le2^q.
\tag{3}
$$

This is an established graph-Clifford-algebra fact; precise primary
locators are in Section 8. A short proof makes the resource accounting
explicit. An ordered product of the B's, multiplied by a suitable scalar
phase, is again a Hermitian involution. Its commutation sign with another
such product is the bilinear form defined by M. A symplectic basis for the
nondegenerate part gives r commuting involutions `Z_1,...,Z_r` and
involutions `X_1,...,X_r` such that X_k flips the eigenvalue of Z_k and
preserves all the other Z eigenvalues. Products of the X's map every
nonzero joint Z eigenspace onto all `2^r` mutually orthogonal eigenspaces
of the same dimension. This proves the divisibility and (3), including
reducible representations and arbitrary degeneracies.

## 3. The all-size norm bound

Enumerate the reference observables as
`P_1=X_1,P_2=Z_1,...,P_(2n)=Z_n`, and put

$$
T_j=P_j\otimes B_j,\qquad H=\sum_{j=1}^{2n}T_j.
$$

The reference commutation matrix is

$$
J=\bigoplus_{i=1}^n
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad \operatorname{rank}J=2n.
$$

The full terms have binary commutation matrix `A=J+M`, so

$$
\operatorname{rank}A\ge2n-\operatorname{rank}M\ge2(n-q).
\tag{4}
$$

**Elementary matching lemma.** A graph whose adjacency matrix over
`F_2` has rank `2s` contains s disjoint edges. To see this, an alternating
matrix has a nonsingular principal submatrix of size equal to its rank:
successive symmetric pivots on nonzero off-diagonal pairs give this by
induction, with alternating Schur complements. In the determinant of
that principal submatrix, zero diagonal eliminates fixed points, and
cycles of length at least three cancel with their reversals in
characteristic two. The remaining terms are perfect matchings. A nonzero
determinant therefore supplies one on the original vertices.

By (4), choose `n-q` disjoint anticommuting pairs of the T's. Each pair
satisfies `(T_j+T_k)^2=2I`, while an unmatched T has norm one. The triangle
inequality gives

$$
\boxed{\|H\|_\infty\le(n-q)\sqrt2+2q.}
\tag{5}
$$

Different matched pairs need not commute; no such assumption was used.

For a normalized Kraus seed L, vectorization gives
`Tr(B_j L P_j L^dagger)=<L|P_j^T tensor B_j|L>`.
The reference X/Z matrices are real, so (5) bounds its decoded score.
For arbitrary physical Kraus operators K_c, use

$$
p_c=\frac{\|K_c\|_F^2}{2^n},\qquad
L_c=\frac{K_c}{\|K_c\|_F},\qquad\sum_c p_c=1.
$$

Taking Pauli coefficients of the effective observables yields (2) by
p-weighted averaging of the branch bounds. These weights are not assumed
to be input-independent physical outcome probabilities. Uniform-TV
tolerances imply the same contrast bound by finite Pauli twirling;
query relabelings and decoder sign changes preserve the stated algebra.

For equality, retain q sites, use their Pauli readouts, and measure each
discarded site with the compatible bisector parent POVM. Conditioned on
the stored classical outcome, its decoder is a scalar sign. Averaging
the selected subset equalizes the contrasts and attains (1).

### The three-input argument in one paragraph

For `n=3,D<=4`, all six T's cannot commute. Otherwise `M=J` would have
rank six, requiring `D>=8` by (3). Some two T's must therefore
anticommute, and their sum has norm `sqrt(2)`. The other four contribute
at most four. Thus the bound is `4+sqrt(2)`. The matching argument is
what makes this reasoning extend to arbitrary n and q.

## 4. Full accuracy profiles when q=n-1

For this budget the same decoder hypothesis gives the entire weighted
retention support, including the three-input, two-qubit-memory case.
For nonnegative a_i,b_i put

$$
\delta_i=a_i+b_i-\sqrt{a_i^2+b_i^2}.
$$

**Corollary.** When `D<=2^(n-1)`,

$$
\left\|\sum_i(a_iX_i\otimes B_{i,X}+b_iZ_i\otimes B_{i,Z})\right\|_\infty
\le\sum_i(a_i+b_i)-\min_i\delta_i.
\tag{6}
$$

If A contains an original X/Z-pair edge, grouping that anticommuting
pair saves its delta from the sum of the coefficients, proving (6).
Otherwise M contains every edge of the original perfect matching J.
Since `rank M<=2n-2`, its determinant is zero over `F_2`. The
determinant/matching identity therefore implies a second perfect
matching. Its union with J contains an alternating cycle through `k>=2`
original pairs. The k edges of the second matching on that cycle are
disjoint cross-pair edges of A.

Let m be the smallest query coefficient on the cycle. Grouping those
edges saves at least `k(2-sqrt(2))m >= m`: the pair saving
`u+v-sqrt(u^2+v^2)` is increasing in both nonnegative arguments and is
at least `(2-sqrt(2))m` when `u,v>=m`. The original pair containing the
coefficient m has `delta_i<=m`; thus the saved amount is at least
`min_i delta_i`. Zero coefficients cause no difficulty. This proves (6).

Kraus averaging transfers (6) to every profile of the stated decoder
class. Conversely, retain all but a site minimizing delta and use its
compatible disk point to attain the support function. The
[retention-region geometry](../EXACT_AXIS_SPECTRAL_REDUCTION.md) therefore
gives exactly

$$
\sum_i w(x_i,z_i)\le n-1,\qquad
w(x,z)=\left[x+z-1-\sqrt{2(1-x)(1-z)}\right]_+.
\tag{7}
$$

This full-profile conclusion is proved here for `q=n-1`; the all-q
theorem in Section 1 concerns the equal-weight score. No general
all-q weighted extension is asserted.

## 5. Why the readout hypothesis is substantive

It is false that every normalized seed admits trace-norm-optimal
readouts of this form. For one input qubit take

$$
\rho=\frac12\left(I+\frac{X+Z}{2}\right),\qquad
L=\sqrt\rho,\qquad s=1/\sqrt2.
$$

Its invertible, indefinite compressed observables have unique optimal
sign decoders

$$
B_X=\frac{(1+s)X+(1-s)Z}{\sqrt3},\qquad
B_Z=\frac{(1-s)X+(1+s)Z}{\sqrt3}.
$$

Their anticommutator is `(2/3)I`, and their commutator is nonzero.
Thus they neither commute nor anticommute. The seed score is only
`sqrt(3)`, so this is an obstruction to a per-seed decoder replacement,
not an advantage witness. It does not rule out a separate theorem about
the existence of a different global optimizing seed. No such theorem
is supplied for the unresolved integer-memory cases.

Consequently any violating seed must have **no** optimal decoder family
satisfying the pairwise hypothesis. Having a pair outside that hypothesis
is necessary but not sufficient for an advantage.

## 6. Exact reduction of the remaining three-input case

The existing [spectral seed reduction](../COLLECTIVE_ENCODING_REDUCTION.md)
gives

$$
\Gamma(3,4)=\max_{B_j=B_j^\dagger,\ B_j^2=I_4}
\lambda_{\max}\!\left(\sum_{j=1}^{6}P_j\otimes B_j\right).
\tag{8}
$$

Extreme Hermitian contractions are reflections; dimension-smaller seeds
are padded to four without losing any protocols.

If any B_j is scalar, its two-query site operator h_i obeys `h_i^2=2I`.
The other two site operators each have norm at most two. Every sector
containing a scalar decoder is therefore bounded by `4+sqrt(2)`.

Otherwise, the positive-eigenspace ranks are 1, 2, or 3. Independent
decoder sign flips are absorbed by Pauli conjugations on the reference,
so ranks 3 can be replaced by ranks 1 without changing the optimized
spectrum. Local Hadamards exchange X/Z, and site permutations exchange
the three pairs. Thus only multisets of three site-types remain:

$$
(1,1),\quad(1,2),\quad(2,2).
$$

There are exactly ten. For each pattern t let M_t be the maximum in (8)
with those ranks fixed. Each domain is a product of compact unitary
orbits, so its maximum exists. Exactly,

$$
\boxed{\Gamma(3,4)=\max\{4+\sqrt2,\ \max_{t=1}^{10}M_t\}.}
\tag{9}
$$

This retains every continuous decoder orientation. The ten-pattern
reduction is not a finite enumeration of all physical encoders and is
not a proof of any M_t upper bound.

## 7. Bounded diagnostics

The reproducible script
[`check_three_input_decoders.py`](../../tools/check_three_input_decoders.py)
uses small complex normalized seeds and alternating optimization of
readouts and the top Hamiltonian eigenvector. It performs 128 unrestricted
runs, including rank-three outputs and perturbed subset seeds, then 12
starts in each of the ten nonscalar sectors. Recorded results are in
[`three_input_decoders.json`](../../results/three_input_decoders.json).

No certified violation was obtained. The best unrestricted score agrees
with `4+sqrt(2)` to floating-point precision. The largest fixed-sector
score observed is `3sqrt(3)`, already attained by the nonuniform
bisector-star support in the
[existing exact example](../NONUNIFORM_SUPPORT_OPTIMA.md).
Neither observation is a sector optimum or an unrestricted upper bound.

The comparison (5) is proved analytically and does not depend on these
searches. No large-register simulation, solver certificate, or exhaustive
search of continuous matrices is claimed.

## 8. Primary-source comparison and claim boundaries

| Ingredient or nearby result | Precise source | Consequence and limitation |
|---|---|---|
| Graph-Clifford representation dimension | Tanya Khovanova, [arXiv:0810.3322v1](https://arxiv.org/pdf/0810.3322v1), Section 2, p. 2; Corollary 7.4, p. 9; Lemma 8.1 and Corollary 8.2, p. 10 | Rescale reflections by i to match generators squaring to -1. Binary adjacency rank 2r gives simple blocks Mat_(2^r)(C), hence irreducible representation dimension 2^r. Equation (3) is prior algebra. |
| Modern quantum-measurement restatement | Daniel McNulty, [arXiv:2511.15954v1](https://arxiv.org/pdf/2511.15954v1), Definition 1/Eq. (4), p. 3; Appendix B, Remark 1/Eq. (B4), p. 15 | The identical complete commute/anticommute pattern and minimum dimension are explicit, with credit to Khovanova. Its inspected incompatibility-robustness and graph-norm results do not state the present memory-allocation conclusion. |
| Parallel CHSH self-testing | Andrea Coladangelo, [arXiv:1609.03687v2](https://arxiv.org/pdf/1609.03687v2), Eqs. (14)–(18), pp. 6–7; Theorems 3.1 and 3.4, pp. 7–8 and 11–12 | Its score theorems use joint n-bit outputs and corresponding common-projector marginals. Those hypotheses are absent from six independent delayed binary queries. The near-perfect operator lemmas may be useful with additional checks, but supply no sharp dimension-four value here. |

The representation-rank fact, the elementary matching lemma, and the
norm of an anticommuting pair are established ingredients. Combining
them with `A=J+M` and normalized Kraus averaging gives the supplied
all-size restricted-readout deduction. No direct prior statement of
this combined allocation consequence was identified in the bounded
comparison; this is not exhaustive originality evidence.

The single-query task has not been replaced by simultaneous execution
of its decoders. The general encoder optimization remains unrestricted.
The next unresolved analytical step is control of the ten full decoder
orbits in (9), including pairs that neither commute nor anticommute.
The unrestricted equal-accuracy rate and its midpoint benchmark remain
open, as does the publication significance of these deductions.
