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

## Historical archive provenance

The user-provided archive was Q1_Quantum_Interface_Dossier_v0_1.zip.
Its SHA-256 is
`3f3538c0307f3a1131746d84410b21752b97aa0e87d8de1722392d3b114dd8ec`.
The following three files were imported unchanged at bootstrap commit
`eaf085a8cb299e6b297b11d2dc3c85e24f02779e`. These are historical hashes; the
research note has subsequently been revised to version 0.7:

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
