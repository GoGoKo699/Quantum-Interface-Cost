# Quantum Interface Cost

## How much must remain quantum when the readout is chosen later?

A first module receives one unknown quantum register. A later module will ask
for just one local X or Z readout, but the question is not known when the first
module must release the input. How many qubits must cross that interface if
classical records are free?

**Randomly retaining original qubits is optimal for equal accuracy at
every integer memory budget through four input qubits.** The
[nonflat quarter-rank converse](docs/audits/NONFLAT_QUARTER_RANK_CONVERSE.md)
closes the last four-input case. Together with the one-qubit and half-rank
theorems, it gives

$$
\boxed{\Gamma(n,2^q)=2q+\sqrt2(n-q),\qquad
1\le n\le4,\quad q=0,\ldots,n.}
$$

The best common contrast is `eta=q/n+(1-q/n)/sqrt(2)`. Randomly retain q
original qubits and use the optimal joint X/Z measurement on every discarded
site. The converse allows arbitrary collective encoders, nonuniform seed
spectra, and query-dependent binary decoders at the same worst-case memory cap.

For four inputs and two retained qubits, the new proof keeps the actual
eigenvalues throughout. Positivity and the rank cap constrain the local
Pauli coefficients; a sum-of-squares identity handles one branch, and two
polynomials with positive Bernstein coefficients handle the other. Their
signs are certified by exact rational arithmetic on one rectangle, without
subdivision or numerical optimization. Equality identifies exactly the
two-site retention seeds.

The [dimension-independent continuation](docs/audits/AFFINITY_METHOD_LIMIT.md)
identifies the limit of that proof method. A weighted Hamming star on
15 inputs has rank 16 and violates the proposed general root-affinity bound,
while its actual query score remains below retention. More generally,
the root-affinity sum cannot obey `sqrt(2)n+C log2(rank)` with a fixed C.
The note evaluates the relaxation's asymptotic optimum using established
Faber–Krahn theory and identifies the exact decoder terms it discards.

A [spectral-layer comparison](docs/audits/SPECTRAL_LAYER_SCORE_BOUND.md)
now controls the original score directly: every seed has one common mixture
of nested flat spectral seeds whose query profile differs by at most a
sharp square-root function of the decoder gap. Every layer respects the
original rank cap, and no eigenvalue-spacing assumption is needed. This
quantifies the cost of replacing a nonuniform spectrum; it does not yet
prove the general retention or entropy conjecture.

The [balanced-spectrum theorem](docs/audits/BALANCED_SPECTRUM_OPTIMALITY.md)
now evaluates an entire family at **every input size**. For spectra with
two equally sized eigenspaces, write `rho=(I+tR)/2^n`, where R is a
traceless Hermitian reflection and `0<=t<=1`. The exact maximum original
query score over all eigenvectors is

$$
2(n-1)+\sqrt{4-2t^2}.
$$

For t>0, every maximizing state is one original-site X/Z bisector with
Bloch length t, tensored with maximally mixed spectators. At t=1 this
proves the retention bound and all equality cases for **every flat
half-rank seed, at arbitrary n**. The same family obeys the sharp entropy
bound. Arbitrary nonflat half-rank spectra at larger n remain unresolved.

**Read the [short core argument](docs/CORE_ARGUMENT.md)** for this result,
the exact allocation rule for one retained qubit at every input size, and
a collective advantage for unequal accuracies. Together they separate
three questions:

- **One retained qubit:** the entire local X/Z accuracy region is known.
- **Every integer budget through four inputs:** the equal-accuracy
  optimum above is known, including nonflat seeds.
- **General memories and the asymptotic common-accuracy rate:** still open.
  The smallest remaining finite case is five inputs with two retained qubits.

These are supplied analytical results with independent internal proof
reconstruction. The measurement-simulation framework and the cited
fidelity, monogamy, and entropy ingredients are established prior work;
publication originality remains a separate question. The
[claim ledger](docs/STATUS.md) records precise scope and provenance.
Earlier decoder and channel arguments remain available as supporting
results, including the obstructions to insufficient proof methods.

## Start here

| Purpose | Read |
|---|---|
| Short theorem-led argument with proofs and prior attribution | [Core argument](docs/CORE_ARGUMENT.md) |
| Exact assumptions and baseline proofs | [RESEARCH_NOTE.md](RESEARCH_NOTE.md), Sections 2–7 |
| What is established, derived, or still a target | [STATUS](docs/STATUS.md) |
| Exact four-input, two-qubit optimum, all maximizing seeds, and exact certificate | [Nonflat quarter-rank converse](docs/audits/NONFLAT_QUARTER_RANK_CONVERSE.md) |
| Why the affinity proof cannot yield the general retention bound; exact relaxation profile and decoder gap | [Affinity method limit](docs/audits/AFFINITY_METHOD_LIMIT.md) |
| Original-score comparison with nested flat seeds, with a sharp decoder-gap error | [Spectral-layer bound](docs/audits/SPECTRAL_LAYER_SCORE_BOUND.md) |
| Exact all-size balanced-spectrum optimum and every flat half-rank equality seed | [Balanced-spectrum theorem](docs/audits/BALANCED_SPECTRUM_OPTIMALITY.md) |
| Exact unrestricted half-rank optimum through four inputs and all maximizing seeds | [Half-rank converse](docs/audits/HALF_RANK_RETENTION_CONVERSE.md) |
| Unrestricted collective-encoding problem | [Seed reduction](docs/COLLECTIVE_ENCODING_REDUCTION.md) |
| Two sharp ququart query pairs and an arbitrary third pair obey the retention bound | [Complete sharp-pair converse and exact scalar certificate](docs/audits/TWO_SHARP_PAIR_CONVERSE.md) |
| Sharp sum of the two leading energies for arbitrary pairs, weighted support and equality | [Two-mode support theorem and boundary converse](docs/audits/SHARP_TWO_MODE_SUPPORT.md) |
| Explicit stability near that boundary and a converse allowing nonclassical head channels | [Quantitative stability](docs/audits/QUANTITATIVE_TWO_MODE_STABILITY.md); [robust channel criterion](docs/audits/ROBUST_HEAD_CHANNEL_CONVERSE.md) |
| High second mode with a one-block last query; conserved-symmetry readouts with any last query | [One-block theorem](docs/audits/HIGH_SECOND_MODE_ONE_BLOCK.md); [bound five](docs/audits/CONSERVED_SYMMETRY_CONVERSE.md) |
| Exact link between Pauli support and coherent head structure | [Zero-gap dichotomy](docs/audits/ZERO_PAULI_GAP_DICHOTOMY.md) |
| Exact optimum with one retained qubit | [One-qubit theorem and equality cases](docs/ONE_QUBIT_OPTIMALITY.md) |
| Exact region for separate accuracies at every local query | [One-qubit allocation theorem](docs/ONE_QUBIT_ALLOCATION_REGION.md) |
| Collective advantage for unequal X/Z accuracies | [Exact-axis spectral reduction](docs/EXACT_AXIS_SPECTRAL_REDUCTION.md) |
| Quantitative structure of nearly optimal one-qubit seeds | [One-qubit stability](docs/ONE_QUBIT_STABILITY.md) |
| Exact two-qubit SLD minimum at every spectrum | [Two-qubit spectral theorem](docs/TWO_QUBIT_SLD_SPECTRUM.md) |
| Two-qubit sharp entropy bound when the bottom two eigenvalues sum to at least 1/29 | [All-eigenbasis spectral-tail converse and exact certificate](docs/audits/TWO_QUBIT_SPECTRAL_TAIL_GATE.md) |
| Explicit two-qubit low-rank neighborhood and high-score core stability | [Core-stability theorem and exact scalar certificate](docs/audits/TWO_QUBIT_CORE_STABILITY.md) |
| Sharp two-qubit subspace bounds and all equal-leading-eigenvalue entropy cases | [Subspace theorem and flat-core proof](docs/audits/SHARP_SUBSPACE_AND_FLAT_CORE.md) |
| Sharp all-size parity readout bound and unequal parity-core entropy closure | [Parity theorem and short fidelity proof](docs/audits/PARITY_READOUT_BOUND.md) |
| A structured family that cannot beat the subset strategy | [Product-diagonal entropy bound](docs/COMMUTING_SEED_BOUND.md) |
| Exact regularized formulation of the asymptotic rate | [Entropy-rate characterization](docs/ENTROPY_RATE_CHARACTERIZATION.md) |
| Stronger bound for every collective encoder | [Logarithmic-Sobolev converse](docs/STRONG_ENTROPIC_CONVERSE.md) |
| Linear onset of common-accuracy quantum memory | [Asymmetric entropy converse](docs/ASYMMETRIC_ENTROPIC_CONVERSE.md) |
| Exact memory rate with every X query preserved | [Exact-axis rate](docs/EXACT_AXIS_RATE.md) |
| Complete product-diagonal rate and unequal-accuracy phase boundary | [Profile rate theorem](docs/PRODUCT_DIAGONAL_PROFILE_RATE.md) |
| Publication case and the precise unrestricted-optimality obstacle | [Critical assessment](docs/audits/PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md) |
| Full-profile distinction from steering priors and exact remaining formation identity | [Profile source comparison](docs/audits/PROFILE_NOVELTY_AND_STEERING_REDUCTION.md) |
| Exact two-correlation formation cost and minimum realization dimension | [Dimension and prior comparison](docs/audits/TWO_CORRELATION_FORMATION.md) |
| All qutrit entropy optimizers and a closer weighted-guessing precedent | [Optimizer structure and source map](docs/audits/FORMATION_OPTIMIZERS_AND_PRIOR.md) |
| Incompatible negativity/entropy optima and projective two-input joint decoders | [Resource optima and decoder structure](docs/audits/RESOURCE_OPTIMA_AND_JOINT_DECODERS.md) |
| Complete simultaneous formation/negativity frontier and real-encoder rate equality | [Joint resource frontier](docs/audits/JOINT_RESOURCE_FRONTIER.md) |
| An exact matrix certificate for the unresolved two-input joint entropy bound | [Common-state operator cover](docs/audits/FORMATION_OPTIMIZERS_AND_PRIOR.md#3-an-exact-matrix-certificate-for-the-unresolved-two-input-joint-bound) |
| Why total Holevo budgets and rank-two interpolation do not close the entropy proof | [Proof-method obstructions](docs/audits/ENTROPY_PROOF_RELAXATIONS.md) |
| Entropy-production, coherence and steering-cost precedents | [Entropy trade-off source audit](docs/ENTROPY_TRADEOFF_PRIOR_AUDIT.md) |
| Exact rank-two spectrum trade-off and excluded families | [Entropy-inequality boundaries](docs/ENTROPY_INEQUALITY_BOUNDARIES.md) |
| Sharp flat half-rank result through four input qubits | [Flat-seed theorem](docs/FLAT_HALF_RANK_OPTIMALITY.md) |
| Further entropy exclusions and failed local proof route | [Classical flags](docs/CLASSICAL_FLAG_ENTROPY_BOUND.md), [locally mixed two-qubit states](docs/LOCALLY_MIXED_TWO_QUBIT_BOUND.md), [bounded spectral condition](docs/SPECTRAL_CONDITION_ENTROPY_BOUND.md) |
| Converses covering nonuniform spectra | [Support inertia and geometric neighborhood](docs/SUPPORT_INERTIA_CONVERSE.md), [spectral-tail stability](docs/LOW_RANK_ENTROPY_STABILITY.md) |
| Further exact spectral results and kernel certificates | [Two-level spectra](docs/ENTROPY_INEQUALITY_BOUNDARIES.md), [two-qubit kernel converse](docs/TWO_QUBIT_KERNEL_CONVERSE.md) |
| Why a sharp local squashed-entanglement charge cannot work | [Calibration obstruction](docs/ENTANGLEMENT_CALIBRATION_OBSTRUCTION.md) |
| Exact obstructions to proposed proof shortcuts | [Nonuniform fixed-support optima](docs/NONUNIFORM_SUPPORT_OPTIMA.md), [SLD source and proof-route audit](docs/SLD_ENTROPY_ROUTE_AUDIT.md) |
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

The half-rank theorem proves optimality at `(n,q)=(3,2)` and `(4,3)`;
the quarter-rank theorem closes `(4,2)`. Other budgets at larger input sizes
remain unresolved. A separate entropy
argument excludes every seed whose Gram matrix is diagonal in a fixed tensor
product of local bases, allowing correlated spectra and arbitrary local axes.
It does not assume that unrestricted optimizers have that form.

The asymptotic rate also equals a regularized minimum of the seed's entropy
at the requested contrast. The proof constructs a fixed-dimensional,
trace-preserving interface; it does not change worst-case memory to average
memory. This characterization turns any violation of the unrestricted entropy
bound into a collective rate advantage, but does not yet evaluate the optimum.

For example, at contrast eta=0.8 the new unrestricted entropy converse
requires at least 0.25293250 n retained qubits, improving the previous
logarithmic-Sobolev bound 0.14144054 n; the subset construction uses
asymptotically 0.31715729 n. The new proof combines established quantum
random-access and classical cube-entropy ingredients through normalized
seeds. It preserves the original common-accuracy task.

Writing t=eta-1/sqrt(2)>0, the same proof gives

$$
2\log_2(1+\sqrt2)\,t\le R(1/\sqrt2+t)\le(2+\sqrt2)t.
$$

Thus the memory fraction has **linear onset** at the classical threshold.
The coefficients are approximately 2.54311 and 3.41421; the exact onset
coefficient and full rate remain open. The full nonlinear lower bound
improves on the displayed tangent bound. The earlier converse can be
stronger extremely close to perfect accuracy, so both bounds are retained.

The main research target remains a sharp common-accuracy rate or a proven
collective advantage for that task. Every integer-budget finite problem
through four inputs is now settled. The smallest remaining finite
diagnostic is `Gamma(5,4) ?= 4+3sqrt(2)`, corresponding to five inputs and
two retained qubits. The next priority is a dimension-independent bound
on the original trace norms, retaining the optimal decoder's interaction
with the seed spectrum. The affinity-only extension is now explicitly
ruled out; the original retention conjecture remains open.
For the entropy route,
even a two-input state of rank three could in principle certify a rate
advantage: all rank-two states and all flat rank-three two-input states are
now excluded, but nonuniform rank-three and general full-rank states remain
open outside the excluded families. Any two-input witness must be
nonclassical on both sites and cannot have both marginals maximally mixed.
A full-rank witness must additionally have spectral condition number above
6.235819648. It must also stay outside an open neighborhood of the entire
rank-at-most-two set at that fixed input size. The latter exclusion is proved
analytically; its uniform neighborhood size is existential.

The earlier support and decoder converses remain useful independently,
but their three-input exclusions are superseded by the unrestricted
half-rank theorem. The finite rank theorem does not prove the entropy
inequality or the general asymptotic rate. Publication novelty is not certified.

## Collective advantage for unequal accuracies

Allowing different requested X and Z contrasts, while preserving uniformity
over all inputs and queries, reveals a strict collective advantage.
For 31 input qubits, a 32-dimensional quantum memory (five qubits) can
preserve every X query exactly and every Z query at contrast `1/sqrt(31)`.
The same construction with X contrast `9999/10000` still exceeds the
complete region of strategies that retain at most five original sites,
even allowing branch-dependent retained sets, arbitrary processing on those
sites, and joint measurements of the rest. The note defines that comparison
class precisely and proves its region `sum_i w(x_i,z_i)<=q`.

More generally, with every X query exact, the optimal common Z contrast is
the largest adjacency eigenvalue of an induced Boolean-cube subgraph on at
most D vertices, divided by n. Combining this reduction with an established
graph theorem gives the exact value `sqrt(D-1)/n` for `100000<=D<=n`.
The 31-input example is an achievable separation, without a claim that it is
optimal. This does not settle the original equal-X/Z-accuracy conjecture.

The [exact-axis rate theorem](docs/EXACT_AXIS_RATE.md) now evaluates the
asymptotic quantum-memory fraction when all X queries are exact and the
common Z contrast is z:

$$
R_X(z)=h_2\!\left(\frac{1-\sqrt{1-z^2}}2\right).
$$

This is strictly below the original-site-retention fraction z for every
0<z<1. The separation survives fixed error on both axes: at X contrast
0.99 and Z contrast 0.5, a new explicit mixture reduces the achievable
fraction from 0.354579 to 0.325067,
while that retention class requires exactly 0.39. The unrestricted optimum
with both axes noisy is not evaluated. The entropy curve and corresponding
graph asymptotics are prior, and the same curve is an established dephasing
channel cost. The supplied theorem proves the delayed-query converse and
constructs complete instruments preserving X exactly at every block size.

The [profile theorem](docs/PRODUCT_DIAGONAL_PROFILE_RATE.md) explains where
these savings occur. For `0<z<=x<1` outside the classical disk, its exact
product-diagonal rate is strictly below the retention cost precisely when

$$
\frac{1-x}{1-z}<2\left(\frac1{\ln2}-1\right)^2\simeq0.391958.
$$

This supplies collective advantages throughout that asymmetric region.
On the common-accuracy line, the product-diagonal optimum is still the
subset rate. Improving that line requires seeds outside this family.

The [proof](docs/EXACT_AXIS_SPECTRAL_REDUCTION.md) supplies the complete
trace-preserving instrument analytically. Small diagnostics verify full
three-input instruments and only the 32-vertex support calculation for the
31-input example; no matrix of dimension `2^31` is simulated.

The separate [two-qubit SLD result](docs/TWO_QUBIT_SLD_SPECTRUM.md) evaluates
the minimum over all eigenbases at every spectrum and proves the proposed
SLD entropy inequality for two inputs. Its entropy-only square-root bound
remains weaker than the sharp linear target. Retaining the full spectrum
now proves that target whenever `lambda_3+lambda_4>=1/29`, by an
[analytical reduction and exact rational certificate](docs/audits/TWO_QUBIT_SPECTRAL_TAIL_GATE.md).
This does not close the remaining region. The
[stability theorem](docs/ONE_QUBIT_STABILITY.md) quantifies how nearly
optimal one-qubit seeds approach the exact retaining-one-site form.
These are supplied, internally checked deductions; publication novelty
remains under investigation.

The [sharp subspace continuation](docs/audits/SHARP_SUBSPACE_AND_FLAT_CORE.md)
now proves the entropy target for **every two-qubit state with equal largest
two eigenvalues**, with arbitrary complex eigenvectors and arbitrary remaining
spectrum. Its supporting theorem gives sharp bounds on the four local Pauli
couplings across any two-dimensional subspace, including the universal
constant `7/8`. The flat-core proof uses one scalar polynomial majorant and no interval
partition. Generic unequal-core states and the all-block-size conjecture
remain open.

A [parity theorem](docs/audits/PARITY_READOUT_BOUND.md) now gives the sharp
score `g_n<=n sqrt(2+8q(1-q))` for every state commuting with a product
parity of weight q. One binary measurement and established fidelity theory
prove it. This closes another two-qubit entropy family: an arbitrary
unequal coherent core whose top-two spectral support is a parity sector.
It does not prove the entropy bound for every parity-commuting state.

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
python tools/check_half_rank_retention.py --output results/half-rank-rerun.json
python checks.py --max-n 4 --output results/baseline-rerun.json
python tools/check_seed_twirl.py --output results/seed-rerun.json
python tools/check_one_qubit_tradeoff.py --output results/one-qubit-rerun.json
python tools/check_product_diagonal_bound.py --output results/product-diagonal-rerun.json
python tools/check_entropy_bounds.py --output results/entropy-bounds-rerun.json
python tools/check_entropy_structure.py --output results/entropy-structure-rerun.json
python tools/check_nonuniform_seeds.py --output results/nonuniform-rerun.json
python tools/check_allocation_and_kernels.py --output results/allocation-kernels-rerun.json
python tools/check_entropy_geometry.py --output results/entropy-geometry-rerun.json
python tools/check_asymmetric_rate.py --output results/asymmetric-rate-rerun.json
python tools/check_profile_rate.py --output results/profile-rate-rerun.json
```

The half-rank checker verifies exact scalar witnesses and fixed small matrix
constructions for the new proof; its recorded run is described in
[REPRODUCIBILITY](docs/REPRODUCIBILITY.md). The baseline command checks 14
explicit subset constructions, and the seed command checks 10
seed-to-interface constructions. The new scripts check
43 one-qubit identities/examples, 10 product-diagonal cases, 22 entropy-bound
and seed-family cases, 20 structure diagnostics, 16 nonuniform-seed
diagnostics, 14 allocation, spectral, kernel, and obstruction cases, and
13 exact-axis, SLD-spectrum, and stability cases, 17 asymmetric-entropy
and exact-axis-rate cases, and 18 profile-rate cases. These finite
diagnostics supplement the analytical proofs and use no numerical
optimization or large simulation. Separate bounded exploratory searches
are documented with their limitations in the latest audit; they supplied
no proof of optimality. No hosted CI run is claimed.

## Collaboration

This project's originating conversation is the Research Lead. The additional
workspace is an independent Proof and Novelty Audit, not a second copy of the
same derivation process. Coordination happens through issues, commit-pinned
notes, and pull requests; separate chats do not automatically exchange results.
Read [AGENTS.md](AGENTS.md) before editing.

Research owner: Ruge Lin. The existing [MIT license](LICENSE), copyright
(c) 2026 Ruge Lin, is preserved. The motivating fiction is not redistributed.
