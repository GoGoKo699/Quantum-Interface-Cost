# An actual two-mode channel can have a negative Choi partial transpose

**Research base:** main `8a88536b62a3e9ac2082b1108416af7958d87dda`.
**Date:** 26 September 2026.

The [two-mode resolvent reduction](TWO_MODE_RESOLVENT.md) retains the full
channel of the two leading eigenvectors. That channel cannot generally
be assumed entanglement breaking, even when both leading energies exceed
`2+sqrt(2)`. The following actual reflection construction gives an exact
negative partial transpose of its Choi matrix.

**Status:** supplied algebraic obstruction, independently reconstructed
within this workspace. It does not violate the three-query norm bound or
show that the two-mode spectral envelope fails its last-query test. No
publication-priority claim is made.

## 1. An allowed earlier Hamiltonian with two high modes

Order the tensor factors as R1,R2,A,B, with Q=A tensor B. Four-letter
Pauli words use this order. Put

\[
a=\sqrt{3/2},\qquad b=1/\sqrt2,\qquad
c=\cos(2\epsilon),\qquad s=\sin(2\epsilon),
\]

and consider, for c,s positive,

\[
H_0=a\,ZIZI+b\,XIXI+c\,IZIZ+s\,IZYY
       +c\,IXZX-s\,IXXI.
\tag{1}
\]

After a reference bisector rotation, the first site's original memory
reflections are
`B1=(a Z_A+b X_A)/sqrt(2)` and
`D1=(a Z_A-b X_A)/sqrt(2)`. Their squares are I because a²+b²=2.
The second memory pair is the simultaneous conjugation of the sharp
pair `Z_B,Z_A X_B` by `exp(i epsilon Y_A X_B)`. Its two operators are

\[
cZ_B+sY_AY_B,\qquad cZ_AX_B-sX_A.
\]

They remain anticommuting reflections and give the last four terms of
(1). Thus this is an allowed earlier Hamiltonian with one nonorthogonal
pair and one sharp pair, rather than freely specified spectral data.

Set

\[
U=\sqrt{7+4ac},\qquad L=\sqrt{7-4ac},\qquad d=U^2-1=6+4ac.
\]

Its spectrum, including multiplicities, is

\[
\{+U\ (\times2),+L\ (\times2),+1\ (\times4),
   -1\ (\times4),-L\ (\times2),-U\ (\times2)\}.
\tag{2}
\]

Here is a direct reduction proving (2). The Pauli P=ZZZZ commutes with
H0. On its k eigenspace, k=+1 or -1, the Hamiltonian is unitarily
equivalent to two identical copies of

\[
H_k=(a+kc)\tau_Z+b\sigma_X+c\sigma_Z
       +ks\tau_Y\sigma_Y-s\tau_X\sigma_X.
\]

Its square is

\[
H_k^2=(4+2akc)I
 +2b(a+kc)\tau_Z\sigma_X
 +2(ac+k)\tau_Z\sigma_Z-2bs\tau_X.
\]

The last three Pauli operators mutually anticommute. Their coefficient
length, after removing the displayed factor two, is `3/2+akc`.
The squared eigenvalues are therefore 1 and `7+4akc`. Reference
chirality preserves each k sector and gives both signs. In particular,
the two-dimensional top projector is exactly

\[
P_+=\frac{(I+ZZZZ)(H_0^2-I)(I+H_0/U)}{4d}.
\tag{3}
\]

## 2. The complete channel and its Choi spectrum

The physical Paulis

\[
L_X=IXIX,\qquad L_Z=XIXZ,\qquad L_Y=XXXY
\]

commute with H0 and restrict to logical Pauli matrices on its top space.
Choose its isometry V accordingly. For the head-to-memory channel
`Phi(omega)=Tr_(R1 R2)(V omega V^dagger)`, expanding (3) gives

\[
\begin{aligned}
\Phi(I)&=I/2,\\
\Phi(X)&=\alpha ZI+\beta XX,\\
\Phi(Y)&=\eta XY,\\
\Phi(Z)&=\gamma IZ+\delta YY,
\end{aligned}
\qquad
\begin{aligned}
\alpha&=\frac{2a+8c+4ac^2}{Ud},&\beta&=-\frac{s}{U},\\
\eta&=-\frac{2bs}{d},&\gamma&=\frac{8b+6abc}{Ud},\\
\delta&=\frac{2abs}{Ud}.&&
\end{aligned}
\tag{4}
\]

Use the normalized Choi matrix, with trace one. Its partial transpose
on the head is

\[
J_\Phi^{T_h}=
\frac14\left[I\otimes\Phi(I)+X\otimes\Phi(X)
              +Y\otimes\Phi(Y)+Z\otimes\Phi(Z)\right].
\tag{5}
\]

On the three tensor factors head,A,B, the Pauli C=YXY commutes with
(5). In its q eigenspace,
`ZYY=-q XZI` and `ZIZ=-q XXX`. The remaining two Pauli operators
XZI and XXX anticommute, so the two eigenvalues in that sector are

\[
\frac18+\frac{q\eta}{4}
\ \mathord\pm\ \frac14
\sqrt{(\alpha-q\delta)^2+(\beta-q\gamma)^2},
\]

each with multiplicity two. Substitution in (4) gives the exact identities

\[
\alpha^2+\beta^2+\gamma^2+\delta^2=\frac14+\eta^2,
\qquad 2(\alpha\delta+\beta\gamma)=\eta.
\tag{6}
\]

For example, after multiplication by U²d², the first identity reduces
on both sides to `77+100c²+128ac+16ac³`; the second follows from
`a²=3/2`, `b²=1/2`, and `c²+s²=1`. Thus the square root above is
`1/2-q eta`, which is positive since d>=6 and `|eta|<1/2`. Therefore

\[
\boxed{\operatorname{spec}(J_\Phi^{T_h})
 =\{\tfrac14\ (\times4),+bs/d\ (\times2),-bs/d\ (\times2)\}.}
\tag{7}
\]

Every positive s in this construction gives a negative eigenvalue.
An entanglement-breaking channel has a separable Choi matrix, whose
partial transpose is positive. Equation (7) therefore rules out that
property for this actual top-space channel.

## 3. One exact point above the rank-one threshold

Take the rational angle data

\[
c=\frac{39999}{40001},\qquad s=\frac{400}{40001}.
\]

Then

\[
U=m=\sqrt{7+2\sqrt6\frac{39999}{40001}}
 >\frac{86}{25}>2+\sqrt2,
\tag{8}
\]

while

\[
\lambda_{\min}(J_\Phi^{T_h})
 =-\frac{100\sqrt2}{120003+39999\sqrt6}<0.
\tag{9}
\]

For (8), use `c>999/1000` and `sqrt(6)>61/25`, then square;
also `(36/25)²>2`. Numerically, m is approximately 3.449454238 and
the negative eigenvalue is approximately -0.0006487809215. The energy
and partial-transpose gaps are strict. Since the top two-dimensional
space is separated from the remaining spectrum, continuity also gives
nearby actual readouts with both properties.

The [targeted checker](../../tools/check_two_mode_resolvent.py)
reconstructs this one exact construction alongside the separate two-mode
reduction checks. The proof is (2)--(9), not a search over perturbations.

This obstruction excludes a general entanglement-breaking or
positive-partial-transpose shortcut. It leaves open the actual matrix
inequality in the two-mode resolvent report, all three remaining full
reflection signatures, and the unrestricted retention conjecture.
