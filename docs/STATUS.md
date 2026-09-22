# Status and claim ledger

Updated: 2026-09-22. Stage: audited baseline and analytical finite-block results.
Research base: `df45e2eaceb5669cfff9ac063d3da845d622dac3`, the merge of audit PR #3.

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
| q=n for exact readout | Also a corollary of Ballester–Wehner–Winter Lemma 5.1 | Audit Section 6.1 |
| Positive linear rate for fixed eta>1/sqrt(2) | Derived and independently checked, using corrected one-way-LOCC faithfulness | Note Section 6; audit Section 4.2 |
| Existence of R(eta) by subadditivity | Derived and independently checked | Note Section 7; audit Section 4.3 |
| Exact normalized-seed variational formulation | Derived and independently checked; not asserted novel | Seed reduction; audit Section 5 |
| Seed twirl produces a valid uniform interface | Analytical proof checked; 10 finite construction diagnostics | results/seed_twirl.json |
| Gamma(n,2)=2+sqrt(2)(n-1), for every n | Derived and independently checked from Cheng–Hall monogamy; subset strategy optimal with one retained qubit | ONE_QUBIT_OPTIMALITY.md |
| All maximizing one-qubit seeds retain one site and project the rest onto product bisectors, up to output unitaries | Derived equality characterization; independently checked | ONE_QUBIT_OPTIMALITY.md Section 5 |
| g(L)<=sqrt(2)n+(2-sqrt(2))S(L^dagger L) for product-diagonal Gram matrices | Derived and independently checked; arbitrary correlated spectra and local bases allowed; restricted-family result | COMMUTING_SEED_BOUND.md |
| Same entropy bound for unrestricted Gram matrices | Unresolved; a proposed local conditional-entropy proof is explicitly refuted | COMMUTING_SEED_BOUND.md Section 6 |
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

## Research division and next target

Issue #1 records the proof-and-novelty audit. Issue #2 coordinates the
unrestricted finite-block/rate investigation. The user subsequently authorized
continued research and merging; audit PR #3 was integrated under that explicit
authorization. Research changes still use a separate branch and pull request.
The original repository contained only LICENSE at
`310a0730a04ada47eeda41bada41412414442ee1`.

The smallest unresolved block is now `n=3,q=2`: prove
`Gamma(3,4)<=4+sqrt(2)` or construct a violating seed. A collective advantage
must use a Gram matrix outside the product-diagonal family. The one-qubit
CHSH argument cannot be extended by treating a four-dimensional memory as
one qubit: two Bell pairs explicitly violate its key pair bound.
The all-contrast asymptotic subset-rate conjecture is equivalent to the seed
entropy inequality holding for every Gram matrix, including entangled
eigenbases. The established entropy formula does not itself evaluate the rate.

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
