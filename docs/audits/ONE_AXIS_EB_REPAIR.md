# An explicit entanglement-breaking repair from one Pauli image

**Research base:** main `7cb964b47b8aa13a604a3ab5df663d4f399fa6f4`.
**Date:** 27 September 2026.

A qubit-input channel that transmits little information about one Pauli
axis has an explicit nearby entanglement-breaking channel. The construction
mixes it with a measurement-and-preparation channel whose response on that
axis has the opposite sign. It applies in every finite output dimension.
For the actual two-mode head, a direct resolvent comparison proves the
converse throughout `m>=2+sqrt(2)` whenever the trace norm of one Pauli
image is at most `2/3`.

**Status:** supplied channel construction and norm estimate, independently
reconstructed within this workspace. The underlying separability criterion
and closely related positive-completion geometry are established prior
work, credited below. This is internal review, not external peer review.
No publication-priority claim or unrestricted interface converse is made.

## 1. The channel repair and its distance

Let Phi be any channel from a qubit to a finite-dimensional memory Q.
Choose an input Pauli observable A, so `A=A^dagger`, `A^2=I`, and
`Tr A=0`, and put

$$
M=\Phi(A),\qquad n=\frac12\|M\|_1.
\tag{1}
$$

Trace preservation and trace-norm contraction give `Tr M=0` and
`0<=n<=1`. Write `M=M_+-M_-` for its positive and negative parts.
When n>0, each has trace n. Let `P_+=(I+A)/2`, `P_-=(I-A)/2`, and define

$$
\Theta_A(\omega)=
 \operatorname{Tr}(P_-\omega)\frac{M_+}{n}
 +\operatorname{Tr}(P_+\omega)\frac{M_-}{n}.
\tag{2}
$$

This is an EB channel: measure the input axis and prepare the indicated
state with the **opposite** output sign. In particular
`Theta_A(A)=-M/n`. Consequently the channel

$$
\boxed{\Psi_A=\frac{\Phi+n\Theta_A}{1+n}}
\tag{3}
$$

kills A. Every qubit-input channel that kills one Pauli observable is EB;
Section 2 supplies the established separability implication and its proof.
Thus (3) is an explicit EB comparator. Since two channels have full
diamond distance at most two,

$$
\boxed{\operatorname{dist}_\diamond(\Phi,\mathrm{EB})
\le\|\Phi-\Psi_A\|_\diamond
\le\frac{2n}{1+n}
=\frac{\|\Phi(A)\|_1}{1+\|\Phi(A)\|_1/2}.}
\tag{4}
$$

For n=0, Phi itself kills A and is EB; set `Psi_A=Phi`. Any input axis
may be chosen, so (4) also holds with n minimized over all unit Pauli
axes. The norm in (4) is the full diamond norm, without an additional
factor one half. No unitality, Choi-rank, PPT or real-matrix assumption
is imposed on Phi.

The quantity n is the trace distance between `Phi(P_+)` and `Phi(P_-)`.
It therefore measures distinguishability of the two opposite input
states on the chosen axis. Equation (4) is a sufficient distance bound;
its optimality is asserted only at the identity endpoint in Section 4,
not at every intermediate n.

## 2. Killing one Pauli is an established separability condition

A unitary change of input basis reduces to A=Y. In the normalized Choi
convention,

$$
J_\Phi=\frac14\bigl[I\otimes\Phi(I)+X\otimes\Phi(X)
 -Y\otimes\Phi(Y)+Z\otimes\Phi(Z)\bigr].
\tag{5}
$$

When `Phi(Y)=0`, J is invariant under partial transpose on its input
qubit. Theorem 2 of M. Lewenstein, J. I. Cirac and S. Karnas,
[*Separability and entanglement in 2 x N composite quantum systems*](https://arxiv.org/abs/quant-ph/9903012)
(1999), proves that every such positive operator is separable. The
Pauli-component positive completion used in Section 3 is also closely
related to their Eqs. (8)--(11) and Theorem 3. The channel-preserving
normalization, norm estimate and application here are supplied deductions;
no new separability or positive-completion principle is claimed.

For completeness, the implication has an elementary block proof. Write

$$
J=\begin{pmatrix}A_0&B_0\\B_0&C_0\end{pmatrix}\ge0,
\qquad B_0=B_0^\dagger.
$$

If A_0 is positive definite, conjugation by
`I_2 tensor A_0^(-1/2)` gives

$$
J'=\begin{pmatrix}I&B\\B&C\end{pmatrix},
\qquad B=B^\dagger,\qquad C-B^2\ge0.
$$

The last inequality is the Schur complement. Diagonalize
`B=sum_j b_j |v_j><v_j|`. Then

$$
\begin{pmatrix}I&B\\B&B^2\end{pmatrix}
=\sum_j (|0\rangle+b_j|1\rangle)
 (\langle0|+b_j\langle1|)\otimes|v_j\rangle\langle v_j|
\tag{6}
$$

is separable, as is the remaining positive term
`|1><1| tensor (C-B^2)`. Undoing the local congruence preserves
separability. For singular A_0, add
`epsilon |0><0| tensor I_Q`, apply the preceding argument, and let
epsilon decrease to zero. The finite-dimensional separable cone is
closed. Thus J is separable, equivalently Phi is EB. Input-unitary
changes preserve both EB and diamond distance, giving the assertion
for any Pauli A.

## 3. Choi normalization and the sign of the correction

Still use A=Y and set `M=Phi(Y)`. Define

$$
N=\frac14(I\otimes|M|+Y\otimes M)
 =\frac12\bigl(P_+^Y\otimes M_++P_-^Y\otimes M_-\bigr).
\tag{7}
$$

This is positive and separable, with

$$
\operatorname{Tr}N=n,\qquad
\operatorname{Tr}_Q N=nI_2/2.
$$

Hence N/n is the normalized Choi state of the EB channel Theta_Y.
The input transpose in the Choi convention flips Y. This accounts for
the opposite physical measurement labels in (2): P_- prepares M_+/n,
and P_+ prepares M_-/n.

The repaired Choi state is

$$
J_{\Psi_Y}=\frac{J_\Phi+N}{1+n}.
\tag{8}
$$

Its Y component cancels, it remains positive, and its input marginal is
I/2. In particular the construction does not assume that simply averaging
J with its partial transpose would preserve positivity.

## 4. Sharpness at the identity endpoint

For the identity qubit channel, n=1 for every Pauli axis, so (4) gives an
EB comparator at full diamond distance at most one. Conversely the
normalized Choi state of any EB channel is separable and has overlap at
most one half with the Bell state `J_id`. Measuring that Bell projector
gives `||J_id-J_EB||_1>=1`. The normalized Bell input is allowed in the
diamond norm, proving

$$
\boxed{\inf_{\Psi\in\mathrm{EB}}
 \|\operatorname{id}_2-\Psi\|_\diamond=1.}
\tag{9}
$$

Thus the bound is sharp at n=1. This does not prove that the function
`2n/(1+n)` is optimal at intermediate n.

## 5. A direct resolvent comparison using the two EB channels

The particular repair also yields a pointwise bound without first passing
through diamond distance. Let `B,D_3` be Hermitian memory contractions,
`h=X tensor B+Z tensor D_3`, and `R_t=(tI-h)^(-1)` for t>2. The
[exact pure-memory resolvent bound](EXACT_LAST_QUERY_RESOLVENT.md#1-the-readout-elimination-theorem)
is

$$
F(t)=\begin{cases}
\displaystyle\frac1{2(\sqrt{2t^2-4}-t)},&2<t\le3\sqrt2,\\[5pt]
\displaystyle\frac1{t-\sqrt2},&t\ge3\sqrt2.
\end{cases}
\tag{10}
$$

Every EB channel Xi satisfies both inequalities

$$
\frac{I}{t+\sqrt2}
\le(\operatorname{id}_2\otimes\Xi^*)(R_t)
\le F(t)I.
\tag{11}
$$

For the upper bound, apply (10) to each prepared memory state of Xi.
For the lower bound, let `C_tau(W)=Tr_Q[(I tensor tau)W]` be the
unital completely positive compression associated with a memory state
tau. Applying this map blockwise to the positive matrix

$$
\begin{pmatrix}R_t&I\\I&tI-h\end{pmatrix}\ge0
$$

and taking its Schur complement gives

$$
\mathcal C_\tau(R_t)
\ge(tI-X\operatorname{Tr}(\tau B)
        -Z\operatorname{Tr}(\tau D_3))^{-1}
\ge\frac{I}{t+\sqrt2}.
$$

The last inequality uses the bound of one on each expectation.
In a measurement-and-preparation representation of Xi, its positive
measurement effects sum to I; summing these compression bounds proves
(11), also for mixed and nonorthogonal prepared states.

Equation (3) gives `Phi=(1+n)Psi_A-nTheta_A`. Since both comparison
channels are EB, use the upper bound for Psi_A and the lower bound for
Theta_A to obtain

$$
\boxed{(\operatorname{id}_2\otimes\Phi^*)(R_t)
\le\left[(1+n)F(t)-\frac{n}{t+\sqrt2}\right]I.}
\tag{12}
$$

For n=0 the same inequality follows directly because Phi is EB.
In the [actual two-mode envelope](TWO_MODE_RESOLVENT.md), let U,m,ell
be the first three earlier eigenvalues, set `Lambda=4+sqrt(2)` and
`t=Lambda-ell>2`, and let `Delta=diag(U-ell,m-ell)`. Congruence by
`I tensor sqrt(Delta)` in (12) implies

$$
\boxed{\mathcal K_t\le
(U-\ell)\left[(1+n)F(\Lambda-\ell)
 -\frac{n}{\Lambda-\ell+\sqrt2}\right]I.}
\tag{13}
$$

Thus a right side at most I is another sufficient converse condition,
retaining the actual coherent head channel. It can be checked directly
at the actual U,ell,n; the next section gives a uniform consequence.

## 6. A uniform sufficient condition for the actual head channel

For the actual two-mode channel keep the definitions

$$
\Lambda=4+\sqrt2,\qquad D=\Lambda-U,\qquad t=\Lambda-\ell.
$$

**Theorem.** Suppose the actual spectral parameters obey

$$
D\ge19/10,\qquad12/5\le t\le\Lambda.
\tag{14}
$$

If an input Pauli axis A satisfies

$$
\boxed{\|\Phi(A)\|_1\le\frac23,}
\tag{15}
$$

then the coherent two-mode envelope passes strictly for every third
binary-POVM pair, and the actual three-query norm is at most Lambda.
The whole regime `m>=2+sqrt(2)` meets (14), so (15) is sufficient
throughout that regime.

**Proof.** Here `n<=1/3`. The coefficient in (13) increases with n,
and `U-ell=t-D`. It therefore suffices to prove

$$
(t-19/10)\left[\frac43F(t)-\frac1{3(t+\sqrt2)}\right]<1
\tag{16}
$$

on (14). First suppose `t<=3sqrt(2)`. The positive-square identity

$$
\left(\frac{3t}{2}-\frac7{10}\right)^2-(2t^2-4)
=\frac14\left(t-\frac{21}{5}\right)^2+\frac2{25}
$$

gives `sqrt(2t^2-4)<=3t/2-7/10`. Rationalizing (10) and using
`sqrt(2)<10/7`, the left side of (16) minus one is at most

$$
\frac{P(t)}{3(t^2-4)(t+10/7)},\qquad
P(t)=t^3-\frac{43}{7}t^2+\frac{1081}{350}t+\frac{467}{35}.
\tag{17}
$$

The branch lies in `[12/5,17/4]`. There `P''(t)>=74/35>0`, while

$$
P(12/5)=-\frac{703}{875},\qquad
P(17/4)=-\frac{86469}{11200}.
$$

Convexity gives strict negativity throughout the containing interval.

For `3sqrt(2)<=t<=Lambda`, write `r=sqrt(2)` and use the second
branch of F. Clearing the positive denominator `3(t^2-2)` reduces
(16) to

$$
L(t):=(5r-57/10)t-19r/2+6<0.
\tag{18}
$$

The slope is positive. At the upper endpoint,
`L(Lambda)=(24r-34)/5<-2/175`, using `r<99/70`.
This proves (16), then (13) proves the strict envelope test.

Finally, every actual head with `m>=2+sqrt(2)` has `D>19/10` and
`t>12/5` by
[the spectral bounds for the robust converse](ROBUST_HEAD_CHANNEL_CONVERSE.md#2-the-complete-high-second-mode-strip-lies-in-the-rectangle).
Reference chirality gives `ell>=0`, hence `t<=Lambda`. Thus (14)
holds on the entire stated strip.

Independently, (4) gives full diamond distance at most `2/5` under the
condition `||Phi(A)||_1<=1/2`, recovering the earlier robust criterion.
The threshold (15) instead uses the explicit EB difference in (12).
Both arguments retain the actual channel and its coherent blocks.

This replaces an existential EB-distance condition by a directly evaluable
one-axis condition. It is **not** claimed that every high-m head satisfies
(15). For example the scalar endpoint
`U=m=2+sqrt(2)`, `Phi(omega)=I_A/2 tensor omega_B` has
`||Phi(A)||_1=2` on every input Pauli axis and EB distance one. Its
physical converse follows instead from the triangle inequality. A useful
global relation between earlier support and the one-axis norm remains
open.

## 7. Verification and scope

Independent internal review reconstructed the opposite-label channel,
Choi factors and trace-preserving condition, the diamond estimate, the
singular-block separability argument, and identity endpoint. The direct
resolvent comparison additionally uses the supplied block-positivity
argument and the established exact pure-memory bound. The uniform
`2/3` threshold follows from the independently reconstructed cubic and
linear certificates in Section 6. No numerical calculation is needed
for these deductions.

Targeted fixed constructions supplement the proof:

```bash
python tools/check_direct_resolvent_and_channel.py --output results/direct_resolvent_and_channel.json
```

The [checker](../../tools/check_direct_resolvent_and_channel.py) and
[result record](../../results/direct_resolvent_and_channel.json) distinguish
finite matrix diagnostics from analytical statements and record hashes of
the source and proof notes. They do not establish a universal theorem by
sampling or certify publication novelty. The single-specimen model,
unlimited classical side information, worst-case quantum-memory bound,
and unrestricted encoding assumptions are unchanged.
