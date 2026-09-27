# A physical reflection counterexample to both one-mode spectral envelopes

Research base: main `556df48950c2de3162171dd1d85c3df9e5937fc2` (PR #48).
Date: 27 September 2026.
Status: supplied analytical construction and proof, independently reconstructed
within this workspace. This is internal mathematical review, not external
peer review or a claim of publication priority.

There are four actual earlier reflection readouts and two explicit third-pair
variants, each with just one noncommuting Jordan block, for which both the
ordinary one-mode envelope and the envelope retaining its negative partner
fail at Lambda=4+sqrt(2). Nevertheless the actual H0 obeys the strict bound
||H0+h3||<21/4<Lambda for **every** third pair of Hermitian contractions.
Thus neither envelope is a uniform target in either remaining one-block
sector, `(22)^2(11)` or `(22)^2(12)`.
This strengthens the distinction between a positive inverse and a passing
[rank-one spectral certificate](EXACT_LAST_QUERY_RESOLVENT.md#6-exact-test-for-a-rank-one-spectral-upper-bound).
The [high-second-mode one-block theorem](HIGH_SECOND_MODE_ONE_BLOCK.md) remains
valid: the present failure occurs below its threshold, where the inverse
exists but the spectral envelope loses too much information.

## 1. The earlier reflection family

Use reference bisector coordinates, and put

```math
a=2/\sqrt3,\qquad b=\sqrt{2/3},\qquad
C=399/401,\qquad S=40/401.
```

Thus a^2+b^2=2 and C^2+S^2=1. Define

```math
\begin{aligned}
H_0={}&aZ_1Z_A+bX_1X_A+aC Z_2Z_B-bS Z_2Z_AZ_B\\
 &+bC X_2Z_AX_B+aS X_2X_B.
\end{aligned}
\qquad\text{(1)}
```

The original reference X/Z readouts before rewriting them in bisector
coordinates are

```math
B_1=(aZ_A+bX_A)/\sqrt2,\qquad
D_1=(aZ_A-bX_A)/\sqrt2,
```

```math
B_2=\frac{(aC-bS Z_A)Z_B+(bC Z_A+aS I)X_B}{\sqrt2},\quad
D_2=\frac{(aC-bS Z_A)Z_B-(bC Z_A+aS I)X_B}{\sqrt2}.
\qquad\text{(2)}
```

Each readout is a reflection. For the second pair, fix Z_A=z. The two
Pauli coefficients satisfy

```math
(aC-zbS)^2+(zbC+aS)^2=a^2+b^2=2.
```

Both coefficients are nonzero: aC>bS because a>b and C>S, while
bC>aS because C>sqrt(2)S, already implied by 399>60. Thus there are two genuinely
noncommuting two-dimensional blocks. Pair 1 likewise has two such blocks.
Their reflections are balanced: two positive and two negative eigenvalues.
No contractive interpolation is used in this example.

## 2. Exact spectrum and ordering

The commuting reflections

```math
A_0=Z_1Z_A,\qquad B_0=Z_2Z_B,\qquad R_0=X_2X_B
```

commute with H0 and with one another. Each joint sector (alpha,beta,r) has
dimension two. In that sector X1 XA and ZA are anticommuting reflections,
and H0 becomes

```math
a\alpha+aC\beta+aSr+bX_1X_A+b(rC-\beta S)Z_A.
```

Hence all sixteen eigenvalues are

```math
\lambda_{\alpha\beta r\pm}
=a\alpha+aC\beta+aSr\pm b\sqrt{1+(rC-\beta S)^2}.
\qquad\text{(3)}
```

The two largest come from alpha=beta=+1, the positive square-root branch,
and respectively r=+1,-1:

```math
U=\frac{1680+2\sqrt{144841}}{401\sqrt3},\qquad
m=\frac{1520+2\sqrt{176761}}{401\sqrt3}.
\qquad\text{(4)}
```

For ordering, when alpha,beta are not both positive the largest possible
value is at most

```math
a(1-C+S)+b\sqrt{1+(C+S)^2}<\frac3{20}+\frac32<2.
```

Here a<6/5, 1-C+S=42/401<1/8, b<1, and
sqrt(1+(C+S)^2)<3/2. If alpha=beta=+1 but the square-root sign is negative,
the eigenvalue is less than (6/5)(21/10)-4/5=43/25<2, using S<1/10 and
b>4/5. The two values (4) exceed 3.395, and U>m by the bounds below.
Thus U is simple and m is the actual second eigenvalue.

The following coarse rational bounds suffice for every comparison:

```math
\frac{1732}{1000}<\sqrt3<\frac{1733}{1000},\quad
380<\sqrt{144841},\quad
420<\sqrt{176761}<\frac{841}{2}.
```

They give

```math
\boxed{\frac{679}{200}<m<\frac{17}{5},\qquad
c:=U-m>\frac{11}{100}.}
\qquad\text{(5)}
```

For explicit rational witnesses,

```math
\frac{2360000}{694933}-\frac{679}{200}
=\frac{140493}{138986600}>0,
```

```math
\frac{2361000}{694532}-\frac{17}{5}
=-\frac{511}{868165}<0,
\qquad
\frac{79000}{694933}-\frac{11}{100}
=\frac{255737}{69493300}>0.
```

The last line lower-bounds the numerator of U-m by
160+2(380-420.5)=79. All radical brackets above follow by squaring positive
numbers. Since 7/5<sqrt(2)<283/200, (5) implies

```math
m<2+\sqrt2,\qquad
0<t-2<\frac1{50},\quad t:=4+\sqrt2-m.
\qquad\text{(6)}
```

Numerically, U is about 3.51472363 and m about 3.39910880. These decimal
values are illustrative only; no numerical root decision is used.

## 3. Actual top vector and chiral cross marginal

Let d=C-S=359/401 and q=d/sqrt(1+d^2). In the top sector, the R2,B pair is
the Bell state Phi+, and the R1,A pair is

```math
|\varphi\rangle=\sqrt{\frac{1+q}{2}}|00\rangle+
\sqrt{\frac{1-q}{2}}|11\rangle.
```

Consequently the unique top vector is Omega=varphi_(R1 A) tensor Phi+_(R2 B),
with actual memory marginal

```math
\boxed{\rho_Q=\frac{I+qZ_A}{4},\qquad q>\frac12.}
\qquad\text{(7)}
```

The last inequality is equivalent to 3*359^2>401^2. In particular this
marginal is full rank. Define Gamma=Y1Y2 and Omega_-=Gamma Omega. The exact
cross marginal is

```math
\boxed{\tau_Q:=\mathrm{Tr}_{R_1R_2}
|\Omega\rangle\langle\Omega_-|
=\frac{Y_AY_B}{4\sqrt{1+d^2}}.}
\qquad\text{(8)}
```

Indeed each local cross marginal equals minus the product of its two
Schmidt amplitudes times Y; multiplying the two factors gives (8).
It is off-diagonal in the Z_A basis.

## 4. An explicit one-block third pair makes the envelopes fail

Let P_+=(I+Z_A)/2 and P_-=(I-Z_A)/2. Take

```math
B_3=P_+Z_B+P_-I_B,\qquad
D_3=P_+X_B+P_-I_B.
\qquad\text{(9)}
```

On A=+ this is one sharp anticommuting pair; on A=- both readouts are
identity. Thus (9) has one noncommuting two-dimensional Jordan block plus
two scalar blocks, with minority ranks (11).

For a `(12)` variant, keep B3 unchanged and replace D3 by
`P_+ X_B+P_- Z_B`. Its active block is identical; on A=- the readouts
are I_B and Z_B, giving two scalar blocks. B3 has minority rank one and
the modified D3 has minority rank two. Both readouts still commute with
Z_A. The active Bell pole and the vanishing signed cross block used below
are therefore unchanged. The following argument applies to both variants.

Let h3=X3 B3+Z3 D3. On the active A=+ block it has eigenvalue 2 with Bell
projector P_+ tensor Pi_(R3 B). Since t>2, its positive resolvent obeys

```math
(tI-h_3)^{-1}\ge\frac{P_+\otimes\Pi_{R_3B}}{t-2}.
```

Compressing with the actual top vector and (7), the rank-one envelope
resolvent test obeys

```math
c\langle\Omega|(tI-h_3)^{-1}|\Omega\rangle
\ge\frac{c(1+q)}{8(t-2)}I_{R_3}
>\frac{(11/100)(3/2)}{8/50}I
=\boxed{\frac{33}{32}I>I.}
\qquad\text{(10)}
```

Therefore the ordinary actual one-mode envelope
mI+(U-m)|Omega><Omega| fails at Lambda.

The same example defeats the signed envelope retaining its exact negative
partner,

```math
H_0\le mI+c|\Omega\rangle\langle\Omega|
 -(U+m)|\Omega_-\rangle\langle\Omega_-|.
\qquad\text{(11)}
```

The final resolvent is block diagonal in Z_A, whereas (8) is off-diagonal.
Thus its compressed cross block between Omega and Omega_- is exactly zero.
Writing J_+,J_- for insertion of the two head vectors and A=tI-h3>0,
Woodbury gives

```math
J_+^*(A+(U+m)J_-J_-^*)^{-1}J_+
=J_+^*A^{-1}J_+
```

because J_+^*A^(-1)J_-=0. Hence the signed positive-update criterion is
identical to the already failing test (10). Keeping the one negative
partner cannot repair the loss from flattening the rest of the spectrum.

## 5. The actual Hamiltonian remains strictly below the benchmark

Let H* be the balanced Hamiltonian, obtained from (1) by C=1,S=0.
The [conserved-symmetry theorem](CONSERVED_SYMMETRY_CONVERSE.md#3-the-full-norm-bound-of-five)
gives `||H*+h3||<=5` for every third pair of Hermitian contractions, including
arbitrary complex readouts. The earlier [sharp equality theorem](SHARP_TWO_MODE_SUPPORT.md#5-the-whole-equality-boundary-obeys-a-strict-full-norm-bound)
even gives `(4+2sqrt(5))/sqrt(3)<5`, but the non-strict bound of five already
suffices here. Directly,

```math
\|H_0-H_*\|\le(a+b)(1-C+S)<\frac{84}{401}<\frac14,
```

using a+b<2. Thus

```math
\boxed{\|H_0+h_3\|<\frac{21}{4}<4+\sqrt2}
```

for every allowed third pair, not only (9). The envelope failure is
therefore a proof obstruction, not a counterexample to the interface
converse. It occurs with actual leading spectral data and actual memory
marginals, with all six displayed readouts genuine reflections in a still
unresolved complete signature.

## 6. Retaining the second positive mode repairs this example

The two positive leading eigenvectors both lie in the alpha=beta=+1
subspace, spanned by the copying vectors |ab>_R |ab>_Q. Tracing out R
therefore makes the entire two-mode head channel diagonal in the Q
computational basis, including its off-diagonal input blocks. It is EB.
Section 2 showed all other eigenvalues are less than two. Hence

```math
H_0\le2I+V\mathrm{diag}(U-2,m-2)V^*.
```

At Lambda the scalar resolvent parameter is t=k=2+sqrt(2). The [exact pure-memory resolvent bound](ROBUST_HEAD_CHANNEL_CONVERSE.md#11-center-the-resolvent-before-comparing-channels),
from the [last-query theorem](EXACT_LAST_QUERY_RESOLVENT.md#1-the-readout-elimination-theorem),
and the EB representation imply

```math
K_k\le(U-2)F(k)I<I,
```

because U<18/5 and F(k)<5/8. The first follows from sqrt(144841)<381 and
the previous lower bound on sqrt(3):
`U<2442000/694532<18/5`, witnessed by `5*2442000<18*694532`. For the second,

```math
\sqrt{8+8\sqrt2}>\frac{14}{5}+\sqrt2
```

by positive squaring: the squared gap is
`-46/25+(12/5)sqrt(2)>38/25>0`. Therefore
`F(k)=[2(sqrt(8+8sqrt(2))-k)]^(-1)<5/8`, and
`(U-2)F(k)<(8/5)(5/8)=1`.

Thus a two-positive-mode envelope succeeds for this exact instance,
whereas keeping only the top positive mode, even with its exact negative
partner, fails. This comparison concerns sufficient envelopes for the
same physical H0 and does not assert that all two-mode envelopes succeed.


## 7. Verification and remaining scope

Independent readers reconstructed the reflection identities, sixteen-eigenvalue
spectrum and ordering, radical brackets, actual Schmidt vector, both chiral
marginals, the Bell-pole normalization, the vanishing signed cross block,
and the successful two-positive-mode envelope. All universal and strict
comparisons above have analytical witnesses; displayed decimals are not
used to decide any inequality.

The two last-pair variants identify this limitation in both `(22)^2(11)`
and `(22)^2(12)`: flattening all other positive modes to the second
eigenvalue can lose the required bound. It does not refute the physical converse,
which holds here with a strict margin for every third pair. It also does
not refute the general two-mode strategy. All three complete remaining
reflection signatures, unrestricted optimality and publication originality
remain open. The operational model and MIT license are unchanged.

Reproduce the targeted exact comparisons and fixed matrix identities with

```bash
python tools/check_block_budget_and_envelopes.py --output results/block_budget_and_envelopes.json
```

The result records source and proof-note hashes. Its finite constructions
check the displayed identities and supplement the analytical proof; they do
not establish an unrestricted bound by sampling or certify novelty.
