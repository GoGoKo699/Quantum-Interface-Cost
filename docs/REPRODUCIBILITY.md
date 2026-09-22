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

No hosted CI run, independent proof audit, solver optimality certificate,
large-register simulation, or hardware experiment is claimed.

## Commands

From the repository root, with Python 3.10 or later:

```bash
python -m pip install -r requirements.txt
python checks.py --max-n 4 --output results/baseline-rerun.json
python tools/check_seed_twirl.py --output results/seed-rerun.json
```

For exact environment replay, use Python 3.13.5 and NumPy 2.3.5. The broader
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

## Provenance

The user-provided archive was Q1_Quantum_Interface_Dossier_v0_1.zip.
Its SHA-256 is
`3f3538c0307f3a1131746d84410b21752b97aa0e87d8de1722392d3b114dd8ec`.
The following three files are imported unchanged:

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
