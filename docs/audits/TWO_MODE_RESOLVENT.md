# Two leading modes give a uniformly regular last-query test

**Research base:** main `8a88536b62a3e9ac2082b1108416af7958d87dda`.
**Date:** 26 September 2026.

For two arbitrary earlier query pairs on a four-dimensional memory, the
third Hamiltonian eigenvalue is always below `2+sqrt(2)`. Retaining the two
leading eigenvectors therefore leaves a uniformly invertible last-query
resolvent. The resulting exact test for the spectral envelope is a four
by four matrix inequality. It retains the coherences between the two
leading modes through a unital completely positive map.

No internal anticommutation, common memory factorization, equal Jordan
angles, or real-matrix hypothesis is imposed. The earlier four readouts
may themselves be arbitrary Hermitian contractions.

**Status:** supplied structural reduction. The final four-by-four
inequality has not been proved uniformly over its actual head channels
and the third readout pair. This report does not close a remaining full
reflection signature or the unrestricted retention conjecture. A failed
test would refute this particular spectral envelope, not automatically
the original operator bound. Publication priority is unresolved.

## 1. A universal bound on the third eigenvalue

Let R1,R2 be reference qubits, let Q have dimension four, and put

\[
H_0=X_1\otimes B_1+Z_1\otimes D_1
    +X_2\otimes B_2+Z_2\otimes D_2,
\qquad -I\le B_i,D_i\le I.
\tag{1}
\]

Write its three largest eigenvalues, with multiplicity, as U,m,ell.
The involution `Gamma=Y_1 Y_2 tensor I_Q` anticommutes with H_0. Its two
eigenspaces have dimension eight, so

\[
H_0=\begin{pmatrix}0&C\\C^\dagger&0\end{pmatrix},
\qquad \operatorname{spec}(H_0)=\{\pm\sigma_j(C):1\le j\le8\}.
\]

The four reference Pauli factors in (1) are trace-orthogonal. Hence

\[
\operatorname{Tr}H_0^2
=4\operatorname{Tr}_Q(B_1^2+D_1^2+B_2^2+D_2^2)
\le64.
\tag{2}
\]

There is equality in (2) when the four readouts are reflections.
Chirality then gives

\[
\sum_{j=1}^8\sigma_j(C)^2\le32,
\qquad
\boxed{0\le\ell=\sigma_3(C)\le\kappa:=\sqrt{32/3}<2+\sqrt2.}
\tag{3}
\]

For the last strict inequality, squaring reduces to `6sqrt(2)>7`,
which follows from `72>49`. Put

\[
\Lambda=4+\sqrt2,\qquad t=\Lambda-\ell.
\]

Then, uniformly over all earlier readouts,

\[
\boxed{t-2\ge2+\sqrt2-\sqrt{32/3}>0.}
\tag{4}
\]

The lower gap is approximately 0.148227239. This is a moment argument,
not a bound inferred from a sampled family of Jordan angles.

## 2. The positive head has dimension at most two

Choose orthonormal eigenvectors Omega_1,Omega_2 for U,m. Define the
isometry V from a two-dimensional auxiliary head space to R1 R2 Q by
`V e_a=Omega_a`, and set

\[
\Delta=\operatorname{diag}(U-\ell,m-\ell)\ge0.
\]

Spectral ordering gives

\[
\boxed{H_0\le\ell I+V\Delta V^\dagger.}
\tag{5}
\]

If m=ell, the second weight vanishes. Degenerate leading eigenvalues
cause no ambiguity in the envelope: choose any orthonormal basis of the
selected eigenspace. The actual value ell in (5) keeps both weights
nonnegative and uses the full available gap (4).

This extends the preceding
[rank-one resolvent method](EXACT_LAST_QUERY_RESOLVENT.md), Section 6.
There, the inverse was uniformly positive only when the second
eigenvalue was below `Lambda-2`. Equation (3) gives that condition for
the third eigenvalue without any restriction on the earlier pairs.

The uniform constant kappa establishes invertibility; replacing the
actual tail by that constant can make the envelope too loose. For
example, take the two independent Bell Hamiltonians, with U=4 and
m=ell=2. Their top vector is the product of the two Bell vectors. Raising
the baseline to beta and using the positive part of the head gives
`beta I+(4-beta)|Omega><Omega|` when `2<beta<4`. In the regular range
`2<beta<2+sqrt(2)`, the allowed third pair `B=X_A,D=Z_A` has test value

\[
(4-\beta)\frac{t^2-2}{t(t^2-4)},\qquad t=\Lambda-\beta.
\]

At beta=13/4 this exceeds one: the positive denominator times
`1-test_value` is
`sqrt(2)(12sqrt(2)-23)/16<0`. Increasing beta increases the envelope,
and `kappa>13/4` follows from `512>507`. Thus the fixed-kappa envelope
also fails, although the actual three-query norm is `2+2sqrt(2)<Lambda`.
The bound (5) avoids this loss. This warning concerns that fixed
baseline choice; it does not rule out tighter adaptive alternatives.

## 3. Preserve the two-mode memory channel

For a memory operator A define

\[
\mathcal E(A)=V^\dagger(I_{R_1R_2}\otimes A)V.
\tag{6}
\]

This is a unital completely positive map from four-by-four memory
matrices to two-by-two head matrices. In a reference basis r, put
`K_r=(<r| tensor I_Q)V`. Then

\[
\mathcal E(A)=\sum_{r=1}^4K_r^\dagger A K_r,
\qquad \sum_rK_r^\dagger K_r=I_2.
\]

Thus its Kraus rank is at most four. Define the cross marginals

\[
\rho_{ab}=\operatorname{Tr}_{R_1R_2}
|\Omega_a\rangle\langle\Omega_b|.
\]

The entries are

\[
\mathcal E(A)_{ab}=\operatorname{Tr}(\rho_{ba}A).
\tag{7}
\]

The block matrix `[rho_ab]` is positive and its partial trace over Q is
`I_2`. It is the unnormalized Choi matrix of the trace-preserving dual
map. The diagonal blocks alone generally do not specify the test below.
No dephasing of the head, entanglement-breaking assumption, or reduction
to two unrelated scalar marginals is made.

For convenience also set

\[
\mathcal E_\Delta(A)=\sqrt\Delta\,\mathcal E(A)\sqrt\Delta,
\qquad \mathcal E_\Delta(I_Q)=\Delta.
\]

The weighted map is completely positive but need not be unital.

### 3.1. A necessary matrix moment of the actual channel

Let Phi denote the trace-preserving dual of E, so
`Phi(A)=Tr_R(V A V^dagger)`. Actual head channels satisfy

\[
\boxed{\Phi(\operatorname{diag}(U^2,m^2))\le8I_Q.}
\tag{7a}
\]

Indeed, partial tracing (1) squared gives
`Tr_R H_0^2=4(B_1^2+D_1^2+B_2^2+D_2^2)<=16I_Q`. Each positive
head eigenvector has an orthogonal negative partner Gamma Omega_a with
the same memory marginal. Spectral positivity of H_0 squared therefore
gives `2(U^2 rho_11+m^2 rho_22)<=16I_Q`. Zero eigenvalues contribute
zero and cause no exception. This is a necessary matrix condition on
the actual channel, not a characterization of all channels that arise
from (1).

## 4. Exact four-by-four Schur condition

Let R3 be the final reference qubit, and let B,D be arbitrary Hermitian
contractions on Q. Write

\[
h=X_3\otimes B+Z_3\otimes D,\qquad
R_t(B,D)=(tI-h)^{-1}.
\]

The triangle inequality gives `||h||<=2`, so (4) makes the inverse
strictly positive for every allowed last pair. With tensor factors
ordered as R3 followed by the head, define

\[
\boxed{\mathcal K_t(B,D)
=(\operatorname{id}_{R_3}\otimes\mathcal E_\Delta)
       [R_t(B,D)]\in M_4.}
\tag{8}
\]

Then the spectral envelope satisfies the exact equivalence

\[
\boxed{\ell I+V\Delta V^\dagger+h\le\Lambda I
\quad\Longleftrightarrow\quad
\mathcal K_t(B,D)\le I_4.}
\tag{9}
\]

Spectator identities and the natural tensor reordering are implicit on
the left. To prove (9), let J insert `I_{R_3} tensor V` into R1 R2 R3 Q
and let `W=J(I_{R_3} tensor sqrt(Delta))`. The left side is equivalent to

\[
P-WW^\dagger\ge0,
\qquad P=I_{R_1R_2}\otimes(tI-h)>0.
\]

Conjugating by `P^{-1/2}` and using the equality of the nonzero
eigenvalues of `AA^dagger` and `A^dagger A` gives

\[
P-WW^\dagger\ge0
\quad\Longleftrightarrow\quad W^\dagger P^{-1}W\le I_4.
\]

The last matrix is precisely (8). In the R3 basis, its two-by-two
blocks are `E_Delta((R_t)_{st})`. Equivalently, its head indices retain
the factors `sqrt(Delta_aa Delta_bb)` multiplying the cross-marginal
traces (7).

If (8) is at most I for every last pair, (5) proves the desired upper
bound for the original three-query Hamiltonian. Conjugating all three
references by Y reverses that Hamiltonian, so the same upper bound
also proves its operator-norm bound. The converse implication applies
to the envelope in (9), not necessarily to the original H_0+h.

### 4.1. The last pair still reduces exactly to reflections

For fixed V,Delta,t, the positive inverse is operator convex in h.
Consequently (8) is operator convex separately in B and D. The extreme
points of the Hermitian contraction ball are reflections. Decomposing
each contraction into such extremes proves that

\[
\sup_{-I\le B,D\le I}\lambda_{\max}\mathcal K_t(B,D)
=\sup_{B^2=D^2=I}\lambda_{\max}\mathcal K_t(B,D).
\tag{10}
\]

This does not force the two last reflections to anticommute. Their
arbitrary one- and two-dimensional Jordan blocks remain allowed.

For an explicit block form when B,D are reflections, put
`T=B+iD`. In a suitably phased Y3 eigenbasis, h has blocks
`[[0,T],[T^dagger,0]]`. Therefore

\[
R_t(B,D)=
\begin{pmatrix}
t(t^2-TT^\dagger)^{-1}&T(t^2-T^\dagger T)^{-1}\\
T^\dagger(t^2-TT^\dagger)^{-1}&t(t^2-T^\dagger T)^{-1}
\end{pmatrix}.
\tag{11}
\]

Applying E_Delta entrywise gives an explicit four-by-four test. Here
`TT^dagger=2I-i[B,D]` and `T^dagger T=2I+i[B,D]`; all inverses exist by
(4). The channel acts on the full memory matrices in (11), including
its off-diagonal blocks. Equation (11) is not a scalar eigenvalue-pairing
formula like the rank-one theorem.

## 5. Why one leading mode does not suffice uniformly

The following exact example has two leading eigenvalues above
`Lambda-2`. Its two-mode envelope nevertheless passes (9) for every
third pair, and its channel gives an explicit reason to retain the cross
marginals.

### 5.1. An actual balanced example needs both leading modes

Let Q=A tensor B. After independent rotations of the two reference X/Z
frames, consider

\[
H_0=aZ_1Z_A+bX_1X_A+cZ_2Z_B+dX_2Z_AX_B,
\quad a^2+b^2=c^2+d^2=2.
\tag{12}
\]

This is an allowed original-query Hamiltonian: before those reference
rotations its memory pairs are

\[
\begin{aligned}
B_1&=(aZ_A+bX_A)/\sqrt2,&D_1&=(aZ_A-bX_A)/\sqrt2,\\
B_2&=(cZ_B+dZ_AX_B)/\sqrt2,&D_2&=(cZ_B-dZ_AX_B)/\sqrt2.
\end{aligned}
\]

Each is a traceless reflection because its two Pauli summands
anticommute. Thus each memory reflection has two positive and two
negative eigenvalues. Put

\[
a=c=2/\sqrt3,\qquad b=d=\sqrt{2/3}.
\]

The operators `Z_1 Z_A` and `Z_2 Z_B` commute with each other and with
`X_1 X_A` and `X_2 Z_A X_B`; the latter two anticommute. Each joint
eigenspace of the first two has dimension four. On it the last two
terms have eigenvalues `+-sqrt(b^2+d^2)`, each twice. The full spectrum
is therefore

| Eigenvalue | Multiplicity |
|---|---:|
| `2sqrt(3)` | 2 |
| `2/sqrt(3)` | 6 |
| `-2/sqrt(3)` | 6 |
| `-2sqrt(3)` | 2 |

In particular

\[
U=m=2\sqrt3>2+\sqrt2,\qquad \ell=2/\sqrt3.
\tag{13}
\]

Any positive rank-at-most-one majorant `H_0<=b_0 I+A` requires
`b_0>=m`: the two-dimensional top eigenspace contains a nonzero vector
annihilated by A. It therefore cannot put the baseline strictly below
`Lambda-2`. Some allowed third pairs have eigenvalue two, so the
inverse required by that uniform rank-one method need not be positive.
This is a limitation of the method, not a physical violation of Lambda.

The two-mode envelope instead has

\[
H_0\le\ell I+gVV^\dagger,
\qquad \ell=2/\sqrt3,\quad g=4/\sqrt3,
\quad \Delta=gI_2.
\tag{14}
\]

### 5.2. The full head channel is explicit

Define the copying isometry J0 by
`J0|ab>=|ab>_(R1 R2)|ab>_Q`. The two positive commuting constraints
in (12) select its range. On that range the top projector becomes

\[
P_S=\frac12\left[I+\frac{X_A+Z_AX_B}{\sqrt2}\right].
\]

An isometry onto this two-dimensional space is

\[
V_S=\exp(i\pi Y_AX_B/8)(|+\rangle_A\otimes I_B),
\qquad V=J0 V_S.
\]

Tracing out the references dephases the copying basis. The complete
head-to-memory channel is consequently

\[
\Phi(\omega)=\sum_{a,b=0}^1
\operatorname{Tr}(E_{ab}\omega)|ab\rangle\langle ab|,
\qquad
E_{ab}=\frac14\left[I+
\frac{(-1)^aX_h+(-1)^bZ_h}{\sqrt2}\right].
\tag{15}
\]

For example, the A=a row of V_S is
`[cos(pi/8)I+(-1)^a sin(pi/8)X]/sqrt(2)`. Sandwiching `|b><b|`
between this row and its adjoint gives (15). These four effects have
rank one, trace 1/2, and sum I. They do not commute.

In the head Y basis, both diagonal memory marginals are exactly I_Q/4.
Nevertheless Phi is not constant: head X and Z eigenstates produce
nonuniform memory distributions. Identical flat diagonal marginals
therefore do not justify deleting the cross terms in (7).

To see a strict change for the same last pair, choose `B=Z_A,D=Z_B`.
Then `h^2=2I` and E obeys `E(Z_A)=X_h/sqrt(2)` and
`E(Z_B)=Z_h/sqrt(2)`. With `t=4+sqrt(2)-2/sqrt(3)`, (8) is exactly

\[
\mathcal K_t=
\frac{g}{t^2-2}\left[tI+
\frac{X_3X_h+Z_3Z_h}{\sqrt2}\right],
\qquad
\|\mathcal K_t\|=\frac{g}{t-\sqrt2}.
\tag{16}
\]

Dephasing the head in its Y basis removes both correlations and gives
the strictly smaller norm `gt/(t^2-2)`. This comparison fixes the same
third pair; it does not compare two independently reoptimized decoder
problems. The change has no definite operator sign and cannot be
silently substituted into the sufficient upper-bound test.

### 5.3. The envelope passes every third pair in this example

Here `t>3sqrt(2)`. Indeed `2-sqrt(2)>1/sqrt(3)` follows, by positive
squaring, from `17>12sqrt(2)`, and the latter follows from `289>288`.
For any `t>=3sqrt(2)`, the exact last-query theorem gives the pure-memory
resolvent bound `1/(t-sqrt(2))`. It can also be checked directly on its
block functions: for `1<=a<=sqrt(2)`,

\[
\frac{t-a}{(t-a)^2-(2-a^2)}\le\frac1{t-\sqrt2}
\]

is equivalent to
`(sqrt(2)-a)[t-sqrt(2)-2a]>=0`. The other block eigenvalue is no larger,
and scalar blocks obey the same bound. Reflection reduction includes
arbitrary last Hermitian contractions.

Thus every pure memory compression
`<ab|R_t(B,D)|ab>` is at most `I/(t-sqrt(2))`. The positive effects
E_ab in (15) sum to I, so their complete head compression obeys

\[
\boxed{\sup_{B,D}\|\mathcal K_t(B,D)\|
=\frac{g}{t-\sqrt2}
=\frac{2}{2\sqrt3-1}<1.}
\tag{17}
\]

The last pair in (16) attains the bound. Therefore this actual example
needs two modes for the uniformly positive inverse, and its two-mode
envelope succeeds for every third binary pair. Together with (3), it
establishes the minimal worst-case head dimension for this strategy.

The explicit channel (15) is entanglement breaking because it measures
a POVM and prepares orthogonal memory states. No such property is
available in general: the companion
[nonclassical head-channel example](NONCLASSICAL_TWO_MODE_CHANNEL.md)
has two leading eigenvalues above `2+sqrt(2)` and an exactly negative
partial-transpose eigenvalue of its Choi state. That actual head channel
is not entanglement breaking.

## 6. Verification and the remaining global question

The [targeted checker](../../tools/check_two_mode_resolvent.py) and
[recorded result](../../results/two_mode_resolvent.json) verify the
moment identity, chiral pairing, the head compression, the four-by-four
Schur equivalence, and the reflection resolvent block formula on small
deterministic constructions. They also reconstruct (12)--(17), including
the full head channel and the strict change after dephasing. These
matrix identities supplement the supplied proofs; they do not establish
the missing uniform bound by sampling.

The run contains 28 earlier-pair constructions, 112 full-versus-head
inertia comparisons, 14 reflection resolvent block checks, and eight
operator-convexity checks. The matrices have dimension at most 32.
The largest reported identity residual is below `1.43e-14`; the channel
moment's smallest eigenvalue is no less than `-2.05e-14` from rounding,
against tolerance `4e-10`. The two exact auxiliary examples also check
the fixed-baseline failure and the stated nonclassical Choi spectrum.

The proof received an independent internal reconstruction, and a separate
rerun reproduced the recorded diagnostic byte for byte. The exact fixed
baseline warning and nonclassical channel example were also independently
checked. These are within-workspace checks, not external peer review or
publication-priority certification.

The remaining question is now concrete: do the actual channels (6),
their weights Delta, and their actual lower-spectrum level ell always
satisfy (8) for every third reflection pair? A generic unital completely
positive map is not asserted to satisfy the needed bound. The relation
between the earlier Pauli readouts and their two-dimensional top space
must be retained.

The model remains one arbitrary unknown specimen, one delayed local
X/Z query, unrestricted collective encoding, free finite classical
records, and worst-case retained quantum dimension. The head space is
a proof device, not an additional retained system. No specimen copying,
free entanglement, physical reaccess, sequential queries, postselection,
or average-memory substitution is introduced.
