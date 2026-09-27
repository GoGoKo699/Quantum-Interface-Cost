# From incompatible measurements to quantum memory

[Repository overview](../README.md) · [First tutorial](tutorial/MEASUREMENTS_TO_MEMORY.md) · [Proof bridge](tutorial/PROOF_BRIDGE.md)

An unknown quantum register must be stored before someone decides which
local X or Z measurement to request. Classical records cost nothing;
quantum memory is limited. When does keeping original qubits suffice,
and when can a collective encoding do better?

This reading path uses **one external teaching source**. The local
tutorials explain the additional model, reductions and examples needed
to reach the repository's results. Research references remain available
for attribution and checking individual ingredients.

## 1. The teaching anchor

Otfried Gühne, Erkka Haapasalo, Tristan Kraft, Juha-Pekka Pellonpää and
Roope Uola, **Colloquium: Incompatible measurements in quantum information
science**, *Reviews of Modern Physics* **95**, 011003 (2023).

[arXiv entry](https://arxiv.org/abs/2112.06784) ·
[PDF, version 3](https://arxiv.org/pdf/2112.06784v3) ·
[HTML, version 3](https://arxiv.org/html/2112.06784v3) ·
[Published article](https://doi.org/10.1103/RevModPhys.95.011003)

The starting point is undergraduate quantum mechanics and finite-dimensional
linear algebra: density matrices, the Born rule, tensor products and Pauli
matrices. Generalized measurements are introduced by the review and revisited
locally. The proof bridge introduces the extra matrix language as it is used.

Use the following selections; the whole review is not a prerequisite.
Section labels below follow the **PDF**. The HTML replaces subsection
letters with numbers, so II.A appears as II.1, for example.

| Read in the review | Bring this idea | Continue locally |
|---|---|---|
| II.A–B | Instruments and a common parent measurement | [The delayed task](tutorial/MEASUREMENTS_TO_MEMORY.md): what remains after encoding |
| III.A and III.C.1 | Noisy qubit compatibility and explicit joint measurements | The classical disk and an attaining measurement |
| III.B.2 | Mixing compatible and incompatible measurements | The local weight and how one stored qubit is allocated |
| IV.A; optional IV.B | CHSH correlations and the measurement–state viewpoint | [Proof bridge](tutorial/PROOF_BRIDGE.md): the virtual reference and the specific monogamy ingredient |
| II.A revisited; optional V.C.5 | Retrieving a later measurement from an earlier instrument | Query-dependent decoding; the branch dimension bound and complete seed construction are added locally |

These selections supply vocabulary and motivation. The dimension cap,
normalized-seed optimization and sharp finite-memory inequalities are
developed in this repository. The particular Cheng–Hall monogamy theorem
used here is a separately attributed ingredient, explained in the proof
bridge; the review's CHSH discussion does not itself supply that theorem.

## 2. A route through the repository

| Stage | Read | What you should be able to explain afterward |
|---|---|---|
| Understand the question | [Measurements to memory](tutorial/MEASUREMENTS_TO_MEMORY.md) | Why a classical record can answer either noisy X or noisy Z, how a quantum register changes the possibilities, and what the memory cap means |
| Work an example | The retention and allocation examples in the same tutorial | How two inputs share one quantum-memory slot, and how unequal accuracies consume that slot |
| Understand the reduction | [Memory to proofs](tutorial/PROOF_BRIDGE.md) | Why the problem becomes an optimization over a density matrix of bounded rank, and how every candidate seed produces a complete protocol |
| Follow the results | [Core argument](CORE_ARGUMENT.md), Sections 2–4 | The all-size one-qubit rule, exact common accuracy through four inputs, and the unequal-accuracy collective separation |
| Inspect the sharp steps | The proof appendices linked from the core | Where CHSH monogamy, spectral rank constraints and the exact polynomial certificate enter |

The [balanced-spectrum result](CORE_ARGUMENT.md#5-a-separate-all-size-structural-companion)
and its stability extension are optional structural companions. They are
not needed to understand or prove the three operational conclusions.

## 3. Translate the language carefully

| Phrase | Meaning here |
|---|---|
| Compatible measurements | All requested statistics can be obtained by classical processing of one parent measurement; this is the zero-quantum-memory endpoint |
| A quantum instrument | An encoding with both a classical outcome and a remaining quantum output |
| Delayed query | The site and X/Z choice are revealed only after encoding; only one binary answer is required |
| Quantum memory dimension | At most $`D=2^q`$ in every branch; the classical alphabet has no fixed size bound but is finite |
| Normalized seed | An auxiliary operator describing a refined encoding branch; its Gram matrix is not the unknown physical input state |
| Uniform error | A guarantee for every input state and each allowed query, including inputs entangled across sites |

Two nearby topics in the review require care. Section V.C.1 discusses
simulation by a smaller **number of POVMs**; this is not the same constraint
as our smaller **quantum output dimension**. Section IV.E.2 discusses
quantum random-access codes for a known classical string and an average
guessing score. Here the encoder receives one unknown quantum specimen,
with requested statistics guaranteed uniformly. Those sections are useful comparisons,
not definitions of this task.

## 4. The result to keep in view

For common contrast, random subset retention attains

```math
\eta_{\mathrm{ret}}(n,q)=\frac qn+
\left(1-\frac qn\right)\frac1{\sqrt2}.
```

This is the unrestricted optimum for every integer $`0\le q\le n\le4`$
with $`n\ge1`$, and for $`q=1`$ at every input size. The full one-qubit
theorem also determines unequal local accuracies. A different complete
protocol, with 31 inputs and five memory qubits, exceeds the precisely
defined original-site-retention class when X and Z accuracies differ.

The tension is the subject of the project: a simple retention rule is
provably optimal in the stated regimes, while collective storage can help
for a different accuracy profile. The unequal-accuracy example does not
settle the unrestricted common-accuracy problem at larger input sizes.

## 5. Sources and evidence

The review is the teaching anchor. The
[focused prior comparison](CORE_PRIOR_COMPARISON.md) identifies the
established operational frameworks and the specific prior ingredients;
it is a reference map, not a second required tutorial. No new measurement
compression framework or CHSH monogamy inequality is claimed.

The [scientific scope](SCIENTIFIC_SCOPE.md) states the exact result boundaries.
The [evidence freeze](SCIENTIFIC_EVIDENCE_FREEZE.md) pins the reviewed
scientific inputs and distinguishes analytical proofs, the essential exact
certificate and finite diagnostics. The teaching pages explain those inputs
without changing them. Internal reconstruction is not external peer review.

For other derived results, limitations and earlier proof routes, use the
[research index](RESEARCH_INDEX.md). None of that entire archive is assumed
as background for this reading path.
