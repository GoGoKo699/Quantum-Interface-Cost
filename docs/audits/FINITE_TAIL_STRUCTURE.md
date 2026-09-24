# Finite-tail structure: completion, concavity and a sharp product envelope

Reviewed main: `3964f9b97766463a2aff65233560c9dcdf60c297` (PR #26).
Reviewed tree: `0bdb23c6045674fc4d0c2b18d5119e095d531196`.
Date: 2026-09-24. This continues the
[coherent-transfer audit](COHERENT_TRANSFER_AUDIT.md).

**Proved:** the decoder cross block has an exact contraction-completion
description; the square of the fixed-core, fixed-tail four-query sum is
concave in the squared tail parameter; and product supports have a sharp
finite-tail envelope. These give finite tangent bounds even when query
compressions are singular. They do not prove the unrestricted transfer
inequality, add an entropy exclusion, or establish publication originality.

The operational problem retains one unknown specimen, one delayed local
X/Z query, unrestricted collective encoding, unlimited finite classical
records, worst-case quantum dimension and uniform error on every input
and query. All subspaces, blocks and decoders below are proof coordinates.
They impose no operational projection, postselection or encoder restriction.

## 1. Setting and evidence labels

Let P,Q be orthogonal rank-two supports on two qubits, with normalized
states sigma on P and tau on Q. The tail may have rank one. For each
`U in {X_A,Z_A,X_B,Z_B}`, put

    L_U=sqrt(sigma) PUP sqrt(sigma),
    X_U=sqrt(sigma) PUQ sqrt(tau),
    M_U(s)=[[L_U,sqrt(s)X_U/2],[sqrt(s)X_U^dagger/2,0]],
    S(s)=sum_U ||M_U(s)||_1 = mathcal S_{sqrt(s)}(sigma,tau).

If `spec(sigma)=(1-m,m)`, the established rank-two envelope is
`G(m)=sqrt(2)+sqrt[4-2(1-2m)^2]`. The open target is

    S(s)<=G(m)+(3/8)[1-sqrt(1-4s)],
    0<=s<=1/7, 1/5<=m<=1/2.                                  (1)

| Statement | Status |
|---|---|
| Contraction completion and ordinary concavity | Established dilation/fidelity ingredients; elementary proofs supplied |
| Squared concavity for 2 by 2 blocks and their sum | Derived with proof; independently reconstructed within this workspace |
| Positive-parameter tangent and product-support envelope | Supplied deductions; independently checked |
| Arbitrary-support inequality (1) | Unproved |
| Publication originality | Not established; no priority claim is made |

## 2. Exact completion keeps the decoder defect

For a Hermitian A and rectangular B, there exists Hermitian C such that
`D=[[A,B],[B^dagger,C]]` is a contraction **if and only if**

    A^2+BB^dagger<=I.                                         (2)

Necessity is the core compression of `D^2<=I`. For sufficiency, (2)
gives `B=sqrt(I-A^2)K` with `||K||<=1`: use the inverse on the support
of `sqrt(I-A^2)` and zero on its kernel. The inequality ensures both
the range inclusion and the contraction bound. The Hermitian unitary

    J=[[A,sqrt(I-A^2)],[sqrt(I-A^2),-A]]

compressed by `diag(I,K)` gives the required D with
`C=-K^dagger A K`. This argument includes singular defects.

Trace-norm duality and optimization over K therefore give exactly

\[
\left\|\begin{pmatrix}L&tX/2\\tX^\dagger/2&0\end{pmatrix}\right\|_1
=\max_{-I\le A\le I}
\left\{\operatorname{Tr}(LA)+t\|X^\dagger\sqrt{I-A^2}\|_1\right\},
\quad t\ge0.                                                  \tag{3}
\]

Thus `I-A^2` is exactly the available cross-block budget. A compressed
decoder need not be a scalar or traceless reflection; applying the
rank-two extreme-decoder classification directly to A would be invalid.

## 3. Ordinary concavity in every block dimension

Fix `M=[[L,X/2],[X^dagger/2,0]]` and `P_s=diag(I,sI)`. With root
fidelity for positive, possibly unnormalized operators,

    ||P_s^(1/2) M P_s^(1/2)||_1 = F(P_s,M P_s M).               (4)

The second argument is positive despite M being indefinite. The identity
holds because the matrix under the fidelity square root is
`(P_s^(1/2) M P_s^(1/2))^2`.

For completeness, `F(A,B)=inf_{Z>0}[Tr(AZ)+Tr(BZ^-1)]/2`.
For A>0, set `Y=A^(1/2)ZA^(1/2)` and `C=A^(1/2)BA^(1/2)`.
The objective minus `Tr sqrt(C)` is

    (1/2)||Y^(1/2)-Y^(-1/2)sqrt(C)||_HS^2>=0.

Choose `Y=sqrt(C)`, or a positive regularization if C is singular,
to obtain the infimum. The general semidefinite extension is also proved
in the [classical-flag note](../CLASSICAL_FLAG_ENTROPY_BOUND.md).
For s>0, (4) consequently equals

    inf_{Z>0} (1/2)Tr[P_s(Z+M Z^-1 M)].                        (5)

This is an infimum of affine functions of s, hence concave. Continuity
includes s=0. Formula (3) also shows monotonicity. Therefore S(s) itself
is increasing and concave, in arbitrary block dimensions.

## 4. Stronger squared concavity for two-dimensional blocks

**Theorem.** If A is Hermitian 2 by 2 and B is complex 2 by 2, then

    f(s)=||[[A,sqrt(s)B],[sqrt(s)B^dagger,0]]||_1

has concave square on `s>=0`. Neither A nor B must be invertible.

First take B invertible and s>0. Put `C=BB^dagger` and

    a=Tr A, b=det A, c=Tr C, d=Tr(adj(A)C), e=det C>0.

The characteristic polynomial is

    lambda^4-a lambda^3+(b-sc)lambda^2+sd lambda+s^2 e.          (6)

The block matrix has two positive and two negative eigenvalues. Indeed
its determinant is nonzero, and scaling A continuously to zero preserves
inertia. Let P_+,P_- be the sums of its positive eigenvalues and absolute
negative eigenvalues, and u,v the products within those respective pairs.
Vieta's formulas give

    f=P_++P_-, a=P_+-P_-, y=P_+P_-=(f^2-a^2)/4>0,
    u+v=y+b-sc, uP_--vP_+=sd, uv=s^2e.

Writing `w=u+v`, the identity
`f(u-v)=2sd+aw` gives

    y w^2-asd w-s^2(d^2+ea^2+4ey)=0.

Take its positive root and substitute `w=y+b-sc` to obtain

    y+b=s k(y),
    k(y)=c+[ad+sqrt((a^2+4y)(d^2+4ey))]/(2y).                 (7)

The arithmetic-geometric mean variational identity rewrites this as

    k(y)=inf_{z>0}(C_z+D_z/y),
    C_z=c+z+e/z>0, D_z=(a sqrt(z)+d/sqrt(z))^2/4>=0.

The infimum is attained at
`z=sqrt[(d^2+4ey)/(a^2+4y)]`. Thus

\[
y(s)=\inf_{z>0}R_z(s),\qquad
R_z(s)=\frac{sC_z-b+\sqrt{(b-sC_z)^2+4sD_z}}2.                 \tag{8}
\]

To check the direction, (7) gives
`y^2+(b-sC_z)y-sD_z<=0` for every z, so positive y is at most the
nonnegative quadratic root R_z. Equality holds at the minimizing z.

For positive s the radical in (8) is nonzero, and

    R_z''(s)=2D_z(bC_z-D_z)/[(b-sC_z)^2+4sD_z]^(3/2).         (9)

We have `D_z>=bC_z`. For b<=0 this is immediate. For b>0 diagonalize
`A=diag(alpha,beta)` and write `C=[[r,h],[h^dagger,w]]`. Expansion gives

    D_z-bC_z
      =[(alpha-beta)sqrt(z)+(alpha w-beta r)/sqrt(z)]^2/4
        +b|h|^2/z >=0.                                      (10)

These same inequalities exclude a zero radical at s>0: that would require
`D_z=0` and `b=sC_z>0`, contradicting `D_z>=bC_z`. Hence each R_z is
concave on the positive half-line. An infimum of concave functions is
concave, so (8) proves concavity of y and therefore of `f^2=a^2+4y`.
Continuity includes s=0, where derivatives need not be finite, and
singular B by approximation with invertible matrices.

Finally, this property is preserved under finite sums of these norms:

    (sum_i f_i)^2=sum_i f_i^2+2 sum_{i<j}sqrt(f_i^2 f_j^2).

The geometric mean is jointly concave and coordinatewise nondecreasing.
Applying the theorem with `A=L_U,B=X_U/2` proves that **S(s)^2 is
concave for each fixed complex core and tail**.

## 5. A finite tangent at every positive tail parameter

Fix s0>0, let `D_U=sign(M_U(s0))`, taking zero on the kernel, and let
A_U be its core block. Put `S0=S(s0)` and `a0=sum_U Tr(L_U A_U)`.
For s>0 the rank is constant under the invertible congruence in (4).
Thus the trace norm is differentiable along this curve even with a
persistent kernel. Direct differentiation gives

    S'(s0)=(S0-a0)/(2s0).

The squared-concavity tangent is consequently

\[
S(s)^2\le S_0^2+
\frac{S_0(S_0-a_0)}{s_0}(s-s_0),\qquad s\ge0.                 \tag{11}
\]

All quantities are finite; no singular core compression is inverted.
This is a state-specific bound. A supremum over core/tail states need not
preserve concavity. Also, the target in (1) is convex in s, so checking
only interval endpoints would not establish (1).

For an exact endpoint obstruction, take `P=(I+Y tensor Y)/2`,
`sigma=P/2,tau=(I-P)/2`. All four query compressions L_U vanish and
`S(s)=4sqrt(s)`. Its ordinary derivative is infinite at zero although
`S(s)^2=16s`. A proof must retain the available deficit `G(m)-g(sigma)`.

## 6. Sharp product-support envelope

Suppose `P=I_A tensor |b><b|`, with
`sigma=omega tensor |b><b|` and `tau=nu tensor |b_perp><b_perp|`.
The normalized omega,nu may be complex, singular and noncommuting. Then

    mathcal S_t<=g_1(omega)+sqrt(2+2t^2), 0<=t<=1.             (12)

The A-query cross blocks vanish, contributing exactly `g_1(omega)`.
For a B query put `a=<b|U|b>` and `z=<b|U|b_perp>`; then
`a^2+|z|^2=1`. Its matrix has blocks
`[[a omega,t z sqrt(omega)sqrt(nu)/2],[h.c.,0]]`.
For a Hermitian contraction decoder with core H and cross K, set
`x=Tr(omega H)` and `y=Tr(sqrt(omega)sqrt(nu)K^dagger)`.
Hilbert--Schmidt Cauchy--Schwarz and (2) give

    |y|^2<=Tr(omega K K^dagger)
          <=1-Tr(omega H^2)<=1-x^2.

Its expectation is at most
`a x+t|z|sqrt(1-x^2)<=sqrt[a^2+t^2(1-a^2)]`.
For the X/Z pair, `a_X^2+a_Z^2<=1`; Cauchy--Schwarz and t<=1 give
the spectator contribution `sqrt(2+2t^2)`. Taking nu=omega makes
each block a scalar 2 by 2 matrix tensored with omega. A bisector flag
axis then attains (12), for every omega.

At fixed core spectrum `(1-m,m)`, optimize omega's Bloch direction to
obtain the sharp envelope

    mathcal S_t<=G(m)+sqrt(2)[sqrt(1+t^2)-1].                  (13)

A bisector Bloch direction attains the qubit score; at m=1/2 its direction
is irrelevant. For `s=t^2<=1/7`, the increment in (13) is at most
`s/sqrt(2)<=3s/4<=(3/8)[1-sqrt(1-4s)]`, proving (1) on these supports.
Their associated full states are already covered by the
[classical-flag entropy theorem](../CLASSICAL_FLAG_ENTROPY_BOUND.md),
including noncommuting omega,nu. This is no additional entropy exclusion.

## 7. Verification and the remaining question

The completion, characteristic polynomial, Vieta reduction, scalar root
ordering, concavity identity, tangent and product attainers were separately
reconstructed within this workspace. This is internal checking, not external
peer review. The exact algebra checker
[`tools/check_finite_tail_structure.py`](../../tools/check_finite_tail_structure.py)
checks the polynomial identities; it does not establish the arbitrary-
support envelope. The analytical proofs above carry the continuum claims.

The separate [Bayes--rank comparison](BAYES_RANK_PRIOR_COMPARISON.md)
audits related operational prior work; it does not certify originality
of the matrix lemmas in this report.

The remaining task is to bound the shared four-query geometry uniformly
over sigma,tau. Neither these lemmas nor passing algebra checks close (1),
the all-block-size entropy conjecture, unrestricted equal-accuracy
optimality, or publication originality.
