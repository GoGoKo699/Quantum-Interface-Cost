# Exact trade-off with one retained qubit

Date: 22 September 2026. Research base: `df45e2eaceb5669cfff9ac063d3da845d622dac3`.

**Status:** supplied analytical deduction, independently checked within this workspace. The key inequality is an established theorem of Cheng–Hall; this is not a new monogamy theorem or a certification of publication novelty. The operational model and the normalized-seed reduction are unchanged.

## 1. Result

For every integer `n>=1`, arbitrary collective encoding into one retained qubit and unlimited finite classical information has optimal uniform local X/Z contrast

$$
\boxed{\eta_{\max}(n,1)=\frac1{\sqrt2}
+\frac1n\left(1-\frac1{\sqrt2}\right).}
$$

Equivalently, for the unrestricted complex-seed optimization,

$$
\boxed{\Gamma(n,2)=2+\sqrt2(n-1).}
$$

The random-subset construction attains this value. Thus collective encoding cannot improve its performance when the worst-case retained quantum dimension is at most two. The theorem includes internally entangled inputs, arbitrary finite classical records, branch-dependent decoders, nonisometric encoders, complex matrices, and unequal singular values.

In particular, the formerly open diagnostic `(n,q)=(2,1)` is settled:

$$
\eta_{\max}(2,1)=\frac{1+1/\sqrt2}{2}.
$$

This solves the entire two-input-qubit memory function: zero qubits suffice up to `eta0=1/sqrt(2)`, one qubit is necessary and sufficient for `eta0<eta<=(1+eta0)/2`, and two qubits are necessary and sufficient above that value through `eta=1`. For general n, the analogous first nonclassical interval has exact memory one; above it at least two qubits are necessary. No claim for optimality at `2<=q<n` follows.

## 2. Prior theorem and its exact scope

Cheng–Hall, *Anisotropic invariance and the distribution of quantum correlations*, [arXiv:1610.09302v3](https://arxiv.org/abs/1610.09302v3), 25 January 2017; [PRL 118, 010401 (2017)](https://doi.org/10.1103/PhysRevLett.118.010401).

Equation (1), PDF p. 1, gives for any three-qubit state

$$
\langle\mathcal B_{AB}\rangle^2+
\langle\mathcal B_{AC}\rangle^2\le8,
$$

where the two CHSH tests may use **different measurement directions on the common qubit A**. Equations (13)–(14), PDF p. 3, prove the corresponding optimized correlation bound; the following paragraph extends it to mixed states by convexity. These two qualifications are essential: our memory decoders depend on the queried site, and a three-qubit marginal of a larger seed can be mixed. The older same-observable monogamy statement alone would not justify this application.

The [publisher's note, PRL 118, 059901 (2017)](https://doi.org/10.1103/PhysRevLett.118.059901), corrects the paper's description of its invariants, not the inequality used here. The v3 source was checked alongside that note.

The reduction from this established inequality to the exact interface bound is supplied below. Neither the source nor this review is claimed to have established the unrestricted many-qubit-memory rate.

## 3. Reduction to extreme qubit decoders

The audited variational formulation is

$$
\Gamma(n,2)=\max_{-I\le B_{i,b}\le I}
\lambda_{\max}\left[\sum_i
\left(X_i\otimes B_{i,X}+Z_i\otimes B_{i,Z}\right)\right].
$$

The reference X/Z matrices are real, so the transpose in the general vectorization formula is suppressed. All B are Hermitian two-by-two matrices. For fixed seed state the objective is linear separately in every B; equivalently, the spectral maximum is convex separately in each B. A maximum can therefore be attained with every B an extreme point of the Hermitian contraction ball. In two dimensions these are exactly

$$
B=+I,\quad B=-I,\quad\text{or}\quad B=\mathbf b\cdot\boldsymbol\sigma,
\qquad |\mathbf b|=1.
$$

Indeed an eigenvalue strictly between -1 and 1 admits a nontrivial two-sided perturbation, while matrices with all eigenvalues in `{-1,+1}` are extreme. This step does not restrict the original encoders; it is an exact optimization over their binary decoders. In particular, arbitrary Y components of b remain allowed.

Write `h_i=X_i tensor B_(i,X)+Z_i tensor B_(i,Z)`. Call a site active if both its decoder extremes are traceless.

If a site is not active, one decoder is a scalar sign. The other extreme squares to I, and the anticommutator of X_i and Z_i vanishes. Thus

$$
h_i^2=2I,\qquad \|h_i\|_\infty=\sqrt2.
$$

This includes the case where both decoders are scalar. At an active site, the triangle inequality gives `||h_i||_infinity<=2`.

## 4. At most one active site can provide an advantage

Consider any normalized state of the n reference qubits and the memory qubit, and write `f_i=<h_i>`. For an active site i choose the two reference observables

$$
A_{i,0}=(X_i+Z_i)/\sqrt2,
\qquad A_{i,1}=(X_i-Z_i)/\sqrt2.
$$

Use `B_(i,X), B_(i,Z)` as the memory's CHSH observables. The CHSH operator is exactly `sqrt(2) h_i`. For distinct active sites i,k, reduce to the three qubits `(Q,R_i,R_k)` and apply the prior theorem, with Q the common qubit. Consequently

$$
f_i^2+f_k^2\le4.
$$

No compatibility or simultaneous execution of these tests is assumed. They are expectations on the same mathematical state, using precisely the independently selected observables permitted by the cited theorem.

If there are `r>=2` active sites, summing all pair inequalities gives

$$
(r-1)\sum_{i\text{ active}}f_i^2\le 4\binom r2,
\qquad
\sum_{i\text{ active}}f_i\le
\sqrt{r\sum_{i\text{ active}}f_i^2}\le r\sqrt2.
$$

The second inequality remains valid when some f_i are negative. The inactive sites each contribute at most `sqrt(2)`. Hence the entire expectation is at most `n sqrt(2)` whenever `r>=2`. It is also at most that value when `r=0`. For `r=1`, the triangle bound is

$$
\sum_i f_i\le2+(n-1)\sqrt2.
$$

This bounds every state and every extreme decoder choice. Maximization and the exact seed reduction prove the desired upper bound for **all** admissible protocols.

For achievability, a normalized seed is an identity matrix divided by `sqrt(2)` on one input site, tensored with bisector bras on all other input sites. Its score is `2+(n-1)sqrt(2)`. Its complete Pauli-orbit and query-symmetry instrument is trace preserving and achieves the uniform target, as already proved in `COLLECTIVE_ENCODING_REDUCTION.md`. Equivalently, retain one uniformly selected input qubit and measure all other sites with the classical parent POVM.

## 5. Equality: structure of all maximizing seeds

There is also a useful structural consequence. Up to the choice of retained site, a unitary on the output, and overall phase, every maximizing normalized seed is

$$
L=\frac1{\sqrt2}U
\left(I_i\otimes\bigotimes_{k\ne i}\langle\beta_k|\right),
$$

after reordering tensor factors. Each real state beta_k is the positive eigenstate of `(s_(k,X)X+s_(k,Z)Z)/sqrt(2)` for signs `s_(k,X),s_(k,Z)` in `{-1,+1}`.

To see this, fix a maximizing L and choose extreme dual decoders attaining all its trace norms. Such an extreme choice always exists, including by extending the sign choice at a zero eigenvalue to a sign. The previous proof forces exactly one active site: the other cases fall short by `2-sqrt(2)>0`.

Equality in the sum of bounds forces the active term to have expectation 2. If its Bloch directions are b and c, then

$$
h_i^2=2I+2Y_i\otimes(\mathbf b\times\mathbf c)\cdot\boldsymbol\sigma,
$$

so its norm is 2 only when `b` and `c` are orthogonal. Its top eigenvalue is then simple, with a maximally entangled eigenvector on `(R_i,Q)`; an output unitary reduces it to the familiar top eigenvector of `X tensor X+Z tensor Z`. Therefore the entire pure vectorized seed factors as that Bell pair and a state on the remaining references.

If another site had one scalar and one traceless decoder, the latter expectation would vanish because Q is maximally mixed and independent of the remaining references. That site's contribution would be at most 1, strictly below the required `sqrt(2)`. Thus every other site's two decoders are scalar. Saturating its `sqrt(2)` bound forces its reference qubit into the unique appropriate bisector eigenstate. The remaining reference state therefore factors into those pure states. Vectorizing back gives the claimed L.

For a contrast-optimal instrument, the normalized-Kraus upper bound is an average of quantities each at most Gamma. Equality forces every nonzero refined Kraus seed to be a maximizer. Consequently, its refined branch maps have the form

$$
K_a=c_aU_a\left(I_{i_a}\otimes
\bigotimes_{k\ne i_a}\langle\beta_{a,k}|\right),
$$

with scalar amplitudes c_a subject to instrument completeness. A fine-grained optimal implementation therefore consists branch by branch of retaining one input qubit, applying an output unitary, and projecting the other sites onto product bisectors. This is a statement about refined branch maps, **not** an assertion that the retained site's choice is input independent. Uniform random-subset encoding is one optimal implementation.

## 6. Limits and next question

The central-qubit hypothesis cannot be dropped: two Bell pairs with a four-dimensional memory have `f_1=f_2=2`, so `f_1^2+f_2^2=8`, violating the pair inequality used here. Also, in higher dimension an extreme decoder can have unequal positive and negative eigenspace dimensions; the scalar/traceless qubit classification no longer holds. Artificially assigning each global decoder to one output qubit would restrict the model.

The smallest unresolved nontrivial block is now `n=3,q=2`, asking whether `Gamma(3,4)` can exceed `4+sqrt(2)`. The general finite-block inequality and asymptotic rate remain open. The separate `COMMUTING_SEED_BOUND.md` rules out a broad class of seeds but does not restrict this unrestricted target.

`tools/check_one_qubit_tradeoff.py` checks representative matrix identities, attaining seeds, complex-seed examples, and the higher-dimensional negative control. These checks supplement the proof; they do not establish its generality or publication novelty. This all-n one-qubit result should be presented as a task-specific deduction from established monogamy, pending a separate novelty assessment of any broader publishable contribution.
