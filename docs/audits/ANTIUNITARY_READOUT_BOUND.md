# A bound for every common antiunitary readout symmetry

Date: 24 September 2026. Reviewed main:
`0730608b9daa9ba09a27843d57b47134a5852fd4`.

**Verdict.** The previous square-minus-one readout theorem extends to
every common antiunitary that negates the six readouts. Its square need
not be scalar. The proof combines the preceding spin-flip result with
an explicit two-qubit algebra reduction and established qubit monogamy.
The resulting classwide constant is sharp. General balanced readouts
need not admit this symmetry; unrestricted optimality and publication
originality remain unresolved.

## 1. Statement and short core argument

Let `U_j` run over `X_1,Z_1,X_2,Z_2,X_3,Z_3`. Suppose six Hermitian
contractions B_j on C^4 admit one antiunitary Theta such that

$$
\Theta B_j\Theta^{-1}=-B_j\quad\text{for all }j.
\tag{1}
$$

No condition on `Theta^2`, no pairwise commutation condition, and no
condition on the original seed state is imposed. General binary POVMs
are included. If B_j is a reflection, it is balanced because Theta
pairs its positive and negative eigenspaces.

**Theorem.** For every real weight vector w,

$$
\boxed{\left\|\sum_{j=1}^{6}w_j U_j\otimes B_j\right\|_\infty
\le2\|w\|_2.}
\tag{2}
$$

Equivalently, for every state omega on the reference and memory,

$$
\sum_{j=1}^{6}\bigl[\operatorname{Tr}\omega(U_j\otimes B_j)\bigr]^2
\le4.
\tag{3}
$$

The exact equal-weight maximum over the entire class (1) is `2sqrt(6)`.
It yields uniform contrast `sqrt(2/3)`, below the retention contrast
`(4+sqrt(2))/6` at three inputs and two retained qubits.

The argument has three cases. The unitary `V=Theta^2` commutes with
every readout. If V is nonscalar, its eigenspaces have dimension at most
two, so qubit bounds apply to each block. If V=+I, the extreme readouts belong
to two commuting Pauli algebras, and qubit monogamy again applies.
If V=-I, the [spin-flip theorem](SPIN_FLIP_PURITY_BOUND.md), Section 5,
already proves (2). These cases exhaust every antiunitary on C^4.

## 2. The qubit ingredient, including scalar readouts

For a two-qubit state define M as the sum of the two largest squared
singular values of its 3-by-3 spin correlation matrix. For arbitrary
mixed three-qubit states the established Cheng–Hall inequality is

$$
M_{AB}+M_{AC}\le2.
\tag{4}
$$

The settings for the two pairs may differ. Consequently two fixed
orthogonal X/Z correlations with a common memory qubit have squared
sum at most the corresponding M. A single correlation square is also
at most M. Partial tracing to the required three-qubit state is allowed.

Consider arbitrary reflection readouts on a memory of dimension two.
They are scalar signs or unit Pauli observables. If at least one
readout of a reference pair is scalar, the two complete correlation
operators anticommute. Their squared expectation sum is at most one:
the square of their real weighted sum is `(a^2+b^2)I`.
Call the other sites active. Each active site's squared sum is at most
M and hence at most two. For two or more active sites, sum (4) over
their pairs: their total is at most their number. For three references,
zero or at least two active sites therefore give a total at most three;
one active site gives at most four. Thus every qubit-memory state obeys
(3), even with scalar readouts. The corresponding weighted norm bound
extends to all Hermitian qubit contractions: their extreme points are
reflections, and the operator norm is convex in each readout separately.
A one-dimensional block is included by padding to a qubit.

For later comparison the established unrestricted qubit-memory
equal-weight bound is `2+2sqrt(2)`; see
[the one-qubit theorem](../ONE_QUBIT_OPTIMALITY.md).

## 3. Square plus one gives two commuting qubit algebras

An antiunitary with square +I has an orthonormal fixed basis. In that
basis Theta is ordinary conjugation, so every odd Hermitian B is purely
imaginary. The six-dimensional space of such 4-by-4 matrices has basis

$$
L=(X\otimes Y,\ Y\otimes I,\ Z\otimes Y),\qquad
R=(Y\otimes X,\ I\otimes Y,\ Y\otimes Z).
\tag{5}
$$

Each triple obeys the Pauli algebra, and the two triples commute with
one another. Write `B=x dot L+y dot R`, with real x,y. Then

$$
B^2=(|x|^2+|y|^2)I+2\sum_{a,b}x_a y_b L_aR_b.
\tag{6}
$$

The nine products L_a R_b are linearly independent traceless Pauli
words. Thus `B^2=I` forces every `x_a y_b=0`. Exactly one of x,y
is a unit vector and the other vanishes. The two commuting Pauli
algebras identify one fixed tensor factorization `Q=Q_1 tensor Q_2`.
Every reflection readout acts as a unit Pauli on one of these factors. Its factor
may depend on the query. This is deduced from symmetry, not imposed
on the encoder or on a general ququart readout.

We now prove (3). A reference site is split if its X and Z readouts act
on different factors. At a split site the two full correlation
operators anticommute, so their squared sum is at most one. At any
other site it is at most two. Let s be the number of split sites.

- If s is two or three, the total is at most `s+2(3-s)<=4`.
- If s is zero, distribute the three sites between Q_1 and Q_2.
  Two sites on the same factor have total at most two by (4), and the
  remaining site contributes at most two. If all three share a factor,
  summing their three pair inequalities gives at most three.
- If s is one and both whole sites share a factor, their total is at
  most two, with at most one more from the split site.
- If s is one and the whole sites use different factors, denote the
  split correlations on Q_1 and Q_2 by c,d. Apply (4) to the whole
  site and split reference using Q_1 as the common qubit. Their whole
  pair squared sum plus c^2 is at most two. Apply the same argument
  with Q_2 and d. Adding gives four.

This proves (3) and hence (2) for square plus one. For equal weights
there is a stronger, not asserted sharp, upper bound:

$$
\left\|\sum_jU_j\otimes B_j\right\|_\infty
\le2\sqrt3+\sqrt2<2\sqrt6.
\tag{7}
$$

Only the last case above requires this larger constant. Put
`t=c^2+d^2<=1`. The four other squared correlations sum to at most
`4-t`, so their absolute sum is at most `2sqrt(4-t)`. The split
absolute sum is at most `sqrt(2t)`. Their total increases on `[0,1]`
and at t=1 equals (7). All other cases give at most `2+2sqrt(2)`
or `3sqrt(2)`. A lower value `2+2sqrt(2)` is attainable in this class:
one memory factor forms a Bell pair with one reference; the other
factor and two references are product states, with collinear memory
readouts and bisector reference states. No exact optimum for (7)
is claimed.

For a general odd contraction the same decomposition gives
`||x dot L+y dot R||=|x|+|y|<=1`, since the factors commute and their
joint eigenvalues are the four combinations `+/-|x|+/-|y|`.
It is therefore a convex combination of the unit Pauli readouts in
the two factors and zero. Zero itself is the midpoint of opposite
reflections. Applying the norm bounds separately in each readout
extends (2) and (7) to all such contractions; (3) follows from (2).

## 4. Arbitrary squares reduce to the preceding cases

Set `V=Theta^2`. Equation (1) implies `VB_j=B_jV`. Moreover Theta
maps the lambda eigenspace of V antiunitarily onto its conjugate-lambda
eigenspace. The -1 eigenspace has even dimension by Kramers pairing.

If V is scalar, its scalar must equal its complex conjugate because
Theta commutes with its square; it is therefore +1 or -1. If V is
nonscalar in dimension four, no eigenspace can have dimension three:
a nonreal eigenvalue would require a conjugate eigenspace of dimension
three; -1 cannot have odd multiplicity; +1 of multiplicity three
would leave a one-dimensional invariant complement on which the square
of an antiunitary is necessarily +1. Multiplicity four is scalar.
Every eigenspace of a nonscalar V consequently has dimension at most two.

The Hamiltonian in (2) is block diagonal on these eigenspaces. Apply
Section 2 in each block, permitting arbitrary restricted contractions.
The norm of a block diagonal matrix is the largest block norm. This
proves (2) in the nonscalar case. Its equal-weight bound is actually
`2+2sqrt(2)` by the earlier one-qubit theorem.

For V=-I, the preceding spin-flip proof gives (2). Its symmetry-fixed
eigenvector argument and trace-norm duality use only `||B_j||<=1`, so
they apply to odd contractions as well. The cyclic projector
and complete orbit instrument in
[that report](SPIN_FLIP_PURITY_BOUND.md), Section 5, attain `2sqrt(6)`.
Together these observations establish the claimed sharp maximum over
all common antiunitaries, even though the separate +I maximum is not
evaluated.

## 5. Operational meaning and boundaries

For a complete instrument refine each branch to a Kraus matrix K_a,
omit zero branches,
put `L_a=K_a/||K_a||_F`, and use weights `p_a=||K_a||_F^2/8`.
They sum to one. If each branch's six binary readout contractions satisfy (1),
allowing a different Theta on each branch, (2) bounds every normalized
branch score by `2sqrt(6)`. Averaging gives `6 eta<=2sqrt(6)` for
a uniform target. The complete cyclic instrument supplies attainment,
accepts every branch, and has quantum dimension four on every branch.

Encoding remains collective and unrestricted within this readout class.
There is one unknown specimen and one delayed query, unlimited finite
classical records, worst-case quantum dimension, and uniform input/query
error. The antiunitary is an algebraic condition; it is not a physical
operation implemented by the protocol.

The common antiunitary assumption cannot be removed by changing memory
coordinates. For example the six balanced reflections

$$
X\otimes I,\ Z\otimes I,\ Y\otimes I,\ I\otimes X,\ I\otimes Z,
\ X\otimes X
\tag{8}
$$

admit no antiunitary that negates all of them: negating `X tensor I`
and `I tensor X` preserves their product `X tensor X`. This refutes
the proposed symmetry reduction, not the unrestricted score bound.
The other nonscalar signature sectors also remain to be controlled.

For general balanced readouts the exact remaining formulation is useful.
For any normalized 4-by-8 seed L and `C_j=L U_j L^dagger`, let

$$
\beta_j=\lambda_1(C_j)+\lambda_2(C_j)-\lambda_3(C_j)-\lambda_4(C_j)
=\min_{t\in\mathbb R}\|C_j-tI\|_1,
\tag{9}
$$

with eigenvalues in descending order. The unproved weighted bound for
all balanced readouts
is exactly `sum_j beta_j^2<=4`. These scores need not be root
fidelities. For rank-three seeds one may use 3-by-3 compressions C and
the exact identity

$$
\beta(C\oplus0)=\|(\operatorname{Tr}C)I_3-2C\|_\infty.
\tag{10}
$$

It follows by listing the three eigenvalues and zero. Optimal readouts
on the support can be chosen as `+/- (I_3-2|v><v|)`; their extensions to
dimension four share an eigenvector in the unused memory direction.
No proof that the rank-three
maximum occurs at rank two was obtained.

## 6. Prior ingredients, deductions, and verification

Cheng–Hall, *Anisotropic invariance and the distribution of quantum
correlations*, [arXiv:1610.09302v3](https://arxiv.org/pdf/1610.09302v3),
PRL 118, 010401 (2017), Eq. (1), p. 1, and Eqs. (13)–(14) plus the
following mixed-state paragraph, p. 3, supply (4). Independently chosen
settings and a common qubit are essential. The theorem is applied only
after the algebraic reduction; it does not directly apply to an
arbitrary ququart memory. The publisher correction is addressed in the
[earlier source audit](../ONE_QUBIT_OPTIMALITY.md), Section 2.

The anticommuting-observable squared-expectation inequality is also
established; see Kurzynski et al.,
[arXiv:1010.2012v2](https://arxiv.org/pdf/1010.2012v2), PRL 106,
180402 (2011), Eq. (1), p. 2. Here its short weighted-square proof is
included. Kramers pairing, real structures and Pauli algebra are prior
ingredients. The supplied deductions are their explicit application
to the +I class, the arbitrary-square reduction, and the unified
readout bound. They do not constitute a new monogamy theorem or an
exhaustive originality finding. The -I case retains the primary-source
comparison in the preceding spin-flip report.

Independent internal reconstructions checked the algebra, all assignment
cases, nonscalar-square multiplicities, norm transfer, and operational
quantifiers. Small deterministic construction checks are recorded by
[`check_antiunitary_readouts.py`](../../tools/check_antiunitary_readouts.py)
in [`antiunitary_readouts.json`](../../results/antiunitary_readouts.json).
They supplement the analytic proof; they are not optimality or priority
certificates. Separate bounded exploratory searches found no violation
of the full balanced conjecture and supplied no universal upper bound.

All 198 weighted operator construction checks passed at tolerance
1e-10 in Python 3.12.14 with NumPy 2.3.5. The parent independently
reran the script and reproduced its JSON byte-for-byte. The largest
Hamiltonian has dimension 32. No optimizer enters this diagnostic.
