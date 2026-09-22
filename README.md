# Quantum Interface Cost

## How much must remain quantum when the readout is chosen later?

A first module receives one unknown quantum register. A later module will ask
for just one local X or Z readout, but the question is not known when the first
module must release the input. How many qubits must cross that interface if
classical records are free?

**Status (22 September 2026): research in progress, not a manuscript or a
novelty-certified result.** The repository contains explicit constructions,
supplied baseline proofs, a new working variational reduction, and small
reproducibility checks. Independent proof review and theorem-level novelty
comparison are pending. The general model is established measurement
simulability, not a new framework: see [the literature comparison](docs/LITERATURE_COMPARISON.md).

## Start here

| Purpose | Read |
|---|---|
| Exact assumptions and baseline proofs | [RESEARCH_NOTE.md](RESEARCH_NOTE.md), Sections 2–7 |
| What is established, derived, or still a target | [STATUS](docs/STATUS.md) |
| Unrestricted collective-encoding problem | [Seed reduction](docs/COLLECTIVE_ENCODING_REDUCTION.md) |
| Closest precedents and unresolved translations | [Literature comparison](docs/LITERATURE_COMPARISON.md) |
| Run the small checks and understand their limits | [Reproducibility](docs/REPRODUCIBILITY.md) |
| Instructions for the independent workspace | [Review brief](docs/WORKSPACE_REVIEW_BRIEF.md) |

For a first reading, use this page, then Sections 2, 4, 5, 8, and 9 of the
research note. Proof reviewers should also read Section 6 in full.

## The resource contract

One arbitrary unknown n-qubit input, including internally entangled states,
is encoded before the query into an unrestricted finite classical record C
and a quantum register Q of dimension at most 2^q. The classical alphabet has
no fixed size bound. The quantum bound holds on every branch, not on average.
Global encoders and query-dependent binary decoders are allowed.

After encoding, exactly one query selects a site i and X_i or Z_i. For every
input and every query the effective observable must be eta times that Pauli.
Equivalently, the worst-case binary total-variation error is (1-eta)/2.
There are no extra specimens, free entanglement links, source reaccess,
postselected successes, or uncharged quantum systems crossing the interface.

## Baseline bounds, not a sharp-rate claim

Write eta_0 = 1/sqrt(2). The supplied proofs give a classical cutoff at eta_0,
exact memory n at eta=1, and positive linear memory for each fixed eta>eta_0.
A simple strategy retains a uniformly random subset of q qubits and measures
the rest. It achieves

$$
\eta=\frac{1}{\sqrt2}+\frac qn\left(1-\frac{1}{\sqrt2}\right).
$$

The lower bounds and their assumptions are in the research note. **The subset
strategy is not known here to be optimal.** Passing tests does not settle that.

The main research target is a sharp finite-accuracy rate, or a proven
collective-coding advantage with meaningful converse bounds. The smallest
first diagnostic is n=2, q=1: can an unrestricted encoder exceed
(1+1/sqrt(2))/2? This question is a research target, not a certified gap in the
literature.

## Essential boundary

This is a single-specimen delayed-readout problem, not a general quantum
sampling speedup. With fresh independent copies, this local X/Z workload has
an elementary classical estimator using O(log(n/delta)/alpha^2) copies.
See Section 9 of the note. No result here establishes faster classical-data
learning, consciousness, hardware feasibility, or the need to make every
computational stage quantum.

## Reproduce locally

Python 3.10 or later and NumPy are sufficient. The recorded environment is
Python 3.13.5 with NumPy 2.3.5.

```bash
python -m pip install -r requirements.txt
python checks.py --max-n 4 --output results/baseline-rerun.json
python tools/check_seed_twirl.py --output results/seed-rerun.json
```

The first command after installation checks 14 explicit subset constructions;
the second checks 10 seed-to-interface constructions. There is no numerical
optimization or large simulation. No hosted CI run is claimed.

## Collaboration

This project's originating conversation is the Research Lead. The additional
workspace is an independent Proof and Novelty Audit, not a second copy of the
same derivation process. Coordination happens through issues, commit-pinned
notes, and pull requests; separate chats do not automatically exchange results.
Read [AGENTS.md](AGENTS.md) before editing.

Research owner: Ruge Lin. The existing [MIT license](LICENSE), copyright
(c) 2026 Ruge Lin, is preserved. The motivating fiction is not redistributed.
