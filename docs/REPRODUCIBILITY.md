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
thesis was available only at metadata/abstract level; its unread full text
remains an explicit source gap.

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
remain full-text gaps; no absence-of-prior-art conclusion is certified.
No large simulation or new solver output underlies the results, and the
unchanged repository diagnostics were not rerun. Local links, whitespace,
and the identities of LICENSE and the historical audit were checked.

## Original archive provenance

The user-provided archive was Q1_Quantum_Interface_Dossier_v0_1.zip.
Its SHA-256 is
`3f3538c0307f3a1131746d84410b21752b97aa0e87d8de1722392d3b114dd8ec`.
The following three files were imported unchanged at bootstrap commit
`eaf085a8cb299e6b297b11d2dc3c85e24f02779e`. These are historical hashes; the
research note has subsequently been revised to version 0.17:

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
