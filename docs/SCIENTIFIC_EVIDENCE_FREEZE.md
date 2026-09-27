# Scientific evidence freeze

Prepared 27 September 2026. The selected scientific package is prepared
for manuscript drafting. This closes G4 of the
[scientific scope](SCIENTIFIC_SCOPE.md#5-bounded-completion-gates).
Theorems, assumptions and source boundaries are unchanged.

## 1. Frozen scientific base

The [machine-readable manifest](../results/scientific_evidence_freeze.json)
pins the scientific inputs to commit
`466bbb770d150fb8f43c4f9eca04bbadabe85188` (the merge of PR #59), tree
`8f6b04d5d5676d92183d33f0c4102370ec3d0da6`.
Every entry in its `files` array refers to that commit's bytes. The
manifest and this freeze note are subsequent records, not files in the
frozen base. Later overview edits report completion without changing
those pinned versions. At the base, overview documents still describe
G4 as pending; this note records its subsequent completion.

The manifest contains 36 file fingerprints: the 31 proof/checker/report
entries in the earlier evidence map, plus the integrated core, its
exact-text review, focused source comparison, scope and evidence map.
The license is pinned separately and preserved.

The integrated `CORE_ARGUMENT.md` has SHA-256
`15009f875db417d7926491376312cba8c0ac6cb56b68efcd29483c7eb9e12f45`,
matching the [integration review](audits/INTEGRATED_CORE_REVIEW.md).
That review covers the operational and analytical connections; the
manifest does not replace it or the underlying proof appendices.

## 2. Reconciliation with the earlier map

All 31 older fingerprints were verified against their declared base
`357a4dfd523e0b895dbeead46fb1e3190c7afd78`. Thirty files have identical
bytes at the new frozen base. The only changed entry is
`RESEARCH_NOTE.md`: its version and integrated-exposition overview were
updated. Its model and endpoint Sections 2–4 are byte-identical, with
SHA-256 `2b0caabc4d413151742f7336f29b8305c87d8d728b1f58af97203941449c429f`
for the text from the Section 2 heading to immediately before Section 5.
Both old and new whole-file hashes appear in the manifest. The old map's
fingerprints remain intact and are not silently reassigned to a later
checkout.

## 3. Essential certificate reproduced once

The exact quarter-rank checker was executed once at the clean frozen
base, using CPython 3.12.14 and the standard library only. It exited
successfully on 27 September 2026 at 10:19:20 UTC. The output was written
outside the repository and compared with the historical report.

| Certificate | Bidegree | Bernstein coefficients | Strict lower bound |
|---|---|---|---|
| C | (6,4) | 35 | 4/25 |
| P | (10,8) | 99 | 1/10000 |

Both conclusions hold on the single rectangle `[0,9/25]^2`, with no
subdivision. All decisions use exact rational intervals and integer
squaring for radical enclosures. The reproduced 4,267-byte JSON was
byte-identical and semantically identical to the historical report,
with SHA-256
`d9ddb1376188246bca676e0fc45b1ad8c4810a67b3c6ff2db1065d591880b639`.
The proof, checker and historical-report fingerprints, commit and clean
repository state were unchanged before and after execution. The
manifest records runtime, timestamps, exact conclusions and comparisons.
No other research checker was run for this freeze, and no historical
report was overwritten.

To reproduce the same certificate at the pinned base:

```bash
python tools/check_nonflat_quarter_rank_certificate.py --output /tmp/qic-nonflat-quarter-rank-certificate.json
```

The computation certifies two scalar positivity statements. The
[analytical proof](audits/NONFLAT_QUARTER_RANK_CONVERSE.md) and its
integration review supply the reduction, sign conditions, branch
coverage and equality argument. The remaining pinned computational
records are historical diagnostics or fixed-construction checks; their
pass records do not establish universal optimality.

## 4. Claims carried into drafting

| Role | Selected result | Boundary |
|---|---|---|
| Main finite theorem | `Gamma(n,2^q)=2q+sqrt(2)(n-q)` for all integer `1<=n<=4`, `0<=q<=n` | Fourteen budgets; arbitrary collective encoders and spectra. Equality classifications concern normalized seeds |
| Full one-qubit allocation | Exact all-n region `sum_i w(x_i,z_i)<=1` | Derived application of established independently optimized CHSH monogamy; the framework and ingredient are credited |
| Unequal-accuracy separation | Complete `n=31,q=5` instrument, all `x_i=1`, all `z_i=1/sqrt(31)` | Strictly beyond the defined original-site-retention class admitting a factorizing Kraus refinement, including joint measurements of discarded sites |
| Structural companion | Exact balanced-spectrum optimum and flat half-rank equality at every n | A fixed spectral family; not a general nonflat rank converse |
| Supporting result | Quantitative stability and the explicit sufficient nonflat half-rank neighborhood | Conservative sufficient constants; no optimality claim for them |

All review described here is internal reconstruction and consistency
checking. The [focused prior comparison](CORE_PRIOR_COMPARISON.md)
remains a bounded comparison with primary sources, not exhaustive
publication-priority certification. The freeze does not preapprove a
manuscript that has not yet been written.

The unrestricted all-n common-accuracy converse, sharp general entropy
inequality and asymptotic rate remain open; the smallest remaining
finite case is `(n,q)=(5,2)`. Unrestricted optimality and implementation
efficiency of the 31-input example are not asserted. These are future
work, not completion gates for the selected package. Drafting should
preserve the reviewed assumptions, source attribution and exact scope.
