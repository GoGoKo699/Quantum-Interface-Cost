# Exact last-query optimization with a Jordan-block budget

Research base: `556df48950c2de3162171dd1d85c3df9e5937fc2`.
Date: 27 September 2026.

**Status:** supplied analytical theorem, independently reconstructed within
this workspace. This is internal review, not external peer review or a
claim of publication priority.

Let rho be a density matrix on memory Q of dimension M>=2, with ordered
eigenvalues lambda_1>=...>=lambda_M. For t>2 write r=sqrt(2), s=1/(t-r).
For 1<=a<=r set b=sqrt(2-a^2),

```math
f_a=\frac{t-a}{(t-a)^2-b^2},\qquad
g_a=\frac{t+a}{(t+a)^2-b^2},
```

and use the [previously proved scalar function](EXACT_LAST_QUERY_RESOLVENT.md#1-the-readout-elimination-theorem)

```math
\Phi_t(x,y)=\max\left\{s(x+y),\max_{1\le a\le r}(xf_a+yg_a)\right\},
\qquad x\ge y\ge0.
```

Extend Phi and the gain G below symmetrically to unordered arguments.

Define the rho-weighted last-query resolvent on a reference qubit by

```math
R_t(\rho;B,D)=\operatorname{Tr}_Q\left[
(I\otimes\sqrt\rho)(tI-X\otimes B-Z\otimes D)^{-1}
(I\otimes\sqrt\rho)\right].
```

The structural theorem fixes how many noncommuting two-dimensional Jordan
blocks the last reflection pair may use. For an integer
0<=k<=floor(M/2), let F_k be the supremum of the operator norm of R_t over
all reflection pairs with at most k such blocks, allowing arbitrary scalar
signs on the complement. Define the nonnegative block gain

```math
G_t(x,y)=\Phi_t(x,y)-s(x+y).
```

Then its exact optimal resolvent is

```math
\boxed{F_k(t,\rho)=s+
\sum_{j=1}^{k}G_t(\lambda_j,\lambda_{M+1-j}).}
\tag{1}
```

The k outermost eigenvalue pairs are optimal. This works in odd and even
memory dimension, and each added block has no larger gain than the
previous one. The integer k is a readout Jordan-block count, not the
physical retained-qubit budget. The result eliminates the decoder
optimization; it does not establish the unrestricted interface converse.

Sections 1--2 prove (1); Section 3 gives its particularly short one-block
comparison, and Section 4 retains the fixed minority ranks `(11)`.

## 1. The one-block theorem

Take the supremum over all reflection pairs (B,D) with at most one
noncommuting two-dimensional Jordan block, allowing arbitrary scalar
signs on its complement and allowing commuting pairs. Then

```math
\boxed{
F_{\rm one}(t,\rho)
=(1-\lambda_1-\lambda_M)s+\Phi_t(\lambda_1,\lambda_M).
}
\tag{2}
```

The formula is valid in odd and even memory dimension. It depends only
on the largest and smallest memory eigenvalues. Both orientations and
all middle/negative eigenvalues of the active-block Hamiltonian have been
retained before optimization. The same supremum holds for Hermitian
contraction pairs admitting a joint block decomposition with at most one
block of dimension two and all other blocks scalar.

### Proof

For a reference pure state chi, compress the full resolvent to its
expectation on chi. A scalar Jordan block has readout signs (epsilon,eta)
and contributes

```math
\frac{t+\epsilon\langle X\rangle_\chi+
\eta\langle Z\rangle_\chi}{t^2-2}\le s.
```

On a noncommuting two-dimensional block, the
[exact block calculation](EXACT_LAST_QUERY_RESOLVENT.md#3-one-jordan-block-has-an-exact-two-eigenvalue-description)
gives two eigenvalues whose vector is majorized by (f_a,g_a) for some
a in [1,r]. This is because the trace of the compressed block resolvent
does not depend on chi, while its eigenvalue spread is largest on the
bisector corresponding to the larger of the two Jordan coefficients.
Both f_a and g_a are the exact resolvent eigenvalues, not a spectral
majorant of the local Hamiltonian.

Increasing every scalar complement eigenvalue to s and maximizing the
active eigenvalue spread gives an upper bound under trace rearrangement
against ordered nonnegative lambda. The resulting full spectrum is

```math
\{f_a,g_a,s,\ldots,s\}.
```

Always g_a<1/t<s: the first inequality is equivalent to
a(t+a)>b^2, which follows from a>=1, t>2, and b^2<=1.
If f_a<=s, every eigenvalue is at most s, so the resulting
weighted sum is at most the all-scalar value s. If f_a>=s, rearrangement
assigns lambda_1 to f_a and lambda_M to g_a; all other weights receive s.
Hence the largest possible gain above s is exactly

```math
\max\{0,\max_a[\lambda_1(f_a-s)+\lambda_M(g_a-s)]\},
```

which is (2).

For attainment of a positive gain, choose the active plane spanned by
eigenvectors for lambda_1 and lambda_M, use active readouts

```math
B=(aZ+bX)/\sqrt2,\qquad D=(aZ-bX)/\sqrt2,
```

and put B=D=I on the scalar complement. At the single common reference
state (X+Z)/sqrt(2)=+1, the active eigenvalues are f_a,g_a and all scalar
entries are s. A zero maximal gain is attained by B=D=I everywhere.
Compactness gives attainment of the maximizing active parameter a.

For contraction pairs with the stated fixed block decomposition, decompose
both contractions into reflection vertices in that same block algebra.
Operator convexity of the inverse, positivity of the rho-weighted trace,
and convexity of the largest eigenvalue reduce the supremum to reflections
without increasing the number of two-dimensional blocks. Reflection
attainment proves that the supremum remains exactly (2).

## 2. The exact block-budget theorem

We now prove (1) for an arbitrary allowed block count k. Apply Section 1's
block compression to each active block. Full memory trace rearrangement
then assigns disjoint pairs of eigenvalue weights to the active planes.
Relative to the all-scalar value s, each plane's gain is at most
G_t(x,y)=Phi_t(x,y)-s(x+y). Every such partial matching is simultaneously
attainable, with zero-gain planes replaced by scalar readouts.

This k is a Jordan-block count in a proof optimization, not the physical
retained-qubit budget of the interface model.

The [proved decreasing-differences inequalities](EXACT_LAST_QUERY_RESOLVENT.md#4-pair-the-extreme-eigenvalues) for Phi also hold
for G, because subtracting s(x+y) cancels in each four-point inequality.
On ordered x>=y, G is nondecreasing in x and nonincreasing in y. To see
this, terms with f_a<=s cannot give a positive gain; all remaining gain
terms have coefficient f_a-s>0 on x and g_a-s<0 on y. Taking their maximum
with zero preserves both monotonicities.

Because G is nonnegative, extend any partial matching to exactly k selected
pairs without reducing its gain. For k>0 force the largest and smallest
remaining eigenvalues into the same pair. If only one extreme is unpaired,
replace the other endpoint of the pair containing the paired extreme.
If both extremes are unpaired, replace any selected pair by them. Both
operations increase or preserve the gain by the preceding monotonicity.
If the extremes belong to different pairs, the four-point inequality
uncrosses those pairs without reducing their total gain. If they are
already paired, nothing changes. Fix this extreme pair and repeat on the
remaining k-1 selected pairs. This gives the k outermost pairs while
preserving the selected count. Zero-gain pairs can be realized by scalar
readouts, so the value covers fewer than k genuinely active blocks as well.

The gain sequence is nonincreasing, because its larger argument decreases
and its smaller argument increases with j. Each pair's optimum can be
realized at the same reference bisector,
with all remaining directions scalar. This proves (1). At k=floor(M/2)
it recovers the existing unrestricted even-dimensional theorem and adds
the unpaired middle scalar contribution when M is odd.

The same fixed-block-algebra convexity argument as in Section 1 includes
contraction pairs admitting at most k common blocks of dimension two,
with scalar remaining blocks. At k=floor(M/2), independent reflection
extremization additionally covers every unrestricted contraction pair,
whether or not the original contractions have such a joint decomposition.

## 3. One cubic-root comparison

To compare F_one against a threshold T, put x=lambda_1, y=lambda_M and
K=T-(1-x-y)s. The [exact scalar test](EXACT_LAST_QUERY_RESOLVENT.md#5-exact-algebraic-test-for-the-scalar-function) for Phi_t(x,y)<=K applies:
first K>=s(x+y), equivalently T>=s, and then minimize the strictly convex
quartic

```math
P_K(a)=4Ka^4+2da^3-8Ka^2-d(t^2+2)a
+K(t^2-2)^2-wt(t^2-2),
\quad w=x+y,\quad d=x-y.
```

The quartic's unique minimum on [1,r] occurs at min{z,r}, where z>=1 is the unique
positive root of

```math
16Kz^3+6dz^2-16Kz-d(t^2+2)=0.
```

Since lambda_1>0 for a density operator, the scalar-branch condition gives
K>0 and strict convexity is automatic. There is no memory-matrix
optimization left: one scalar-branch test and one cubic-root sign test
are necessary and sufficient for the one-block resolvent bound.

For an earlier Hamiltonian with unique leading eigenvalue U, second
eigenvalue m<Lambda-2, and actual top-vector memory marginal rho, the
[rank-one envelope](EXACT_LAST_QUERY_RESOLVENT.md#6-exact-test-for-a-rank-one-spectral-upper-bound)

```math
H_0\le mI+(U-m)|\Omega\rangle\langle\Omega|
```

passes every one-block last pair exactly when

```math
(U-m)F_{\rm one}(\Lambda-m,\rho)\le1.
```

This equivalence concerns the envelope, not the original Hamiltonian.
Strictly positive denominators alone do not imply that it passes.

## 4. Fixed `(11)` signature refinement

For M=4, require both reflection minority ranks to equal one. After
independent overall signs, B=I-2|u><u| and D=I-2|v><v|, so their scalar
complement necessarily has B=D=I. Define Psi_t(x,y)=max_a(xf_a+yg_a),
omitting the all-scalar branch from Phi. Then the exact fixed-signature
value is

```math
\boxed{
F_{11}(t,\rho)=\max\left\{
(\lambda_2+\lambda_3)s+\Psi_t(\lambda_1,\lambda_4),\quad
(\lambda_1+\lambda_2)s+\Psi_t(\lambda_3,\lambda_4)
\right\}.}
\tag{3}
```

The derivation is the same spectrum sorting, but the all-scalar value is
no longer freely available. When f_a>=s the active large eigenvalue gets
lambda_1, and when f_a<=s it gets lambda_3. In either case g_a gets lambda_4.
The maximum of the two linear assignments implements both cases exactly.
Either assignment is attained by choosing its two specified eigenvectors
as the active plane and using the explicit reflections of Section 1;
both reflections have exactly one minority eigenvalue.

There is one additional orientation point for this fixed signature.
If the coefficient of (X+Z)/sqrt(2) is smaller than the coefficient of
(X-Z)/sqrt(2), interchange the two coefficients in the active pair. This
is another allowed rank-(11) pair. It preserves the active resolvent trace
and maximal spread, while arranging the maximum at the same bisector as
the scalar complement. Thus the common attaining reference direction is
valid without changing the fixed reflection ranks. As in Section 1,
increasing the active eigenvalue spread majorizes that pair, and raising
the common scalar-complement eigenvalue to s then gives weak majorization
of the complete compressed spectrum. Trace rearrangement therefore
justifies this comparison even before the active memory plane is chosen.

For arbitrary M>=2 with both minority ranks one, replace the second active
weight lambda_3 in (3) by lambda_(M-1), and replace each complementary
sum by 1 minus the two active weights. No parity assumption is needed.

Comparison of Psi_t(x,y) with K>0 uses exactly the same convex quartic and
cubic root, without the scalar-branch prerequisite K>=s(x+y). When x+y>0
and K<=0 the comparison fails; when x=y=0, Psi=0. Thus (3) requires at most
two cubic-root comparisons.

In the frequent range 2<t<=2+sqrt(2), one has f_a>=s throughout and only
the first term in (3) is needed. Indeed

```math
\operatorname{sign}(f_a-s)
=\operatorname{sign}[(\sqrt2-a)(\sqrt2+2a-t)].
```

For a flat ququart marginal,

```math
F_{11}(t,I_4/4)
=\frac1{2(t-\sqrt2)}+\frac{t^2-2}{2t(t^2-4)}.
```

The active trace is maximized at a=b=1. Equation (3) remains finite for
every t>2 but diverges as t decreases to two, just as its single active
Bell pole requires. The one-block union formula is max{s,F_11} in
dimension four, and therefore can only be larger.

## 5. Verification and model scope

The constrained matching proof, common attaining reference direction,
odd-dimensional extension, fixed-signature orientation comparison, and
cubic-root decision rules received an independent symbolic reconstruction
within this workspace. Finite construction diagnostics supplement the
analytical argument; they do not establish universal optimality by
sampling. Reproduction details and recorded runs are in
[reproducibility](../REPRODUCIBILITY.md).

The [targeted checker](../../tools/check_block_budget_and_envelopes.py)
and [recorded result](../../results/block_budget_and_envelopes.json) use

```bash
python tools/check_block_budget_and_envelopes.py --output results/block_budget_and_envelopes.json
```

The formulas concern the last original site's two possible readouts in a
virtual score Hamiltonian. They do not introduce sequential queries on the
same specimen. The interface model still uses one arbitrary unknown
specimen, one delayed local X/Z query, unrestricted collective encoding,
unlimited classical side information, and worst-case retained quantum
dimension. The block count k is a mathematical decoder classification,
not a changed physical memory budget.

The unrestricted interface converse, the complete remaining reflection
signatures, and publication originality remain open.
