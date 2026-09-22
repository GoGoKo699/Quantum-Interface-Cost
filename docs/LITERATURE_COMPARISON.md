# Literature comparison and remaining novelty questions

Updated: 2026-09-22. The [commit-pinned audit](audits/PROOF_AND_NOVELTY_AUDIT.md)
contains exact source versions, theorem/equation/page locators, resource maps,
proof reconstructions, and counterexamples for the bootstrap dossier. The
table below summarizes those completed targeted comparisons; subsequent
sections cover the later one-qubit and spectral results. It is not an
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

## Complete one-qubit accuracy region: established local resource, global deduction

The [allocation theorem](ONE_QUBIT_ALLOCATION_REGION.md) evaluates all 2n
separate local contrasts under the same worst-case dimension-two cap:
`sum_i w(eta_(i,X),eta_(i,Z))<=1`, where
`w(x,z)=[x+z-1-sqrt(2(1-x)(1-z))]_+`. The local w is the established
incompatibility weight, not a new resource definition. The new repository
deduction is its exact global budget, proved through weighted Cheng–Hall
monogamy, Kraus refinement and convex geometry, with a matching mixture of
strategies retaining at most one site. It does not assert that every encoder
has that form.

Section 7 of that note records exact versions, dates and theorem locators:
Yu–Liu–Li–Oh [0805.1538v2](https://arxiv.org/abs/0805.1538v2), Theorem 1 /
Eq. (5), pp. 1–2, gives the orthogonal compatibility disk; Pusey
[1502.03010v2](https://arxiv.org/abs/1502.03010v2), Eq. (15), p. 4, defines
incompatibility weight. Cope–Uola
[2207.05722v4](https://arxiv.org/abs/2207.05722v4), Section IV.C /
Eqs. (13)–(14), pp. 7–8, relates it to average compression dimension.
That average resource does not supply a cap on every collective branch.
Their full-product-measurement subadditivity also does not supply this
local-query-union converse. Ioannou et al.'s simulability model contains
the task exactly, but its inspected Claim 3 / Eq. (13), p. 4, in
[2202.12980v1](https://arxiv.org/abs/2202.12980v1) evaluates a different
measurement family. Alves–Gigena–Kaniewski
[2302.08494v3](https://arxiv.org/abs/2302.08494v3), Eq. (7), p. 3, and
Lemma 4 / Eq. (30), p. 9, instead gives the sender a classical string;
unlimited input-dependent classical records would trivialize that task.

These inspected statements establish the ingredients and framework without
settling subsumption of this evaluated region. Its publication novelty
remains unresolved; the result is a short task-specific application of
established monogamy, not a new general correlation inequality.

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

## Further functional-inequality comparison

Beigi, [2105.00462v2](https://arxiv.org/abs/2105.00462v2), Theorem 2,
Eqs. (6)–(7), printed p. 4, provides a nonlinear entropy/Dirichlet inequality
for arbitrary positive operators. Theorem 4, p. 6, gives its rank version.
Audenaert–Nussbaum–Szkoła–Verstraete,
[0708.4282v1](https://arxiv.org/abs/0708.4282v1), Appendix A, Theorem 6,
Eq. (55), p. 32, bounds root fidelity squared by affinity. The
[global converse](STRONG_ENTROPIC_CONVERSE.md) supplies the normalization,
two-Pauli Fourier comparison and worst-case dimension reduction that turn
these established ingredients into a stronger memory lower bound.

This is a new deduction in the repository, with independent analytical
checks, rather than a new logarithmic-Sobolev result. No prior theorem's
sharpness transfers automatically through the fidelity inequality; the note
quantifies the remaining loss. Whether this exact operational corollary has
appeared before remains an open novelty comparison.

The [boundary note](ENTROPY_INEQUALITY_BOUNDARIES.md) proves exact rank-two
spectrum optimization and additional exclusions. Its rank-two proof uses
the already identified Cheng–Hall theorem plus an elementary mixed-marginal
correlation bound. Its stabilizer argument reduces to the classical two-point
logarithmic-Sobolev inequality and entropy conditioning. Its projector
arguments are elementary compression identities. These are separate scoped
deductions; their presence does not certify an original general theorem.

Sections 6–7 of the boundary note now optimize spectra `(t,b,...,b)` at every
input size and `(a,a,b,b)` on two inputs. Their proofs use invariant
two-dimensional blocks, principal angles, Pauli expansions and concavity;
product-diagonal attainers transfer the already proved entropy inequality.
Together they exclude all two-qubit spectra with at most two distinct
eigenvalues, counting zero. The separate
[kernel converse](TWO_QUBIT_KERNEL_CONVERSE.md) uses compression inertia,
a Pauli sum identity and an adjugate bound to obtain further rank-three
certificates, including all kernels containing a maximally entangled vector.
These are independently reconstructed deductions, not a proof of the
unrestricted entropy bound or certified original spectral inequalities.

The [entanglement calibration obstruction](ENTANGLEMENT_CALIBRATION_OBSTRUCTION.md)
uses Christandl–Winter [quant-ph/0308088v3](https://arxiv.org/abs/quant-ph/0308088v3),
Definition 1, printed p. 1: taking a trivial extension gives
`E_sq<=I(A:B)/2`. An exact near-Bell family then refutes a sharp affine
local charge and every calibration with finite endpoint slope, sharp at the
Bell endpoint `phi(2)=1`, and bounded by this upper bound. It leaves the existing weaker faithfulness
converse valid and is not a counterexample to the seed entropy conjecture.

## Nonuniform spectra and the proposed SLD route

The [support-inertia note](SUPPORT_INERTIA_CONVERSE.md) uses Sylvester inertia,
trace-norm duality and two anticommuting local Paulis to give an all-spectrum
support converse and an explicit geometric neighborhood. The
[spectral-tail note](LOW_RANK_ENTROPY_STABILITY.md) combines a supplied block
trace-norm estimate with the already proved rank-two equality classification,
orthogonal-mixture entropy and compactness. These are task-specific deductions
with independent reconstruction; no absence from the literature is asserted.
The [fixed-support optima](NONUNIFORM_SUPPORT_OPTIMA.md) use concavity of root
fidelity and a symmetry average. They disprove two proposed flattening steps,
without supplying a collective advantage or a new general fidelity theorem.

The [SLD audit](SLD_ENTROPY_ROUTE_AUDIT.md) supplies exact versioned locators
and mathematical comparisons for the following primary sources:

| Source and locator | Established statement | Missing transfer to the proposed local X/Z SLD entropy sum |
|---|---|---|
| Yu, arXiv:1302.5311v1, Eqs. (1),(4), p. 1 | SLD/4 is the convex roof of variance for one observable | Separately minimizing ensembles cannot be replaced by one common ensemble |
| Cao–Lu, arXiv:1904.06562v2, Theorem 1, p. 2; Section 5.1, p. 17 | Chi-square contraction tensorizes under specified metric/channel hypotheses | SLD's weight lies outside the two stated cases; reference-state contraction is a different target |
| Bu–Gu–Jaffe, arXiv:2302.07841v3, Section IV.B, Theorem 15, p. 5 | Convolution inequality for local divergence Fisher information | The logarithmic eigenvalue kernel is not SLD, and convolution does not implement this encoder |
| Toth, arXiv:1701.07461v5, Observation 3, p. 2; Section V | Averages over all traceless observables; an approximate entropy relation in Eq. (69) | Neither an all-directions average nor an approximation proves the fixed local-query inequality |
| Rouze–Wirth–Zhang, arXiv:2209.07279v3, Section 6.4, pp. 33–34 | A quantum maximum-L1-influence bound; a classical sharp edge formula | The needed sharp total-L2 rank inequality is not an inspected theorem there |
| Liu, arXiv:2303.01952v5, Definition 3.1, printed p. 13; Theorem 3.4 and footnote 22, printed p. 14 | An upper bound on quantum Jensen–Shannon divergence using a geometric-kernel triangular discrimination | This is not the measured harmonic-kernel SLD quantity; no finite universal entropy-to-single-pinching-SLD conversion exists |
| Cheng–Hsieh, arXiv:1506.06801v2, Corollary 8, p. 10; normalized trace, p. 3 | A defective matrix logarithmic-Sobolev inequality | The dimension defect makes the direct Pauli-orbit substitution vacuous for the desired entropy deficit |
| Chang–Li, arXiv:2601.01900v2, Corollary 4.1 / Eq. (36), pp. 23–24 | A strengthened influence lower bound | Substitution of `A=2P-I` gives a valid but weaker flat-state information bound than `log_2(1/t)` |

Two exact counterexamples refute a local conditional-entropy charge and a
unit-coefficient SLD bound on pinching entropy increase. Neither refutes the
proposed global SLD sum or the sharp seed entropy conjecture. The audit
distinguishes the three-Pauli projector energy from the X/Z query energy;
they cannot be identified by dropping a normalization or a Y contribution.
These comparisons are scoped to the inspected statements; subsumption by
other prior work and publication novelty remain unresolved.

The same audit now derives a commutator integral and an all-spectrum
comparison between the X/Z and three-Pauli information sums. It reformulates
the target as a rational entropy inequality on graphs induced by quantum
eigenbases. An explicit nonphysical graph satisfies the elementary necessary
constraints but violates the target, showing that those constraints alone
lose essential structure. None of these steps proves or refutes the global
quantum SLD candidate.

## Remaining comparisons and research target

The [flat-seed comparison](FLAT_SEED_PRIOR_COMPARISON.md) now checks
Montanaro–Osborne, arXiv:0810.2435v3, Proposition 57 and Theorem 58,
p. 31, and Proposition 71 / Eq. (163), p. 37, together with their v5
locators. Blecher–Gao–Xu, arXiv:2409.00224v1, Section 6, Lemma 6.1 and
Theorem 6.2, supplies a later repair of a step in the original FKN proof.
The exact mapping separates standard Pauli influence from the X/Z query
energy and from compression trace norms. The inspected prior bounds do not
by themselves give the sharp flat-seed value. The new proof supplies a
four-sign spectrum calculation, grouped compression estimates, and separate
lower-flat-rank estimates; it is not a new general FKN theorem. Possible
subsumption by a different sharp result remains unresolved.

The further classical-flag, locally mixed two-qubit, and bounded-condition
entropy exclusions use standard fidelity monotonicity, elementary two-qubit
spin-flip algebra, and the already identified Beigi inequality, respectively.
Their proof notes supply the matrix steps explicitly. They are short
task-specific deductions and do not establish a novel general framework
or a new unrestricted rate formula.

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
