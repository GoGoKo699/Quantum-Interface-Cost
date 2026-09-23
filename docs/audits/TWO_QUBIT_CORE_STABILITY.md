# Two-qubit core stability and an explicit low-rank neighborhood

Date: 2026-09-23. Reviewed main:
`b653fe866930aa8d1c07ad3bf34629a14b41009a`.
Reviewed tree: `fb3049fa092eda007d470bad8873038787638c30`.

**Status:** supplied analytical deduction with an exact rational interval
certificate for one compact scalar domain. The reductions and certificate
received independent checks within this workspace. This is not external
peer review, a proof of unrestricted optimality, or a publication-originality
certificate.

## 1. Statement and remaining gap

For any complex two-qubit density matrix, define

$$
g(\rho)=\sum_{U\in\{X_A,Z_A,X_B,Z_B\}}
\|\sqrt\rho U\sqrt\rho\|_1,
\qquad
\Delta(\rho)=2\sqrt2+(2-\sqrt2)S(\rho)-g(\rho).
$$

Entropy is in bits. Order the eigenvalues as
`lambda_1>=lambda_2>=lambda_3>=lambda_4`, and put
`epsilon=lambda_3+lambda_4`. When epsilon is positive and the top-two
spectral subspace is chosen, let sigma be the normalized restriction to
that subspace. Thus

$$
\rho=(1-\epsilon)\sigma+\epsilon\tau,
\qquad \sigma\tau=0,
\qquad \operatorname{rank}\sigma,\operatorname{rank}\tau\le2.
\tag{1}
$$

**Theorem.** If `0<epsilon<=1/29` and `g(sigma)>10/3`, then
`Delta(rho)>0`. Separately, every spectrum with `0<epsilon<=1/29` and
`m=lambda_2/(lambda_1+lambda_2)<=1/5` satisfies `Delta(rho)>0`,
regardless of its eigenvectors or core score. Moreover, **every** two-qubit
state with `epsilon<=2^(-20)` satisfies the entropy inequality; the
inequality is strict when epsilon is positive.

Combined with the preceding
[spectral gate](TWO_QUBIT_SPECTRAL_TAIL_GATE.md), any two-qubit counterexample
must satisfy all three conditions

$$
\boxed{2^{-20}<\lambda_3+\lambda_4<\frac1{29},\qquad
\frac{\lambda_2}{\lambda_1+\lambda_2}>\frac15,\qquad
g(\sigma)\le\frac{10}{3}.}
\tag{2}
$$

The top-two subspace is unique for every state to which the new high-score
argument applies: its proof gives `lambda_2>(3/10)(1-epsilon)>lambda_3`.
Rank-at-most-two states are already covered by the prior rank-two theorem.

The interval certificate uses a strictly negative SLD-gap upper bound on
its SLD branch, preserving the theorem's strict conclusion. Equation (2)
also makes the remaining top-two subspace unique, since
`lambda_2>(1-epsilon)/5>lambda_3`.
**The two-qubit case with a low-score core remains unresolved.**
The separate all-n entropy inequality, unrestricted equal-accuracy memory
rate, and publication originality also remain open.

All matrices here are virtual normalized seeds. The original operational
model still allows one arbitrary unknown quantum specimen, one delayed
local query, unrestricted collective encoding, unlimited finite classical
records, worst-case quantum dimension, and error uniform over every input
and query. The argument introduces no physical copies, encoder restriction,
average-memory accounting, joint-decoder requirement, or postselection.

## 2. Established inputs and the core decoder classification

Set `c=2-sqrt(2)`. Write the nonzero eigenvalues of sigma as
`p>=m>0`, where `p+m=1`, and define

$$
\begin{aligned}
G_{\rm act}(m)&=\sqrt{4-2(p-m)^2},&
G(m)&=\sqrt2+G_{\rm act}(m),\\
d&=G(m)-g(\sigma),&
a_0&=2-G_{\rm act}(m),\\
\delta(m)&=2\sqrt2+c h_2(m)-G(m).
\end{aligned}
\tag{3}
$$

The [rank-two spectrum theorem](../ENTROPY_INEQUALITY_BOUNDARIES.md),
Section 1, gives `d>=0`, `delta>=0`, and `Delta(tau)>=0`. It permits
arbitrary complex eigenvectors. The
[one-qubit decoder proof](../ONE_QUBIT_OPTIMALITY.md), Sections 3--4,
allows each trace-norm optimizing memory-qubit decoder to be chosen as
`+I`, `-I`, or a traceless Pauli direction. A site is active if both
its decoders are traceless. With zero or two active sites,
`g(sigma)<=2sqrt(2)`, so a core with score greater than `10/3` has exactly
one active site.

For completeness, the inactive site cannot have one scalar and one
traceless decoder at that score. Write its two contributions as a and b,
with the traceless contribution b. Their full observables anticommute and
square to I, hence `a^2+b^2<=1`. Independent-setting CHSH monogamy gives
`f_active^2+b^2<=4`: the optimized two-traceless score at the inactive
site is at least `|b|`. Therefore

$$
\begin{aligned}
g(\sigma)&\le\sqrt{4-b^2}+\sqrt{1-b^2}+|b|\\
&\le3+|b|-\frac34 b^2\le\frac{10}{3}.
\end{aligned}
\tag{4}
$$

Thus the inactive site has **two scalar decoders**. Relabel it B and the
active site A. Adjust its X/Z signs and define

$$
B_0=\frac{X_B+Z_B}{\sqrt2},\quad
C_0=\frac{X_B-Z_B}{\sqrt2},\quad
P_* = I_A\otimes|\beta_+\rangle\langle\beta_+|,
\quad Q_*=I-P_*.
\tag{5}
$$

Here beta_+ is the positive eigenstate of the signed bisector B_0;
the displayed notation absorbs those signs. No axes outside the original
query pair are substituted into the task.

## 3. A block trace-norm estimate retaining the actual support

Let `P=supp(sigma)`, `Q=I-P`. For an invertible Hermitian A, the block
matrix `M=[[A,B],[B^dagger,D]]` satisfies

$$
\|M\|_1\le\|A\|_1+
\operatorname{Tr}(B^\dagger|A|^{-1}B)
+\|D-B^\dagger A^{-1}B\|_1.
\tag{6}
$$

Indeed, write M as
`[I;B^dagger A^{-1}] A [I,A^{-1}B]` plus its lower Schur block.
Splitting A into its positive and negative parts bounds the first term's
trace norm by `Tr|A|+Tr(B^dagger|A|^{-1}B)`. A further triangle inequality
uses
`||B^dagger A^{-1}B||_1<=Tr(B^dagger|A|^{-1}B)` and yields the simpler
upper bound with `||D||_1` and twice the cross trace.

For a query U set, on P,

$$
T_U=PUP,\qquad
C_U=\sqrt\sigma\,|\sqrt\sigma T_U\sqrt\sigma|^{-1}\sqrt\sigma.
$$

All these compressions will be shown invertible below. Applying (6) to
`sqrt(rho) U sqrt(rho)` gives

$$
\begin{aligned}
g(\rho)&\le(1-\epsilon)g(\sigma)+\epsilon g(\tau)+2\epsilon K,\\
K&=\sum_U\operatorname{Tr}(\tau QUP C_U PUQ),\\
\Delta(\rho)&\ge(1-\epsilon)[\delta(m)+d]
+c h_2(\epsilon)-2\epsilon K.
\end{aligned}
\tag{7}
$$

The entropy identity for orthogonal supports in (1) is exact, and
`Delta(tau)>=0` was used only in the last line.

If T_U is positive or negative definite, then `C_U=|T_U|^{-1}`.
Generally, with `kappa=p/m`,

$$
\|C_U\|_\infty\le\frac{\sqrt\kappa}{s_{\min}(T_U)}.
\tag{8}
$$

To prove (8), direct multiplication gives `C_U T_U sigma T_U C_U=sigma`.
Since `T_U sigma T_U>=m s_min(T_U)^2 I` and `sigma<=pI`, the claim follows.

## 4. Coupled principal angles and the monogamy input

Let `u>=v>=0` be the squared sines of the two principal angles between
P and P_*. Put

$$
\xi=\sqrt2-f_B,\qquad L=G_{\rm act}(m)-f_A,
\qquad d=\xi+L.
$$

The rank-two correlation bound gives `L>=0`, while the scalar B decoders
give the exact identity and lower bound

$$
\xi=2\sqrt2\operatorname{Tr}(\sigma P Q_*P)
\ge2\sqrt2(m u+p v).
\tag{9}
$$

The final inequality pairs the larger principal-angle eigenvalue with
the smaller eigenvalue m of sigma.

Write

$$
q=\sqrt{(1-u)(1-v)}+\sqrt{uv}
=\cos(\arcsin\sqrt u-\arcsin\sqrt v).
$$

The B marginal of the flat state P/2 has Bloch length at most q. To see
this, use the cosine-sine decomposition of P relative to P_* and Q_*.
Its two diagonal block traces are `2-u-v` and `u+v`; the magnitude of
the off-diagonal block trace is at most
`sqrt(u(1-u))+sqrt(v(1-v))`. The squared marginal Bloch length is therefore
at most

$$
(1-u-v)^2+
[\sqrt{u(1-u)}+\sqrt{v(1-v)}]^2=q^2.
$$

Since `sigma>=mP`, partial trace and the minimum-eigenvalue bound imply

$$
r_B(\sigma)\le R:=1-2m(1-q).
\tag{10}
$$

The required stronger active-score estimate is a consequence of an
**established prior theorem**. Cheng--Hall,
[arXiv:1610.09302v3](https://arxiv.org/pdf/1610.09302v3), 25 January 2017,
printed p. 3, Eq. (10), gives the difference of the optimized CHSH
parameters of two marginals in terms of the remaining local Bloch lengths.
Equation (14) gives their sum bound, allowing independent settings. For
the pure three-qubit purification QAB of sigma these read

$$
M_{AQ}-M_{AB}=2(r_B^2-r_Q^2),\qquad M_{AQ}+M_{AB}\le2.
$$

The squared CHSH optimum is `4M`. Our active score, multiplied by
sqrt(2), is an admissible CHSH value, and `r_Q=p-m`. Hence

$$
f_A^2\le2M_{AQ}\le2(1+r_B^2-(p-m)^2).
\tag{11}
$$

The pure three-qubit hypothesis holds because the **core**, not the full
state rho, has a qubit purification. The theorem is not applied to a
four-dimensional memory. The same source's Eq. (1) and Eqs. (13)--(14),
with the mixed-state extension following them, justify (4).

Combining (10)--(11) gives

$$
L\ge\frac{1-r_B^2}{G_{\rm act}}
\ge m(1-q^2)
\ge m(1-u)(\sqrt u-\sqrt v)^2.
\tag{12}
$$

Here `G_act<=2` and `1-R^2>=2m(1-q^2)` because `m<=1/2`.
The final inequality follows by expanding the sine of the angle difference.
This step retains both principal angles; controlling only their maximum
would lose the active site's necessary score deficit.

### A uniform finite-angle cutoff

High core score forces `G(m)>10/3`, hence `m>3/10`. Also
`d<G(m)-10/3<=sqrt(2)-4/3<17/210`; (9) first gives `u<1/10`.
Using (9), (12), `p>=m`, and minimizing over sqrt(v),

$$
d\ge m u\left[2\sqrt2+
\frac{(9/10)2\sqrt2}{2\sqrt2+9/10}\right]
>\frac72 m u.
$$

The strict scalar comparison follows, for example, from
`97/20-(17/5)sqrt(2)>0`. On the other hand, writing `r=1-2m`,

$$
G(m)-\frac{10}{3}\le\sqrt2-\frac43-\frac{r^2}{2}
<\frac{7m}{40}.
$$

For the last inequality, complete the square in r. Its largest possible
difference is less than
`17/210-7/80+49/12800=-731/268800`. Therefore

$$\boxed{u<\frac1{20}.}\tag{13}$$

## 5. Exact finite-angle bounds for K

For either active-site query V, `[V,P_*]=0`, so
`||PVQ||<=2sqrt(u)`. The identity
`(PVP)^2=P-PVQVP` shows
`s_min(PVP)>=sqrt(1-4u)>0`. Trace-norm Cauchy--Schwarz also gives

$$
F_V(\sigma)^2\le\operatorname{Tr}(\sigma(PVP)^2),
\qquad
1-F_V(\sigma)\ge\tfrac12\operatorname{Tr}(\sigma PVQVP).
$$

Using (8), `tau<=I_Q` and `sigma>=mP`, the two active terms satisfy

$$
K_A\le\min\left\{
B(u,m)[a_0+L],\frac{8\sqrt\kappa u}{\sqrt{1-4u}}\right\},
\qquad B(u,m)=\frac{2\sqrt\kappa}{m\sqrt{1-4u}}.
\tag{14}
$$

The term `a_0+L=2-f_A` must not be replaced by L alone.

For the two scalar-site queries define operators on Q by
`R_0=-QB_0Q` and `T_0=-QC_0Q`. Closeness to Q_* gives

$$
R_0\ge(1-2u)I,
\qquad \|T_0\|\le2\sqrt{u(1-u)}.
$$

The latter follows from the anticommuting B_0,C_0 expectation bound for
a vector in Q whose P_* weight is at most u. Put `r_0=1-2u` and
`t_0=2sqrt(u(1-u))`. Equation (13) implies `r_0>t_0`, so the scalar-site
compressions are strictly definite. For an involution U, its block inverse
identity gives

$$
QUP(PUP)^{-1}PUQ=QUQ-(QUQ)^{-1}.
$$

Consequently

$$
K_B\le A(u):=
\sqrt2(1-2u)\left[\frac{2}{1-8u+8u^2}-1\right].
\tag{15}
$$

Here is the operator step preserving the finite-angle cancellation. The
sum of the two inverse compressions uses

$$
(R_0+T_0)^{-1}+(R_0-T_0)^{-1}
=2R_0^{-1/2}[I-(R_0^{-1/2}T_0R_0^{-1/2})^2]^{-1}R_0^{-1/2}.
$$

It is at most `2r_0/(r_0^2-t_0^2) I`; subtracting the two direct
compressions proves (15). No Taylor remainder is discarded.

On `0<=u<=1/20`,

$$
A(u)-\sqrt2\le29u,\qquad
B(u,m)\le\frac{\sqrt5\sqrt\kappa}{m}.
\tag{16}
$$

For the first, the difference of numerator polynomials decreases on that
interval and is positive at the endpoint: `899>622sqrt(2)`. Define

$$
B_*(m)=\frac{\sqrt5\sqrt\kappa}{m},\quad
C_1(m)=\frac9m,\quad
C_2(m)=\frac{29+4\sqrt5\sqrt\kappa}{(7/2)m}.
$$

Equations (9), (12), (14)--(16) yield the two useful bounds

$$
\boxed{K-\sqrt2\le
\min\{C_1d+B_*a_0,\ C_2d\}.}
\tag{17}
$$

For the second, (14) is at most `4sqrt(5)sqrt(kappa)u` and
`d>(7/2)mu`. For the first it suffices to prove
`29u+B_*L<=C_1(xi+L)`. Set `t=sqrt(kappa)`,
`a=18sqrt(2)` and `b=(19/20)(9-sqrt(5)t)`. The required difference is
bounded below by the quadratic form in `sqrt(u),sqrt(v)` with matrix

$$
\begin{pmatrix}a+b-29&-b\\-b&a t^2+b\end{pmatrix}.
$$

It is positive definite uniformly for `1<=t<sqrt(7/3)`. Indeed,
`a>=126/5`, `a-29>=-19/5`, `209/40<=b<=133/20`; its first diagonal
is at least `57/40`, and its determinant is at least

$$
\frac{57}{40}\frac{126}{5}
-\frac{133}{20}\frac{19}{5}=\frac{266}{25}>0.
$$

Also `C_2>C_1` and `C_2<41` throughout the domain.

## 6. Small tails: an elementary certificate

For `epsilon<=1/100`, (7), (17) and `delta>=0` give

$$
\Delta(\rho)\ge c h_2(\epsilon)-2\sqrt2\epsilon
+(1-\epsilon-2\epsilon C_2)d>0.
\tag{18}
$$

The coefficient of d is positive because `C_2<41`. The remaining term
is positive since
`h_2(epsilon)/epsilon>log_2(1/epsilon)>=log_2(100)>6>2sqrt(2)/c`.
This proves the first elementary part for every high-score core, with
no spectral SLD condition.

## 7. Nearly balanced cores: an elementary certificate

Suppose `m>=9/20`, so `r=p-m<=1/10`. On (13), the sharper constants are

$$
A(u)-\sqrt2\le\frac{57}{2}u,
\qquad B(u,m)\le\frac{11}{2}.
$$

For A, the endpoint comparison is `622sqrt(2)/31<57/2`; the same
polynomial monotonicity used in (16) applies. For B its squared upper
bound is `22000/729<121/4`.

Equation (12) implies `L>=(5/12)(sqrt(u)-sqrt(v))^2`, and (9) gives
`xi>=(9sqrt(2)/10)u+sqrt(2)v`. These imply

$$
\frac{57}{2}u+\frac{11}{2}L\le19(\xi+L)=19d,
\qquad
K\le\sqrt2+19d+\frac{11}{2}a_0.
\tag{19}
$$

For an explicit verification, the quadratic matrix has off-diagonal
`-45/8`, lower diagonal `19sqrt(2)+45/8` and upper diagonal
`171sqrt(2)/10-183/8`. Its first diagonal is positive and its determinant is

$$
\frac{39159}{80}-\frac{5415}{16}\sqrt2
>\frac{12141}{1120}>0.
$$

Write `d_flat=sqrt(2)-4/3`. High core score gives `d<d_flat-a_0`.
For `epsilon<=1/39`, substitution of (19) into (7), dropping the
nonnegative d coefficient and spectral entropy margin, gives

$$
\Delta(\rho)\ge c h_2(\epsilon)-2\sqrt2\epsilon-11\epsilon a_0>0.
$$

Indeed `log_2(1/epsilon)>5`, `5c-2sqrt(2)>1/10`, and
`a_0<=3r^2/5<=3/500`.

For `epsilon` between `1/39` and `1/29`, substitute
`d<=d_flat-a_0` into the negative d coefficient. The resulting lower bound is

$$
F(\epsilon)=c h_2(\epsilon)-2\sqrt2\epsilon
+(1-39\epsilon)d_{\rm flat}+27\epsilon a_0
-c(1-\epsilon)[1-h_2(m)].
\tag{20}
$$

It is concave in epsilon. The scalar inequalities
`a_0>=r^2/2` and `1-h_2(m)<=3r^2/4` hold for `r<=1/10`.
The latter follows by bounding the positive entropy series by
`r^2/[2 ln(2)(1-r^2)]` and using `ln(2)>69/100`.

At `epsilon=1/39`, the flat part exceeds `1/390`, and the nonflat
addition is at least `-(6/65)r^2>=-3/3250`, so (20) is positive.
At `epsilon=1/29`, the nonflat addition is nonnegative because

$$
\frac{27}{29}a_0-\frac{28c}{29}[1-h_2(m)]
\ge\left(\frac{27}{58}-\frac{63}{145}\right)r^2>0
$$

when r is nonzero, and equals zero at r=0. The flat endpoint multiplied
by 29 is

$$
c[\log_2 29+28\log_2(29/28)]-12\sqrt2+\frac{40}{3}
>\frac{1279}{121800}>0.
$$

An exact lower certificate uses `29^20>2^97`, `ln(2)<7/10`,
`ln(29/28)>1/29` and `sqrt(2)<99/70`. Concavity completes this
entire region, independently of the spectral SLD condition.

## 8. The compact scalar domain

It remains to consider

$$
\frac1{100}\le\epsilon\le\frac1{29},
\qquad \frac3{10}\le m\le\frac9{20}.
\tag{21}
$$

The [exact two-qubit SLD minimum](../TWO_QUBIT_SLD_SPECTRUM.md) gives
`g(rho)<=2sqrt(4-E_*(lambda))`. Put `r=1-2m`,
`A=4-(1-2epsilon)^2`, `z=(1-epsilon)r^2`, and

$$
\begin{aligned}
D(\epsilon,m)={}&2\sqrt{A-z}-(2+\sqrt2)-c h_2(\epsilon)\\
&+c(1-\epsilon)[1-h_2(m)]
+\epsilon\max\{0,c-1/\sqrt A\}.
\end{aligned}
\tag{22}
$$

If the exact spectral SLD bound fails to certify the entropy target,
then necessarily `D>0`. To prove this implication, write the two tail
eigenvalues as `epsilon(1+s)/2, epsilon(1-s)/2`. The two within-pair
terms and the parallel-sum inequality for the cross terms give

$$
E_*\ge(1-2\epsilon)^2+(1-\epsilon)r^2+\epsilon s^2.
$$

Explicitly, for the ordered eigenvalues a,b,c',d', use
`ac'/(a+c')+bd'/(b+d')<=(a+b)(c'+d')/(a+b+c'+d')`.
Also `h_2((1+s)/2)>=1-s^2`. With `y=epsilon s^2`, the derivative
of the relaxed score-minus-entropy gap in y is
`c-1/sqrt(A-z-y)<=c-1/sqrt(A)`. Its possible increase over
`0<=y<=epsilon` is bounded by the last term of (22). Thus `D<=0`
is already a valid entropy certificate.

Define

$$
D_{\max}(m)=G(m)-10/3,\qquad b(m)=B_*(m)a_0(m),
$$

and let Lambda be the maximum, over `0<=d<=D_max`, of

$$
\ell(d)=2\epsilon\min\{C_1d+b,C_2d\}-(1-\epsilon)d.
$$

This is piecewise linear. Its maximum is attained at zero, at D_max,
or at `d_*=b/(C_2-C_1)` if that point lies between them. Equations
(7), (17) give the sufficient condition

$$
\boxed{c h_2(\epsilon)-2\sqrt2\epsilon
+(1-\epsilon)\delta(m)-\Lambda(\epsilon,m)>0.}
\tag{23}
$$

This is an optimization over two real scalars, not over quantum states.

## 9. Exact rational interval certificate

[tools/certify_two_qubit_core.py](../../tools/certify_two_qubit_core.py)
verifies the disjunction `D<0` or (23) throughout the closed rectangle
(21). Run

```bash
python tools/certify_two_qubit_core.py
```

The script uses only standard-library integer operations. Each interval
endpoint is an integer divided by `2^80`. Products and quotients round
outward using integer floor and ceiling. Square roots use integer square
root with an explicit upward correction. For logarithms, range reduction
to `[1,2]` is followed by

$$
\ln x=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,
\quad z=\frac{x-1}{x+1},\quad
0\le R_N\le\frac{2z^{2N+1}}{(2N+1)(1-z^2)},\quad N=72.
$$

Binary entropy is enclosed using its monotonicity on `(0,1/2]`.
The certificate has no floating-point arithmetic, numerical optimizer,
random sampling or state simulation. It uses explicit runtime checks;
Python optimization flags do not disable its verification.

Subdivision covers the full rectangle, with shared exact dyadic boundaries
between children. Every accepted leaf has either `D.upper<0` or a strictly
positive interval lower bound for (23). The analytic nonnegativity of delta
and D_max is used only by intersecting intervals with the physically
relevant half-line. The piecewise-linear maximum includes every possible
breakpoint, including uncertain membership near an interval boundary.
An unclassified leaf causes failure rather than a success claim.

Recorded exact result:
[two_qubit_core_certificate.json](../../results/two_qubit_core_certificate.json).

| Quantity | Value |
|---|---:|
| Accepted leaves | 755 |
| Leaves certified by D<0 | 476 |
| Leaves certified by (23) | 279 |
| Subdivisions | 754 |
| Maximum subdivision depth | 16 |
| Smallest positive lower-bound numerator | 12665039428067297599 |
| Common denominator | 1208925819614629174706176 = 2^80 |

Ordinary and optimized-interpreter runs reproduced the same certificate.
This finite calculation proves the stated scalar disjunction conditional
on the supplied analytical reductions; it is not evidence from testing
sampled density matrices. Together with Sections 6--7 it proves the
high-score-core theorem.

## 10. A separate gate for very unbalanced cores

The same necessary condition (22) also excludes every normalized core
spectrum with `m<=1/5`, without the high-score assumption or any interval
calculation. Here the scalar expression satisfies

$$D(\epsilon,m)\le0,\qquad
0\le\epsilon\le1/29,\quad 0\le m\le1/5,
\tag{24}$$

and is strictly negative when epsilon is positive. We prove this by
reducing the rectangle to four endpoints.

The maximum term in (22) can be removed: `c>1/sqrt(3)` because
`17>12sqrt(2)`, and `A>=3`. Thus write its last term as
`epsilon(c-1/sqrt(A))`. Put `q=1-epsilon`, `r=1-2m`, and
`B=A-q r^2>=2`. For positive epsilon,

$$
\partial_\epsilon^2(2\sqrt B)
=-\frac8{\sqrt B}-\frac{(B')^2}{2B^{3/2}}
\ge-\frac{57}{4\sqrt2},
$$

because `B'=4-8epsilon+r^2<=5`. Meanwhile

$$
-c h_2''(\epsilon)
=\frac{c}{\ln(2)\epsilon(1-\epsilon)}
>\frac{1160}{49}>\frac{57}{4\sqrt2},
$$

using `c>4/7`, `ln(2)<7/10`, and
`epsilon(1-epsilon)<=1/29`. The term `cq[1-h_2(m)]` is affine in
epsilon. The second derivative of the last term is

$$
\frac{A'-4\epsilon-3\epsilon(A')^2/(4A)}{A^{3/2}}>0:
$$

its numerator is at least `4-16epsilon`. Hence D is strictly convex in
epsilon and continuous at zero; its maximum is on an epsilon endpoint.

For each fixed epsilon, put `t=m(1-m)` and `B_0=A-q>=2`. Direct
differentiation yields

$$
\begin{aligned}
D_m&=q\left[\frac{4(1-2m)}{\sqrt B}
-c\log_2\frac{1-m}{m}\right],\\
D_{mm}&=q\left[\frac{c}{\ln(2)t}
-\frac{8A}{(B_0+4qt)^{3/2}}\right].
\end{aligned}
$$

The sign of the second derivative is the sign of
`c(B_0+4qt)^(3/2)/t-8A ln(2)`. Its first term strictly decreases in t,
since its derivative has the sign of `2qt-B_0<0`. Thus D_mm changes
sign at most once, from positive to negative. Also `D_m` tends to
negative infinity at zero, while `D_m(1/5)>0`: use
`B<=A<81/25`, `c<3/5`, and `log_2(4)=2` to bound the bracket below by
`4/3-6/5>0`. Consequently D_m crosses zero at most once, from negative
to positive. D has no interior maximum in m. Only four corners remain.

At the first corner, `D(0,0)=0`. Since
`h_2(1/5)=log_2(5)-8/5>18/25`, as certified by `5^25>2^58`,

$$
D(0,1/5)<\frac{2\sqrt{66}}5-
\frac{32\sqrt2}{25}-\frac{36}{25}<0.
$$

The last comparison reduces by squaring positive quantities to
`407<288sqrt(2)`, verified by `407^2<2(288)^2`.

At epsilon=`1/29`, (22) simplifies to

$$
D=2\sqrt B-2\sqrt2
-c[h_2(1/29)+(28/29)h_2(m)]-\frac1{\sqrt{2635}}.
$$

Here `h_2(1/29)>1/5`: `29^5>2^24` gives `log_2(29)>24/5`, while
`(29/28)^28>2` follows from its first three binomial terms,
`1+1+27/56>2`. With `140/99<sqrt(2)<99/70` and
`sqrt(2635)<52`, the remaining two corners have the rational certificates

$$
\begin{aligned}
D(1/29,0)
&<\frac{427}{145}-\frac{280}{99}-\frac{41}{350}-\frac1{52}
=-\frac{518051}{26126100}<0,\\
D(1/29,1/5)
&<\frac{486}{145}-\frac{280}{99}
-\frac{41}{70}\frac{649}{725}-\frac1{52}
=-\frac{2626291}{130630500}<0.
\end{aligned}
$$

The square-root bounds used here are `sqrt(1823)<427/10` and
`sqrt(58567)<243`; the corresponding values of B are `1823/841` and
`58567/21025`. Convexity in epsilon and the negative right endpoint
make (24) strict for every positive epsilon. By (22), this proves the
stated unbalanced-core gate for all eigenvectors, including the rank-one
core limit. It introduces no unsupported uniform entropy margin near a
pure state.

## 11. An explicit neighborhood of the entire rank-two boundary

The two preceding gates also permit an explicit uniform tail radius,
completing a quantitative step that was only existential in
[the earlier stability theorem](../LOW_RANK_ENTROPY_STABILITY.md).

First, every rank-two core satisfying `m>=1/5` and `g(sigma)<=10/3` has

$$\boxed{\Delta(\sigma)>\frac1{100}.}\tag{25}$$

This is a gap on the specified low-score core set. It is not a positive
gap for arbitrary rank-two states, which include equality states.

To prove (25), the spectral entropy margin delta from (3) is strictly
decreasing on `[1/5,1/2]`, apart from its zero derivative at the right
endpoint. Indeed, with `r=1-2m`,

$$
\delta'(m)=2r\left[
\frac{c}{\ln2}\frac{\operatorname{atanh}r}{r}
-\frac2{G_{\rm act}(m)}\right].
$$

The positive power series makes `atanh(r)/r` increasing. At `r=3/5`
it equals `(5/3)ln(2)`. Since `G_act<=2` and `c<3/5`, the bracket
is at most `(5/3)c-1<0`.

At `r=2/5`, the positive binary-entropy series gives

$$
1-h_2(3/10)
\le\frac{r^2/2+r^4/[12(1-r^2)]}{\ln2}
=\frac{26/315}{\ln2}
<\frac{520}{4347}<\frac3{25}.
$$

Here `ln(2)>69/100` follows already from the first two positive terms
`2(1/3+1/81)=56/81`. Consequently

$$
2\sqrt2+c h_2(3/10)-\frac{10}{3}
>\frac{28\sqrt2}{25}-\frac{118}{75}>\frac1{100}.
$$

The last inequality is equivalent to `sqrt(2)>475/336`, verified by
`475^2<2(336)^2`. Also `G(3/10)<10/3`, as follows from
`sqrt(2)<99/70<1061/750` after squaring positive sides.
For `m>=3/10`, entropy monotonicity and the low-score assumption now prove
(25). For `1/5<=m<=3/10`, the rank-two spectral theorem instead gives

$$
\Delta(\sigma)\ge\delta(m)\ge\delta(3/10)
>2\sqrt2+c h_2(3/10)-10/3>1/100.
$$

For an arbitrary orthogonal tail in (1), no compression-gap condition is
needed for the following rough continuity estimate. The off-diagonal block
of a sandwiched query is
`sqrt(epsilon(1-epsilon)) sqrt(sigma) U sqrt(tau)`, and Schatten
Holder gives `||sqrt(sigma) U sqrt(tau)||_1<=1`. The block triangle
inequality therefore yields

$$
\begin{aligned}
g(\rho)&\le(1-\epsilon)g(\sigma)+\epsilon g(\tau)
+8\sqrt{\epsilon(1-\epsilon)},\\
\Delta(\rho)&\ge(1-\epsilon)\Delta(\sigma)
+\epsilon\Delta(\tau)+c h_2(\epsilon)
-8\sqrt{\epsilon(1-\epsilon)}.
\end{aligned}
\tag{26}
$$

Both cores and tails have rank at most two, so the old rank-two theorem
still gives `Delta(tau)>=0`. If `0<epsilon<=2^(-20)`, then

$$
1-\epsilon\ge(2^{20}-1)\epsilon>640000\epsilon,
\qquad
\frac{1-\epsilon}{100}>8\sqrt{\epsilon(1-\epsilon)}.
$$

Equations (25)--(26) prove strict positivity for all low-score cores with
`m>=1/5` at that tail size. The high-score core theorem covers the
complementary score range; Section 10 covers `m<=1/5`. At epsilon=0
the old rank-two theorem applies. Thus **every complex two-qubit state**
with `lambda_3+lambda_4<=2^(-20)` satisfies the entropy bound.

The explicit radius is deliberately conservative. It does not overlap
with the proved upper-tail gate `epsilon>=1/29`, so it does not settle
the two-qubit conjecture. It places the remaining candidate region
strictly away from the rank-two boundary, as stated in (2).

## 12. Provenance and limits

Cheng--Hall's independent-setting monogamy and local-purity identity are
established inputs. The rank-two spectral theorem, entropy margin and SLD
envelope are prior repository deductions with their own source comparisons.
Block trace norms, cosine-sine decomposition, eigenvalue trace inequalities,
and rational interval arithmetic are standard tools. The supplied new
consequences are the complete exclusion of high-score top-two cores, including
nonflat spectra and arbitrary complex support rotations, and the separate
all-eigenbasis exclusion of normalized core spectra with m<=1/5. Their
combination with a uniform low-score core gap yields the explicit
two-qubit neighborhood `epsilon<=2^(-20)`. No new general
monogamy theorem or general numerical certification method is claimed.

The result narrows the remaining two-qubit problem rather than solving it.
A proof for cores with `g(sigma)<=10/3` and `m>1/5` in the remaining
tail window `2^(-20)<epsilon<1/29`, or an admissible violating state
there, is still required. Even a full two-qubit proof would leave the
all-n extension. Publication originality remains a separate unresolved
comparison, and this localization is not itself asserted to meet a journal's
novelty threshold. LICENSE and the historical initial audit are unchanged.
