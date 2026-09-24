# Literature comparison and remaining novelty questions

Updated: 2026-09-23. The [commit-pinned audit](audits/PROOF_AND_NOVELTY_AUDIT.md)
contains exact source versions, theorem/equation/page locators, resource maps,
proof reconstructions, and counterexamples for the bootstrap dossier. The
table below summarizes those completed targeted comparisons; subsequent
sections cover the later one-qubit and spectral results. It is not an
exhaustive certification of publication novelty.

The [coherent-transfer continuation](audits/COHERENT_TRANSFER_AUDIT.md)
compares Holevo–Shirokov, [2609.12667v1](https://arxiv.org/abs/2609.12667v1),
Proposition 1, Eqs. (14)–(15), printed p. 6. Its same-support rank-two
specialization is `1-h_2(m)<=[1-2sqrt(m(1-m))]/ln(2)`; the source uses
natural-log entropy and squared root fidelity. This established scalar
bound supplies no four-query score estimate and does not evaluate the full
two-parameter formation profile. The coherent block inequality used in the
continuation is itself an elementary trace-norm triangle consequence, not
a proposed novelty. The report makes no new publication-originality claim.

The later [publication and optimality assessment](audits/PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md),
pinned to `81bcfefb2b545742d513c4f51364a7f72972451e`, narrows the paper claim
and adds a prior CHSH derivation of the symmetric one-site entropy curve.
Its convexity consequences and exact failed-tensorization example explain
why the unrestricted rate question needs a new global argument.

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

## Additional prior derivation of the symmetric formation-entropy curve

Zhu–Zhang–Ma, *Interplay among entanglement, measurement incompatibility,
and nonlocality*, [2303.08407v2](https://arxiv.org/pdf/2303.08407v2),
20 June 2025, Theorem 2 / Eq. (25), printed p. 14, gives the
dimension-independent CHSH lower bound `E_F >= (S_CHSH-2)/(2sqrt(2)-2)`
at alpha=1. Their convention is Eq. (2), p. 5; Appendix A.1,
pp. 28–29, supplies the dimension reduction. For the assemblage
`sigma_(+/-|X)=(I+/-eta X)/4`, `sigma_(+/-|Z)=(I+/-eta Z)/4`, trusted
observables `(X+Z)/sqrt(2)` and `(X-Z)/sqrt(2)` give
`S_CHSH=2sqrt(2)eta`. Cope 2102.02333v2, Theorem 2, p. 3, then gives
`E_FA >= [(eta-1/sqrt(2))/(1-1/sqrt(2))]_+`. A flagged mixture of the
compatible and Bell endpoints attains it. Thus this symmetric one-site
formula is a short exact corollary of prior results.

The [assessment](audits/PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md), Section 2,
supplies the explicit normalization and attainment. This further narrows
the novelty candidate to the full two-parameter evaluation, phase boundary
and scoped product-diagonal tensorization. It does not establish the
unrestricted many-site entropy inequality: summing local formation costs
against one global entropy budget is not justified by the source theorem.

## Exact-axis reduction and unequal-accuracy collective advantage

The [exact-axis note](EXACT_AXIS_SPECTRAL_REDUCTION.md) proves that perfect
X preservation forces every refined seed Gram matrix to be diagonal in the
product X basis. The complementary-query optimum is exactly
`Lambda(n,D)/n`, the induced-cube spectral-radius problem with support size
at most D. A complete translation instrument proves the reverse direction.
This is an operational reduction to an established graph problem.

| Primary source and locator | Established ingredient and exact transfer |
|---|---|
| Bollobás–Lee–Letzter, [1605.06360v1](https://arxiv.org/pdf/1605.06360v1), Question 1 p. 2, Theorem 2 p. 3, Rayleigh quotient in Section 2 p. 4; [final author PDF](https://www.homepages.ucl.ac.uk/~ucahsle/papers/cube-evals.pdf), dated 7 August 2020, Theorem 2 p. 3 | The induced-cube spectral optimization is prior. The v1 theorem says 103<=D<=n; the later author version says 105<=D<=n. The repository uses their common range 105<=D<=n. Padding a smaller support and applying this theorem gives `z_max=sqrt(D-1)/n`. The graph theorem is not a new deduction. |
| Avni–Samorodnitsky, [2411.14597v1](https://arxiv.org/pdf/2411.14597v1), 21 November 2024, Corollary 1.8 p. 6, Example 1.12 p. 8, Corollary 1.15 p. 11 | Gives Krawtchouk-root characterizations, the Hamming-ball/star spectrum, and asymptotic comparisons. These do not certify optimality of the separate n=31,D=32 construction. |
| Guerini–Quintino–Aolita, [1904.08435v4](https://arxiv.org/pdf/1904.08435v4), 14 October 2019, Theorems 2–3 p. 4 | Trusted quantum-input distributed sampling relates classical simulation to joint measurability. It does not evaluate the present worst-case retained-quantum-dimension boundary. |
| Lobo–Balanzó-Juandó–Pironio, [2605.16151v1](https://arxiv.org/pdf/2605.16151v1), 15 May 2026, Definitions 1–2 pp. 2–3, Eqs. (2)–(3), (9)–(11) | Partial input joint measurability permits selected settings to become classical while residual quantum information remains. The inspected definitions do not impose the dimension cap here or identify all collectively compressed protocols with mixtures retaining original sites. |

The complete region of the explicitly defined original-site-retention class
is `sum_i w(x_i,z_i)<=q`. A star seed at n=31,D=32 lies strictly outside it,
also at X contrast 9999/10000 and Z contrast 1/sqrt(31). The constituent
star spectrum, compatibility disk and local weight are established;
the supplied operational reduction, full comparison-class converse and
separation are repository deductions. Neither an original graph theorem nor
an equal-X/Z-accuracy advantage is claimed. Prior subsumption of the precise
operational separation remains an open novelty comparison.

## Quantitative one-qubit stability

The [stability note](ONE_QUBIT_STABILITY.md) turns the exact one-qubit
equality form into explicit overlap and Frobenius-distance bounds using
the established Cheng–Hall inequality and a spectral gap. Kaniewski,
[1604.08176v3](https://arxiv.org/pdf/1604.08176v3), 11 August 2016,
defines extraction fidelity on p. 2 and proves a CHSH extraction bound in
Proposition 1 / Eq. (10), p. 3. That device-independent task permits
arbitrary dimensions and local extraction channels. Here the input
reference and output are fixed qubits, and the conclusion locates the
entire normalized seed relative to a retaining-one-site form. No new
general self-testing method or complete-channel distance bound is claimed.

## Exact two-qubit SLD minimum

The [fixed-spectrum theorem](TWO_QUBIT_SLD_SPECTRUM.md) evaluates the
minimum local SLD sum and proves `I_XZ>=2-S` for all two-qubit states.
It combines established ingredients with the special two-qubit identity.
Wootters, [quant-ph/9709029v2](https://arxiv.org/pdf/quant-ph/9709029v2),
Eqs. (4)–(5), p. 3, supplies the familiar spin flip; Rungta et al.,
[quant-ph/0102040v2](https://arxiv.org/pdf/quant-ph/0102040v2), 10 June
2001, Eq. (2.11), p. 7, gives its universal-inversion identity with unit
normalization. Fiderer–Fraïsse–Braun,
[1905.06101v2](https://arxiv.org/pdf/1905.06101v2), 27 December 2019,
Theorem 1 / Eq. (3), p. 2, maximizes QFI over a unitary orbit for one
fixed generator. Its Supplemental Lemma 3 proof, Eqs. (16)–(17), p. 8,
already contains the relevant eigenvalue-kernel crossing inequality.
The present deduction instead minimizes a fixed sum of local generators.

Kim–Li–Kumar–Wu, [1711.02323v5](https://arxiv.org/pdf/1711.02323v5),
Eq. (6), p. 2, uses the same SLD/4 normalization. Section III.A's
definition before Theorem 1, p. 3, minimizes a sum over one party's
orthonormal projectors with the state fixed, a different optimization.
The full assumption map is in the new proof note. The resulting square-root
score bound does not prove the sharp linear seed entropy conjecture, and
the all-n SLD inequality remains unresolved. These targeted comparisons
do not certify absence of the operational results from the literature.

The [spectral-tail corollary](audits/TWO_QUBIT_SPECTRAL_TAIL_GATE.md) now
proves the sharp two-qubit seed entropy target for every complex eigenbasis
when `lambda_3+lambda_4>=1/29`. It uses this same SLD envelope, the standard
binary entropy series, and an explicit exact rational interval certificate.
The additional supplied deduction is this scalar spectral implication;
neither its ingredients nor the general SLD framework are claimed new.
The remaining low-tail region, all-block optimality, and prior subsumption
of the separate two-parameter steering-formation result remain unresolved.

The [core-stability continuation](audits/TWO_QUBIT_CORE_STABILITY.md)
additionally uses Cheng--Hall, [1610.09302v3](https://arxiv.org/pdf/1610.09302v3),
25 January 2017, printed p. 3, Eqs. (10) and (14). These established
identities relate optimized CHSH parameters to local purities and bound
their sum with independent measurement settings. Applied to the pure
three-qubit purification of a rank-two core, they give the stronger
active-score bound `f_A^2<=2(1+r_B^2-r_Q^2)`. They are not applied to the
full state's four-dimensional purifying system.

The supplied consequences are a finite-tail theorem for all high-score
rank-two cores, an analytical exclusion of sufficiently unbalanced core
spectra, and an explicit uniform n=2 entropy-valid radius `2^-20`.
Block trace inequalities, principal-angle geometry and interval arithmetic
are standard ingredients. These deductions neither close the all-state
inequality nor certify a new monogamy theorem or publication originality.

## Asymmetric entropy converse and the sharp exact-axis rate

The [asymmetric converse](ASYMMETRIC_ENTROPIC_CONVERSE.md) combines known
entropy ingredients with the normalized-seed reduction to prove
`log_2D>=sum_i max{0,f(z_i)-h_2((1-x_i)/2),f(x_i)-h_2((1-z_i)/2)}`,
where `f(c)=h_2((1-sqrt(1-c^2))/2)`. Its common-accuracy consequence
improves the rate lower bound and proves linear onset above the classical
threshold. The [exact-axis rate](EXACT_AXIS_RATE.md) evaluates R_X(z)=f(z),
with complete instruments preserving X exactly at every finite block length.

| Primary source and exact locator | Established result and operational comparison |
|---|---|
| Wehner–Christandl–Doherty, [0808.3960v2](https://arxiv.org/pdf/0808.3960v2), 20 November 2008, Lemma I.1 begins p. 2; proof and Corollary I.2 p. 3 | Already supplies `H(Q)>=H(U^n)-sum_i h(error_i)` for arbitrary correlated, nonuniform labels and separate coordinate decoders. In our proof the priors are squared X-basis column norms, the signal states are normalized columns, and `H(Q)=S(L^dagger L)`. This subsumes the quantum decoding ingredient exactly. The physical unknown specimen has not been replaced by a supplied classical string. |
| Wootters, [quant-ph/9709029v2](https://arxiv.org/pdf/quant-ph/9709029v2), Eq. (8) and following text p. 4 | Defines the same scalar function, its monotonicity and convexity. Its use here does not identify a general many-qubit seed with two-qubit concurrence. |
| Samorodnitsky, [0807.1679v1](https://arxiv.org/pdf/0807.1679v1), 10 July 2008, Theorem 1.2 / Eq. (7) p. 5; Theorem 1.4 begins p. 6, Eq. (10) p. 7 | The nonlinear cube entropy inequality and asymptotically sharp support-cardinality bound are prior. With a square-root probability vector, the Dirichlet quotient is `2(n-sum_i F_i)`; convert natural entropy to bits. Combined with our finite exact-axis reduction, these statements already imply R_X(z)=f(z). The asymptotic curve is a corollary, not new graph theory. |
| Friedman–Tillich, *Generalized Alon–Boppana Theorems and Error-Correcting Codes*, [primary manuscript](https://gilkalai.wordpress.com/wp-content/uploads/2024/01/bounds.pdf), Proposition 8.5 p. 10 and Appendix C pp. 18–19, manuscript pagination | Supplies the asymptotic Hamming-ball spectral attainer, credited by Samorodnitsky. The repository instead spells out a truncated Bernoulli seed and its complete quantum instrument; neither Hamming-ball asymptotics nor support truncation is claimed as new mathematics. |
| Wilde, [1807.11939v3](https://arxiv.org/pdf/1807.11939v3), 31 October 2018, Section II.A pp. 3–4; Section IV.B Eq. (65) p. 10 | The dephasing-channel entanglement cost is exactly f(z) after setting its dephasing parameter to `(1-z)/2` and conjugating by Hadamards. Its uniform channel simulation allows arbitrary inputs, including internally entangled inputs. Full reconstruction is stronger than answering one local query; its converse cannot simply be transferred, and approximate channel simulation does not ensure exact X at each finite n. |
| Bagan–Bergou–Hillery, [2004.13573v1](https://arxiv.org/pdf/2004.13573v1), 28 April 2020, Eq. (30) p. 4; Eq. (31) p. 5 | A related wave–particle entropy bound reduces, for two alternatives and zero failure probability, to the binary entropy-loss penalty. Its coherence interpretation is prior; it does not supply the complete coordinatewise conjugate-score bound. |

The new repository deduction is the combination of the cube-flip
trace-norm comparison, these established entropy bounds, arbitrary Kraus
averaging and restriction to selected input sites. This proves a useful
unrestricted converse and its linear-onset corollary. The exact-axis result
adds a sharp local-query converse and exact-axis finite construction to an
already known rate curve. This is a substantial prior overlap, not a proof
of identical operational subsumption or an originality certificate.
The general common-accuracy optimum and publication novelty remain open.

## Baseline uncertainty and entanglement ingredients

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

## Entropy and steering-cost identifications

The [entropy trade-off audit](ENTROPY_TRADEOFF_PRIOR_AUDIT.md) adds two
substantive source identifications. Roga–Fannes–Zyczkowski
[1004.4782v1](https://arxiv.org/abs/1004.4782v1), Corollary 4 / Lemma 5 /
Eq. (26), printed p. 4, already bounds binary entropy of mixing by root
fidelity. Commuting pinching and relative-entropy data processing recover
the quantum penalty in the asymmetric seed inequality. Coherence of
formation superadditivity and its established qubit formula recover its
classical flip-entropy term. Exact source versions and normalizations are
recorded in that audit; these are alternative applications of prior results.

The [profile theorem](PRODUCT_DIAGONAL_PROFILE_RATE.md) also evaluates
Cope's established steering entanglement of formation for
`sigma_(+/-|X)=(I+/-xX)/4`, `sigma_(+/-|Z)=(I+/-zZ)/4`.
Cope [2102.02333v2](https://arxiv.org/abs/2102.02333v2), Eq. (10) and
Theorem 2, printed p. 3, defines that resource and relates it to state
entanglement of formation. The audit supplies both directions of the
Kraus/assemblage reduction. The evaluated convex envelope, retention-saving
phase boundary and product-diagonal tensorization are the supplied
deductions; the underlying resource is prior. No regularized
complete-assemblage cost is silently imported as the unrestricted local-query
rate. Novelty of this explicit evaluation remains under comparison.

Section 5.1 now makes that evaluation constructive: each strict-saving
profile has a unique mixture of a compatible-circle point and a single
exact-axis atom, determined by one scalar equation. Its proof uses explicit
supporting planes, strict convexity and a monotone family of chords. These
are standard convex-geometric tools applied to the already identified
resource. The uniqueness is at the level of generating profile-cost atoms,
not all assemblage decompositions or physical encoders. The source boundary
is unchanged: the two-dimensional evaluation is the candidate contribution;
the resource and its exact-axis and symmetric slices have the established
precedents detailed above.

## Remaining comparisons and research target

The [optimizer/source follow-up](audits/FORMATION_OPTIMIZERS_AND_PRIOR.md)
adds a closer direct precedent: Han–Li–Wang–Zhu,
[2111.02800v2](https://arxiv.org/abs/2111.02800v2), 27 December 2021,
Theorem 1 / Eqs. (5)–(6), p. 3, gives the full weighted pure-state
guessing optimization against trusted qubit measurements. Theorem 2 /
Eq. (10), p. 3, gives its exact mixed-concurrence counterpart; the
orthogonal product/Bell supports in Eqs. (S49)–(S50), pp. 12–13,
already require only untrusted dimension three. The central-phase qutrit
construction is therefore an explicit prior specialization.

Optimizing that entire weighted concurrence family gives minimum
concurrence w(x,z). Its scalar entropy conversion f(w) is strictly below
C at every point outside the disk with both contrasts below one, with
equality exactly on the disk and exact axes. The audit also derives the
existing C dual directly by entropy reweighting of the prior pure-state
support. Thus the full entropy convexification and optimizer evaluation
are the specific remaining calculations, not a new weighted guessing
framework. The supplied saturation analysis additionally characterizes
all qutrit entropy optimizers. Historical priority remains unresolved.

The [two-correlation formation audit](audits/TWO_CORRELATION_FORMATION.md)
identifies another direct prior ingredient. Verstraete–Wolf,
[quant-ph/0112012v1](https://arxiv.org/abs/quant-ph/0112012v1), Eq. (2),
p. 1 and Theorem 1, p. 2, gives the raw qubit minimum
`gamma(x,z)=f(sqrt([x^2+z^2-1]_+))` through an explicit normalized-CHSH
map. This formula should not be claimed new. Zhu–Zhang–Ma,
[2303.08407v2](https://arxiv.org/abs/2303.08407v2), Eq. (24), p. 13 and
the direct-sum example preceding Theorem 2, p. 14, already demonstrate
the qualitative reduction in formation cost from higher dimensions and
classical flags. Schneeloch–Howland,
[PRA 97, 042338](https://link.aps.org/accepted/10.1103/PhysRevA.97.042338),
Eqs. (2)–(3), printed p. 2, supplies an earlier conditional-entropy
certificate from two complementary correlation distributions; its
one-sided specialization is compared explicitly in the audit.

The supplied exact comparison is E_2=gamma and E_d=C for all d>=3 when
only x,z and Bob's trusted qubit X,Z are fixed. One universal qutrit
readout pair attains C, and the complete strict/equality sets are proved.
All flags count toward d here; this is separate from free classical
records in the interface problem. The full matching/cross X/Z probability
table is Bell local throughout the square, so unrestricted fully
device-independent certification from that table cannot supply positive C.
Neither that elementary distinction nor generic flagging is a novelty.

A completed full-text comparison is Giacomo Tomassoli's 2024/25 thesis,
*Certificatori di Entanglement per due qubit con due correlatori*,
[Padua catalogue](https://thesis.unipd.it/handle/20.500.12608/84769).
After earlier primary retrieval attempts returned HTTP 403, the user
supplied the PDF. The [source audit](audits/TOMASSOLI_FULL_TEXT_COMPARISON.md)
reads its definitions and formulas and proves the strongest calibrated
two-parameter extension. Its scalar concurrence boundary and exact-axis
family are prior ingredients; its printed negativity needs a factor-two
correction. Fixed orthogonal readouts give G=f([x+z-1]_+), distinct from
the optimized-readout profile C. Exhaustive originality remains open.

The [roof provenance audit](audits/ROOF_PROVENANCE_AND_JOINT_SCORE.md)
supplies a direct subsumption map to Vollbrecht–Werner
[quant-ph/0010095v2](https://arxiv.org/abs/quant-ph/0010095v2), Section IV.A,
Eqs. (38)–(41), pp. 10–11, and IV.B, Eq. (42), p. 11. These prior results
supply the symmetry convex-roof method and the abstract fixed-block
affinity/dichotomy argument. The noisy-Pauli orbit minimum and product
moment simplex are the task-specific substitutions. Their OO-invariant
state formula is not an affine identification of C: its separable region
is polygonal, while C vanishes on a quarter disk. This obstruction does
not rule out arbitrary nonlinear reductions.

Cope–Uola [2207.05722v4](https://arxiv.org/abs/2207.05722v4), Eqs. (8),
(13)–(14), pp. 5, 7–8, specializes exactly to D_M=W=w for the entire
independently noisy X/Z family. The report proves equality by twirling
the whole SDP, preserving its worst-input average-rank objective. Thus
the existing C-versus-w phase theorem also gives the full comparison with
that prior measure; equal-accuracy slices coincide. This does not equate
average log rank, formation entropy and maximum retained dimension.

Wallden–Dunjko–Andersson
[1312.5205v1](https://arxiv.org/abs/1312.5205v1), Theorem 3 / Eq. (74),
p. 14, and Lemma 7, p. 15, subsumes product additivity of the joint score:
the filtered ensemble factors with independent priors and additive Hamming
loss. A correlated seed does not satisfy those hypotheses. An explicit
exact local/joint score gap therefore persists under repetition despite
collective readout. Neither this prior theorem nor the new one-effect
formula supplies the missing all-state entropy inequality.

The [tensor-formation and channel audit](audits/TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md)
follows the fixed-readout compression chain through Cope–Uola, Wootters and
Wilde. Minimizing Choi formation entropy over all qubit channels with
`Lambda*(X)=xX, Lambda*(Z)=zZ` gives exactly `f([x+z-1]_+)`. This exceeds
the full profile C at every x+z>1 with both x,z<1; equality holds exactly
on the triangle x+z<=1 and the exact axes. Wilde's covariant-channel
theorem concerns regularized Choi entanglement cost; its dephasing special
case supplies the familiar exact-axis curve. These ingredients and the
general fixed-readout/direct-readout distinction are prior, while the
supplied comparison rules out a precise proposed subsumption of C.

The report also proves exact retained dimensions two versus three for
local versus joint product queries at a specified two-input contrast,
and a fixed-block all-or-nothing dichotomy for tensor formation. These
are supplied task-specific deductions using established machinery, not
claims of new resource theories or an unrestricted rate evaluation.

The [full-profile follow-up audit](audits/PROFILE_NOVELTY_AND_STEERING_REDUCTION.md)
supplies a complete comparison with Zhu–Zhang–Ma Theorem 2: optimizing its
whole affine weighted-CHSH family gives only the radial bound, strictly
below C at every asymmetric point outside the compatibility disk. It also
distinguishes Cope's exact-first-measurement family by outcome ranks while
crediting its earlier free/partially entangled mixture mechanism.
Tóth–Moroder–Gühne's steering linear-entropy optimization, Cope–Osborne's
extremal-decomposition algorithm and a 2026 convex-functional witness paper
are compared at specific theorem/equation locators. None of these inspected
statements is the claimed full entropy evaluation; that is a scoped finding.

The same report proves R=inf_n E_FA(L_n)/n for the single-query assemblage
and nR<=A_n<=B_n<=nC_eta for local-query versus full tensor-product formation.
An explicit incompatible-decoder example blocks an automatic branchwise
tuple extension. It explains why Cope–Uola's tensor-copy regularization or
Kaur–Wang–Wilde's intrinsic-steerability superadditivity does not supply the
missing unrestricted converse. It does not prove distinct optimal costs.

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
The [resource-optimum continuation](audits/RESOURCE_OPTIMA_AND_JOINT_DECODERS.md)
adds two closer primary comparisons. Pusey 1305.1767v1, Section IV / Figure 1,
p. 4, already presents the equal-weight negativity line and its flagged
endpoint attainment. A supplied analytical all-weight proof now evaluates
ordinary N_min=w/2 on the full profile. Its equality analysis gives a
different statement: in the noisy nonclassical interior, minimum E_F among
negativity minimizers is w. Thus the established phase C<w requires distinct
resource optima. This is not obtained by substituting negativity into Han's
convex-roof concurrence theorem.

Guehne–Reimpell–Werner quant-ph/0607163v2, Eq. (1), p. 1, Eqs. (6),(8),
p. 2, and Eisert–Brandao–Audenaert quant-ph/0607167v4, Eqs. (21)–(30),
p. 4, already supply tight joint Legendre optimization from several
expectation values. Their framework directly applies to the fixed qutrit
pair and gives the existing dual after its block evaluation. Generic
two-correlation optimization is therefore not a new method. Explicit
evaluation, unrestricted-readout universality, equality structure and the
operational translation remain the specific calculations to assess for
originality. Das et al. 1702.00672v5, Eq. (69), p. 8 / Theorem 2, p. 9,
provides a close exact-axis box-weight example, whose value V differs from
formation cost f(V). These are scoped comparisons. The Tomassoli source
has since been read; the exhaustive-priority question remains open.

The [joint-resource continuation](audits/JOINT_RESOURCE_FRONTIER.md)
extends the separate-resource comparison to the complete conditional
E_F/ordinary-negativity Pareto frontier. Verstraete et al.,
quant-ph/0108021v1, Theorems 1–2 and Eq. (14), already give the unconditional
two-qubit concurrence/negativity range; their negativity equals twice the
ordinary negativity used here. Their mixed states demonstrate why a pure
convex-roof substitution would compute E_F+lambda concurrence instead of
E_F+lambda(2N). The supplied mixed-state support proof, lambda-dependent
phase/root evaluation and arbitrary-dimension Pareto exhaustion address
that distinction. Han's weighted geometry and flagged constructions,
Pusey's equal-weight negativity endpoint, and the GRW/EBA convex-duality
method remain established ingredients. The nonlinear-source follow-up
below now derives the mixed-state support and entire sharp resource hull
from Zhu–Zhang–Ma's qubit negativity theorem. The explicit phase/root
and conditional-budget evaluation is a further calculation whose
historical priority and significance remain unverified.

McKague–Mosca–Gisin 0810.1923v1, Section II A–B, Eqs. (1)–(3), p. 2,
supplies the established real simulation representation. The continuation
specializes it to unchanged arbitrary complex inputs with real target
effects, proving an at-most-one-qubit worst-case overhead and equal
asymptotic interface rates. Real-only fixed-size entropy searches are
still not exhaustive.

For the preceding decoder theorem, Nakahira–Kato–Usuda 1501.05744v2,
Theorems 1–2, and Eldar–Megretski–Verghese quant-ph/0205178v1,
Eqs. (24)–(27)/Theorem 2, directly supply the SDP and low-rank
complementarity machinery. The new report excludes a common-positive-shift
reduction to pure minimum-error hypotheses, but the sufficient rank
condition in Nakahira–Usuda, PRA 86, 062305 (2012), was initially unread.
The [completed comparison](audits/BAYES_RANK_PRIOR_COMPARISON.md) now checks
Theorem 2 and its entire weighted extension: under the natural Hamming
ensemble, their best rank certificate is two, whereas our theorem proves
rank one. This closes that specific comparison; other reductions remain
open. The Tomassoli thesis has also since been read, as recorded below.
Exhaustive originality remains open.

Preserve exact source versions, locators, timing, resource accounting and
quantifiers in every further comparison. Absence from this ledger is not
evidence of absence from the literature.

## Sharp subspace bounds and flat-core entropy closure

The [subspace continuation](audits/SHARP_SUBSPACE_AND_FLAT_CORE.md) credits
Niu–Griffiths, [quant-ph/9810008v2](https://arxiv.org/abs/quant-ph/9810008v2),
29 April 1999, Section II.A theorem/Eq. (2.5), p. 4, and Section III
Eqs. (3.5)–(3.7), p. 6. Those statements supply the canonical form of every
complex two-dimensional two-qubit subspace and its compressed local Pauli
maps. Rotating the subspace also rotates the physical query planes, whose
orientations must still be optimized.

The report supplies that exact local-orbit optimization, with a sharp
universal `7/8` floor, and a separate sharp `2/sqrt(3)` relation between
mean coupling and its state dependence. These evaluated constants are
not stated in the inspected prior canonical/Bloch-map results. This is a
scoped comparison, not an exhaustive absence claim. A common-frame scalar
moment and an explicit polynomial majorant yield the entropy consequence
for every two-qubit state with equal largest two eigenvalues. The preceding
full-profile steering comparison, unrestricted equal-accuracy optimality,
and publication originality remain open.

## Product parity: an elementary fidelity specialization

The [parity proof](audits/PARITY_READOUT_BOUND.md) uses Fuchs–van de Graaf,
[quant-ph/9712042v2](https://arxiv.org/abs/quant-ph/9712042v2), 3 April 1998:
Definition 8 and Proposition 4, Eqs. (23)–(24), printed p. 13, identify
root fidelity with the minimum classical Bhattacharyya coefficient over
measurements, crediting Fuchs–Caves. Theorem 1, Eq. (46), p. 17, is an
equivalent route via half trace distance. The explicit observable
`A=(R-URU)/(2sqrt(1-z^2))` gives swapped binary laws for a parity-invariant
state and its local-query conjugate. This immediately proves the sharp
single-query bound; the all-n sum, simultaneous attainer and two-qubit
entropy-family consequence are supplied deductions. This is not a new
fidelity principle or an originality certificate. The separate mixed-decoder
operator evaluation has an internal proof review but no completed
primary-source subsumption comparison.

## Further full-profile comparison: complementary mutual information

Wang–Wang–Chen, *Complementary Quantum Correlations Are Universal for Qubits*,
[2608.04916v1](https://arxiv.org/abs/2608.04916v1), 5 August 2026,
Eq. (1), printed p. 1, bounds two complementary classical mutual informations
by quantum mutual information. The arbitrary-qubit-ensemble lemma is Eq. (2),
p. 2; Eqs. (16)–(17), p. 3, give distillation/capacity lower bounds.
The printed scope on pp. 3–4 requires both systems to be qubits and both
readout pairs to be calibrated complementary projective measurements.

Those assumptions differ from our formation minimization: Alice may have
arbitrary finite dimension and flags, and her binary measurements are
optimized. At x=z=1/sqrt(2), our profile C is zero, whereas a separable
two-qubit state with calibrated complementary Pauli readouts obeys
`|<X_A X_B>|+|<Z_A Z_B>|<=1` by the product Bloch-vector Cauchy inequality
and convexity. Thus imposing the additional readout conditions changes
the realization problem.

Even when the source's hypotheses hold, its printed distillation certificate
at unbiased matching correlations gives only
`[1-h_2((1-x)/2)-h_2((1-z)/2)]_+`. At x=z=3/4 this is zero, while
our already evaluated `C=(2-sqrt(2))/4>0`. The first claim follows exactly
from `h_2(1/8)>1/2`, since `8^7>2*7^7`. Hence these inspected statements
do not evaluate the full formation profile or prove the unrestricted seed
entropy bound. This is a scoped comparison, not an exhaustive novelty claim.
At that comparison's research base, renewed Tomassoli retrieval attempts
returned HTTP 403. The user has since supplied the source; the
[full-text audit](audits/TOMASSOLI_FULL_TEXT_COMPARISON.md) resolves its
objective and formulas directly.

## A shorter mixed-decoder proof from prior anticommutation

Kurzyński–Paterek–Ramanathan–Laskowski–Kaszlikowski,
*Correlation complementarity yields Bell monogamy relations*,
[1010.2012v2](https://arxiv.org/html/1010.2012v2), 19 May 2011,
Eq. (1), printed p. 2, bounds the sum of squared expectations within
each set of anticommuting dichotomic observables. The following grouping
method on pp. 2–3 is an established ingredient, not new monogamy here.
The [extended-core report](audits/EXTENDED_CORE_TRANSFER.md), Section 2,
applies it separately to three overlapping sets of Hermitian Pauli
involutions and then uses Young's inequality. Every source hypothesis
holds; arbitrary complex states and decoder directions remain allowed.
This proves `||H||<=13/4` without computing the sharper envelope.

The stronger angular estimate and the partial finite-tail exclusion are
supplied deductions. The source does not state the task's full sharp
mixed-decoder envelope or two-parameter formation evaluation; their
historical priority remains unverified. This focused comparison closes
neither exhaustive originality nor the all-n entropy conjecture.

## Nakahira–Usuda's full weighted rank theorem

The official primary text of *Minimum-Bayes-cost discrimination for
symmetric quantum states*, [PRA 86, 062305 (2012)](https://doi.org/10.1103/PhysRevA.86.062305),
is now read. Theorem 2, Eqs. (8)–(9), printed p. 062305-2, and its
weighted extension Eq. (14), p. 062305-3, apply without ensemble symmetry.
For our prior-weighted pure hypotheses `sqrt(rho)Pi_t sqrt(rho)`, Remark 1
gives the nonnegative Bayes matrix `C_st=(2-d_H(s,t))/4`.

The [exact comparison](audits/BAYES_RANK_PRIOR_COMPARISON.md) exhausts
all competing-decision weights. Excluding the two neighboring hypotheses
requires opposite strict weight inequalities, so every selected sum has
rank at least two; an endpoint weight attains two. Thus the printed
certificate does not directly subsume rank-one projectivity under this
reduction. It remains established measurement theory, and a different
reduction is not ruled out. The user subsequently supplied the Tomassoli
PDF, resolving that specific request for human help.

## Tomassoli's full text: calibrated witnesses versus optimized readouts

The [commit-pinned comparison](audits/TOMASSOLI_FULL_TEXT_COMPARISON.md)
reads all 27 pages and visually checks the defining equations. Eq. (1.8),
printed p. 6, fixes one scalar expectation on two qubits; Section 1.3,
p. 7, fixes orthogonal Pauli readouts on both sides. Eq. (2.15), p. 15,
gives [abs(s)-1]_+ for concurrence, also valid for twice ordinary
negativity. Eq. (1.14), p. 9, instead defines ordinary negativity, so
the printed negativity bound has a factor-two mismatch.

The supplied exact extension fixes both XX and ZZ separately and
minimizes E_F to G(x,z)=f([abs(x)+abs(z)-1]_+). Bell-diagonal states
simultaneously minimize concurrence and ordinary negativity. All weighted
calibrated witnesses have the same underlying geometry. At x=z=2/3,
G=f(1/3)>0, whereas our arbitrary-readout gamma=C=0 via a product state.
Thus this source does not evaluate C or its joint E_F/N frontier. Its
Eq. (2.14), p. 15, does already give the (1,v) exact-axis generator.

The source's reference 25, Eisert–Brandao–Audenaert quant-ph/0607167v4,
Eq. (2), p. 2, and Eqs. (24)–(30), p. 4, already treats multiple fixed
witness constraints and tight formation bounds. That machinery applies
directly to our fixed qutrit pair. The candidate contribution must be the
explicit evaluated profile, universality over readouts, and equality
structure; having two parameters or using convex duality is not novelty.
The thesis access gap is closed. Exhaustive subsumption, publication
significance, and unrestricted memory optimality remain unresolved.

## Nonlinear weighted-CHSH subsumption of the resource support

The [new exact source map](audits/NONLINEAR_CHSH_SUBSUMPTION.md), pinned
to main `ac0bf7cebd5a8a346d8b64371edab7b2c30ca271`, strengthens the
earlier affine-only comparison with Zhu–Zhang–Ma,
[2303.08407v2](https://arxiv.org/abs/2303.08407v2). Corollary 1 /
Eq. (30), printed pp. 15–16, gives the nonlinear two-qubit bound
`2N>=sqrt(S_alpha^2/4-alpha^2)`. Its measurement convention is Eq. (2),
p. 5, with alpha>=1 and ordinary negativity.

For correlation weights a>=b>0, set
`t^2=a^2/alpha^2+b^2`, `cos(theta)=a/(alpha*t)`,
`sin(theta)=b/t`, and `B_±=cos(theta)X±sin(theta)Z`.
Then `S_alpha=2(ax+bz)/t`. At fixed v=2N the source yields
`ax+bz<=sqrt((a^2/alpha^2+b^2)(alpha^2+v^2))` even below the
violation threshold. Minimizing at `alpha^2=max(1,av/b)` gives exactly
the two branches of B_v in the joint-resource report. Thus that entire
mixed-state lemma is a direct prior corollary.

Using E_F>=f(V), radial concavity, Jordan pinching and orthogonal flags
then gives the sharp support for every nonnegative price mu,lambda:
`max{sqrt(a^2+b^2),a+max_v[bv-mu*f(v)-lambda*v]}`. Product and
exact-axis states attain it. Consequently the full minimum-cost hull,
not just an isolated scalar line, is a short consequence of prior
theorems and standard convexity. This includes the weighted negativity
inequality underlying min N=w/2. No new mixed-state support principle
should be claimed.

This does not invalidate the earlier strict comparison with the source's
affine Eq. (25). Optimizing its nonlinear qubit theorem before mixing
blocks retains information lost by taking the scalar affine certificate
first. The candidate contribution is the explicit phase/root/budget
and equality evaluation with its operational consequences; its novelty
and publication significance remain open. Neither reduction sums costs
across trusted sites sharing one memory register.

## Weighted allocation within the decoder algebra

The [all-budget weighted proof](audits/WEIGHTED_DECODER_ALLOCATION.md),
Section 6, credits prior graph-Clifford dimension and weighted graph-norm
methods, including Xu et al. 2511.13531v1, Section IX.1 Eq. (37).
The supplied threshold ordering and finite operator levels evaluate the
original-pair allocation bound. Its broader priority remains unresolved;
the theorem explicitly restricts the readout algebra, not the encoder.

## Spin-flip purity bound

The [source comparison](audits/SPIN_FLIP_PURITY_BOUND.md), Section 7,
credits Uhlmann's published PRA 62, 032307 (2000) for the exact
three-qubit conjugation family and individual fidelity roofs. The
corrected version was checked. The supplied joint six-score purity
inequality and its readout consequence are separate deductions;
exhaustive originality and publication significance remain unresolved.

## Every common antiunitary readout symmetry

The [extension](audits/ANTIUNITARY_READOUT_BOUND.md) combines the preceding
spin-flip result with an explicit Pauli-algebra reduction and Cheng–Hall's
established independently optimized, mixed-three-qubit monogamy inequality
(1610.09302v3, Eqs. (13)–(14), p. 3). It covers square +I and nonscalar
squares, as well as general odd Hermitian contractions. The qubit theorem
is invoked only after a valid reduction of the readouts or memory blocks.
The supplied deduction is the resulting common-antiunitary bound; no new
monogamy principle or exhaustive priority claim is made. The full balanced
sector remains outside the conclusion.

## Jordan-block converse and established singlet monogamy

The [qutrit and four-sector converse](audits/JORDAN_BLOCK_CONVERSE.md)
uses established Bell-projector overlap geometry. Kay–Kaszlikowski–Ramanathan,
*Optimal Cloning and Singlet Monogamy*, PRL 103, 050501 (2009),
[0901.3626v3](https://arxiv.org/pdf/0901.3626), Eqs. (3)–(6), printed
pp. 2–3, supplies the weighted overlap mechanism. That version does not
prove its fully general asymmetric ansatz; the present direct Gram upper
bound uses no unproved part.

Jorquera et al., *Monogamy of Entanglement Bounds and Improved Approximation
Algorithms for Qudit Hamiltonians*, Quantum 10, 2088 (2026),
[2410.15544v4](https://arxiv.org/pdf/2410.15544), Lemma 3.4/Eq. (8),
p. 7, Proposition 3.6/Eq. (18), p. 8, and Theorem 3.7, p. 9, already
gives the equal-dimensional star-projector bound and unweighted attainment.
These locators follow the PDF marked v4, 20 April 2026. Its qubit,
three-edge constant is two. The interface proof permits distinct embedded
memory planes and proves the needed ordinary-operator estimate directly;
it does not extend the source's pseudo-density/SOS conclusion.

The supplied deduction is the local Jordan-block spectral majorant and
its interface application: all three-input rank-at-most-three seeds and
four ququart signature patterns obey the two-site-retention benchmark.
This is not a new general monogamy theorem. Exhaustive priority,
publication significance, and unrestricted optimality remain open.

## Double-block spectral certificate and closer dimension precedent

The [continuation](audits/JORDAN_SPECTRAL_BUDGET.md), Section 5, maps the
two-site operator to Bermejo Morán–Pozas-Kerstjens–Huber's PRL 131, 080201
(2023), J_2, with exact PDF locators and numerical-status qualifications.
Its pairwise bounds do not settle the three-site target. Gour–Wallach's
2007 Proposition 3 and Corollary 4 already supply the double-Bell-subspace
representation as a qubit subsystem; site-dependent subsystem choices
remain unconstrained. The supplied all-block Gram application and exact
failure of every finite negative-top penalty do not establish publication
originality or unrestricted optimality.

## One double-block pair: full-spectrum converse and prior Choi bound

The [full-spectrum continuation](audits/SINGLE_DOUBLE_BLOCK_CONVERSE.md)
excludes the three entire patterns `(22)(11)^2`, `(22)(11)(12)`, and
`(22)(12)^2`. Combined with the earlier four-pattern exclusion, three
nonscalar signatures remain unresolved. Its supplied deduction is the
positive-spectrum resolvent estimate and its interface application;
the mixed qubit-Choi inequality used inside it is a prior-theorem corollary.

Specifically, let A,C,B all have dimension d and let the positive,
trace-one operators rho_AB and sigma_CB obey
`Tr_B rho=I_A/d` and `Tr_B sigma=I_C/d`. In the output-first Choi
convention, `J(T)=d rho` and `J(U)=d sigma` define unital completely
positive maps. Applying `T_A tensor U_C tensor id_B` to the pure
Bell-star inequality gives
`rho_AB+sigma_CB<=(1+1/d)I`, with spectator identities understood.
The maps act on different leaves. No simultaneous choice of memory
factors, pure-state decomposition into Bell vectors, or unital
Schrodinger-picture channel is required.

The pure inequality is supplied by Jorquera et al.,
[2410.15544v4](https://arxiv.org/pdf/2410.15544), Proposition 3.6,
Eq. (18), printed p. 8, specialized to two edges. These locators refer
to the PDF marked 20 April 2026. The pullback establishes an ordinary
operator inequality; no extension of its pseudo-density/SOS certificate
is asserted. At d=2 this yields the mixed-Choi bound 3/2 and, after
the report's compression identity, the required bound 3/4.

Renes, *Better bounds on optimal measurement and entanglement recovery,
with applications to uncertainty and monogamy relations*, PRA 96, 042328
(2017), [1707.01114v1](https://arxiv.org/pdf/1707.01114), Section 3.2,
Eqs. (17)–(18), printed p. 4, independently supplies a stronger
local-recovery fidelity region. Taking the recovery channels to be
the adjoints of T and U gives the same sum bound. The retrieved arXiv
version is dated 4 July 2017; its equation numbering is used here.

The report also supplies a direct Kraus/Gram proof for arbitrary center
dimension. The equal-dimensional pullback above does not by itself
subsume that broader formulation; its priority is not established.
Neither formulation evaluates unrestricted `Gamma(3,4)` or the general
equal-accuracy rate. Publication originality remains unresolved.
