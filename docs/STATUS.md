# Status and claim ledger

Updated: 2026-09-22. Stage: repository bootstrap and independent-audit handoff.

## Evidence labels

**Established ingredient** means an identified prior result, not our result.
**Derived / review pending** means this repository supplies an argument, but it
has not been independently audited. **Construction checked** means only that
listed finite matrix identities were tested. **Candidate** means an objective
for further research, with neither a proof nor novelty certification implied.
The original v0.1 note's word "proved" refers to supplied internal proofs,
not external review. This ledger supplies the repository-level status.

| Claim | Status | Location |
|---|---|---|
| General delayed measurement simulation with classical assistance | Established framework; no new-definition claim | Note [1–3]; literature comparison |
| q=0 iff eta<=1/sqrt(2) | Established threshold; elementary derivation | Note Section 3 |
| Random-subset achievable contrast | Explicit construction; checked through n=4 | Note Section 4; checks.json |
| Entropic memory lower bound; q=n for exact readout | Derived / review pending; standard uncertainty ingredients | Note Section 5 |
| Positive linear rate for fixed eta>1/sqrt(2) | Derived / review pending; corrected one-way-LOCC theorem required | Note Section 6 |
| Existence of R(eta) by subadditivity | Derived / review pending | Note Section 7 |
| Exact normalized-seed variational formulation | Derived / review pending; not asserted novel | COLLECTIVE_ENCODING_REDUCTION.md |
| Seed twirl produces a valid uniform interface | Construction checked for 10 n<=2 seeds, including complex seeds | results/seed_twirl.json |
| Sharp intermediate rate or collective advantage | Candidate, unsolved in this repository | Note Section 8 |
| Exponential many-copy estimation speedup | Not claimed; easy classical control rules out that narrative here | Note Section 9 |

## Research division

The Research Lead develops the unrestricted collective-encoding trade-off,
starting from the seed reduction. The audit workspace reconstructs the model,
checks the supplied arguments independently, and compares primary-source
results at theorem level. It may refute a proof, identify an existing solution,
or supply a stronger result. Agreement is not a success criterion.

Issue #1 records the proof-and-novelty audit. Issue #2 records the unrestricted
finite-block/rate investigation. Their conclusions must name the exact commit
reviewed. The initial repository contained only LICENSE at
`310a0730a04ada47eeda41bada41412414442ee1`.

## Publication gate

The project seeks a publishable, analytically led result with a clear
conceptual story. A baseline inequality or a familiar framework with a new
name does not meet that objective. Before manuscript work, identify an actual
new theorem or strategy, give an explicit useful consequence, complete the
closest theorem-level comparisons, and resolve material proof gaps.

Do not add noise, hardware, many-copy access, a classical-description source,
or average quantum memory merely to preserve an attractive narrative. Any
such variant must be separately stated and justified. No large simulation is
on the critical path. No independent report or completed novelty audit exists
at this bootstrap checkpoint.
