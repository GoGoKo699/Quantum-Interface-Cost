# Flat seeds and quantum Boolean-function results

Date: 2026-09-22. Research base:
`87b6432cdd1f29bc4981f24bd6732bb933741193`.
Status: targeted primary-source comparison, with the normalization and
elementary deductions below supplied explicitly. This is not an exhaustive
novelty certification.

The new flat-spectrum question asks whether, for every rank-four projector
P on three qubits,

$$
g(P/2)=\frac14\sum_{i=1}^3\sum_{b=X,Z}\|P P_{i,b}P\|_1
\le 4+\sqrt2.
\tag{1}
$$

Here the normalized seed is $L=P/2$, its Gram matrix is $\rho=P/4$,
and the norm is the ordinary trace norm. The
[flat-seed proof](FLAT_HALF_RANK_OPTIMALITY.md) establishes
(1) using the reflection $S=2P-I$ and the exact spectrum of a sum of three
commuting single-site observables. Quantum Boolean-function theory is
therefore close prior mathematics. Its terminology and qualitative
rigidity must be credited, while its existing conclusions must be compared
with the actual trace-norm objective.

The proof also covers every rank-eight projector on four qubits, with
score at most $6+\sqrt2$. More generally, for any n it proves
$g(\sqrt{P/2^{n-1}})\le2(n-1)+\sqrt2$ whenever the singleton X/Z
Fourier projection of $2P-I$ is supported on at most four sites. This
condition allows higher-degree terms involving arbitrarily many sites;
it does not require P itself to act on only four qubits. The three-qubit
case below makes the distinction from prior FKN statements explicit.

## 1. Precise source statements

**Montanaro–Osborne**, *Quantum boolean functions*: both
[arXiv:0810.2435v3](https://arxiv.org/pdf/0810.2435v3), 24 April 2009,
and [v5](https://arxiv.org/pdf/0810.2435v5), 24 August 2010, were
retrieved. These dates agree with the
[arXiv submission history](https://arxiv.org/abs/0810.2435).

| Statement | v3 locator | v5 locator |
|---|---|---|
| No Fourier mass above degree one implies a single-site operator or constant | Proposition 57, p. 31 | Proposition 59, p. 31 |
| Tail mass below $\varepsilon$ implies $K\varepsilon$ closeness to that family, for universal K | Theorem 58, p. 31 | Theorem 60, p. 32 |
| $\delta$ closeness means squared normalized Hilbert–Schmidt distance at most $4\delta$ | Definition 11, p. 11 | Definition 11, p. 11 |
| $\operatorname{Var}(S)\le I(S)$ | Proposition 71, Eq. (163), p. 37 | Proposition 72, Eq. (163), p. 38 |

All page numbers are printed pages. The relevant conclusions agree across
these versions; v5 does not add an exact local-X/Z compression optimum.
The published paper has different theorem numbering again. For the FKN
proof issue, use the later comparison below.

**Blecher–Gao–Xu**, *Geometric influences on quantum Boolean cubes*,
[arXiv:2409.00224v1](https://arxiv.org/pdf/2409.00224v1), version dated
30 August 2024: Section 6, **Lemma 6.1, printed p. 32**, bounds squared
distance to a single-site operator by $K\varepsilon$, where
$\varepsilon=\|S^{>1}\|_{2,\tau}^2$. **Theorem 6.2, printed p. 34**,
replaces that operator by a single-site Hermitian unitary, with another
universal constant. The proof of Lemma 6.1, pp. 33–34, uses
$\varepsilon\le10^{-6}$ for its nontrivial estimate and the coarse
bound $10^7\varepsilon$ otherwise. Its Section 6 footnote, p. 32,
identifies a fixable issue in the earlier FKN proof and supplies an
alternative argument. Thus the FKN conclusion is prior work, and the
later proof is the appropriate reference when relying on its stability
form. These statements concern all Pauli directions, not only X and Z.

## 2. Mapping the quantities exactly

For the remainder let $d=2^n$, $r=d/2$, $P$ be a rank-r projector,
$S=2P-I$, and $\tau(A)=\operatorname{Tr}(A)/d$. Then

$$
S=S^\dagger,\qquad S^2=I,\qquad \tau(S)=0.
$$

Thus S is exactly a balanced quantum Boolean function in the cited
framework. Expand it in the orthonormal Pauli basis,

$$
S=\sum_{w\in\{I,X,Y,Z\}^n}s_w\sigma_w,
\qquad s_{I^n}=0,\qquad\sum_w s_w^2=1.
$$

Let $\mathcal E_i$ be normalized partial trace over site i, with the local
identity reinserted. The standard site influence is

$$
I_i(S)=\|S-\mathcal E_i(S)\|_{2,\tau}^2
=\sum_{w:w_i\ne I}s_w^2,
\qquad
I(S)=\sum_w |w|s_w^2.
\tag{2}
$$

For a queried local Pauli U define instead

$$
w_U=\left\|\frac{S-USU}{2}\right\|_{2,\tau}^2
=\sum_{w:\sigma_wU=-U\sigma_w}s_w^2.
\tag{3}
$$

At a given site, X anticommutes with Y and Z, and Z anticommutes with
X and Y. Therefore

$$
w_{X_i}+w_{Z_i}
=I_i(S)+\sum_{w:w_i=Y}s_w^2,
$$

and, summing sites,

$$
\boxed{\sum_{i,b=X,Z}w_{P_{i,b}}
=I(S)+\sum_w N_Y(w)s_w^2.}
\tag{4}
$$

The queried energy counts a Y letter twice and an X or Z letter once.
It is not the standard total influence. A general local change of basis
preserves standard influence but changes this query-dependent quantity.

There is a second distinction: even (3) is an energy, not the seed's root
fidelity. Write

$$
F_U=\|\sqrt\rho U\sqrt\rho\|_1=\frac1r\|PUP\|_1,
\qquad \rho=P/r.
$$

Direct expansion of $P=(I+S)/2$ gives

$$
\frac1r\operatorname{Tr}(PUPU)
=\frac{1+\tau(SUSU)}2=1-w_U.
$$

If $t_1,\ldots,t_r\in[0,1]$ are the singular values of the compression
of U to $\operatorname{ran}P$, then

$$
F_U=\frac1r\sum_k t_k,\qquad
1-w_U=\frac1r\sum_k t_k^2.
$$

Consequently

$$
1-w_U\le F_U\le\sqrt{1-w_U},
\qquad
\frac{w_U}{2}\le1-F_U\le w_U.
\tag{5}
$$

No identity equating a fidelity deficit with the standard influence is
available from these formulas. Replacing one by the other would lose both
the Pauli-direction weights and the compression's singular-value data.

## 3. What the prior bounds yield for this objective

The Poincare statement and (4) imply $\sum_Uw_U\ge1$. Equation (5) and
Cauchy–Schwarz then give the following valid but nonsharp deduction:

$$
g(\sqrt\rho)=\sum_U F_U
\le\sqrt{2n\left(2n-\sum_Uw_U\right)}
\le\sqrt{2n(2n-1)}.
\tag{6}
$$

For three qubits this is $\sqrt{30}\simeq5.477226$, whereas the sharp
flat-seed value is $4+\sqrt2\simeq5.414214$. The numerical comparison
concerns two explicit analytic bounds, not an optimization experiment.

To locate the extra structural step, define the singleton X/Z mass

$$
T=\sum_{i=1}^3(s_{X_i}^2+s_{Z_i}^2).
$$

Every other nonidentity Pauli string contributes at least two per unit
squared coefficient in (4). Hence $\sum_Uw_U\ge2-T$ and

$$
g(\sqrt\rho)^2\le6(4+T).
\tag{7}
$$

A putative score exceeding $4+\sqrt2$ would require

$$
T>\frac{4\sqrt2}{3}-1\simeq0.885618.
\tag{8}
$$

The usual FKN tail is instead
$\varepsilon=\sum_{|w|>1}s_w^2\le1-T$; singleton Y terms belong to
degree one in that theorem. FKN gives an approximate single-site
description. Its stated universal-constant conclusion, and the concrete
coarse constants above, do not by themselves turn the entire range (8)
into the exact bound (1).

The additional elementary observation specific to three sites uses

$$
L=\sum_{i=1}^3(s_{X_i}X_i+s_{Z_i}Z_i)
=\sum_{i=1}^3\beta_i B_i,
\qquad \beta_i=\sqrt{s_{X_i}^2+s_{Z_i}^2}.
$$

Each nonzero $B_i$ is a single-site reflection, and the three $B_i$
commute. Hilbert–Schmidt projection and trace-norm duality give
$T=\tau(SL)\le\tau|L|$. Evaluating the eight signed eigenvalues gives

$$
\tau|L|=\max\left\{\max_i\beta_i,
\frac{\beta_1+\beta_2+\beta_3}{2}\right\}.
\tag{9}
$$

Since $T=\sum_i\beta_i^2$, the second alternative is at most
$\sqrt{3T}/2$. Thus $T>3/4$ forces $\max_i\beta_i\ge T$.
This exact finite-dimensional constraint, followed by query-specific
compression bounds, is the additional argument in the flat-seed proof.
The spectral evaluation is an elementary three-sign calculation; it
should not be advertised as a new general FKN theorem.

## 4. Scope of the novelty conclusion

Balanced reflections, Pauli Fourier analysis, Poincare bounds, and
degree-one rigidity and stability are established ingredients. The
supplied deduction evaluates a different, direction-dependent sum of
compression trace norms. The inspected FKN statements do not directly
state the rank-four three-qubit optimum, and their quantitative bounds
do not settle it through the substitutions above. This comparison leaves
open whether an equivalent sharp result appears elsewhere.

Flatness is a theorem hypothesis on a family of mathematical seeds. The
original interface still permits arbitrary collective encoders and
nonuniform seed spectra, so (1) alone does not establish
$\Gamma(3,4)=4+\sqrt2$. No additional copies, simultaneous query answers,
average memory, or postselected success are introduced by this comparison.

The completed proof additionally supplies separate flat lower-rank estimates,
so every allowed flat rank obeys the q=n-1 finite-budget benchmark for
n<=4. These elementary biased-reflection estimates do not extend the
claim to nonflat spectra, and do not rely on FKN stability constants.
