# A normalized-seed formulation of the unrestricted interface

Date: 2026-09-22. Status: derivation independently checked in the
[commit-pinned audit](audits/PROOF_AND_NOVELTY_AUDIT.md), Section 5.
This is an optimization reduction, not a solution of the optimization, and
not asserted to be a novel theorem. Compare the established measurement
simulability/steering framework in note references [1–2].

## 1. Statement

Keep exactly the operational model in RESEARCH_NOTE.md Section 2. Put
$d=2^n$, $D=2^q$, and let $P_j$ range over the $2n$ local X/Z observables.
For a complex $D$-by-$d$ matrix $L$ with Frobenius norm one, set

$$
g(L)=\sum_{j=1}^{2n}\|L P_j L^\dagger\|_1,
\qquad \Gamma(n,D)=\max_{\operatorname{Tr}(L^\dagger L)=1}g(L).
$$

Here the norm is the trace norm. All matrices L are allowed, not merely
isometries, product encodings, real matrices, or flat-singular-value matrices.
The claimed exact reduction is

$$
\eta_{\max}(n,q)=\frac{\Gamma(n,2^q)}{2n}.
$$

The maximum exists by compactness and continuity. Lower contrasts can be
obtained by random output flips. No restriction on the free classical record
is introduced by the reduction.

## 2. Upper bound for every admissible encoder

Resolve each instrument map into Kraus matrices K_a. The branch label may
be refined to include the Kraus index because classical storage is free.
For a lower-bound argument, it is also enough to keep the old decoder for
all refinements. Completeness gives

$$
\sum_a K_a^\dagger K_a=I_d,\qquad
\sum_a\|K_a\|_F^2=d.
$$

Let B_{a,j} be the Hermitian decoder contraction. Uniform contrast implies
$\sum_a K_a^\dagger B_{a,j}K_a=\eta P_j$. Take its Hilbert–Schmidt inner
product with P_j, divide by d, and sum over j:

$$
2n\eta=\frac1d\sum_{a,j}
\operatorname{Tr}(B_{a,j}K_aP_jK_a^\dagger).
$$

For nonzero K_a define $L_a=K_a/\|K_a\|_F$. Trace-norm duality gives

$$
2n\eta\le\sum_a\frac{\|K_a\|_F^2}{d}\,g(L_a)
\le\Gamma(n,D).
$$

Zero Kraus matrices contribute nothing. This bound allows arbitrary global
instruments and branch-dependent decoders; it does not assume a kept subset.

## 3. Constructing a deterministic interface from any seed

For each j choose the Hermitian contraction
$B_j=\operatorname{sign}(LP_jL^\dagger)$, with sign(0)=0. Then
$v_j=\operatorname{Tr}(B_jLP_jL^\dagger)=\|LP_jL^\dagger\|_1$.
Let U run over the n-qubit Pauli representatives, a set of size m=4^n,
and define

$$
K_U=\sqrt{d/m}\,L U.
$$

Pauli averaging shows $\sum_U K_U^\dagger K_U=I_d$. These are all the
branches of one valid instrument; no favorable branch is selected or
postselected. The branch U is stored in C and the quantum output has dimension D.

If $UP_jU^\dagger=s_{U,j}P_j$, use decoder $s_{U,j}B_j$. Pauli-character
orthogonality gives

$$
\sum_U K_U^\dagger(s_{U,j}B_j)K_U
= v_jP_j.
$$

For completeness, the character projection used here is

$$
\frac1m\sum_U s_{U,j}U^\dagger A U
=\frac{\operatorname{Tr}(P_jA)}d P_j.
$$

Thus this interface has possibly unequal local contrasts v_j. Randomize the
input by all site permutations and independent local Hadamards; store the
seed classically and relabel the downstream query accordingly. This family
acts transitively on the 2n queries and makes the common contrast equal to
$\sum_jv_j/(2n)=g(L)/(2n)$. The quantum dimension never exceeds D.
This proves achievability of the claimed variational value.

The Pauli index is a physical instrument outcome, while the final
permutation/Hadamard choice can be independent classical randomness. Treating
the normalized seed alone as a trace-preserving channel would be an error.
The orbit construction, not postselection, fixes that issue.

## 4. Analytic target and checks

The random-subset baseline has a seed consisting of q maximally entangled
factors (equivalently identity matrix factors in L) and n-q pure bisector
factors. It gives

$$
g(L)=2q+\sqrt2(n-q).
$$

The key candidate inequality is therefore

$$
\Gamma(n,2^q)\stackrel{?}{\le}2q+\sqrt2(n-q).
$$

It remains unresolved for general `2<=q<n`. Proving it for all n,q would establish the subset
strategy's finite-size optimality. Finding a seed that violates it would
construct a genuine collective advantage after the orbit completion above.
The [one-qubit theorem](ONE_QUBIT_OPTIMALITY.md) now proves it for every n
when q=1 and classifies all maximizing seeds. The
[product-diagonal bound](COMMUTING_SEED_BOUND.md) proves it whenever
`L^dagger L` is diagonal in a fixed local product basis, for arbitrary q.
Neither statement restricts the encoders in the unresolved general problem.
The smallest remaining block is n=3,q=2, with threshold $g(L)=4+\sqrt2$.

The same problem admits the spectral expression

$$
\Gamma(n,D)=\max_{-I\le B_j\le I}
\lambda_{\max}\left(\sum_j P_j^T\otimes B_j\right).
$$

To see this, vectorize L in input-then-output order and use trace-norm
duality; the P_j are real in this workload. This is generally a nonconvex
optimization over all B_j. A seesaw or a restricted ansatz supplies candidate
seeds, not certified global upper bounds.

`tools/check_seed_twirl.py` checks the complete channel and uniform effect
identities for five subset seeds and five seeded dense complex seeds with
n<=2. Recorded output is `results/seed_twirl.json`. These checks do not
prove the upper-bound reduction or the candidate inequality and do not
establish novelty. The derivation above is the material to audit.
