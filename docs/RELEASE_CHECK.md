# Release sanity check

Checked 27 September 2026 against main
`400490aad505948f1bd62969fc6ddeb246706f4e`.
This is an internal release check of the selected scientific package and
repository presentation. It is not external peer review, a new proof of
every archived result, or an exhaustive publication-priority search.

## Scientific and reproducibility findings

The overview, teaching pages, integrated argument, scope and cited proof
dependencies agree on the model, the 14 finite budgets, the complete
one-qubit allocation region and the defined unequal-accuracy separation.
The balanced-spectrum and stability results remain separate companions.
No scientific release blocker was identified in this bounded pass.

All 36 scientific-freeze fingerprints and all 31 earlier evidence-map
fingerprints match their declared commits. At the release baseline, all
47 source/proof fingerprints embedded in historical reports match their
referenced files. All 49 computational Python files parse; the separate
tutorial plotting helper was inspected. All 48 historical JSON reports
parse. The MIT license and copyright are unchanged.

The following baseline commands ran once each under CPython 3.12.14, with fresh
outputs outside the repository. Matrix diagnostics used NumPy 2.3.5.

| Checker in `tools/` | Outcome | Comparison with historical report |
|---|---|---|
| `check_nonflat_quarter_rank_certificate.py` | PASS, exact arithmetic, 0.102 seconds | All 4,267 bytes identical |
| `check_seed_twirl.py` | PASS | Only Python-version metadata differs: 3.13.5 to 3.12.14 |
| `check_one_qubit_tradeoff.py` | PASS | Identical |
| `check_allocation_and_kernels.py` | PASS | Identical |
| `check_half_rank_retention.py` | PASS | Identical |
| `check_quarter_rank_geometry.py` | PASS | Identical |
| `check_nonflat_quarter_rank.py` | PASS | Identical |
| `check_entropy_geometry.py` | PASS | Identical |
| `check_balanced_spectrum_optimality.py` | PASS | Identical |
| `check_balanced_spectrum_stability.py` | PASS | Identical |

The nine diagnostics took 1.216 seconds in total. Their largest matrices
have dimension 32. The 31-input example uses its 32-vertex support, not a
full 31-qubit matrix. The twirl and one-qubit suites include fixed-seed
pseudorandom fixtures; the other checks use prescribed constructions.
No optimizer or large simulation ran. No diagnostic pass certifies a
universal theorem. The exact certificate's report hash is
`d9ddb1376188246bca676e0fc45b1ad8c4810a67b3c6ff2db1065d591880b639`;
its two polynomial inequalities remain conditional on the supplied
analytical reduction, branch coverage and equality argument.

## Presentation repairs and surgical reductions

The baseline contains 204 tracked files and 101 Markdown documents. All
101 documents are reachable from the README. Its 852 local link occurrences,
including 76 heading anchors, resolve. The external-link inventory was not
a claim to revalidate every remote article or its current availability.
No byte-identical duplicate files were found.

Six Markdown table rows truncated mathematical or explanatory content
because literal pipes were read as column separators. The affected rows
in the research note, status ledger, focused prior comparison and three
entropy notes now preserve their intended cells. In particular, the Jones
comparison again displays the full scope distinction.

The formatting pass converts 476 legacy display delimiters and 134 inline
delimiter pairs in 24 documents to GitHub-native math, and joins one
multiline inline expression. One absolute value is written with equivalent
`\lvert` and `\rvert` commands to protect its table cell.

Live GitHub inspection then exposed rejected operator-name macros and
numbered equations collapsing into narrow columns. The second pass
replaces 410 operator-name macros with the same names in roman type and
1,089 equation tags with the same visible parenthesized labels. No
automatic label references are used in these documents. The replacement
preserves every equation identifier and named operation; it changes
typesetting, not inequalities. The repaired research-note model and
numbered error equation were visually checked on GitHub, and the Jones
comparison's full table cells were checked in the rendered page.

After the repairs, all 856 local links and 78 heading anchors resolve.
The Markdown parser retains all 670 data rows across 77 tables, with
consistent column counts. This combines repository-wide static checks
with representative live rendering, not a pixel-by-pixel review of every
page or device.

The reductions remove a duplicate archive link, a repeated index
introduction, a repeated finite-case status summary and obsolete workflow
authorization prose. The remaining open problem is labeled future work.
The overview and current scope explicitly place manuscript writing on hold
and provide the collaboration contact. Repeated worked examples across
the overview, tutorial and proof bridge serve different reading stages;
the proof appendices and historical reports remain available.

The [current reproduction instructions](REPRODUCIBILITY.md#reproduce-without-changing-the-recorded-evidence)
keep assertions enabled and place fresh outputs outside the recorded
evidence. Historical commands remain part of their original run records.

## Version and evidence boundary

The [formatting and release map](../results/release_sanity_map.json) gives
before/after SHA-256 fingerprints and change categories. Mechanical
math/table repairs were checked by reversing the recorded transformations
and by a separate comparison of their mathematical content. Other edits change navigation,
reproduction guidance or manuscript status.

The scientific freeze remains pinned to
`466bbb770d150fb8f43c4f9eca04bbadabe85188`. Neither its manifest nor any
historical JSON report is rewritten. Every checker source remains
unchanged. Display repairs also affect the integrated core and proof
appendices. Their historical hashes identify the exact text reviewed at
the recorded base; the release map connects that text to the displayed
revision without changing its mathematical content. Rerunning a checker
on this checkout can change embedded proof-hash metadata without changing
its numerical results. The reproduction guide supplies an exact-version
archive command when byte-identical historical evidence is wanted.

Specifically, 19 embedded proof-hash entries covering 18 proof notes now
identify the earlier presentation bytes; the other 28 embedded
fingerprints still match the current files. All 36 manifest fingerprints
remain valid at their frozen commit. Of those, 22 also match the current
checkout and 14 differ, including three pre-existing overview revisions.

The general common-accuracy optimum, sharp entropy inequality, asymptotic
rate and exhaustive originality assessment remain outside this release
check. They are not silently promoted to completed results.
