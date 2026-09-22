# An obstruction to sharp local entanglement calibration

Research base: `358d887058eb9fa2fe8bb899d0261ec811d42fa6` (22 September 2026).

**Status:** supplied analytical obstruction to a proposed proof route,
independently reconstructed within this workspace.
The unrestricted seed entropy conjecture and existing quadratic converse
are not refuted.

## 1. The proposed local step

For a state sigma on a reference qubit A and a quantum system Q, define
its fixed-X/Z steering score

$$
f(\sigma)=\|\operatorname{Tr}_A[(X_A\otimes I)\sigma]\|_1
 +\|\operatorname{Tr}_A[(Z_A\otimes I)\sigma]\|_1,
\qquad c=2-\sqrt2.
$$

Trace-norm duality optimizes the decoder contractions separately. Consider the local claim

$$
E_{\rm sq}(A:Q)_\sigma\stackrel{?}{\ge}
\frac{f(\sigma)-\sqrt2}{c},
\tag{1}
$$

followed by monogamy on a pure normalized seed. Although the Bell state
saturates (1), it is false already when Q is a qubit.

## 2. An exact two-qubit counterexample

Let `|Phi+>=(|00>+|11>)/sqrt(2)` and put

$$
\sigma_\epsilon=(1-4\epsilon)|\Phi^+\rangle\langle\Phi^+|
 +\epsilon I_4,\qquad 0<\epsilon<\frac14.
\tag{2}
$$

Its Bell-basis spectrum is `(1-3epsilon,epsilon,epsilon,epsilon)`;
both marginals are `I/2`. Partial trace gives the conditional operators
`(1-4epsilon)X/2` and `(1-4epsilon)Z/2`, so

$$
f(\sigma_\epsilon)=2-8\epsilon.
\tag{3}
$$

Christandl--Winter's definition is
`E_sq(A:Q)=inf_E I(A:Q|E)/2`. Taking a one-dimensional extension yields

$$
E_{\rm sq}(\sigma_\epsilon)
\le\tfrac12 I(A:Q)_{\sigma_\epsilon}
=1-\tfrac12H(1-3\epsilon,\epsilon,\epsilon,\epsilon).
\tag{4}
$$

See Christandl--Winter, [quant-ph/0308088v3](https://arxiv.org/pdf/quant-ph/0308088v3),
Definition 1, printed p. 1; also [S6] in the
[commit-pinned audit](audits/PROOF_AND_NOVELTY_AUDIT.md). No infimum evaluation is needed.

Choose `epsilon=1/1024`. The three small eigenvalues alone give
`H>=3epsilon log_2(1/epsilon)=30epsilon`. Therefore

$$
E_{\rm sq}(\sigma_\epsilon)
\le1-15\epsilon
<1-(8+4\sqrt2)\epsilon
=\frac{f(\sigma_\epsilon)-\sqrt2}{2-\sqrt2}.
\tag{5}
$$

Since `15>8+4sqrt(2)`, this refutes (1), including its positive-part variant.
Allowing arbitrary Q cannot repair a claim already false for a qubit Q.

## 3. Every calibration bounded by half the mutual information has the same issue

More generally, suppose a bipartite quantity E satisfies
`E(sigma)<=I(A:Q)_sigma/2`, and a universal scalar calibration obeys

$$
E(\sigma)\ge\phi(f(\sigma)),\qquad \phi(2)=1.
$$

Set `delta=2-f(sigma_epsilon)=8epsilon` in (4). Necessarily,

$$
\begin{aligned}
\phi(2-\delta)
&\le1-\tfrac12H(1-3\delta/8,\delta/8,\delta/8,\delta/8),\\
1-\phi(2-\delta)
&\ge\frac{3\delta}{16}\log_2\frac8\delta.
\end{aligned}
\tag{6}
$$

The discarded entropy contribution is nonnegative. In particular,

$$
\liminf_{\delta\downarrow0}
\frac{1-\phi(2-\delta)}\delta=+\infty.
\tag{7}
$$

A calibration sharp at the Bell endpoint cannot have a finite endpoint
slope under these hypotheses. The affine charge in (1) is therefore
incompatible with this entire class of quantities, including squashed
entanglement.

## 4. What remains open

This local obstruction does not refute the global seed inequality: other
reference sites can contribute compensating deficits. The established weak
squashed-entanglement bound uses a different calibration and remains valid.
A sharp global proof needs information beyond (1). This is an elementary
deduction from standard entropy identities; publication novelty is not
asserted. All physical quantifiers of the original single-specimen,
single-delayed-query problem remain unchanged.
