# Scientific background for the selected manuscript

[Learning path](LEARNING_PATH.md) · [Core argument](CORE_ARGUMENT.md) · [Exact source comparisons](CORE_PRIOR_COMPARISON.md) · [BibTeX](../references.bib)

Prepared 30 September 2026 against main
`a6b183cc31bbc4b94c271ff3d25766440576aba4`.
This is a background and citation guide for the bounded package in
[Scientific scope](SCIENTIFIC_SCOPE.md).
It consolidates the existing source audits and a focused primary-text
update; it does not assert an exhaustive literature search or external
validation. The proof statements and historical evidence freeze remain
the scientific basis.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s
self-directed learning. For discussion or potential collaboration, please
contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## 1. The scientific question in its existing setting

Measurement incompatibility asks which measurement statistics can be
recovered by classical processing of one earlier measurement. This project
asks how that ability changes when the earlier operation may leave a small
quantum register as well as its classical outcome. Its setting is already
dimensional measurement simulability; the contribution is an evaluation
for the particular family of delayed original-site X/Z queries.

The relevant factorization is

```math
M_{s|U}=\sum_c K_c^\dagger E_{s|U,c}K_c,
\qquad \sum_c K_c^\dagger K_c=I,
\qquad K_c:\mathbb C^{2^n}\longrightarrow\mathbb C^D.
```

Here U is learned after encoding, s is a binary answer, c is the stored
classical label, and D is a cap on every branch. The effects on the memory
may depend on U and c. The equality concerns operators, hence all input
states, rather than a selected ensemble of test states. No common decoded
quantum state is required. A smaller output on some branches can be
embedded into the same D-dimensional space.

Ioannou et al., Eq. (1), is the most direct framework citation. Jones
et al., Theorems 1–2, supplies its measurement/steering correspondence.
Ballester–Wehner–Winter is an earlier operational predecessor: after the
specified symmetrization, its postmeasurement-information task for the
ensemble `(I+sU)/2^n` has success probability `(1+eta)/2`. Its exact-storage
criterion already gives the endpoint q=n. These roles, including their
precise limits, are tabulated in the [focused comparison](CORE_PRIOR_COMPARISON.md).

Two later framework references are also relevant. Sekatski's bottleneck
dimension includes quantum operations more generally. Achenbach et al.'s
2026 multimeter factorization, Section 4.1, treats instruments with finite
classical labels and an intermediate state space. Its general probabilistic
maps are positive; the present quantum model retains completely positive
encoding operations. These broader formulations do not by themselves
evaluate the fixed local-query workload. Neither is a replacement teaching
anchor.

The informative contrast is within the same operational model: original
qubits suffice at the proved common-accuracy budgets and throughout the
one-qubit allocation region, whereas a specified collective encoder exceeds
the original-site-retention class for unequal accuracies. This is the
scientific story to explain before the technical reductions.

## 2. Resource distinctions that belong in the background

| Nearby question | What must be kept distinct here | Primary route |
|---|---|---|
| Joint measurability | With D=1, a parent POVM and conditional output probabilities suffice. A quantum output is what extends this endpoint. | Gühne et al., II.A–B and III.A; Yu et al., Theorem 1 |
| Compression with reconstruction | A single recovered state on which all requested measurements are performed imposes a common channel completion. Arbitrary query-dependent effects need not admit it. | Bluhm–Rauber–Wolf, Definition 4.1 and Section 9.1 |
| Asymptotic measurement compression | Winter's task fixes a source and POVM and trades classical communication against common randomness over repeated preparations. Its rates do not evaluate a branchwise quantum-memory cap for a delayed query on one arbitrary specimen. | Winter; Wilde et al., Section 2.1, Eq. (7), and Section 2.2, Theorem 5 |
| Full measurement contexts | Separate binary answers for local queries need not combine into a decoder returning an entire product-basis outcome. Coarse-graining gives constructions but does not reverse this implication for converses. | Jones et al., Section VI; focused comparison |
| Average dimensional cost | An average of log Kraus ranks can allow expensive branches. Here every branch has rank/output dimension at most D, and classical flags are free. | Cope–Uola, Section IV, Eqs. (8)–(9) |
| Quantum random-access coding | Preparing a codeword from a known classical string differs from encoding an unknown specimen with a uniform statistics guarantee. A bound needs a proved reduction before reuse. | Gühne et al., IV.E.2; the virtual-state argument in the proof bridge |
| Tomography and classical shadows | Estimating means from repeated preparations allows real-valued estimators. A single recorded outcome must instead yield an actual probability distribution for the requested binary answer. | Heinosaari–Miyadera–Ziman, Section 3.4, Eq. (32); Huang–Kueng–Preskill; Research note, Section 9 |

Informational completeness alone does not solve the task. Expanding a target
effect in the span of an informationally complete POVM can require negative
coefficients; these cannot be conditional sampling probabilities. This is
the useful conceptual distinction in Heinosaari–Miyadera–Ziman's Section 3.4.
The repository's repeated-copy estimator is a negative control, not an
achievable decoder for the one-specimen problem.

For a binary effective observable A and target U, the uniform
total-variation error is `||A-U||_infinity/2`. Pauli symmetrization puts
the target into noisy form `eta U`, with error `(1-eta)/2`. The
[proof bridge, Sections 1–3](tutorial/PROOF_BRIDGE.md#1-separate-the-unknown-input-from-the-optimization-variable)
explains why neither this symmetrization nor the use of normalized branch
weights changes the unknown-input guarantee.

## 3. What must be learned beyond the single review

The external teaching source remains **Gühne et al. (2023)**. The
[learning path](LEARNING_PATH.md) gives its section-level selections and
compares two alternatives. Primary articles below are citations for proof
ingredients, not additional textbooks that the reader must master first.

| Needed idea | Established background | Repository bridge and remaining sharp step |
|---|---|---|
| Effects, instruments and compatibility | Review II.A–B; III.A and III.C.1 introduce the noisy-qubit geometry and constructions. | [First tutorial](tutorial/MEASUREMENTS_TO_MEMORY.md) builds the classical disk and random retention protocol. |
| Decoder optimization and branch normalization | Kraus/polar representations, trace-norm duality and finite Pauli averaging are standard tools. For the matrix/instrument foundations, see Watrous, Sections 1.1.3, 2.2.2, 2.3.2 and 3.1.1. | [Proof bridge, Sections 1–3](tutorial/PROOF_BRIDGE.md) derives the bounded-rank seed objective and completes every seed into a trace-preserving instrument. |
| Local incompatibility weight | Review III.B.2 and Pusey Eq. (15) supply the resource definition; Yu et al. supplies the qubit compatibility criterion. | [Allocation proof, Section 7](ONE_QUBIT_ALLOCATION_REGION.md#7-established-local-weight-and-the-global-deduction) evaluates that weight for the pair and distinguishes it from robustness. |
| One memory qubit as a shared correlation resource | Review IV.A supplies CHSH vocabulary. Cheng–Hall Eq. (1), Eqs. (13)–(14) and the mixed-state extension allow independent settings on the shared qubit. | The [one-qubit argument](CORE_ARGUMENT.md#2-the-exact-one-qubit-theorem) converts weighted decoder scores into CHSH scores and evaluates the global allocation budget. The review alone does not supply this monogamy theorem. |
| Rank-constrained finite converses | Root fidelity, Schatten Hölder and spectral rearrangement; Audenaert et al., Appendix A, Theorem 6, Eq. (55), supplies the fidelity–affinity comparison. | [Proof bridge, Sections 6–7](tutorial/PROOF_BRIDGE.md#6-fidelity-affinity-and-the-constraint-that-cannot-be-dropped) explains the rank constraint and the exact polynomial certificate. The half- and quarter-rank inequalities are supplied in the linked proofs. |
| Small-support collective construction | Induced-cube spectral optimization and the star eigenvalue are established graph mathematics; Avni–Samorodnitsky, Example 1.12. | [Proof bridge, Section 8](tutorial/PROOF_BRIDGE.md#8-a-small-support-explains-the-31-input-collective-example) turns the weighted star into a complete instrument, then proves its separation from the stated retention class. |

The normalized Gram matrix is an optimization variable for the encoder,
not its physical input. Likewise, vectorizing a Kraus operator introduces
a virtual reference only for the proof. A reader who can explain these
two distinctions, trace-norm decoder optimization, and Pauli completion
has crossed the main gap between the review and the core results.

## 4. How to introduce the results and attribute them

The background can support the following progression when writing resumes.

1. Introduce delayed measurement choice through incompatibility, then state
   dimensional simulability and the branchwise resource model.
2. Give the classical compatibility endpoint and the random retention
   construction. Use the two-input example to make the contrast/error
   convention concrete.
3. Explain that the main issue is optimality against collective instruments.
   State the complete one-qubit region and all integer budgets through four
   inputs, separating the established ingredients from their task-specific
   evaluation.
4. Show why this is not a universal endorsement of retention: the complete
   31-input, five-memory-qubit construction separates unequal accuracies
   from the precisely defined retention class.
5. Put the balanced-spectrum theorem after these operational results, if
   retained in the manuscript. State the unrestricted larger-block questions
   as open rather than importing conclusions from the spectral subfamily.

The additional higher-memory finite cases are exactly `(3,2)`, `(4,2)` and
`(4,3)`. The one-qubit converse uses existing monogamy; the classical and
exact-storage endpoints are prior. Seed equality classifications do not
classify every physical instrument. The collective example establishes a
class separation, not its unrestricted optimality or a common-accuracy
advantage. These are presentation boundaries, not unresolved assumptions
inside the selected proofs.

## 5. Optional background for the structural companion

The balanced-spectrum result optimizes the sum of responses to the fixed
original X/Z queries over global eigenbases at a prescribed two-level
spectrum. Its proof uses a Pauli expansion, random-sign moment identities,
and a scalar polynomial comparison. The
[proof's source section](audits/BALANCED_SPECTRUM_OPTIMALITY.md#6-prior-context-and-verification)
compares response-based discord and quantitative Khintchine bounds.
Roga–Giampaolo–Illuminati's Eqs. (9) and (20) identify the individual
root-fidelity response and its qubit trace-norm expression; optimizing one
local perturbation of a fixed state differs from the fixed-query sum here. The
[focused comparison](CORE_PRIOR_COMPARISON.md#supporting-source-boundaries)
also distinguishes quantum Boolean FKN rigidity from this score-based
stability statement. These antecedents motivate the tools; their different
objectives and hypotheses must remain visible.

Beigi's nonlinear entropy/Dirichlet and rank inequalities belong in a
discussion of the wider archive or the limitation of the affinity method.
They are not prerequisites for the three selected operational results.
The full product-diagonal formation profile, asymptotic-rate program and
earlier partial decoder classifications likewise remain outside this
manuscript's required background. Their detailed attribution stays in the
[literature record](LITERATURE_COMPARISON.md).

## 6. Citation and coverage record

[references.bib](../references.bib) collects the selected framework,
ingredient and tutorial references. Versioned preprint URLs match the text
used for equation/theorem locators where available; publication metadata
does not imply that the journal and preprint number their results identically.
The focused comparison is the authority for that distinction. The bibliography
is a starting set for this package, not a replacement for the archive's
per-proof references or a requirement to cite every entry in an introduction.

The 30 September pass checked the tutorial alternatives, operational
frameworks, essential compatibility/monogamy/fidelity/star ingredients and
recent dimensional-simulability context. It adds Achenbach et al.'s published
factorization formulation and records its figure-only correction. Existing
equation-level comparisons were retained where the checks supported them.
No additional evaluated converse for the three higher-memory finite cases
was identified in the inspected statements. This bounded finding does not
establish priority or the absence of further relevant work.

The preparation is sufficient to begin drafting the selected package when
writing resumes. Any later change of theorem scope requires its own source
comparison; the open all-size optimum and asymptotic rate are not additional
background tasks needed to understand the present results.
