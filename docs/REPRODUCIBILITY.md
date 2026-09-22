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

## Provenance

The user-provided archive was Q1_Quantum_Interface_Dossier_v0_1.zip.
Its SHA-256 is
`3f3538c0307f3a1131746d84410b21752b97aa0e87d8de1722392d3b114dd8ec`.
The following three files were imported unchanged at bootstrap commit
`eaf085a8cb299e6b297b11d2dc3c85e24f02779e`. These are historical hashes; the
research note has subsequently been revised to version 0.2:

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
