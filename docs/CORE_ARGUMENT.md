# Exact allocation of one qubit and a finite collective advantage

**Core argument, 24 September 2026.** Synthesis of results on main at
`e197699d87171635028d1639e025c8e5759e5c68`; no new optimality or originality
claim. The proofs below were independently reconstructed within this
workspace, not externally peer reviewed.

**One qubit of memory can be allocated exactly:** every achievable local
X/Z accuracy profile has an implementation that randomly retains at most
one original qubit. **Larger memories can benefit from collective encoding:**
an explicit five-qubit memory beats the entire original-site-retention
class for an unequal-accuracy task. These statements concern one unknown
specimen and one query chosen after encoding.

## 1. The task

An encoder receives an arbitrary unknown state of n qubits, possibly
entangled internally. It produces a quantum register Q and an unlimited
finite classical record. Only then is one query `(i, X)` or `(i, Z)` revealed;
the decoder returns one binary outcome. Every branch obeys `dim Q <= 2^q`.
The encoder may act collectively on all n inputs. There are no additional
copies, source reaccess, free quantum bypass, preshared entanglement, or
postselected success.

Write the requested effective observables as

\[
x_iX_i,\qquad z_iZ_i,\qquad 0\le x_i,z_i\le1.
\]

Their binary effects are `(I ± x_i X_i)/2` and `(I ± z_i Z_i)/2`.
They approximate ideal readout uniformly over all input states with total
variation errors `(1-x_i)/2` and `(1-z_i)/2`.
Conversely, any protocol meeting these error tolerances can be converted
to these exact observables without increasing memory: finite Pauli
twirling removes unwanted coefficients, and classical output noise
attenuates any excess contrast. Thus the exact-contrast formulation retains
the original uniform-error quantifiers. It is an outcome-sampling task.

## 2. The exact one-qubit theorem

Define the local weight

\[
w(x,z)=\left[x+z-1-\sqrt{2(1-x)(1-z)}\right]_+,
\qquad [t]_+=\max\{t,0\}.
\]

**Theorem.** An unrestricted encoder with `dim Q <= 2` on every branch
realizes the requested profile if and only if

\[
\boxed{\displaystyle\sum_{i=1}^{n}w(x_i,z_i)\le1.}
\]

For equal contrasts this gives, for every n,

\[
\eta_{\max}(n,1)=\frac1{\sqrt2}
 +\frac{1-1/\sqrt2}{n}.
\]

### Why every collective encoder obeys the bound

Fix nonnegative weights `a_i,b_i`, and put

\[
r_i=\sqrt{a_i^2+b_i^2},\qquad
\delta_i=a_i+b_i-r_i.
\]

The key is the sharp weighted inequality

\[
\sum_i(a_ix_i+b_iz_i)\le\sum_i r_i+\max_i\delta_i. \tag{1}
\]

Refine an instrument into Kraus operators `K_c` with output dimension at
most two. For each nonzero operator set

\[
L_c=K_c/\|K_c\|_F,\qquad p_c=\|K_c\|_F^2/2^n.
\]

Completeness gives `sum_c p_c=1`. These are proof weights; physical branch
probabilities can depend on the input state. Trace-norm duality bounds the
left side of (1) by the p-weighted average of the normalized-seed scores

\[
\sum_i f_i,\qquad
f_i=a_i\|LX_iL^\dagger\|_1+b_i\|LZ_iL^\dagger\|_1.
\]

Choose extreme Hermitian contractions attaining the two trace norms.
On a qubit each such decoder is a scalar sign or a traceless Pauli
observable. Vectorizing L gives a normalized *virtual* state of n reference
qubits and the memory qubit, on which

\[
f_i=\langle h_i\rangle,\qquad
h_i=a_iX_i\otimes B_{i,X}+b_iZ_i\otimes B_{i,Z}.
\]

If either decoder is scalar, anticommutation gives `h_i^2=r_i^2 I`, hence
`f_i <= r_i`. If both are traceless, the reference directions
`(a_i X_i ± b_i Z_i)/r_i` make `2h_i/r_i` a CHSH operator.
Cheng–Hall's established monogamy theorem, allowing independently chosen
memory directions and mixed three-qubit marginals, then implies for any
two such sites

\[
(f_i/r_i)^2+(f_k/r_k)^2\le2.
\]

Zero-weight sites can be omitted. At most one site exceeds its r-value;
always `f_i <= a_i+b_i`. Summing proves (1) for each seed, then for the
physical instrument. The reference is only a proof device, and no two
delayed decoders are executed together.

### Why random retention attains the whole region

The compatible disk

\[
D=\{(x,z)\ge0:x^2+z^2\le1\}
\]

is achievable using only classical memory: measure the four-outcome POVM
`G_{s,t}=(I+s x X+t z Z)/4`, store `(s,t)`, and answer the later query.
Retaining one site realizes any point of `[0,1]^2` there; every other site
can independently realize a disk point. These product instruments are
valid on entangled inputs as well.

Their convex hull has support function exactly the right side of (1):
retain a site maximizing `delta_i`. This hull is compact and downward
closed, so nonnegative support directions suffice. Thus (1) proves that
this hull is the entire unrestricted feasible region.

The least retained fraction needed for one pair is w. Outside the disk,
solve

\[
(x-p)^2+(z-p)^2=(1-p)^2
\]

for its smaller root; it is w and lies between zero and `min(x,z)`.
Any decomposition `(x,z)=p s+(1-p)d`, with `s` in the square and `d` in D,
necessarily satisfies

\[
\|((x,z)-p(1,1))_+\|_2\le1-p.
\]

For `p<w`, both coordinates are nonnegative and this quadratic inequality
fails. Thus w is the minimum p in `p[0,1]^2+(1-p)D`.
Consequently every retention mixture satisfies `sum_i w <= 1`.
Conversely, choose site i with probability `p_i=w(x_i,z_i)`, retain it
perfectly, and whenever it is discarded use the disk point

\[
\frac{(x_i,z_i)-p_i(1,1)}{1-p_i}.
\]

Use an all-classical branch with the remaining probability. If `p_i=1`,
that site is always retained and its discarded formula is unnecessary.
This proves sufficiency explicitly. It characterizes the achievable
queried effects, not every encoder realizing them.

## 3. A collective advantage with five memory qubits

Take `n=31`. Label the X-basis vectors by bit strings. Let
`S={0,e_1,...,e_n}`, and use 32 orthogonal output states labelled by S.
Set

\[
p_0=\tfrac12,\quad p_{e_i}=\tfrac1{2n},\qquad
L=\sum_{u\in S}\sqrt{p_u}\,|u\rangle_Q\langle u|_X.
\]

The **complete** instrument is

\[
K_s=LZ^s,\qquad s\in\{0,1\}^n,
\]

with s stored classically. No extra normalization factor is needed:
translations of the diagonal seed give `sum_s K_s^dagger K_s=I`, since
`sum_u p_u=1`. All outcomes are accepted; every branch uses dimension 32.

For X, decode with the diagonal signs `(-1)^(u_i+s_i)`. For Z, decode with
`|0><e_i|+|e_i><0|`, a Hermitian contraction that is zero on the other
output states. Zero means a fair binary output, not a discarded event.
Direct summation gives the effective observables

\[
\sum_sK_s^\dagger B_{s,i,X}K_s=X_i,\qquad
\sum_sK_s^\dagger B_{s,i,Z}K_s
=2\sqrt{p_0p_{e_i}}\,Z_i=\frac{Z_i}{\sqrt{31}}.
\]

These operator identities establish uniform performance without a
31-qubit numerical simulation.

For comparison, define **original-site retention** precisely: every refined
Kraus branch factors as `K_c=M_c ⊗ <v_c|` across original sites
`T_c` and their complement, with `|T_c| <= q`. The retained-site operation,
the selected sites, and the discarded-site vector may depend on c; the
discarded sites may be measured jointly. This is a substantial comparison
class, although it does not include every collective encoder.

Its normalized Gram matrices factor across that split. Retained-site
scores are at most `a+b`; discarded-site scores are at most
`sqrt(a^2+b^2)` by the Bloch disk. For `a,b >= 0`, the same Kraus averaging gives

\[
\sum_i(a x_i+b z_i)
\le q(a+b)+(n-q)\sqrt{a^2+b^2}.
\]

With every `x_i=1`, set `b=1` and let a tend to infinity to obtain
`sum_i z_i <= q`. The collective construction instead gives

\[
\sum_i z_i=\sqrt{31}>5=q.
\]

Thus it strictly exceeds that entire retention class at the same
worst-case memory cap. No claim is made that this collective construction
is optimal among unrestricted encoders.

## 4. What is prior, and what is being claimed

| Established ingredient | Primary source and precise locator |
|---|---|
| Dimension-constrained measurement simulation with classical records | [Ioannou et al., arXiv:2202.12980v1](https://arxiv.org/pdf/2202.12980v1), Eq. (1), p. 2. |
| Independently optimized CHSH monogamy, including mixed states | [Cheng–Hall, arXiv:1610.09302v3](https://arxiv.org/pdf/1610.09302v3), Eq. (1), p. 1; Eqs. (13)–(14) and following paragraph, p. 3. |
| Orthogonal-qubit compatibility disk; incompatibility weight | [Yu–Liu–Li–Oh, arXiv:0805.1538v2](https://arxiv.org/pdf/0805.1538v2), Theorem 1/Eq. (5), pp. 1–2; [Pusey, arXiv:1502.03010v2](https://arxiv.org/pdf/1502.03010v2), Section III/Eq. (15), p. 4. The displayed w is an elementary evaluation of this prior resource. |
| Related average compression cost | [Cope–Uola, arXiv:2207.05722v4](https://arxiv.org/pdf/2207.05722v4), Section IV.C/Eqs. (13)–(14), pp. 7–8. An average branch cost does not itself give a dimension-two cap on every branch. |
| The cube-star spectrum underlying the finite construction | [Avni–Samorodnitsky, arXiv:2411.14597v1](https://arxiv.org/pdf/2411.14597v1), Example 1.12, p. 8. The star eigenvector and eigenvalue are prior mathematics. |

The supplied deductions are the exact all-n allocation theorem and the
complete finite collective protocol with its retention-class separation.
They are a focused candidate for theorem-level priority comparison;
publication originality is not established by these proofs or by the
sources inspected so far. The broader two-parameter entanglement profile
has substantial prior subsumption, detailed in the
[nonlinear-source audit](audits/NONLINEAR_CHSH_SUBSUMPTION.md), and is not
needed for this core argument.

Unrestricted **equal-accuracy** optimality for larger memories remains
open. The unequal-accuracy separation does not decide it. Full supporting
proofs are in the [allocation note](ONE_QUBIT_ALLOCATION_REGION.md),
[exact-axis note](EXACT_AXIS_SPECTRAL_REDUCTION.md), and
[seed reduction](COLLECTIVE_ENCODING_REDUCTION.md).
