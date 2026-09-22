# Spectral tails cannot create an infinitesimal entropy witness

Date: 22 September 2026. Research base:
`6ddc97a549316ed9edb7a14a110ceee70b87bdf9`.

**Status:** supplied analytical deduction, independently reconstructed within
this workspace. Publication novelty remains unresolved. This note supplies a quantitative
spectral-tail criterion and an existential neighborhood theorem at each
fixed block size; it does not settle the unrestricted entropy inequality.

Put `c=2-sqrt(2)` and

$$
\Delta_n(\rho)=\sqrt2 n+cS(\rho)-g_n(\rho),\qquad
 g_n(\rho)=\sum_{P\in\{X_i,Z_i\}}\|\sqrt\rho P\sqrt\rho\|_1.
$$

## Block trace-norm lemma

Let A be an invertible Hermitian matrix on a finite-dimensional subspace,
let `mu=min |spec(A)|>0`, and let B,C be matrices making

$$M=\begin{pmatrix}A&B\\B^\dagger&C\end{pmatrix}$$

Hermitian. Then

$$
\|M\|_1\le\|A\|_1+\|C\|_1+\frac{2\|B\|_2^2}{\mu}.
\tag{1}
$$

Here `||.||_2` is Hilbert--Schmidt norm, not operator norm.

To prove (1), choose an optimal Hermitian trace-norm dual contraction
`T=[[D,E],[E^dagger,F]]`. Since `T^2<=I`, we have
`D^2+EE^dagger<=I`. With `J=sign(A)`, the matrix
`I-(JD+DJ)/2` is positive semidefinite. Because `|A|` commutes with J,

$$
\begin{aligned}
\|A\|_1-\operatorname{Tr}(AD)
&\ge\mu\bigl(r-\operatorname{Tr}(JD)\bigr)\\
&\ge\frac\mu2\operatorname{Tr}(I-D^2)
\ge\frac\mu2\|E\|_2^2.
\end{aligned}
$$

The middle inequality is `Tr(D-J)^2>=0`. Therefore

$$
\operatorname{Tr}(MT)
\le\|A\|_1+\|C\|_1+2\|B\|_2\|E\|_2-\frac\mu2\|E\|_2^2
\le\|A\|_1+\|C\|_1+2\|B\|_2^2/\mu.
$$

## Quantitative spectral-tail criterion

Let sigma,tau be density matrices with orthogonal supports and let
`rho=(1-epsilon)sigma+epsilon tau`, `0<epsilon<1`. Suppose each query
compression

$$
M_P=\sqrt\sigma P\sqrt\sigma\big|_{\operatorname{supp}\sigma}
$$

is invertible, and put `mu_P=min |spec(M_P)|`. Define

$$
K(\sigma)=\sum_P\left(1+\frac{2\|\sigma\|_\infty}{\mu_P}\right).
\tag{2}
$$

Then, irrespective of the tail eigenvectors,

$$
g_n(\rho)\le(1-\epsilon)g_n(\sigma)+\epsilon K(\sigma),
\tag{3}
$$

and consequently

$$
\Delta_n(\rho)\ge
(1-\epsilon)\Delta_n(\sigma)
+c h_2(\epsilon)-[K(\sigma)-\sqrt2 n]\epsilon
+c\epsilon S(\tau).
\tag{4}
$$

Indeed, the blocks of each sandwiched query are

$$
A=(1-\epsilon)M_P,\quad
B=\sqrt{\epsilon(1-\epsilon)}\sqrt\sigma P\sqrt\tau,
\quad C=\epsilon\sqrt\tau P\sqrt\tau.
$$

They obey `||C||_1<=epsilon` and
`||B||_2^2<=epsilon(1-epsilon)||sigma||_infty`. Applying (1), whose
minimum absolute eigenvalue is `(1-epsilon)mu_P`, proves (3).
Orthogonality gives the exact entropy identity

$$
S(\rho)=h_2(\epsilon)+(1-\epsilon)S(\sigma)+\epsilon S(\tau),
$$

which yields (4).

Whenever `Delta_n(sigma)>=0`, a simple sufficient condition is

$$
0<\epsilon<
2^{-[K(\sigma)-\sqrt2 n]/c}.
\tag{5}
$$

It makes (4) strictly positive, because
`h_2(epsilon)>epsilon log_2(1/epsilon)` for `0<epsilon<1`.
This criterion is deliberately conservative; neither its constant nor
its sharpness is claimed. It applies, in particular, when sigma is the
normalized spectral truncation of rho to its largest one or two
eigenvalues and has the stated nonzero compression gaps. The existing
rank-two entropy theorem then certifies `Delta_n(sigma)>=0`.

## A neighborhood theorem for the entire rank-two boundary

**Theorem.** For every fixed `n>=2`, there is a number `delta_n>0` such
that any n-qubit density matrix with

$$
1-\lambda_1(\rho)-\lambda_2(\rho)<\delta_n
\tag{6}
$$

satisfies `Delta_n(rho)>=0`. The conclusion is strict when `rank(rho)>2`.
No explicit universal value of delta_n, or dimension-independent
lower bound on it, is asserted.

The proof uses the previously established
[rank-two spectrum theorem](ENTROPY_INEQUALITY_BOUNDARIES.md), Section 1,
and its equality cases from
[the one-qubit rigidity theorem](ONE_QUBIT_OPTIMALITY.md), Section 5; it does not assume the unrestricted entropy conjecture.
All rank-at-most-two states satisfy `Delta_n>=0`. Equality occurs only at
pure products of X/Z bisectors, and at a maximally mixed retained qubit
tensored with pure X/Z bisectors on the other sites (any retained site
and either bisector signs are allowed).

For completeness, a pure state has query score
`sum_i (|<X_i>|+|<Z_i>|)<=n sqrt(2)`. Equality requires every local
Bloch vector to be a unit X/Z bisector. Every one-qubit marginal is then
pure, forcing a product of those bisectors. At rank two, the scalar
entropy inequality in the spectrum theorem is strict unless the two
eigenvalues are equal; the cited rigidity theorem then gives the
retained-site form above. Thus there are no unclassified rank-two
equality states being excluded by assumption.

At a pure equality state, each one-dimensional compression has absolute
eigenvalue `1/sqrt(2)`. At a rank-two equality state, its two supported
compression eigenvalues have absolute value `1/2` for a query on the
retained site and `1/(2sqrt(2))` for every other query. Thus every equality
state has strictly positive supported compression gaps.

Consider any equality state rho_* of rank r=1 or r=2. For rho sufficiently
close to rho_*, its top-r spectral truncation is uniquely separated from
the remaining eigenvalues. Writing it as
`rho=(1-epsilon)sigma+epsilon tau`, the normalized top-r state sigma
converges to rho_*, while epsilon tends to zero. The supported singular
values of `sqrt(sigma)P sqrt(sigma)` are continuous, so K(sigma) remains
bounded by a finite constant in a small neighborhood. Also
`Delta_n(sigma)>=0`, by the rank-two theorem. The ratio
`h_2(epsilon)/epsilon` diverges as epsilon tends to zero; equation (4)
therefore proves `Delta_n(rho)>0` whenever epsilon>0 and rho is close
enough. If epsilon=0, rho itself has rank at most two and is already
covered. This gives an open neighborhood of every equality state in which
the desired entropy inequality holds; for rank greater than two it is
strict.

Every other rank-at-most-two state has a strictly positive Delta_n, so
continuity supplies a neighborhood with the same property. The union of
these neighborhoods is an open set containing the compact set of all
rank-at-most-two density matrices. If no delta_n in (6) existed, one
could choose a sequence of counterexamples with tails tending to zero.
A convergent subsequence would approach a rank-at-most-two state, hence
would eventually enter that open set, a contradiction. The identical
argument applied to states of rank greater than two with Delta_n<=0
establishes the claimed strictness.

In particular, a possible two-input entropy witness cannot be an
arbitrarily small spectral-rank expansion of the known rank-two family:
it needs a third eigenvalue bounded away from zero at that fixed n.
Indeed, `1-lambda_1-lambda_2 <= (2^n-2)lambda_3`, so every witness has
`lambda_3 >= delta_n/(2^n-2)`. This is an existential compactness conclusion at fixed n,
not a numerical exclusion interval and not a proof for all rank-three
states. It does not change the operational encoder class, which remains
unrestricted.

## Explicit compression-gap neighborhood of a subset optimizer

The qualitative theorem does not hide a numerical value of delta_n.
The following separate, conservative estimate gives a directly checkable
local criterion. Let sigma_* be a rank-r equality state, with r=1 or 2,
and let sigma be a rank-r density matrix obeying

$$
\|\sigma-\sigma_*\|_\infty\le t.
$$

Set `a_*=||sigma_*||_infty` and
`m_*=min_P min |spec(sqrt(sigma_*)P sqrt(sigma_*))|` on its support.
The values are `(a_*,m_*)=(1,1/sqrt(2))` at a pure optimizer and
`(1/2,1/(2sqrt(2)))` at a rank-two optimizer for `n>=2`. The elementary
operator square-root estimate
`||sqrt(sigma)-sqrt(sigma_*)||_infty<=sqrt(t)` gives

$$
\|\sqrt\sigma P\sqrt\sigma-\sqrt{\sigma_*}P\sqrt{\sigma_*}\|_\infty
\le (\sqrt{a_*+t}+\sqrt{a_*})\sqrt t.
\tag{7}
$$

The square-root estimate follows from `sigma<=sigma_*+t I`, operator
monotonicity of the square root, and
`sqrt(sigma_*+t I)<=sqrt(sigma_*)+sqrt(t) I`, together with the
reverse inequality obtained by exchanging the two states. Singular-value
perturbation then proves

$$
\mu_P\ge m_*-(\sqrt{a_*+t}+\sqrt{a_*})\sqrt t.
\tag{8}
$$

If the right side is a positive number m, equation (2) gives

$$
K(\sigma)\le 2n\left(1+\frac{2(a_*+t)}{m}\right).
\tag{9}
$$

Equations (5) and (9) certify sufficiently small orthogonal spectral tails
uniformly over all such support rotations. They allow arbitrary tail
eigenvectors and are not limited to a classical flag state. Their constants
are intentionally loose; using the individual measured compression gaps
in (2) gives a stronger sufficient condition. At a pure reference optimizer,
sigma is taken to have rank one; at a rank-two reference optimizer it has
rank two. Applying the rank-two truncation near a pure reference would
incorrectly allow its smallest supported compression gap to collapse.

## Sharper tail bound at an exact subset core

The preceding criterion allows the core's support to rotate. At an exact
subset core, the orthogonal query-flipped supports give a sharper bound
whose extra score coefficient is independent of n.

Let J be a set of q retained sites, with `0<=q<n`, let r=`2^q`, and put

$$
\Pi=I_J\otimes\bigotimes_{i\notin J}
 |\beta_i\rangle\langle\beta_i|,
\qquad \sigma=\Pi/r,
$$

where each beta_i is an X/Z bisector state. Let tau be any density matrix
supported in the orthogonal complement of Pi, and set
`rho=(1-epsilon)sigma+epsilon tau`, with `0<epsilon<1`. Then

$$
\boxed{
 g_n(\rho)\le (1-\epsilon)g_n(\sigma)
 +\epsilon g_n(\tau)+2\sqrt2\,\epsilon.
}
\tag{10}
$$

Since `S(sigma)=q` and
`g_n(sigma)=2q+sqrt(2)(n-q)`, the core satisfies `Delta_n(sigma)=0`.
The exact orthogonal-mixture entropy identity therefore gives

$$
\boxed{
 \Delta_n(\rho)\ge
 \epsilon\Delta_n(\tau)+c h_2(\epsilon)-2\sqrt2\,\epsilon.
}
\tag{11}
$$

### Proof of the refined coefficient

For each discarded site i, let Pi_i be the rank-r projector obtained from
Pi by replacing its factor `|beta_i><beta_i|` with the orthogonal bisector
projector `|beta_i^perp><beta_i^perp|`. The projectors Pi_i are mutually
orthogonal and orthogonal to Pi, so `sum_i Pi_i<=I-Pi`.

Apply the block trace-norm lemma (1) to each query, keeping the actual
Hilbert--Schmidt norm of its off-diagonal block rather than the uniform
bound used in (3). A retained-site query preserves the core support and
has zero off-diagonal block. At a discarded site i, either query P has
supported compression gap

$$
\mu_P=\frac{1}{\sqrt2\,r}.
$$

Write `C_P=sqrt(sigma)P sqrt(tau)`. The off-diagonal block in (1) is
`sqrt(epsilon(1-epsilon)) C_P`, and its leading-block gap is
`(1-epsilon)mu_P`. Because tau is supported outside Pi,

$$
\begin{aligned}
\|C_P\|_2^2
&=\frac1r\operatorname{Tr}(\tau P\Pi P)\\
&=\frac{1}{2r}\operatorname{Tr}(\tau\Pi_i).
\end{aligned}
$$

The second identity uses
`(I-Pi)P Pi P(I-Pi)=Pi_i/2`: either X or Z takes a bisector into its
original direction and its orthogonal bisector with equal squared
amplitudes. The cross terms vanish against tau's support condition.
The gain term in (1) is thus at most

$$
\frac{2\epsilon\|C_P\|_2^2}{\mu_P}
=\sqrt2\,\epsilon\operatorname{Tr}(\tau\Pi_i).
$$

Summing both queries at each discarded site gives at most
`2sqrt(2)epsilon sum_i Tr(tau Pi_i)<=2sqrt(2)epsilon`.
The diagonal-block trace norms sum exactly to
`(1-epsilon)g_n(sigma)+epsilon g_n(tau)`. This proves (10), and the
entropy identity proves (11).

### Two explicit sufficient tail cutoffs

If the tail itself satisfies `Delta_n(tau)>=0`, then

$$
0<\epsilon\le 2^{-(2+2\sqrt2)}
=0.03519642908204362\ldots
\quad\Longrightarrow\quad \Delta_n(\rho)>0.
\tag{12}
$$

Indeed, `2sqrt(2)/c=2+2sqrt(2)`, and
`h_2(epsilon)>epsilon log_2(1/epsilon)` for `0<epsilon<1`.
For an arbitrary tail, the elementary bounds `g_n(tau)<=2n` and
`S(tau)>=0` give `Delta_n(tau)>=-cn`. Consequently

$$
0<\epsilon\le 2^{-n-(2+2\sqrt2)}
\quad\Longrightarrow\quad \Delta_n(\rho)>0,
\tag{13}
$$

with no entropy-inequality assumption on tau. These are conservative
sufficient cutoffs, not sharp transition values. They require the exact
subset core specified above; equations (7)--(9) handle support rotations
with different, weaker constants. For `n=2,q=1`, every mixture in this
exact-core construction is already classical on the discarded site and
is therefore globally covered by the
[classical-flag theorem](CLASSICAL_FLAG_ENTROPY_BOUND.md). The numerical
cutoff in that case is an illustration of (12), not a newly excluded
family.

The score coefficient `2sqrt(2)` in (10) is sharp to first order in
small epsilon. Take `tau=Pi_i/r` for one discarded site. The state rho
then differs from the core only by mixing the two orthogonal bisectors
on that site, while `g_n(tau)=g_n(sigma)`. The single-qubit score formula
gives the exact gain

$$
\begin{aligned}
g_n(\rho)-[(1-\epsilon)g_n(\sigma)+\epsilon g_n(\tau)]
&=\sqrt2\left(\sqrt{1+4\epsilon(1-\epsilon)}-1\right)\\
&=2\sqrt2\,\epsilon+O(\epsilon^2).
\end{aligned}
\tag{14}
$$

Thus a uniformly smaller linear coefficient cannot replace `2sqrt(2)`
in (10). This sharpness statement concerns the score estimate; it does
not make either sufficient entropy cutoff sharp.

## Scope and provenance

The block estimate uses trace-norm duality, a quadratic completion, and
finite-dimensional spectral continuity. The entropy identity is the usual
one for orthogonal mixtures. The prior rank-two theorem and its equality
classification are essential inputs. The new consequence supplied here is
the exclusion of a full open neighborhood of the entire rank-at-most-two
set, including nearby states with coherent eigenvectors and higher rank.
No absence from the prior literature is asserted.

The seed is a mathematical Gram matrix in the
[normalized-seed reduction](COLLECTIVE_ENCODING_REDUCTION.md). The result
places no restriction on the actual physical encoder. One unknown specimen,
one delayed query, unrestricted collective encoding, unlimited finite
classical records, a worst-case quantum dimension cap, and uniform
arbitrary-input error all remain as specified in the model. An entropy
witness of rank three or higher may still exist outside the proved
neighborhood; the theorem does not give an explicit search cutoff without
additional quantitative work.
