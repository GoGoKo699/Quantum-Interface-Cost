# Publication case and unrestricted optimality: a critical assessment

Date: 23 September 2026. Reviewed main:
`81bcfefb2b545742d513c4f51364a7f72972451e`.
Main and issues #1–#2 were rechecked; no open pull request or newer external
review was present at the start. This supplements, and does not rewrite,
the [historical audit](PROOF_AND_NOVELTY_AUDIT.md).

**Judgment:** there is a credible, narrowly scoped paper candidate, but the
dossier does not establish a new general compression framework or the
unrestricted equal-accuracy optimum. The full heterogeneous one-qubit
allocation theorem and the two-parameter steering-formation evaluation are
the strongest candidates. Several attractive scalar formulas are already
short consequences of prior work. More excluded seed families do not, by
themselves, strengthen the publication case or demonstrate proximity to a
general proof.

This is an internal mathematical and source assessment, not external peer
review or an acceptance prediction. The operational problem remains one
arbitrary unknown specimen, one delayed local query, arbitrary collective
encoding, unlimited finite classical records, a quantum dimension cap on
every branch, and uniform performance on every input and query.

## 1. What could carry a paper?

| Result | Prior overlap | Defensible contribution and limitation |
|---|---|---|
| Full dimension-two region `sum_i w(x_i,z_i)<=1`, every n | Cheng–Hall's independently optimized qubit CHSH monogamy supplies the central inequality; local incompatibility weight is established | Exact evaluation of an unrestricted collective simulation problem, with a matching construction. Strongest clean operational theorem. It is an application of monogamy, not a new monogamy principle. |
| Equality and stability for one retained qubit | Saturation analysis and spectral-gap methods are standard | Useful structural strengthening of that evaluation. It concerns normalized seeds and stated branch weights, not diamond-norm closeness of whole channels. |
| Complete `C(x,z)=E_FA(sigma_xz)` evaluation and its strict-saving boundary | Cope defines the resource and already supplies the exact-axis atom; the symmetric slice has the further prior derivation below | Most promising distinct analytic evaluation: the whole two-noisy-Pauli family and the boundary `2(1/ln2-1)^2`. The inspected sources do not state this full formula. Absence from those sources is not an exhaustive originality certificate. |
| `R_PD(x,z)=C(x,z)` | Entropy convex roofs and typical compression are established methods | Exact correlated product-diagonal benchmark and unrestricted achievability. The Gram restriction needs a clear reason to matter to a reader; it does not become an unrestricted converse. |
| Exact-axis spectral reduction and `R_X(z)=f(z)` | The induced-cube problem, sharp asymptotic curve and dephasing cost formula are prior | Claim the operational reduction, local-query converse and complete exact-axis instruments. Do not sell the scalar curve as newly discovered. |
| Unrestricted linear onset | Combines established QRAC/mixing and cube/coherence entropy inequalities | A meaningful scaling theorem. The coefficient gap is material, and the known ingredients deserve prominent attribution. |
| Spectral, kernel and neighborhood exclusions | Mostly task-specific consequences of known inequalities | Supporting research and possible appendix material. Neither their number nor passing diagnostics measures significance. |

The precise source maps for all but the additional comparison below are in
[LITERATURE_COMPARISON.md](../LITERATURE_COMPARISON.md) and
[ENTROPY_TRADEOFF_PRIOR_AUDIT.md](../ENTROPY_TRADEOFF_PRIOR_AUDIT.md).
In particular, Ioannou et al., [2202.12980](https://arxiv.org/abs/2202.12980),
Eq. (1), already contains the simulation model. Ballester–Wehner–Winter,
[quant-ph/0608014v2](https://arxiv.org/abs/quant-ph/0608014v2), Lemma 5.1,
subsumes its exact endpoint through the previously supplied ensemble map.
Cheng–Hall, [1610.09302v3](https://arxiv.org/abs/1610.09302v3), Eqs. (13)–(14),
printed p. 3, supplies the independently optimized common-qubit monogamy.

A defensible paper would lead with the complete one-qubit allocation
region and its structure, then show precisely how asymmetric collective
compression goes beyond retaining original sites. The full steering-cost
evaluation could be its second main theorem or a focused separate paper.
The many partial attacks on the equal-accuracy conjecture should not be
the main narrative. Publication does not require solving that conjecture,
but the paper's title, abstract and theorems must match the narrower result.

## 2. Additional subsumption: the symmetric one-site entropy curve

Zhu–Zhang–Ma, *Interplay among entanglement, measurement incompatibility,
and nonlocality*, [2303.08407v2](https://arxiv.org/pdf/2303.08407v2),
20 June 2025, Theorem 2 / Eq. (25), printed p. 14, gives

\[
 E_F(\omega)\ge
 \frac{S_{\rm CHSH}-2\alpha}{2\sqrt{1+\alpha^2}-2\alpha}.
\]

Their convention is Eq. (2), p. 5, with `alpha>=1`; the arbitrary-dimension
reduction is Appendix A.1, pp. 28–29. We need only `alpha=1`.
Cope, [2102.02333v2](https://arxiv.org/pdf/2102.02333v2), Theorem 2,
p. 3, identifies assemblage formation entropy with minimum compatible-state
entanglement of formation.

Here is the full specialization, rather than an inference from titles.
Let

\[
 \sigma_{\pm|X}=\frac{I\pm\eta X}{4},\qquad
 \sigma_{\pm|Z}=\frac{I\pm\eta Z}{4}.
\]

In any realization, the differences of the two outcome substates are
`eta X/2` and `eta Z/2`. Give the trusted qubit observables
`B_0=(X+Z)/sqrt(2)` and `B_1=(X-Z)/sqrt(2)`. The ordinary CHSH expectation is
therefore `2sqrt(2) eta`, independently of the untrusted dimension. The
two cited theorems imply

\[
 E_{FA}(\sigma_{\eta,\eta})\ge
 \left[\frac{\eta-1/\sqrt2}{1-1/\sqrt2}\right]_+.
\tag{1}
\]

The compatible assemblage at `eta_0=1/sqrt(2)` has a separable realization;
the unit-contrast assemblage has a Bell realization. A classical flag on
the untrusted side mixes them with weight
`t=(eta-eta_0)/(1-eta_0)`. This realizes the required assemblage with average
pure-state entanglement at most t. It matches (1); below the threshold the
assemblage is compatible. Thus the symmetric one-site formula is already
an exact short corollary of prior results.

This is additional subsumption of a slice, not of the whole profile theorem.
Cope's analytic family on p. 6, Eqs. (26)–(27), explicitly fixes one
measurement's two substates to rank-one orthogonal projectors. It supplies
the exact-axis atom, but does not evaluate both-noisy orthogonal profiles.
Ordinary CHSH at general `(x,z)` gives only
`[(sqrt(x^2+z^2)-1)/(sqrt(2)-1)]_+`; the full convex-envelope calculation
uses additional information. No claim is made here that all possible
reductions from weighted Bell inequalities have been exhausted.

Nor does (1) solve the many-site problem: summing local entanglement of
formation and charging it to one shared register's entropy is false in
general, as the W-state counterexample in the prior audit demonstrates.
Cope–Uola, [2207.05722v4](https://arxiv.org/pdf/2207.05722v4), Eq. (8) and
Section VI.1, also distinguishes an average dimension measure and full
tensor-product assemblages from the present worst-case, single-query task.

**Novelty verdict:** the strongest distinct analytic candidate is the evaluated
two-dimensional profile, its analytic boundary, and the stated restricted
tensorization. The framework, exact-axis atom and symmetric scalar slice
cannot be the novelty claim. Targeted primary-source checks have not found
the complete profile formula; that is a scoped finding, not proof that it
has never appeared.

## 3. The equal-accuracy question is an all-or-nothing rate problem

Put `eta_0=1/sqrt(2)`, `c=2-sqrt(2)`, and

\[
 H(\eta)=\frac{\eta-\eta_0}{1-\eta_0},\qquad
 g_n(\rho)=\sum_i\bigl(\|\sqrt\rho X_i\sqrt\rho\|_1+
                            \|\sqrt\rho Z_i\sqrt\rho\|_1\bigr).
\]

The proved [entropy characterization](../ENTROPY_RATE_CHARACTERIZATION.md)
states that R is convex, has endpoints `R(eta_0)=0`, `R(1)=1`, lies below H,
and equals the regularized minimum of `S(rho)/n` at
`g_n(rho)/(2n)>=eta`. It preserves the original worst-case physical resource
through complete instruments; virtual seed tensor powers are not extra
specimens or a postselection protocol.

The following elementary consequences clarify how large the remaining
problem is. They are deductions from that characterization, not claims of
a new general convexity theorem.

**Rate dichotomy.** Either `R=H` on the entire interval, or `R<H` at every
interior point. To see this, suppose at an interior `eta_*` that
`delta=H(eta_*)-R(eta_*)>0`. Convexity and time-sharing with the endpoints give

\[
 H(\eta)-R(\eta)\ge
 \begin{cases}
 \delta\dfrac{\eta-\eta_0}{\eta_*-\eta_0},&\eta_0\le\eta\le\eta_*,\\[4pt]
 \delta\dfrac{1-\eta}{1-\eta_*},&\eta_*\le\eta\le1.
 \end{cases}
\tag{2}
\]

Consequently, equality with the subset rate at even one interior accuracy
would prove equality everywhere. A single strict advantage would instead
give a strict advantage at every nontrivial accuracy, possibly of different
size and requiring different block lengths. This is an asymptotic claim;
it does not say that one fixed small block works at all accuracies.

**The exact onset slope is equally hard.** Convexity gives existence of

\[
 \lambda=\lim_{t\downarrow0}\frac{R(\eta_0+t)}t
 =\inf_{\eta>\eta_0}\frac{R(\eta)}{\eta-\eta_0}.
\]

Thus `lambda=2+sqrt(2)` forces `R>=H`, and hence `R=H` everywhere.
Conversely that rate curve has exactly this slope. Define the dimension-free
score-per-entropy constant

\[
 K_* =\sup_{n,\rho:S(\rho)>0}
       \frac{[g_n(\rho)-\sqrt2 n]_+}{S(\rho)}.
\]

The same characterization gives

\[
 \boxed{\lambda=\frac2{K_*}},\qquad
 2-\sqrt2\le K_*\le\frac1{\log_2(1+\sqrt2)}.
\tag{3}
\]

Indeed every feasible seed implies `S/n>=2(eta-eta_0)/K_*`, so
`lambda>=2/K_*`. Conversely a seed with positive excess and contrast
`eta=g_n/(2n)` gives `R(eta)<=S/n`, whence
`lambda<=2S/(g_n-sqrt(2)n)`. Take the infimum. Seeds with no positive excess
do not affect the supremum, and maximally mixed seeds make it nonzero.
Tensoring any positive-excess seed with arbitrarily many pure bisector
qubits preserves its entropy and total excess, while moving its normalized
contrast arbitrarily close to the classical threshold.

In particular the following are equivalent:

1. `g_n(rho)<=sqrt(2)n+c S(rho)` for every state and every n.
2. The subset asymptotic rate is optimal at every contrast.
3. It is optimal at one interior asymptotic contrast.
4. The onset slope is `2+sqrt(2)`.
5. For every integer `0<=q<=n`,
   `Gamma(n,2^q)=sqrt(2)n+c q`.

For item 5, the entropy inequality and `S<=log_2 rank<=q` give the upper
bound and subset seeds attain it. Conversely all finite budget optima give
the asymptotic subset rate, which is equivalent to item 1. A two-qubit
entropy violation can therefore lead to a finite-budget advantage only
after a larger-block compression; the known `(n,q)=(2,1)` optimum does
not rule it out.

Current proved bounds are quantitatively separated:

\[
 2.5431066063\le\lambda\le3.4142135624,
 \qquad 0.25293250\le R(0.8)\le0.31715729.
\]

These are scalar evaluations of existing analytical bounds, not fitted
simulation results. There is no basis for calling the gap a small missing
technical detail.

## 4. Why the existing routes do not close the gap

**SLD loses too much information.** Even proving the proposed all-n
inequality `I_XZ>=n-S` would only give
`g_n/n<=sqrt(2(1+S/n))`. Strict concavity of the square root puts this
strictly above the desired chord `sqrt(2)+c S/n` whenever `0<S/n<1`.
The full n=2 SLD theorem therefore does not already contain the desired
n=2 trace-norm result. An additional joint constraint on its slack would
be essential.

**Local entanglement charges cannot simply be summed.** The proposed
sharp affine squashed-entanglement calibration has an exact noisy-Bell
counterexample, documented in
[ENTANGLEMENT_CALIBRATION_OBSTRUCTION.md](../ENTANGLEMENT_CALIBRATION_OBSTRUCTION.md).
Replacing it with ordinary formation entropy loses the needed monogamy.
These are mathematical obstructions, not requests for a larger simulation.

**Scalar entropy sharpening is not enough by itself.** The Fano/mixing and
cube/coherence ingredients are individually sharp. Subset seeds already
saturate relevant state-level steps, while averaging scores across queries
and Kraus branches loses their joint structure. A sharp proof must control
that structure or its aggregate slack, not assume independently optimized
local decoders admit one common decomposition.

**A direct deficit tensorization is false, even for classical correlations.**
Here is a further exact obstruction, independently reconstructed for this
assessment. Let `beta_+`, `beta_-` be the orthogonal eigenvectors of
`(X+Z)/sqrt(2)` and let

\[
 \rho_\epsilon=(1-\epsilon)|\beta_+\beta_+\rangle\langle\beta_+\beta_+|
 +\epsilon|\beta_-\beta_-\rangle\langle\beta_-\beta_-|.
\]

Each compressed local X/Z is diagonal on this two-dimensional support,
with diagonal entries `+1/sqrt(2),-1/sqrt(2)`. Thus

\[
 g_2(\rho_\epsilon)=2\sqrt2,\quad
 g_1(\rho_A)=g_1(\rho_B)=\sqrt2\sqrt{1+4\epsilon-4\epsilon^2},\quad
 S(\rho_{AB})=S(\rho_A)=S(\rho_B)=h_2(\epsilon).
\]

For `Delta_n=sqrt(2)n+c S-g_n`, it follows that

\[
 \Delta_2(\rho_{AB})-\Delta_1(\rho_A)-\Delta_1(\rho_B)
 =2\sqrt2(\sqrt{1+4\epsilon-4\epsilon^2}-1)-c h_2(\epsilon).
\]

At the exact value `epsilon=1/1024`, use `sqrt(1+x)<=1+x/2` and
`h_2(epsilon)>=10epsilon`. The difference is at most
`(14sqrt(2)-20)epsilon<0`. So this deficit is not superadditive.
More generally, the score loss `g_1(rho_A)+g_1(rho_B)-g_2(rho_AB)` divided by
mutual information `h_2(epsilon)` tends to zero as epsilon tends to zero;
no positive universal coefficient repairs that
particular marginal argument. The conjecture itself remains satisfied:
`Delta_2=c h_2(epsilon)>0`. A successful tensorization needs a different
mechanism than this natural marginal-deficit bound.

**The exclusions do not cover the domain.** Product-diagonal states permit
arbitrary correlated spectra, but not arbitrary eigenvectors. Rank-two
neighborhoods are only controlled at fixed n. Neither result licenses
pinching an arbitrary candidate to a product basis or flattening its
spectrum; the fixed-support examples already show flattening can lose score.

## 5. A research decision with concrete stopping criteria

The smallest unresolved entropy problem is **all two-qubit states**, with
nonuniform rank-three and general full-rank states still relevant. The
smallest unresolved integer-qubit budget is separately `n=3,q=2`:
`Gamma(3,4) ?= 4+sqrt(2)`. Resolving one does not automatically resolve the
other or the all-n theorem.

A useful bounded next attempt is a complete n=2 trace-norm theorem, not
another list of neighborhoods. One explicit stronger candidate is the
fixed-spectrum rearrangement statement, for ordered eigenvalues lambda:

\[
 \max_U g_2(U\operatorname{diag}(\lambda)U^\dagger)
 \stackrel{?}{=}\sqrt2(K_{12}+K_{13}+K_{24}+K_{34}),
 \qquad K_{ij}=\sqrt{\lambda_i^2+6\lambda_i\lambda_j+\lambda_j^2}.
\tag{4}
\]

The right side is an explicit product-bisector eigenbasis attainer: each
edge block contributes `sqrt(2)K_ij` to the two queries at that site.
Equation (4) is **unproved**, stronger than necessary, and not a result in
the claim ledger. If it held, the existing product-diagonal entropy theorem
would settle n=2. The fixed-spectrum SLD minimization provides no theorem
transferring it to these four nuclear norms.

The acceptance criterion should be one of: a proof for every two-qubit
spectrum and eigenbasis; a comparably complete new structural inequality;
or an explicit algebraic/rational seed with a certified strict violation
and its complete operational construction. If (4) fails, first test the
actual entropy gap: beating that product-basis attainer need not violate
the main conjecture.

If the attempt yields only additional isolated spectra, small neighborhoods
or numerical near-attainers, stop that route and prepare the narrower paper.
Even a complete n=2 proof would leave the all-n step open; it would be useful
because it resolves a full state space and can expose a reusable mechanism.
Do not advertise the sharp onset slope or one interior asymptotic equality
as easier fallback targets: Section 3 proves otherwise.

For novelty, the publication gate is a theorem-level delta against the
closest sources, not another unsuccessful keyword search. The one-qubit
region and full two-parameter profile should each have a concise statement
of the known theorem being used, the additional argument, and the precise
operational conclusion absent from that theorem. The CHSH overlap in
Section 2 illustrates why that gate still matters.

## 6. Verification and limits of this assessment

Two independent within-workspace reviews checked the convexity/slope
deductions and the explicit deficit counterexample. The new CHSH source
was inspected at its definition, theorem and dimension-reduction steps,
and the assemblage substitution above was independently reconstructed.
The assessment does not rerun old construction diagnostics or treat them
as evidence for novelty. Small exploratory 4-by-4 optimization probes used
to screen (4) are not certificates and supply no theorem asserted here.
No unrestricted violation, complete n=2 proof, or all-n tensorization has
been established in this assessment.

The original report and LICENSE are preserved. Primary-source searches
were targeted and had incomplete retrieval; the accessible arXiv versions,
not an unseen publisher revision, support the comparisons. A negative
search result is not used as proof of originality.
