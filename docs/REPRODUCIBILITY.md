# Reproducibility and source provenance

## What was actually run at bootstrap

On 2026-09-22, the original dossier's four manifest entries were verified
against its ZIP contents. The separately attached research note matched the
archived note byte-for-byte. The unmodified original checks.py was rerun with
max-n=4 and tolerance 1e-10. All 14 cases passed, with maximum absolute
matrix-entry residual 2.6645352591003757e-15. The recorded environment was
Python 3.13.5 and NumPy 2.3.5. checks.json preserves the original report;
the bootstrap rerun reproduced it exactly.

The additional seed-twirl script was run on five subset seeds and five dense
complex seeds at n=1,2. All 10 cases passed. Random seed: 20260922. Maximum
absolute matrix-entry residual: 3.1086244689504383e-15. The output is
results/seed_twirl.json. This is fixed-seed reproducible construction testing,
not an optimization or a search for a better code.

These were the bootstrap checks, before the independent proof audit. No
hosted CI run, solver optimality certificate, large-register simulation, or
hardware experiment is claimed.

## Commands

From the repository root, with Python 3.10 or later:

```bash
python -m pip install -r requirements.txt
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
python tools/certify_profile_optimizer.py --output results/profile-optimizer-rerun.json
python tools/certify_two_qubit_tail.py
python tools/certify_two_qubit_core.py
python tools/check_two_qubit_flat_core.py
python tools/check_coherent_transfer.py
python tools/check_parity_and_decoder.py
python tools/certify_extended_core.py
python tools/check_finite_tail_structure.py
python tools/certify_curved_core.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/check_three_input_decoders.py --output results/three-input-rerun.json
python tools/check_spin_flip_purity.py --output results/spin-flip-purity-rerun.json
python tools/check_antiunitary_readouts.py --output results/antiunitary-readouts-rerun.json
python tools/check_jordan_block_converse.py --output results/jordan-block-converse-rerun.json
python tools/check_jordan_spectral_budget.py --output results/jordan-spectral-budget-rerun.json
python tools/check_single_double_block.py --output results/single-double-block-rerun.json
python tools/check_commuting_query_algebras.py --output results/commuting-query-algebras-rerun.json
```

The bootstrap environment was Python 3.13.5 and NumPy 2.3.5. The audit
reruns and new analytical diagnostics used Python 3.12.14 and NumPy 2.3.5. The broader
requirements range is not a matrix of tested environments. Cross-platform
floating-point residuals need not be byte-identical; compare tolerances and
identities. The requirements installation needs package access, but the checks
themselves make no network requests and require no GPU.

## Scope of the evidence

The original script checks parent-POVM positivity, normalization, X/Z marginals,
complete subset-instrument trace preservation, effective-observable identities,
unbiased estimators, second moments, and arithmetic values of analytical bounds.
The largest input Hilbert dimension is 16. It does not check the validity of
the lower-bound proofs or optimize over unrestricted encoders.

The new script explicitly builds the Pauli/permutation/Hadamard instrument
for each supplied normalized matrix seed. It checks trace preservation and
all uniform target observables, including on dense complex seeds. An operator
identity implies agreement on arbitrary input states at those checked sizes;
a finite numerical residual is not a general proof. The full proof attempt
is in docs/COLLECTIVE_ENCODING_REDUCTION.md.

## Subsequent analytical diagnostics

On 2026-09-22, after audit integration at
`df45e2eaceb5669cfff9ac063d3da845d622dac3`, the following were run with
Python 3.12.14, NumPy 2.3.5 and tolerance 1e-10:

| Script and recorded output | Cases and scope | Maximum identity residual |
|---|---|---:|
| `tools/check_one_qubit_tradeoff.py`; `results/one_qubit_tradeoff.json` | 43: ten attaining seeds at all retained sites for n=1,...,4; sixteen dense complex seeds; sixteen decoder-identity cases; one four-dimensional negative control | 1.7763568394002505e-15 |
| `tools/check_product_diagonal_bound.py`; `results/product_diagonal_bound.json` | Ten n=2,3 spectra, with correlations, zeros, bisector equality cases, and local axes with Y components | 9.676811017052383e-15 |

The first script checks normalization, the dual spectral score, extreme
reflection decoders, the scalar/traceless cases, and the CHSH substitution.
The four-dimensional negative control explicitly violates the pair bound
outside its central-qubit hypothesis. Random seed: 20260923.

The second independently compares full eigensolver trace norms to the exact
edge formulas and checks the entropy chain. Its maximum norm-formula error
is 7.771561172376096e-16. Neither script optimizes, proves a universal bound,
or establishes publication novelty. The one-qubit and product-diagonal
proofs were separately reconstructed by another workspace agent. This is
internal independent checking, not external peer review.

The earlier audit reran all 14 baseline and 10 seed-twirl cases successfully,
with the same maximum residuals as the recorded bootstrap outputs. The
historical [audit report](audits/PROOF_AND_NOVELTY_AUDIT.md) remains pinned to
its reviewed bootstrap commit.

## Further converse and family diagnostics

The continuation based on main
`f9a5fc72d15e9d314f6deae65096605e955a2051` added
`tools/check_entropy_bounds.py` and `results/entropy_bounds.json`. Its 22
deterministic cases use matrices of dimension at most eight and no optimizer.
They include rank-two spectrum attainers and complex eigenvectors, arbitrary
flat rank-three complements, Bell/graph stabilizer eigenbases with nonuniform
and zero eigenvalues, balanced flat projectors outside product-diagonal bases,
general full-rank states, and endpoints.

The Dirichlet form is computed independently through partial trace and Pauli
twirling. The script checks their equality and the root-fidelity/affinity/
energy/entropy chain, plus the proved formulas for each labeled family.
The rate table is arithmetic evaluation of the analytical bounds. In
Python 3.12.14 with NumPy 2.3.5, all 22 cases passed at tolerance 1e-10;
maximum identity error was 5.551115123125783e-15 and maximum positive
inequality residual was 1.7763568394002505e-15. Random seed: 20260924.
Eigenvalues at most 1e-14 are treated as numerical zeros; reconstruction
of each input matrix is separately checked against the stated tolerance.
This numerical convention does not restrict the theorem's spectra.

The complete analytical proofs were independently checked within the
workspace. Finite examples do not prove the universal statements, settle
the unrestricted subset conjecture, or certify publication novelty.

## Further structure diagnostics

The continuation based on main
`87b6432cdd1f29bc4981f24bd6732bb933741193` adds
`tools/check_entropy_structure.py` and `results/entropy_structure.json`.
Its 20 deterministic cases have matrix dimension at most 16 and use no
optimizer. They check flat half-rank projectors through four qubits,
the four-sign identity and equality examples, the non-half-rank compression
normalization and rank-seven refinement, classical flags with noncommuting
conditional states, the exact local conditional-entropy counterexample,
rotated Bell spectra and their directional fidelity identity, and spectra
on both sides of the sufficient condition-number threshold.

All 20 cases pass at tolerance 1e-10 in Python 3.12.14 and NumPy 2.3.5.
An independent rerun exactly reproduced the recorded JSON.
Maximum identity residual: 3.552713678800501e-15. Maximum positive
inequality residual: 4.440892098500626e-16. Random seed: 20260925.
Eigenvalues at most 1e-14 are treated as numerical zero, with matrix
reconstruction checked separately. The lower-flat-rank cases are labeled
by the finite-budget estimates they test; those checks do not certify a
general lower-rank entropy inequality. The separate Ky Fan refinement for
flat rank-three three-input states was checked analytically; that refinement
is not a script assertion. Independent analytical reconstruction
within the workspace carries the theorem claims. No external peer review
or publication novelty certification is implied.

## Nonuniform-seed diagnostics

The continuation based on main
`6ddc97a549316ed9edb7a14a110ceee70b87bdf9` adds
`tools/check_nonuniform_seeds.py` and `results/nonuniform_seeds.json`.
All 16 deterministic cases pass at tolerance 1e-10 in Python 3.12.14 and
NumPy 2.3.5; an independent rerun exactly reproduces the JSON. Maximum
matrix dimension is eight. Maximum identity residual is
8.881784197001252e-16; maximum positive inequality residual is
2.220446049250313e-16. No optimization or random search is performed.

The cases check both exact fixed-support optima and flat comparisons,
an explicitly averaged local-bisector twirl of a coherent state,
support-inertia bounds and subset equality, supports below/at/above the
pi/8 semidefinite-compression radius, a complex indefinite block trace-norm
estimate, coherently rotated low-rank cores with spectral tails, and both
failed local SLD steps. Supplied eigenvectors and positive eigenvalues are
used directly to construct square roots. No spectral clipping or inferred
numerical rank is used; one positive tail is 2^(-55), below machine epsilon.
This checks the supplied decomposition in floating-point arithmetic, not
resolution of that eigenvalue by numerical diagonalization.

The exact subset-core sharpening and the compactness neighborhood theorem
are checked analytically. No diagnostic computes the existential uniform
neighborhood size, proves unrestricted optimality, or certifies novelty.
The historical audit report and LICENSE are unchanged.

## Accuracy-allocation and kernel diagnostics

The continuation based on main
`358d887058eb9fa2fe8bb899d0261ec811d42fa6` adds
`tools/check_allocation_and_kernels.py` and
`results/allocation_and_kernels.json`. All 14 deterministic cases pass at
tolerance 1e-10 in Python 3.12.14 and NumPy 2.3.5. An independent rerun
exactly reproduces the recorded JSON. Maximum matrix dimension is eight;
maximum identity error and maximum positive inequality residual are both
3.552713678800501e-15. There is no optimizer or random search.

The script constructs a complete 48-branch, three-input instrument with
unequal site-retention probabilities and unequal X/Z contrasts. It checks
trace preservation, all six effective-observable identities, and the
dimension-two output cap on every branch. A separate weighted seed attains
the new support-function bound. Further cases check rank-three kernel
inertia, the Pauli sum identity, adjugate and rearrangement certificates,
one-distinguished-eigenvalue formulas and attainers through three inputs,
and a two-doublet spectrum with an attaining projector.

SLD values are compared with the exact integrated Fourier remainder using
finite spectral sums, with no numerical quadrature. The nonphysical graph
example is explicitly labeled as a failed relaxation, not a quantum-state
counterexample. The near-Bell obstruction compares the proposed charge
with the valid half-mutual-information upper bound; squashed entanglement
is not numerically evaluated. Supplied spectral decompositions construct
square roots directly, with no spectral clipping or inferred numerical rank.

The complete proofs and primary-source mappings were independently checked
within the workspace. These finite diagnostics do not prove the full accuracy
region, settle the unrestricted entropy conjecture, or certify publication
novelty. The historical audit report and LICENSE remain unchanged.

## Exact-axis, SLD-spectrum, and stability diagnostics

The continuation based on main
`f761bbca3ba3c1b263a1914175e3bdab94be70a7` adds
`tools/check_entropy_geometry.py` and `results/entropy_geometry.json`.
The local checkout was unavailable after a workspace disconnection; these
files and the three accompanying proof notes were reconstructed from the
research checkpoint and checked again. This is a new recorded run, not a
claim that the lost draft was recovered byte-for-byte.

All 13 deterministic cases pass at tolerance 1e-10 in Python 3.12.14 and
NumPy 2.3.5. Maximum identity residual is 2.6645352591003757e-15;
maximum positive inequality residual is 1.7763568394002505e-15. An
independent rerun exactly reproduces the recorded JSON. Maximum matrix
dimension is 32. There is no optimizer, random search, spectral clipping,
or inferred numerical rank.

Two cases construct complete three-input translation instruments: an
eight-branch star and a 24-branch asymmetric-support example with cyclic
coordinate flags. They check trace preservation, exact-X intertwining,
and all six effective-observable identities. A third case evaluates only
the 32-vertex support graph, Perron vector and scalar separation for
n=31,q=5. Its full input dimension is 2^31; no such input matrix or
complete 2^31-branch instrument is built numerically.

Six SLD cases cover pure, rank-two, two rank-three, unequal full-rank and
uniform spectra. Each uses an explicit complex eigenbasis and the ordered
product-basis attainer. They check spin flip, bistochastic transition
weights, all 24 assignment costs, the SLD/entropy inequalities, and the
seed score bound. Four stability cases at n=1,3,4,3 construct actual sign
decoders and their dual Hamiltonian from perturbed seeds. They verify the
spectral gap, an exact subset certificate, overlap and Frobenius-distance
bounds. This is not a closest-seed optimization.

The full analytical proofs were independently reconstructed within the
workspace; primary ingredients and unresolved novelty are recorded in
each proof note. No large simulation, hosted CI, external peer review,
or publication-novelty certification is claimed. LICENSE and the
historical commit-pinned audit are unchanged.

## Asymmetric entropy and exact-axis rate diagnostics

The continuation based on main
`9697d4d72cc34c52f4680fbf0c588b39af5c0471` adds
`tools/check_asymmetric_rate.py` and `results/asymmetric_rate.json`.
All 17 deterministic cases pass in Python 3.12.14 / NumPy 2.3.5, and an
independent rerun exactly reproduces the JSON. Maximum matrix dimension
is 16. At tolerance 1e-10, the maximum identity residual is
3.3306690738754696e-15 and maximum positive inequality residual is
8.881784197001252e-16.

Twelve explicitly specified complex or equality-case seeds test the
classical-quantum entropy identity, biased-prior Helstrom/Fano bounds,
conditional-entropy chain, cube-flip overlaps, and asymmetric seed bound.
Three of these assert equality for product bisectors, an exact-axis
Bernoulli seed, and a maximally mixed endpoint. Four further cases build
the complete translation instruments for small Bernoulli supports,
including one full-support endpoint; all local effective observables,
normalization, truncation trace distance and applicable support/tail
estimates are checked. Small-block attainment of the asymptotic rate is
not asserted.

One scalar case checks the entropy curve, interior separation and displayed
derivative formulas by centered differences. That derivative comparison
has separate absolute allowance 2e-6 at step 1e-4; the algebraic identities
and theorem inequalities use 1e-10. The scalar rate tables are evaluations
of proved formulas, not simulation or optimization results.

Every probability/positive-semidefinite endpoint adjustment is checked
against 1e-12 and listed in the JSON: there are 42, with largest actual
adjustment 2.220446049250313e-16. There is no numerical rank inference,
unreported spectral clipping, random search, optimizer or large-block
simulation. The proofs and primary-source mappings were independently
checked within the workspace. These finite diagnostics certify neither
the universal statements nor publication novelty. LICENSE and the
historical audit are unchanged.

## Product-diagonal profile diagnostics

The continuation based on main
`3ebde02b2d9d5dcdcd0dd445e4a16b4f5aaf03b0` adds
`tools/check_profile_rate.py` and `results/profile_rate.json`.
All 18 deterministic cases pass in Python 3.12.14 / NumPy 2.3.5;
an independent rerun reproduces the recorded JSON exactly. The largest
matrix dimension is eight. Maximum identity and positive inequality
residuals are both 6.0443533557040756e-15 at tolerance 1e-10.

Seven specified qubit states check the Bloch score formula, including Y
components and pure/mixed endpoints. Four correlated product-diagonal
states on two or three qubits check full-matrix trace norms against edge
decompositions, conditional entropies and weighted profile bounds. Three
zero-mass edges are explicitly omitted by the stated mathematical rule.
Five scalar cases check the exact-axis conjugate and selected weighted
supports. One case checks the rational mixture using exact Fraction
arithmetic; its entropy is separately evaluated in floating point. The
remaining case checks five fixed profiles against the analytic phase
criterion, including its boundary.

Conjugate maximizers use monotonicity of f' and ordinary floating-point
bisection, with bracket widths at most 2e-14. The recorded derivative
brackets are diagnostics, not directed-rounding certificates or optimizer
proofs. Both endpoint roundoff adjustments are reported explicitly: each
is 2.220446049250313e-16, below the allowance 1e-12. No numerical rank
inference, random search, large-block simulation or new complete-instrument
enumeration is used. The existing complete-orbit and truncation proofs
carry achievability; the new analytical proof and phase boundary were
independently reconstructed within the workspace. The source audit records
established ingredients and unresolved publication novelty separately.

## Exact rational certificate for the constructive profile optimizer

The continuation based on main
`65fabd7d870df705193017cc61e7230fc4943a5b` adds
`tools/certify_profile_optimizer.py` and
`results/profile_optimizer_certificate.json`. The analytical theorem in
[the profile note](PRODUCT_DIAGONAL_PROFILE_RATE.md), Section 5.1, proves
global optimality within its stated comparison class and uniqueness of
the scalar root. The script encloses that root and the rate at the single
specified profile `(99/100,1/2)`; it does not prove the general theorem.

This certificate uses only standard-library Python integers, `Fraction`
and `isqrt`. There is no floating-point arithmetic. Each arithmetic
operation rounds outward to a 75-place decimal lattice; square roots use
65-place exact integer enclosures. Logarithms are range-reduced to an
atanh argument in `[0,1/3]`; 100 series terms and an explicit rational
positive remainder bound enclose their values. Decimal output endpoints
are rounded outward to 18 places and represent exact rational numbers.

The verified root bracket is `[0.52576013296870,0.52576013296872]`.
The cost enclosure is
`[0.324848239185893024,0.324848239186576377]`, of width below `6.834e-13`.
The endpoint signs are separated from zero by exact rational intervals.
All mixture parameters are certified physical, and the cost is strictly
smaller than the earlier explicit mixture. These are genuine interval
certificates for the stated scalar quantities, unlike the earlier
floating-point bisection diagnostics.

The script and interval formulas were independently read; a root-workspace
rerun on Python 3.12.14 reproduced the recorded JSON byte for byte. Checks
use explicit exceptions and remain enabled under `python -O`; the
implementing agent also verified an identical optimized replay. No matrix
optimizer, network call, GPU or large-block simulation is involved. Old
construction diagnostics were not rerun because their formulas and
implementations were unchanged. Publication novelty and unrestricted
optimality are outside this certificate's scope.

## Tensor-formation and channel comparison

The continuation pinned to main `3a668f92afe5145e3273c5796ee74e0120214e1f`
is an analytical proof audit. Independent internal reconstructions checked
the exact moment twirl and finite ensemble reduction, simplex compensation,
one-qubit rigidity/parity contradiction, rank-three Kraus construction,
compactness extension, Pauli-channel completion and full profile equality
set. No new numerical optimization or large simulation was used. The
explicit qutrit instrument is verified symbolically in the report; its
rank, completeness and induced effects do not depend on a tolerance or
solver output. Unchanged earlier diagnostics were not rerun. None of these
checks establishes exhaustive novelty or the missing unrestricted entropy
inequality. See [the complete proofs](audits/TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md).

## Roof provenance and joint-score continuation

The audit pinned to `b1f93ac69e4007f9d21df16ab16aa5bbecf94332` used
primary theorem statements and exact mathematical reconstruction. Internal
independent reviews checked the rank-two gap seed, all four primal/dual
context certificates, product additivity including collective readout,
and the single-effect variational formula for complex and singular states.
Review caught and corrected a dual-attainment caveat: the full-space dual
may only have an infimum for singular seeds; support compression gives an
attained minimum. The Cope–Uola SDP twirl and Vollbrecht–Werner assumption
maps were reviewed separately. No new matrix search, solver certificate or
large simulation was used; unchanged numerical diagnostics were not rerun.
See [the exact proofs and limits](audits/ROOF_PROVENANCE_AND_JOINT_SCORE.md).

## Two-correlation dimensions and proof-method obstructions

The continuation pinned to `d74f329605c9cf82707c09a3c0e925919e8512c0`
used exact proof reconstruction. Two independent internal reviews checked
the qubit CHSH normalization, arbitrary binary contractions, signed
pure-component converse, fixed qutrit pair, radial strictness and all
dimension/equality cases. Primary-source review checked Verstraete–Wolf,
Zhu–Zhang–Ma and Schneeloch–Howland at the locators recorded in
[the dimension audit](audits/TWO_CORRELATION_FORMATION.md). Tomassoli's
thesis was available only at metadata/abstract level at that research
base. The full-text comparison is now completed in the follow-up below.

Independent reviews also checked both exact constructions in
[the proof-method note](audits/ENTROPY_PROOF_RELAXATIONS.md): the classical
channel's prior, information and Hamming loss; and the larger-class
Hamiltonian's spectrum, arbitrary-complex-rank-two bound, strict entropy
violation and forbidden trusted-Pauli coefficient. Neither is an admissible
counterexample to the quantum conjecture. No numerical optimization,
matrix search or large simulation was used. Earlier diagnostics were
unchanged and not rerun. These checks establish neither unrestricted
optimality nor exhaustive originality.

## Formation optimizer equality and weighted-guessing prior

The further [optimizer/source audit](audits/FORMATION_OPTIMIZERS_AND_PRIOR.md)
is pinned to `d3000ccc1f89fc357ebce7025bb166df2197e7d7`. Internal
independent reconstruction checked the weighted concurrence support,
strict entropy-conversion comparison, supporting-plane equality chain,
all four classical sign sectors and the complete qutrit optimizer family.
Han et al.'s primary arXiv version and supplement were inspected directly.
Public OAI metadata supplied the canonical Tomassoli PDF link, but its
full text still returned HTTP 403; no mathematical content is attributed
to that unread source. The common-state operator-covering equivalence
also received independent review of normalization, dual signs, Slater
feasibility, attainment and singular-state limits. No numerical solver
was used to claim a feasible or infeasible covering instance. No numerical
search supports these deductions; unchanged diagnostics were not rerun.

## Resource optima and projective joint decoders

The continuation pinned to `6367ab89601eb45485cba15df8feabb553e0fac1`
supplies analytical proofs of the full ordinary-negativity profile,
formation cost among negativity minimizers, and optimal two-input joint
decoder structure. Independent internal reviews reconstructed the common
reflection dilation, Jordan pinching, partial-transpose bound, equality
contacts, exact-axis exception, SDP complementarity, singular compactness
limit and rank-two projection reduction. Direct primary-source reads
checked the Pusey, Guehne–Reimpell–Werner, Eisert–Brandao–Audenaert and
Das et al. version/equation/page maps. These checks are not external review
or historical-priority certification.

Small exploratory computations were separate from those proofs. A
common-state joint SDP used six deterministic initial states and eight
updates per state, with CVXPY 1.9.3 / Clarabel 0.11.1 in a scratch-only
environment. Forty of 48 outputs had `optimal_inaccurate` status; the
smallest assemblage eigenvalue reached approximately -1.12e-8. No positive
entropy excess was observed, and no output is a certified feasible cover
or an upper bound. Separate bounded local-objective and fixed-spectrum
searches likewise supplied no certified violation. These were exploratory
attempts, not an extension of the repository's regression suite. No large
simulation was run. The stated theorems require none of their numerical
outputs. Unchanged construction diagnostics were not rerun.

See [the proof report](audits/RESOURCE_OPTIMA_AND_JOINT_DECODERS.md).

## Joint resource frontier and real encoding

The [continuation report](audits/JOINT_RESOURCE_FRONTIER.md) is pinned to
main `f5c2486d5fee236eb4d2c0f15f5b1a80b5ef6306` and tree
`24fc783fb7d9dfb77686d7df67a732806da96450`. Its analytical checks cover
the mixed ordinary-negativity support bound, every nonnegative resource
price, endpoint derivatives, the explicit phase/root calculation, and
convex separation over a compact generator hull without assuming a bound
on Alice's dimension. A separate adversarial reconstruction found no
substantive flaw. The Kraus realification, uniform error on arbitrary
complex inputs, and tensor-seed/global-real-part argument were separately
checked. These are internal proof reviews, not external peer review.

Primary-source reads cover the versions and theorem locators stated in
the report. Tomassoli's thesis and the 2012 Nakahira–Usuda rank theorem
were then full-text gaps; both have since been read in the follow-ups
below. No absence-of-prior-art conclusion is certified.
No large simulation or new solver output underlies the results, and the
unchanged repository diagnostics were not rerun. Local links, whitespace,
and the identities of LICENSE and the historical audit were checked.

## Two-qubit spectral-tail certificate

The [partial entropy converse](audits/TWO_QUBIT_SPECTRAL_TAIL_GATE.md) is
pinned to main `07f557be8d5863f27304b1060274a14bfee1cd50`, tree
`de1570ec31021b198ffc5b53c93e9c447b550b98`. Its analytical reduction and
finite certificate were independently reconstructed within this workspace.
The certificate covers every ordered two-qubit spectrum with bottom-two
weight at least `1/29`, without restricting complex eigenvectors.

`tools/certify_two_qubit_tail.py` uses only standard-library rational and
integer arithmetic for acceptance. It checks 400 closed interval enclosures
on `[1/29,9/25]`, a balanced-spectrum endpoint, and the exact inequalities
used for the remaining interval. Decimal output is diagnostic only.
It was run with Python 3.12.14, both ordinary and `python -O`; explicit exceptions
keep all acceptance checks active in both modes. The reported minimum
determinant is approximately `0.00007866733984615593`, balanced margin
`0.003513637500858673`, and high-tail margin `0.03165915412695304`.

The certificate proves the finite scalar comparisons conditional on the
analytical argument and the previously proved SLD envelope. It does not
certify the unhandled low-tail region, arbitrary-block optimality, or
originality. No large simulation or new solver output is used. Unchanged
construction diagnostics were not rerun; the new certificate, local links,
whitespace, and the protected file identities were checked.

## Two-qubit core stability and explicit neighborhood

The [core-stability report](audits/TWO_QUBIT_CORE_STABILITY.md) is pinned to
main `b653fe866930aa8d1c07ad3bf34629a14b41009a`, tree
`fb3049fa092eda007d470bad8873038787638c30`. Independent workspace
reconstruction covered the noncommutative block inequality, decoder
classification, coupled support angles, Cheng--Hall normalization, finite
stability constants, scalar reductions and their domain coverage. The
unbalanced-core exclusion and uniform entropy margin were separately
checked analytically. No external peer review is claimed.

`tools/certify_two_qubit_core.py` uses integer endpoints divided by `2^80`,
outward-rounded arithmetic, integer square roots, and a 72-term positive
logarithm series with an explicit remainder bound. It certifies a scalar
disjunction over every point of 755 closed boxes, after the analytical
reduction in the report. There are 476 strict SLD exclusions and 279
strict stability certificates, 754 subdivisions, and maximum depth 16.
The smallest positive stability-margin numerator is `12665039428067297599`
with denominator `1208925819614629174706176`. The recorded output is
[results/two_qubit_core_certificate.json](../results/two_qubit_core_certificate.json).

The script was run with Python 3.12.14, ordinarily and with `-O`; both
reproduced the same output. Acceptance uses explicit exceptions, with no
floating-point decisions, random state sampling, optimization solver or
large simulation. The explicit full n=2 radius `2^-20` additionally uses
the separately supplied analytical core-gap and cross-block estimates;
that conclusion cannot be inferred from the interval script alone.
Whitespace, local links, LICENSE and historical-audit identities were
checked. Unchanged construction diagnostics were not rerun.

## Original archive provenance

The user-provided archive was Q1_Quantum_Interface_Dossier_v0_1.zip.
Its SHA-256 is
`3f3538c0307f3a1131746d84410b21752b97aa0e87d8de1722392d3b114dd8ec`.
The following three files were imported unchanged at bootstrap commit
`eaf085a8cb299e6b297b11d2dc3c85e24f02779e`. These are historical hashes; the
research note has subsequently been revised to version 0.23:

| File | SHA-256 |
|---|---|
| RESEARCH_NOTE.md | 0af31a81b3b5db1534746d321d238d9fc1677bda93cc25bb0458010874ccc1b8 |
| checks.py | f99052c18cb2d98b5cbf9fea6470a64bdbac7e0ac955a548138a9a4de5d7f50b |
| checks.json | 0a4b94a30bab50049dbf30c97b9a8e4f8a964dac2eadb9d3c11fd077451ab516 |

The archive README is replaced by a repository-specific front page, so its
original four-file manifest is not presented as a manifest of this repository.
The source ZIP and fiction PDF are not redistributed. The fiction's page-24
interface discussion is an inspiration, not evidence for the mathematical
claims or permission to publish unrelated narrative content.

The user's original repository main was
`310a0730a04ada47eeda41bada41412414442ee1` (LICENSE only).
The existing license blob `e17a781bf47c4aadf18b68fc593846a1193b86c1`
is preserved rather than recreated during the GitHub tree update.

## Sharp subspace and flat-core continuation

The [report](audits/SHARP_SUBSPACE_AND_FLAT_CORE.md) reviews main commit
`fa2443ca413a5c1935722db1c1415be0c7ad7266`. Its canonical compressions,
sharp subspace bounds, exact attainers, fidelity pinching and entropy
reduction were independently reconstructed within the workspace.

`tools/check_two_qubit_flat_core.py` uses only standard-library rational
arithmetic. It expands the scalar proof's polynomial identities, verifies
nine positive Bernstein coefficients, and checks the exact endpoint margin
`151/23312520`. It uses no interval subdivision, matrix sampling, solver,
or floating-point acceptance tolerance. Run it normally or with `python -O`;
both produce the same [recorded output](../results/two_qubit_flat_core_check.json).
The script checks these algebraic ingredients, not the analytical reductions,
full two-qubit optimality, or originality. The proved entropy scope is every
complex two-qubit state with `lambda_1=lambda_2`, using the previously proved
high-score-core and spectral-tail gates for the complementary cases.

## Coherent-transfer audit

The [report](audits/COHERENT_TRANSFER_AUDIT.md) reviews main
`fab95daf5e1f9a7d42ef778e3494330fa8e1c73f`. The two-line block proof,
physical decoder construction and conditional entropy implication were
independently reconstructed within the workspace. No additional entropy
theorem or originality claim results from this continuation.

`tools/check_coherent_transfer.py` checks the counterexample's physical
Pauli compressions, decoder reflections, radical score identities and
rational sign certificates using exact arithmetic. Normal and optimized
Python runs produce the same [recorded output](../results/coherent_transfer_check.json).
The finite support-function inequality remains unproved; the checker
does not test or certify it. The report separately labels the bounded local
falsification screening, which is not used in a proof.

## Parity and mixed-decoder continuation

The [parity report](audits/PARITY_READOUT_BOUND.md) and
[operator note](audits/MIXED_DECODER_PATTERN_BOUND.md) review main
`ef3a6c9f62f7b9b591b56503ba5d24e0b10d2c12`. Their arguments were
independently reconstructed within this workspace, including the binary
fidelity witness, complex-state scope, all-n attainer, two-qubit entropy
case split, decoder canonicalization and characteristic-root comparison.

`tools/check_parity_and_decoder.py` uses standard-library exact rational
sparse polynomials. It expands the 4x4 determinant by its 24 permutation
terms and verifies the orientation derivative, endpoint residual, scalar
majorant, witness reflection/sign flip and rational entropy margin 25/348.
Normal and `python -O` runs on Python 3.12.14 produce identical
[recorded output](../results/parity_and_decoder_check.json). There is no
floating-point acceptance or interval partition. These checks support the
displayed analytical reductions; they do not certify unrestricted entropy
optimality, extend the tail certificate, or establish publication novelty.

## Extended core transfer

The [extension](audits/EXTENDED_CORE_TRANSFER.md) reviews main
`449984f346ed396f515c885cb0c5921cb7739735`, tree
`9ee1a7d345d3fc574791cbf36cba90481dce1407`. Independent workspace
reconstruction checked the three anticommuting sets, Young inequality,
core-purification hypothesis, stronger sine estimate, quadratic minimization,
elementary angle cutoff, and inverse-compression bounds on the larger domain.
There is no new external review or hosted CI claim.

`tools/certify_extended_core.py` imports the existing outward-rounded
integer interval arithmetic from `certify_two_qubit_core.py`. It uses no
logarithm evaluation in its scalar test, no floating-point decisions,
no density-matrix sampling, and no solver. It certifies `U(m)<1/10` and
`C(m)<49` throughout `m in [7/32,1/2]`, with positive-part extension
where the high-score hypothesis is impossible. The 97 closed leaves cover
the entire initial interval; their maximum depth is 8. Failure to resolve
a box raises an exception, including under optimized Python.

Normal and `python -O` executions on Python 3.12.14 reproduce the same
[record](../results/extended_core_certificate.json). The minimum angle
and constant margin numerators are `22610467235550810200` and
`14480460893618248359602`, respectively, over `2^80`. These are exact
scalar certificates conditional on the supplied proof, not tests of the
unrestricted conjecture. The report separately gives an entirely elementary
`1/201` tail cutoff. Local links, whitespace and protected file identities
were checked; unrelated numerical construction diagnostics were not rerun.

## Finite-tail structure and Bayes-rank source comparison

The [matrix report](audits/FINITE_TAIL_STRUCTURE.md) and
[source comparison](audits/BAYES_RANK_PRIOR_COMPARISON.md) review main
`3964f9b97766463a2aff65233560c9dcdf60c297`. Independent workspace
reconstruction checked contraction completion, both concavity reductions,
the variational root ordering, positive-parameter tangent, product-support
attainers, and the entire weighted Bayes-rank obstruction. The prior paper
was read from its official publisher PDF; it is not redistributed.

`tools/check_finite_tail_structure.py` verifies exact rational polynomial
identities for the block characteristic polynomial, Vieta discriminant,
scalar-root second derivative and determinant square decomposition. It also
checks Bayes normalization and the incompatible strict weight conditions
for all four decisions. Normal and `python -O` runs produce the same
[record](../results/finite_tail_structure_check.json). There is no interval
partition, floating-point acceptance or state sampling in this checker.
The continuum claims rely on the supplied analytical proofs, and the
general four-query transfer target remains unproved.

## Curved core transfer through the full high-score strip

The [proof](audits/CURVED_CORE_TRANSFER.md), pinned to the same main
`3964f9b97766463a2aff65233560c9dcdf60c297`, was independently reconstructed
for root-fidelity pinching, definite core/tail score preservation, the
convex chord and endpoint-mass tangent, active finite-tail curvature,
the imbalanced SLD disk, and elimination of the tail eigenvalue parameter.
The theorem concerns normalized top-two cores; all operational quantifiers
remain unchanged.

`tools/certify_curved_core.py` imports the previously checked 80-bit
outward-rounded integer interval arithmetic and positive-series logarithm
enclosures. It exhausts the closed four-variable scalar enlargement in
10,647 visited boxes: 5,324 terminal leaves, with 1,868 strict transfer
certificates, 2,898 strict SLD certificates and 558 infeasible boxes.
Maximum depth is 20. The minimum positive transfer and SLD margin
numerators are `416550709650178248` and `1311935999616578036`, over `2^80`.
These deliberately conservative bounds include impossible parameter
combinations; no simultaneous physical saturation is assumed.

Every arithmetic and subdivision comparison uses integers. Unresolved
boxes, exhausted budgets or subdivision failures raise exceptions under
both normal and optimized Python. Both runs on Python 3.12.14 reproduce
the same [record](../results/curved_core_certificate.json). Earlier floating-
point scalar probes motivated the reduction but are not its proof or part
of the certificate. No large state simulation or solver is used. Local
links, whitespace, LICENSE and historical-audit identities were checked.

## User-supplied Tomassoli thesis: full-text comparison

The [source audit](audits/TOMASSOLI_FULL_TEXT_COMPARISON.md) reviews
main `c2857e9b912ceae47d3067a62aa1f07f4acb1cf2`. The user's 27-page,
3,085,312-byte PDF has SHA-256
`0c84d0246528c900559b678c54a1f63393f6d18e54be377b88fa653254c2b7ab`.
It was read directly from the supplied attachment. Title and authorship
match the institutional record; byte identity with an independently
downloaded institutional copy was not asserted. No third-party PDF,
render or extracted text is committed.

All pages were read, with visual checks of defining and disputed equations
against rendered pages. Two independent internal reconstructions checked
the corrected scalar minima, Bell-diagonal two-parameter attainers, all
weighted calibrated witnesses, rational product-state separator, exact-axis
overlap and printed counterexamples. Eisert–Brandao–Audenaert's primary
arXiv PDF was also read at the specified equation/page locators. These
checks close the named source gap, not exhaustive originality.

This is an exact proof and source-comparison change; it introduces no
simulation or solver result. Unchanged entropy certificates were not
rerun. Repository links, whitespace and protected-file identities were
checked. Historical access-failure accounts are retained with follow-up
links; the request for the thesis is resolved by the user's upload.

## Nonlinear CHSH theorem and the sharp resource hull

The [subsumption audit](audits/NONLINEAR_CHSH_SUBSUMPTION.md) reviews
main `ac0bf7cebd5a8a346d8b64371edab7b2c30ca271`. The official
Zhu–Zhang–Ma arXiv v2 PDF and its HTML were read at the specified
definition, theorem and dimension-reduction locators. The ordinary-N
factor and Corollary 1 were also checked against rendered PDF pages.

Independent workspace derivations checked the auxiliary-angle map,
subthreshold case, minimizing alpha>=1, zero-weight endpoints, all
nonnegative resource prices, common-space reflection dilation, Jordan
pinching, flag identities and exact support attainers. They confirm a
stronger prior implication than the earlier affine-only comparison:
the mixed-state support and full minimum-cost convex hull are short
prior corollaries. The explicit phase/root formulas are unchanged.

The source comparison needs no simulation or numerical acceptance test.
Unchanged entropy certificates were not rerun. Separate small exploratory
four-dimensional searches of a possible spectral-product reduction and
finite-tail envelope yielded no proof or admissible counterexample; they
are not used in the report's deductions or any optimality claim. Local
links, whitespace, LICENSE and the original audit identity were checked.
No primary paper, extracted text or rendered page is committed.

## Short core argument

The [core argument](CORE_ARGUMENT.md) is pinned to main
`e197699d87171635028d1639e025c8e5759e5c68`. It condenses existing results;
it introduces no new optimality or originality claim. Separate workspace
agents reconstructed the weighted one-qubit converse and its allocation
geometry, the complete 31-input star instrument and the full stated
retention-class converse, and the primary-source attribution. Review of
the draft added an explicit minimality argument for w and specified the
nonnegative weights in the retention bound.

The construction is verified by symbolic operator identities, including
completeness of all translated Kraus branches. No 31-qubit simulation was
run or needed. Unchanged numerical certificates were not rerun. Local
Markdown links, whitespace, LICENSE and the original audit identity were
checked. This is internal independent proof reconstruction, not external
peer review or certification of priority.

## Decoder algebra and the three-input continuation

The [report](audits/DECODER_ALGEBRA_AND_THREE_INPUT.md) is pinned to main
`f46ed69785ace49d6f3f52645fefbb9dbdc99f1f`. Independent internal proof
reconstructions checked the prior graph-Clifford dimension bound, the
alternating-matrix matching argument, normalized Kraus transfer, the
weighted q=n-1 extension, and the explicit obstruction to replacing every
seed's optimal readouts by pairwise commuting/anticommuting reflections.
Primary-source comparisons distinguish established algebra from the
supplied operational deductions.

`tools/check_three_input_decoders.py` runs 248 small complex initializations:
128 unrestricted seeds and 12 in each of ten nonscalar decoder-signature
sectors, with subsequent unrestricted release. Its largest Bell matrix
is 32 by 32. Python/NumPy versions, fixed seeds, tolerances, source hash,
iteration counts, known analytical controls and sector summaries are
recorded in `results/three_input_decoders.json`. No candidate exceeded
the subset benchmark by the stated 1e-9 detection tolerance. This is
bounded numerical evidence, not an upper-bound or optimality certificate.

The parent workspace reran this diagnostic independently and reproduced
the JSON byte-for-byte with Python 3.12.14 and NumPy 2.3.5. Unchanged
entropy certificates were not rerun. Local links, whitespace, the LICENSE
blob and the historical audit blob were checked. No primary-source PDFs,
extracted text, or unreported numerical candidates are committed.

## Full weighted decoder allocation

The [follow-up proof](audits/WEIGHTED_DECODER_ALLOCATION.md) is pinned to
`98fa6f4bb9849d6d8317cd93cc14626d288a9ec5`. Independent internal
reconstructions checked the threshold-ordering lemma, strict triangularity
over `F_2`, threshold equality, active-site restrictions, finite operator
decomposition, zero and repeated deficits, endpoint budgets, sharp weighted
attainment, and normalized Kraus transfer. This extends the full accuracy
region from q=n-1 to every integer memory budget for the same explicit
readout class. It needs no numerical optimizer or new computational gate.

The simultaneous weighted-matching conjecture was not proved and is not
used: different operator levels may have different matchings. The separate
unrestricted balanced-sector attempt yielded no universal nonflat proof;
an exact GHZ counterexample refutes one proposed intermediate shortcut.
Neither that failed shortcut nor finite search evidence is a claim about
the unrestricted optimum. Local links, whitespace, LICENSE and the original
audit blob were checked. Unchanged numerical certificates were not rerun.

## Sharp spin-flip purity bound

The [proof](audits/SPIN_FLIP_PURITY_BOUND.md) is pinned to main
`e97d0d4a164c73c8ce1d945febadc1d267c0b6d5`. Independent internal
reconstructions checked the Kramers-paired spectrum, rank-two completion,
support determinant identity, every quadratic coefficient, the exact
sum-of-squares certificate, sharpness at every allowed purity, the
symmetry-fixed extremal eigenvector argument, and the complete Pauli-orbit
instrument. The primary-source comparison checks the published Uhlmann
paper and corrected arXiv version at the specified equation/page locators.
This is internal review, not external peer review or a priority certificate.

`tools/check_spin_flip_purity.py` records 47 constructions in
`results/spin_flip_purity.json`: eight deterministic complex Kramers
supports at five spectral imbalances, five members of the exact
all-purity attaining family, one cyclic uniform attainer, and one
deliberately nonsymmetric negative control. The 46 invariant states
include rank-two endpoints. The negative control's squared-score sum is
five against an inapplicable bound of four; it tests the scope of the
hypothesis and is excluded from the theorem residual.

The checks passed with Python 3.12.14, NumPy 2.3.5, random seed
2026092403, tolerance 1e-10 and spectral-zero threshold 1e-14. The
imbalances are -1, -0.37, 0, 0.4 and 1; the largest matrices have dimension
eight. Square-root reconstruction is checked after clipping numerical
zeros. Maximum identity error: 7.105427357601002e-15. Maximum positive
inequality residual: 3.1086244689504383e-15. The source SHA-256 is
`e5eff393daacd668fec2e7755bad97a2b221f4a137494741627df59e6d4160b9`.
The parent workspace independently reran the script and reproduced the
JSON byte-for-byte. No optimization or broad search is performed.

Finite checks do not establish the symbolic theorem, unrestricted
optimality, or publication novelty. Unchanged numerical certificates were
not rerun. Local links, whitespace, LICENSE and the original audit blob
were checked. No third-party PDF, extracted source text or private
exploratory material is committed.

## Every common antiunitary readout symmetry

The [unified theorem](audits/ANTIUNITARY_READOUT_BOUND.md) is pinned to
main `0730608b9daa9ba09a27843d57b47134a5852fd4`. Independent internal
reconstructions checked the two commuting Pauli algebras, every split-site
assignment, the arbitrary-square eigenspace argument, the contraction
extension, the stronger +I equal-weight estimate, and normalized Kraus
transfer. The actual report was reviewed with general binary POVMs and
uniform errors retained. This is internal review, not external peer review.

`tools/check_antiunitary_readouts.py` records its finite construction
checks in `results/antiunitary_readouts.json`. All 64 assignments of six
+I-class reflection readouts to the two Pauli factors are checked with
three weight vectors each. A cyclic -I attainer and a nonscalar-square
paired-sector example are each checked with those three vectors, for
198 Hamiltonian eigensystems of dimension 32. The script separately
checks the logical factor identification, an exact quadratic attainer,
and a balanced sextuple whose antiunitary-intertwiner system has only
the zero solution. That last control is not a score-bound violation.

The run passed with Python 3.12.14, NumPy 2.3.5, random seed 2026092404,
and tolerance 1e-10. The maximum +I readout identity error is
4.440892098500626e-16; the nonscalar example's maximum exact-norm error
is 2.6645352591003757e-15. Source SHA-256:
`92a77489cdc0ae6b9d2e48a929f813e5e5c884e202e952a41b753d2466b9066a`.
The parent workspace independently reran the script and reproduced the
JSON byte-for-byte. Convexity extends the analytic proof to contractions;
the finite diagnostic uses reflection constructions and does not certify
that extension or a universal optimum.

No optimizer enters the committed diagnostic. Separate small exploratory
searches supplied neither a counterexample nor a general proof and are
not acceptance evidence. Unchanged numerical certificates were not rerun.
Local links, whitespace, LICENSE and the original historical audit blob
were checked. No third-party papers or private exploratory files are
committed. Publication priority and unrestricted optimality remain open.

## Jordan-block converse

The [report](audits/JORDAN_BLOCK_CONVERSE.md) is pinned to main
`012bafa1895a66e22eac676ba1702a2bde531881`. Independent internal
reconstructions checked the local spectral majorant, Bell eigenvector,
arbitrary complex memory planes, weighted Gram estimate, norm symmetry,
zero-weight cases, full trace-norm and normalized-Kraus transfer, and
four-excluded/six-remaining signature count. A separate review of the
actual draft found no proof gap. The two primary PDFs were checked at
the version and equation/page locators in the report. Internal review
does not establish external peer review or publication priority.

`tools/check_jordan_block_converse.py` records 84 weighted constructions
in `results/jordan_block_converse.json`: eight dense complex qutrit
families, four qutrit controls with scalar readouts, and sixteen dense
ququart families, four for each excluded signature pattern. Each uses
uniform, unequal, and zero-containing weight vectors. The checks cover
reflection identities, the unique possible local excess direction,
its Bell marginal, the local positive-semidefinite majorant, overlap at
most one half, the weighted projector sum, and the full Hamiltonian norm.

A separate exact negative control gives the mixed-rank projector norm
`(5+sqrt(13))/4=2.1513878188659974`, refuting the naive projector extension.
Its actual interface Hamiltonian has norm `4.739640107280844`, below the
independently proved upper bound `2+2sqrt(2)` and below the benchmark.
It is not an interface counterexample.

The run passed with Python 3.12.14, NumPy 2.3.5, random seed 2026092405,
tolerance 1e-10, and Hamiltonian dimension at most 32. Maximum Bell-marginal
error: 8.98415317816539e-15. Maximum local-majorant violation:
1.4571813044708227e-15. Maximum inter-reference projector overlap:
0.5000000000000007. Source SHA-256:
`fd1dae777b365f9f626ea5d1e5f1e8c3dbaa88e2d2007bb6671e3639a8f28c69`.
The parent workspace independently reran the script and reproduced the
JSON byte-for-byte. No optimizer or broad numerical search is used.

The proof covers all qutrit binary POVMs by convexity; the finite checks
use reflection constructions and do not prove that extension. Unchanged
certificates were not rerun. Local links, whitespace, LICENSE and the
original historical audit blob were checked. No third-party papers or
private exploratory files are committed. The general balanced quadratic
conjecture, unrestricted optimality, and publication originality remain open.

## Jordan spectral budget

The [all-block report](audits/JORDAN_SPECTRAL_BUDGET.md) is pinned to
main `780605b723919defd382d88c8adb09ed1fd8d204`. Independent internal
reconstructions checked the actual block excesses, same-site orthogonality,
cross-site Gram comparison, rank-one-update equivalence, scalar fractions,
and exact signed counterexample for every finite penalty. Actual-draft
review corrected the all-zero-excess quantifier to require positive Lambda.
The independent review is internal, not external peer review or priority
certification. Primary PDFs were read at the locators stated in the report.

`tools/check_jordan_spectral_budget.py` writes
`results/jordan_spectral_budget.json`. It checks 48 weighted constructions:
all eight ordered one/two-block patterns, each in canonical and independently
rotated complex memory coordinates, with uniform, unequal and zero-containing
weight vectors. Top Bell vectors are obtained within the known two-dimensional
blocks, avoiding arbitrary diagonalization of degenerate global eigenspaces.
The tests cover reflection identities, top eigenvalues, Bell marginals,
local spectral caps, insertion overlaps, the comparison bound, the scalar
criterion and full Hamiltonian norms, with largest dimension 32.

Two additional explicit constructions check strict improvements over the
triangle bound. One double pair with excesses `(delta/2,delta/2)` and two
maximal single pairs has comparison eigenvalue `(1+sqrt(3)/2)delta`.
Three double pairs each with `(9delta/10,delta/5)` have budget `138/145`
and comparison eigenvalue `(11+sqrt(67))delta/10`; even the coarse
total-excess certificate fails in this example. Here `delta=2-sqrt(2)`.
Four signed-projector cases at kappa=1, 2+2sqrt(2), 10 and 100 agree with
the exact formula and exceed two. Their shared actual Hamiltonian has
norm about 4.7396401073, below its analytical bound `2+2sqrt(2)`.

The run passed with Python 3.12.14, NumPy 2.3.5, random seed 2026092406,
and tolerance 1e-10. Maximum Bell-marginal error: 3.447104417482014e-15;
local-majorant violation: 1.734760030792195e-15; same-site overlap:
1.7554167342883506e-16; cross-site overlap: 0.5000000000000019.
Source SHA-256:
`2f51bada38ee8552795d4be69690347bce0231c4d7490bf44ec635fe7d72aac2`.
The parent workspace reran the final script and reproduced the JSON
byte-for-byte. A separate geometry reviewer also reran the repository
version and obtained the identical JSON. No optimizer or large simulation
enters this diagnostic.

Unchanged certificates were not rerun. Local links, whitespace, LICENSE,
and the historical audit blob were checked. No third-party source text,
papers or private exploratory files are committed. All six remaining
signature sectors, unrestricted rate optimality, and publication priority
retain their stated unresolved status.

## Single double-block converse

The [supplied report](audits/SINGLE_DOUBLE_BLOCK_CONVERSE.md) is pinned to main
`ac5863e1e026a8a9432a27385e6ee9491b423e92`. The supplied proof excludes
all three ququart signature patterns with exactly one `(22)` query pair,
including unequal angles and arbitrary relative memory orientations.
Two independent internal reconstructions checked the mixed-Choi star lemma,
the rank-one and rank-two compression bounds, the positive-spectrum cap,
resolvent comparison, weighted compression estimate, scalar conclusion,
and operational transfer. This is internal proof checking, not external
peer review or publication-priority certification.

`tools/check_single_double_block.py` writes
`results/single_double_block.json`. Its 48 constructions are the three
other-pair signatures `(11)(11)`, `(11)(12)`, and `(12)(12)`, four angle
pairs for the exceptional query, and four choices of memory coordinates:
canonical and three independently rotated dense complex families.
The angle cases include one commuting block, two maximally noncommuting
blocks, and two unequal-angle pairs. Bell vectors are constructed inside
the known two-dimensional blocks; at commuting degeneracies, an explicit
maximally entangled top vector is selected analytically.

The diagnostics check reflection identities, the local positive-spectrum
majorant, `K<=3I/2`, compression bounds `P_k K P_k<=P_k/2` and
`P K P<=3P/4`, the resolvent chord, weighted comparison, scalar criterion,
the asymmetric intermediate bound, and the actual interface Hamiltonian.
Four additional mixed-Choi constructions check the cross-Gram bound one
half and star bound three halves for random trace-preserving channels.
These use central dimensions two and three; the latter checks the broader
algebraic lemma and is not an additional hypothesis of the ququart theorem.

All 48 construction cases and four mixed-Choi cases passed with Python
3.12.14, NumPy 2.3.5, random seed 2026092407, tolerance 1e-10, and
Hamiltonian dimension at most 32. The largest positive recorded inequality
residual was 1.9966277025315366e-15; the exceptional-pair spectral-cap
residual was 1.7636814329896129e-15. Source SHA-256:
`bee740469ad919af6d908a2df765b9275647b08852d1e9b55e3f8347f690e3ad`.
The repository script was rerun into a separate scratch output, reproducing
the recorded JSON byte-for-byte. Cross-platform floating-point
outputs need only satisfy the stated tolerance.

No optimizer or large simulation enters this diagnostic, and unchanged
certificates were not rerun. Finite construction checks supplement the
symbolic proof; they do not establish a universal bound or originality.
Three signature sectors, unrestricted equal-accuracy optimality, and
publication novelty remain unresolved.

## Commuting query algebras

The [supplied report](audits/COMMUTING_QUERY_ALGEBRAS.md) is pinned to main
`a383214b357ccbd83a62ae0c94660083cb8b090e`. The all-size theorem bounds
`norm(H)<=2q+sqrt(2)` at `n=q+1` when q original query pairs act on
separate memory-qubit factors and the final pair is arbitrary. At q=2,
the finite-dimensional algebra classification and the prior one-double
converse imply that any two cross-commuting original query algebras suffice.
These are explicit decoder hypotheses, not an unrestricted optimality proof.
An independent internal reconstruction checked the spectral gap, product-Bell
compression, normalized Jordan-block counts, scalar inequalities, endpoint
and contraction extensions, algebra classification, and uniform operational
transfer. Internal review does not certify originality or external acceptance.

`tools/check_commuting_query_algebras.py` writes
`results/commuting_query_algebras.json`. The diagnostic performs 140
factor constructions for q=1,2,3, with Hamiltonian dimension at most 128.
The first q pairs include commuting endpoints, maximally noncommuting
angles, different angles between sites, and an angle of 1e-4 near a
commuting endpoint. Each construction uses canonical coordinates or a
common dense complex memory rotation defining the dedicated factors;
the last pair has an independently chosen complex memory orientation.
The last-pair families include scalar and commuting reflections,
one active block with different scalar complements, and multiple active
blocks with unequal angles. Scalar final readouts with maximal first-pair
angles check exact attainment of `2q+sqrt(2)`.

The construction checks cover reflection identities, cross-commutators,
the product-Bell isometry and marginal, the dedicated-query spectral cap,
the partial-trace resolvent identity, its Jordan-block bound, the two
scalar inequalities, the positive-rank-update criterion, and the actual
Hamiltonian norm. The resolvent identity uses relative operator error,
normalized by the larger of one and the compressed-resolvent norm;
this avoids treating its large norm near a commuting endpoint as an
absolute-error requirement. All inequality residuals are absolute.
Four additional ququart constructions cover the separate two-dimensional
summand case of the algebra classification and the direct triangle case
with an internally commuting query pair. The exact cap obstruction is
also checked: the two-Bell-pair Rayleigh value is
`4+(2-sqrt(2))/8 = 4.0732233047033635`, already above four.

All construction checks passed with Python 3.12.14, NumPy 2.3.5, random
seed 2026092408, and tolerance 1e-9. The largest positive recorded residual
was 1.921629522172452e-12; maximum relative resolvent-identity error was
1.4932836252197592e-12; maximum spectral-cap residual was
1.8021548755309465e-14. The largest actual benchmark excess was
5.329070518200751e-15. Source SHA-256:
`badb5e00a55f0b6e334d32a4634d4de6d8e18822569b0fc911cf7f04692be05d`.
The final repository script was rerun into a separate scratch output and
reproduced the recorded JSON byte-for-byte. Cross-platform outputs need
only satisfy the stated tolerances.

No optimizer, large simulation, or source-distribution restriction enters
these checks. They supplement the symbolic proof and do not establish the
all-size bound on their own. The three remaining ququart signatures,
unrestricted equal-accuracy optimality, and publication originality remain
unresolved. Unchanged diagnostics were not rerun.

## Noncommuting query families

The [report](audits/NONCOMMUTING_QUERY_FAMILIES.md) is pinned to main
`e8fffa3ccac4b03b354d354101e20302fc934616`. Independent internal
reconstruction checked both proofs, including the complete exceptional
representations and all endpoint cases. This is not external review.

Run the two new checks:

```bash
python tools/check_partial_swap_basis.py --output results/partial_swap_basis.json
python tools/check_noncommuting_families.py --output results/noncommuting_families.json
```

The first uses exact rational combinations of square roots, with only
the Python standard library. It constructs the nine highest-weight
vectors in the computational basis; checks their spin, orthonormality,
memory-SWAP signs and invariant-subspace actions; verifies all 27
off-diagonal coefficients and 23 diagonal-sum coefficients; and checks
the zero symmetric block. This makes the finite coefficient calculation
reproducible. The continuous-angle Schur-complement positivity remains
the supplied analytic proof.

The second independently builds physical matrices of dimension at most
32 from Pauli matrices. Twelve two-angle query constructions include
seven simple and five degenerate top eigenvalues, signed angles, and
complex memory rotations. It checks the Cartesian spectrum, explicit
maximally entangled top vector, full spectral cap, two mixed cross
commutators, and both permitted nonzero same-axis commutators.
There are 108 third-reflection cases, 63 full resolvent evaluations,
and 12 attenuated/general-contraction cases. All 16 exceptional joint
sign patterns are checked, with 144 third-reflection constructions.

Twelve partial-SWAP angle triples check the two reduced spin matrices
against the complete physical operator, including its full spectrum,
the Schur determinant and the sharp projector bound. Forty-eight
associated physical Hamiltonians use unequal angles between sites
while keeping equal spectra within each site's two Jordan blocks.
Thirty scalar constructions check the polynomial identities at
interior points and endpoints. Projector attainment at 5/2 and physical
attainment of 4+sqrt(2) in the two-cross-commutator family are separate
checks; no attainment in the partial-SWAP physical subclass is asserted.

Both scripts passed with Python 3.12.14; the matrix check used NumPy
2.3.5, seed 2026092409 and tolerance 2e-9. Its maximum positive
residual was 7.105427357601002e-15. The exact verifier has no numerical
tolerance. Source SHA-256 values:

- `check_partial_swap_basis.py`:
  `ac9fa40a027b2a95077960c972df34e7d8fca8d629b2f0512059a948ceefab60`.
- `check_noncommuting_families.py`:
  `5865167f54a948754a2d89f00ebed82aec51eba75580149c52014278f39d2c1a`.

The final repository scripts were rerun into separate scratch outputs
and reproduced the recorded JSON byte-for-byte. These finite checks
and exact coefficient calculations do not prove arbitrary-U(4)
geometry, a complete remaining signature, unrestricted optimality,
or originality. No optimizer or large simulation was used.
