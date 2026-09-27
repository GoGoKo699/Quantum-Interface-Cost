# From measurement incompatibility to the memory proofs

[Learning path](../LEARNING_PATH.md) · [Previous: measurements to memory](MEASUREMENTS_TO_MEMORY.md) · [Core argument](../CORE_ARGUMENT.md)

The starting point is [Gühne et al., *Colloquium: Incompatible
measurements in quantum information science*](https://arxiv.org/abs/2112.06784v3).
Sections II.A–B introduce measurements, instruments, and joint
measurability; Section III.A treats qubit compatibility. This language
explains why an early
classical record cannot reproduce every later sharp measurement. This
bridge asks the next question: what changes when a small quantum register
also survives until the query arrives? Read
[Measurements to memory](MEASUREMENTS_TO_MEMORY.md) first if effects,
instruments, or joint measurements are unfamiliar.

The review supplies the teaching vocabulary. The reductions and finite
memory results below are those in the repository's
[reviewed core argument](../CORE_ARGUMENT.md), with their own credited
ingredients. They are not theorems attributed to the review article.

By the end, you should be able to follow the reduction from a physical
encoder to a bounded-rank seed, and locate the converse for each result.

| Read this part | Role in the argument |
|---|---|
| [Input and seed](#1-separate-the-unknown-input-from-the-optimization-variable), [decoder](#2-why-a-decoder-disappears-into-a-trace-norm) and [completion](#3-why-a-seed-really-gives-a-complete-protocol) | Turn the operational task into an exact matrix optimization |
| [Retention](#4-calculate-what-retaining-a-site-means-in-seed-notation) and [one-qubit monogamy](#5-why-one-memory-qubit-brings-in-chsh) | Construct the benchmark and prove the allocation rule |
| [Rank constraint](#6-fidelity-affinity-and-the-constraint-that-cannot-be-dropped) and [finite budgets](#7-locate-every-finite-budget-and-the-exact-certificate) | Locate the sharp finite converses and their certificate |
| [Collective example](#8-a-small-support-explains-the-31-input-collective-example) and [boundary](#9-continue-with-the-proof-keeping-its-boundary-visible) | Understand the separation and what remains open |

## 1. Separate the unknown input from the optimization variable

Call the physical input $\omega$. It is one arbitrary unknown n-qubit
state, possibly entangled across sites. The encoder must work for every
$\omega$, before learning which $U\in\{X_i,Z_i\}_{i=1}^n$ will be queried.
Write $d=2^n$ and $D=2^q$. Every recorded branch may retain a quantum
register of dimension at most D; the finite classical record is unrestricted.
The task asks for one binary output, not a reconstructed quantum state.

Refine the encoder into Kraus operators $K_c:\mathbb C^d\to\mathbb C^D$
with $\sum_cK_c^\dagger K_c=I$. Recording the Kraus label only adds
classical information. For each nonzero branch define

```math
p_c=\frac{\|K_c\|_F^2}{d},\qquad
L_c=\frac{K_c}{\|K_c\|_F},\qquad \rho_c=L_c^\dagger L_c.
```

Here $\|K\|_F^2=\operatorname{Tr}(K^\dagger K)$.
Completeness implies $\sum_cp_c=1$, while each $\rho_c$ is positive,
has trace one, and has rank at most D. Zero Kraus operators contribute
nothing and are omitted. The weights $p_c$ are the branch probabilities
only for $\omega=I/d$. In general the physical probability is
$\operatorname{Tr}(K_c\omega K_c^\dagger)$ and depends on $\omega$.

The matrix $\rho=L^\dagger L$ describes a normalized encoding operator.
It is called a **seed Gram matrix**. Optimizing over $\rho$ does not
choose a convenient physical input or replace the arbitrary-input task
by an average-source problem. It packages information about the encoder.

## 2. Why a decoder disappears into a trace norm

A binary decoder has effects $E_+,E_-$ and observable
$B=E_+-E_-$, so $-I\le B\le I$. Conversely any Hermitian contraction B
defines the effects $(I\pm B)/2$. For a Hermitian matrix H,

```math
\max_{-I\le B\le I}\operatorname{Tr}(BH)=\|H\|_1
=\sum_j|\lambda_j(H)|.
```

To see this, diagonalize H. Choosing B to have eigenvalue +1 on positive
eigenvectors and −1 on negative ones attains the sum of absolute values.
On the kernel choose B=0: the decoder returns a fair binary outcome there.
This event remains part of the protocol; it is not rejected.

Set $S=\sqrt\rho$. The polar decomposition $L=VS$ has V isometric on
the support of $\rho$, even if its rank is less than D. Thus

```math
F_U(\rho):=\|LUL^\dagger\|_1=\|SUS\|_1.
```

Why may we use an exact noisy Pauli when the original request only
specified an error tolerance? If a protocol's effective binary observable
is $A_U$, its uniform total-variation error is
$\|A_U-U\|_\infty/2$, where the operator norm of a Hermitian matrix
is its largest absolute eigenvalue. An error at most $\varepsilon_U\le1/2$ therefore
gives the Pauli coefficient

```math
\kappa_U=\frac{\operatorname{Tr}(UA_U)}d
\ge1-2\varepsilon_U.
```

Choose a uniformly random Pauli before encoding, record it, and correct
the decoded sign according to its commutation with U. This averages
$A_U$ to $\kappa_UU$: all unwanted Pauli coefficients cancel. The same
encoding randomization works for every allowed query and preserves the
memory cap. Independent classical output flips can reduce any excess
contrast to the target $\eta_U=1-2\varepsilon_U$. If both coefficients
are zero, a fair output suffices. Thus the exact noisy-observable form
does not restrict the general uniform-error problem.

Now suppose the complete instrument implements the effective observable
$\eta_UU$. Taking its Hilbert–Schmidt coefficient along U gives

```math
\eta_U=\frac1d\sum_c\operatorname{Tr}(B_{c,U}K_cUK_c^\dagger)
\le\sum_cp_cF_U(\rho_c).
```

This is the converse bridge: a bound on every rank-at-most-D seed bounds
every physical instrument. Nonnegative weighted sums obey the same rule.
Define

```math
\begin{aligned}
g(\rho)&=\sum_{i=1}^n[F_{X_i}(\rho)+F_{Z_i}(\rho)],\\
\Gamma(n,D)&=\max_{\substack{\rho\ge0,\,\operatorname{Tr}\rho=1\\
\operatorname{rank}\rho\le D}}g(\rho).
\end{aligned}
```

## 3. Why a seed really gives a complete protocol

A converse alone would leave a gap: perhaps the maximizing seed could
never belong to a valid instrument. A finite Pauli average closes it.
Given $\rho$ of rank at most D, choose $L=V\sqrt\rho$ with V an isometry
from the support of $\rho$ into the memory. Let P range over the
$m=4^n$ Pauli representatives $\{I,X,Y,Z\}^{\otimes n}$, and set

```math
K_P=\sqrt{d/m}\,LP,\qquad
\sum_PK_P^\dagger K_P=\frac dm\sum_PP^\dagger\rho P=I.
```

The last equality uses $m^{-1}\sum_PP^\dagger\rho P=I/d$.
Store P classically. Choose $B_U=\operatorname{sign}(LUL^\dagger)$,
zero on its kernel. If $PUP^\dagger=s_{P,U}U$, where $s_{P,U}=\pm1$,
use the decoder $s_{P,U}B_U$. The character identity

```math
\frac1m\sum_Ps_{P,U}P^\dagger AP=\frac{\operatorname{Tr}(UA)}d\,U
```

then makes the effective observable exactly $F_U(\rho)U$.
Every branch is included; every output dimension is at most D. The seed
has become an instrument without postselection or an additional specimen.

Finally randomize the sites and independently exchange X with Z using
local Hadamards, recording these choices. This equalizes all 2n query
contrasts while preserving their sum. The exact common-accuracy optimum is

```math
\boxed{\eta_{\max}(n,q)=\frac{\Gamma(n,2^q)}{2n},}
```

with uniform error

```math
\varepsilon_{\min}(n,q)=\frac{1-\eta_{\max}(n,q)}2.
```

For arbitrary input $\omega$, the effective effect $(I+\eta U)/2$
differs from $(I+U)/2$ by at most $(1-\eta)/2$ in outcome probability,
with equality on an appropriate U eigenstate. This explains the uniform
binary total-variation error. The full argument is in the
[normalized-seed reduction](../COLLECTIVE_ENCODING_REDUCTION.md).

## 4. Calculate what retaining a site means in seed notation

For one retained site, use the Gram factor $\rho_{r}=I/2$. Its square
root is $I/\sqrt2$, so for $U=X$ or Z,

```math
F_U(\rho_{r})=\|U/2\|_1=1.
```

For a discarded site, use a pure X/Z bisector
$\rho_{d}=|\beta\rangle\langle\beta|$, with
$|\langle X\rangle_\beta|=|\langle Z\rangle_\beta|=1/\sqrt2$. Then

```math
\sqrt{\rho_{d}}U\sqrt{\rho_{d}}
=\langle\beta|U|\beta\rangle\rho_{d},\qquad
F_U(\rho_{d})=1/\sqrt2.
```

Spectator factors have trace norm one and do not change these local
scores. A product seed with q retained factors therefore has rank $2^q$
and score $2q+\sqrt2(n-q)$. Randomizing the retained subset attains the
corresponding common contrast. On discarded sites its physical realization
is the compatible four-outcome POVM $(I+(sX+tZ)/\sqrt2)/4$.

The maximally mixed **Gram factor** on a retained site does not mean
that the physical input was depolarized. For example, the normalized
operator $L=I/\sqrt2$ has Gram $I/2$ while preserving the site's quantum
directions. The normalization belongs to the seed calculation; completion
into an instrument supplies the correct physical probabilities.

## 5. Why one memory qubit brings in CHSH

For $D=2$, choose extreme decoder contractions attaining the trace norms.
Each is a scalar sign or a traceless qubit Pauli observable. Vectorizing
L means forming

```math
\begin{aligned}
|L\rangle\!\rangle&=\sum_{a=0}^{d-1}|a\rangle_R\otimes L|a\rangle,\\
\langle\!\langle L|L\rangle\!\rangle&=\operatorname{Tr}(L^\dagger L)=1.
\end{aligned}
```

This is a normalized **virtual** pure state of n reference qubits and
the memory qubit. The references are a mathematical representation of L,
not extra copies or shared entanglement available to the protocol.

For nonnegative weights $\alpha_i,\beta_i$, the site's score becomes
$f_i=\langle\!\langle L|h_i|L\rangle\!\rangle$, where
$h_i=\alpha_iX_i\otimes B_{i,X}+\beta_iZ_i\otimes B_{i,Z}$.
The vectorization identity transposes the reference operator; the queried
X and Z matrices are real and symmetric, so that transpose changes nothing.
Put $r_i=\sqrt{\alpha_i^2+\beta_i^2}$. If either decoder is scalar,
anticommutation gives $h_i^2=r_i^2I$, so its score is at most $r_i$.
Otherwise the reference directions $(\alpha_iX_i\pm\beta_iZ_i)/r_i$
make $2h_i/r_i$ a CHSH operator. Omit sites with $r_i=0$.

The review's Section IV.A introduces the CHSH/Bell connection. The
specific ingredient here is the established Cheng–Hall monogamy result,
which permits **independently chosen
settings on the common memory qubit**, including mixed three-qubit
marginals. It implies $(f_i/r_i)^2+(f_j/r_j)^2\le2$ for the two weighted
site scores. Hence at most one site exceeds its compatible-disk value.
Since always $f_i\le\alpha_i+\beta_i$, the support bound is

```math
\sum_i(\alpha_ix_i+\beta_iz_i)
\le\sum_ir_i+\max_i(\alpha_i+\beta_i-r_i).
```

This is a qubit-memory argument, not a monogamy theorem for arbitrary
memory dimension. Its matching retention construction yields the exact
region $\sum_iw(x_i,z_i)\le1$, where
$w(x,z)=[x+z-1-\sqrt{2(1-x)(1-z)}]_+$ and $[a]_+=\max(a,0)$.
Read [the allocation proof](../ONE_QUBIT_ALLOCATION_REGION.md) for the
disk/square geometry, and [the source comparison](../CORE_PRIOR_COMPARISON.md)
for the precise Cheng–Hall attribution. The ingredient is prior work.

## 6. Fidelity, affinity, and the constraint that cannot be dropped

The root-fidelity convention is
$F(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1$, without squaring.
For a queried reflection U, $F_U(\rho)=F(\rho,U\rho U)$.
The affinity $a_U=\operatorname{Tr}(SUSU)$ is easier to expand in Pauli
coefficients, and the established inequality is $F_U^2\le a_U$.
Here is a short proof that also covers singular S. Put $A=USU\ge0$;
then $\operatorname{Tr}A^2=\operatorname{Tr}S^2=1$. Schatten Hölder gives

```math
\begin{aligned}
F_U=\|SA\|_1
&\le\|S^{1/2}\|_4\|S^{1/2}A^{1/2}\|_2\|A^{1/2}\|_4\\
&=\sqrt{\operatorname{Tr}(SA)}=\sqrt{a_U}.
\end{aligned}
```

The exponents satisfy $1/4+1/2+1/4=1$, with
$\|M\|_p=(\operatorname{Tr}|M|^p)^{1/p}$ and
$|M|=\sqrt{M^\dagger M}$. The
[sourced fidelity–affinity lemma](../STRONG_ENTROPIC_CONVERSE.md#3-root-fidelity-affinity-and-the-two-pauli-energy)
supplies its prior attribution. The finite converses bound the stronger
sum $\sum_U\sqrt{a_U}$, but keep $\operatorname{rank}S\le D$ throughout.

Rank enters through spectral rearrangement: only D eigenvalues of S can
pair with the largest eigenvalues of a chosen linear combination of
Pauli operators. Its trace
and nonuniform eigenvalues still affect that pairing. Replacing S by a
multiple of its support projector would erase constraints the proof uses;
rank alone does not authorize flattening the spectrum.

## 7. Locate every finite budget and the exact certificate

The result $\Gamma(n,2^q)=2q+\sqrt2(n-q)$ covers these 14 integer budgets:

| Input count n | Endpoint budgets | One-qubit theorem | Additional converse |
|---|---|---|---|
| 1 | $q=0,1$ | — | — |
| 2 | $q=0,2$ | $q=1$ | — |
| 3 | $q=0,3$ | $q=1$ | Half rank: $q=2$ |
| 4 | $q=0,4$ | $q=1$ | Quarter rank: $q=2$; half rank: $q=3$ |

These are integer-qubit budgets, not all non-power-of-two dimensions D.
At $q=0$, rank-one seeds obey the local Bloch bound; at $q=n$, each
query score is at most one and full retention attains it. The
[half-rank proof](../audits/HALF_RANK_RETENTION_CONVERSE.md) uses spectral
pairing and a positive quadratic. The
[quarter-rank proof](../audits/NONFLAT_QUARTER_RANK_CONVERSE.md) uses a
sum of squares in one branch and an exact polynomial certificate in the other.

Why can finitely many coefficients prove positivity everywhere? On
$[0,1]$, the Bernstein functions $B_{j,N}(t)=\binom Nj t^j(1-t)^{N-j}$
are nonnegative and sum to one. A bivariate polynomial expressed as
$\sum_{j,k}c_{jk}B_{j,N}(x)B_{k,M}(y)$ is therefore a weighted average
of its coefficients at every point. If all coefficients exceed a bound,
the polynomial exceeds it on the entire square, including the boundary.
Rescaling applies the same reasoning to $[0,9/25]^2$.

The needed polynomials C and P have bidegrees $(6,4)$ and $(10,8)$:
35 and 99 coefficients. Exact rational interval arithmetic proves their
coefficients exceed $4/25$ and $1/10000$, respectively, without subdivision.
This proves two scalar inequalities. The analytical argument must still
justify the substitutions, positive denominators, complete branch
coverage, and equality cases. Neither sampled matrices nor a numerical
grid supplies those steps. The [certificate report](../../results/nonflat_quarter_rank_certificate.json)
and [evidence freeze](../SCIENTIFIC_EVIDENCE_FREEZE.md) distinguish this
exact proof component from historical construction diagnostics.

## 8. A small support explains the 31-input collective example

In the X eigenbasis, take the support $\mathcal C=\{0,e_1,\ldots,e_n\}$
with $p_0=1/2$ and $p_{e_i}=1/(2n)$. The diagonal Gram matrix has rank
$n+1$, and a seed is $L=\sum_{u\in\mathcal C}\sqrt{p_u}|u\rangle_Q\langle u|_X$.
Since $X_i$ is diagonal, $LX_iL^\dagger$ has entries $\pm p_u$, giving
$F_{X_i}=\sum_up_u=1$. Since $Z_i$ flips the ith X-basis bit, its only
pair wholly inside this support is $0\leftrightarrow e_i$. Thus

```math
\begin{aligned}
LZ_iL^\dagger&=\sqrt{p_0p_{e_i}}
(|0\rangle\langle e_i|+|e_i\rangle\langle0|),\\
F_{Z_i}&=2\sqrt{p_0p_{e_i}}=1/\sqrt n.
\end{aligned}
```

For $n=31$ the required dimension is $D=32=2^5$. The particularly simple
complete instrument is $K_s=LZ^s$ for all bit strings s, with s stored
classically: translations give $\sum_sK_s^\dagger K_s=I$, without another
normalization factor. Correct the X decoder's signs using s; for Z use
$B_{i,Z}=|0\rangle\langle e_i|+|e_i\rangle\langle0|$, with fair outputs
on its kernel. This decoder has eigenvalues $+1,-1,0$; the probability
factor in $LZ_iL^\dagger$ is not part of the decoder. The
[exact-axis proof](../EXACT_AXIS_SPECTRAL_REDUCTION.md) derives the effective
observables $X_i$ and $Z_i/\sqrt{31}$ on arbitrary physical inputs.

The comparison class admits a Kraus refinement
$K_c=M_c\otimes\langle v_c|$ across a branch-dependent original subset
$T_c$ and its complement, with $|T_c|\le q$. The discarded vector may
be entangled, allowing joint measurements of discarded sites; all branches
obey the same output cap and global completeness. Retained and discarded
site scores respectively give, for $a,b\ge0$,

```math
\sum_i(ax_i+bz_i)\le q(a+b)+(n-q)\sqrt{a^2+b^2}.
```

When all $x_i=1$, taking $b=1$ and $a\to\infty$ gives $\sum_i z_i\le q$.
The collective example instead gives $\sqrt{31}>5$. This separates the
specified retention class; it neither proves an unrestricted optimum
nor improves the equal-accuracy theorem.

## 9. Continue with the proof, keeping its boundary visible

The stronger affinity objective cannot establish the general retention
formula: an [exact counterexample to that surrogate](../audits/AFFINITY_METHOD_LIMIT.md)
already exists at $n=15,q=4$, while its original trace-norm score remains
below retention. This is a limitation of the relaxation, not a
counterexample to the original common-accuracy conjecture. The unrestricted
common-accuracy problem at larger intermediate budgets remains open,
beginning at $(5,2)$.

The [balanced-spectrum theorem](../audits/BALANCED_SPECTRUM_OPTIMALITY.md)
and [stability extension](../audits/BALANCED_SPECTRUM_STABILITY.md) are
optional structural companions. Their all-size flat half-rank result
and sufficient nonflat neighborhood do not replace an unrestricted
rank converse or supply a missing premise of the 14-budget proof.

Next read [CORE_ARGUMENT.md](../CORE_ARGUMENT.md), Sections 1–4, with
this distinction in mind: the physical input is arbitrary, the seed is
optimized, and every claimed protocol must be completed into an instrument.
