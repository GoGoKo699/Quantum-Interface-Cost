# A global converse from quantum logarithmic-Sobolev theory

Date: 2026-09-22. Research base:
`f9a5fc72d15e9d314f6deae65096605e955a2051`.
Status: derived with the proof below and independently reconstructed by
another agent in this workspace. This is an application of established
functional inequalities, not a new logarithmic-Sobolev theorem or a
certification of publication novelty.

This note gives an explicit lower bound throughout the nonclassical region
of the unrestricted interface problem. It preserves the single unknown
specimen, one delayed local query, arbitrary collective encoding, free
finite classical records, worst-case quantum dimension, and uniform
arbitrary-input error in [RESEARCH_NOTE.md](../RESEARCH_NOTE.md), Section 2.

## 1. Statement

Write $\eta_0=1/\sqrt2$, and let $h_2$ denote binary entropy in bits. Define

$$
b(\eta)=
\begin{cases}
0,&0\le\eta\le\eta_0,\\[2mm]
h_2\!\left(\dfrac{1-\sqrt{1-(2\eta^2-1)^2}}2\right),
&\eta_0<\eta\le1.
\end{cases}
\tag{1}
$$

**Theorem.** Every admissible protocol of contrast $\eta$ retaining at most
q qubits on every branch satisfies

$$
\boxed{q\ge n b(\eta).}
\tag{2}
$$

Thus $q_{\min}(n,\eta)\ge\lceil n b(\eta)\rceil$ and
$R(\eta)\ge b(\eta)$. In particular, $b(\eta)>0$ for every
$\eta>\eta_0$, and $b(1)=1$.

The underlying state inequality holds for every n-qubit density matrix
$\rho$, including singular matrices with entangled eigenvectors. Set

$$
f_n(\rho)=\frac1{2n}\sum_{i=1}^n\sum_{b=X,Z}
\|\sqrt\rho P_{i,b}\sqrt\rho\|_1,
\qquad s=\frac{S(\rho)}n,
\qquad u=h_2^{-1}(s),
$$

where the inverse uses the interval $[0,1/2]$. Then

$$
\boxed{f_n(\rho)^2\le\frac12+\sqrt{u(1-u)}.}
\tag{3}
$$

This is weaker than the conjectured linear entropy bound that would prove
the subset strategy optimal. It improves the available global converse
without resolving that conjecture.

## 2. The prior entropy-energy theorem and normalization

Let $d=2^n$, $\tau(T)=\operatorname{Tr}(T)/d$, and
$A=\sqrt{d\rho}$. Thus $\tau(A^2)=1$. For site i, define the conditional
expectation $\mathcal E_i$ by normalized partial trace at i and reinsertion
of the local identity. Put

$$
\mathcal K_n=\sum_i(\mathrm{id}-\mathcal E_i),
\qquad \mathscr D(A)=\tau(A\mathcal K_n(A)).
\tag{4}
$$

These are exactly the tensor-product depolarizing generator and Dirichlet
form used by Beigi, [arXiv:2105.00462v2](https://arxiv.org/pdf/2105.00462v2),
9 December 2021, Eqs. (2)–(3). His **Theorem 2, Eqs. (6)–(7), printed
p. 4**, applies to every positive semidefinite A. In its natural-logarithm
convention,

$$
\operatorname{Ent}(A^2)
=\tau(A^2\ln A^2)-\tau(A^2)\ln\tau(A^2)
=(n-S(\rho))\ln2.
$$

The source's parameter is therefore
$\xi=\operatorname{Ent}(A^2)/(n\tau(A^2))=(1-s)\ln2$.
Its inverse binary entropy at $\ln2-\xi$ is our $u=h_2^{-1}(s)$.
Substitution gives the established inequality in the form needed here:

$$
\frac{\mathscr D(A)}n
\ge\frac12-\sqrt{u(1-u)}.
\tag{5}
$$

All subsequent steps are the supplied deduction connecting this energy
bound to the interface workload.

## 3. Root fidelity, affinity, and the two-Pauli energy

For each local Pauli P define

$$
F_P=\|\sqrt\rho P\sqrt\rho\|_1,
\qquad a_P=\operatorname{Tr}(\sqrt\rho P\sqrt\rho P)
=\tau(A P A P).
$$

Here $F_P$ is the **root fidelity**, without squaring, between $\rho$
and $P\rho P$. The number $a_P$ is their affinity. The needed comparison is

$$
F_P^2\le a_P.
\tag{6}
$$

Audenaert–Nussbaum–Szkoła–Verstraete,
[arXiv:0708.4282v1](https://arxiv.org/pdf/0708.4282v1), **Appendix A,
Theorem 6, Eq. (55), printed p. 32**, gives this at its parameter $s=1/2$.
Its root-fidelity convention is explicit in Eq. (27). For completeness,
the relevant special case follows from Schatten Hölder with exponents
4, 2, 4: for two states $\rho,\sigma$,

$$
\begin{aligned}
\|\rho^{1/2}\sigma^{1/2}\|_1
&=\|\rho^{1/4}(\rho^{1/4}\sigma^{1/4})\sigma^{1/4}\|_1\\
&\le\|\rho^{1/4}\|_4
\|\rho^{1/4}\sigma^{1/4}\|_2
\|\sigma^{1/4}\|_4\\
&=\sqrt{\operatorname{Tr}(\sqrt\rho\sqrt\sigma)}.
\end{aligned}
$$

Taking $\sigma=P\rho P$ proves (6), including singular states. This uses
only a matrix inequality from the source; its many-copy hypothesis-testing
task is not substituted for the interface model.

Expand A in the normalized Pauli basis:

$$
A=\sum_{w\in\{I,X,Y,Z\}^n}c_w\sigma_w,
\qquad \sum_w c_w^2=1.
$$

The coefficients are real because A is Hermitian; matrices and seeds need
not be real. Let $N_X(w),N_Y(w),N_Z(w)$ count the corresponding letters,
and $|w|=N_X(w)+N_Y(w)+N_Z(w)$. The generator is diagonal in this basis,
so $\mathscr D(A)=\sum_w|w|c_w^2$. Conjugation by a local X or Z changes
a Pauli string's sign precisely when the two local letters anticommute.
Consequently the exact identity is

$$
\begin{aligned}
\sum_{i,b=X,Z}(1-a_{P_{i,b}})
&=\sum_w\bigl(2N_X(w)+4N_Y(w)+2N_Z(w)\bigr)c_w^2\\
&=2\mathscr D(A)+2\sum_w N_Y(w)c_w^2
\ge2\mathscr D(A).
\end{aligned}
\tag{7}
$$

Cauchy–Schwarz, (6), and (7) now give

$$
\begin{aligned}
f_n(\rho)^2
&\le\frac1{2n}\sum_{i,b}F_{P_{i,b}}^2
\le\frac1{2n}\sum_{i,b}a_{P_{i,b}}\\
&\le1-\frac{\mathscr D(A)}n
\le\frac12+\sqrt{u(1-u)}.
\end{aligned}
\tag{8}
$$

This proves (3). If $f_n(\rho)\ge\eta\ge\eta_0$, then
$\sqrt{u(1-u)}\ge\eta^2-1/2$. Both $u(1-u)$ and $h_2(u)$ increase
on $[0,1/2]$, giving $S(\rho)/n\ge b(\eta)$ after inversion.

## 4. Why the converse charges worst-case quantum dimension

Here is the required direction of the
[normalized-seed reduction](COLLECTIVE_ENCODING_REDUCTION.md), stated
explicitly to keep the resource accounting independent of an asymptotic
compression interpretation.

Refine every classical branch of the encoder into individual Kraus maps
$K_a:\mathbb C^d\to\mathbb C^D$, where $D\le2^q$, retaining the finite
refinement label classically. Each branch has the same dimension cap.
Let $B_{a,j}$ be the decoder's Hermitian contraction for query j. The
effective observable identity is

$$
\sum_a K_a^\dagger B_{a,j}K_a=\eta P_j,
\qquad \sum_a K_a^\dagger K_a=I.
$$

Omit zero Kraus maps and define

$$
L_a=\frac{K_a}{\sqrt{\operatorname{Tr}K_a^\dagger K_a}},
\qquad p_a=\frac{\operatorname{Tr}K_a^\dagger K_a}{d}.
$$

Then $\sum_a p_a=1$ and $\operatorname{Tr}L_a^\dagger L_a=1$.
Trace-norm duality implies

$$
2n\eta
=\frac1d\sum_j\operatorname{Tr}
\left(P_j\sum_aK_a^\dagger B_{a,j}K_a\right)
\le\sum_a p_a\sum_j\|L_aP_jL_a^\dagger\|_1.
\tag{9}
$$

At least one normalized seed has score at least $2n\eta$. For its Gram
matrix $\rho=L_a^\dagger L_a$, polar decomposition preserves the relevant
nonzero singular values, so $f_n(\rho)\ge\eta$, while

$$
S(\rho)\le\log_2\operatorname{rank}\rho\le\log_2D\le q.
$$

Combining this with (3) proves (2). The weights $p_a$ are an algebraic
averaging device under the maximally mixed test input, not an average
memory allowance. Every term already obeys the original worst-case cap.
There is no postselection or physical branch-discarding step in this
converse. The reduction from uniform total-variation error to contrast in
the research note preserves the same cap.

Alternatively, Beigi's **Theorem 4, printed p. 6**, supplies (5) with
$u=h_2^{-1}(\log_2\operatorname{rank}\rho/n)$ directly. Equations (6)–(8)
then prove the dimension bound without first passing through entropy.
Neither route uses the repository's asymptotic entropy characterization.

## 5. Consequences, endpoint scales, and the remaining gap

All established lower bounds may safely be combined as

$$
L_{\rm combined}(\eta)=\max\left\{
0,\ b(\eta),\ 1-2h_2((1-\eta)/2),\
\frac{(\eta-\eta_0)_+^2}{16\ln2}
\right\}.
$$

Then $q_{\min}(n,\eta)\ge\lceil nL_{\rm combined}(\eta)\rceil$.
The [subset construction](../RESEARCH_NOTE.md), Section 4, gives

$$
L_{\rm combined}(\eta)\le R(\eta)
\le\frac{\eta-\eta_0}{1-\eta_0}
\qquad(\eta_0<\eta\le1).
$$

The maximum retains earlier proofs without asserting an unproved
pointwise dominance relation between their formulas. For illustration,
these are evaluations of proved scalar bounds:

| Contrast | $b(\eta)$ | Earlier uncertainty bound, clipped at zero | Subset rate upper bound |
|---:|---:|---:|---:|
| 0.75 | 0.03699741 | 0 | 0.14644661 |
| 0.80 | 0.14144054 | 0.06200881 | 0.31715729 |
| 0.90 | 0.49293649 | 0.42720609 | 0.65857864 |
| 0.95 | 0.72860252 | 0.66267814 | 0.82928932 |

For $t\downarrow0$, the argument of $h_2$ in $b(\eta_0+t)$ is
$2t^2+O(t^3)$. Hence

$$
b(\eta_0+t)=4t^2\log_2(1/t)+O(t^2).
\tag{10}
$$

The converse therefore improves the earlier quadratic threshold bound by
a logarithmic factor. It still leaves a gap to the subset rate, which is
linear in t.

For $\delta\downarrow0$, put $v=1-(2(1-\delta)^2-1)^2
=8\delta+O(\delta^2)$. The expansion
$h_2((1-\sqrt v)/2)=1-v/(2\ln2)+O(v^2)$ gives

$$
b(1-\delta)=1-\frac{4\delta}{\ln2}+O(\delta^2).
\tag{11}
$$

Thus, with $\varepsilon_0=(1-\eta_0)/2$ and
$0<\varepsilon<\varepsilon_0$, substituting
$\eta=1-2\varepsilon$ gives a converse in the original worst-case
binary total-variation error. At perfect readout, (2) recovers $q=n$.

The bound does not settle the first unresolved block. With $n=3,q=2$,
let $u=h_2^{-1}(2/3)\simeq0.1739523314$. Equation (3) only gives

$$
\eta_{\max}(3,2)\le0.9375865224,
\qquad \Gamma(3,4)\le5.6255191343.
$$

The subset construction has contrast $(4+\sqrt2)/6\simeq0.9023689271$
and score $4+\sqrt2$. Both a strict collective advantage and the sharp
subset converse remain unresolved for this block.

## 6. Novelty and proof boundary

The improvement comes from applying Beigi's established entropy-energy
theorem to the exact seed formulation, with the fidelity comparison and
two-Pauli Fourier identity. It is a short task-specific deduction. The
underlying logarithmic-Sobolev, Faber–Krahn, and fidelity inequalities are
prior results. A search for an earlier identical operational corollary
remains part of the publication audit.

Affinity satisfies $a_P\le F_P$, so simply replacing the Dirichlet
affinity by root fidelity would reverse the useful inequality. Equation
(6) is the valid replacement and exposes the quantitative loss. For
example, at $u=0.1$, hence $s=h_2(0.1)\simeq0.46899559$, (3) permits
$g/n\le\sqrt{3.2}\simeq1.78885438$. The conjectured linear upper bound
$\sqrt2+(2-\sqrt2)s$ is approximately $1.68894$. Sharpness of the prior
Dirichlet theorem therefore does not establish sharpness for this
interface score, and the unrestricted linear entropy inequality remains
open.

`tools/check_entropy_bounds.py` checks the fidelity, energy and entropy chain
on 22 finite matrices alongside the separately proved seed-family formulas.
The recorded `results/entropy_bounds.json` also reproduces the scalar rate
table. These diagnostics supplement the proof; no optimization is performed.
