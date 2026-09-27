# Core evidence map

Base: `357a4dfd523e0b895dbeead46fb1e3190c7afd78`. Prepared 27 September 2026. Paths below are relative to the repository root.

This is a dependency and readiness inventory. Sources and existing JSON records were read and SHA-256 hashes checked at the pinned base; no frozen checker was imported or executed for this map. Existing “independent” review means internal reconstruction, not external peer review. No publication-originality conclusion is made. The [scientific scope](SCIENTIFIC_SCOPE.md) governs the completion gates. Overview documents may change after this base; all fingerprints below refer to the base version, not automatically to a later working copy.

## 1. Coherent core and minimal dependencies

Use three operational conclusions: (i) the exact all-n one-qubit allocation region, with the common-accuracy formula as a corollary; (ii) exact common-accuracy tradeoff for every integer 0<=q<=n<=4; (iii) one explicit unequal-accuracy collective protocol outside the precisely defined original-site-retention class. These are compatible claims, not a claim that retention is globally optimal for all accuracy profiles.

The finite-block formula is Gamma(n,2^q)=2q+sqrt(2)(n-q), or eta_max=[q+(n-q)/sqrt(2)]/n. Its proof coverage is q=0 and q=n (elementary/prior endpoints), q=1 (all n), (n,q)=(3,2),(4,3) (half rank), and (4,2) (quarter rank). This covers integer-qubit budgets, not arbitrary non-power-of-two output dimensions.

Proof spine: model and twirl -> unrestricted normalized seed -> shared fidelity–affinity lemma -> half/quarter-rank converses. The q=1 theorem instead uses extreme qubit decoders and independently optimized common-qubit CHSH monogamy. Unequal separation uses the complete translation instrument and the original-site-retention support inequality; it needs no large-n graph optimality theorem or asymptotic profile result.

| Role | Proof source / needed part | SHA-256 |
|---|---|---|
| Model/endpoints | `RESEARCH_NOTE.md` — Sections 2–4: uniform error, classical endpoint, retention construction. | `be10de868c505ae2edcb100280aa9a39d206097b7d2d82eba3318e2fedc76fa4` |
| Seed reduction | `docs/COLLECTIVE_ENCODING_REDUCTION.md` — Sections 1–3: unrestricted Kraus converse and finite orbit completion. | `dce313c21d9942ee4d72183cc319aac440adc71eb1a31c066a925e6ccfe908c4` |
| q=1 prior application | `docs/ONE_QUBIT_OPTIMALITY.md` — Precise Cheng–Hall scope; scalar all-n theorem. | `2a34ee4050bd3591f73411e99a28f94e1f76be4c1881234f1d9189e88fd3291f` |
| q=1 full region | `docs/ONE_QUBIT_ALLOCATION_REGION.md` — Weighted converse and exact region sum_i w(x_i,z_i)<=1; implies scalar theorem. | `9a973e4d89a8dc6177ee71dc10daf911a8fd8d534e6451363ed2b67b885d03b9` |
| Shared prior lemma | `docs/STRONG_ENTROPIC_CONVERSE.md` — Only Section 3 fidelity–affinity comparison is needed; remaining entropy results are not dependencies. | `e822f1bd67a9d3e2cd5cdd6f2e5e418e1a0e96b4f41d360e51c8e7d0fd3f6e6f` |
| Half rank | `docs/audits/HALF_RANK_RETENTION_CONVERSE.md` — Unrestricted rank 2^(n-1), n=2,3,4; exact value and seed equality. | `69b5c179242fceed9f7af194a5884b3215ad6b01c38a20bb1f028ee540e694f5` |
| Quarter geometry | `docs/audits/QUARTER_RANK_GEOMETRY.md` — Top-quarter spectrum and local block inequalities used by the next proof. | `e923369b35807ff8dc89250d61ffd453c1fd4adb46b7176bab541b4c065a59cd` |
| n=4,q=2 | `docs/audits/NONFLAT_QUARTER_RANK_CONVERSE.md` — All rank<=4 spectra; exact scalar certificate and analytical reduction; seed equality. | `c761cb2e9835a59b0aa40ef5b27658724af6bd772cddf1cba8adcb43cf0e63a2` |
| Unequal separation | `docs/EXACT_AXIS_SPECTRAL_REDUCTION.md` — Sections 2–3 suffice: complete translation instrument, full defined retention-class region, n=31,q=5 separation. Full graph converse and Section 4 graph-optimality corollary are optional. | `bfeb82fcbbb99d268a62e7ff69d5b6f8f0431629bce7fef5e594815340640df3` |

For a self-contained paper, reproduce the short shared fidelity–affinity proof instead of routing readers through the entropy program. The full q=1 allocation note already supplies the scalar theorem; the earlier q=1 note remains necessary source provenance, not a second theorem to prove. The n=31 star example only needs its explicit probabilities and translation identities, not enumeration of 2^31 input basis vectors or Kraus branches.

## 2. Minimal existing computation manifest

Only the exact quarter-rank scalar certificate is computationally essential to the currently supplied finite-block proof route. The other scripts corroborate fixed identities/constructions and scalar comparisons; their pass records do not prove universal optimality. All paths and hashes below are current file bytes at the pinned base.

| Role | Checker / current SHA-256 | Existing report / current SHA-256 | Existing evidence and scope |
|---|---|---|---|
| Seed completion | `tools/check_seed_twirl.py`<br>`f02c51cae96c5a6e8e77a05cbeac4c56d5151d2c21347767c3b1c493fabe52b4` | `results/seed_twirl.json`<br>`4cf94b4d1b1b266c3e31e457fd9bb8003edecd9bb68d6e0aeebaa34a1844afcf` | Existing PASS record; finite instrument identities. No embedded source/proof hashes. |
| q=1 scalar | `tools/check_one_qubit_tradeoff.py`<br>`77f2e2ca45a7703bb7f042d8f16027cdf4b6382181d44fc76bbc16d48f52edbf` | `results/one_qubit_tradeoff.json`<br>`c0592e4452b47fde83ad332a1fffa479557d836a0002408d846229ff9ee2e8a3` | Existing PASS record; attaining seeds and decoder identities, not a monogamy proof. No embedded source/proof hashes. |
| q=1 full region | `tools/check_allocation_and_kernels.py`<br>`1ee642d0a11b1347ae9af0015b0f3597d6781feeee9aa5b75a3578f0bd10cdb3` | `results/allocation_and_kernels.json`<br>`22eb5a017f6e8692565dd2894e5977e8d5037db541b9ef1f804d3d4be5e70359` | Existing PASS; 14 cases, max dimension 8. Includes complete weighted allocation instrument, plus unrelated older cases. No embedded source/proof hashes. |
| Half rank | `tools/check_half_rank_retention.py`<br>`c9d45e281d393cb6b4387b068de571f4440a96e17344312d49904eaecd9ff6e6` | `results/half_rank_retention.json`<br>`ba59605fe8cf0ebeb1b555702c1f3cb050674cab2e85134d7230de84d32b67d7` | Existing exact-comparison/fixed-construction pass; 13 constructions, n=2,3,4. Embedded source/proof hashes match current bytes. |
| Quarter geometry | `tools/check_quarter_rank_geometry.py`<br>`8901e2b6d5a8730704a9d1a06402fee238491aeca69d83f091b261027df1d26f` | `results/quarter_rank_geometry.json`<br>`71dbe369baec49b015c10fbd872ff78d36aca95d55a759ab2741259df78aef29` | Existing exact-comparison/fixed-construction pass, max dimension 16. Embedded source/proof hashes match current bytes. |
| Essential exact certificate | `tools/check_nonflat_quarter_rank_certificate.py`<br>`10cdb4c62ed2d0b8418abd189484c6d57cd06bd45443c2bd92b4523036d90ec9` | `results/nonflat_quarter_rank_certificate.json`<br>`d9ddb1376188246bca676e0fc45b1ad8c4810a67b3c6ff2db1065d591880b639` | Existing exact rational pass. 35 C coefficients >4/25 and 99 P coefficients >1/10000 on [0,9/25]^2, no subdivision. Embedded hashes match current bytes. |
| Quarter matrix diagnostics | `tools/check_nonflat_quarter_rank.py`<br>`c028be07b5278d145d3a000e07ee6bedd093fa0c6882fbc16a3a1942c201aaa6` | `results/nonflat_quarter_rank.json`<br>`0533454680f9536fc03a3e2cfb40eeb19fb87065221429677e62b1a6cb64b683` | Existing exact-comparison/fixed-construction pass, max dimension 16. Embedded source/proof hashes match current bytes. |
| Unequal separation | `tools/check_entropy_geometry.py`<br>`494da25b678326af60977d305ae615056690df4d2304d0d89019540770aa19f4` | `results/entropy_geometry.json`<br>`6adaeb809fa9a1eec83bf2c96eed21e6dd118c5d9683f5e8187521bdd8b07210` | Existing PASS; 13 cases, max dimension 32. First three cases check two complete n=3 translation instruments and the n=31 star support/interior separation. Remaining cases are unrelated. No embedded source/proof hashes. |

The exact certificate is stdlib Fraction/isqrt arithmetic. It proves its two explicit scalar positivity statements; the analytical reductions, sign conditions, branch coverage, and equality argument remain indispensable. The older twirl, q=1, allocation and entropy-geometry reports predate embedded source/proof fingerprints. A new manifest can pin them externally without modifying those historical reports. Floating reports used NumPy 2.3.5; the twirl record used Python 3.13.5 and the other listed floating records Python 3.12.14. Do not promise byte identity across runtimes.

## 3. Structural companion and supporting stability

Balanced spectra at every n are selected as a structural companion; quantitative stability and the nonflat neighborhood are supporting results. Neither is needed to close any case in the core finite-block theorem. They add an independent scalar proof chain, which should remain separate in the integrated exposition.

| Proof | Proof SHA-256 | Checker SHA-256 | Report SHA-256 |
|---|---|---|---|
| `docs/audits/BALANCED_SPECTRUM_OPTIMALITY.md` | `4c3da955567c0478e3300900ea680cffb18d32f9c7d79f8137ad89906d36f8f8` | `tools/check_balanced_spectrum_optimality.py`<br>`9f095c451c27cb8696b8b13ae4dff2725389ca3b146ffc08be124c03dee686b6` | `results/balanced_spectrum_optimality.json`<br>`9ba5b06663a200dfa732eab427a0641dd027d5643b683370d3f74a072ec6c6ec` |
| `docs/audits/BALANCED_SPECTRUM_STABILITY.md` | `02474352d858fb80ed291e3b751f4d0f077a559cf806e391dbed2e35d7e561ff` | `tools/check_balanced_spectrum_stability.py`<br>`d1c2641f99d0e8222a042ed11d5f0002c37f1006f81b391c562580741ba3bad9` | `results/balanced_spectrum_stability.json`<br>`ec8ce50a987662920cea160ae327891190b77ba0fed094a35c04a7a0541a3664` |

These reports record existing exact-comparison/fixed-construction passes, with source/proof fingerprints matching the current files. Their frozen internal review and one independent reproduction were completed in the preceding rounds. No new run was performed for this map.

## 4. Already verified gates versus bounded remaining gates

Already supplied and internally checked: arbitrary-input uniform-error/contrast conversion; Kraus normalization and complete finite twirl; q=1 CHSH source qualifications (independent memory settings and mixed marginals); half-rank branch coverage and equality; quarter-rank analytical reduction plus exact certificate; complete translation-instrument normalization; strict star-versus-retention separation. The n=31 numerical diagnostic checks its 32-vertex support and scalars, not a full 31-qubit instrument. The analytical note supplies the latter operator identities.

The [completion gates](SCIENTIFIC_SCOPE.md#5-bounded-completion-gates) now
require one integrated exposition and its review, source reconciliation,
and a final evidence freeze. That review must preserve the model and
normalizations, rank-deficient and zero-branch cases, all integer budget
endpoints, analytical-to-polynomial substitutions, seed equality scope,
and the asymmetric comparison class. It does not require another review
of every historical research branch.

A separate internal reread at this checkpoint checked the full asymmetric
instrument, its effective effects and retention-class bound, and the
exhaustive finite-budget assembly. This was an analytical review, not a
new checker run or review of a not-yet-written manuscript.

Not blockers: the general all-n intermediate-memory conjecture; sharp
entropy/rate closure; arbitrary non-power-of-two dimensions; optimizing
the n=31 collective example; or stronger stability constants.

## 5. Reproduction after the exposition freezes

This map is the minimal manifest now. Verify its fingerprints against the
pinned commit before using a later checkout. Preserve historical reports.
For the final evidence freeze, plan one scoped reproduction of the
essential exact certificate into a temporary output file:

```bash
python tools/check_nonflat_quarter_rank_certificate.py --output /tmp/qic-nonflat-quarter-rank-certificate.json
```

Compare exact rational conclusions and the embedded source fingerprints.
The analytical reduction still needs review. Other fixed-construction
checks are useful when an edit changes a relevant identity or a concrete
discrepancy appears; there is no need to rerun the full research archive.
Floating-point report bytes need not be identical across runtimes.

The allocation and entropy-geometry scripts also contain unrelated older
cases. Keep their relevant fixture descriptions in this map; splitting
those scripts or building a new test framework is not a completion gate.

## 6. Reference-only history to retain

Preserve earlier decoder/Jordan/resolvent/SLD searches; finite two-mode and spectrum classifications; asymptotic entropy/profile-rate and optimizer certificates; steering/channel/resource comparisons; spectral-layer bounds; and affinity-method obstruction notes. They supply context or limitations but are not dependencies of the three selected conclusions. The full exact-axis optimization theorem and graph-rate corollaries are optional context for the elementary star example. Do not delete notes, reports or research branches to simplify the paper.

Keep the commit-pinned `docs/audits/PROOF_AND_NOVELTY_AUDIT.md` and `docs/audits/PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md` unchanged as historical sources. They predate the later finite-block proofs; neither is a current approval or rejection of novelty for those later theorems. `docs/CORE_ARGUMENT.md` is a useful synthesis, not the sole proof source; its synthesis header and the final evidence freeze should always identify the research base being reviewed.
