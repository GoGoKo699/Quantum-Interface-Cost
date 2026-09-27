# A robust head-channel criterion and a nonclassical-family converse

**Research base:** main `3d230411930a2ac198cdb7f2ef9ad86701face1a`.
**Date:** 27 September 2026.

The coherent two-mode resolvent test tolerates a definite distance from
an entanglement-breaking channel. On a stated rectangle of actual
spectral parameters, full diamond distance at most `2/5` guarantees the
three-query bound `4+sqrt(2)`. That rectangle contains the entire regime
where the second earlier eigenvalue is at least `2+sqrt(2)`.

The criterion also proves the converse for the whole positive-quadrant
family in [NONCLASSICAL_TWO_MODE_CHANNEL](NONCLASSICAL_TWO_MODE_CHANNEL.md),
with an arbitrary third binary-POVM pair. This includes actual leading
channels with negative Choi partial transpose and two energies above
the one-mode threshold. The comparison channel is entanglement breaking;
the actual channel need not be.

**Status:** supplied analytical proofs, independently reconstructed
within this workspace. The channel criterion uses standard norm duality
and the previously evaluated pure-memory resolvent. No full remaining
reflection signature or unrestricted three-input converse is settled.
No publication-priority claim is made.

## 1. A quantitative criterion for the actual two-mode envelope

Let Q have dimension four and let

```math
H_0=X_1B_1+Z_1D_1+X_2B_2+Z_2D_2,
\qquad -I\le B_i,D_i\le I.
\qquad\text{(1)}
```

Write its first three eigenvalues as U,m,ell. Choose an isometry V
onto its first two eigenvectors and define

```math
\Phi(\omega)=\mathrm{Tr}_{R_1R_2}(V\omega V^\dagger),
\qquad \mathcal E=\Phi^*,\qquad
\Delta=\mathrm{diag}(U-\ell,m-\ell).
```

The [two-mode reduction](TWO_MODE_RESOLVENT.md) gives
`H_0<=ell I+V Delta V^dagger`. Put

```math
\Lambda=4+\sqrt2,\qquad D=\Lambda-U,\qquad t=\Lambda-\ell.
\qquad\text{(2)}
```

For a third pair of Hermitian contractions, let
`h=X_3 tensor B+Z_3 tensor D_3` and `R_t=(tI-h)^(-1)`.
The scalar D in (2) is unrelated to the memory readout D_3. The
four-by-four envelope test is

```math
\mathcal K_t=(I\otimes\sqrt\Delta)
  (\mathrm{id}_2\otimes\mathcal E)(R_t)
  (I\otimes\sqrt\Delta)\le I_4.
\qquad\text{(3)}
```

**Theorem.** Suppose the actual spectral parameters obey

```math
\boxed{D\ge19/10,\qquad 12/5\le t\le11/2.}
\qquad\text{(4)}
```

If there is an entanglement-breaking channel Psi from the head qubit
to Q such that

```math
\boxed{\|\Phi-\Psi\|_\diamond\le2/5,}
\qquad\text{(5)}
```

then (3) holds strictly for every third pair. Consequently
`||H_0+h||<=4+sqrt(2)`.

Here the diamond norm is the **full** completely bounded trace norm,
without the conventional extra factor 1/2 sometimes included in channel
distance. The theorem requires the rectangle (4); it does not require
`m>=2+sqrt(2)` if (4) is verified directly.

### 1.1. Center the resolvent before comparing channels

Since `||h||<=2` and t>2, its resolvent satisfies

```math
\left\|R_t-\frac{t}{t^2-4}I\right\|
\le\frac2{t^2-4}.
\qquad\text{(6)}
```

Both dual channels are unital, so their difference kills the scalar
term. Duality between the completely bounded trace norm and operator
norm gives, with `epsilon=||Phi-Psi||_diamond`,

```math
\left\|(\mathrm{id}_2\otimes(\Phi^*-\Psi^*))(R_t)\right\|
\le\frac{2\epsilon}{t^2-4}.
\qquad\text{(7)}
```

The [exact last-query theorem](EXACT_LAST_QUERY_RESOLVENT.md#1-the-readout-elimination-theorem)
gives the following upper bound for every pure memory compression of
R_t, and hence for every mixed memory compression:

```math
F(t)=\begin{cases}
\displaystyle\frac1{2(\sqrt{2t^2-4}-t)},&2<t\le3\sqrt2,\\[5pt]
\displaystyle\frac1{t-\sqrt2},&t\ge3\sqrt2.
\end{cases}
\qquad\text{(8)}
```

Write an entanglement-breaking channel as
`Psi(omega)=sum_j Tr(M_j omega) tau_j`, where the M_j are positive,
sum to I, and each tau_j is a memory state. Applying (8) to each tau_j
gives ` (id_2 tensor Psi^*)(R_t)<=F(t)I`. Thus (7) and
`Delta<=(U-ell)I` imply

```math
\boxed{\mathcal K_t\le
(U-\ell)\left[F(t)+\frac{2\epsilon}{t^2-4}\right]I.}
\qquad\text{(9)}
```

The comparison permits mixed and nonorthogonal prepared states. It
retains every off-diagonal block of the actual head channel.

### 1.2. Two quadratic comparisons prove the radius 2/5

Since `U-ell=t-D`, it suffices to use D=19/10 and epsilon=2/5 in
(9). First suppose t<=3sqrt(2), and put `r=sqrt(2t^2-4)`. The positive
square identity

```math
\left(\frac{3t}{2}-\frac7{10}\right)^2-r^2
=\frac14\left(t-\frac{21}{5}\right)^2+\frac2{25}
```

gives `r<=3t/2-7/10`. Rationalizing (8), the right side of (9) is
at most

```math
\frac{(t-19/10)(5t/2+9/10)}{2(t^2-4)}.
```

This is strictly below one when

```math
q_{\rm low}(t)=\frac{t^2}{2}-\frac{77t}{20}+\frac{629}{100}<0.
\qquad\text{(10)}
```

The branch interval is contained in `[12/5,17/4]`, because
`3sqrt(2)<17/4`. The quadratic is convex and its endpoint values are

```math
q_{\rm low}(12/5)=-7/100,\qquad
q_{\rm low}(17/4)=-833/800.
```

Next suppose `t>=3sqrt(2)>4`. Using `sqrt(2)<10/7`, the bound
`F(t)<=1/(t-10/7)` reduces the desired strict inequality to

```math
q_{\rm high}(t)=\frac45(t-19/10)(t-10/7)
 -(19/10-10/7)(t^2-4)<0.
\qquad\text{(11)}
```

This quadratic is convex, with leading coefficient 23/70. On the
containing interval `[4,11/2]`, its endpoint values are

```math
q_{\rm high}(4)=-234/175,\qquad
q_{\rm high}(11/2)=-909/1400.
```

Both comparisons prove `K_t<I`. The positive-update equivalence proves
the upper bound for the spectral envelope and hence for `H_0+h`.
The latter anticommutes with `Y_1Y_2Y_3 tensor I_Q`, so its spectrum
is symmetric and the same estimate bounds its operator norm.

## 2. The complete high-second-mode strip lies in the rectangle

Let `k=2+sqrt(2)` and suppose m>=k. The
[sharp support theorem](SHARP_TWO_MODE_SUPPORT.md) gives
`U+m<=4sqrt(3)`, hence

```math
D\ge6+2\sqrt2-4\sqrt3>19/10.
\qquad\text{(12)}
```

The strict comparison follows by positive squaring from
`sqrt(6)>3919/1600`, certified by
`6*1600^2-3919^2=1439>0`.

The positive-eigenvalue square budget from the two-mode reduction gives

```math
\ell^2\le32-U^2-m^2\le20-8\sqrt2<9.
\qquad\text{(13)}
```

The last inequality uses `121<128`. Since `7/5<sqrt(2)<3/2`,
it follows that `12/5<t<11/2`. Thus every actual operator in the
whole strip m>=k meets (4), and the channel-distance condition (5)
suffices uniformly there.

This implication uses m>=k. A near-maximal value of U+m alone has
not been used to infer m>=k or the rectangle.

## 3. A complete continuous family with non-EB leading channels

Use the actual construction from
[NONCLASSICAL_TWO_MODE_CHANNEL](NONCLASSICAL_TWO_MODE_CHANNEL.md).
In tensor order R1,R2,A,B, set

```math
a=\sqrt{3/2},\quad b=1/\sqrt2,\quad
0\le c\le1,\quad s=\sqrt{1-c^2},
```

and let

```math
H_0(c)=a\,ZIZI+b\,XIXI+c\,IZIZ+s\,IZYY
             +c\,IXZX-s\,IXXI.
\qquad\text{(14)}
```

As in that construction, the first reference is written in bisector
coordinates: its original readouts are `(aZ_A+-bX_A)/sqrt(2)`, which
are reflections. The second pair
`cZ_B+sY_AY_B, cZ_AX_B-sX_A` consists of anticommuting reflections.
Thus (14) retains the original physical constraints.

**Family converse.** For every c in `[0,1]` and every third pair of
Hermitian contractions,

```math
\boxed{\|H_0(c)+X_3B_3+Z_3D_3\|\le4+\sqrt2.}
\qquad\text{(15)}
```

The earlier exact spectral calculation gives

```math
U=m=\sqrt{7+4ac},\qquad
\ell=L=\sqrt{7-4ac},\qquad d=U^2-1=6+4ac.
\qquad\text{(16)}
```

At c=0 the two displayed positive levels coincide; the subsequent
triangle argument covers that endpoint directly.

### 3.1. Bound the coherent channel on c>=19/20

In the fixed logical Pauli frame of the exact construction,

```math
\begin{aligned}
\Phi_c(I)&=I/2,&
\Phi_c(X)&=\alpha ZI+\beta XX,\\
\Phi_c(Y)&=\eta XY,&
\Phi_c(Z)&=\gamma IZ+\delta YY,
\end{aligned}
\qquad\text{(17)}
```

where

```math
\begin{aligned}
\alpha&=\frac{2a+8c+4ac^2}{Ud},&\beta&=-s/U,\\
\eta&=-2bs/d,&\gamma&=\frac{8b+6abc}{Ud},&
\delta&=\frac{2abs}{Ud}.
\end{aligned}
\qquad\text{(18)}
```

At c=1 the last three coefficients beta,eta,delta vanish, while
`alpha(1)=1/sqrt(6)` and `gamma(1)=1/(2sqrt(3))`. Every output of
Phi_1 is diagonal, so Phi_1 is entanglement breaking.

For a qubit-input map Theta with **Theta(I)=0**, Pauli expansion gives

```math
\Theta(A)=\frac12\sum_{\sigma=X,Y,Z}
 \mathrm{Tr}(\sigma A)\Theta(\sigma),\qquad
\|\Theta\|_\diamond\le\frac12\sum_\sigma
 \|\Theta(\sigma)\|_1.
\qquad\text{(19)}
```

The second assertion uses that the completely bounded trace norm of
the scalar functional `A->Tr(sigma A)` equals `||sigma||=1`.
Here `Theta=Phi_c-Phi_1` satisfies Theta(I)=0 by (17). Every memory
Pauli has trace norm four, hence

```math
\|\Phi_c-\Phi_1\|_\diamond\le
2\bigl(|\alpha(c)-\alpha(1)|+|\gamma(c)-\gamma(1)|
       +|\beta|+|\eta|+|\delta|\bigr).
\qquad\text{(20)}
```

For `19/20<=c<=1`, use
`6/5<a<5/4`, `b<3/4`, and `ab<7/8`. They imply
`ac>57/50`, `U>17/5`, and `d>264/25>21/2`, giving

```math
|\beta|\le3s/10,\qquad |\eta|\le3s/20,
\qquad |\delta|\le s/20.
\qquad\text{(21)}
```

The sharper intermediate coefficients are 5/17, 1/7, and 5/102.
To control the two remaining terms, simplify and differentiate:

```math
\alpha(c)=\frac{1+2ac}{2aU},\qquad
\alpha'(c)=\frac{2(3+ac)}{U^3}<\frac{125}{578}<\frac14,
```

```math
\gamma'(c)=-\frac{ab(17+30ac+12a^2c^2)}
                    {U^3(3+2ac)^2}.
\qquad\text{(22)}
```

Writing z=ac, we have `1<z<5/4`. In the last expression the numerator
is less than 75 and the denominator exceeds `3^3*5^2=675`, so
`|gamma'|<1/9<1/4`. Therefore

```math
|\alpha(c)-\alpha(1)|+|\gamma(c)-\gamma(1)|\le(1-c)/2.
```

Equations (20)--(22) yield a uniform bound in the full diamond norm:

```math
\boxed{\|\Phi_c-\Phi_1\|_\diamond\le s+1-c
\le\frac{29}{80}<\frac25.}
\qquad\text{(23)}
```

Indeed `s^2<=39/400<25/256`, so `s<=5/16`, and `1-c<=1/20`.
There is no optimization over sampled angles in this argument.

### 3.2. The rectangle and triangle ranges cover all c

Since `7+4a<12<49/4`, (16) gives U<7/2, so
`D>1/2+sqrt(2)>19/10`. Also `ell^2<=7<9`, and therefore
`12/5<t<11/2`. The actual parameters meet (4). Theorem 1 and (23)
prove (15) for every c>=19/20.

For the remaining angles define

```math
c_*:=\frac{4\sqrt2-1}{2\sqrt6}.
\qquad\text{(24)}
```

When c<=c_*, (16) gives `U<=2+sqrt(2)`. Thus the triangle inequality
already yields `||H_0+h_3||<=U+2<=4+sqrt(2)`. The ranges overlap:
`19/20<c_*<1`. For the first comparison,

```math
c_*^2=\frac{33-8\sqrt2}{24}>\frac{361}{400}
\quad\Longleftrightarrow\quad567>400\sqrt2,
```

certified by `567^2-2*400^2=1489>0`. The second reduces to
`9<8sqrt(2)`, certified by `81<128`. This proves (15) on all of
`[0,1]`, including both endpoints.

For every `c_*<c<1`, both leading energies exceed `2+sqrt(2)`, while
the normalized Choi partial transpose of Phi_c has eigenvalue

```math
-\frac{bs}{6+4ac}<0.
\qquad\text{(25)}
```

Thus the converse includes a full continuous set of actual non-EB
leading channels. The earlier rational point
`c=39999/40001, s=400/40001` is included. No extension to all other
earlier-pair orientations is inferred from this family.

## 4. A complementary-state route to the distance condition

Let rho_RE be the complementary state of the normalized Choi
purification of Phi. Suppose rho0_RE, on the same R and E spaces, is
the corresponding complement of an EB channel Psi0 with output
dimension at most four, and both
states have E marginal I_2/2. Put

```math
q=\|\sqrt\rho-\sqrt{\rho_0}\|_2.
```

Uhlmann's theorem aligns their purifications by a memory unitary so
that their overlap is the root fidelity f. The corresponding isometries
then satisfy `||V-V_0||<=||V-V_0||_2=2sqrt(1-f)`. Expanding the
difference of their two dilation channels gives

```math
\|\Phi-\Psi\|_\diamond\le4\sqrt{1-f}
\le2\sqrt2\,q,
\qquad\text{(26)}
```

where Psi is a memory-unitary conjugate of Psi0 and is still EB.
The second inequality uses
`f>=Tr(sqrt(rho)sqrt(rho0))=1-q^2/2`. Consequently, under the spectral
rectangle (4), the sufficient root-state distance is

```math
q\le\sqrt2/10.
\qquad\text{(27)}
```

This continuity criterion is conditional. The additional construction in
[QUANTITATIVE_TWO_MODE_STABILITY](QUANTITATIVE_TWO_MODE_STABILITY.md)
supplies the support-deficit bridge: writing
`epsilon=4sqrt(3)-(U+m)`, it proves the converse for
`epsilon<=2^-24` when m>=k. A separate decoder-stability argument there
proves the unconditional bound `||H_0+h_3||<16/3` for
`epsilon<=2^-32`, with no assumption on m. These are sufficient radii,
not optimal ones. The rectangle inference in this report's Section 2
continues to require its m>=k hypothesis.

## 5. Verification and remaining scope

The centered-resolvent estimate, both rational quadratic comparisons,
the channel coefficient derivatives, and the complete family overlap
were independently reconstructed within this workspace. These are
analytical arguments over the stated intervals, not parameter scans.
Internal verification is not external peer review or a novelty claim.

The [targeted checker](../../tools/check_quantitative_two_mode.py)
verifies the exact scalar comparisons and reconstructs three specified
NPT-family points and four head constructions. Run

```sh
python tools/check_quantitative_two_mode.py --output results/quantitative_two_mode.json
```

The [recorded JSON](../../results/quantitative_two_mode.json) includes
source and proof-file hashes. Identical files in the same runtime
environment give byte-identical output; matrix rounding can differ
across environments within the reported tolerance. These fixed
construction checks supplement the supplied proofs and do not replace
the interval arguments or establish an unrestricted converse.

The criterion (5) remains a sufficient condition on the actual coherent
channel. This report does not show it for every physical head. The
complete family theorem leaves the three full unresolved reflection
signatures and the unrestricted converse open. No operational model,
encoder class, memory convention, or LICENSE term is changed.
