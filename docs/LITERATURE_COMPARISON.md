# Literature comparison and remaining novelty questions

Updated: 2026-09-22. The [commit-pinned audit](audits/PROOF_AND_NOVELTY_AUDIT.md)
contains exact source versions, theorem/equation/page locators, resource maps,
proof reconstructions, and counterexamples for the bootstrap dossier. The
table below summarizes those completed targeted comparisons and adds the
primary theorem used in the subsequent one-qubit result. It is not an
exhaustive certification of publication novelty.

## Direct precedents and exact implications

| Primary source | Checked locator and relationship | Consequence |
|---|---|---|
| Ballester–Wehner–Winter, *State discrimination with post-measurement information*, [quant-ph/0608014v2](https://arxiv.org/abs/quant-ph/0608014v2) | Section 5, Lemma 5.1, p. 20; Eq. (11), p. 21. Use the uniformly weighted ensemble `(I+sP_j)/2^n`; symmetry gives `eta=2 p_success-1`. | Direct prior task with an exactly equivalent finite-error optimization for this ensemble. The full local-Pauli algebra makes exact q=n a corollary. Its inspected evaluated cases do not solve intermediate memory. |
| Ioannou et al., *Simulability of high-dimensional quantum measurements*, [2202.12980](https://arxiv.org/abs/2202.12980), PRL 129, 190401 | Published Eq. (1), p. 2, matches our model. Result 1, Eq. (6), treats full-outcome MUBs. | The framework is established. Coarse-graining gives an achievable local protocol, but does not transfer a full-outcome converse. |
| Jones et al., *Equivalence between simulability of high-dimensional measurements and high-dimensional steering*, [2207.04080](https://arxiv.org/abs/2207.04080), PRA 107, 052425 | Theorems 1–2, Eqs. (5)–(11), p. 4; Appendix A Lemma 1; Section VI Eqs. (20)–(21). | Steering/Schmidt-number equivalence is established. Its full-outcome two-MUB bound cannot bound our separate binary queries: the `(2,1)` subset protocol exceeds that visibility. |
| Bluhm–Rauber–Wolf, *Quantum compression relative to a set of measurements*, [1708.04898v4](https://arxiv.org/abs/1708.04898v4) | Definition 4.1, pp. 5–6; Theorem 6.1, p. 9; Section 9.1, p. 26. | Common reconstruction is an extra constraint, explicitly distinguished in the source. At `(1,0)` it allows equal X/Z contrast at most 1/2, versus 1/sqrt(2) here. |
| Devetak–Berger, *Quantum Rate-Distortion Theory for I.I.D. Sources*, [quant-ph/0011085v3](https://arxiv.org/abs/quant-ph/0011085v3) | Eqs. (12)–(14), p. 4; Theorem 2, pp. 10–11; Theorem 3, p. 13. | An actual fixed-cap reconstruction code at marginal entanglement distortion delta can be twirled to uniform arbitrary-input contrast `1-4 delta/3`. This is an achievability bridge; reverse identification fails. |
| Cheng–Hall, *Anisotropic invariance and the distribution of quantum correlations*, [1610.09302v3](https://arxiv.org/abs/1610.09302v3), PRL 118, 010401 | Eq. (1), p. 1; Eqs. (13)–(14) and mixed-state extension, p. 3. CHSH monogamy permits independent settings on the common qubit. | Supplies the key known theorem for our deduction `Gamma(n,2)=2+sqrt(2)(n-1)` and its equality analysis. This is an application, not a new monogamy result. |

The last source's [publisher's note](https://doi.org/10.1103/PhysRevLett.118.059901)
changes its description of invariants, not the monogamy theorem used here.
The [one-qubit proof](ONE_QUBIT_OPTIMALITY.md) states all source assumptions
and the exact CHSH operator substitution. The common-memory qubit and mixed
three-qubit marginal hypotheses are essential. The older same-setting form
alone does not justify independently chosen site decoders.

## Established proof ingredients

- Berta et al., [0909.0950](https://arxiv.org/abs/0909.0950), Eq. (2): quantum-memory uncertainty, combined here with Fano and conditional-entropy subadditivity.
- Brandao–Christandl–Yard, [1010.1750v5](https://arxiv.org/abs/1010.1750v5), Corollary 1 / Eq. (12), with the [erratum](https://doi.org/10.1007/s00220-012-1584-y): squared distance in the corrected one-way-LOCC norm, coefficient `1/(16 ln 2)`.
- Christandl–Winter, [quant-ph/0308088](https://arxiv.org/abs/quant-ph/0308088), and Koashi–Winter as cited in audit Section 7: squashed-entanglement definition, properties and monogamy. The copied classical flag keeps its dimension bound at log(dim Q).

The audit checks the direction of the witness test, all normalization factors,
and the absence of simultaneous decoder assumptions. Those checks validate
the applications; they do not make the underlying ingredients new.

## Source-proof caveats, separated from theorem conclusions

Jones et al.'s transpose-composition shortcut is not generally completely
positive; conjugating the Kraus operators repairs the needed statement.
Devetak–Berger's Theorem 3 proof uses a unitary-invariance identity that is
false for its average marginal distortion. The audit supplies exact unitary
and nondegenerate two-qubit counterexamples to that step. These are not
counterexamples to the respective theorem conclusions. A later
rate-distortion treatment's re-use of the same single-letter reduction does
not repair it. See audit Sections 6.3 and 6.5 before importing a converse.

## Remaining comparisons and research target

The [entropy-rate note](ENTROPY_RATE_CHARACTERIZATION.md) additionally compares
Cope–Uola [2207.05722v4](https://arxiv.org/abs/2207.05722v4), Eq. (7) and
Section VI / Eqs. (20)–(22), and Cope
[2102.02333v2](https://arxiv.org/abs/2102.02333v2), Eqs. (5)–(6). These are
essential prior art for dimension/entropy regularization. The new note
proves its own fixed-cap construction and scalar-contrast continuity rather
than assuming that complete-assemblage or average-dimension formulas already
solve this single-query rate. The exact source comparison is kept there.

The audit also inspected theorem-level statements in bounded/noisy quantum
storage, random-access encodings and later quantum rate-distortion theory.
Whole-string recovery or entropy, reconstruction, and a charged classical
message cannot be silently substituted for one binary answer with free C.
The exact comparisons and unresolved reductions are in audit Section 6.6.

The new product-diagonal entropy bound has a complete elementary proof in
[COMMUTING_SEED_BOUND.md](COMMUTING_SEED_BOUND.md), but its independent novelty
has not been established. Its restricted family includes correlated spectra
and arbitrary fixed local bases; it does not include every separable state.
The new all-n one-qubit optimum is a short consequence of an established
monogamy theorem, so the novelty question concerns the task-specific theorem
and rigidity statement, not a new correlation inequality.

The remaining finite-block question starts at `n=3,q=2`. Search for a genuine
collective advantage or a converse that handles higher-dimensional global
decoders. A settling prior theorem would be a useful research result.
Preserve exact source versions, locators, timing, resource accounting and
quantifiers in every further comparison. Absence from this ledger is not
evidence of absence from the literature.
