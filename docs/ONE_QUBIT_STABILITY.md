# Quantitative stability of the one-qubit optimum

Date: 22 September 2026. Research base:
`f761bbca3ba3c1b263a1914175e3bdab94be70a7`.

**Status:** supplied analytical deduction, independently reconstructed within
this workspace. The argument uses the established Cheng–Hall monogamy
inequality and an elementary spectral-gap estimate. It is not external peer
review, a new self-testing method, or a certification of publication novelty.

## 1. Statement and conventions

Let `n>=1`, and let `L:C^(2^n)->C^2` be any complex matrix with
`||L||_F=1`. Outputs of dimension one may be embedded in dimension two.
For the same local queries as in the operational model, put

$$
g(L)=\sum_{i=1}^n\bigl(\|LX_iL^\dagger\|_1+
                         \|LZ_iL^\dagger\|_1\bigr),
\qquad G_n=2+(n-1)\sqrt2,
\qquad \delta=G_n-g(L).
\tag{1}
$$

The [one-qubit theorem](ONE_QUBIT_OPTIMALITY.md) gives `delta>=0`.
Let `S_n` be the set of exact maximizing normalized seeds

$$
M=\frac1{\sqrt2}U\left(I_k\otimes
                 \bigotimes_{j\ne k}\langle\beta_j|\right),
\tag{2}
$$

after reordering tensor factors. Here U is any two-dimensional output
unitary, and each beta_j is the positive eigenstate of
`(s_(j,X)X+s_(j,Z)Z)/sqrt(2)`, for signs in `{-1,+1}`.
An overall phase is included in U. These are real input bisectors, but L
and U need not be real.

**Theorem.** If `0<=delta<=1/48`, some `M in S_n` satisfies

$$
\boxed{\left|\operatorname{Tr}(M^\dagger L)\right|^2
             \ge1-\frac{2\delta}{3}.}
\tag{3}
$$

After choosing its phase, the same M satisfies

$$
\boxed{\|L-M\|_F^2\le\frac{4\delta}{3}.}
\tag{4}
$$

For every normalized L, without the small-deficit condition,

$$
\boxed{\inf_{M\in\mathcal S_n}\|L-M\|_F^2
                  \le\min\{2,96\delta\}.}
\tag{5}
$$

The constants in (3)–(4) do not depend on n. This is stability of
normalized branch matrices, with a consequence for their natural weights
in Section 5. It does not by itself approximate an entire physical
instrument in an operational channel norm.

## 2. The deficit forces exactly one active site

Vectorize L as

$$
|\psi\rangle=\sum_x|x\rangle_R\otimes L|x\rangle_Q.
$$

It is a normalized pure state on n reference qubits and one memory qubit.
Since the reference X/Z matrices are real, for each query P choose an
extreme Hermitian contraction B attaining

$$
\|LPL^\dagger\|_1
 =\operatorname{Tr}(B LPL^\dagger)
 =\langle\psi|P\otimes B|\psi\rangle.
$$

Such a choice exists even if `LPL^dagger` has a zero eigenvalue: extend
its sign to a sign on the kernel. The extreme qubit contractions are
`+I`, `-I`, and traceless Pauli observables `b dot sigma`, with `|b|=1`.
Define

$$
h_i=X_i\otimes B_{i,X}+Z_i\otimes B_{i,Z},
\qquad f_i=\langle\psi|h_i|\psi\rangle,
\qquad g(L)=\sum_i f_i.
\tag{6}
$$

A site is active when both its decoder extremes are traceless. At any
inactive site `h_i^2=2I`, hence `f_i<=sqrt(2)`. An active site has
`f_i<=2`.

For distinct active sites i and j, Cheng–Hall's three-qubit inequality,
with independently optimized observables on the common memory qubit,
gives `f_i^2+f_j^2<=4`. Its precise prior-source statement and reduction
are in [ONE_QUBIT_OPTIMALITY.md](ONE_QUBIT_OPTIMALITY.md), Sections 2–4.
Summing the pair bounds shows that two or more active sites have total
contribution at most their number times `sqrt(2)`. Thus either zero or
at least two active sites would imply

$$
g(L)\le n\sqrt2,
\qquad \delta\ge2-\sqrt2>\frac1{48}.
$$

Under the hypothesis of (3), there is therefore exactly one active site
k. Every individual upper-bound deficit is nonnegative, so

$$
f_k\ge2-\delta,
\qquad f_j\ge\sqrt2-\delta\quad(j\ne k).
\tag{7}
$$

## 3. A Bell factor and exclusion of mixed decoder types

Write `B_(k,X)=b dot sigma`, `B_(k,Z)=c dot sigma`, and `t=b dot c`.
The case `|t|=1` has `||h_k||=sqrt(2)`, contradicting (7), so `|t|<1`.
Set

$$
A_\pm=\frac{X_k\pm Z_k}{\sqrt2},\qquad
D_+=\frac{B_{k,X}+B_{k,Z}}{\sqrt{2+2t}},\qquad
D_-=\frac{B_{k,X}-B_{k,Z}}{\sqrt{2-2t}}.
$$

Each pair consists of anticommuting qubit Pauli observables. Consequently

$$
h_k=\sqrt{1+t}\,A_+\otimes D_+
      +\sqrt{1-t}\,A_-\otimes D_-.
\tag{8}
$$

The two tensor-product reflections commute. Their four joint eigenspaces
are one-dimensional: each joint spectral projector has trace one, as
both generators and their product are traceless. Their common positive
eigenvector `|Phi>` is maximally entangled. For example, its projector is
`(I+A_+ tensor D_+)(I+A_- tensor D_-)/4`; either partial trace is `I/2`.

Put

$$
u=\sqrt{1+t}+\sqrt{1-t},\qquad
v=\left|\sqrt{1+t}-\sqrt{1-t}\right|.
$$

The spectrum of `h_k` is `u,v,-v,-u`, with unique top eigenvector Phi,
and `u^2+v^2=4`. By (7), `u>=2-delta`, and therefore

$$
v\le2\sqrt\delta,\qquad
u-v\ge2-\delta-2\sqrt\delta>\frac32
\quad\left(0\le\delta\le\frac1{48}\right).
\tag{9}
$$

The strict inequality follows already from
`2-1/48-2/sqrt(48)>3/2`.
Let `p=<psi|(|Phi><Phi| tensor I)|psi>` be the weight in its top
eigenspace, including the other reference qubits. The gap and (7) give

$$
1-p\le\frac{u-f_k}{u-v}\le\frac{2\delta}{3}.
\tag{10}
$$

Projecting and normalizing produces a pure state
`|Phi> tensor |chi>` whose squared overlap with psi is p. The trace-norm
distance of the corresponding density matrices is `2 sqrt(1-p)`.

Suppose an inactive site j had one scalar decoder and one traceless
decoder. In the projected state the memory qubit is maximally mixed and
independent of all other reference qubits. The term involving its
traceless decoder has zero expectation; the term involving the scalar
decoder has expectation at most one. Since `||h_j||=sqrt(2)`, (10)
would imply

$$
f_j\le1+2\sqrt2\sqrt{1-p}
     \le1+4\sqrt{\delta/3}
     \le\frac43
     <\sqrt2-\delta.
\tag{11}
$$

This contradicts (7). Hence **both decoders at every inactive site are
scalar**. No claim that an arbitrary near-optimal physical decoder has
exactly this form is needed: these are extreme dual decoders chosen to
attain the seed's trace norms.

## 4. One global spectral gap proves the theorem

With the preceding decoder choices, the full operator `H=sum_i h_i`
is a sum on disjoint tensor factors: the active two-qubit block on
`(R_k,Q)`, and one reference-qubit operator
`s_(j,X)X_j+s_(j,Z)Z_j` at each other site. Its unique top eigenvector is

$$
|\Omega\rangle=|\Phi\rangle_{R_kQ}
                    \otimes\bigotimes_{j\ne k}|\beta_j\rangle,
$$

and its top eigenvalue is `lambda_0=u+(n-1)sqrt(2)<=G_n`. Its spectral
gap is `u-v>3/2` for n=1, and
`min{u-v,2sqrt(2)}>3/2` for n>1. Thus

$$
1-|\langle\Omega|\psi\rangle|^2
 \le\frac{\lambda_0-\langle\psi|H|\psi\rangle}{3/2}
 \le\frac{2\delta}{3}.
\tag{12}
$$

There is no accumulation of a separate error for each discarded site.
Every maximally entangled state on `(R_k,Q)` is the vectorization of
`U/sqrt(2)` for an output unitary U; the real beta states become the
bras in (2). Therefore Omega vectorizes a seed M in `S_n`, proving (3).
After phase alignment, writing `a=|<Omega|psi>|` gives

$$
\|L-M\|_F^2=2(1-a)\le2(1-a^2)\le\frac{4\delta}{3},
$$

which proves (4). For arbitrary delta, the distance after phase
alignment to any fixed normalized seed is at most two. If
`delta>1/48`, then `96delta>2`; combining this with (4) proves (5).

## 5. Weighted consequence for an actual instrument

Consider any admissible dimension-two instrument achieving common
contrast eta, and refine its branches into nonzero Kraus maps K_a. Put

$$
p_a=\frac{\|K_a\|_F^2}{2^n},\quad
L_a=\frac{K_a}{\|K_a\|_F},\quad
\delta_a=G_n-g(L_a),\quad
\Delta=G_n-2n\eta.
\tag{13}
$$

Completeness gives `sum_a p_a=1`. The uniform operator identities
`sum_a K_a^dagger B_(a,i,b) K_a=eta P_(i,b)`, followed by the
trace-norm dual bound, give

$$
2n\eta\le\sum_a p_a g(L_a),\qquad
0\le\sum_a p_a\delta_a\le\Delta.
\tag{14}
$$

Indeed multiply each operator identity by its P, take the trace, sum
over queries, and divide by `2^n`. This uses all branches and no
postselection.
Writing `d_a^2=inf_(M in S_n)||L_a-M||_F^2`, for every `0<t<=1/48`
equation (4) and Markov's inequality imply

$$
\sum_{a:d_a^2>4t/3}p_a
 \le\sum_{a:\delta_a>t}p_a
 \le\min\{1,\Delta/t\}.
\tag{15}
$$

Equation (5) also gives

$$
\sum_a p_a d_a^2\le\min\{2,96\Delta\}
 =\min\{2,192n(\eta_{\rm opt}-\eta)\},
\qquad \eta_{\rm opt}=\frac{G_n}{2n}.
\tag{16}
$$

These p_a equal the branch probabilities on the maximally mixed input.
They are not asserted to be the branch probabilities for every input,
and the retained site can vary with a. Replacing each L_a separately by
a nearby M_a need not preserve completeness. Consequently (15)–(16)
do not establish diamond-norm proximity to a valid subset instrument,
nor an input-uniform statement about the weight of exceptional branches.
The operational model remains one arbitrary unknown specimen, one
delayed query, unrestricted collective encoding, unlimited finite
classical information, worst-case output dimension two, and uniform
query accuracy.

## 6. Prior theorem and novelty boundary

Kaniewski, *Analytic and nearly optimal self-testing bounds for the
Clauser–Horne–Shimony–Holt and Mermin inequalities*,
[arXiv:1604.08176v3](https://arxiv.org/pdf/1604.08176v3), version stamp
11 August 2016 (printed header: 12 August), defines extractability on
PDF p. 2 by optimization over local quantum channels. Proposition 1
and Eq. (10), PDF p. 3, give an explicit linear lower bound on singlet
extractability from a CHSH value, for arbitrary local dimensions and
untrusted measurements.

That established theorem already supplies robust certification of an
entangled pair. Here the reference Pauli operators and the two-dimensional
memory are fixed. The extra deduction is a bound for the entire normalized
seed: exactly one active dual site, a Bell factor there, product bisectors
on every other reference, and the weighted branch consequences above.
The direct spectral proof uses this narrower geometry. It does not
establish a new robust self-testing technique, and no priority claim for
the stability statement follows from this scoped comparison. Possible
subsumption by broader rigidity results remains a novelty question.
