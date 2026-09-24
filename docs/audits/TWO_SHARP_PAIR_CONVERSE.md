# Two sharp anticommuting pairs and an arbitrary third pair

**Research base:** main `9fc2be03587986d85341aa3f766653e6ba94bb75`.
**Date:** 24 September 2026.

For a four-dimensional retained memory, two internally anticommuting
sharp readout pairs and an arbitrary third binary pair obey the retention
operator bound `4+sqrt(2)`. The two sharp pairs need not commute with each
other or define complementary memory subsystems.

The proof combines the exact last-readout formula with the new spectral
circle and Schmidt-tail constraints. All remaining dependence reduces
to one scalar parameter. Two explicit scalar upper bounds are certified
on its complete interval using rational interval arithmetic.

**Status:** supplied proof independently reconstructed within this workspace,
with an exact finite scalar certificate.
Publication originality and significance remain unresolved. The theorem
does not cover arbitrary earlier Jordan angles, including equal but
nonright block angles,
all three remaining complete reflection signatures, or the unrestricted
three-input optimum. The finite certificate proves sufficient scalar
inequalities; it is not a numerical claim that an optimizer found the
global maximum.

## 1. The operator theorem

Let R1,R2,R3 be qubits and Q have dimension four. Set

\[
H=\sum_{i=1}^3(X_i\otimes B_i+Z_i\otimes D_i).
\]

For i=1,2 suppose B_i,D_i are Hermitian reflections with
`{B_i,D_i}=0`. Let B_3,D_3 be arbitrary Hermitian contractions. Then

\[
\boxed{\|H\|\le4+\sqrt2.}
\tag{1}
\]

The constant is attained: identify Q=A tensor B, use X_A,Z_A for
the first pair and X_B,Z_B for the second, and put B_3=D_3=I_Q.
The Hamiltonian is then the sum of two commuting Bell Hamiltonians
and the independent reference field X_3+Z_3. Its largest eigenvalue
is `2+2+sqrt(2)`. This establishes sharpness of the operator constant;
it does not by itself claim that this fixed choice of sharp sites is a
uniform-accuracy interface protocol.

## 2. Keep the actual top state and enlarge only the lower spectrum

Write r=sqrt(2), Lambda=4+r, and

\[
H_0=X_1\otimes B_1+Z_1\otimes D_1
   +X_2\otimes B_2+Z_2\otimes D_2.
\]

Let U,m be its two largest eigenvalues, with multiplicity. If U<=2+r,
the third pair has norm at most two, proving the desired upper bound.
It therefore suffices to treat `2+r<U<=4`.

The [sharp-pair constraints](SHARP_PAIR_SCHMIDT_TAIL.md), Section 4,
give m>=2 and

\[
(U-2)^2+(m-2)^2\le4.
\]

Define

\[
M(U)=2+\sqrt{4-(U-2)^2}.
\tag{2}
\]

Then `m<=M(U)<U`, so the top vector Omega is unique, and

\[
H_0\le M I+(U-M)|\Omega\rangle\langle\Omega|.
\tag{3}
\]

This is an operator ordering: increasing the lower-spectrum cap from m
to M adds `(M-m)(I-|Omega><Omega|)>=0`. No monotonicity inferred from a
numerical plot of the resolvent expression is used.

Let rho be Omega's actual memory marginal, with ordered eigenvalues
lambda_1,...,lambda_4, and put tau=lambda_3+lambda_4. The already
proved necessary conditions imply

\[
\begin{aligned}
\tau&\ge\frac{U-3}{U+M},\\
\lambda_1&\le\frac{2+M}{U+M},\\
E_*(\lambda)&\le e(U):=2+U-\frac38U^2.
\end{aligned}
\tag{4}
\]

The first lower bound becomes weaker when m increases to M; the second
upper bound increases because U>2. The six-Pauli condition for E_* is
independent of m. It is proved in the
[joint-spectrum report](JOINT_SPECTRUM_NORMAL_FORM.md), Section 6.
Thus (4) continues to hold for the same actual marginal after (3).

Set

\[
c=U-M>0,\qquad t=\Lambda-M\in(2,2+r].
\tag{5}
\]

By the [exact last-readout theorem](EXACT_LAST_QUERY_RESOLVENT.md),
Section 6, it suffices to prove

\[
c\left[\Phi_t(\lambda_1,\lambda_4)
       +\Phi_t(\lambda_2,\lambda_3)\right]\le1.
\tag{6}
\]

That theorem permits all third-pair Hermitian contractions. Equation (6)
controls the rank-one envelope (3), and hence the original Hamiltonian.

## 3. Three scalar branch patterns suffice

For the block functions in the last-readout theorem define

\[
s=\frac1{t-r},\qquad
F=\frac1{2(\sqrt{2t^2-4}-t)},\qquad
G=\frac{t+1}{t(t+2)}.
\tag{7}
\]

On `1<=a<=r`, with b=sqrt(2-a^2), the exact block eigenvalues are
`f_a=(t-a)/((t-a)^2-b^2)` and
`g_a=(t+a)/((t+a)^2-b^2)`. Differentiation gives

\[
\operatorname{sign}f_a'
=\operatorname{sign}(t^2-4ta+2a^2+2),\qquad g_a'<0.
\]

The unique maximum of f_a occurs at
`a=t-sqrt((t^2-2)/2)` in [1,r], and evaluates to F. The maximum
of g_a occurs at a=1 and equals G. In particular F>=s>G, since
`f_r=s` and `G<1/t<s`. Hence

\[
\Phi_t(x,y)\le\max\{s(x+y),Fx+Gy\}\qquad(x\ge y\ge0).
\tag{8}
\]

Put alpha=F-s>=0 and beta=s-G>0. Expanding the two maxima in
(8) and using the ordering of lambda gives

\[
\begin{aligned}
\Phi_t(\lambda_1,\lambda_4)+\Phi_t(\lambda_2,\lambda_3)
\le\max\{&s,\ F(1-\tau)+G\tau,\\
          &s+\alpha\lambda_1-\beta\lambda_4\}.
\end{aligned}
\tag{9}
\]

Indeed, if exactly one pair uses its block branch, choosing the outer
pair is at least as large as choosing the inner pair. This uses
alpha,beta>=0, lambda_1>=lambda_2, and lambda_3>=lambda_4.

The scalar branch causes no problem:

\[
cs=\frac{U-M}{4-M}\le1,
\tag{10}
\]

because U<=4. The remaining two branches have useful spectral bounds.

## 4. Bound the two nontrivial branches

Recall

\[
E_*=k_{12}+k_{13}+k_{24}+k_{34},\qquad
k_{ij}=\frac{(\lambda_i-\lambda_j)^2}{\lambda_i+\lambda_j},
\]

with a zero-over-zero term defined as zero. Cauchy--Schwarz on the
13 and 24 edges gives

\[
E_*\ge k_{13}+k_{24}\ge(1-2\tau)^2.
\tag{11}
\]

Together with (4), this yields

\[
\tau\ge T(U):=\max\left\{
0,\frac{U-3}{U+M},\frac{1-\sqrt e}{2}\right\}.
\tag{12}
\]

Since F>G, the block-block branch in (9), multiplied by c, is at most

\[
\mathcal A(U)=c\,[F-(F-G)T(U)].
\tag{13}
\]

For the mixed branch, (4) immediately gives

\[
\mathcal B_1(U)=c\left[s+\alpha\frac{2+M}{U+M}\right].
\tag{14}
\]

There is also a bound that is useful near U=4. Since each pair sum is
at most one, E_* is at least the unweighted squared-difference sum on
the four-cycle with edges 12,13,24,34. That cycle's Laplacian has gap
two on the subspace of zero-sum vectors. Consequently

\[
E_*\ge2\sum_{j=1}^4(\lambda_j-1/4)^2.
\tag{15}
\]

Projecting the coefficient vector `(alpha,0,0,-beta)` onto that subspace
and using Cauchy--Schwarz gives the second mixed-branch bound

\[
\mathcal B_2(U)=c\left[
s+\frac{\alpha-\beta}{4}
\,+\sqrt{\frac e2}
\sqrt{\alpha^2+\beta^2-\frac{(\alpha-\beta)^2}{4}}
\right].
\tag{16}
\]

Thus (6) follows from the two one-variable inequalities

\[
\boxed{\mathcal A(U)\le1,\qquad
\min\{\mathcal B_1(U),\mathcal B_2(U)\}\le1}
\quad(2+r<U\le4).
\tag{17}
\]

## 5. Exact scalar certification

The expressions in (17) have a removable endpoint singularity because
F diverges as U approaches 2+r while c tends to zero. The certificate
uses the products cF,cG,cs directly, after rationalizing cF, and a rational
parameterization of the spectral circle. Put

\[
x\in[0,1],\quad z=(r-1)x,\quad
U=\frac4{1+z^2},\quad M=2+\frac{4z}{1+z^2},\quad
t=2+r-\frac{4z}{1+z^2}.
\tag{18}
\]

This covers the full arc from `(U,M)=(4,2)` to `(2+r,2+r)`.
For stable nonnegative interval factors use

\[
c=\frac{2(r-1)(1-x)(r+1+z)}{1+z^2},\qquad
L=\frac{r(r+1+z)}{r+1-z}.
\tag{19}
\]

For x<1, `L=c/(t-2)`; the displayed expression supplies its continuous
endpoint value. The scaled quantities are

\[
\begin{aligned}
\widehat F&=\frac{L(\sqrt{2t^2-4}+t)}{2(t+2)}=cF,\\
\widehat G&=\frac{c(t+1)}{t(t+2)}=cG,\\
\widehat S&=\frac c{t-r}=cs,\\
e&=\frac{4z^2}{1+z^2}\frac{3U+4}{8}.
\end{aligned}
\tag{20}
\]

The last identity uses `e=(4-U)(3U+4)/8`, avoiding subtraction at U=4.
At x=1 the continuous values are `widehat F=1`, `widehat G=widehat S=0`.
The original Hamiltonian at this endpoint was already handled by the
triangle inequality; including it in the certificate is a convenient
closed-interval extension.

Write `kappa=(2+M)/(U+M)`, `a=widehat F-widehat S`, and
`b=widehat S-widehat G`. Both a and b are nonnegative. The expressions
to certify are exactly

\[
\begin{aligned}
\mathcal A&=\widehat F(1-T)+\widehat G T,\\
\mathcal B_1&=\widehat F\kappa+\widehat S(1-\kappa),\\
\mathcal B_2&=\frac{\widehat F+2\widehat S+\widehat G}{4}
 +\sqrt{e/2}\sqrt{\frac34(a^2+b^2)+\frac12ab}.
\end{aligned}
\tag{21}
\]

The [exact verifier](../../tools/check_two_sharp_pair_converse.py)
partitions [0,1] into the 400 closed cells `[j/400,(j+1)/400]`.
All interval endpoints and arithmetic operations use exact rational
numbers. Square roots are enclosed outward with denominator `D=10^35`:
for a nonnegative rational q, set

\[
k=\left\lfloor\sqrt{\lfloor qD^2\rfloor}\right\rfloor,
\qquad k/D\le\sqrt q\le(k+1)/D.
\]

The integer square root computes k exactly. This encloses sqrt(2) as
well as every later radical. The verifier checks positive denominators,
nonnegative square-root arguments, and the needed interval ordering.

Within each cell it takes a lower bound on T, upper bounds on
`widehat F,widehat G,widehat S`, and an upper bound on kappa clipped
at one. The checked upper-endpoint inequalities
`widehat F_hi>=widehat G_hi` and
`widehat F_hi>=widehat S_hi` justify the two interpolation bounds
in (21). For the moment bound, the radical is monotone in nonnegative
a,b, so individual upper bounds suffice. The smaller of the two
resulting mixed-branch upper bounds is valid on the entire cell.

Every cell passes the exact rational assertions

\[
\mathcal A\le999/1000,\qquad
\min(\mathcal B_1,\mathcal B_2)\le999/1000.
\tag{22}
\]

The [recorded result](../../results/two_sharp_pair_converse.json) gives
the following rational ceilings on the largest cell upper bounds:

| Branch | Certified upper ceiling | Cell index, starting at zero |
|---|---:|---:|
| Both block branches | 950194781/1000000000 | 298 |
| One block branch | 498252169/500000000 | 198 |

The capped mixed bound is selected on 201 cells and the moment bound on
199. These are bounds on complete cells, not evaluations at selected
points. All arithmetic that certifies (22) is rational or integer; no
floating-point optimizer, sampling assumption, or numerical optimality
claim enters the proof. The checker also rejects execution with Python
assertions disabled. Independent internal reruns reproduced the result.

Equations (10) and (22) establish (17), and thus (6). The nonscalar
branches have a strict certified margin; the scalar branch can saturate
at U=4, consistently with the operator attainer in Section 1.

## 6. Scope and operational interpretation

The upper bound follows from (3)--(17). Conjugating all three references
by Y sends H to -H, giving the matching lower bound and proving the
operator norm statement (1).

The result applies to every normalized seed and every actual decoder
family with two internally anticommuting sharp pairs. The memory
orientations and classical branches may vary freely. No commutation
between different pairs, no preassigned decomposition into retained
qubits, and no real-matrix assumption is imposed.

To transfer the theorem to a trace-norm optimized seed, its optimizing
decoder family must satisfy this sharpness hypothesis; the existence of
such a family for every seed is not assumed. General nonorthogonal
pairs, including equal nonright or unequal Jordan-block angles, and the
remaining complete reflection signatures
therefore remain open. The physical model still uses one unknown
specimen and one delayed query, with no extra copy, quantum bypass,
free entanglement, postselection, or average-memory substitution.

The ingredients in the argument include established Pauli and projector
algebra, spectral interlacing, and Cauchy--Schwarz. The prior reports give
the exact resolvent formula and the supplied sharp-pair constraints.
The present result is their deduction for this complete sharp-pair
family. Its publication priority has not been settled.
