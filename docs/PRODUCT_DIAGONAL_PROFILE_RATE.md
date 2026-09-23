# The complete product-diagonal profile rate

Date: 23 September 2026. Research base:
`3ebde02b2d9d5dcdcd0dd445e4a16b4f5aaf03b0`.

**Status:** supplied analytical deduction, independently reconstructed within
this workspace. This evaluates a defined family of collective encoders and
gives achievable upper bounds for the unrestricted problem. It does not
evaluate the unrestricted noisy-X/noisy-Z rate or certify publication novelty.

## 1. Restricted benchmark and statement

Keep the original task: one arbitrary unknown n-qubit specimen, one delayed
local X/Z query, free finite classical records, arbitrary input entanglement,
uniform operator identities for the requested contrasts, and a worst-case
quantum dimension cap on every branch.

Define the **product-diagonal Gram class** as instruments admitting a
refinement into single Kraus maps such that each nonzero normalized Gram
matrix `rho_a=K_a^dagger K_a/Tr(K_a^dagger K_a)` is diagonal in some tensor
product of one-qubit bases. The basis can depend on the branch, and the
eigenvalues can be arbitrarily correlated. The encoder and its decoder need
not factor across sites. This is a comparison class, not an assumption on
the unrestricted task.

Write

$$
f(v)=h_2\!\left(\frac{1-\sqrt{1-v^2}}2\right),\qquad 0\le v\le1.
\tag{1}
$$

Define a scalar cost `C(x,z)` on `[0,1]^2` as follows. Available profile-cost
points are

$$
(u,v,0)\quad(u,v\ge0,\ u^2+v^2\le1),
\qquad
(1,v,f(v)),\quad(v,1,f(v))\quad(0\le v\le1).
\tag{2}
$$

Take convex combinations of these points, allow either profile coordinate
to decrease, and minimize the cost needed to attain `(x,z)`. This minimum
defines C. The defining hull is compact, so the minimum exists; a finite
combination suffices. Equivalently, C is the lower convex, coordinatewise
nondecreasing envelope specified by (2). In particular `0<=C<=1`.

**Theorem 1.** Every interface in the product-diagonal Gram class with
profile `(x_i,z_i)` and worst-case output dimension D satisfies

$$
\boxed{\log_2D\ge\sum_{i=1}^n C(x_i,z_i).}
\tag{3}
$$

Let `q_PD(n;x,z)` denote the minimum integer qubit budget in this class
for a common X contrast x and common Z contrast z. Then

$$
\boxed{
R_{\rm PD}(x,z):=\lim_{n\to\infty}\frac{q_{\rm PD}(n;x,z)}n=C(x,z).
}
\tag{4}
$$

Thus C is also an achievable upper bound for the unrestricted profile
rate. It already includes the [exact-axis rate](EXACT_AXIS_RATE.md), but
mixing the two kinds of points in (2) gives stronger interior upper bounds
than merely degrading an exact-axis decoder.

The convexification in (2) is implemented by deterministic proportions of
input sites followed by compression and a recorded random permutation.
It is not an allowance to average the quantum dimension of different
physical branches.

## 2. Every one-qubit entropy profile is dominated by (2)

For a one-qubit state with Bloch vector r, direct two-by-two calculation
gives

$$
F_X^2=\|\sqrt\rho X\sqrt\rho\|_1^2=1-r_y^2-r_z^2,
\qquad
F_Z^2=1-r_x^2-r_y^2.
\tag{5}
$$

For a pair `(x,z)` outside the compatibility disk, the smallest entropy
of a single-qubit state with these exact scores is therefore

$$
\gamma(x,z)=h_2\!\left(\frac{1-\sqrt{2-x^2-z^2}}2\right).
\tag{6}
$$

Indeed, `|r|^2=2-x^2-z^2-r_y^2` is largest when `r_y=0`, and entropy
decreases with Bloch length. Choose
`r_x=sqrt(1-z^2), r_z=sqrt(1-x^2)` to attain (6). Profiles inside the
disk have zero minimum entropy: a pure Bloch vector with
`r_x=x, r_z=z, r_y=sqrt(1-x^2-z^2)` attains them.

Arbitrary rotations of a nonpure one-qubit seed do not add new extremal
points to the convexified entropy tradeoff. To prove this constructively,
put

$$
\phi(R)=h_2\!\left(\frac{1-\sqrt{2-R^2}}2\right),
\qquad 1\le R\le\sqrt2.
$$

This function is strictly concave. For `s=sqrt(2-R^2)` in `(0,1)`,

$$
\phi''(R)=-\frac{J(s)}{s^3\ln2},\qquad
J(s)=\frac{s(2-s^2)}{1-s^2}-2\operatorname{atanh}s.
$$

Here `J(0)=0` and

$$
J'(s)=\frac{s^2+s^4}{(1-s^2)^2}>0.
\tag{7}
$$

Concavity extends to the endpoints by continuity. Suppose `x>=z`,
`R=sqrt(x^2+z^2)>1`, and `x<1`. The ray through `(x,z)` joins the
compatible point `u=(x,z)/R` to the exact-X point `e=(1,z/x)`. With

$$
p=\frac{R-1}{R/x-1},\qquad 0<p<1,
$$

we have

$$
(x,z)=(1-p)u+p e,
\qquad
\gamma(x,z)=\phi(R)\ge p\phi(R/x)=p f(z/x).
\tag{8}
$$

The inequality is strict for the indicated interior segment. At `x=1`
the profile is already an exact-axis point; interchange X and Z when
`z>=x`. Thus every qubit profile can be reproduced from (2) with average
entropy no larger than the original qubit entropy. Conversely every point
in (2) is realized by a qubit state. This proves that C is exactly the
convexified minimum one-qubit seed entropy, including arbitrary rotations.

## 3. Correlated product-diagonal spectra cannot improve C

Let rho be diagonal in a fixed local product basis with probability law
`p(u_1,...,u_n)`. Its entropy is `H(p)`. Fix site i, condition on all other
coordinates y, and write

$$
m_y=p(0,y)+p(1,y),\qquad
\sigma_{i|y}=\frac{p(0,y)}{m_y}|0_i\rangle\langle0_i|
+\frac{p(1,y)}{m_y}|1_i\rangle\langle1_i|.
$$

Omit y with zero weight. Since each query acts on site i alone, its
sandwiched matrix is a direct sum of these two-dimensional edge blocks.
Therefore, for `b=X,Z`,

$$
F_i^b(\rho)=\|\sqrt\rho P_{i,b}\sqrt\rho\|_1
=\sum_y m_y F_b(\sigma_{i|y}).
\tag{9}
$$

The local eigenbasis is arbitrary, including axes with Y components.
Convexity of C and the qubit result give

$$
\begin{aligned}
C(F_i^X,F_i^Z)
&\le\sum_y m_y C(F_X(\sigma_{i|y}),F_Z(\sigma_{i|y}))\\
&\le\sum_y m_y S(\sigma_{i|y})
=H(U_i\mid U_{-i}).
\end{aligned}
$$

The Shannon chain rule and conditioning imply

$$
\boxed{
S(\rho)=H(p)\ge\sum_i H(U_i\mid U_{-i})
\ge\sum_i C(F_i^X,F_i^Z).
}
\tag{10}
$$

Now refine an admissible instrument as in the
[normalized-seed reduction](COLLECTIVE_ENCODING_REDUCTION.md). For nonzero
Kraus branches put `omega_a=Tr(K_a^dagger K_a)/2^n`, so `sum_a omega_a=1`.
Trace-norm duality gives

$$
x_i\le\sum_a\omega_a F_i^X(\rho_a),\qquad
z_i\le\sum_a\omega_a F_i^Z(\rho_a).
$$

Apply monotonicity and convexity of C, then (10), and finally the
branchwise rank bound:

$$
\sum_i C(x_i,z_i)
\le\sum_a\omega_a\sum_i C(F_i^X(\rho_a),F_i^Z(\rho_a))
\le\sum_a\omega_a S(\rho_a)\le\log_2D.
$$

This proves (3), even when each branch uses a different local product
basis. The omega weights are only an algebraic averaging device on the
maximally mixed test input. Every branch obeys the same quantum dimension
cap before averaging.

## 4. Achievability with a fixed quantum dimension

The class is closed under concatenating encoders on disjoint sites, so
`q_PD(n+m;x,z)<=q_PD(n;x,z)+q_PD(m;x,z)`. Retaining all sites is allowed.
Fekete's lemma consequently gives existence of the rate and its equality
to the infimum of finite-block ratios.

First suppose `x,z<1`. Fix arbitrarily small positive contrast and rate
slack. The finite convex function C is continuous in the interior of the
square. Choose a profile slightly above `(x,z)` in both coordinates,
with cost arbitrarily close to `C(x,z)`. For coordinates equal to zero,
either use the zero-memory compatibility disk directly or work at a
nearby interior point. Approximate a minimizing finite mixture in (2)
by rational weights while retaining some of the contrast slack.

Make a deterministic block of qubit Gram states in these rational
proportions. Its entropy is the sum of their entropies, and its average X
and Z scores are the corresponding mixture coordinates. Take virtual
tensor powers of this auxiliary block seed and project its Schmidt
coefficients onto a typical set, as in
[the entropy-rate proof](ENTROPY_RATE_CHARACTERIZATION.md), Section 4.
The new normalized seed has fixed rank at most
`2^{M(S_block+tau)}` and loses at most `2sqrt(epsilon_M)` in each original
query score, with `epsilon_M -> 0`.

The truncation is diagonal in the original product eigenbasis. Thus the
new Gram matrix still belongs to the product-diagonal family, although its
eigenvalues are now correlated. A complete Pauli orbit makes the seed a
trace-preserving instrument. Average site permutations, storing their
labels classically, to equalize X scores across sites and Z scores across
sites separately. Do not swap X and Z. Pauli conjugations and permutations
preserve the product-diagonal Gram condition.

For sufficiently large M both equalized contrasts exceed x,z; independent
output flips tune them down to the exact prescribed values. Every
physical branch has the fixed typical rank cap. This achieves cost C after
letting the slacks vanish. Typicality refers to virtual seed coefficients,
not copies of the physical unknown specimen or successful postselection.

Boundary points require no continuity assumption about exact readout.
In a mixture attaining `x=1`, every participating profile must have X
coordinate one. The only available atoms are the exact-X curve, including
its endpoints. Convexity of f gives `C(1,z)=f(z)`. The complete diagonal
truncation construction in [EXACT_AXIS_RATE.md](EXACT_AXIS_RATE.md) preserves
X exactly at every finite block and attains this rate within the present
class. The boundary `z=1` is symmetric. The compatibility disk has exact
zero-memory protocols, and `(1,1)` requires and permits all n qubits.
This completes (4) on the whole square.

## 5. Exact support function and comparison with site retention

Let

$$
f^*(b)=\max_{0\le v\le1}\{bv-f(v)\},\qquad b\ge0.
\tag{11}
$$

For weights `a>=b>=0`, the exact entropy-penalized support of (2) is

$$
\boxed{M(a,b)=\max\{\sqrt{a^2+b^2},\ a+f^*(b)\}.}
\tag{12}
$$

Indeed, the disk has support `sqrt(a^2+b^2)`. At equal v the exact-X
point has weighted score at least that of the exact-Z point, since
`(a+bv)-(b+av)=(a-b)(1-v)>=0`. Maximizing the exact-X score minus entropy
gives the second term. Interchange a,b otherwise. Consequently

$$
C(x,z)=\sup_{a,b\ge0}\{ax+bz-M(a,b)\},
\tag{13}
$$

with the symmetric definition of M understood. This is ordinary convex
duality for the closed, downward profile hull and upward cost epigraph.
Nonnegative weights suffice because C is coordinatewise nondecreasing.

The scalar maximization in (11) is unambiguous. The
[exact-axis note](EXACT_AXIS_RATE.md) proves that f is strictly convex,
`f'(0)=0`, and `f'(1)=1/ln2`. Hence

$$
f^*(b)=b-1\quad\text{if }b\ge1/\ln2;
$$

for `0<b<1/ln2`, its unique maximizer lies in `(0,1)` and solves `f'(v)=b`.
In that interval `f^*(b)>b-1`.

Recall the exact original-site-retention cost

$$
w(x,z)=[x+z-1-\sqrt{2(1-x)(1-z)}]_+.
$$

Its convex construction uses just the free disk and `(1,1,1)`, so
`C(x,z)<=w(x,z)` everywhere. The following identifies exactly where
enlarging that construction to the full exact-axis curve improves it.

**Theorem 2.** Put

$$
\tau_*=2(1/\ln2-1)^2=0.39195779845536194\ldots.
\tag{14}
$$

For `0<z<=x<1` outside the compatibility disk,

$$
\boxed{
C(x,z)<w(x,z)
\quad\Longleftrightarrow\quad
\frac{1-x}{1-z}<\tau_*.
}
\tag{15}
$$

There is equality at and above the threshold. Interchange x,z for the
other half of the square. Both costs vanish inside and on the disk.
At `x=1, 0<z<1`, strictness is `f(z)<z`; at `(1,1)` both costs equal one.

To prove (15), outside the disk the gradient of w is

$$
A=1+\sqrt{\frac{1-z}{2(1-x)}},\qquad
B=1+\sqrt{\frac{1-x}{2(1-z)}},\qquad A\ge B.
$$

Direct algebra gives

$$
\sqrt{A^2+B^2}=A+B-1,\qquad
Ax+Bz-(A+B-1)=w(x,z).
\tag{16}
$$

If `B>=1/ln2`, (12) has `M(A,B)=A+B-1`, so (13) proves `C>=w` at this
point, and equality follows. This is exactly the weak inequality opposite
to the right side of (15).

If `B<1/ln2`, some exact-X atom `(1,v,f(v))` lies strictly below this
retention supporting plane, because `Bv-f(v)>B-1`. Suppose nevertheless
that `C(x,z)=w(x,z)`. A subgradient of the finite convex function C exists
at this interior point. Since `C<=w` everywhere and w is differentiable
here, every such subgradient must be `(A,B)`: its supporting plane for C
would also support w at the contact point. This is impossible at the
displayed exact-X atom. Thus `C<w`, proving strictness.

For common accuracy the point lies in the equality region. In particular

$$
\boxed{
C(\eta,\eta)
=\left[\frac{2\eta-\sqrt2}{2-\sqrt2}\right]_+.
}
\tag{17}
$$

Thus all product-diagonal spectra, arbitrary rotations of qubit seeds,
and their convex combinations give exactly the subset common-accuracy
rate. The unrestricted common-accuracy rate is still open.

## 6. A fully specified interior improvement

Take a proportion `87/100` of exact-axis seed blocks with profile
`(1,15/29)` and a proportion `13/100` with the compatible profile
`(12/13,5/13)`. The latter lies exactly on the unit circle. Their averaged
profile is exactly

$$
\frac{87}{100}(1,15/29)
+\frac{13}{100}(12/13,5/13)=(99/100,1/2).
$$

The fixed-dimension construction in Section 4 consequently gives

$$
\begin{aligned}
R(99/100,1/2)
&\le C(99/100,1/2)\\
&\le\frac{87}{100}f(15/29)
=0.32506602063355716\ldots.
\end{aligned}
\tag{18}
$$

Here R denotes the unrestricted common-across-sites profile rate. The
exact expression in (18), rather than a numerical optimizer, specifies
the construction. The earlier exact-axis-plus-decoder-noise bound was
`f(1/2)=0.3545789026652717...`; one directly rotated qubit seed gives
`gamma(.99,.5)=0.3325062937559609...`. Original-site retention requires
`w(.99,.5)=.39` exactly. Thus (18) improves both explicit collective
upper bounds while remaining a statement about one delayed query on one
arbitrary specimen. No unrestricted interior optimality is asserted.

These strict comparisons do not depend on the displayed decimals. Here
is one conservative elementary certificate. For
`a=(1-sqrt(1-(15/29)^2))/2`, squaring gives `a<721/10000=:a_0`.
The entropy bound

$$
h_2(a)\le\frac{-a\ln a+a-a^2/2}{\ln2}
$$

follows from the power series of `-(1-a)ln(1-a)`. Use
`ln(1/a_0)<8/3` and `ln2>693/1000` to obtain

$$
\frac{87}{100}f(15/29)
<\frac{87}{100}
\frac{(11/3)a_0-a_0^2/2}{693/1000}
=\frac{650679119}{1980000000}<\frac{33}{100}.
$$

For the direct rotated seed, its smaller eigenvalue is greater than
`p=153/2500`, again by squaring. Since `p<1/16`,
`-log_2 p>4`. The inequalities `-ln(1-p)>=p+p^2/2` and `ln2<694/1000`
then give

$$
\gamma(99/100,1/2)
>4p+\frac{p-p^2/2-p^3/2}{694/1000}
=\frac{7159495923}{21687500000}>\frac{33}{100}.
$$

Also `gamma(99/100,1/2)<f(1/2)` by strict monotonicity of f, because its
argument is `sqrt(2301)/100<1/2`. The elementary logarithm bounds used
above follow, for example, from the series
`ln2=2 sum_{k>=0} 1/((2k+1)3^(2k+1))` and
`exp(8/3)>sum_{k=0}^6 (8/3)^k/k!>10000/721`.

## 7. Ingredients and novelty boundary

The compatibility disk and exact-axis scalar curve are established
ingredients, with primary-source comparisons in the
[allocation-region note](ONE_QUBIT_ALLOCATION_REGION.md) and
[exact-axis rate note](EXACT_AXIS_RATE.md). The qubit entropy formula,
convexification, Shannon conditioning, and Schmidt typicality are likewise
standard mathematical tools. The supplied additions here are the complete
profile benchmark for the specified product-diagonal Gram class, its
support formula, the exact region (15) where it improves original-site
retention, and the explicit interior construction.

The one-qubit cost C also evaluates an established resource quantity.
For the qubit steering assemblage

$$
\sigma_{\pm|X}=(I\pm xX)/4,\qquad
\sigma_{\pm|Z}=(I\pm zZ)/4,
$$

we have `C(x,z)=E_FA(sigma)`, where E_FA is Cope's entanglement of
formation for assemblages,
[arXiv:2102.02333v2](https://arxiv.org/pdf/2102.02333v2), Eq. (10) and
Theorem 2, printed p. 3. This identification follows directly in both
directions. In any convex decomposition of the assemblage, each component
has a qubit marginal rho and can be realized by measurements on a
purification of rho. Its X/Z coefficients are bounded by the two
trace-norm scores of rho. Convexity and monotonicity of C therefore bound
the average marginal entropy below by C. Conversely, the complete Pauli
orbit of any qubit seed produces the corresponding noisy-Pauli assemblage
with average component entropy `S(rho)`; convex combinations give all
points defining C. Refining a component into extremal assemblages cannot
increase its average marginal entropy, by entropy concavity, so this
argument also respects Cope's extremal-component definition. Thus no new
entropy resource is being defined here. The fixed-cap multi-input result
(4) additionally requires the product-diagonal converse and the complete
encoding construction proved above.

The product-diagonal condition cannot be removed by diagonalizing a
general seed: an arbitrary eigenbasis need not be a tensor product of
local bases, and then the edge decomposition (9) is unavailable. General
separable Gram states also need not be product diagonal. Nothing here
establishes the conjectured unrestricted sharp entropy inequality or
its failure. Publication novelty of this operational specialization
remains under primary-source comparison.
