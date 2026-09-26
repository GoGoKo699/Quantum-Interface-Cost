# Compression bounds do not certify the two-mode spectral envelope

**Research base:** main `5434c44c31f42143d4b1f3d32892744b443d6cd4`.
**Date:** 26 September 2026.

The [two-mode reduction](TWO_MODE_RESOLVENT.md) leaves a four-by-four
last-query test that retains the full channel of the leading eigenspace.
This note proves a necessary matrix compatibility inequality for that
channel, then gives an exact obstruction to a stronger relaxation. Even
the complete spectrum, all memory-valued polynomial moments, fixed
reference chirality, and every rank-one and rank-two memory compression
bound together do not imply that the spectral envelope passes its test.

**Status:** supplied analytical proofs and an exact synthetic obstruction.
The constructed operator is outside the allowed earlier-query class.
Its specified leading eigenspace cannot occur at the specified energy
in that class. Failure of its positive spectral envelope does not imply
failure of the original operator bound. The universal envelope test for
physical data, the unrestricted converse, and publication priority remain
unresolved.

## 1. A matrix compatibility inequality for actual heads

Let

\[
H_0=X_1B_1+Z_1D_1+X_2B_2+Z_2D_2,
\qquad -I\le B_i,D_i\le I,
\tag{1}
\]

on reference qubits R1,R2 and a four-dimensional memory Q. Its chiral
symmetry is `Gamma=Y_1Y_2 tensor I_Q`. Write its first three eigenvalues
as U,m,ell, let `V e_a=Omega_a` select the first two eigenvectors, and put
`Sigma=diag(U,m)`. The dual head channel is

\[
\mathcal E(A)=V^\dagger(I_R\otimes A)V,
\qquad \Phi(\omega)=\operatorname{Tr}_R(V\omega V^\dagger).
\]

Every rank-r memory projector Pi obeys

\[
\|\widehat\Pi H_0\widehat\Pi\|\le k_r,
\qquad \widehat\Pi=I_R\otimes\Pi,
\qquad k_1=2\sqrt2,\quad k_2=2+\sqrt2.
\tag{2}
\]

For r=1 each compressed reference field has norm at most sqrt(2).
For r=2 this is the established
[one-retained-qubit bound](../ONE_QUBIT_OPTIMALITY.md).

For U>0 these full compression bounds imply the matrix inequality

\[
\boxed{\mathcal E(\Pi)\le
(U+k_r)(\Sigma+UI_2)^{-1}.}
\tag{3}
\]

Indeed chirality gives `||H_0||=U`, and spectral ordering gives
`H_0>=V(Sigma+UI_2)V^dagger-UI`. Combining its compression with (2)
yields
`Pi_hat V(Sigma+UI_2)V^dagger Pi_hat<=(U+k_r)Pi_hat`.
The nonzero singular values of
`Pi_hat V sqrt(Sigma+UI_2)` give
`sqrt(Sigma+UI_2) E(Pi) sqrt(Sigma+UI_2)<=(U+k_r)I_2`, proving (3).
The zero operator needs no inverse and is trivial.

In particular every pure head superposition, not only the selected
eigenbasis, satisfies

\[
\sum_{j=1}^r\lambda_j\bigl(\Phi(|z\rangle\langle z|)\bigr)
\le\min\left\{1,\frac{U+k_r}{U+m}\right\}.
\tag{4}
\]

If `m>2+sqrt(2)`, every nonzero leading superposition therefore has
Schmidt rank at least three across references versus memory. This rules
out a noiseless head qubit tensored with a fixed rank-two ancillary state.
The next example nevertheless satisfies the stronger full bounds (2).

## 2. An explicit chiral operator and its coherent head channel

Use tensor order R1,R2,F,L, with `Q=F tensor L`. Set

\[
u=2\sqrt3,\qquad \ell=2/\sqrt3,\qquad g=u-\ell=4/\sqrt3,
\qquad p=1/20,\qquad q=19/20.
\tag{5}
\]

Let W swap the memory qubits F,L, and define

\[
V_0|\psi\rangle=|0\rangle_{R_1}|\Phi^+\rangle_{R_2F}|\psi\rangle_L,
\quad P_0=V_0V_0^\dagger,\quad
T=\sqrt q\,I-i\sqrt p\,Y_1W.
\]

The unitary T commutes with Gamma. Begin with

\[
H_{\rm base}=\ell Z_1+g(P_0-\Gamma P_0\Gamma)
=\frac{3Z_1+X_2X_F+Z_2Z_F-Z_1Y_2Y_F}{\sqrt3},
\]

where identities on omitted factors are implicit. Put

\[
H=T H_{\rm base}T^\dagger,\quad V=TV_0,\quad P=VV^\dagger,
\quad N=\Gamma P\Gamma,\quad
J=T Z_1T^\dagger=(1-2p)Z_1+2\sqrt{pq}X_1W.
\]

Then J is an involution, `JP=P`, `JN=-N`, and

\[
H=\ell J+g(P-N),\qquad \Gamma H\Gamma=-H.
\tag{6}
\]

Its spectrum, including multiplicity, is

\[
\boxed{\{+u\ (\times2),+\ell\ (\times6),
             -\ell\ (\times6),-u\ (\times2)\}.}
\tag{7}
\]

This is the complete spectrum of the actual balanced example in
[the two-mode note, Section 5.1](TWO_MODE_RESOLVENT.md#51-an-actual-balanced-example-needs-both-leading-modes).
In particular the actual third eigenvalue is ell, and
`2u^2+6ell^2=32`. No raised or approximate tail is used.

The leading isometry is the coherent sum

\[
V|\psi\rangle=\sqrt q\,|0\rangle_1|\Phi^+\rangle_{2F}|\psi\rangle_L
+\sqrt p\,|1\rangle_1|\psi\rangle_F|\Phi^+\rangle_{2L}.
\]

Its full channel, including off-diagonal head inputs, is

\[
\boxed{\Phi(\omega)=q\frac{I_F}{2}\otimes\omega_L
+p\omega_F\otimes\frac{I_L}{2}.}
\tag{8}
\]

The specified reference space has dimension four, so four Kraus
operators suffice. No head dephasing or independent-marginal replacement
is made.

## 3. All polynomial memory moments and low-rank compression caps pass

Equation (8) gives `Phi(I_2)=I_4/2`, hence
`Tr_R P=Tr_R N=I_4/2`. The absolute eigenvalues in (7) give, for every
integer k>=0,

\[
\boxed{\operatorname{Tr}_R H^{2k}=(u^{2k}+3\ell^{2k})I_4,
\qquad \operatorname{Tr}_R H^{2k+1}=0.}
\tag{9}
\]

The even identity follows by separating P+N from its orthogonal
complement. The odd identity follows from reference-only chirality.
The same identities hold for the actual balanced example, whose
aggregate head marginal is also `I_4/2`. Thus every memory-valued
polynomial moment agrees, not merely the scalar spectrum or second
moment. In particular

\[
\operatorname{Tr}_R H^2=16I_4,\qquad
\operatorname{Tr}H^2=64,\qquad
\Phi(\operatorname{diag}(u^2,u^2))=6I_4\le8I_4.
\tag{10}
\]

For every pure head input, the output (8) has spectrum

\[
\{1/2,19/40,1/40,0\}.
\tag{11}
\]

To check this, rotate the input to `|0>` and apply the same unitary to
F and L. Thus its largest eigenvalue is 1/2 and the sum of its largest
two eigenvalues is 39/40. For every memory projector Pi of rank r,

\[
\|\widehat\Pi P\widehat\Pi\|
=\|V^\dagger\widehat\Pi V\|
\le\sup_{\|z\|=1}\sum_{j=1}^r
  \lambda_j\bigl(\Phi(|z\rangle\langle z|)\bigr).
\]

Since `H<=ell I+gP`, this bounds the largest eigenvalue of every
compression of H. Each compression remains chiral, because Gamma
commutes with every memory Pi; its spectrum is therefore symmetric.
Consequently the full operator norms satisfy, for every support,

\[
\boxed{\begin{aligned}
\operatorname{rank}\Pi=1:\quad
\|\widehat\Pi H\widehat\Pi\|
&\le\ell+g/2=4/\sqrt3<2\sqrt2,\\
\operatorname{rank}\Pi=2:\quad
\|\widehat\Pi H\widehat\Pi\|
&\le\ell+39g/40=59/(10\sqrt3)<2+\sqrt2.
\end{aligned}}
\tag{12}
\]

The second strict comparison reduces by positive squaring to
`1681<1200sqrt(2)`, certified by
`2*1200^2-1681^2=54239>0`. These are the full compression inequalities
(2), rather than only their head-channel consequences (3) and (4).

## 4. The actual-tail spectral envelope fails its last-query test

Take the allowed sharp last pair `B=I_F tensor X_L`,
`D=I_F tensor Z_L`, and set

\[
\Lambda=4+\sqrt2,\quad t=\Lambda-\ell>2,\quad
\alpha(t)=\frac{t^2-2}{t(t^2-4)}.
\]

The envelope of H is `ell I+gP`; its head weight is `Delta=gI_2`.
Using the coherent channel (8), the exact four-by-four test is

\[
\mathcal K_t=g\left[q(tI-X_3X_h-Z_3Z_h)^{-1}
+p\alpha(t)I_4\right].
\tag{13}
\]

Here the first branch preserves the logical-qubit resolvent and the
second takes its normalized logical partial trace. The largest
eigenvalue is attained on the Bell vector, giving

\[
\boxed{\|\mathcal K_t\|
=g\left[\frac{19}{20(t-2)}+
\frac{t^2-2}{20t(t^2-4)}\right]>1.}
\tag{14}
\]

The strict sign has an exact rational certificate. Write
`nu=t(t^2-4)(||K_t||-1)`. Expansion gives

\[
15\nu=1050\sqrt3+438\sqrt6-830\sqrt2-1716.
\]

The bounds `sqrt(3)>1732/1000`, `sqrt(6)>2449/1000`, and
`sqrt(2)<1415/1000` follow by integer squaring. They imply
`15nu>812/1000>0`. The test value is approximately 1.00191730556;
the proof of its strict sign uses no floating-point inference.

## 5. Compatibility with the original local Pauli operators is missing

For a physical leading isometry V, any head density matrix omega must
also satisfy

\[
\boxed{\operatorname{Tr}(\Sigma\omega)\le
\sum_{A\in\{X_1,Z_1,X_2,Z_2\}}
\left\|\operatorname{Tr}_R
 [(A\otimes I_Q)V\omega V^\dagger]\right\|_1.}
\tag{15}
\]

Indeed the left side equals `Tr(H_0 V omega V^dagger)`. Optimizing each
of the four independent memory contractions in (1) gives the
corresponding trace norm on the right. The partial traces are Hermitian
because A acts only on the traced reference system.

The specific isometry defining (8) cannot be an energy-u physical head. Take
`sigma=V(I_2/2)V^dagger=P/2`. Its four partial correlations are

\[
\begin{aligned}
C_{X_1}&=\sqrt{pq}\,W/2,&
C_{Z_1}&=(q-p)I_4/4,\\
C_{X_2}&=(qX_F\otimes I_L+pI_F\otimes X_L)/4,&
C_{Z_2}&=(qZ_F\otimes I_L+pI_F\otimes Z_L)/4.
\end{aligned}
\]

Their trace norms sum to

\[
2\sqrt{pq}+(q-p)+2q
=\frac{14}{5}+\frac{\sqrt{19}}{10}
<\frac{33}{10}<2\sqrt3=u.
\tag{16}
\]

The strict comparisons use `19<25` and `1089<1200`. Thus (15)
excludes this particular isometry with these head energies independently
of its completion outside the leading space. This statement concerns
the specified placement in the trusted reference space: it does not
exclude every alternative Stinespring realization of the same channel.

One can also see directly that the explicit H is outside (1): its
Pauli coefficient on `Z_1 Y_2 Y_F tensor I_L` is
`-19/(20sqrt(3))`, whereas (1) contains no word acting nontrivially on
both references. Under T the original such term contributes
`-q Z_1Y_2Y_F/sqrt(3)`; its p contribution has Y_L in place of Y_F,
and its mixed contribution has X_1 in place of Z_1. The other original
terms do not contribute to this coefficient.

The obstruction therefore identifies a limitation of spectral,
moment, and compression relaxations. It does not decide whether every
physical two-mode envelope passes (14)'s matrix counterpart, and it
does not show that this synthetic H plus its last pair exceeds Lambda.

## 6. Verification and scope

The accompanying [targeted checker](../../tools/check_two_mode_compatibility_obstruction.py)
verifies the exact field expansion and rational strict signs, then
reconstructs the single 16-dimensional operator, its channel, spectrum,
moments, resolvent, and local-Pauli obstruction. Matrix arithmetic is
used only to check the displayed construction identities. The proof
of the compression bounds for every support is the analytical argument
in Section 3; finitely many checks are not substituted for that proof.
The [recorded output](../../results/two_mode_compatibility_obstruction.json)
includes the verifier's source hash.

The core construction and its full compression proof received an
independent within-workspace reconstruction before integration. A
separate source audit checked the exact scalar arithmetic and matrix
identities, and an independent verifier rerun reproduced the recorded
JSON byte for byte. This is internal mathematical review, not external peer review or a claim
of publication originality. No operational assumption, encoder class,
memory convention, or LICENSE term is changed.
