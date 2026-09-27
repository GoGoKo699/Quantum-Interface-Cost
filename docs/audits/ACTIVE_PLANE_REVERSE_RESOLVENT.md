# A direct active-plane resolvent bound

Research base: `7cb964b47b8aa13a604a3ab5df663d4f399fa6f4` (PR #49).
Date: 27 September 2026.
Status: supplied analytical theorem, independently reconstructed within
this workspace. This is internal mathematical review, not external peer
review or a claim of publication priority.

The [physical one-mode obstruction](REFLECTION_ENVELOPE_OBSTRUCTION.md)
shows that a valid inverse and the actual top marginal need not make a
flattened spectral envelope pass. Here the full earlier Hamiltonian remains
inside the inverse. Retaining the loss on the last query's active memory
plane gives an explicit norm bound, independent of the memory dimension.

## 1. Quantitative statement and benchmark corollary

Let N>=1 trusted reference qubits precede a final reference qubit, and let
Q have any finite dimension at least two. Write

```math
H_0=\sum_{i=1}^N(X_iB_i+Z_iD_i),\qquad
-I\le B_i,D_i\le I,\qquad U=\|H_0\|\le2N.
```

Let h=X_(N+1) B+Z_(N+1) D, where B,D are reflections with at most one
noncommuting two-dimensional Jordan block. On its active memory plane P,
write the Hamiltonian eigenvalues as ±u,±v, with

```math
r=\sqrt2,\qquad r\le u\le2,\qquad 0\le v\le r,
\qquad u^2+v^2=4,\qquad x=u-r.
```

Define the scalar coefficients and their reference-field norm

```math
\beta_i=\tfrac12\mathrm{Tr}_Q(PB_i),\qquad
\delta_i=\tfrac12\mathrm{Tr}_Q(PD_i),\qquad
\zeta_P=\sum_{i=1}^N\sqrt{\beta_i^2+\delta_i^2}
\le\min\{U,Nr\}.
\qquad\text{(1)}
```

**Theorem.** For arbitrary earlier Hermitian contractions and every such
last reflection pair,

```math
\boxed{\|H_0+h\|\le r+
\frac{x+\sqrt{x^2+4U^2+4\zeta_Px}}2.}
\qquad\text{(2)}
```

If the last pair is commuting, set x=0; the right side is U+r and no
choice of an active plane is needed. Formula (2) never exceeds the
triangle bound U+u. No attainment or optimality claim for (2) is made.

In particular, the exact plane-dependent sufficient condition

```math
\boxed{U^2+(2N+\zeta_P)(u-r)\le4N^2}
\qquad\text{(3)}
```

implies `||H0+h||<=2N+r`. The following simpler condition suffices
without computing the plane means:

```math
\boxed{U^2+N(2+r)(u-r)\le4N^2.}
\qquad\text{(4)}
```

Since u<=2, the all-angle cutoff is

```math
\boxed{U\le\sqrt{4N^2-2N}
\quad\Longrightarrow\quad\|H_0+h\|\le2N+\sqrt2.}
\qquad\text{(5)}
```

For the three-input problem N=2, this gives **U<=2sqrt(3)**, strictly
beyond the triangle threshold 2+sqrt(2). There is no condition on the
second earlier eigenvalue or on the head channel. The memory dimension
need not be four or even; the block condition concerns only the last
readout pair.

## 2. Keep the active-plane baseline loss

Let Pi be the last block's top Bell projector on its reference and P Q.
The complete active-block spectrum and the scalar complement give

```math
h\le rI-aP+b\Pi,\qquad a=r-v,\quad b=u-v.
\qquad\text{(6)}
```

Reference spectator identities are implicit. On the active plane the
right side is vP+(u-v)Pi; all other active eigenvalues are at most v.
On the scalar complement every eigenvalue is at most r. This cap retains
the loss r-v on the entire active plane, which a positive-Bell-only cap
discards.

If u=v=r, then ||h||<=r and (2) is the triangle inequality. Suppose u>r.
Choose any A>U and put

```math
K=AI-H_0>0,\qquad c=A^2-U^2>0.
```

To prove H0+h<=(A+r)I it suffices, by (6), to establish

```math
K+aP-b\Pi\ge0.
\qquad\text{(7)}
```

The inverse used below is the inverse of the full earlier Hamiltonian
with a plane term added. No leading-mode or lower-spectrum replacement
is made.

## 3. A spectral chord and an exact compressed inverse

The spectrum of K lies in [A-U,A+U]. The convex function y^(-1) lies
below its endpoint chord, so functional calculus gives

```math
K^{-1}\le\frac{2AI-K}{c}=\frac{AI+H_0}{c}.
\qquad\text{(8)}
```

When U=0 this is equality. Let J insert the earlier reference space
tensored with C^2 into the active plane, so JJ*=P, and define

```math
T=J^*K^{-1}J,\qquad H_P=J^*H_0J,\qquad D_P=(AI+H_P)/c.
```

Then 0<T<=D_P. The exact inverse-update identity gives

```math
J^*(K+aP)^{-1}J=f_a(T),\qquad
f_a(y)=\frac{y}{1+ay}.
\qquad\text{(9)}
```

For example, the left side is
`T-aT(I+aT)^(-1)T=T(I+aT)^(-1)`.
The function f_a is operator monotone increasing and operator concave
on positive matrices. For a>0 both facts follow from
`f_a(T)=a^(-1)[I-(I+aT)^(-1)]` and inverse monotonicity/convexity;
for a=0 it is linear. Hence

```math
J^*(K+aP)^{-1}J\le f_a(D_P).
\qquad\text{(10)}
```

## 4. Bell compression is a normalized plane trace

Let E_P(M)=(1/2)Tr_(C^2) M, a unital completely positive map. Concavity gives

```math
E_P[f_a(D_P)]\le f_a[E_P(D_P)].
\qquad\text{(11)}
```

This Jensen step also follows directly by averaging the four active-qubit
Pauli conjugations: `E_P(M) tensor I_2` is that unitary average, to which
operator concavity applies.

The original earlier Pauli structure now gives

```math
E_P(H_P)=\sum_i(\beta_iX_i+\delta_i Z_i),\qquad
\|E_P(H_P)\|=\zeta_P.
```

Different-site terms commute, and each site's two-axis field has norm
sqrt(beta_i^2+delta_i^2), proving the norm identity. Each scalar coefficient
has magnitude at most one, giving zeta_P<=Nr. The compression followed by
normalized partial trace is unital and contractive, also giving zeta_P<=U.
Thus, with L=A+zeta_P, (10)--(11) imply

```math
E_P\left[J^*(K+aP)^{-1}J\right]
\le\frac{L}{c+aL}I.
\qquad\text{(12)}
```

Inserting Pi while leaving the earlier references untouched gives exactly
the normalized plane trace on the left: the inverse acts trivially on the
last reference, and the Bell vector has active-memory marginal I_2/2.
The positive-update criterion for (7) therefore passes whenever

```math
b\frac{L}{c+aL}\le1
\quad\Longleftrightarrow\quad
A^2-U^2\ge(A+\zeta_P)(u-r).
\qquad\text{(13)}
```

Here b-a=u-r. Set A to the positive root of equality in (13):

```math
A=\frac{x+\sqrt{x^2+4U^2+4\zeta_Px}}2>U\qquad(x>0).
```

This proves the upper-eigenvalue bound (2). Conjugating all N+1 trusted
references by Y reverses H0+h, so the same bound controls its operator norm.
The x=0 case was handled before any inverse was taken.

## 5. Consequences and precise remaining regime

Because zeta_P<=U, the square root in (2) is at most x+2U; thus (2)
never exceeds U+u. Substitution of A=2N in (13) gives (3), and
zeta_P<=Nr gives (4). Finally `(2+r)(2-r)=2` gives (5).

For comparison with the triangle certificate at the target 2N+r, write
x=u-r in (0,2-r]. The triangle threshold is U<=2N-x. The squared difference
between the new universal threshold and that threshold is

```math
[4N^2-N(2+r)x]-(2N-x)^2=x[N(2-r)-x].
```

For N>=2 it is strictly positive throughout the noncommuting interval.
For N=1 it is positive except at the sharp endpoint x=2-r, where the
two thresholds coincide. This is a global spectral improvement, without
an orientation assumption on the earlier pairs or a small stability radius.

Combining N=2 with the [high-second-mode theorem](HIGH_SECOND_MODE_ONE_BLOCK.md),
a possible violating one-block tuple must satisfy

```math
U>2\sqrt3,\qquad m<2+\sqrt2,
\qquad U^2+(4+\zeta_P)(u-\sqrt2)>16.
```

The first two are necessary conditions for any violation, and the third
retains the actual last block's angle and plane. They do not assert that
the remaining region contains a violation or close a complete signature.

The actual-plane condition also repairs both last-pair variants in the
[physical one-mode obstruction](REFLECTION_ENVELOPE_OBSTRUCTION.md).
There P is the Z_A=+1 memory plane, u=2, and zeta_P=2/sqrt(3): only the
first earlier site's two scalar means are nonzero, each equal to
`(2/sqrt(3))/sqrt(2)`. The already proved radical bounds give U<71/20,
while zeta_P<6/5 and 2-sqrt(2)<3/5. Consequently

```math
16-U^2-(4+\zeta_P)(2-\sqrt2)
>16-\left(\frac{71}{20}\right)^2-
\frac{26}{5}\frac35=\frac{111}{400}>0.
```

Thus the present direct certificate passes the same explicit `(11)` and
`(12)` pairs for which both one-mode spectral envelopes fail. This does
not assume that those envelopes approximate the actual Hamiltonian.

The all-angle cutoff (5) also applies when the last binary-POVM pair is
jointly block diagonal on one fixed plane and scalar blocks on its
complement. Decompose each contraction into reflection vertices within
that fixed block algebra and use convexity of operator norm. This does
not assign the reflection-specific u,v parameters to a general POVM pair.

## 6. Verification and scope

Independent readers reconstructed the inverse chord, compressed inverse,
monotonicity and concavity directions, normalized Bell compression, all
endpoints, the general-N extension, and the comparison with the triangle
bound. These are analytical arguments; no parameter scan establishes any
of the universal claims.

Reproduce the targeted scalar and fixed matrix identities with

```bash
python tools/check_direct_resolvent_and_channel.py --output results/direct_resolvent_and_channel.json
```

The result records the checker and proof-note hashes. Finite diagnostics
supplement the proof and do not certify publication novelty.

The extension to arbitrary memory dimension is a sufficient spectral
bound, not a claim that a larger unrestricted memory has the same capacity
as a ququart. All three complete remaining ququart reflection signatures,
unrestricted optimality and publication originality remain open. The model
still uses one unknown specimen, one delayed local query, unrestricted
collective encoding and worst-case quantum memory; the proof introduces
no extra physical resource or sequential-query requirement.
