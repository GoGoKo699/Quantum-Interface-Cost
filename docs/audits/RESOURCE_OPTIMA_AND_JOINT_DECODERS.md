# Distinct resource optima and projective two-input joint decoders

Date: 2026-09-23. Reviewed main:
`6367ab89601eb45485cba15df8feabb553e0fac1` (PR #18 merge).
Reviewed tree: `7a40a3200bcbb537366e0188a9d3e65a1713508a`.
No open pull requests or newer issue work was present at inspection.
Status: supplied analytical deductions with independent internal review;
targeted primary-source audit, not historical-priority certification.

The original interface still receives one arbitrary unknown specimen before
one delayed local query. Collective encoders, unlimited classical records,
worst-case quantum dimension, and uniform input/query errors are unchanged.
The auxiliary realization problem below counts all Alice flags in its
dimension; its negativity is not an operational memory charge.

## 1. Exact ordinary-negativity profile

Let B be a trusted qubit, let A have arbitrary finite dimension, and let
A_0,A_1 be Hermitian contractions. Only
`x=Tr omega(A_0 tensor X)`, `z=Tr omega(A_1 tensor Z)` are specified,
with x,z in [0,1]. No marginals or cross-correlations are imposed.
Use ordinary negativity, not logarithmic negativity or convex-roof
concurrence:

$$
N(\omega)=\frac{\|\omega^{T_B}\|_1-1}{2},\qquad
w(x,z)=\left[x+z-1-\sqrt{2(1-x)(1-z)}\right]_+.
$$

**Theorem 1.** Over all such realizations,

$$
\boxed{\min N(\omega)=\frac{w(x,z)}2.}
\tag{1}
$$

Dimension three suffices throughout. This supplies a full two-parameter
ordinary-negativity comparison. The concurrence benchmark w and attaining
flags follow from previously mapped steering results, and the equal-weight
negativity line is explicitly prior;
the weighted proof and the optimizer consequence below are supplied here.

### 1.1 A weighted inequality valid in every finite dimension

Fix a,b>=0 and put R=sqrt(a^2+b^2), T=a+b. We prove

$$
ax+bz\le R+2(T-R)N(\omega).
\tag{2}
$$

For each contraction use the reflection dilation on the same doubled
Alice space,

$$
\widetilde A_j=
\begin{pmatrix}A_j&\sqrt{I-A_j^2}\\
\sqrt{I-A_j^2}&-A_j\end{pmatrix}.
$$

Embed the state in the first summand. This local isometry preserves both
correlations, N, and E_F. Jordan's lemma for two reflections decomposes
the doubled Alice space into common reducing blocks of dimensions at most
two. Pinch Alice onto these blocks, writing the resulting state as
`omega'=direct_sum_k p_k omega_k`. The pinching preserves the correlations
and cannot increase either N or E_F. Ordinary negativity is exactly
`N(omega')=sum_k p_k N(omega_k)`, by the trace norm of a direct sum.
The entropy formation cost has the same flag identity: convexity gives
one direction and measuring the orthogonal local flag gives the other.
These are standard local-measurement properties, not new resource rules.

On a one-dimensional block the weighted score is at most R and N=0.
On an irreducible two-dimensional block both reflections are traceless
Pauli directions. The weighted Hamiltonian

$$
H=aA_0\otimes X+bA_1\otimes Z
$$

has a real rank-at-most-two correlation matrix. Local unitary changes of
axes put it in the form `H=s_1 Z tensor Z+s_2 X tensor X`, where

$$
s_1\ge s_2\ge0,\qquad s_1^2+s_2^2=R^2,\qquad s_1+s_2\le T.
\tag{3}
$$

The first identity uses the orthogonality of the trusted X,Z columns;
the last inequality is the nuclear-norm triangle inequality for their
two rank-one terms. A zero third singular value allows both displayed
coefficients to be positive using physical local rotations.

Let Pi be the Bell projector at the maximal eigenvalue s_1+s_2. The
remaining eigenvalues are at most s_1-s_2, hence

$$
H\preceq(s_1-s_2)I+2s_2\Pi.
$$

For any two-qubit state tau, partial transposition and trace-norm duality
give `Tr(Pi tau)<=||Pi^{T_B}||_infinity ||tau^{T_B}||_1=1/2+N(tau)`.
Writing v=2N(tau) in [0,1], we obtain

$$
\operatorname{Tr}(H\tau)
\le s_1+v s_2
=(1-v)s_1+v(s_1+s_2)
\le(1-v)R+vT.
\tag{4}
$$

Average (4) and the one-dimensional bounds over the blocks. Since
N(omega')<=N(omega) and T>=R, this proves (2), including arbitrary binary
POVMs in the original realization. No common execution of incompatible
Alice measurements is assumed.

### 1.2 Optimizing all weights and attaining the result

Outside the disk x^2+z^2<=1, excluding the Bell corner, let q=w and set
`u=(x-q)/(1-q)`, `s=(z-q)/(1-q)`. Then u,s>=0 and u^2+s^2=1.
Choose a=u,b=s in (2). Since

$$
ux+sz=1+q(u+s-1),
$$

it follows that N>=q/2 whenever u+s>1. This covers the noisy interior.
On x=1, taking a/b to infinity in (2) gives N>=z/2; interchange the
axes for z=1. The Bell corner follows by either limit. On the disk the
bound is N>=0.

For attainment outside the disk use the known orthogonally flagged state
with a product component of probability 1-q and a Bell component of
probability q. Its Alice dimensions are 1+2. Let the product component's
Bob Bloch vector be (u,0,s), and use Alice readouts equal to +1 on its
one-dimensional flag and appropriately paired Pauli observables on the
Bell block. The correlations are (x,z), and N=q/2. The Bell corner is
the Bell state itself. Inside the disk a product state with Bob Bloch
vector (x,0,z) and Alice readouts +1 suffices. This proves (1).

## 2. Minimizing negativity can forbid the entropy optimum

Let C(x,z) be the already evaluated minimum E_F with arbitrary finite A,
as established in [the two-correlation audit](TWO_CORRELATION_FORMATION.md).

**Theorem 2.** If x^2+z^2>1 and max(x,z)<1, then

$$
\boxed{\min_{\substack{\omega,A_0,A_1\text{ realize }(x,z)\\
N(\omega)=w(x,z)/2}} E_F(\omega)=w(x,z).}
\tag{5}
$$

Thus a minimum-negativity realization and a minimum-formation-entropy
realization can coincide exactly when C=w in this interior. Throughout
the strict-saving phase C<w, no realization minimizes both resources.
This is stronger than merely observing that scalar conversion of a prior
resource bound gives a weaker entropy certificate.

**Proof.** The u,s chosen above are strictly positive, so a=u,b=s is a
finite positive supporting pair, R=1 and T>1. When N(omega)=w/2,
every inequality in the weighted-score/negativity chain leading to (2)
is an equality.
In particular N(omega')=N(omega), and every positive-weight block saturates
its version of (4).

An irreducible two-dimensional block cannot have 0<v<1: equality in the
last step of (4) would require both s_1=R and s_1+s_2=T. Equation (3)
would then give s_2=0 and T=R, a contradiction. A block with v=0 also
requires s_1=R, s_2=0. Because a,b>0, the two Alice Pauli directions
would then be collinear and commute, contradicting irreducibility.
Thus every zero-negativity equality block is one-dimensional and separable.

Every remaining two-dimensional block has v=1 and weighted score T.
Equation (3) then gives s_1+s_2=T and s_1 s_2=ab>0. Its maximal
eigenvalue is nondegenerate, and the state must be its pure Bell
eigenvector. The total Bell-block probability is therefore
`2N(omega')=w`. All other blocks are classical and separable, so the
flag identity gives E_F(omega')=w. Local pinching cannot increase E_F;
hence E_F(omega)>=w. The product-plus-Bell construction from Section 1.2
attains both N=w/2 and E_F=w, proving (5).

The exact axes are deliberately excluded from (5). At (1,z), a pure
partially entangled state simultaneously attains N=z/2 and E_F=f(z),
where `f(z)=h_2((1-sqrt(1-z^2))/2)`. For 0<z<1, f(z)<z=w.
There is no finite positive supporting pair of the kind used above at
that boundary. On the classical disk a product realization minimizes both.

For 0<z<=x<1 outside the disk, the existing phase theorem now gives the
explicit optimizer incompatibility region

$$
\frac{1-x}{1-z}<2\left(\frac1{\ln2}-1\right)^2.
\tag{6}
$$

Exchange x,z on the other half of the square. For example, at
(x,z)=(.99,.5), minimum negativity is .195, but every realization
attaining that negativity has E_F>=.39. The existing exact interval
certificate places the unconstrained entropy minimum between
.324848239185893024 and .324848239186576377. These values evaluate
proved formulas; they are not fitted to a simulation.

## 3. Primary-source comparison and actual prior subsumption

Pusey, *Negativity and steering: a stronger Peres conjecture*,
[1305.1767v1](https://arxiv.org/abs/1305.1767v1), 8 May 2013,
Section IV / Figure 1 and adjacent text, p. 4, already gives the
equal-weight line
`N>=(F-sqrt(2))/(4-2sqrt(2))`, with F the sum of two trusted orthogonal
Pauli correlations. Its text describes level-three SDP convergence and
attainment by mixing separable and maximally entangled realizations.
After rotating its Y to Z, this is exactly (1) on x=z. The present
weighted proof does not rely on the precision of that numerical hierarchy.
The equal-weight line and the mixture mechanism must not be presented
as new. The supplied addition is the all-weight ordinary-negativity
calculation and its equality consequence (5); absence elsewhere is unproved.

As derived in the [preceding audit](FORMATION_OPTIMIZERS_AND_PRIOR.md),
optimizing Han et al.'s complete weighted concurrence family gives the
same minimum value w for convex-roof concurrence. Ordinary negativity is a
different mixed-state function. Its lower bound here needs (2); it does
not follow merely by replacing concurrence with twice negativity in
Han's theorem. The construction used for attainment is prior.

Guehne–Reimpell–Werner, *Estimating entanglement measures in experiments*,
[quant-ph/0607163v2](https://arxiv.org/abs/quant-ph/0607163v2),
12 March 2007, Eq. (1), p. 1, and Eqs. (6),(8), p. 2, already characterize
the exact entanglement minimum from several Hermitian expectation values
by a jointly optimized Legendre transform, with a pure-state conjugate
for convex roofs. Eisert–Brandao–Audenaert,
[quant-ph/0607167v4](https://arxiv.org/abs/quant-ph/0607167v4),
27 August 2013 version stamp, Eqs. (21)–(30), p. 4, gives the parallel
convex-roof framework and its tightness. These directly supply the general
two-data variational method, not merely an analogy to it.

For the fixed qutrit readouts `A_0=1⊕Z`, `A_1=1⊕X`, insert
`W_0=A_0 tensor X`, `W_1=A_1 tensor Z` into that prior theorem. Its
conjugate separates into the classical block and the qubit block: a local
block measurement preserves the scores and decreases E_F. For a>=b>=0,
the classical support is sqrt(a^2+b^2); the qubit support is
`a+f*(b)`, where `f*(b)=max_v[bv-f(v)]`. The latter follows from
the established two-qubit pure correlation singular values (1,v,v)
and their entropy f(v); alignment attains a+bv at fixed v. Therefore
the supplied specialization is exactly the existing dual

$$
M(a,b)=\max\{\sqrt{a^2+b^2},\ a+f^*(b)\}.
\tag{7}
$$

The source theorem supplies the abstract tight transform. The block
evaluation, the full phase/contact calculation, and the proof that this
fixed pair suffices even when Alice's readouts are unrestricted are the
task-specific calculations. Calling joint optimization of two correlations
a new general method would be incorrect.

Das–Datta–Jebaratnam–Majumdar,
[1702.00672v5](https://arxiv.org/abs/1702.00672v5),
*Cost of Einstein-Podolsky-Rosen steering in the context of extremal boxes*,
Eqs. (14)–(15), p. 3, defines a box decomposition weight, not entropy.
Its colored-BB84 Eq. (69), p. 8, reduces to matching correlations (1,V)
after an output sign change; Theorem 2, p. 9, gives weight V. The same
axis has entropy cost f(V)<V for 0<V<1. Thus different resource functions
already occur in this close two-setting scenario. That theorem does not
state the full entropy phase calculation or the optimizer incompatibility
in (5). This is a specific comparison, not an exhaustive originality claim.

The previously identified Tomassoli full-text gap remains unresolved.
No new attempt to bypass its access restriction was made.

## 4. Every full-rank two-input joint optimum is projective

There is also an all-state structural deduction for the weaker joint-query
route. It does not require a product eigenbasis or any restriction on
collective encoding. Fix one context b in {XX,XZ,ZX,ZZ}. In its four-vector
product basis write

$$
D_{s|b}=\frac{s_1P_{1,b_1}+s_2P_{2,b_2}}2
=\Pi_s-\Pi_{-s},\qquad
J_b(\rho)=\max_{\Gamma_s\succeq0,\ \sum_s\Gamma_s=\rho}
\sum_s\operatorname{Tr}(D_{s|b}\Gamma_s).
\tag{8}
$$

Each Pi_s is a rank-one basis projector. This is the existing joint
Hamming-score optimization; `j_2=(1/4)sum_b J_b` and `j_2<=f_2`.

**Theorem 3.** For every positive-definite two-qubit rho, every optimal
four-outcome readout in the four-dimensional canonical purification is
a rank-one projective measurement. For singular rho an optimal such
four-dimensional projective readout still exists, but its compression to
the support of rho can be a general POVM.

**Proof.** For rho>0 the primal in (8) is strictly feasible at
Gamma_s=rho/4. Its dual has an attained minimum

$$
\min_Y\operatorname{Tr}(\rho Y),\qquad Y\succeq D_{s|b}\quad\forall s.
\tag{9}
$$

A scalar Y>I is strictly dual feasible. For an optimal Y, the paired
constraints Y>=±D_{++} and Y>=±D_{+-} imply Y>=0. If Yv=0,
positivity of Y±D implies Dv=0 for both D's: their quadratic forms at v
must vanish, and a positive matrix with zero quadratic form annihilates v.
But `D_{++}^2+D_{+-}^2=I`, so v=0. Thus Y is positive definite.

For each sign pair,
`Y-D_s=(Y+Pi_{-s})-Pi_s`. Subtracting a rank-one matrix from the positive
definite first term leaves a kernel of dimension at most one. Optimal
primal/dual complementarity gives
`range(Gamma_s) subset kernel(Y-D_s)`, hence rank Gamma_s<=1. Four
such positive terms sum to rank-four rho, so all four have rank one.
Their normalized effects `E_s=rho^(-1/2)Gamma_s rho^(-1/2)` sum to I.
Four rank-one positive effects summing to I in dimension four are
orthogonal rank-one projectors: their four weighted defining vectors
are the columns of a square matrix V with VV^dagger=I, hence V is unitary.
In the canonical purification a transpose may be needed to identify the
physical effects; it preserves this conclusion.

For singular rho apply the full-rank result to
`rho_e=(1-e)rho+e I/4`. The set of four ordered rank-one projectors is
compact. Along a convergent subsequence their score converges to the
score at rho. The maximum in (8) is continuous in rho, as is also seen
by maximizing the continuous canonical-purification score over the compact
set of four-outcome POVMs. Thus the limit projective measurement is optimal.
This argument does not assert an attained full-space dual at singular rho;
the caveat established in the preceding audit remains in force.

### A smaller exact variational domain

The earlier one-effect formula groups the two equal-sign guesses into F.
Theorem 3 shows that its maximum can always be attained at

$$
F=\sqrt\rho\,\Pi\sqrt\rho,\qquad \Pi^2=\Pi=\Pi^\dagger,
\quad\operatorname{rank}\Pi=2.
\tag{10}
$$

Indeed take Pi to be the sum of the two equal-sign projectors in the
steering representation of an optimal readout. Conversely every (10) is
feasible for 0<=F<=rho, so
restricting the maximum to (10) leaves its value unchanged. Thus the
exact scalar square-root objective in
[the earlier formula](ROOF_PROVENANCE_AND_JOINT_SCORE.md#5-exact-two-qubit-reduction-and-the-remaining-analytic-obstruction)
needs only the complex Grassmannian of rank-two subspaces of C^4.
For full-rank rho the two optimal output-bit observables commute and are
balanced reflections (two positive and two negative eigenvalues).

This is an existence/necessity theorem for joint decoders, derived from
standard semidefinite duality and complementarity. It does not turn local
query decoders into compatible ones or evaluate the outer entropy maximum.
For a rank-three seed it does not restrict the physical qutrit decoder
to projective measurements: the support compression is essential. The
rank argument is particular to two bits; higher-bit Hamming payoffs have
more than one positive eigenvalue. Novelty of this specialized decoder
statement has not been certified.

## 5. Unrestricted attempt, verification, and remaining gap

The sharp original target remains

$$
g_n(\rho)=\sum_{i,b}\|\sqrt\rho P_{i,b}\sqrt\rho\|_1
\le\sqrt2 n+(2-\sqrt2)S(\rho).
\tag{11}
$$

Theorems 1–2 concern a single trusted site. Ordinary negativity supplies
no established linear monogamy statement that turns (1) into (11).
Optimizer incompatibility does not identify an unrestricted interface
optimum. No all-state proof or admissible counterexample was obtained.

A bounded two-input exploration examined the genuine local objective and
the common-state joint SDP from the preceding report. The latter used
six deterministic initial states and eight updates each; none yielded a
positive entropy excess. Forty of the 48 solver outputs had
inaccurate-optimum statuses, with small positivity residuals; none is a
rigorous cover.
Separate small local searches likewise produced no certified violation.
These exploratory failures are not upper bounds and are not used in any
proof or novelty claim. They are not new regression tests.

One precise sufficient spectral statement remains open. For ordered
eigenvalues l_1>=l_2>=l_3>=l_4 and `h(r,s)=sqrt(r^2+6rs+s^2)`, define

$$
B(l)=\sqrt2[h(l_1,l_2)+h(l_1,l_3)+h(l_2,l_4)+h(l_3,l_4)].
$$

This is the exact maximum among product-bisector eigenbases with that
spectrum: the cube edges exclude the opposite pairing (1,4),(2,3),
which minimizes the excluded matching since
`partial_r partial_s h=8rs/(r^2+6rs+s^2)^(3/2)>=0`.
The existing product-diagonal theorem bounds B(l) by the right side of
(11). But `g_2(rho)<=B(spectrum(rho))` for arbitrary entangled eigenvectors
is **unproved**. The small search is not a justification for inserting
that claim into a converse. It is stronger than the desired two-input
entropy inequality and is not an equivalence to it.

Independent internal reconstructions checked the dilation, block
normalizations, partial-transpose bound, equality contacts and the exact-axis
exception in (5). Separate reviews checked the projective-decoder proof,
including dual attainment and the singular limit. Primary statements above
were read directly. The results
do not depend on numerical optimization. Earlier construction diagnostics
were unchanged and were not rerun. LICENSE and the historical initial audit
are preserved. Publication originality and unrestricted equal-accuracy
optimality remain open.
