# Quantum Interface Cost

## How much must remain quantum when the readout is chosen later?

A first module receives one unknown quantum register. A later module will ask
for just one local X or Z readout, but the question is not known when the first
module must release the input. How many qubits must cross that interface if
classical records are free?

**Status (22 September 2026): research in progress, not a manuscript or a
novelty-certified result.** The baseline proofs and seed reduction have passed
an independent workspace audit, including primary-source comparisons. Further
analytical work proves the exact optimum with one retained qubit for every
input block size, an entropy bound for product-diagonal seeds, and a regularized
entropy characterization of the asymptotic rate. Evaluating that rate remains
unresolved. A further converse derived from quantum logarithmic-Sobolev theory
improves the quantitative memory lower bounds. The model is established measurement
simulability, not a new framework: see [the literature comparison](docs/LITERATURE_COMPARISON.md).

## Start here

| Purpose | Read |
|---|---|
| Exact assumptions and baseline proofs | [RESEARCH_NOTE.md](RESEARCH_NOTE.md), Sections 2–7 |
| What is established, derived, or still a target | [STATUS](docs/STATUS.md) |
| Unrestricted collective-encoding problem | [Seed reduction](docs/COLLECTIVE_ENCODING_REDUCTION.md) |
| Exact optimum with one retained qubit | [One-qubit theorem and equality cases](docs/ONE_QUBIT_OPTIMALITY.md) |
| A structured family that cannot beat the subset strategy | [Product-diagonal entropy bound](docs/COMMUTING_SEED_BOUND.md) |
| Exact regularized formulation of the asymptotic rate | [Entropy-rate characterization](docs/ENTROPY_RATE_CHARACTERIZATION.md) |
| Stronger bound for every collective encoder | [Logarithmic-Sobolev converse](docs/STRONG_ENTROPIC_CONVERSE.md) |
| Exact rank-two spectrum trade-off and excluded families | [Entropy-inequality boundaries](docs/ENTROPY_INEQUALITY_BOUNDARIES.md) |
| Commit-pinned independent proof and source review | [Audit report](docs/audits/PROOF_AND_NOVELTY_AUDIT.md) |
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

## Bounds and a sharp finite-memory result

Write eta_0 = 1/sqrt(2). The supplied proofs give a classical cutoff at eta_0,
exact memory n at eta=1, and positive linear memory for each fixed eta>eta_0.
A simple strategy retains a uniformly random subset of q qubits and measures
the rest. It achieves

$$
\eta=\frac{1}{\sqrt2}+\frac qn\left(1-\frac{1}{\sqrt2}\right).
$$

The lower bounds and their assumptions are in the research note. **The subset
strategy is optimal for q=1, for every n.** The analytical proof applies
Cheng–Hall's established three-qubit CHSH monogamy theorem, including its
independent-setting and mixed-state scope. It also characterizes all maximizing
normalized seeds. The q=0 and q=n endpoints are established separately.

For general `2<=q<n`, optimality remains unresolved. A separate entropy
argument excludes every seed whose Gram matrix is diagonal in a fixed tensor
product of local bases, allowing correlated spectra and arbitrary local axes.
It does not assume that unrestricted optimizers have that form.

The asymptotic rate also equals a regularized minimum of the seed's entropy
at the requested contrast. The proof constructs a fixed-dimensional,
trace-preserving interface; it does not change worst-case memory to average
memory. This characterization turns any violation of the unrestricted entropy
bound into a collective rate advantage, but does not yet evaluate the optimum.

For example, at contrast eta=0.8 the new unrestricted converse requires at
least 0.14144054 n retained qubits, improving the previous lower bound
0.06200881 n; the subset construction uses asymptotically 0.31715729 n.
This is a deduction from Beigi's established theorem and a standard fidelity
inequality, not a new logarithmic-Sobolev theorem or a sharp rate claim.

The main research target is a sharp finite-accuracy rate, or a proven
collective-coding advantage with meaningful converse bounds. The smallest
remaining diagnostic is n=3, q=2: can an unrestricted seed exceed the subset
score `4+sqrt(2)` in the optimization `Gamma(3,4)`? For the entropy route,
even a two-input state of rank three could in principle certify a rate
advantage: all rank-two states and all flat rank-three two-input states are
now excluded, but nonuniform rank-three and general full-rank states remain
open. These are distinct diagnostics. Publication novelty is not certified.

## Essential boundary

This is a single-specimen delayed-readout problem, not a general quantum
sampling speedup. With fresh independent copies, this local X/Z workload has
an elementary classical estimator using O(log(n/delta)/alpha^2) copies.
See Section 9 of the note. No result here establishes faster classical-data
learning, consciousness, hardware feasibility, or the need to make every
computational stage quantum.

## Reproduce locally

Python 3.10 or later and NumPy are sufficient. The bootstrap used Python
3.13.5; the audit and new checks used Python 3.12.14, both with NumPy 2.3.5.

```bash
python -m pip install -r requirements.txt
python checks.py --max-n 4 --output results/baseline-rerun.json
python tools/check_seed_twirl.py --output results/seed-rerun.json
python tools/check_one_qubit_tradeoff.py --output results/one-qubit-rerun.json
python tools/check_product_diagonal_bound.py --output results/product-diagonal-rerun.json
python tools/check_entropy_bounds.py --output results/entropy-bounds-rerun.json
```

The first command after installation checks 14 explicit subset constructions;
the second checks 10 seed-to-interface constructions. The new scripts check
43 one-qubit identities/examples, 10 product-diagonal cases, and 22 entropy-bound
and seed-family cases. These finite
diagnostics supplement the analytical proofs. There is no numerical
optimization or large simulation. No hosted CI run is claimed.

## Collaboration

This project's originating conversation is the Research Lead. The additional
workspace is an independent Proof and Novelty Audit, not a second copy of the
same derivation process. Coordination happens through issues, commit-pinned
notes, and pull requests; separate chats do not automatically exchange results.
Read [AGENTS.md](AGENTS.md) before editing.

Research owner: Ruge Lin. The existing [MIT license](LICENSE), copyright
(c) 2026 Ruge Lin, is preserved. The motivating fiction is not redistributed.
