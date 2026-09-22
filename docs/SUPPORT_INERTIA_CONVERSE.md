# A support criterion excluding nonflat collective seeds

Date: 22 September 2026. Research base:
`6ddc97a549316ed9edb7a14a110ceee70b87bdf9`.

**Status:** analytical deduction with proof; the core argument has been
independently reconstructed within this workspace. Publication novelty
remains unresolved. The result applies to arbitrary
nonzero spectra on a specified support, including complex and entangled
eigenvectors. It does not prove the unrestricted rank or entropy conjecture.

Let

$$
g(\rho)=\sum_{i=1}^n\sum_{b=X,Z}
\|\sqrt\rho P_{i,b}\sqrt\rho\|_1,
\qquad c=2-\sqrt2.
$$

The [normalized-seed reduction](COLLECTIVE_ENCODING_REDUCTION.md) permits
every density matrix of rank at most `2^q`. Its subset benchmark is
`sqrt(2)n+cq`. The support condition below is an exclusion criterion for
candidate seeds; it is not an assumption imposed on physical encoders.

## 1. Inertia of the compressed observables

For a nonzero orthogonal projector P, call a site active when **both**
`PX_iP` and `PZ_iP`, restricted to `ran(P)`, have a strictly positive and
a strictly negative eigenvalue. Let a(P) be the number of active sites.
Zero eigenvalues are permitted. A site is inactive as soon as either
compressed observable is positive semidefinite or negative semidefinite;
the zero operator is both.

**Theorem.** Every density matrix rho with support projector P satisfies

$$
\boxed{g(\rho)\le\sqrt2 n+c\,a(P).}
\tag{1}
$$

In particular, when `rank(rho)<=2^q` and `a(P)<=q`, the seed cannot
improve the subset benchmark, whatever its nonzero eigenvalues are.
An entropy consequence is that any state with `S(rho)>=a(P)` satisfies
`g(rho)<=sqrt(2)n+cS(rho)`. Neither sufficient condition is necessary.

For an encoder, refine its classical branches to single Kraus matrices
`K_a` and set `rho_a=K_a^dagger K_a/||K_a||_F^2` for nonzero branches.
The established reduction gives
`2n eta<=sum_a (||K_a||_F^2/2^n) g(rho_a)`, with weights summing to one.
Hence an encoder beating the subset contrast must have at least one
normalized branch with `a(supp(rho_a))>q`. No favorable branch is
postselected: this is a necessary condition from the weighted upper bound
for the complete trace-preserving instrument.

**Proof.** On its support, rho is positive definite. The matrix
`sqrt(rho) P_{i,b} sqrt(rho)` is an invertible congruence of the
compression `P P_{i,b} P`. An invertible change of variables in its
quadratic form preserves the numbers of positive and negative directions.
Thus its inertia, and in particular semidefiniteness, depends only on P.

Choose a purification `|psi>` of rho on an auxiliary system Q. For every
query, trace-norm duality supplies a Hermitian reflection B on Q attaining
the score:

$$
F_{i,b}=\|\sqrt\rho P_{i,b}\sqrt\rho\|_1
=\langle\psi|P_{i,b}\otimes B_{i,b}|\psi\rangle,
\qquad B_{i,b}^2=I.
\tag{2}
$$

For example, take the canonical purification in the computational basis
and transpose a sign matrix of the sandwiched observable. At a zero
eigenvalue, the sign can be extended by either +1 or -1, so the decoder
can be chosen to square to I. All queried X/Z operators are real.

If the sandwiched observable is semidefinite, its dual reflection in (2)
can instead be chosen as the scalar `+I` or `-I`, respectively. At an
inactive site suppose, without loss of generality, that `B_{i,X}=sI`.
Then

$$
h_i=sX_i\otimes I+Z_i\otimes B_{i,Z},
\qquad h_i^2=2I.
\tag{3}
$$

The cross terms vanish because `X_i Z_i+Z_i X_i=0`; no dimension
restriction on Q was used. Consequently the sum of the two attained
scores at an inactive site is at most sqrt(2). Each query score is at
most one, so an active site contributes at most two. Summing gives (1).

This is the scalar-decoder step of the
[one-qubit proof](ONE_QUBIT_OPTIMALITY.md), used in arbitrary auxiliary
dimension. It does not extend that proof's three-qubit monogamy step to
larger memories.

## 2. Equality under the rank cap

**Proposition.** Suppose `rank(rho)<=2^q` and `a(P)<=q`. Equality with
the subset score holds if and only if rho is a subset seed Gram matrix:

$$
\rho=\frac{I_T}{2^q}\otimes
\bigotimes_{i\notin T}|\beta_i\rangle\langle\beta_i|,
\qquad |T|=q,
\tag{4}
$$

where each beta_i is an X/Z bisector, allowing independent signs of its
X and Z Bloch coordinates. The tensor factors may be reordered.

**Proof.** Since c is positive, equality forces `a(P)=q`. Every active
site must contribute two, so both of its scores in (2) are one. Root
fidelity between two normalized states is one only when those states
coincide. Using
`F_{i,b}=F(rho,P_{i,b} rho P_{i,b})`, it follows that rho commutes with
both local X and Z on every active site. Expanding rho in the Pauli basis
then gives

$$
\rho=\frac{I_T}{2^q}\otimes\sigma_{T^c}.
\tag{5}
$$

The rank cap forces sigma to have rank one. For this pure remaining
state, each query score is the absolute value of the corresponding
one-site Bloch coordinate. Saturating the inactive-site bound requires

$$
|x_i|+|z_i|=\sqrt2.
$$

Since `x_i^2+y_i^2+z_i^2<=1`, equality implies
`|x_i|=|z_i|=1/sqrt(2)` and `y_i=0`. Each one-site marginal is therefore
pure, so the remaining state is a product of the claimed bisectors.
Conversely, every state in (4) attains the score directly. Its active
sites are precisely T. This includes the endpoints q=0 and q=n.

This proposition classifies equality **within the support criterion**.
It does not classify unrestricted optimal seeds with more than q active
sites.

## 3. An explicit neighborhood around every subset support

Let T be a set of q sites and define the rank-`2^q` subset projector

$$
P_0=I_T\otimes
\bigotimes_{i\notin T}|\beta_i\rangle\langle\beta_i|.
$$

**Corollary.** If `rank(rho)<=2^q`, with support P, and

$$
\boxed{\|(I-P_0)P\|_\infty\le\sin(\pi/8),}
\tag{6}
$$

then `a(P)<=q`, so rho obeys the subset bound. Its nonzero eigenvalues
are unrestricted. Equality holds exactly when `rho=P_0/2^q`.

When P and P_0 have equal rank, the norm in (6) equals
`||P-P_0||_infinity`, the sine of the largest principal angle between
their ranges. The one-sided version in (6) also handles smaller ranks.

**Proof.** Fix a discarded site i. The range of P_0 lies in that of
`P_{0,i}=I_rest tensor |beta_i><beta_i|`. Hence (6) implies
`||(I-P_{0,i})P||_infinity<=sin(pi/8)`. Each unit vector in `ran(P)` can
be written

$$
|v\rangle=\cos\alpha\,|\beta_i\rangle|u\rangle
+\sin\alpha\,|\beta_i^\perp\rangle|w\rangle,
\qquad 0\le\alpha\le\pi/8,
\tag{7}
$$

with normalized u,w whenever their coefficient is nonzero. Select signs
s_X,s_Z so beta_i has expectations `s_X/sqrt(2),s_Z/sqrt(2)`. In this
local basis each signed Pauli has diagonal entries `+1/sqrt(2)` and
`-1/sqrt(2)`, with off-diagonal entry of absolute value `1/sqrt(2)`.
Consequently, for b=X,Z,

$$
\begin{aligned}
\langle v|s_b P_{i,b}|v\rangle
&\ge\frac{\cos^2\alpha-\sin^2\alpha
-2\cos\alpha\sin\alpha}{\sqrt2}\\
&=\frac{\cos(2\alpha)-\sin(2\alpha)}{\sqrt2}\ge0.
\end{aligned}
\tag{8}
$$

Thus both signed compressed queries are positive semidefinite at every
discarded site. Only the q sites in T can be active. Equations (1) and
(6) prove the claim. Section 2 restricts equality to a subset projector
`P_1` divided by `2^q`. If its retained set differs from T, a vector in
`ran(P_1)` can be chosen orthogonal to `ran(P_0)` on a site retained only
by `P_1`, giving one-sided distance one. If the retained sets agree but
some discarded bisector differs, the squared overlap of the discarded
product states is at most 1/2: distinct X/Z bisectors have squared overlap
0 or 1/2. The distance is then at least `1/sqrt(2)`. Neither possibility
satisfies (6), so `P_1=P_0`.

Equivalently, the worst leakage probability of a support vector outside
the subset subspace can be as large as

$$
\sin^2(\pi/8)=\frac{2-\sqrt2}{4}
=0.1464466094\ldots.
\tag{9}
$$

This is a nonzero neighborhood in support geometry for all spectra. It
is not a neighborhood in trace distance: a tiny eigenvalue on a distant
new direction changes the support and can invalidate (6).

## 4. Sharpness of the support-radius criterion

The radius pi/8 is sharp for guaranteeing semidefiniteness at a discarded
site. This is **not** a counterexample to the subset bound.

Take two input qubits A,B and put

$$
|\beta(t)\rangle=\cos(t)|0\rangle+\sin(t)|1\rangle,
\qquad t_0=\pi/8.
$$

Let P_theta project onto the orthonormal vectors

$$
|0\rangle_A|\beta(t_0+\theta)\rangle_B,
\qquad
|1\rangle_A|\beta(t_0-\theta)\rangle_B,
\tag{10}
$$

and let `P_0=I_A tensor |beta(t_0)><beta(t_0)|`. Both principal angles
are theta, so `||P_theta-P_0||_infinity=sin(theta)`. In the displayed
support basis the B-site compressions are diagonal:

$$
\begin{aligned}
P_\theta X_B P_\theta&\cong
\operatorname{diag}\bigl(\sin(\pi/4+2\theta),
                         \sin(\pi/4-2\theta)\bigr),\\
P_\theta Z_B P_\theta&\cong
\operatorname{diag}\bigl(\cos(\pi/4+2\theta),
                         \cos(\pi/4-2\theta)\bigr).
\end{aligned}
\tag{11}
$$

For every `pi/8<theta<pi/4`, both have one positive and one negative
eigenvalue. The A-site Z compression has eigenvalues +1,-1, while its
X compression has eigenvalues `+cos(2theta),-cos(2theta)`. Thus all four
compressions are indefinite immediately beyond the radius. Nevertheless
all spectra on this rank-two support satisfy the already proved
one-retained-qubit optimum. Indefiniteness is necessary for a possible
advantage in the regime considered below, not sufficient.

## 5. Consequence for the unresolved three-input block

At `n=3,q=2`, any seed beating `4+sqrt(2)` must have both compressed
queries indefinite at **each** of the three sites. Combining this with
the existing rank-two and flat-seed exclusions, a witness must have
nonuniform rank three or four and satisfy this inertia condition.

Moreover, for every site i and every one-site X/Z bisector beta,

$$
\|(I-I_{\rm rest}\otimes|\beta\rangle\langle\beta|)P\|_\infty
>\sin(\pi/8).
\tag{12}
$$

For rank four, this is an operator-norm distance condition from every
rank-four subset support. For rank three it remains a one-sided leakage
condition. These exact support restrictions apply before optimizing the
nonzero eigenvalues; no flat-spectrum assumption enters their proof.

The ingredients are elementary trace-norm duality, the anticommutation of
X and Z, invariance of inertia under an invertible congruence, and the
geometry of two subspaces. The arbitrary-dimension scalar-decoder argument
was already implicit in the repository's one-qubit proof. This note makes
its support and nonflat consequences explicit; no novelty claim is made.
The operational task remains one unknown specimen, one delayed query,
unrestricted collective encoding, unlimited finite classical records,
worst-case quantum dimension, and uniform arbitrary-input statistics.
