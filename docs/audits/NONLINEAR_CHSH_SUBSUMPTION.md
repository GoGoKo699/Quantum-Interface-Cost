# Nonlinear CHSH bounds already imply the joint resource support

Date: 2026-09-24. Reviewed main:
`ac0bf7cebd5a8a346d8b64371edab7b2c30ca271` (PR #28).
Reviewed tree: `364a8f73fbd18a78eb0ef367beee3119d2f7df00`.

**Finding:** our sharp mixed-state two-qubit support bound is a direct
corollary of Zhu–Zhang–Ma's nonlinear negativity theorem. Combining that
theorem with the standard formation/negativity inequality and Jordan
blocks also recovers the **entire all-price convex-hull characterization**
of the two-correlation resource problem. These are stronger prior
implications than the earlier comparison with their affine formation
certificate. The latter comparison remains mathematically correct, but
does not establish separation from everything in that source.

The explicit phase formula, scalar-root evaluation and optimizer/equality
analysis remain supplied calculations to assess for originality and
publication significance. No unrestricted memory optimum is established.
This report corrects attribution without changing the proved profile.

## 1. Exact primary theorem and conventions

Yuwei Zhu, Xingjian Zhang and Xiongfeng Ma, *Interplay among entanglement,
measurement incompatibility, and nonlocality*,
[arXiv:2303.08407v2](https://arxiv.org/html/2303.08407v2), 20 June 2025.
The official primary PDF was read; pages below are printed PDF pages.

Equation (2), p. 5, uses alpha>=1 and the weighted CHSH score

$$
S_\alpha=\alpha\langle A_0(B_0+B_1)\rangle
+\langle A_1(B_0-B_1)\rangle.
\tag{1}
$$

Corollary 1 starts on p. 15. Equation (30), p. 16, bounds **ordinary
negativity** for every two-qubit state when S_alpha>2alpha:

$$
2N\ge\sqrt{S_\alpha^2/4-\alpha^2}.
\tag{2}
$$

Equation (31) on that page supplies Bell-diagonal saturators. Corollary
2 / Eq. (32) then convexifies the scalar certificate for arbitrary
dimension. Theorem 2 / Eq. (25), p. 14, is the separate affine formation
certificate compared in our [earlier report](PROFILE_NOVELTY_AND_STEERING_REDUCTION.md#3-exact-separation-from-the-whole-inspected-weighted-chsh-family).
The source's Section 3.2, Eq. (24), pp. 13–14, also discusses the radial
formation curve and its concavity. The calculations below apply (2)
before discarding the qubit-block information.

## 2. The full mixed-state support is an optimized prior corollary

Fix Bob's qubit X,Z and write

$$
x=\langle A_0\otimes X\rangle,\quad
z=\langle A_1\otimes Z\rangle,\quad
v=2N,\quad a\ge b>0,\quad R=\sqrt{a^2+b^2}.
$$

First consider a two-qubit block with binary projective Alice readouts.
For any alpha>=1 define

$$
t_\alpha=\sqrt{a^2/\alpha^2+b^2},\quad
\cos\theta=\frac{a}{\alpha t_\alpha},\quad
\sin\theta=\frac{b}{t_\alpha},\quad
B_\pm=\cos\theta X\pm\sin\theta Z.
\tag{3}
$$

The cosine and sine are normalized. Anticommutation of X,Z makes B_+
and B_- valid qubit reflections, and (1) is exactly
S_alpha=2(ax+bz)/t_alpha. Therefore (2) implies

$$
ax+bz\le\sqrt{(a^2/\alpha^2+b^2)(\alpha^2+v^2)}.
\tag{4}
$$

This also holds when S_alpha<=2alpha: the right side is at least
alpha t_alpha, and the claimed upper bound is then immediate. Thus no
violation condition or imaginary square root is silently omitted.

Put r=alpha^2>=1. The square on the right of (4) is

$$
a^2+b^2v^2+b^2r+\frac{a^2v^2}{r}.
$$

Its minimizer is r=max(1,av/b), including v=0. Hence

$$
\boxed{ax+bz\le B_v(a,b):=
\begin{cases}
R\sqrt{1+v^2},&0\le v\le b/a,\\
a+bv,&b/a\le v\le1.
\end{cases}}
\tag{5}
$$

For b=0 the statement is simply ax<=a. Exchanging the weights gives
the other ordering. This is exactly Eq. (9) in the
[joint-resource report](JOINT_RESOURCE_FRONTIER.md#22-sharp-mixed-state-support-bound),
now with a direct prior-theorem derivation. The Bell-projector proof
there remains a valid alternative proof. It is not a new mixed-state
entanglement inequality.

The bound is about ordinary negativity, not a substitution of negativity
for convex-roof concurrence. That distinction in the earlier report was
necessary; the overlooked prior corollary already handles it.

## 3. The implication extends to every formation/negativity price

Let E=E_F in bits, V=2N and

$$
f(v)=h_2\!\left(\frac{1-\sqrt{1-v^2}}2\right),\quad
q(v)=\mu f(v)+\lambda v,\qquad\mu,\lambda\ge0.
$$

On every two-qubit state E>=f(V). For example, in any pure-state
decomposition convexity of V and convexity and monotonicity of f give
sum p f(v_j)>=f(sum p v_j)>=f(V); minimize the left side. No identity
between ordinary negativity and a mixed-state convex roof is assumed.

For arbitrary finite Alice dimension, dilate both contractions to
reflections on the same doubled space. A local isometry preserves E,V.
Jordan decomposition and pinching produce one- or two-dimensional
Alice blocks while retaining Bob's qubit and both correlations. The
pinching decreases both resources. Orthogonal flags satisfy

$$
E_F\!\left(\bigoplus_jp_j\rho_j\right)
=\sum_jp_jE_F(\rho_j),\qquad
V\!\left(\bigoplus_jp_j\rho_j\right)=\sum_jp_jV(\rho_j).
\tag{6}
$$

The first identity follows from convexity and local-measurement
monotonicity; the second is the trace norm of a direct sum. Scalar
Alice blocks have zero cost and weighted correlation at most R. Apply
(5) separately to the two-qubit blocks; this use does not assert the
qubit corollary for the undivided higher-dimensional state.

On the radial branch of (5) put u=sqrt(1+v^2). Both
f(sqrt(u^2-1)) and sqrt(u^2-1) are concave on 1<=u<=sqrt(2).
Consequently Ru-q(sqrt(u^2-1)) is convex, and its maximum on the
radial interval occurs at an endpoint. The other branch is a+bv-q(v).
Extending that branch to all 0<=v<=1 cannot increase the result
incorrectly: a+bv<=B_v(a,b) everywhere by Cauchy–Schwarz. Thus

$$
\max_{0\le v\le1}[B_v(a,b)-q(v)]
=\max\left\{R,\ a+\max_{0\le v\le1}[bv-\mu f(v)-\lambda v]\right\}.
\tag{7}
$$

This bound is attained; a=b=0 is immediate. Otherwise a product state
with Alice's readouts both +1
and Bob's Bloch direction (a/R,0,b/R) attains R with zero resources.
An exact-axis state with x=1,z=v and (E,V)=(f(v),v) attains the other
term. Such states and their orthogonal-flag mixtures are already prior
ingredients, as recorded in the [Tomassoli comparison](TOMASSOLI_FULL_TEXT_COMPARISON.md).
Therefore, over **all** finite-dimensional realizations,

$$
\boxed{\sup[ax+bz-\mu E-\lambda V]
=\max\left\{\sqrt{a^2+b^2},\ a+
\max_{0\le v\le1}[bv-\mu f(v)-\lambda v]\right\}.}
\tag{8}
$$

Taking mu=1 gives every scalarization E+lambda V. Standard convex
duality and the physical flagged generators identify its minimum
with the convex hull of the free quarter disk and the exact-axis
curves of cost f(v)+lambda v. Decreasing either contrast is physical
by independent random output flips, so nonnegative correlation weights
suffice on the positive square. The mu=0 case includes the negativity
endpoint. Thus not only the block bound, but the complete sharp
all-price **convex-hull characterization**, is a short consequence of
prior inequalities plus established flagging and duality.
This characterizes resource minima and budgets, not every attainable
exact pair (E,V) above the efficient frontier.

This is a derivation from the cited theorem, not a claim that its paper
prints our phase/root formulas. Three-dimensional attainment at each
specified profile additionally uses the explicit optimizer geometry;
it is not inferred just from the existence of arbitrary finite flags.

For example, choose mu=0 and lambda=a+b-R in (8). This gives the
entire weighted negativity inequality

$$
ax+bz\le R+(a+b-R)V,
$$

used in the [separate-resource report](RESOURCE_OPTIMA_AND_JOINT_DECODERS.md).
Its subsequent geometric evaluation yields min V=w. The inequality
itself is another direct prior consequence, not a new negativity witness.

## 4. Why the earlier affine comparison does not contradict this

The earlier comparison optimized the dimension-independent **affine**
formation certificate in Eq. (25). Its best value is the radial bound

$$
L_{\rm rad}(x,z)=\left[\frac{\sqrt{x^2+z^2}-1}{\sqrt2-1}\right]_+,
$$

strictly below C at every asymmetric point outside the disk. That
theorem and its proof remain correct.

The present calculation retains each qubit block, optimizes the
nonlinear source family with that block's V, and only then forms the
joint resource hull. Replacing the block curve by a dimension-independent
scalar chord earlier discards useful information. The two operations
are different; outperforming the affine bound does not demonstrate
independence from the source's nonlinear theorem.

In particular, neither dimension enlargement nor the use of two observed
correlations blocks the reduction above. These distinctions were useful
against specific source statements, but cannot support a blanket
non-subsumption claim.

## 5. Revised claim boundary and proof status

| Item | Revised status |
|---|---|
| Mixed-state weighted support B_v | Direct corollary of prior Corollary 1 / Eq. (30), by (3)–(5); alternative elementary proof retained |
| Sharp support at every nonnegative resource price and disk-plus-axis hull | Short corollary of the same source, E>=f(V), radial concavity, Jordan blocks, flags and established convex duality |
| Full explicit phase, scalar root, conditional budget curve and optimizer/equality analysis | Supplied evaluation of that prior-derived optimization; not found as an explicit statement in the inspected source, but exhaustive originality and significance remain unestablished |
| Fixed-cap operational translation | Separate task-specific result; not supplied merely by an average entanglement cost or the source's Bell bound |
| Unrestricted equal-accuracy memory rate | Still unresolved; (8) concerns one trusted qubit, not many sites sharing one quantum register |

The publication assessment should therefore emphasize an **explicit
evaluation and its operational consequences**, with this prior chain
stated prominently. A new mixed-state support principle or a distinction
from all weighted-CHSH consequences would be an overclaim. Finding this
overlap is a substantive audit correction, even though the formulas and
their proofs in the repository remain valid.

The same turn also re-examined the shared-memory proof bottleneck. No
all-state entropy proof or admissible violating seed was obtained. A
natural fidelity minimax relaxation returns the trivial value 2n, and
a fixed-spectrum product-basis reduction remains a conjecture. These
unsuccessful approaches are not new entropy exclusions and are not used
as evidence for proximity to a solution.

The operational contract remains one arbitrary unknown specimen, one
delayed local query, unrestricted collective encoding, unlimited finite
classical records, worst-case quantum dimension and uniform error over
all states and queries. Virtual block analysis introduces no physical
postselection, extra copies or free shared entanglement.

## 6. Verification

The primary version, measurement normalization, ordinary-negativity
factor, subthreshold case, r>=1 minimization, zero weights, block
reduction and all-price endpoint argument were independently reconstructed
within the workspace. Key source equations were also checked visually
in the primary PDF. This is internal proof review, not external peer
review. No simulation is needed for the subsumption result; unchanged
entropy certificates were not rerun. Repository links, whitespace,
LICENSE and the historical initial audit were checked before integration.
No third-party primary text is redistributed.
