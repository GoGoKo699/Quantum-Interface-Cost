# Status and claim ledger

Updated: 2026-09-24. Stage: the [all-block spectral certificate](audits/JORDAN_SPECTRAL_BUDGET.md) gives one scalar sufficient test using each Jordan block's actual excess. It excludes continuous families with two noncommuting blocks at every site, without common memory planes or symmetry. Every finite penalty on only the negative top Bell projectors fails to repair the earlier bound; an exact spectrum proves this. The prior rank-three exclusion and four closed ququart patterns remain valid. All six remaining signature patterns retain unresolved regions. Unrestricted equal-accuracy optimality and publication originality remain open; the prior nonlinear-CHSH subsumption remains in force.
Latest research base: `780605b723919defd382d88c8adb09ed1fd8d204`, the merge of PR #35.

Critical assessment base: `81bcfefb2b545742d513c4f51364a7f72972451e`, the
merge of PR #11. The [publication and optimality assessment](audits/PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md)
identifies further prior subsumption, proves the asymptotic rate dichotomy
and rules out a direct deficit-superadditivity argument. Its judgment is
a credible narrower paper candidate, with no proof of unrestricted optimality
or certification of publication novelty.

## Evidence labels

**Established ingredient** means an identified prior result. **Derived and
independently checked** means a supplied argument was reconstructed by another
agent in this workspace; it does not mean external peer review or publication
novelty. **Construction checked** means only the listed finite identities were
tested. **Unresolved** means neither a theorem nor its absence from prior work
is asserted.

| Claim | Status | Location |
|---|---|---|
| General delayed measurement simulation with classical assistance | Established framework; also equivalent here to a prior postmeasurement-information discrimination task | Audit Sections 6.1–6.3 |
| q=0 iff eta<=1/sqrt(2) | Established threshold; elementary derivation checked | Note Section 3; audit |
| Random-subset achievable contrast | Explicit construction; checked through n=4 | Note Section 4; checks.json |
| Entropic memory lower bound | Standard-theorem application; independently checked | Note Section 5; audit Section 4.1 |
| Logarithmic-Sobolev lower bound b(eta) on q/n and R(eta) | Derived and independently checked from Beigi and Audenaert et al.; unrestricted | STRONG_ENTROPIC_CONVERSE.md |
| Asymmetric profile bound log D>=sum_i kappa(x_i,z_i) | Derived and independently checked; combines generalized QRAC entropy and cube-entropy ingredients, preserves every collective branch | ASYMMETRIC_ENTROPIC_CONVERSE.md |
| Common-accuracy rate R(eta_0+t)=Theta(t) as t decreases to zero | Derived and independently checked; coefficients bounded by 2log_2(1+sqrt(2)) and 2+sqrt(2), exact coefficient open | ASYMMETRIC_ENTROPIC_CONVERSE.md |
| Unrestricted linear seed bound g<=sqrt(2)n+S/log_2(1+sqrt(2)) | Derived and independently checked; weaker than the conjectured sharp entropy coefficient | ASYMMETRIC_ENTROPIC_CONVERSE.md |
| q=n for exact readout | Also a corollary of Ballester–Wehner–Winter Lemma 5.1 | Audit Section 6.1 |
| Positive linear rate for fixed eta>1/sqrt(2) | Derived and independently checked, using corrected one-way-LOCC faithfulness | Note Section 6; audit Section 4.2 |
| Existence of R(eta) by subadditivity | Derived and independently checked | Note Section 7; audit Section 4.3 |
| Exact normalized-seed variational formulation | Derived and independently checked; not asserted novel | Seed reduction; audit Section 5 |
| Seed twirl produces a valid uniform interface | Analytical proof checked; 10 finite construction diagnostics | results/seed_twirl.json |
| Gamma(n,2)=2+sqrt(2)(n-1), for every n | Derived and independently checked from Cheng–Hall monogamy; subset strategy optimal with one retained qubit | ONE_QUBIT_OPTIMALITY.md |
| Complete 2n-contrast region for worst-case dimension two | Derived and independently checked; sum of local incompatibility weights <=1, with matching weighted support function and implementation | ONE_QUBIT_ALLOCATION_REGION.md |
| Exact equal-accuracy retention bound at every n,q with pairwise commuting/anticommuting reflection readouts | Derived and independently checked from prior graph-Clifford rank and elementary matching; arbitrary encoders, explicit decoder hypothesis | audits/DECODER_ALGEBRA_AND_THREE_INPUT.md |
| Full region sum_i w(x_i,z_i)<=q under that readout hypothesis at every n,q | Derived and independently checked; threshold matching, finite operator levels, and retention attainment give every nonnegative weighted support | audits/WEIGHTED_DECODER_ALLOCATION.md |
| Unrestricted Gamma(3,4) is the maximum of the subset value and six remaining nonscalar reflection-sector optima | Exact discrete reduction followed by the analytical exclusion of four patterns; the six remaining continuous optimizations are unresolved | audits/DECODER_ALGEBRA_AND_THREE_INPUT.md; audits/JORDAN_BLOCK_CONVERSE.md |
| Every three-input rank-at-most-three seed obeys Gamma(3,3)<=4+sqrt(2) | Derived and independently checked; arbitrary complex eigenvectors, nonuniform spectra and full trace norms. No symmetry assumption or evaluation of the optimal qutrit score | audits/JORDAN_BLOCK_CONVERSE.md |
| One noncommuting Jordan block per original pair gives a weighted converse in every memory dimension | Derived and independently checked via a local Bell-projector majorant and weighted Gram bound; at n=3 it implies the full two-site-retention support. General contractions are included for dimension at most three | audits/JORDAN_BLOCK_CONVERSE.md Sections 1–3 |
| All Jordan blocks give a weighted scalar certificate B(Lambda)<=1 for norm(H)<=sum r_i+Lambda | Derived and independently checked for arbitrary reflection pairs and memory dimension; positive Lambda must exceed every excess. Exact equivalence for the comparison matrix, sufficient only for the physical Hamiltonian | audits/JORDAN_SPECTRAL_BUDGET.md Sections 1–2 |
| At n=3,D=4, sum_i (x_i+y_i-x_i y_i)/(4-x_i-y_i)<=1 excludes a benchmark violation | Derived and independently checked; x_i,y_i are actual block excesses divided by 2-sqrt(2), padded by zero. Covers open double-block families beyond the triangle bound; no full remaining sector is closed | audits/JORDAN_SPECTRAL_BUDGET.md Section 3 |
| Penalizing only the negative top Bell projectors can restore their sum bound two | Incorrect for every finite penalty kappa>=1; exact signed spectrum exceeds two while the actual physical Hamiltonian remains below the interface benchmark | audits/JORDAN_SPECTRAL_BUDGET.md Section 4 |
| Spin-flip invariant three-qubit rank-at-most-four states satisfy sum_j f_j^2<=5-4 Tr(rho^2) | Derived and independently checked by an exact sum-of-squares identity; equality at every allowed purity, and g<=2sqrt(6) excludes a finite-budget advantage in this class | audits/SPIN_FLIP_PURITY_BOUND.md |
| Ququart readouts odd under a common antiunitary of square -I have norm bound 2||w||_2 and exact uniform score 2sqrt(6) | Derived and independently checked; no pairwise commutation assumption, arbitrary actual seeds; common symmetry is an explicit restriction | audits/SPIN_FLIP_PURITY_BOUND.md Section 5 |
| Same weighted bound and classwide uniform maximum for every common odd antiunitary, with arbitrary square and general binary POVMs | Derived and independently checked; +I factor algebra and qubit monogamy, nonscalar-square block reduction, and convexity cover the remaining cases. A concrete balanced sextuple admits no such symmetry | audits/ANTIUNITARY_READOUT_BOUND.md |
| Local incompatibility weight and orthogonal-qubit compatibility disk | Established resource measure and joint-measurability criterion; exact noisy-pair value derived geometrically | ONE_QUBIT_ALLOCATION_REGION.md Section 7 |
| All maximizing one-qubit seeds retain one site and project the rest onto product bisectors, up to output unitaries | Derived equality characterization; independently checked | ONE_QUBIT_OPTIMALITY.md Section 5 |
| g(L)<=sqrt(2)n+(2-sqrt(2))S(L^dagger L) for product-diagonal Gram matrices | Derived and independently checked; arbitrary correlated spectra and local bases allowed; restricted-family result | COMMUTING_SEED_BOUND.md |
| Same entropy bound for unrestricted Gram matrices | Unresolved; a proposed local conditional-entropy proof is explicitly refuted | COMMUTING_SEED_BOUND.md Section 6 |
| Exact maximum score at fixed rank-two spectrum | Derived and independently checked; arbitrary eigenvectors allowed | ENTROPY_INEQUALITY_BOUNDARIES.md |
| Entropy inequality for all stabilizer-basis spectra and all flat rank-three two-input states | Derived and independently checked; additional excluded families | ENTROPY_INEQUALITY_BOUNDARIES.md |
| Subset bound for flat half-rank seeds with a maximally mixed complementary marginal | Derived and independently checked; a scoped converse, not the unrestricted n=3,q=2 result | ENTROPY_INEQUALITY_BOUNDARIES.md |
| Exact flat half-rank optimum and equality cases for n<=4 | Derived and independently checked; arbitrary n also covered with at most four singleton X/Z sites in the reflection | FLAT_HALF_RANK_OPTIMALITY.md |
| No flat seed improves the q=n-1 subset score for n<=4 | Derived and independently checked for every allowed flat rank, including separate lower-rank estimates | FLAT_HALF_RANK_OPTIMALITY.md |
| Entropy bound for all flat rank-three three-input states | Derived and independently checked via a Ky Fan refinement, g<=sqrt(53/2) | FLAT_HALF_RANK_OPTIMALITY.md Section 6 |
| Entropy-bound closure under local classical flags and tensor products | Derived and independently checked; all two-input states classical on either qubit | CLASSICAL_FLAG_ENTROPY_BOUND.md |
| Entropy bound for locally maximally mixed two-qubit states | Derived and independently checked; arbitrary local rotations, stronger entropy-deficit coefficient | LOCALLY_MIXED_TWO_QUBIT_BOUND.md |
| Entropy bound for full-rank states of condition number <=6.235819648070267 | Derived and independently checked; all n and eigenvectors, sufficient threshold only | SPECTRAL_CONDITION_ENTROPY_BOUND.md |
| g(rho)<=sqrt(2)n+(2-sqrt(2))a(P), where a(P) counts sites with both X/Z compressions indefinite | Derived and independently checked for every spectrum on support P; a(P)<=q excludes finite-budget advantage | SUPPORT_INERTIA_CONVERSE.md |
| No improvement on supports within one-sided distance sin(pi/8) of a subset support | Derived and independently checked; all spectra; unique equality seed within the criterion | SUPPORT_INERTIA_CONVERSE.md |
| Entropy-valid open neighborhood of the entire rank-at-most-two set at fixed n | Derived and independently checked; uniform neighborhood size existential, with separate explicit local criteria | LOW_RANK_ENTROPY_STABILITY.md |
| Exact subset-core orthogonal-tail score gain <=2sqrt(2) epsilon | Derived and independently checked; first-order sharp coefficient, conservative explicit entropy cutoffs | LOW_RANK_ENTROPY_STABILITY.md |
| Exact nonuniform optima on two small fixed supports | Derived and independently checked; refutes uniformization on fixed support, including rank four, without beating subset | NONUNIFORM_SUPPORT_OPTIMA.md |
| Exact maximum for spectrum (t,b,...,b) at every n | Derived and independently checked; arbitrary distinguished eigenvector, product-bisector attainer, entropy inequality follows | ENTROPY_INEQUALITY_BOUNDARIES.md Section 6 |
| Exact maximum for two-qubit spectrum (a,a,b,b) | Derived and independently checked; together with Section 6 excludes all two-qubit spectra with at most two distinct values, counting zeros | ENTROPY_INEQUALITY_BOUNDARIES.md Section 7 |
| Two-qubit rank-three kernel-and-spectrum converse | Derived and independently checked; computable scalar and kernel-operator entropy certificates, including all eigenbases at spectrum (1/2,1/4,1/4,0) | TWO_QUBIT_KERNEL_CONVERSE.md |
| Maximally entangled vector in a two-qubit kernel implies g<=2sqrt(2) | Derived and independently checked at every rank and kernel orientation; classwide sharp constant | TWO_QUBIT_KERNEL_CONVERSE.md |
| Sharp linear local squashed-entanglement charge | Incorrect; exact near-Bell example and no finite endpoint slope for a calibration sharp at the Bell endpoint, phi(2)=1, and bounded by half mutual information | ENTANGLEMENT_CALIBRATION_OBSTRUCTION.md |
| Global SLD sum >=n-S(rho) | Proved for n<=2; unresolved for arbitrary n; two sufficient local steps explicitly refuted | TWO_QUBIT_SLD_SPECTRUM.md; SLD_ENTROPY_ROUTE_AUDIT.md |
| SLD commutator integral, all-spectrum X/Z versus three-Pauli comparison, and induced-graph reformulation | Derived and independently checked; a generic graph relaxation is explicitly refuted without a physical-state counterexample | SLD_ENTROPY_ROUTE_AUDIT.md Sections 5–6 |
| Two-qubit local conditional-entropy proposal | Incorrect; explicit rank-two classical-quantum counterexample, without violating the global conjecture | CLASSICAL_FLAG_ENTROPY_BOUND.md Section 5 |
| R(eta) equals the regularized minimum seed entropy at contrast eta | Derived and independently checked; worst-case dimension and uniform error preserved; no closed-form evaluation | ENTROPY_RATE_CHARACTERIZATION.md |
| Exact-axis optimum z_max=Lambda(n,D)/n | Derived and independently checked; unrestricted collective encoders reduce to an established induced-cube spectral problem, with a complete translation instrument | EXACT_AXIS_SPECTRAL_REDUCTION.md |
| Original-site-retention region sum_i w(x_i,z_i)<=q | Derived and independently checked for the explicitly defined full comparison class, including joint measurements of discarded sites | EXACT_AXIS_SPECTRAL_REDUCTION.md |
| Strict collective advantage for unequal X/Z accuracies at n=31,q=5 | Explicit construction and analytical separation, also at X contrast 9999/10000 and Z contrast 1/sqrt(31); no optimality claim at this size | EXACT_AXIS_SPECTRAL_REDUCTION.md |
| Exact-axis value sqrt(D-1)/n for 105<=D<=n | Corollary of the supplied operational reduction and established Bollobás–Lee–Letzter Theorem 2 | EXACT_AXIS_SPECTRAL_REDUCTION.md |
| Exact-axis asymptotic rate R_X(z)=h_2((1-sqrt(1-z^2))/2) | Derived and independently checked operational corollary; scalar curve and asymptotic cube spectrum are established prior results, also matching known dephasing-channel cost | EXACT_AXIS_RATE.md |
| Exact rate C(x,z) for product-diagonal refined Kraus Grams | Derived and independently checked; arbitrary correlated spectra and branch-dependent local bases allowed; fixed-cap implementation from compatibility-disk and exact-axis generators | PRODUCT_DIAGONAL_PROFILE_RATE.md |
| Complete constructive optimizer for C throughout the strict-saving phase | Derived and independently reconstructed: one scalar equation specifies the unique reduced two-generator mixture. No uniqueness of physical encoders or unrestricted rate claim | PRODUCT_DIAGONAL_PROFILE_RATE.md Section 5.1 |
| C(.99,.5) lies between .324848239185893024 and .324848239186576377 | Exact rational interval certificate conditional on the analytical optimizer theorem, independently reproduced; stronger unrestricted achievable upper bound | results/profile_optimizer_certificate.json |
| Exact boundary C<w at (1-x)/(1-z)<2(1/ln2-1)^2 | Derived and independently checked for 0<z<=x<1 outside the disk, with X/Z-symmetric version; a region of unrestricted achievability beating retention, not an unrestricted converse | PRODUCT_DIAGONAL_PROFILE_RATE.md |
| C equals steering entanglement of formation of the noisy Pauli assemblage | Exact reduction to Cope's established resource; supplied explicit evaluation, publication novelty unresolved | ENTROPY_TRADEOFF_PRIOR_AUDIT.md |
| Symmetric one-site C(eta,eta) is the subset line | Also a short corollary of prior Zhu–Zhang–Ma CHSH entanglement bound and Cope Theorem 2, with flagged endpoint attainment | audits/PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md Section 2 |
| Full optimized Zhu–Zhang–Ma affine weighted-CHSH family yields only the radial formation bound | Derived and independently checked for all weights, trusted binary measurements, setting swaps and Bell-party orientations; strictly below C at every asymmetric point outside the disk | audits/PROFILE_NOVELTY_AND_STEERING_REDUCTION.md Section 3 |
| Nonlinear Zhu–Zhang–Ma negativity theorem implies B_v and the all-price joint-resource support | Direct prior corollary, independently reconstructed: optimize the nonlinear qubit theorem before Jordan-block mixing. Also supplies the abstract disk-plus-axis hull; explicit phase/root/equality evaluation is separate | audits/NONLINEAR_CHSH_SUBSUMPTION.md |
| R=inf_n A_n/n=lim_n A_n/n for local-query steering formation A_n | Derived and independently checked using the complete seed twirl and the established fixed-cap entropy theorem; no continuity of general E_FA assumed | audits/PROFILE_NOVELTY_AND_STEERING_REDUCTION.md Section 5 |
| nR<=A_n<=B_n<=nC_eta, with B_n full tensor-product formation | Derived and independently checked; strict B_n<nC_eta would refute unrestricted subset optimality, while ordinary additivity alone is insufficient | audits/PROFILE_NOVELTY_AND_STEERING_REDUCTION.md Section 6 |
| Exact n-moment formulation of B_n using at most n+1 seed orbits | Specific coordinates applying Vollbrecht–Werner symmetry reduction and standard finite convex geometry; arbitrary collective tuple POVMs and flags retained | audits/TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md Section 2 |
| At each fixed n, one interior B_n additivity point forces every-contrast additivity | Direct task-specific application of Vollbrecht–Werner Eq. (42); equivalent to a joint-decoder entropy inequality, weaker than the unproved local-query inequality | audits/TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md Section 3 |
| Local and tuple targets have exact minimum dimensions two and three at n=2, eta=(1+1/sqrt(2))/2 | Derived and independently checked; rigidity lower bound and complete rank-three instrument. This is not an entropy-cost separation | audits/TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md Section 4 |
| Fixed qubit-output completion equals the full formation profile C | Incorrect except on x+z<=1 and exact axes; minimum Choi E_F=f([x+z-1]_+) is strictly above C elsewhere | audits/TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md Section 5 |
| Commuting input queries always admit jointly trace-norm-optimal decoders | Incorrect; explicit normalized two-input seed has uniquely optimal sharp X and Z decoders. This is a branch-level obstruction, not a rate counterexample | audits/PROFILE_NOVELTY_AND_STEERING_REDUCTION.md Section 7 |
| Either R equals the subset line everywhere or lies strictly below it at every interior contrast | Elementary deduction from established convexity and endpoints; independently reconstructed. One interior equality or the conjectured sharp onset slope would settle the full curve | audits/PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md Section 3 |
| Sharp seed deficit is superadditive under taking site marginals | Incorrect; exact correlated product-bisector example at epsilon=1/1024. The global entropy conjecture itself is not refuted | audits/PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md Section 4 |
| Strict collective asymptotic saving for every exact-X profile with 0<z<1, extending to fixed interior profiles | Derived and independently checked; retention cost z exceeds R_X(z); at x=.99,z=.5 collective rate<=.354579 versus retention rate .39 | EXACT_AXIS_RATE.md |
| Exact two-qubit minimum of local SLD sum at every spectrum | Derived and independently checked; yields I_XZ>=2-S, but not the sharper linear seed entropy bound | TWO_QUBIT_SLD_SPECTRUM.md |
| Sharp seed entropy bound for every two-qubit state with lambda_3+lambda_4>=1/29 | Derived and independently checked for arbitrary complex eigenvectors; exact rational interval certificate accompanies the analytical reduction. Remaining witnesses have top-two spectral weight >28/29 | audits/TWO_QUBIT_SPECTRAL_TAIL_GATE.md |
| Sharp entropy bound for every two-qubit state with lambda_3+lambda_4<=2^-20 | Derived and independently checked; first supplied explicit uniform two-qubit radius, with no eigenbasis restriction. It does not overlap the 1/29 gate | audits/TWO_QUBIT_CORE_STABILITY.md |
| No two-qubit entropy witness has top-two core score >10/3 or normalized second core eigenvalue <=1/5 | Derived and independently checked; finite-angle high-score bridge with exact two-variable certificate, plus a separate analytical SLD spectral gate | audits/TWO_QUBIT_CORE_STABILITY.md |
| Exact local-orbit minimum of two-qubit rank-two subspace coupling, with sharp universal floor 7/8 | Derived and independently checked for all complex subspaces; canonical coordinates and compression maps are prior Niu–Griffiths ingredients | audits/SHARP_SUBSPACE_AND_FLAT_CORE.md Section 1 |
| Sharp subspace anisotropy bound with coefficient 2/sqrt(3) | Derived and independently checked with exact attainer; compares average coupling and its state dependence | audits/SHARP_SUBSPACE_AND_FLAT_CORE.md Section 1.3 |
| Sharp seed entropy bound for every two-qubit state with lambda_1=lambda_2 | Derived and independently checked; arbitrary complex eigenvectors and remaining spectrum, one scalar polynomial majorant and existing gates | audits/SHARP_SUBSPACE_AND_FLAT_CORE.md Section 2 |
| Coherent core/tail trace-norm bound | Elementary triangle-inequality consequence; preserves the exact zero-tail score, including singular compressions. Not proposed as novel | audits/COHERENT_TRANSFER_AUDIT.md Section 2 |
| Three stronger quadratic decoder-deficit shortcuts | Incorrect; one exact physical m=1/4 core and rational decoder reflections refute all three. No entropy counterexample | audits/COHERENT_TRANSFER_AUDIT.md Section 4 |
| Finite support-function target for unequal-core transfer | Unresolved; a proof on t<=1/sqrt(7), m>=1/5 would close n=2. Conditional entropy implication checked using the tail's actual entropy | audits/COHERENT_TRANSFER_AUDIT.md Section 3 |
| g_n<=n sqrt(2+8q(1-q)) for all states commuting with product parity of weight q | Sharp direct specialization of prior fidelity theory, independently checked; uniform parity blocks attain every individual local-query bound | audits/PARITY_READOUT_BOUND.md Section 1 |
| Two-qubit entropy bound when a top-two spectral projector is a local product-parity sector | Derived and independently checked; unequal coherent cores allowed, residual-strip margin >1/16. Does not include every parity-commuting state | audits/PARITY_READOUT_BOUND.md Section 2 |
| Coherent-transfer target on parity supports | Proved with the sharp envelope S_t<=2sqrt(2+2t^2) for 0<=t<=1, arbitrary core/tail spectra and coherences | audits/PARITY_READOUT_BOUND.md Section 3 |
| Exact mixed-decoder operator envelope, with maximum below sqrt(21/2) | Derived and independently checked; improves decoder classification only. A short prior-method corollary gives 13/4 without a characteristic polynomial | audits/MIXED_DECODER_PATTERN_BOUND.md; audits/EXTENDED_CORE_TRANSFER.md Section 2 |
| Entropy bound for core score >13/4 and tail weight <=1/99 | Earlier partial result, derived and independently checked; stronger angle inequality and 97 exact intervals. Entirely elementary through <=1/201; extended by the next row | audits/EXTENDED_CORE_TRANSFER.md |
| Entropy bound for top-two core score >13/4 and tail weight <=1/29 | Derived and independently checked; finite paired scalar-query gain plus imbalanced SLD certificate, 5,324 exact leaves. Generic lower-score cores remain unresolved | audits/CURVED_CORE_TRANSFER.md |
| Squared fixed-core/tail transfer sum is concave in squared tail parameter | Derived and independently checked for arbitrary complex 2x2 blocks; finite tangents at positive parameter, sharp product-support envelope. No uniform arbitrary-state envelope | audits/FINITE_TAIL_STRUCTURE.md |
| Nakahira–Usuda 2012 full weighted rank theorem under the natural Hamming reduction | Completed scoped comparison: best certificate has rank two, so it does not directly subsume the supplied rank-one projectivity theorem. Other reductions and exhaustive originality remain open | audits/BAYES_RANK_PRIOR_COMPARISON.md |
| Tomassoli 2024/25 two-correlator thesis | Full text read; scalar calibrated concurrence boundary and axis family are prior. Exact calibrated lift G differs from optimized-readout C, with a rational separator. Ordinary-negativity normalization repaired; specified source gap closed, exhaustive novelty open | audits/TOMASSOLI_FULL_TEXT_COMPARISON.md |
| Quantitative stability of one-qubit maximizing seeds | Derived and independently checked; dimension-independent normalized-seed bounds and specified branch-weighted consequences | ONE_QUBIT_STABILITY.md |
| Full noisy-X/Z average-rank profile D_M=W=w | Exact specialization of Cope–Uola SDPs; the already proved C-versus-w phase boundary supplies its full entropy comparison | audits/ROOF_PROVENANCE_AND_JOINT_SCORE.md Section 3 |
| Collective readout can improve joint score per copy of a product seed | Incorrect: product additivity follows from Wallden–Dunjko–Andersson Theorem 3; an explicit f_2-j_2=(sqrt(2)-1)/8 gap persists under powers | audits/ROOF_PROVENANCE_AND_JOINT_SCORE.md Section 4 |
| Complete all-state two-qubit joint entropy inequality | Unresolved; an exact one-effect formula is proved, with the singular-state dual handled on its support | audits/ROOF_PROVENANCE_AND_JOINT_SCORE.md Section 5 |
| Minimum E_F from two correlations for two qubits, with one trusted X/Z pair | E_2=gamma, a direct specialization of prior Verstraete–Wolf Theorem 1; general binary POVMs included | audits/TWO_CORRELATION_FORMATION.md Section 2.1 |
| Same two-correlation minimum with larger untrusted dimension | E_d=C for every d>=3, attained by one fixed qutrit pair; strict E_2>E_3 outside the disk when both contrasts are below one. Flags are counted in this separate realization problem | audits/TWO_CORRELATION_FORMATION.md Section 2 |
| Every minimum-formation realization outside the disk with both contrasts below one has orthogonal classical and entangled sectors | Derived and independently checked equality theorem; all qutrit optima classified, with four possible classical signs and one entangled-block marginal parameter | audits/FORMATION_OPTIMIZERS_AND_PRIOR.md Section 2 |
| Ordinary negativity minimum from the full two-correlation profile | N_min=w/2, supplied weighted proof; equal-weight line and flagged construction are prior. This is a separate realization resource, not retained memory | audits/RESOURCE_OPTIMA_AND_JOINT_DECODERS.md Section 1 |
| Minimum E_F among minimum-negativity realizations in the noisy nonclassical interior | Exactly w, so C<w implies incompatible resource minimizers; exact axes have a distinct jointly optimal partially entangled realization | audits/RESOURCE_OPTIMA_AND_JOINT_DECODERS.md Section 2 |
| Complete E_F versus ordinary-negativity budget frontier at fixed X/Z data | Derived and independently checked for arbitrary finite Alice dimension; all scalar prices, explicit phase boundary, unique scalar root and qutrit attainment. Auxiliary state resources, not interface memory | audits/JOINT_RESOURCE_FRONTIER.md Sections 2–4 |
| Real matrices suffice for the unrestricted asymptotic interface rate | Derived from established realification: at most one extra retained qubit, arbitrary complex input and uniform error preserved. All-size real and complex entropy conjectures are equivalent; fixed-n reduction is not asserted | audits/JOINT_RESOURCE_FRONTIER.md Section 6 |
| Two-input joint optimal decoder structure for arbitrary states | Every full-rank optimum is a rank-one PVM; singular states admit an optimal ambient PVM with possibly nonprojective support compression. One-effect maximum can be restricted to ambient rank-two projections | audits/RESOURCE_OPTIMA_AND_JOINT_DECODERS.md Section 4 |
| Complete weighted guessing and the central-phase product-plus-Bell qutrit construction | Established ingredients in Han et al. 2111.02800v2 Theorems 1–2 and Eqs. (S49)–(S50); the prior pure support leads directly into the project's entropy convexification | audits/FORMATION_OPTIMIZERS_AND_PRIOR.md Section 1 |
| Minimum convex-roof concurrence from the two data equals w | Exact specialization of Han et al.'s whole weighted family; C>f(w) exactly outside the disk with both contrasts below one | audits/FORMATION_OPTIMIZERS_AND_PRIOR.md Section 1.1 |
| Universal four-context operator cover is equivalent to the all-state two-input joint entropy bound | Derived and independently checked SDP/entropy application; failed cover yields an admissible violating state. Universal feasibility and any failed instance remain unresolved | audits/FORMATION_OPTIMIZERS_AND_PRIOR.md Section 3 |
| Full X/Z probability table certifies C without trusting either party | Incorrect with unrestricted dimensions: an explicit local model reproduces the entire table at every profile | audits/TWO_CORRELATION_FORMATION.md Section 4 |
| Exact priors and total Holevo information suffice for the sharp joint entropy line | Incorrect relaxation: exact classical channels exceed the line at every interior subset equality seed; those channels are not measurements of its filtered ensemble | audits/ENTROPY_PROOF_RELAXATIONS.md Section 2 |
| Complete rank-two spectral bounds and norm four imply the all-state entropy-energy inequality | Incorrect relaxation, even with zero partial traces; explicit violating Hamiltonian contains forbidden trusted Pauli terms and is not a QIC counterexample | audits/ENTROPY_PROOF_RELAXATIONS.md Section 3 |
| General sharp intermediate common-accuracy rate or common-accuracy collective advantage | Unresolved | Note Section 8 |
| Exponential many-copy estimation speedup | Not claimed; easy classical control rules out that narrative here | Note Section 9 |

## What changed after the audit

The commit-pinned [audit](audits/PROOF_AND_NOVELTY_AUDIT.md) reviewed bootstrap
commit `eaf085a8cb299e6b297b11d2dc3c85e24f02779e`. Its historical verdicts are
preserved. It found no error in the repository's supplied baseline proofs,
but identified earlier subsumption of the exact endpoint, a direct equivalent
discrimination problem, strict obstructions to importing reconstruction or
full-outcome converses, and two source-proof caveats.

Subsequent analytical work settles the former `(n,q)=(2,1)` diagnostic and
extends it to every n at q=1. The proof requires Cheng–Hall's independently
optimized common-qubit settings; a weaker common-setting CHSH statement would
not suffice. Rigidity describes refined branch maps, without assuming that
the retained site's choice is independent of the physical input.

The product-diagonal entropy argument excludes correlated diagonal spectra
and all local basis rotations as a route beyond the subset benchmark. It
does not restrict the original operational model or cover every separable
Gram matrix. Both new proofs were independently checked within the workspace.
The 43 one-qubit and 10 product-diagonal diagnostics support specific matrix
identities; the proofs carry the general claims.

The further entropy-rate characterization converts asymptotic rank into a
regularized entropy minimum using virtual Schmidt truncation and complete
seed orbits. Midpoint convexity supplies the continuity needed to remove
contrast slack. This proof was independently checked as well. A violation
of the unrestricted seed entropy bound is now a sufficient certificate of
an asymptotic collective advantage; no such violation has been established.

## Further converse and exclusions

The subsequent continuation derives an explicit unrestricted lower bound
from Beigi's improved quantum logarithmic-Sobolev theorem. For example, at
eta=0.8 it raises the necessary memory fraction from 0.06200881 to
0.14144054; the achievable subset fraction remains 0.31715729. Near the
classical threshold its coefficient scales as `4 t^2 log_2(1/t)+O(t^2)`
for contrast advantage t. This is a task-specific consequence of prior
functional inequalities, not new logarithmic-Sobolev mathematics.

The exact rank-two spectrum envelope now excludes every rank-two Gram matrix
from witnessing an entropy-based rate advantage. Further analytical exclusions
cover arbitrary spectra in stabilizer eigenbases, flat rank-three two-input
states, and a family of flat half-rank projectors extending beyond fixed
product-diagonal bases. The notes supply proofs and preserve their family
conditions explicitly.

## Latest structural deductions

Every flat half-rank seed on n<=4 inputs has score at most
`2(n-1)+sqrt(2)`, with equality precisely for one pure bisector projector
tensor the identity. The proof also applies for arbitrary n when the
singleton X/Z projection of the reflection occupies at most four sites;
higher-order Pauli terms are unrestricted. Separate flat-rank estimates
exclude every lower allowed rank from improving the q=n-1 finite-budget
score at these sizes. They do not establish the sharper entropy inequality
at every lower rank. The [source comparison](FLAT_SEED_PRIOR_COMPARISON.md)
distinguishes the result from prior Poincare/FKN statements and records a
later repair of a prior FKN proof step.

Local classical flags extend the entropy exclusion beyond fixed product
eigenbases. Two-input states with both marginals maximally mixed are also
excluded, as are all full-rank states with the stated bounded condition
number. These are conditions on candidate Gram matrices, not constraints
on admissible physical encoders. The spectral condition supplies no new
unrestricted rate lower bound. All four proofs have been independently
reconstructed within the workspace; publication novelty remains unresolved.

## Nonuniform support and spectral-tail deductions

The support-inertia converse is independent of a seed's nonzero eigenvalues.
If both compressed queries are indefinite at only a(P) sites, its score is
at most `sqrt(2)n+(2-sqrt(2))a(P)`. Within a(P)<=q, equality at the
q-qubit subset score forces the usual flat subset seed. A geometric
corollary excludes every spectrum on a support P with
`||(I-P0)P||_infty<=sin(pi/8)`, where P0 is any rank-2^q subset support.
The radius is sharp for the semidefinite-compression criterion; this does
not assert that collective advantage begins outside that radius.

An orthogonal block trace-norm estimate also controls higher-rank spectral
tails. At each fixed n, the entropy inequality holds throughout an open
neighborhood of every rank-at-most-two seed, and is strict there above
rank two. Compactness gives an existential positive lower bound on a
witness's third eigenvalue. There is no numerical uniform cutoff or
dimension-independent neighborhood claim. For an exact subset core and an
arbitrary orthogonal tail of weight epsilon, the excess score over the
weighted component scores is at most `2sqrt(2)epsilon`, with a first-order
sharp coefficient. This supplies additional explicit, conservative entropy
cutoffs without assuming anything about the tail eigenvectors.

Uniformization cannot bridge the remaining gap: on a particular rank-four
three-input support the exact optimum is `3sqrt(3)`, attained at nonuniform
weights and strictly above the flat state on that same support. It remains
below `4+sqrt(2)`. A separate rank-three two-input example beats the maximum
over all flat rank-three states. Neither example violates the entropy
conjecture. The SLD-route audit refutes two local proof steps and checks five
primary sources at the theorem level; its proposed global inequality remains
unproved. These are supplied deductions and scoped source comparisons, not
publication-novelty certification. All analytical deductions were independently
reconstructed within this workspace. Sixteen deterministic matrix diagnostics
also pass, with an exact independent rerun.

## Complete accuracy region and further spectral exclusions

The latest continuation evaluates the complete accuracy region when one
qubit may cross the interface. For the existing local queries with separate
contrasts, put `w(x,z)=[x+z-1-sqrt(2(1-x)(1-z))]_+`. Feasibility is
exactly `sum_i w(eta_(i,X),eta_(i,Z))<=1`. Each local w is an established
incompatibility weight. The supplied global budget is a weighted-monogamy
and convexity deduction, with a constructive mixture retaining at most
one input site. It refines the original uniform theorem and preserves
uniformity over arbitrary states for each query. It does not characterize
every physical encoder or settle memory dimensions greater than two.

New spectral optimizations prove the entropy bound for every two-qubit
state with at most two distinct eigenvalues, including zero in that count.
One of the two spectral theorems holds at every n for a single distinguished
eigenvalue and a repeated complementary value. The kernel converse supplies
additional all-eigenbasis certificates for nonuniform rank three and rules
out all two-qubit seeds with a maximally entangled vector in their kernel.
These are proved families; the unrestricted entropy inequality remains open.

The calibration obstruction shows why the existing monogamous entanglement
argument cannot simply be sharpened to a linear charge matching the subset
line. The SLD analysis now has an exact unrestricted integral and graph
formulation, but a graph with only the necessary elementary constraints
can fail the target and need not come from any quantum eigenbasis. Further
primary-source comparisons distinguish prior incompatibility theory, biased
random-access coding, matrix-entropy defects, and different triangular
discriminations. Publication novelty remains unresolved.

All 14 deterministic allocation, spectral, kernel, and obstruction diagnostics
pass with matrix dimension at most eight; an independent rerun exactly
reproduces the recorded JSON. Proof reconstruction and numerical evidence
are recorded separately in [REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## Unequal-accuracy separation, SLD minimum, and stability

The [exact-axis theorem](EXACT_AXIS_SPECTRAL_REDUCTION.md) reconstructs
the whole operational boundary when all X queries are exact. Every refined
Gram matrix must commute with every X_i, so its support is an induced
Boolean-cube subgraph in the product X basis. The maximum common Z contrast
is exactly its best adjacency spectral radius divided by n, optimized over
supports of size at most D. A complete translation instrument proves
achievability; its normalization is not postselected.

For the original-site-retention comparison class defined in that note,
the complete region is `sum_i w(x_i,z_i)<=q`. It permits input-dependent
branch probabilities, joint measurements of discarded sites, and arbitrary
processing on retained sites, while fixing the branch factorization that
defines this class. A collective star construction at n=31,D=32 has
`x_i=1,z_i=1/sqrt(31)` and strictly violates the region. Reducing X contrast
to `9999/10000` preserves the separation, with total weight about
5.167575>5. The proof uses exact inequalities; this decimal is illustrative.
The common-accuracy target and its entropy conjecture are not refuted.

The graph optimization, star spectrum, local compatibility disk and local
weight are prior ingredients. Combining the reduction with
Bollobás–Lee–Letzter's established theorem gives an exact operational value
`sqrt(D-1)/n` for `105<=D<=n`. The final author version uses 105; the earlier
arXiv v1 uses 103. The stated common range avoids relying on the difference.
The n=31,D=32 example falls outside that theorem's range and is not claimed
optimal. Other inspected partial-compatibility and distributed-sampling
frameworks are distinguished at the theorem level in the proof note.

The [two-qubit spectral theorem](TWO_QUBIT_SLD_SPECTRUM.md) evaluates
both the three-Pauli half-sum and X/Z SLD minimum at every spectrum as
`k_12+k_13+k_24+k_34`. It supplies the complete two-qubit proof of
`I_XZ>=2-S`. Spin flip, universal inversion and the kernel crossing
inequality are established ingredients. The resulting square-root score
bound does not close the sharp linear seed entropy conjecture or imply
an all-n SLD inequality.

The [spectral-tail continuation](audits/TWO_QUBIT_SPECTRAL_TAIL_GATE.md)
now extracts the sharp linear entropy bound from the full spectral envelope
whenever `lambda_3+lambda_4>=1/29`, with no eigenbasis restriction. An exact
rational certificate verifies 400 interval enclosures after a supplied
analytical reduction; it is not a sample of states. Any two-qubit witness
must be within trace distance less than `1/29` of its normalized top-two
truncation. The earlier entropy-valid low-rank neighborhood has an
existential uniform radius; no overlap reaching `1/29` has been proved.

The [core-stability continuation](audits/TWO_QUBIT_CORE_STABILITY.md)
now proves a uniform radius `2^-20` for n=2, strictly entropy-valid for
positive tail weight. Its high-score branch covers every normalized
rank-two core with score above `10/3` through tail weight `1/29`, without
assuming flat eigenvalues or aligned supports. A separate analytical gate
covers every core with smaller normalized eigenvalue at most `1/5`.
The remaining low-score cores have entropy defect greater than `1/100`;
a cross-block trace-norm bound then supplies the explicit small-tail radius.
The scalar interval certificate covers 755 closed boxes, with exact outward
arithmetic and no sampled-state inference. No full two-qubit closure follows.

The [stability theorem](ONE_QUBIT_STABILITY.md) proves that deficit
delta<=1/48 from the one-qubit optimum implies squared overlap at least
1-2delta/3 with an exact subset seed, and squared Frobenius distance at
most 4delta/3 after phase alignment. The single global spectral gap avoids
an error proportional to the number of discarded sites. Its instrument
consequence uses normalized Kraus weights, which are outcome probabilities
for the maximally mixed input; it does not assert all-input channel
proximity or completeness after replacing individual branches.

All three proofs were independently reconstructed within this workspace.
The reconstructed 13 deterministic diagnostics pass with maximum matrix
dimension 32. The 31-input example checks only its support graph and scalar
arithmetic. No full 31-qubit matrix or instrument is enumerated.
See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for actual residuals and scope.
These checks do not certify the universal proofs or publication novelty.

## Linear onset and exact-axis rate

The new [asymmetric entropy converse](ASYMMETRIC_ENTROPIC_CONVERSE.md)
applies to all collective encoders. Define
`f(c)=h_2((1-sqrt(1-c^2))/2)` and
`kappa(x,z)=max{0,f(z)-h_2((1-x)/2),f(x)-h_2((1-z)/2)}`.
Every profile requires `log_2D>=sum_i kappa(x_i,z_i)`. Its proof connects
a normalized seed's X-basis column ensemble to established arbitrary-prior
quantum random-access bounds and a classical cube-entropy inequality.
The normalized Kraus average retains the branchwise dimension cap.

For the original common-accuracy problem, this gives
`R(eta)>=ell(eta)=[f(eta)-h_2((1-eta)/2)]_+`. At eta=.8 the lower
fraction rises from .14144054 to .25293250, while the subset upper fraction
is .31715729. Convexity proves
`2log_2(1+sqrt(2))t<=R(eta_0+t)<=(2+sqrt(2))t`, and hence linear onset
as t decreases to zero. This resolves the onset order, not its exact
coefficient or the complete rate. The earlier logarithmic-Sobolev bound
is retained because it is stronger extremely close to eta=1.

The state version yields the unrestricted bound
`g(L)<=sqrt(2)n+S(L^dagger L)/log_2(1+sqrt(2))`. Its entropy coefficient
.78643970 exceeds the desired .58578644, so the sharp entropy conjecture
and the n=3,q=2 diagnostic remain open.

The [exact-axis rate](EXACT_AXIS_RATE.md) is now completely evaluated:
`R_X(z)=f(z)`. The finite heterogeneous converse is
`log_2D>=sum_i f(z_i)`. Explicit auxiliary Bernoulli distributions truncated
to Hamming balls give complete instruments with exact X at every block size,
worst-case dimension and uniform Z operator identities. No physical input
is postselected or assumed to be a product state. For every 0<z<1,
`f(z)<z`, so collective encoding beats the entire defined original-site
retention class asymptotically. At x=.99,z=.5, rate at most .354579 beats
that class's exact .39 with fixed nonzero errors on both axes.

The source audit identifies substantial prior overlap. Samorodnitsky's
Theorems 1.2 and 1.4 supply the classical curve and graph asymptotics;
Wilde's dephasing-channel cost is the same formula for a stronger
reconstruction requirement. Wehner–Christandl–Doherty's Lemma I.1 and
Corollary I.2 already supply the arbitrary-prior decoding entropy penalty.
The supplied contributions are operational deductions with complete
resource/error maps; publication novelty remains unresolved. The original
common-accuracy optimum is not imported from channel reconstruction.

Both new proofs passed independent reconstruction within this workspace.
Finite deterministic diagnostics separately check the entropy chains,
complete small translation instruments and scalar bounds. They do not
certify the asymptotic theorem or novelty. Actual runs and scope are in
[REPRODUCIBILITY.md](REPRODUCIBILITY.md).

## Product-diagonal profile rate and sharper source map

The [profile theorem](PRODUCT_DIAGONAL_PROFILE_RATE.md) evaluates a complete
two-parameter benchmark C(x,z). It is the lower convex monotone envelope of
zero-cost compatible profiles and the exact-axis curves of cost f(v).
Its operational class consists of protocols with an individually refined
Kraus representation whose every Gram matrix is diagonal in some tensor
product of local bases. Local axes may depend on the branch; eigenvalues
may be nonuniform and arbitrarily correlated. This class is explicitly
scoped inside the unrestricted original model.

The proof gives `S(rho)>=sum_i C(F_i^X,F_i^Z)` for every such Gram matrix.
Worst-case dimension bounds follow on each branch before averaging. Conversely,
deterministic block allocation, complete seed instruments and permutation
equalization achieve C with a cap on every branch. This does not replace
worst-case memory by a randomized average.

For `0<z<=x<1` outside the compatibility disk, C is strictly below the
retention cost exactly when `(1-x)/(1-z)<2(1/ln2-1)^2`, approximately
0.39195780. Equality belongs to the retention-optimal side. The opposite
half-square follows by swapping X and Z; the disk is free and the exact
axes are handled separately. On x=z, C is exactly the subset rate. Thus no
correlated product-diagonal construction improves the common-accuracy line.

At x=.99,z=.5, an explicit rational mixture achieves rate
`(87/100)f(15/29)=.3250660206...`, improving the previous .35457890
upper bound. The unrestricted lower bound remains .30916421 and retention
costs .39. The unrestricted interior optimum is still open.

The [new source audit](ENTROPY_TRADEOFF_PRIOR_AUDIT.md) gives an exact
identification with Cope's established steering entanglement of formation,
plus a second derivation of the prior asymmetric seed bound using established
entropy-of-mixture and coherence inequalities. The result is an explicit
evaluation and operational deduction, not a new entropy resource. It does
not identify complete-assemblage entanglement cost with the delayed-query
rate. Prior subsumption of the full evaluated profile remains unresolved.

## Research division and next target

The [optimizer follow-up](audits/FORMATION_OPTIMIZERS_AND_PRIOR.md)
strengthens the one-site equality result: every entropy optimum in the
noisy nonclassical interior has orthogonal classical and entangled
sectors, and all qutrit optima have an explicit form. This does not
assert uniqueness of encoders. It further narrows provenance: Han et al.
already supply the weighted pure guessing geometry and a product-plus-Bell
qutrit realization. Their full mixed-concurrence family gives w; scalar
conversion gives f(w), strictly below C in that interior. The remaining
candidate is the complete entropy evaluation and its specific operational
deductions. The collective entropy inequality remains unproved.

The same report gives an exact operator-covering equivalent for the
weaker two-input joint entropy inequality. Its SDP retains the common
state across contexts, has an attained dual, and detects singular
violating seeds through positive-definite entropy potentials. This is
an admissible certificate target, not a solution of its outer universal
quantifier or a new general duality method.

The [two-correlation audit](audits/TWO_CORRELATION_FORMATION.md) sharpens
both the exact result and its provenance. For a trusted qubit with only
two specified correlations, the minimum formation entanglement is the
raw gamma for a qubit partner and C for a qutrit or any larger partner.
One fixed qutrit readout pair attains the whole profile; the minimum
dimension attaining C is one on the disk, two on nonclassical exact axes
and three elsewhere outside the disk. These dimensions count flags,
unlike the original quantum memory cap. The raw qubit result is a direct
specialization of Verstraete–Wolf, and Zhu–Zhang–Ma already exhibit the
qualitative higher-dimension flag advantage. The complete two-parameter
evaluation remains the candidate contribution, not either prior ingredient.
The user supplied the close 2024/25 Padua thesis by Tomassoli. Its
[full-text comparison](audits/TOMASSOLI_FULL_TEXT_COMPARISON.md) now
distinguishes its calibrated two-qubit problem from C, even after the
strongest two-parameter/weighted extension. Its scalar boundary and
axis family are prior; no exhaustive originality conclusion follows.

The companion [proof-method note](audits/ENTROPY_PROOF_RELAXATIONS.md)
supplies two exact obstructions to global approaches: a total Holevo budget
loses the filtered signals' information allocation, and interpolation of
rank-two bounds loses the allowed trusted Pauli structure. Both relaxed
problems violate the desired sharp line. Neither construction belongs to
the genuine problem, so no all-state proof, admissible counterexample or
unrestricted optimum results. This is an exact account of failed methods,
not further family testing offered as evidence of optimality.

The [roof provenance and joint-score audit](audits/ROOF_PROVENANCE_AND_JOINT_SCORE.md)
identifies actual prior subsumption: Vollbrecht–Werner Eqs. (38)–(42) supply
the symmetry/roof reduction and abstract fixed-block dichotomy. Specific
orbit coordinates and the evaluated profile remain supplied applications.
The full Cope–Uola average-rank measurement profile equals w, so the
existing phase boundary also gives its exact comparison with C. An affine
identification with the inspected OO-invariant state family is impossible
because the zero sets have different geometry; nonlinear subsumption is
not excluded. None of these statements certifies historical originality.

For the entropy problem, joint scores are additive on product seeds by
Wallden–Dunjko–Andersson's prior Bayesian decision theorem. An exact
rank-two seed has a strict local/joint score gap that persists under every
tensor power, while satisfying both entropy bounds. A new exact
one-effect formula for each two-qubit joint context leaves the outer
entropy optimization unresolved. Context averaging cannot be exchanged
with a concave roof, and the earlier deficit-superadditivity obstruction
also survives joint decoding. These are specific blocked routes, not
counterexamples to the unrestricted conjecture.

The [tensor-formation continuation](audits/TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md)
proves an exact finite task separation. For two input qubits at
`eta_*=(1+1/sqrt(2))/2`, a delayed local query needs retained dimension two,
whereas the full product query needs dimension three. One-qubit rigidity
forces a deficient parity moment in every dimension-two branch; an explicit
sixteen-branch qutrit instrument gives the matching upper bound. Compactness
extends the separation to some interval immediately below eta_*, without
an explicit width. This is a worst-case dimension result, not a strict
separation of formation entropies A_n and B_n.

The same report reduces B_n exactly to n moments and at most n+1 seed
orbits. At each fixed n, additivity at one interior contrast forces
additivity throughout the interval; any violation of the corresponding
joint-decoder entropy bound yields savings at every interior contrast,
using an explicit simplex compensation. The joint score j_n is at most
the local score f_n. Neither entropy inequality has been proved generally.

The fixed qubit-output channel completion is evaluated exactly as
`G(x,z)=f([x+z-1]_+)`. It equals C only on x+z<=1 or an exact axis; it is
strictly larger everywhere else. This rules out that complete proposed
reduction to known channel formulas, while crediting the prior distinction
between reconstruction and arbitrary readout. It is not an exhaustive
originality verdict. These deductions passed independent internal proof
reconstruction; no matrix search was used.

The [latest source comparison](audits/PROFILE_NOVELTY_AND_STEERING_REDUCTION.md)
turns two open comparisons into exact statements. The full asymmetric C
strictly exceeds the complete optimized affine weighted-CHSH certificate
family in Zhu–Zhang–Ma Theorem 2. Cope's numerical family fixes one exact
measurement and cannot be identified with the two-noise square by the
stated rank-preserving transformations; its qualitative mixing mechanism
is nevertheless prior. Tóth–Moroder–Gühne's steering optimization uses
linear entropy, and a proved flag obstruction rules out the naive scalar
conversion to the formation-entropy answer. These comparisons support a
specific analytic contribution, not an exhaustive originality claim.

The unrestricted problem is now exactly regularized formation of the
local-query assemblage L_n, with 2n binary settings. Full product
assemblages demand complete setting/outcome tuples. A two-input seed
shows why optimized branches need not extend to that larger task. The
chain nR<=A_n<=B_n<=nC_eta specifies the missing equality and a possible
certified-nonadditivity route to refutation. Neither equality nor strict
separation of these entropy costs has been established. These deductions passed independent
internal proof review; no new matrix search was used.

The bounded two-qubit attempt after PR #12 did not prove the proposed
fixed-spectrum envelope, close the entropy inequality, or produce a
certified violating seed. Direct stationarity and exterior-square routes
give reformulations but no complete global estimate. Small exploratory
4-by-4 searches found no violation; this negative outcome is not a proof
and is not added to the theorem ledger. Numerical expansion was stopped.
Neither the adjacent-Schmidt-pair CHSH construction nor a quadratic SLD
bound was imported as a sharp joint trace-norm theorem.

Following the assessment's stopping criterion, work returned to the
complete profile evaluation. Section 5.1 now constructs its optimizer
through a unique scalar root and proves uniqueness of the reduced
generating profiles. The full strict-saving region is covered, not an
additional exceptional seed family. The explicit point `(.99,.5)` is
certified with rational intervals, giving `C approximately 0.324848239186`; this is
the exact restricted rate and an unrestricted upper bound. The proof had
three independent within-workspace reconstructions; the certificate had
an independent byte-identical rerun. These are internal checks, not
external peer review or novelty certification.

Issue #1 records the proof-and-novelty audit. Issue #2 coordinates the
unrestricted finite-block/rate investigation. The user subsequently authorized
continued research and merging; audit PR #3 was integrated under that explicit
authorization. Research changes still use a separate branch and pull request.
The original repository contained only LICENSE at
`310a0730a04ada47eeda41bada41412414442ee1`.

The smallest unresolved block is now `n=3,q=2`: prove
`Gamma(3,4)<=4+sqrt(2)` or construct a violating seed. Every allowed flat
seed is now excluded from improving this finite-budget score. A witness
must have rank three or four with nonuniform nonzero eigenvalues, outside
the product-diagonal family. Every one of its six query compressions must
be indefinite, and its support must lie outside the stated neighborhood
of every subset support. A separate Ky Fan refinement also proves the
sharper entropy inequality for every flat rank-three three-input state. The one-qubit
CHSH argument cannot be extended by treating a four-dimensional memory as
one qubit: two Bell pairs explicitly violate its key pair bound.
The all-contrast asymptotic subset-rate conjecture is equivalent to the seed
entropy inequality holding for every Gram matrix, including entangled
eigenbases. The established entropy formula does not itself evaluate the rate.

The smallest possible entropy witness is a two-input state of rank three
with nonuniform nonzero eigenvalues; general full-rank two-input states also
remain open. Such a witness must be nonclassical on both sites, must not
have both marginals maximally mixed, and, if full rank, must have condition
number greater than 6.235819648070267. It must additionally stay outside
the proved open neighborhood of the rank-at-most-two set at that fixed n.
It must fail the new spectral and kernel certificates; in particular,
a two-input witness must have `2^-20<lambda_3+lambda_4<1/29`, normalized
second core eigenvalue `1/5<lambda_2/(lambda_1+lambda_2)<1/2`, and normalized
top-two core score at most `13/4`, using the later
[finite-tail theorem](audits/CURVED_CORE_TRANSFER.md). In particular, its largest two
eigenvalues sum to more than `28/29`. Also,
a two-input witness cannot have a maximally entangled kernel vector or
at most two distinct eigenvalues. The example `(t,b,b,0)` generally has
three distinct eigenvalues and is not removed as a whole by that count.
This is distinct from the n=3,q=2 finite-budget diagnostic:
regularization can turn entropy below log(rank) into an asymptotic memory
saving. No entropy witness or collective advantage for the original
common-accuracy target has been found. The unequal-accuracy separation
above is a distinct, proved operational result.

## Simple subspace theorem and flat-core closure

The [subspace continuation](audits/SHARP_SUBSPACE_AND_FLAT_CORE.md) gives
an exact minimum over local query-frame orientations for every rank-two
support orbit, and sharp universal constants `7/8` and `2/sqrt(3)` for its
coupling operator. The proof uses canonical two-qubit compression and
scalar squares; Niu–Griffiths supplies the prior canonical machinery.
A single polynomial majorant then closes the entire `lambda_1=lambda_2`
face of the two-qubit entropy problem without interval partitions.

The proof does not uniformize arbitrary cores. Even a product core with
spectrum `(7/10,3/10)` has actual score below `10/3` while querywise CS
pinching raises it to `2+sqrt(2)`. This lost coherence is the explicit
obstruction to carrying over the flat-core moment cap. Section 3 states
one sufficient coefficient-3 interpolation inequality whose proof would
close n=2; it is clearly labeled conjectural. The full all-n entropy
conjecture and publication originality remain unresolved.

## Publication gate

The [curved-transfer theorem](audits/CURVED_CORE_TRANSFER.md) extends
the preceding `13/4` gate through the full tail interval `epsilon<=1/29`.
Its key improvements are a paired, finite scalar-query gain and an SLD
bound retaining the active/inactive score imbalance. An exact four-variable
certificate covers 5,324 closed leaves after the analytical reduction.
The numerical cutoffs remain sufficient rather than optimal. The separate
[matrix report](audits/FINITE_TAIL_STRUCTURE.md) proves squared concavity
and a sharp product-support envelope; these alone are no new entropy
exclusion. Neither result closes the generic low-score or all-n problems.

The [extended-core continuation](audits/EXTENDED_CORE_TRANSFER.md) supplies
a shorter decoder bound using three anticommuting sets and a genuinely
larger entropy-valid region: `g(sigma)>13/4`, `epsilon<=1/99`.
The decisive analytical improvement removes an unnecessary `1-u` factor
from the coupled principal-angle estimate. The entirely elementary proof
covers `epsilon<=1/201`; the sharper cutoff uses 97 exact scalar intervals.
The source audit credits Kurzyński et al., 1010.2012v2 Eq. (1), for the
anticommutation principle and grouping method. No priority claim follows.
Its formerly unhandled tails between `1/99` and `1/29` are now covered
by the curved-transfer theorem above; low-score cores and the all-n
problem remain unresolved.

The [parity continuation](audits/PARITY_READOUT_BOUND.md) supplies a short
all-size score theorem from a binary symmetry witness and prior fidelity
theory. It closes the full two-qubit family whose leading spectral
subspace is a parity sector, including unequal complex cores. Any remaining
witness must also avoid that support class. The exact
[mixed-decoder envelope](audits/MIXED_DECODER_PATTERN_BOUND.md) improves
the classification constant but by itself does not lower the certified
high-score tail threshold. The later partial extension is stated above.
Neither parity nor decoder classification establishes the general transfer
bound. The first is an elementary prior-theorem specialization; originality
of the auxiliary operator evaluation has not been established.

The [coherent-transfer audit](audits/COHERENT_TRANSFER_AUDIT.md) supplies
a two-line block bound that retains within-core coherence. It also keeps
the tail's score and entropy paired, avoiding an unnecessary loss in the
sufficient interpolation bound. One exact physical example rules out three
stronger decoder-deficit shortcuts. The resulting finite-parameter target
is still unproved; local numerical screening is not a certificate. This
continuation does not enlarge the proved entropy-valid family. A new
same-support comparison with Holevo–Shirokov Proposition 1 supplies only
a scalar entropy estimate, not the missing four-query score control.

The [continuation pinned to PR #19](audits/JOINT_RESOURCE_FRONTIER.md)
evaluates the full conditional E_F/ordinary-negativity frontier. Its
mixed-state support bound is essential: the pure convex roof of
f(c)+lambda c involves concurrence, not ordinary negativity. The explicit
frontier and phase calculation are supplied evaluations. The
[nonlinear-source follow-up](audits/NONLINEAR_CHSH_SUBSUMPTION.md) now
identifies the mixed-state support and full abstract convex-hull
characterization as short prior corollaries, including standard block
reduction and flags. This narrows the candidate novelty; a complete prior
subsumption audit is still needed. Both the
[Tomassoli full-text comparison](audits/TOMASSOLI_FULL_TEXT_COMPARISON.md)
and the [2012 Nakahira–Usuda comparison](audits/BAYES_RANK_PRIOR_COMPARISON.md)
are now completed. The latter's whole weighted rank-certificate family gives only
rank two for the natural Hamming ensemble. No all-state entropy proof or
admissible equal-accuracy violating seed was obtained in this continuation.

The goal remains a publishable, analytically led theorem with a clear novelty
case. These are task-specific deductions; neither familiar monogamy nor a
restricted-family entropy inequality should be presented as a new general
framework. Complete the closest comparisons for the new results and determine
whether a broader sharp theorem or useful separation is available before
making a publication claim. The existing primary-source audit is targeted,
not a proof of absence from the literature.

Preserve one unknown specimen, one delayed query, arbitrary collective
encoding, unlimited finite classical records, worst-case quantum dimension,
and uniform arbitrary-input statistics. No large simulation is on the
critical path.
