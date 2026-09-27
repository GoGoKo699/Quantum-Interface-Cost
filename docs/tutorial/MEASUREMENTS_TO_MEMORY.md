# From compatible measurements to a quantum memory budget

[Learning path](../LEARNING_PATH.md) · [Repository](../../README.md) ·
[Next: the proof bridge](PROOF_BRIDGE.md)

This tutorial starts with a physical question: **what must we keep now if
the measurement question will arrive later?** It develops the operational
meaning of the results before their general encoder proofs.

The single external teaching anchor is Gühne, Haapasalo, Kraft, Pellonpää
and Uola, [*Incompatible measurements in quantum information science*](https://arxiv.org/abs/2112.06784),
Rev. Mod. Phys. **95**, 011003 (2023). Section labels below follow the PDF.
Read its Sections II.A–B and III.A alongside Sections 1–3 here;
Section III.B.2 supplies the incompatibility-weight viewpoint used later.
The explanations and worked examples below are written for this project.

By the end, you should be able to construct the two-input protocol and
explain how unequal local accuracies share one quantum-memory slot.

| Read this part | Question it answers |
|---|---|
| [The task](#1-the-specimen-arrives-before-the-question) and [contrast](#2-contrast-measures-the-accuracy-of-a-binary-answer) | What must the delayed answer reproduce? |
| [Classical memory](#3-what-can-one-qubit-leave-in-purely-classical-memory) and [retaining qubits](#4-keeping-quantum-information-leaves-a-choice-for-later) | How is the two-input protocol built? |
| [Unequal allocation](#5-one-retained-qubit-can-be-allocated-unevenly) and [operational distinctions](#6-keep-the-operational-distinctions-visible) | Which accuracy profiles fit one memory qubit? |

## 1. The specimen arrives before the question

We receive one unknown $n$-qubit state, written $\omega$. It may be mixed,
and its qubits may be entangled with one another. We do not receive a
classical description of $\omega$, and we cannot request another copy.

Before learning the question, we encode this specimen into a memory.
Later, the question specifies one site $i$ and one of its two Pauli
observables, $X_i$ or $Z_i$. We must return one outcome, $+1$ or $-1$.
There is only one question in each use of the protocol.

For either requested observable $U$, the ideal measurement has effects

```math
\begin{aligned}
E^{\mathrm{ideal}}_{\pm|U}&=\frac{I\pm U}{2},\\
p^{\mathrm{ideal}}_\pm&=\frac{1\pm\operatorname{Tr}(\omega U)}{2}.
\end{aligned}
```

We aim to reproduce these **outcome probabilities**. We are not trying
to estimate $\operatorname{Tr}(\omega U)$ numerically from one specimen.
Even a perfect implementation returns a random outcome when the ideal
measurement itself is random.

A POVM describes those probabilities; an instrument additionally
describes the remaining quantum state after each recorded outcome.
That distinction from the anchor's Section II.A matters here: an encoder
may both extract a classical record and leave a quantum system to query.

## 2. Contrast measures the accuracy of a binary answer

The noisy measurement of $U$ with contrast $\eta\in[0,1]$ has effects

```math
E_{\pm|U}=\frac{I\pm\eta U}{2}.
```

At $\eta=1$ it is the desired measurement. At $\eta=0$ it is a fair
coin, independent of the specimen. Intermediate contrast shrinks the
dependence of the answer on the input state.

For two binary distributions, total-variation distance is simply the
absolute difference of their probabilities for the $+1$ outcome. Thus

```math
\operatorname{TV}(p^{\mathrm{ideal}},p)
=\frac{1-\eta}{2}|\operatorname{Tr}(\omega U)|
\le\frac{1-\eta}{2}.
```

An eigenstate of $U$ attains this bound. The uniform error, maximized
over every allowed input, is therefore $\varepsilon=(1-\eta)/2$.
Uniformity includes entangled inputs; there is no preferred input
ensemble over which difficult states can be averaged away.

We allow different contrasts $x_i\in[0,1]$ for $X_i$ and
$z_i\in[0,1]$ for $Z_i$.
The equal-accuracy task is the special case $x_i=z_i=\eta$ for all sites.
The general encoder proofs justify reducing uniform-error guarantees to
these exact noisy observables by symmetry; the [proof bridge](PROOF_BRIDGE.md)
explains that step.

## 3. What can one qubit leave in purely classical memory?

First consider a single input qubit and retain no quantum system.
We must measure it before learning whether the question will be X or Z.
A useful measurement has four outcomes $(s,t)\in\{+1,-1\}^2$:

```math
G_{s,t}=\frac{I+s xX+t zZ}{4}.
```

Store $(s,t)$. If the later question is X, answer $s$; if it is Z,
answer $t$. Summing over the unused coordinate gives

```math
\sum_tG_{s,t}=\frac{I+s xX}{2},\qquad
\sum_sG_{s,t}=\frac{I+t zZ}{2}.
```

These are the required noisy measurements. Because $X$ and $Z$
anticommute, $(s xX+t zZ)^2=(x^2+z^2)I$. Each $G_{s,t}$ consequently
has eigenvalues

```math
\frac{1+\sqrt{x^2+z^2}}4,\qquad
\frac{1-\sqrt{x^2+z^2}}4.
```

The four effects sum to $I$ and are positive precisely when

```math
\boxed{x^2+z^2\le1.}
```

This proves that the quarter disk is **achievable**. Positivity of this
particular construction alone does not prove that every other parent
measurement must obey the same bound.

Any purely classical protocol is an early measurement followed by
classical postprocessing for the chosen question. This is precisely
joint measurability, as defined in the anchor's Section II.B.
Here is a short necessity argument. Any joint implementation of the
two binary POVMs has four positive effects $H_{s,t}$ with the same
marginals. Write their Bloch expansions as

```math
H_{s,t}=\frac{g_{s,t}I+\mathbf v_{s,t}\cdot\boldsymbol\sigma}{2}.
```

Positivity implies $\|\mathbf v_{s,t}\|\le g_{s,t}$; normalization
implies $\sum_{s,t}g_{s,t}=2$ and $\sum_{s,t}\mathbf v_{s,t}=0$.
The two positive-outcome marginals imply

```math
\begin{aligned}
x\mathbf e_X+z\mathbf e_Z&=\mathbf v_{++}-\mathbf v_{--},\\
x\mathbf e_X-z\mathbf e_Z&=\mathbf v_{+-}-\mathbf v_{-+}.
\end{aligned}
```

Applying the triangle inequality to both equations gives
$2\sqrt{x^2+z^2}\le\sum_{s,t}\|\mathbf v_{s,t}\|\le2$.
Thus the disk is necessary too. This is the orthogonal, unbiased case
of the compatibility criterion reviewed in the anchor's Section III.A.

At equal contrast, $x=z=\eta$, the boundary is
$\eta=1/\sqrt2$. A classical record can preserve both *noisy*
measurement statistics to this accuracy. It need not preserve two
sharp outcomes that the unknown qubit possessed beforehand.

## 4. Keeping quantum information leaves a choice for later

Now allow the encoder to retain at most $q$ qubits, together with an
unrestricted finite classical record, where $0\le q\le n$ is an integer.
Operationally, for every recorded
branch $c$, its quantum output has dimension at most $2^q$.

The encoder may act collectively on all input qubits. It need not decide
in advance that particular original qubits will survive. Its later
binary decoder may depend on both the question and the classical record.
Every branch is accepted. There is no source reaccess, free quantum
bypass, or preshared entanglement.

The simplest construction does retain original sites:

1. Choose uniformly a subset of exactly $q$ sites and record that choice.
2. Keep those qubits. Measure each other site with the disk-boundary
   parent POVM from Section 3, using $x=z=1/\sqrt2$.
3. For the delayed question, measure the retained qubit if its site was
   kept; otherwise return the appropriate stored sign.

Each site is retained with probability $q/n$. Its effective contrast is
the mixture of a perfect answer and a compatible classical answer:

```math
\boxed{\eta_{\mathrm{ret}}(n,q)
=\frac qn+\left(1-\frac qn\right)\frac1{\sqrt2}.}
```

The construction works on entangled inputs too. Its effective queried
observable is the stated local Pauli multiplied by the stated contrast,
with identity on all other sites. Averaging over outcomes of measurements
on the other sites preserves the requested marginal distribution.

For two inputs and one retained qubit, keep either site with probability
$1/2$. Every X or Z question then has

```math
\begin{aligned}
\eta_{\mathrm{ret}}(2,1)&=\frac{1+1/\sqrt2}{2}\approx0.8536,\\
\varepsilon&=\frac{1-1/\sqrt2}{4}\approx0.0732.
\end{aligned}
```

<p align="center">
  <img src="../figures/retention_geometry.svg" width="720" alt="A quarter disk shows the classical region. Its equal-contrast boundary point A and perfect-retention point B have midpoint C, the per-site accuracy from retaining either of two sites with equal probability." />
</p>

**Reading the figure.** The line joins two possible treatments of a single
site. Point C averages them with equal weights. Across the two-site protocol, exactly one site
is retained in every branch; each site is retained half the time.

This construction establishes a performance that is possible. Proving
that an arbitrary collective encoder cannot do better is a separate
task. The [core argument](../CORE_ARGUMENT.md) proves optimality at all
integer budgets for $1\le n\le4$, and at $q=1$ for every $n$.
The same common-accuracy assertion for arbitrary $n,q$ remains open.

## 5. One retained qubit can be allocated unevenly

Equal accuracy is only one possible request. For a site with desired
contrasts $(x,z)$, define

```math
w(x,z)=\left[x+z-1-\sqrt{2(1-x)(1-z)}\right]_+.
```

Here $[a]_+=\max\{a,0\}$.

Its geometric meaning is a minimum mixing fraction. Classical storage
provides the disk $\mathcal D=\{(x,z)\ge0:x^2+z^2\le1\}$.
Retaining the qubit provides the square $[0,1]^2$, since either later
measurement can be performed and then independently degraded by output
noise. The smallest $p$ for which

```math
(x,z)\in p[0,1]^2+(1-p)\mathcal D
```

is $w(x,z)$. Inside the disk it is zero. Outside the disk, mix the
perfect point $(1,1)$ with a disk-boundary point. The boundary equation

```math
(x-p)^2+(z-p)^2=(1-p)^2
```

has the displayed expression for $w$ as its smaller root. The
[allocation proof](../ONE_QUBIT_ALLOCATION_REGION.md) also establishes
that allowing a different square point cannot lower this fraction.
The anchor's incompatibility weight supplies the prior resource concept;
the local evaluation and its use as a memory-allocation rule are developed
in the repository, with attribution in the [prior comparison](../CORE_PRIOR_COMPARISON.md).

The exact one-qubit allocation theorem says that a profile
$(x_i,z_i)_{i=1}^n$ is feasible with $q=1$ if and only if

```math
\boxed{\sum_i w(x_i,z_i)\le1.}
```

The sufficiency construction is tangible. Set $p_i=w(x_i,z_i)$ and
retain site $i$ with probability $p_i$. The remaining probability is an
all-classical branch. Whenever site $i$ is discarded and $p_i<1$, use
the disk point $((x_i-p_i)/(1-p_i),(z_i-p_i)/(1-p_i))$ there.
If $p_i=1$, that site is always retained and needs no discarded rule.

For example, take three sites and request

```math
\begin{aligned}
(x_1,z_1)&=(1,1/2),\\
(x_2,z_2)&=(1,1/2),\\
(x_3,z_3)&=(1/\sqrt2,1/\sqrt2).
\end{aligned}
```

Their weights are $1/2,1/2,0$. Keep site 1 or site 2 with equal
probability. Measure X on whichever of those two is discarded: it
provides contrasts $(1,0)$, with a fair coin used for a later Z query.
Always use the compatible parent measurement on site 3. The resulting
contrasts are exactly those requested, using one retained qubit in every
branch.

Necessity is the deeper statement: even a collective encoder must obey
the same sum rule. Its proof uses a virtual reference state and the
established Cheng–Hall CHSH monogamy theorem. The construction above
does not prove that bound, nor does the theorem require every optimal
encoder physically to retain an original site. It guarantees that a
retention implementation exists for every feasible profile.

## 6. Keep the operational distinctions visible

| Distinction | Meaning in this project |
|---|---|
| Unknown specimen versus a known-string QRAC | The encoder receives $\omega$, not a classical string it can freely encode or copy; our guarantee is uniform over states, rather than an average guessing score. |
| One delayed query versus a joint readout | Only one requested outcome is returned; the alternative query labels specify what the same encoder must support. |
| Classical branch versus fixed probability | A physical branch can have input-dependent probability; only the construction's initial random subset is chosen independently of the input. |
| Branch cap versus average cost | Every output branch has quantum dimension at most $2^q$; rare larger memories are forbidden. |
| Outcome sampling versus estimation | Success concerns the distribution of one answer, not learning a probability from repeated copies. |

Continue to the [proof bridge](PROOF_BRIDGE.md) for the route from a
general instrument to one rank-constrained matrix, and from that matrix
to the finite-block converses and the collective separation.
