# Status and claim ledger

Updated: 2026-09-22. Stage: sharp flat-seed theorem and further entropy exclusions.
Latest research base: `87b6432cdd1f29bc4981f24bd6732bb933741193`, the merge of PR #5.

## Evidence labels

**Established ingredient** means an identified prior result. **Derived and
independently checked** means a supplied argument was reconstructed by another
agent in this workspace; it does not mean external peer review or publication
novelty. **Construction checked** means only the listed finite identities were
tested. **Unresolved** means neither a theorem nor its absence from prior work
is asserted.

| Claim | Status | Location |
|---|---|---|
| General delayed measurement simulation with classical assistance | Established framework; also equivalent here to a prior postmeasurement-information discrimination task | Audit Sections 6.1–6.3 |
| q=0 iff eta<=1/sqrt(2) | Established threshold; elementary derivation checked | Note Section 3; audit |
| Random-subset achievable contrast | Explicit construction; checked through n=4 | Note Section 4; checks.json |
| Entropic memory lower bound | Standard-theorem application; independently checked | Note Section 5; audit Section 4.1 |
| Logarithmic-Sobolev lower bound b(eta) on q/n and R(eta) | Derived and independently checked from Beigi and Audenaert et al.; unrestricted | STRONG_ENTROPIC_CONVERSE.md |
| q=n for exact readout | Also a corollary of Ballester–Wehner–Winter Lemma 5.1 | Audit Section 6.1 |
| Positive linear rate for fixed eta>1/sqrt(2) | Derived and independently checked, using corrected one-way-LOCC faithfulness | Note Section 6; audit Section 4.2 |
| Existence of R(eta) by subadditivity | Derived and independently checked | Note Section 7; audit Section 4.3 |
| Exact normalized-seed variational formulation | Derived and independently checked; not asserted novel | Seed reduction; audit Section 5 |
| Seed twirl produces a valid uniform interface | Analytical proof checked; 10 finite construction diagnostics | results/seed_twirl.json |
| Gamma(n,2)=2+sqrt(2)(n-1), for every n | Derived and independently checked from Cheng–Hall monogamy; subset strategy optimal with one retained qubit | ONE_QUBIT_OPTIMALITY.md |
| All maximizing one-qubit seeds retain one site and project the rest onto product bisectors, up to output unitaries | Derived equality characterization; independently checked | ONE_QUBIT_OPTIMALITY.md Section 5 |
| g(L)<=sqrt(2)n+(2-sqrt(2))S(L^dagger L) for product-diagonal Gram matrices | Derived and independently checked; arbitrary correlated spectra and local bases allowed; restricted-family result | COMMUTING_SEED_BOUND.md |
| Same entropy bound for unrestricted Gram matrices | Unresolved; a proposed local conditional-entropy proof is explicitly refuted | COMMUTING_SEED_BOUND.md Section 6 |
| Exact maximum score at fixed rank-two spectrum | Derived and independently checked; arbitrary eigenvectors allowed | ENTROPY_INEQUALITY_BOUNDARIES.md |
| Entropy inequality for all stabilizer-basis spectra and all flat rank-three two-input states | Derived and independently checked; additional excluded families | ENTROPY_INEQUALITY_BOUNDARIES.md |
| Subset bound for flat half-rank seeds with a maximally mixed complementary marginal | Derived and independently checked; a scoped converse, not the unrestricted n=3,q=2 result | ENTROPY_INEQUALITY_BOUNDARIES.md |
| Exact flat half-rank optimum and equality cases for n<=4 | Derived and independently checked; arbitrary n also covered with at most four singleton X/Z sites in the reflection | FLAT_HALF_RANK_OPTIMALITY.md |
| No flat seed improves the q=n-1 subset score for n<=4 | Derived and independently checked for every allowed flat rank, including separate lower-rank estimates | FLAT_HALF_RANK_OPTIMALITY.md |
| Entropy bound for all flat rank-three three-input states | Derived and independently checked via a Ky Fan refinement, g<=sqrt(53/2) | FLAT_HALF_RANK_OPTIMALITY.md Section 6 |
| Entropy-bound closure under local classical flags and tensor products | Derived and independently checked; all two-input states classical on either qubit | CLASSICAL_FLAG_ENTROPY_BOUND.md |
| Entropy bound for locally maximally mixed two-qubit states | Derived and independently checked; arbitrary local rotations, stronger entropy-deficit coefficient | LOCALLY_MIXED_TWO_QUBIT_BOUND.md |
| Entropy bound for full-rank states of condition number <=6.235819648070267 | Derived and independently checked; all n and eigenvectors, sufficient threshold only | SPECTRAL_CONDITION_ENTROPY_BOUND.md |
| Two-qubit local conditional-entropy proposal | Incorrect; explicit rank-two classical-quantum counterexample, without violating the global conjecture | CLASSICAL_FLAG_ENTROPY_BOUND.md Section 5 |
| R(eta) equals the regularized minimum seed entropy at contrast eta | Derived and independently checked; worst-case dimension and uniform error preserved; no closed-form evaluation | ENTROPY_RATE_CHARACTERIZATION.md |
| General sharp intermediate rate evaluation or collective advantage | Unresolved | Note Section 8 |
| Exponential many-copy estimation speedup | Not claimed; easy classical control rules out that narrative here | Note Section 9 |

## What changed after the audit

The commit-pinned [audit](audits/PROOF_AND_NOVELTY_AUDIT.md) reviewed bootstrap
commit `eaf085a8cb299e6b297b11d2dc3c85e24f02779e`. Its historical verdicts are
preserved. It found no error in the repository's supplied baseline proofs,
but identified earlier subsumption of the exact endpoint, a direct equivalent
discrimination problem, strict obstructions to importing reconstruction or
full-outcome converses, and two source-proof caveats.

Subsequent analytical work settles the former `(n,q)=(2,1)` diagnostic and
extends it to every n at q=1. The proof requires Cheng–Hall's independently
optimized common-qubit settings; a weaker common-setting CHSH statement would
not suffice. Rigidity describes refined branch maps, without assuming that
the retained site's choice is independent of the physical input.

The product-diagonal entropy argument excludes correlated diagonal spectra
and all local basis rotations as a route beyond the subset benchmark. It
does not restrict the original operational model or cover every separable
Gram matrix. Both new proofs were independently checked within the workspace.
The 43 one-qubit and 10 product-diagonal diagnostics support specific matrix
identities; the proofs carry the general claims.

The further entropy-rate characterization converts asymptotic rank into a
regularized entropy minimum using virtual Schmidt truncation and complete
seed orbits. Midpoint convexity supplies the continuity needed to remove
contrast slack. This proof was independently checked as well. A violation
of the unrestricted seed entropy bound is now a sufficient certificate of
an asymptotic collective advantage; no such violation has been established.

## Further converse and exclusions

The subsequent continuation derives an explicit unrestricted lower bound
from Beigi's improved quantum logarithmic-Sobolev theorem. For example, at
eta=0.8 it raises the necessary memory fraction from 0.06200881 to
0.14144054; the achievable subset fraction remains 0.31715729. Near the
classical threshold its coefficient scales as `4 t^2 log_2(1/t)+O(t^2)`
for contrast advantage t. This is a task-specific consequence of prior
functional inequalities, not new logarithmic-Sobolev mathematics.

The exact rank-two spectrum envelope now excludes every rank-two Gram matrix
from witnessing an entropy-based rate advantage. Further analytical exclusions
cover arbitrary spectra in stabilizer eigenbases, flat rank-three two-input
states, and a family of flat half-rank projectors extending beyond fixed
product-diagonal bases. The notes supply proofs and preserve their family
conditions explicitly.

## Latest structural deductions

Every flat half-rank seed on n<=4 inputs has score at most
`2(n-1)+sqrt(2)`, with equality precisely for one pure bisector projector
tensor the identity. The proof also applies for arbitrary n when the
singleton X/Z projection of the reflection occupies at most four sites;
higher-order Pauli terms are unrestricted. Separate flat-rank estimates
exclude every lower allowed rank from improving the q=n-1 finite-budget
score at these sizes. They do not establish the sharper entropy inequality
at every lower rank. The [source comparison](FLAT_SEED_PRIOR_COMPARISON.md)
distinguishes the result from prior Poincare/FKN statements and records a
later repair of a prior FKN proof step.

Local classical flags extend the entropy exclusion beyond fixed product
eigenbases. Two-input states with both marginals maximally mixed are also
excluded, as are all full-rank states with the stated bounded condition
number. These are conditions on candidate Gram matrices, not constraints
on admissible physical encoders. The spectral condition supplies no new
unrestricted rate lower bound. All four proofs have been independently
reconstructed within the workspace; publication novelty remains unresolved.

## Research division and next target

Issue #1 records the proof-and-novelty audit. Issue #2 coordinates the
unrestricted finite-block/rate investigation. The user subsequently authorized
continued research and merging; audit PR #3 was integrated under that explicit
authorization. Research changes still use a separate branch and pull request.
The original repository contained only LICENSE at
`310a0730a04ada47eeda41bada41412414442ee1`.

The smallest unresolved block is now `n=3,q=2`: prove
`Gamma(3,4)<=4+sqrt(2)` or construct a violating seed. Every allowed flat
seed is now excluded from improving this finite-budget score. A witness
must have rank three or four with nonuniform nonzero eigenvalues, outside
the product-diagonal family. A separate Ky Fan refinement also proves the
sharper entropy inequality for every flat rank-three three-input state. The one-qubit
CHSH argument cannot be extended by treating a four-dimensional memory as
one qubit: two Bell pairs explicitly violate its key pair bound.
The all-contrast asymptotic subset-rate conjecture is equivalent to the seed
entropy inequality holding for every Gram matrix, including entangled
eigenbases. The established entropy formula does not itself evaluate the rate.

The smallest possible entropy witness is a two-input state of rank three
with nonuniform nonzero eigenvalues; general full-rank two-input states also
remain open. Such a witness must be nonclassical on both sites, must not
have both marginals maximally mixed, and, if full rank, must have condition
number greater than 6.235819648070267. This is distinct from the n=3,q=2 finite-budget diagnostic:
regularization can turn entropy below log(rank) into an asymptotic memory
saving. No entropy witness or collective advantage has been found.

## Publication gate

The goal remains a publishable, analytically led theorem with a clear novelty
case. These are task-specific deductions; neither familiar monogamy nor a
restricted-family entropy inequality should be presented as a new general
framework. Complete the closest comparisons for the new results and determine
whether a broader sharp theorem or useful separation is available before
making a publication claim. The existing primary-source audit is targeted,
not a proof of absence from the literature.

Preserve one unknown specimen, one delayed query, arbitrary collective
encoding, unlimited finite classical records, worst-case quantum dimension,
and uniform arbitrary-input statistics. No large simulation is on the
critical path.
