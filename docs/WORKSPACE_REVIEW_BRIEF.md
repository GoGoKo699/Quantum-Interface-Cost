# Proof and Novelty Audit workspace brief

Repository: https://github.com/GoGoKo699/Quantum-Interface-Cost
Research owner: Ruge Lin. Originating workspace: Research Lead.

## Assignment

Independently audit the model, supplied baseline proofs, and candidate
finite-accuracy memory-rate research. Treat previous assistant conclusions
and passing computations as material to inspect, not evidence of correctness
or originality. Begin substantive work immediately rather than returning only
an acknowledgment or a plan. This is not manuscript polishing.

The user seeks publishable, theorem-led work with a neat conceptual story
and clear novelty. Large network/cloud simulations cannot be on the critical
path. Small local exact or numerical checks are allowed and must be labeled.

## First actions

Read current main and record the full commit SHA under review. Read
AGENTS.md, README.md, RESEARCH_NOTE.md, docs/STATUS.md,
docs/LITERATURE_COMPARISON.md, docs/REPRODUCIBILITY.md,
docs/COLLECTIVE_ENCODING_REDUCTION.md, and issues #1–#2. Inspect any existing
audit notes, open pull requests, and newer relevant issue comments before
duplicating work. Run the small checks if execution is available; distinguish
unrun checks from failures. Do not rely on another chat's inaccessible files.

## Resource contract to preserve

One arbitrary unknown n-qubit input; encoding occurs before one delayed local
X_i/Z_i query. Allow internally entangled inputs, arbitrary global encoders,
branch-dependent decoders, and unlimited finite classical records. Charge all
quantum systems crossing the boundary in the worst-case bound dim Q<=2^q.
Do not substitute an average branch size, permit a quantum bypass, free
preshared entanglement, extra copies, source reaccess, a classical description,
postselected success, or a fixed known query. Success is uniform over all
states and queries. The task is binary output sampling, not expectation
estimation from fresh specimens or simultaneous incompatible measurements.

## Highest-risk proof checks

1. Reconstruct the channel/observable formulation and verify the claimed
   equivalence of uniform TV approximation with the symmetric contrast target.
   Check both twirls, relabeling, arbitrary entangled input, and free flags.
2. Re-derive the entropic converse without silently requiring simultaneous
   execution of all local decoders. Check Fano/data processing, conditional
   subadditivity, the mutually unbiased full bases, and H(R|CQ)>=-q.
3. Re-derive the positive-rate converse. Check the virtual Choi reference,
   separable witness bound, one-way-LOCC direction and norm factor, corrected
   faithfulness theorem, monogamy orientation, and the extension copying C.
4. Check worst-case memory, rounding, subadditivity, and the existence and
   operational meaning of R(eta). Keep eta fixed when using Theta(n).
5. Independently audit the normalized-seed reduction in full: Kraus refinement,
   normalization weights, trace-norm duality, Pauli orbit completeness,
   character projection, symmetry equalization, compactness, and spectral
   vectorization. Do not confuse a filtered seed with a deterministic channel.
6. Recheck the many-copy classical estimator as a negative control. It prevents
   a false narrative of exponential sample savings in this particular workload.

## Novelty audit

Read primary sources at theorem level, not just abstracts. Start with
Ioannou et al. 2202.12980; Jones et al. 2207.04080;
Bluhm–Rauber–Wolf 1708.04898; Devetak–Berger quant-ph/0011085.
Follow relevant citations into bounded/noisy quantum storage, BB84 delayed
information, random-access encodings, steering dimension witnesses, and
quantum rate distortion. Check the corrected 1010.1750v5 result used in the
positive-rate proof and its published erratum.

For each closest comparison provide exact version and theorem/equation/page,
a precise assumption map, resource and error quantifiers, and an explicit
reduction, obstruction, or remaining gap. Existing general machinery,
straightforward corollaries, and actual new deductions must be separated.
The general simulation model, the classical threshold, and the use of known
uncertainty/entanglement inequalities are not proposed novelties. An existing
theorem that settles our candidate problem is an important finding.

## Deliverables

Write docs/audits/PROOF_AND_NOVELTY_AUDIT.md on a separate audit branch.
Include the reviewed SHA, environment and actual tests, claim-by-claim
verdicts, full reasoning for material gaps or repairs, primary-source
comparisons, and the narrowest defensible next research target. Verdicts
should distinguish correct as stated, correct with specified qualifications,
incorrect with counterexample, and unresolved with an exact obstacle.

Post a concise evidence-based summary to issue #1 and open a pull request
with the report and any scoped proposed fixes. Report counterexamples or
subsumption early rather than burying them in prose. A failed proof step is
not automatically a false theorem; a passed test is not a proof.

## Coordination

The Research Lead owns issue #2 and works on the unrestricted finite-block
trade-off and rate. Do not quietly change that problem. You may supply a
stronger proof, an explicit better seed, or a counterexample when found,
but state its assumptions and communicate through the repository.

Use audit/<short-topic> branches from the reviewed commit. Do not force-push,
rewrite another workspace's work, merge your own audit report, or modify main
directly. Preserve LICENSE exactly. Bootstrap material on main is a common
starting point, not a certification. Wait for Research Lead review of the PR.
No separate workspace is running merely because this file exists.
