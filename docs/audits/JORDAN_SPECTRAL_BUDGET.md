# A scalar spectral bound with every Jordan block retained

Date: 24 September 2026. Reviewed main:
`780605b723919defd382d88c8adb09ed1fd8d204`.

**Verdict.** The preceding rank-three proof extends to a quantitative
certificate for arbitrary reflection pairs, including two noncommuting
blocks per pair. It excludes continuous families inside the remaining
ququart sectors, including families in the fully balanced sector.
No additional whole signature sector is closed: all six retain unresolved
regions. A separate exact obstruction shows that penalizing only the
most negative Bell eigenvectors cannot repair the earlier projector bound,
regardless of the finite penalty coefficient.

The simple principle is to charge each block its actual spectral excess
above the classical score. Same-site blocks are orthogonal, while
different-site Bell vectors have overlap at most one half. The resulting
matrix bound reduces to one scalar inequality. This is a supplied
application of established projector geometry and elementary linear
algebra, not a new general monogamy principle or a novelty certificate.

## 1. Weighted theorem for all blocks

Let n reference qubits share a finite-dimensional memory Q, with
Hermitian reflection readouts B_i,D_i and weights a_i,b_i>=0. Set

$$
H=\sum_i h_i,\qquad h_i=a_iX_i\otimes B_i+b_iZ_i\otimes D_i,
\qquad r_i=\sqrt{a_i^2+b_i^2}.
$$

For each noncommuting two-dimensional Jordan block k of pair i, let
u_(i,k) be the largest eigenvalue of h_i on that reference-block space.
Define its excess

$$
\alpha_{ik}=u_{ik}-r_i\ge0.
\tag{1}
$$

Discard zero excesses. In particular, scalar blocks and zero-weight
pairs need no correction. If theta_(i,k) is the angle between the
block's two Pauli directions, then

$$
u_{ik}=\sqrt{r_i^2+2a_i b_i|\sin\theta_{ik}|},\qquad
0\le\alpha_{ik}\le a_i+b_i-r_i.
\tag{2}
$$

For any positive Lambda strictly larger than every retained alpha, define

$$
C_i(\Lambda)=\sum_k\frac{\alpha_{ik}}{\Lambda-\alpha_{ik}},
\qquad
\mathcal B(\Lambda)=\sum_i\frac{C_i(\Lambda)}{2+C_i(\Lambda)}.
\tag{3}
$$

An empty sum is zero. **Theorem:**

$$
\boxed{\mathcal B(\Lambda)\le1
\quad\Longrightarrow\quad
\|H\|_\infty\le\sum_i r_i+\Lambda.}
\tag{4}
$$

There is no common Jordan decomposition, common memory plane, or common
antiunitary assumption. The theorem concerns reflection readouts.
A general contraction decomposition need not preserve (3); no such
extension is asserted for a readout family satisfying a spectral condition.

## 2. Proof by a Gram matrix and one rank-one update

On a noncommuting block the local spectrum is `+/-u,+/-v`, where
`u>=r_i>=v>=0`. The unique eigenvector above r_i, when present, is
maximally entangled between its reference and its two-dimensional memory
plane. Denote its projector by Pi_(i,k), with spectator identities
understood. The local spectral decomposition gives

$$
h_i\le r_i I+\sum_k\alpha_{ik}\Pi_{ik}.
\tag{5}
$$

Use insertion isometries E_(i,k) with `Pi_(i,k)=E_(i,k)E_(i,k)^dagger`,
as in the [preceding proof](JORDAN_BLOCK_CONVERSE.md), Section 3.
For k different from l at the same site, orthogonal memory blocks give
`E_(i,k)^dagger E_(i,l)=0`. Across different sites the norm is at most
one half, including arbitrary complex orientations of the memory planes.
The weighted insertion map is therefore bounded by the scalar matrix G:

$$
G_{ik,jl}=\begin{cases}
\alpha_{ik},&(i,k)=(j,l),\\
0,&i=j,\ k\ne l,\\
\tfrac12\sqrt{\alpha_{ik}\alpha_{jl}},&i\ne j.
\end{cases}
\tag{6}
$$

Taking norms of insertion-domain vector blocks, exactly as in the previous
Gram proof, yields `||sum alpha Pi||<=lambda_max(G)`.

Write v_i for the vector of square roots of the excesses at site i and
v for their concatenation. Then

$$
\Lambda I-G=A-\frac12vv^T,\qquad
A=\bigoplus_i\left[
\operatorname{diag}_k(\Lambda-\alpha_{ik})+\frac12v_iv_i^T\right]>0.
\tag{7}
$$

The rank-one positive-semidefinite criterion and the Sherman–Morrison
identity give

$$
G\le\Lambda I
\iff\frac12v^TA^{-1}v\le1
\iff\sum_i\frac{C_i(\Lambda)}{2+C_i(\Lambda)}\le1.
\tag{8}
$$

Summing (5) proves the upper spectral bound. Conjugating every reference
by Y sends H to -H, proving (4). Equation (8) is an equivalence for G;
it is only a sufficient test for the physical Hamiltonian. A failed test
is not a violating seed. If there are no positive excesses, (5) gives
the classical bound directly.

## 3. The three-input benchmark and a simple two-block boundary

For unit weights put `r=sqrt(2)` and `delta=2-sqrt(2)`. At most two
positive excesses occur per ququart pair. Write `x_(i,k)=alpha_(i,k)/delta`,
so every x lies in (0,1]. Choose `Lambda=2 delta` in (3). The certificate is

$$
\boxed{\sum_{i=1}^3\frac{c_i}{2+c_i}\le1,
\qquad c_i=\sum_k\frac{x_{ik}}{2-x_{ik}}
\quad\Longrightarrow\quad \|H\|\le4+\sqrt2.}
\tag{9}
$$

One block per site has `c_i<=1`, recovering the preceding converse.
Padding missing blocks by zero, write the two strengths at site i as
x_i,y_i. The same certificate has the particularly simple form

$$
\boxed{\sum_{i=1}^3
\frac{x_i+y_i-x_i y_i}{4-x_i-y_i}\le1.}
\tag{9a}
$$

Even more simply, total excess `sum_(i,k) alpha_(i,k)<=3 delta` suffices.
To see this, restore all omitted nonnegative within-site entries of G.
Its largest eigenvalue can only increase, by entrywise comparison for
nonnegative matrices, and the restored matrix is
`(diag(alpha)+vv^T)/2`. Its largest eigenvalue is at most
`(max alpha+sum alpha)/2<=2 delta`. The precise test (9a) is stronger.

With one double-block pair of strengths a,b and two single-block pairs,
even taking both single blocks at their maximum, it suffices that

$$
\boxed{\frac{a}{2-a}+\frac{b}{2-b}\le1
\iff 4(a+b)-3ab\le4.}
\tag{10}
$$

Thus two genuinely noncommuting blocks do not by themselves escape the
converse. For example a=b=1/2 and the other two strengths equal to one
give the stronger bound

$$
\|H\|\le3\sqrt2+\left(1+\frac{\sqrt3}{2}\right)(2-\sqrt2)
<4+\sqrt2.
\tag{11}
$$

Here (6) has largest eigenvalue `(1+sqrt(3)/2)delta`. The direct triangle
bound is `4+(2+sqrt(2))/2`, above the benchmark, so (11) adds information.

There are also exclusions in the fully balanced `(22)^3` sector. If
each pair's two strengths are `(9/10,1/5)`, then `c_i=92/99` and

$$
\sum_i\frac{c_i}{2+c_i}=\frac{138}{145}<1.
\tag{12}
$$

All three pairs have two noncommuting blocks, and their memory rotations
may be chosen independently. Their direct triangle bound is
`3sqrt(2)+(27/10)delta`, again above the benchmark. Their total excess
is `(33/10)delta`, beyond the simpler certificate as well. The exact
comparison eigenvalue is `delta(11+sqrt(67))/10<2 delta`.
Strict inequality in (12) persists under small angle perturbations.
Neither example asserts the optimal norm of its readout class.

For a normalized seed choose reflections attaining all six full trace
norms. If their blocks pass (9), the seed obeys the benchmark. Hence a
violating seed must fail (9) for every optimal reflection family. For a
complete instrument use `p_a=||K_a||_F^2/8` and normalized nonzero Kraus
maps; these weights sum to one. If every refined branch admits a qualifying
optimal family, `6 eta<=sum_a p_a g(L_a)<=4+sqrt(2)`.
This is a sufficient certificate, not a restriction imposed on the original
optimization. Arbitrary collective encoding, unlimited finite classical
records, worst-case quantum dimension, one specimen, one delayed query,
and uniform input/query errors are preserved.

## 4. Every finite negative-top penalty still fails

Could the preceding positive-projector relaxation be repaired just by
keeping the most negative Bell eigenvectors? At unit weights let
`Pi_i^- = Y_i Pi_i^+ Y_i`, summing within each site's active blocks.
The valid local bound

$$
h_i\le rI+\delta\Pi_i^+-2r\Pi_i^-
\tag{13}
$$

would prove the benchmark if
`lambda_max(sum_i(Pi_i^+-kappa Pi_i^-))<=2` at
`kappa=2r/delta=2+2sqrt(2)`. In fact this projector claim fails for
**every finite kappa>=1**, on the same physical block arrangement.

Let `Q=A tensor B`, let Phi project onto `(00+11)/sqrt(2)`, let Psi
project onto `(01-10)/sqrt(2)`, and put `F_kappa=Phi-kappa Psi`.
Set

$$
S_\kappa=F_{R_1A}\otimes I_B+
|0\rangle\langle0|_A\otimes T_\kappa,\qquad
T_\kappa=F_{R_2B}+F_{R_3B}.
\tag{14}
$$

These are the signed projectors from the preceding report's example.
In a Y-eigenbasis put `d=(1-kappa)/2`, `c=(1+kappa)/2`. The zero- and
three-excitation sectors of T are zero. Each of its other two sectors
has, up to local phases, the matrix

$$
\begin{pmatrix}2d&c&c\\c&d&0\\c&0&d\end{pmatrix}.
$$

Thus its maximum eigenvalue is

$$
t_\kappa=\frac{3(1-\kappa)+
\sqrt{(1-\kappa)^2+8(1+\kappa)^2}}4>\frac43.
\tag{15}
$$

For an exact check, the quadratic of its symmetric two-dimensional block
is `p(t)=(t-2d)(t-d)-2c^2`; it satisfies `p(4/3)=-2/9` for every kappa.
Its smaller root is negative, proving the strict inequality.

On a T eigenspace with eigenvalue t, the even computational-parity block
of `R_1A` in (14) is

$$
\begin{pmatrix}t+1/2&1/2\\1/2&1/2\end{pmatrix}.
$$

The odd block is at most `max(t,0)I`, since its other term is negative
semidefinite. The largest eigenvalue of S is consequently exactly

$$
\boxed{\lambda_{\max}(S_\kappa)=
\frac{t_\kappa+1+\sqrt{t_\kappa^2+1}}2>2.}
\tag{16}
$$

At the coefficient in (13), this is approximately 2.023745905865038.
The limit as kappa tends to infinity is two from above. This is an
obstruction also for smaller nonnegative coefficients, by monotonicity
of S_kappa as kappa decreases. It defeats
arbitrary finite strengthening of that particular penalty; it does not
assert that all such coefficients yield valid
local spectral majorants.

The actual realization is `B_1=X_A`, `D_1=Z_A`, with the other two
pairs `X_B,Z_B` conditioned on A=0 and scalar +1 on A=1. Its physical
Hamiltonian has norm at most `2+2sqrt(2)`, as already proved, and is
numerically about 4.7396401073. Equation (16) is therefore a failed
proof step, not an interface counterexample. A repair must use additional
information, such as the middle eigenspaces or scalar-sector directions.
No sufficiency of such a repair is claimed.

## 5. Closer primary-source comparisons

The rank-one overlap argument retains the established provenance in the
[previous source comparison](JORDAN_BLOCK_CONVERSE.md#6-primary-source-comparison-and-evidence).
The block Gram comparison and rank-one update above are elementary
linear algebra applied to that geometry.

Bermejo Morán–Pozas-Kerstjens–Huber, *Bell inequalities with overlapping
measurements*, PRL 131, 080201 (2023),
[arXiv:2303.02127v3](https://arxiv.org/pdf/2303.02127), Eq. (1), p. 2,
Section III/Table I, p. 3, and Appendix B, pp. 5–6, is close prior work
on independently addressed CHSH pairs sharing a dimension-limited center.
Our two-site operator is its J_2 with trusted observables
`(X_i+Z_i)/sqrt(2)` and `(X_i-Z_i)/sqrt(2)`; each CHSH term divided by
sqrt(2) becomes h_i. The reported qutrit upper/lower values meet numerically
near 3.6365. Pairwise averaging yields only about 5.45475 for three sites,
above the analytical `4+sqrt(2)`. Its ququart value four yields only six.
The reported numerical upper bounds retain their computational status.
Its K_2 instead includes overlapping access to the two leaves, not a third
independent leaf. No theorem of that source is claimed to settle our target.

Gour–Wallach, *Entanglement of Subspaces and Error Correcting Codes*,
PRA 76, 042309 (2007),
[arXiv:0704.0251v2](https://arxiv.org/pdf/0704.0251), Proposition 3,
pp. 3–4, and Corollary 4, p. 4, already characterize maximally entangled
subspaces and bound their dimension by `floor(D/2)` here. Two Bell vectors
on orthogonal ququart planes span such a subspace. Equivalently their
sum projector is `U_i(Phi_(R_iA) tensor I_B)U_i^dagger`. Each site can
have a different memory unitary U_i; replacing these by a common qubit
factor is unjustified. This subsystem representation is an established
ingredient, not a new structural theorem.

These comparisons narrow provenance and identify a close physical
precedent. They certify neither exhaustive originality nor PRL significance.
Unrestricted `Gamma(3,4)`, the balanced quadratic conjecture, and the
equal-accuracy entropy/rate questions remain unresolved.

## 6. Verification

Two independent internal reconstructions checked (4), (8), the examples,
and the exact obstruction (16). The construction diagnostic and actual
run record are linked from [reproducibility](../REPRODUCIBILITY.md#jordan-spectral-budget):
[`check_jordan_spectral_budget.py`](../../tools/check_jordan_spectral_budget.py)
and [`jordan_spectral_budget.json`](../../results/jordan_spectral_budget.json).
All 50 construction cases and four signed-spectrum checks passed; parent
and independent reviewer reruns reproduced the JSON byte-for-byte.
Finite checks supplement these proofs; they do not certify optimality or
priority. No large simulation is used.
