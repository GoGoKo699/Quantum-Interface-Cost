# Q1 — Delayed local readout through a bounded quantum interface

**Version:** 0.55, 2026-09-27

**Project:** Falling / Q1  
**Status:** The unrestricted equal-accuracy optimum is proved for every integer quantum-memory budget through four input qubits. The nonflat quarter-rank converse closes `(n,q)=(4,2)` and classifies all maximizing normalized seeds. The exact all-n one-qubit allocation result and the unequal-accuracy collective advantage remain separate results. The general two-qubit entropy inequality, common-accuracy asymptotic rate and publication originality are unresolved. The full product-diagonal profile evaluates an established steering entanglement measure; it is not a new resource framework. All proof review described here is internal, not external peer review.

**Integrated exposition.** The [core argument](docs/CORE_ARGUMENT.md)
now connects the operational model, normalized-seed reduction, exact
one-qubit allocation, finite converses and the collective separation in
one notation. Its [bounded internal review](docs/audits/INTEGRATED_CORE_REVIEW.md)
checks the connecting arguments, rank and budget boundaries, comparison
class, and source attribution. The [scientific scope](docs/SCIENTIFIC_SCOPE.md)
records the completed integration gates. A final evidence freeze remains
before manuscript drafting; no additional theorem is required for this
selected package. The underlying frozen proofs and reports are unchanged.

The [nonflat quarter-rank converse](docs/audits/NONFLAT_QUARTER_RANK_CONVERSE.md)
proves `Gamma(4,4)=4+2sqrt(2)` for arbitrary spectra and decoders. Together
with the earlier results, this gives

$$
\Gamma(n,2^q)=2q+\sqrt2(n-q),\qquad 1\le n\le4,\quad q=0,\ldots,n.
$$

The new proof combines the exact top-quarter Pauli spectrum, a local
spectral-spread bound, a sum-of-squares identity, and an exact two-polynomial
certificate on one rectangle. It does not flatten a nonuniform seed.
Equality at `(4,2)` requires two pure local X/Z bisectors and two maximally
mixed retained sites, up to original-site permutations and output isometries.

The [affinity-method continuation](docs/audits/AFFINITY_METHOD_LIMIT.md)
now shows why this stronger surrogate cannot prove the general retention
formula. An explicit weighted star at `(n,q)=(15,4)` violates the
surrogate bound but satisfies the original benchmark. The star family
rules out every universal linear logarithmic-rank charge for the surrogate.
Its exact entropy optimum and asymptotic rank profile are elementary
corollaries of established Faber–Krahn theory. An exact optimal-decoder gap
identity identifies information needed for a direct trace-norm argument.

The [spectral-layer bound](docs/audits/SPECTRAL_LAYER_SCORE_BOUND.md)
provides such a direct comparison. Write `Delta=sum_U(a_U-F_U^2)`, where
a_U is the affinity and F_U the original query score. The score exceeds its
canonical mixture of nested flat spectral scores by at most
`2sqrt(n Delta)`. The same mixture approximates every query, each layer
respects the seed's rank cap, and the bound needs no spectral separation.
A one-qubit family proves the square-root order and constant sharp for
this comparison. Standard spectral thresholding is prior mathematics;
the supplied decoder-gap application leaves the general optimum open.

The [balanced-spectrum theorem](docs/audits/BALANCED_SPECTRUM_OPTIMALITY.md)
now evaluates the original score for every n at spectra
`(1+t)/2^n` and `(1-t)/2^n`, each repeated `2^(n-1)` times. Its exact
maximum is `2(n-1)+sqrt(4-2t^2)`, with all t>0 maximizers consisting of
one original-site mixed bisector and maximally mixed spectators. The
t=1 endpoint proves the flat half-rank retention bound at all sizes,
removing the earlier restriction on the number of active singleton sites.
The entire balanced-spectrum family satisfies the sharp seed entropy
inequality. This does not settle arbitrary nonflat half-rank spectra or
the unrestricted common-accuracy rate.

The [stability extension](docs/audits/BALANCED_SPECTRUM_STABILITY.md)
gives a quantitative form of this equality theorem and a nonflat
consequence at every n. A flat half-rank seed with original-score gap
epsilon is within full trace norm `16sqrt(2epsilon)` of a retention
seed. For any density matrix of rank at most `k=2^(n-1)`, the spectral
condition `sqrt(2(1-Tr(sqrt(rho))/sqrt(k)))<=1/(4096n)` also guarantees
retention, with equality only at a retention seed. This criterion allows
arbitrary supports and eigenvectors. It leaves spectra outside that
sufficient neighborhood unresolved; neither displayed constant is
claimed optimal.

The [half-rank converse](docs/audits/HALF_RANK_RETENTION_CONVERSE.md)
now settles the unrestricted finite optima

$$
\Gamma(3,4)=4+\sqrt2,\qquad \Gamma(4,8)=6+\sqrt2.
$$

More generally, for n=2,3,4 every positive S with `Tr(S^2)=1` and
`rank(S)<=2^(n-1)` obeys the stronger affinity inequality

$$
\sum_{A\in\{X_i,Z_i\}_{i=1}^n}
\sqrt{\operatorname{Tr}(SASA)}\le2(n-1)+\sqrt2.
$$

The established squared-fidelity/affinity comparison transfers this to
all normalized seed scores. The proof retains the rank constraint through
the top half of the single-site Pauli spectrum; a two-variable positive
quadratic completes the dominant-site case. It requires neither flatness
nor any decoder algebra. Equality forces a maximally mixed state on n-1
sites and a pure X/Z bisector on the remaining site. Output isometries
supply the corresponding normalized Kraus seeds.

The [short core argument](docs/CORE_ARGUMENT.md) combines this finite
result with the exact all-n one-qubit allocation theorem and a collective
advantage for unequal accuracies. The earlier
[quarter-rank geometry](docs/audits/QUARTER_RANK_GEOMETRY.md) supplies the
sharp squared-query-score budget six; the new converse completes the
unsquared optimization. The smallest remaining finite common-accuracy
case is now `(n,q)=(5,2)`. The general entropy inequality, asymptotic
common-accuracy rate, and publication originality remain open.

Earlier readout, resolvent and channel theorems remain in the ledger and
linked proof notes. Their former three-input scope restrictions describe
those individual methods; they are no longer restrictions on the new
finite converse. Historical proof notes and their recorded hashes are
preserved.

## 1. Origin, scope, and claim ledger

Page 24 of the user-supplied *【马兆】坠落.pdf* describes a fictional progression from a quantum solver to a quantum-resident workflow because repeated classical–quantum interfaces become costly. The present model is our proposed scientific extraction; its assumptions and conclusions are not claims made by the fiction.

The general compression problem below is already present in the dimensional measurement-simulability framework of Ioannou et al. [1]. Connections between that framework, steering assemblages, and Schmidt number are established by Jones et al. [2]. Earlier quantum compression relative to measurements is also essential prior art [3]. We therefore do **not** propose a new definition of quantum interface cost as the contribution.

| Item | Status and provenance |
|---|---|
| Arbitrary quantum encoding, unlimited classical side information, delayed measurement choice | Established framework [1,2]. |
| Classical simulability equals joint measurability | Established framework [1,2]; elementary qubit construction below. |
| Exact preservation of all local X/Z readouts requires n retained qubits | Derived below; also subsumed by Ballester–Wehner–Winter [10], Lemma 5.1. |
| Uniform-random-subset hybrid construction | Explicit elementary achievable strategy; optimal for q=1 at every n, every integer budget through n=4, and at the endpoints. General optimality unresolved. |
| Unrestricted Gamma(n,2^(n-1))=2(n-1)+sqrt(2), n=2,3,4 | Derived and independently reconstructed from positivity, a rank-constrained Pauli-spectrum estimate and one positive quadratic. Arbitrary spectra and decoder algebras are included. |
| Every maximizing half-rank normalized seed is a retention seed, n=2,3,4 | Derived with complete equality analysis: one pure X/Z bisector and n-1 maximally mixed reference sites, up to output isometries. This is not a classification of every physical instrument. |
| Unrestricted Gamma(4,4)=4+2sqrt(2), including all maximizing normalized seeds | Derived and independently reconstructed for arbitrary spectra; exact rational Bernstein certificate supports the scalar positivity step. Equality consists of two original-site bisectors and two maximally mixed retained sites. |
| General retention bound for the root-affinity surrogate | False: an exact rank-16 star on 15 inputs exceeds the surrogate benchmark; its original trace-norm score stays below retention. No finite C gives a universal surrogate bound sqrt(2)n+C log2(rank). |
| Exact entropy and asymptotic rank profile of the root-affinity surrogate | Elementary deduction from Beigi's established entropy-energy and Faber–Krahn inequalities with matching product and truncated-product constructions; not the original interface optimum. |
| Equality in every fidelity–affinity comparison | Each flat positive-eigenvalue block has exactly the same original query profile as the seed. A nonflat rank-at-most-2^q seed with this equality can therefore be replaced by a flat seed of rank at most 2^(q-1). |
| Quantitative original-score comparison with nested flat spectral seeds | One common rank-preserving mixture has nonnegative query-profile errors with squared sum at most 2Delta, where Delta=sum_U(a_U-F_U^2). The resulting score error 2sqrt(n Delta) is sharp; general retention and entropy converses remain open. |
| Exact original-score optimum for every balanced two-level spectrum, at every n | Derived and independently reconstructed: max g=2(n-1)+sqrt(4-2t^2). For t>0 equality requires one original-site mixed X/Z bisector and maximally mixed spectators. The family obeys the sharp entropy inequality. |
| Every flat half-rank seed obeys retention at every n | The t=1 balanced-spectrum endpoint gives g<=2(n-1)+sqrt(2), with equality exactly at one discarded original-site bisector. No restriction on singleton sites or eigenvectors; arbitrary nonflat half-rank spectra remain open beyond the proved finite cases. |
| Near-optimal balanced seeds are close to original-site bisectors | Derived with explicit dimension-independent bounds: full trace norm at most 16sqrt(2e_g)/t for bias t>0 and original-score gap e_g. The square-root gap exponent and inverse-bias scaling are necessary; the prefactor is not claimed optimal. |
| Dominant singleton mass excludes arbitrary nonflat half-rank improvements at every n | Derived when at least three quarters of the square root's nonzero singleton X/Z mass lies on one original site, with equality only at retention seeds. This is a sufficient coefficient condition, not an assumption on allowed encoders. |
| An explicit nonflat half-rank spectral neighborhood obeys retention for every n | Derived for rank<=k=2^(n-1) when sqrt(2(1-Tr(sqrt(rho))/sqrt(k)))<=1/(4096n), with arbitrary supports and all equality cases. The radius is sufficient, not an unrestricted half-rank converse. |
| Four-input, rank-at-most-four squared query-score budget | Exactly six, derived and independently reconstructed for arbitrary spectra. Equality fixes two pure X/Z-plane sites and two maximally mixed sites. This does not evaluate the unsquared score. |
| Four-input, two-qubit retention converse for flat seeds and rank at most three | Derived and independently reconstructed; all flat equality seeds are retention seeds with two bisectors. The subsequent nonflat quarter-rank theorem removes the remaining spectrum restriction. |
| Exact optimum and maximizing seeds with one retained qubit | Derived and independently checked from Cheng–Hall monogamy [11]; see Section 8 and the full proof. |
| Exact complete local X/Z accuracy region with one retained qubit | Derived and independently checked: the sum of established local incompatibility weights is at most one; explicit matching allocation. |
| Equal-accuracy optimum for pairwise commuting/anticommuting reflection readouts at all n,q | Derived and independently checked from prior graph-Clifford dimension algebra and an elementary matching argument; unrestricted encoders, explicit decoder restriction. |
| Full accuracy region for the same readout class at all n,q | Derived and independently checked: threshold matching and finite operator levels give sum_i w(x_i,z_i)<=q, with sharp support for every nonnegative query weighting. |
| Sharp three-qubit spin-flip purity bound at rank at most four | Derived and independently checked: sum of six squared root fidelities is at most 5-4 Tr(rho^2), with equality at every allowed purity; all nonuniform invariant seeds are covered. |
| Common Kramers-odd ququart readout class has exact uniform score 2sqrt(6) | Derived and independently checked via a symmetry-fixed extremal eigenvector; arbitrary original seeds allowed, but not every balanced readout family shares this symmetry. |
| Every common antiunitary-odd ququart binary-readout class obeys 2||w||_2, with classwide uniform maximum 2sqrt(6) | Derived and independently checked: +I reduces to two commuting Pauli algebras and qubit monogamy; nonscalar squares reduce to blocks of dimension at most two. General Hermitian contractions are included; the full three-input bound is now supplied by the half-rank theorem. |
| Every three-input seed of rank at most three obeys Gamma(3,3)<=4+sqrt(2) | Derived and independently checked for arbitrary spectra and full trace norms, with no antiunitary condition; the complete weighted two-site-retention support is an upper bound, not an evaluated qutrit optimum. |
| Seven of ten nonscalar ququart signature patterns obey the retention benchmark | Derived and independently checked: the one-block theorem excludes four, and the positive-spectrum resolvent argument excludes three more. The later half-rank theorem closes the other three without classifying their readouts. |
| At most one double-block query pair obeys the three-input retention benchmark | Derived and independently checked for arbitrary complex orientations and unequal angles; uses an established mixed-Choi monogamy corollary plus two simultaneous compression bounds. |
| At n=q+1, q dedicated qubit query pairs plus one arbitrary joint-memory query pair have exact retention optimum | Derived and independently checked for all q>=1, arbitrary binary POVMs and collective encoders; a product-Bell spectral cap and normalized resolvent trace give the sharp norm 2q+sqrt(2). |
| At n=3,D=4, any two commuting original query algebras forbid an advantage | Derived and independently checked by finite-dimensional commutant classification and the preceding factor/one-double-block converses; every violating optimal family must make all three algebras pairwise noncommuting. |
| Two sharp internally anticommuting pairs with two mixed cross commutators zero forbid an advantage | Derived and independently checked: complete ququart algebra classification, a two-angle maximally entangled top eigenvector and the full third-pair resolvent; same-axis cross commutators may be nonzero. |
| Any two sharp internally anticommuting ququart pairs plus an arbitrary third binary-POVM pair obey norm(H)<=4+sqrt(2) | Derived and independently checked, with no cross-commutation hypothesis. Joint spectral-tail constraints and a 400-cell exact rational certificate close the sharp-pair case; the half-rank theorem subsequently removes the angle restriction for the three-input bound. |
| Two spectral modes always suffice for a positive last-query resolvent with arbitrary earlier binary POVMs | Derived and independently checked from the second moment; an exact double eigenvalue 2sqrt(3) rules out a universal one-mode setup. The full head channel gives an exact 4-by-4 envelope test, whose universal validity for physical data remains open. |
| A physical full spectrum, all memory-valued polynomial moments, and the established one-/two-dimensional memory compression caps suffice for the two-mode envelope test | Incorrect: an exact synthetic Hamiltonian satisfies all these constraints and fails the test. Its fixed head violates an explicit support bound from the four reference Pauli correlations; no physical counterexample is claimed. |
| Arbitrary two ququart binary-POVM pairs obey the sharp bound U+m<=4sqrt(3) | Derived and independently checked: a squared trace-norm support budget also evaluates every nonnegative weighted Ky Fan support. Equality uniquely gives the balanced readout family up to the stated symmetries. |
| Every equal-weight two-mode support attainer obeys norm(H0+h3)<=(4+2sqrt(5))/sqrt(3) for arbitrary third pairs | Derived and independently checked from equality rigidity and the pure-memory resolvent. This upper bound is below the retention benchmark; attainment is not asserted. The subsequent half-rank theorem proves the unrestricted three-input converse. |
| An explicit global neighborhood of the maximal two-mode support obeys the converse | Derived and independently checked: deficit at most 2^-32 gives norm(H0+h3)<16/3 for every third pair; within m>=2+sqrt(2), deficit at most 2^-24 suffices. Conservative radii, not the whole remaining region. |
| High-m heads within full diamond distance 2/5 of an entanglement-breaking channel obey the converse | Derived and independently checked by a centered resolvent estimate and two quadratic comparisons. The complete positive-quadrant nonclassical-head example family is covered, including NPT channels. |
| A one-block last pair obeys the strict converse throughout m>=2+sqrt(2) | Derived and independently checked from the actual channel moment, Bell compression and a rational endpoint certificate. This earlier partial exclusion is now superseded for the benchmark by the half-rank theorem. |
| Four readouts in the stated conserved-symmetry Pauli spaces permit any third pair with norm(H)<=5 | Derived and independently checked; all contraction coefficient balls are included. The actual isolated positive head is a rectangular-POVM channel. The bound five is not asserted optimal. |
| Zero Pauli-conjugation gap implies an EB head or support at most 2+sqrt(2) | Derived and independently checked by exact flattening and complete coefficient classification. This requires zero gap; it is not a global approximation theorem for arbitrary heads. |
| Exact last-query resolvent with any allowed Jordan-block count in odd or even dimension | Derived and independently checked: sum the nonnegative gains of the outermost eigenvalue pairs. One block uses only the extreme eigenvalues; fixed `(11)` ranks have a two-branch refinement. |
| A defined inverse makes the actual one-mode envelope pass every one-block last pair | Incorrect even for reflections in `(22)^2(11)` and `(22)^2(12)`: both ordinary and signed-chiral tests exceed 33/32. The actual Hamiltonian stays below 21/4 for every third pair; its two-positive-mode envelope succeeds. |
| Two controlled-phase-coupled query pairs with unequal original angles permit an arbitrary third pair | Derived and independently checked: the exact parity spectrum, flat marginal and actual copying-sector channel give the sharp norm bound 4+sqrt(2). This is a continuous family, not all ququart pairs. |
| A one-block last query has a direct full-H0 norm bound in every memory dimension | Derived and independently checked by a spectral chord, exact plane inverse update and operator concavity. U<=2sqrt(3) suffices at three inputs; the actual-plane refinement also repairs the earlier reflection examples. |
| One small Pauli image gives an explicit entanglement-breaking comparison channel | Derived and independently checked from the established qubit partial-transpose-invariance criterion: image trace norm 2n gives full diamond distance at most 2n/(1+n). No claim that every high-energy head has such an axis. |
| Some Pauli image of trace norm at most 2/3 suffices throughout the high-m strip | Derived and independently checked through the direct EB repair resolvent comparison, with exact cubic and linear endpoint certificates. The actual channel's coherences are retained. |
| Three partial-SWAP Bell-subspace projectors sum to at most 5I/2 | Derived and independently checked, with exact equality classification; gives the retention converse for equal spectra within each site's two Jordan blocks. Arbitrary independent U(4) embeddings remain open. |
| All small subsystem perturbations around the known Bell-subspace attainers lower the sum norm | Derived and independently checked in all eighteen transverse directions; exact negative Hessian and an explicit radius 2^-10. A local converse, not global optimality or global rigidity. |
| Exact worst weighted last-site resolvent in every even memory dimension, including all binary POVMs | Derived and independently checked: extreme spectral pairing and a convex-quartic/cubic-root decision eliminate the added decoder. Exact for a stated spectral upper bound, not a solution of the full Hamiltonian problem. |
| Two sharp query pairs have exact score cap 3 on Schmidt-rank-at-most-two states, a joint spectral-tail bound, and the sharp circle (U-2)^2+(m-2)^2<=4 | Derived and independently checked using a fixed-memory-marginal Choi bound, chiral singular-vector compression and positive-projector overlap. Equality in the cap is classified on the occupied support; the following converse uses these constraints to close the sharp-pair target. |
| Arbitrary reflection families admit an all-Jordan-block scalar spectral certificate | Derived and independently checked; actual excesses and same-site orthogonality give a sufficient bound, including regions in the three ququart patterns that were unresolved before the half-rank theorem. |
| A finite negative-top Bell-projector penalty repairs the bound two | Incorrect for every finite coefficient at least one; exact signed spectra on the existing mixed-rank example. This refutes the relaxation, not the interface conjecture. |
| Entropy bound for product-diagonal Gram matrices | Derived and independently checked, allowing correlated spectra and arbitrary local bases; does not restrict unrestricted encoders. |
| Entropic finite-error lower bound | Direct application of Berta et al. [4], Fano, and conditional-entropy inequalities. |
| Stronger logarithmic-Sobolev converse throughout the nonclassical region | Derived and independently checked from Beigi [14] and the root-fidelity inequality [15]; unrestricted encoder bound. |
| Asymmetric entropy converse and linear onset above the classical threshold | Derived and independently checked; combines established generalized QRAC and cube-entropy ingredients. The exact onset slope remains open. |
| Exact-X asymptotic rate h_2((1-sqrt(1-z^2))/2) | Sharp operational corollary of established cube spectral/entropy results; complete finite instruments preserve exact X, with fixed interior collective separations as a consequence. |
| Exact product-diagonal rate for separate X/Z contrasts | Derived profile theorem with arbitrary correlated spectra; compatibility disk and exact-axis seeds generate its full convex rate, with an explicit strict-saving phase boundary. The unrestricted rate is not identified with this class. |
| Constructive optimizer for the complete strict-saving phase | Derived and independently checked: one scalar root determines the unique reduced two-generator mixture. This is not uniqueness of encoders or unrestricted optimality. |
| Full asymmetric profile versus weighted-CHSH formation bounds | Derived and independently checked: the complete optimized Zhu–Zhang–Ma affine family yields only the radial bound, strictly below C at every asymmetric point outside the disk. This comparison does not exhaust all prior results. |
| Unrestricted rate as local-query steering formation | Derived and independently checked: R=inf_n E_FA(L_n)/n. The required local-query identity is stronger than ordinary tensor-power formation additivity; no evaluation is asserted. |
| Exact dimension separation from joint product queries | Derived and independently checked: for two input qubits at eta=(1+1/sqrt(2))/2, local and tuple targets have minimum dimensions two and three. An explicit qutrit instrument attains the tuple target; no entropy-rate separation follows. |
| Fixed-block full-tuple formation dichotomy | Task-specific application of Vollbrecht–Werner Eq. (42); one interior additivity point is equivalent to all-contrast additivity and a universal joint-decoder entropy inequality. This does not replace the stronger local-query inequality. |
| Full profile versus fixed qubit-output channel completion | Derived and independently checked: the minimum Choi E_F is f([x+z-1]_+), strictly above C whenever x+z>1 and both x,z<1; agreement holds exactly on the remaining triangle and exact axes. |
| Full profile versus Cope–Uola average-rank cost | Exact specialization D_M=W=w; the existing phase boundary identifies C<w. Worst-case quantum dimension remains a different resource. |
| Minimum formation entanglement from two correlations with a trusted qubit | Exact E_2=gamma from the prior Verstraete–Wolf theorem; E_d=C for every d>=3, attained with one fixed qutrit pair. Realization dimension counts flags, unlike the interface memory cap. |
| Structure of every minimum-formation realization in the noisy nonclassical interior | Derived equality theorem: orthogonal classical and entangled sectors are necessary; all qutrit optimizers are classified, including a mixed-state family in the strict-saving phase. |
| Full profile from scalar conversion of the exact prior concurrence cost | Incorrect in the noisy nonclassical interior: Han et al.'s weighted family gives minimum concurrence w, but C>f(w) throughout that region. Their pure weighted geometry and central-phase qutrit construction are prior ingredients. |
| Tomassoli's 2024/25 thesis and the full formation profile | Full text now read: fixed orthogonal two-qubit scalar boundary and axis family are prior. The strongest calibrated two-parameter lift is G=f([x+z-1]_+), with a triangular zero region, not C's quarter disk. A factor-two negativity correction is required. This closes the specified comparison, not exhaustive originality; see the [full-text audit](docs/audits/TOMASSOLI_FULL_TEXT_COMPARISON.md). |
| Ordinary negativity and formation can always share a two-correlation minimizer | Incorrect precisely in the interior phase C<w: minimum N=w/2, while minimum E_F among N-minimizers is w. Supplied weighted/equality proof; Pusey's equal-weight negativity line and flagged attainment are prior. |
| Complete simultaneous formation-entropy/ordinary-negativity tradeoff at fixed two correlations | Derived and independently checked for arbitrary finite Alice dimension: every E_F+lambda(2N) minimum and every negativity-budget optimum are evaluated, with qutrit attainment. This auxiliary resource frontier does not give a memory converse. |
| Mixed-state two-qubit support and full joint-resource convex-hull characterization | Direct prior corollaries: Zhu–Zhang–Ma Corollary 1 / Eq. (30), optimized before Jordan-block convexification, gives the sharp all-price support. The explicit phase/root/equality evaluation is separate; see the [nonlinear-source audit](docs/audits/NONLINEAR_CHSH_SUBSUMPTION.md). |
| Real encoders versus complex encoders for real X/Z targets | Same unrestricted asymptotic rate; real Kraus/readout matrices need at most one extra retained qubit, with arbitrary complex inputs and unchanged uniform error. A task-specific corollary of prior realification, not fixed-budget equivalence. |
| Optimal two-input joint readouts require arbitrary nonprojective measurements at full rank | Incorrect: every full-rank context optimum is a rank-one PVM. An optimal ambient four-dimensional PVM exists at singular rank, but its support compression can be nonprojective. Supplied dual-complementarity proof; the entropy maximum remains unevaluated. |
| Sharp entropy proof from exact priors plus a total Holevo budget, or from rank-two interpolation alone | Both relaxations are refuted by explicit constructions; neither construction is an admissible counterexample to the original quantum entropy inequality. |
| Two-input joint entropy bound as a universal matrix cover | Exact equivalent SDP/entropy certificate; a failed cover supplies an admissible violating seed. No universal cover or failed instance has been proved, and the joint target is weaker than the local one. |
| Product repetition removes the local/joint score distinction | Incorrect: a certified rank-two seed has f_2-j_2=(sqrt(2)-1)/8, preserved under all tensor powers. Product additivity of j is a prior minimum-cost measurement theorem; this seed violates no entropy bound. |
| Exact maximum score at any rank-two spectrum | Derived and independently checked for arbitrary eigenvectors; excludes all rank-two entropy witnesses. |
| Exact flat half-rank optimum through four input qubits | Derived and independently checked, with equality cases; with separate lower-flat-rank estimates; the subsequent half-rank theorem removes the nonflat restriction for n=2,3,4. |
| Further seed entropy exclusions | Derived and independently checked for local classical flags, locally maximally mixed two-qubit states, and condition number at most 6.235819648; restricted families. |
| Support-inertia converse for arbitrary spectra | Derived and independently checked; an explicit neighborhood of every subset support cannot improve its finite-budget score. |
| Stability near all rank-at-most-two seeds | Derived and independently checked; an open entropy-valid neighborhood exists at each fixed n, with separate quantitative spectral-tail criteria. |
| Uniformizing a seed on its support | Invalid as a general optimization step; exact nonuniform fixed-support optima provide counterexamples. |
| Exact maxima for one distinguished eigenvalue at all n and two double eigenvalues at n=2 | Derived and independently checked; all two-qubit spectra with at most two distinct eigenvalues satisfy the entropy inequality. |
| Two-qubit kernel-sensitive entropy certificates | Derived and independently checked; maximally entangled kernel implies score at most the classical threshold. |
| Sharp local squashed-entanglement charge from the X/Z score | Incorrect; exact near-Bell obstruction, leaving the global entropy target unchanged. |
| Positive linear memory for every fixed contrast above 1/sqrt(2) | Derivation below using a two-setting witness and faithful, monogamous squashed entanglement [5,6]. Independent novelty not established. |
| Regularized entropy characterization of the asymptotic rate | Derived and independently checked; fixed-cap coding and scalar-contrast continuity are proved; no closed-form evaluation. |
| Exact-axis boundary and unequal-accuracy collective advantage | Supplied deduction: induced-cube spectral reduction and an explicit five-qubit-memory separation from the complete original-site-retention class. |
| Two-qubit SLD minimum at every spectrum | Supplied deduction; proves the SLD entropy inequality for two inputs, without closing the sharp linear seed entropy target. |
| Sharp two-qubit entropy bound when lambda_3+lambda_4>=1/29 | Derived and independently checked for all complex eigenbases, by analytical reduction and an exact rational certificate. Any remaining witness has top-two weight greater than 28/29. |
| Explicit two-qubit entropy-valid neighborhood lambda_3+lambda_4<=2^-20 | Derived and independently checked for all complex eigenbases. The proof combines high-score core stability, an unbalanced-spectrum gate, and a uniform low-score-core entropy margin. The cutoff is sufficient, not sharp. |
| Two-qubit entropy witnesses require core score <=10/3 and normalized second core eigenvalue >1/5 | Derived and independently checked; finite support-angle estimates plus an exact two-variable certificate handle high-score cores. A nonempty low-score region remains. |
| Sharp two-qubit subspace coupling and entropy bound whenever lambda_1=lambda_2 | Derived and independently checked; exact local-orbit coupling minimum, sharp 7/8 universal floor and 2/sqrt(3) anisotropy coefficient. One scalar majorant closes the remaining flat-core cases without interval partitions; unequal cores remain open. |
| Sharp score at every fixed product-parity weight and every block size | Direct symmetry specialization of prior fidelity theory, with an explicit simultaneous attainer; g_n<=n sqrt(2+8q(1-q)). See the [parity proof](docs/audits/PARITY_READOUT_BOUND.md). |
| Two-qubit entropy bound when the top-two spectral subspace is a local product-parity sector | Derived and independently checked; arbitrary unequal eigenvalues and complex intrablock coherences. This is not all parity-commuting states. |
| Sharp operator envelope for a mixed scalar/traceless inactive decoder site | Derived and independently checked; classification threshold improves to below sqrt(21/2). A later short anticommutation corollary gives 13/4 without the sharp-envelope machinery. |
| Two-qubit entropy bound when core score >13/4 and tail weight <=1/99 | Earlier partial result, derived and independently checked; strengthened angle inequality and a 97-leaf exact scalar certificate. Entirely elementary through <=1/201; extended by the next row. See [the small-tail proof](docs/audits/EXTENDED_CORE_TRANSFER.md). |
| Two-qubit entropy bound when top-two core score >13/4 and tail weight <=1/29 | Derived and independently checked; paired finite scalar-query gains, active curvature and an imbalanced SLD bound close the larger-tail strip using 5,324 exact scalar leaves. [Full-strip proof](docs/audits/CURVED_CORE_TRANSFER.md). Lower-score cores remain unresolved. |
| Square of fixed-core, fixed-tail transfer sum is concave in squared tail parameter | Derived and independently checked for arbitrary complex two-dimensional blocks, including singular blocks; finite positive-parameter tangents. Maximizing over states need not preserve concavity. [Matrix proof](docs/audits/FINITE_TAIL_STRUCTURE.md). |
| Quantitative stability of the one-qubit optimum | Supplied deduction; normalized seeds and maximally-mixed-input branch weights, without a channel-distance claim. |
| Sharp evaluation of the common-accuracy asymptotic memory rate, or a strict common-accuracy collective-coding improvement | Candidate research target; not solved here and not yet certified absent from the literature. |
| Exponential sampling advantage or speedup for classical-data learning | Not established; the many-copy control in Section 9 is deliberately easy classically. |

## 2. Precise operational model

Let S consist of n qubits. The encoder receives **one** arbitrary, unknown density matrix rho on S, without a classical description or another copy. Internal entanglement among the input qubits is allowed.

Before the query is known, the encoder applies a quantum instrument

\[
\mathcal E(\rho)=\sum_c |c\rangle\langle c|_C\otimes\mathcal E_c(\rho),
\qquad \sum_c\mathcal E_c\text{ is trace preserving},
\qquad \dim Q\le 2^q.
\]

The classical alphabet is finite for each protocol, but there is no a priori bound on its size. Thus the number of classical bits is free. The bound q is a **worst-case quantum dimension**, not an average over branches. Arbitrary global encoding is allowed. All systems carrying quantum information across the interface count in Q. There is no uncharged quantum bypass, source reaccess, or preshared entanglement link. Independent decoder ancillas and unlimited classical computation are allowed.

After encoding, a query j=(i,b) arrives, with i in {1,...,n} and b in {X,Z}. A query-dependent decoder measures CQ and returns one physical sign s in {+1,-1}. There is one query per input specimen. We do not demand simultaneous X and Z outcomes or nondestructive reuse of Q.

For P_(i,X)=X_i and P_(i,Z)=Z_i, require

\[
\Pr(s\mid i,b,\rho)=\operatorname{Tr}[M^{\eta}_{s\mid i,b}\rho],
\qquad M^{\eta}_{s\mid i,b}=\tfrac12(I+s\eta P_{i,b}),
\tag{1}
\]

for **every** input rho and every query. Contrast eta ranges from 0 to 1. It specifies the allowed output statistics, not a particular microscopic noise channel. Let q_min(n,eta) be the minimum q.

Relative to the ideal binary measurement, the worst-case total-variation error is

\[
\epsilon=\frac{1-\eta}{2}.
\tag{2}
\]

On a corresponding Pauli eigenstate this is the probability of returning the opposite sign. On a general state, it is a distribution error, not disagreement with a preexisting hidden outcome.

### Why the symmetric target is not an artificial accuracy restriction

Define an alternative problem demanding at most epsilon total-variation error for every rho and every ideal local X/Z readout. Write its effective observable as A_j, so ||A_j-P_j||_infinity <= 2 epsilon.

Twirling an admissible protocol by the n-qubit Pauli group, with the random seed stored in C and the appropriate output-sign correction, replaces A_j by lambda_j P_j. Specifically,

\[
\lambda_j=2^{-n}\operatorname{Tr}(P_j A_j)\ge 1-2\epsilon.
\]

Permutations and independent local Hadamards act transitively on the 2n queries. Averaging over these symmetries equalizes the coefficients to a common lambda >= 1-2 epsilon. All these transformations preserve q because their seeds are classical. Independent random output flips then reduce lambda to eta=1-2 epsilon.

Conversely, (1) has worst-case error (2). Therefore the two minimum-memory formulations coincide for 0 <= epsilon <= 1/2. The lower bounds below do not depend on imposing a physical depolarizing-noise assumption.

## 3. Exact classical threshold

Set

\[
\eta_0=1/\sqrt2,\qquad
\epsilon_0=(1-1/\sqrt2)/2\simeq0.1464466094.
\]

For one input qubit, use the four-outcome POVM

\[
G_{a,b}=\frac14\left(I+\frac{aX+bZ}{\sqrt2}\right),
\qquad a,b\in\{+1,-1\}.
\tag{3}
\]

Every effect has eigenvalues 0 and 1/2, and they sum to I. Its two marginals are

\[
\sum_bG_{a,b}=\tfrac12(I+a\eta_0X),\qquad
\sum_aG_{a,b}=\tfrac12(I+b\eta_0Z).
\]

Apply the product POVM across all n sites, store all pairs (a_i,b_i) in C, and answer the selected query with the corresponding sign. This works on arbitrary entangled inputs because it is an operator identity, not a product-state argument. Extra random output flips give any eta <= eta_0.

For necessity, a purely classical encoding is a parent measurement followed by query-dependent classical postprocessing. Alternatively, Section 6 gives a separable-state witness implying eta <= eta_0 whenever q=0. Thus

\[
\boxed{q_{\min}(n,\eta)=0\ \Longleftrightarrow\ \eta\le\eta_0.}
\tag{4}
\]

This threshold is the familiar joint-measurability threshold of equally noisy orthogonal Pauli measurements; it is not a new quantum phenomenon [1,2].

## 4. An explicit hybrid upper bound

Choose a uniformly random subset K of exactly q input sites. Keep those q qubits unchanged, and apply (3) separately to the remaining n-q sites. Store K and all measurement outcomes classically.

If the queried site is in K, perform the requested ideal Pauli measurement. Otherwise return the relevant recorded sign. Every site is retained with probability q/n, so its effective contrast is

\[
\eta_q=\eta_0+\frac qn(1-\eta_0).
\tag{5}
\]

This is valid for all input states. Measurement of the discarded sites can condition the retained subsystem, but averaging over their outcomes is trace preserving; hence it does not alter the retained site's unconditional marginal.

For eta > eta_0, this gives

\[
q_{\min}(n,\eta)\le
\left\lceil n\frac{\eta-\eta_0}{1-\eta_0}\right\rceil.
\tag{6}
\]

The rounded-up construction can be degraded by random output flips to the exact target eta. The classical record can contain the subset tag plus 2(n-q) signs. Its size is not charged in this model.

No lower bound in this note assumes that the optimum retains individual input qubits. Arbitrary collective coding is allowed. Section 8 settles q=1 at every n and q=n-1 through n=4; the other general intermediate-memory cases in (6) remain unresolved.

## 5. Entropic lower bound

**Proposition.** Every admissible protocol satisfies

\[
q\ge n\left[1-2h_2\!\left(\frac{1-\eta}{2}\right)\right],
\tag{7}
\]

where h_2 is binary entropy, with logarithms to base two. The useful bound is its maximum with zero.

**Proof.** Apply the encoder to S in a virtual maximally entangled state Phi_RS, where R=R_1...R_n and dim R=2^n. Call the resulting state omega_RB, where B=CQ. This is a proof device, not an additional entanglement resource offered to the protocol.

Let D_(i,b) be the decoder's Hermitian contraction on B. Equation (1) implies E*(D_(i,b))=eta P_(i,b). Since X and Z are real,

\[
\langle X_{R_i}\otimes D_{i,X}\rangle_\omega
=\langle Z_{R_i}\otimes D_{i,Z}\rangle_\omega=\eta.
\tag{8}
\]

Bob can therefore guess the outcome of X or Z on R_i, once the basis and site are given, with error epsilon=(1-eta)/2. Fano's inequality and data processing give

\[
H(\mathsf X_i\mid B)\le h_2(\epsilon),\qquad
H(\mathsf Z_i\mid B)\le h_2(\epsilon).
\]

Here the sans-serif variables denote classical measurement outcomes. Applying conditional-entropy subadditivity to the reference outcomes yields

\[
H(\mathsf X^n\mid B)+H(\mathsf Z^n\mid B)
\le 2nh_2(\epsilon).
\tag{9}
\]

This does not assume that all the site-specific decoders can be executed on the same Q. Each individual entropy bound is a property of a marginal state; the entropy inequality combines these bounds without implementing their measurements jointly.

The two full product bases are mutually unbiased, so Berta et al.'s uncertainty relation with quantum memory [4, Eq. (2)] gives

\[
H(\mathsf X^n\mid B)+H(\mathsf Z^n\mid B)
\ge n+H(R\mid B).
\]

Because C is classical,

\[
H(R\mid CQ)=\sum_c p_c H(R\mid Q)_{\omega^c}\ge -\log_2\dim Q\ge-q.
\tag{10}
\]

Combining (9)-(10) proves (7). In particular,

\[
\boxed{q_{\min}(n,1)=n.}
\tag{11}
\]

The exact endpoint is also a direct corollary of the earlier postmeasurement-information result [10], Lemma 5.1: all local X/Z support projectors generate the full matrix algebra. See the [audit](docs/audits/PROOF_AND_NOVELTY_AUDIT.md), Section 6.1. This proof is an application of established uncertainty and entropy results, not a new uncertainty relation. The entropic coefficient is positive only in the smaller-error part of the nonclassical region; a different argument is needed immediately above eta_0.

## 6. A positive memory rate throughout the nonclassical region

**Proposition.** Every admissible protocol satisfies

\[
q\ge \frac{n(\eta-\eta_0)_+^2}{16\ln2}.
\tag{12}
\]

**Proof.** Use the same virtual encoded state and decoders as in Section 5. For each site define

\[
W_i=X_{R_i}\otimes D_{i,X}+Z_{R_i}\otimes D_{i,Z}.
\]

Its expectation on omega is 2 eta. On a product state across R_i:B, let x,z denote the reference Bloch coordinates and u,v the decoder expectations. Since x^2+z^2 <= 1 and |u|,|v| <= 1,

\[
xu+zv\le\sqrt{x^2+z^2}\sqrt{u^2+v^2}\le\sqrt2.
\]

Convexity extends this to every separable state sigma_RiB. Thus the actual state's witness gap is at least 2 eta - sqrt(2).

The witness can be implemented as a **one-way LOCC test from R_i to B**: choose the X or Z basis with equal probability, measure the reference, communicate the basis and sign to B, measure the corresponding decoder, and accept if the signs agree. The accept effect is

\[
T_i=I/2+W_i/4.
\]

Use the convention ||rho-sigma||_(1-LOCC)=4(P_success-1/2), as in the corrected version of [5]. For every separable sigma,

\[
\|\omega_{R_iB}-\sigma\|_{1\text{-LOCC}}
\ge 2\operatorname{Tr}[T_i(\omega-\sigma)]
\ge\eta-\eta_0.
\tag{13}
\]

The corrected one-way-LOCC faithfulness bound [5, Corollary 1, Eq. (12)] is

\[
E_{\rm sq}(R_i:B)_\omega
\ge\frac{1}{16\ln2}
\operatorname{dist}_{1\text{-LOCC}}(\omega_{R_iB},\mathrm{SEP})^2.
\tag{14}
\]

The direction of communication matters: an earlier version of [5] claimed a stronger full-LOCC statement with a flawed proof. Our test is one-way, so (14) uses exactly the corrected theorem.

Squashed entanglement is monogamous [5, Eq. (16); 6], giving

\[
E_{\rm sq}(R_1\cdots R_n:B)_\omega
\ge\sum_i E_{\rm sq}(R_i:B)_\omega.
\tag{15}
\]

Unlimited classical C does not invalidate the quantum-dimension upper bound. Introduce an extension F containing a copy of C. By the definition of squashed entanglement,

\[
E_{\rm sq}(R:CQ)_\omega
\le\tfrac12 I(R:CQ\mid F)
=\tfrac12\sum_c p_c I(R:Q)_{\omega^c}
\le\log_2\dim Q\le q.
\tag{16}
\]

Equations (13)-(16) prove (12). No assumption of product encoding or input independence was used. QED.

This derivation was independently reconstructed in the [commit-pinned audit](docs/audits/PROOF_AND_NOVELTY_AUDIT.md), Section 4.2. The direction, corrected norm coefficient, monogamy and classical-flag dimension bound all check. This workspace review does not establish publication novelty. The coefficient is weak and is not offered as an optimal rate.

### Resource-threshold corollary

For fixed eta,

\[
\boxed{
q_{\min}(n,\eta)=
\begin{cases}
0,&0\le\eta\le1/\sqrt2,\\
\Theta(n),&1/\sqrt2<\eta\le1.
\end{cases}}
\tag{17}
\]

The constants in Theta(n) depend on eta. In particular, q=o(n) cannot sustain a fixed positive contrast advantage over the best purely classical interface. This is a resource threshold, not a thermodynamic phase transition. It does not state that every site must be kept quantum, or that the optimal constant fraction has been found.

## 7. Finite-size and asymptotic gap

Combine the lower bounds by defining

\[
L(\eta)=\max\left\{
0,\ 1-2h_2((1-\eta)/2),\
\frac{(\eta-\eta_0)_+^2}{16\ln2}
\right\}.
\]

The new [logarithmic-Sobolev converse](docs/STRONG_ENTROPIC_CONVERSE.md) gives an additional bound. Set b(eta)=0 for eta<=eta_0 and, for eta>=eta_0, define

$$
b(\eta)=h_2\!\left(
\frac{1-\sqrt{1-(2\eta^2-1)^2}}2
\right).
$$

The subsequent [asymmetric entropy converse](docs/ASYMMETRIC_ENTROPIC_CONVERSE.md)
defines

$$
f(c)=h_2\!\left(\frac{1-\sqrt{1-c^2}}2\right),\qquad
\ell(\eta)=\left[f(\eta)-h_2((1-\eta)/2)\right]_+.
$$

It proves, for every normalized seed, the bound
`S(L^dagger L)>=sum_i[f(F_(i,Z))-h_2((1-F_(i,X))/2)]`.
The proof treats the X-basis columns as an auxiliary quantum random-access
ensemble with correlated classical labels. Established entropy/decoding
bounds control their entropy loss, while a classical cube inequality and
the trace-norm triangle inequality control the complementary Z scores.
No extra copy, simultaneous decoder or source promise is introduced.

Then, with `L_new(eta)=max{L(eta),b(eta),ell(eta)}`,

$$
q_{\min}(n,\eta)\ge\lceil n L_{\rm new}(\eta)\rceil.
$$

The b term is obtained by applying Beigi's improved quantum logarithmic-Sobolev inequality [14, Theorem 2] to a normalized seed's square root, combining root fidelity squared with affinity [15, Appendix A, Theorem 6], and using a Pauli-Fourier comparison. Each refined branch has entropy at most q, so the proof preserves worst-case dimension and unrestricted collective encoding. No typical-input promise or additional specimen is used. The hybrid construction still gives (6).

For fixed eta, product encoding of two blocks yields

\[
q_{\min}(n+m,\eta)\le q_{\min}(n,\eta)+q_{\min}(m,\eta).
\]

This remains valid on states entangled across the two blocks, because only one local query is asked and each block identity is valid for all density matrices. Subadditivity therefore ensures that

\[
R(\eta)=\lim_{n\to\infty}\frac{q_{\min}(n,\eta)}n
=\inf_n\frac{q_{\min}(n,\eta)}n
\]

exists. For eta > eta_0,

\[
L_{\rm new}(\eta)\le R(\eta)\le\frac{\eta-\eta_0}{1-\eta_0}.
\tag{18}
\]

Numerical evaluation of these proved formulas, not simulation data:

| Worst-case TV error epsilon | Contrast eta | Earlier baseline lower bound | Logarithmic-Sobolev bound | Current combined lower bound | Achievable upper bound |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 | 1 |
| 0.01 | 0.98 | 0.8384137282 | 0.8872964169 | 0.8904499196 | 0.9317157288 |
| 0.05 | 0.90 | 0.4272060858 | 0.4929364851 | 0.5718389182 | 0.6585786438 |
| 0.10 | 0.80 | 0.0620088128 | 0.1414405425 | 0.2529325013 | 0.3171572875 |
| 0.14 | 0.72 | 0.0000149892 | 0.0043926999 | 0.0330903683 | 0.0440202025 |
| epsilon_0 | eta_0 | 0 | 0 | 0 | 0 |

For t down to zero, the earlier logarithmic-Sobolev bound has

$$
b(\eta_0+t)=4t^2\log_2(1/t)+O(t^2),
\qquad b(1-t)=1-\frac4{\ln2}t+O(t^2).
$$

The asymmetric converse strengthens the near-threshold scaling:

$$
\ell(\eta_0+t)=2\log_2(1+\sqrt2)t+O(t^2),\qquad
2\log_2(1+\sqrt2)t\le R(\eta_0+t)\le(2+\sqrt2)t.
$$

The latter bound holds for the entire allowed interval 0<=t<=1-eta_0;
convexity supplies the lower supporting tangent. In particular
`R(eta_0+t)=Theta(t)` as t decreases to zero. This proves linear onset,
without evaluating its exact coefficient or the full rate. Extremely close
to eta=1 the earlier b can be stronger than ell, so the maximum is retained.
The corresponding unrestricted seed bound is
`g(L)<=sqrt(2)n+S(L^dagger L)/log_2(1+sqrt(2))`, whose entropy coefficient
0.78643970 remains above the conjectured sharp value 2-sqrt(2).

## 8. Exact one-qubit result and the remaining target

The subsequent [one-qubit theorem](docs/ONE_QUBIT_OPTIMALITY.md) proves, for every n>=1,

$$
\eta_{\max}(n,1)=\frac1{\sqrt2}+\frac1n\left(1-\frac1{\sqrt2}\right),
\qquad \Gamma(n,2)=2+\sqrt2(n-1).
$$

The proof reduces extreme qubit decoders to scalar signs or Bloch observables, then uses Cheng–Hall's three-qubit CHSH monogamy [11]. Their theorem permits different measurement settings on the common qubit and mixed states, exactly as required for site-dependent decoders and three-qubit marginals. Equality forces every maximizing normalized seed to retain one site and project the rest onto product bisectors, up to output unitaries. This characterizes refined branch maps, without assuming that the retained site is chosen independently of the input.

The half-rank theorem now also settles `(n,q)=(3,2)` and `(4,3)` with
`Gamma(n,2^(n-1))=2(n-1)+sqrt(2)` and complete normalized-seed equality
cases. The quarter-rank theorem now closes `(4,2)`. Combined with the
one-qubit theorem and endpoints, every integer qubit-memory budget through
four inputs is evaluated. The general entropy/rate problem remains open.

Thus the former n=2,q=1 diagnostic is settled, including the entire two-input-qubit memory function. For general n, the first nonclassical interval has exact memory one. The argument does not extend to a higher-dimensional central memory: two Bell pairs provide an explicit counterexample to its key pair inequality.

The [allocation theorem](docs/ONE_QUBIT_ALLOCATION_REGION.md) strengthens
this to the complete profile of separate local contrasts. With

$$
w(x,z)=\left[x+z-1-\sqrt{2(1-x)(1-z)}\right]_+,
$$

an interface with worst-case quantum dimension at most two realizes the
profile exactly if and only if `sum_i w(eta_(i,X),eta_(i,Z))<=1`.
Each w is the established incompatibility weight of that noisy orthogonal
Pauli pair. The new global condition follows from weighted CHSH monogamy
and normalized Kraus averaging; a mixture retaining at most one site
attains every feasible profile. All equal contrasts recover the original
uniform theorem. The result describes effects on the specified query family,
not a decomposition of every physical encoder into product operations.

A separate [entropy argument](docs/COMMUTING_SEED_BOUND.md) proves

$$
g(L)\le\sqrt2\,n+(2-\sqrt2)S(L^\dagger L)
\le\sqrt2\,n+(2-\sqrt2)\log_2\operatorname{rank}(L)
$$

whenever the Gram matrix is diagonal in a fixed product of local one-qubit bases. Its eigenvalues may be correlated and nonuniform, and the axes may have Y components. Consequently, this entire structured family cannot improve the common-accuracy subset benchmark. The unrestricted problem has not been narrowed by assumption. A proposed extension using a local quantum conditional-entropy inequality is false; the note gives a two-qubit counterexample, separately from the unresolved global inequality.

The [full profile theorem](docs/PRODUCT_DIAGONAL_PROFILE_RATE.md) now evaluates
the asymptotic rate of protocols admitting such a product-diagonal Gram matrix
on every individually refined Kraus branch. Write C(x,z) for the lower convex,
coordinatewise nondecreasing envelope generated by cost zero on the
compatibility disk and cost f(v) at (1,v) and (v,1), where
`f(v)=h_2((1-sqrt(1-v^2))/2)`. Then this restricted rate is exactly C(x,z).
The proof covers arbitrary correlations among product-basis eigenvalues;
its construction uses complete instruments with a dimension cap on every
branch. Consequently the unrestricted rate is at most C(x,z), while C is
not asserted to be an unrestricted converse.

For `0<z<=x<1` and `x^2+z^2>1`, the comparison with the exact retention
cost w is

$$
C(x,z)<w(x,z)\quad\Longleftrightarrow\quad
\frac{1-x}{1-z}<2\left(\frac1{\ln2}-1\right)^2.
$$

At equality or above this boundary, C=w. In particular C(eta,eta) equals
the subset rate. The explicit convex combination
`(.99,.5)=(87/100)(1,15/29)+(13/100)(12/13,5/13)` achieves rate
`(87/100)f(15/29)=0.3250660206...`, improving the previous 0.354579
upper bound; retention costs 0.39. The second component is classical.
Block allocation and permutation supply uniform performance and worst-case
memory, rather than interpreting mixture cost as average physical memory.

The [source audit](docs/ENTROPY_TRADEOFF_PRIOR_AUDIT.md) identifies C with
Cope's established steering entanglement of formation for the corresponding
noisy Pauli assemblage. The explicit evaluation and restricted tensorization
are the supplied deductions; neither the entropy resource nor its general
framework is new. Publication novelty remains unresolved.

The [two-correlation comparison](docs/audits/TWO_CORRELATION_FORMATION.md)
further proves that C is the minimum state entanglement of formation
consistent with correlations x,z against a trusted qubit's X,Z, when the
other system has dimension at least three. One fixed qutrit pair suffices
for all profiles. If that system is itself a qubit, the exact cost is
`gamma(x,z)=f(sqrt([x^2+z^2-1]_+))`, a direct application of the prior
Verstraete–Wolf CHSH/concurrence bound. It exceeds C exactly outside the
compatibility disk when both contrasts are below one. This separately
defined realization dimension includes classical flags; it does not
replace the interface's free-classical-record resource convention.
The qualitative flag advantage is also prior. The candidate contribution
remains the full two-parameter evaluation and the fixed-cap operational
deduction, with exhaustive originality still unresolved.

The [optimizer follow-up](docs/audits/FORMATION_OPTIMIZERS_AND_PRIOR.md)
proves that every minimum-formation realization in the noisy nonclassical
interior must have orthogonal classical and entangled sectors. It
classifies all qutrit optimizers rather than only constructing one.
The same audit identifies a closer precedent: Han et al.'s weighted
trusted-qubit guessing theorem supplies the pure support optimization,
and their product-plus-Bell flag construction already gives the central
phase's qutrit realization. Their exact mixed-concurrence family yields
w on the full square; its scalar entropy conversion f(w) is strictly
below C throughout the noisy nonclassical interior. The explicit entropy
convexification remains a candidate contribution, not a new general
guessing theorem or a certified original result.

That follow-up also expresses the unresolved two-input joint entropy
inequality as an exact four-context operator-covering problem for every
positive-definite density matrix. It retains the common quantum state
and all context constraints. A failed cover would yield a genuine
violating Gram state; a universal cover would settle only the weaker
joint inequality. Neither outcome has been obtained.

Two [exact proof-method obstructions](docs/audits/ENTROPY_PROOF_RELAXATIONS.md)
show why the sharp all-state entropy bound does not follow from either
exact basis priors with only a total Holevo budget or from the complete
rank-two spectral envelope and a norm constraint alone. The first permits
classical outputs that are not measurements of the filtered ensemble; the
second permits forbidden trusted Pauli terms. Neither refutes the genuine
quantum inequality, which remains open.

The [entropy-rate characterization](docs/ENTROPY_RATE_CHARACTERIZATION.md) additionally proves

$$
R(\eta)=\inf_{n\ge1}\frac1n
\min_{\rho:\ f_n(\rho)\ge\eta} S(\rho),
\qquad
f_n(\rho)=\frac1{2n}\sum_{i,b}
\|\sqrt\rho P_{i,b}\sqrt\rho\|_1.
$$

This is unrestricted and retains the original worst-case dimension and uniform-error quantifiers. Typical Schmidt truncation constructs a new normalized seed; its full orbit supplies a trace-preserving protocol. A continuity argument removes strict contrast slack. A single violation of the unrestricted entropy inequality above would therefore prove a collective asymptotic advantage. Conversely, that inequality holding for every Gram matrix would establish the subset rate for the whole nonclassical interval. Related asymptotic dimension/entropy methods are prior work [12,13]; the note compares their complete-assemblage demands and average-dimension quantities with this task.

The [entropy-inequality boundaries](docs/ENTROPY_INEQUALITY_BOUNDARIES.md) further prove the exact maximum at any rank-two spectrum:

$$
\max_{\operatorname{spec}\rho=(\lambda,1-\lambda,0,\ldots)}g(\sqrt\rho)
=\sqrt2(n-1)+\sqrt{2[1+4\lambda(1-\lambda)]}.
$$

This holds for arbitrary entangled eigenvectors and implies the conjectured entropy inequality for every rank-two state. Also excluded are all states diagonal in a global Clifford stabilizer basis, all flat rank-three states on two inputs, and flat half-rank projectors with one maximally mixed complementary marginal. Each is a proved family inside the unrestricted optimization; none is an assumption about admissible encoders. The smallest possible entropy witness is therefore a two-input, nonuniform rank-three state, while general full-rank two-input states also remain unresolved. Such an entropy witness would certify an asymptotic advantage through regularization even though rank three consumes two qubits at that finite block size.

The [flat half-rank theorem](docs/FLAT_HALF_RANK_OPTIMALITY.md) now proves

$$
\max_{\operatorname{rank}P=2^{n-1}}g\!\left(\sqrt{P/2^{n-1}}\right)
=2(n-1)+\sqrt2,\qquad 1\le n\le4.
$$

Equality requires a pure X/Z bisector projector on one site tensor the identity on the others. The proof also applies at arbitrary n when the singleton X/Z part of `2P-I` occupies at most four sites, without restricting higher-order Pauli terms. It uses a short signed-spectrum calculation and query-specific compression bounds. Its relation to established quantum Boolean-function results is audited in [the source comparison](docs/FLAT_SEED_PRIOR_COMPARISON.md).

The entropy inequality is also closed under [local classical flags and tensor products](docs/CLASSICAL_FLAG_ENTROPY_BOUND.md). In particular, all two-input states classical on either qubit are excluded, even with noncommuting conditional states. All [two-input states with both marginals maximally mixed](docs/LOCALLY_MIXED_TWO_QUBIT_BOUND.md) satisfy a stronger bound, including arbitrary local rotations of Bell-diagonal states. A [spectral theorem](docs/SPECTRAL_CONDITION_ENTROPY_BOUND.md) excludes every full-rank Gram matrix with `lambda_max/lambda_min <= 6.235819648070267`, in any dimension and any eigenbasis. That sufficient threshold is not asserted optimal. An explicit two-qubit counterexample refutes a proposed local conditional-entropy route; it does not refute the global inequality.

The half-rank theorem removes the flat-spectrum restriction and settles
the finite `(3,2)` and `(4,3)` diagnostics, including all lower allowed
ranks. The quarter-rank theorem closes `(4,2)`, so the smallest remaining
finite case is `(5,2)`. This does
not prove the entropy inequality: a two-input entropy witness must still
be nonclassical on both sites. It cannot have both marginals maximally mixed
and, if full rank, must exceed the stated condition-number threshold. The sharp
common-accuracy rate and publication originality remain unresolved.

The [support-inertia converse](docs/SUPPORT_INERTIA_CONVERSE.md) now treats
every spectrum on a given support P. Let a(P) count the sites where both
compressed X/Z operators have positive and negative eigenvalues. Then

$$
g(\sqrt\rho)\le\sqrt2 n+(2-\sqrt2)a(P).
$$

Thus a(P)<=q excludes finite-budget advantage; equality in that class forces
the flat subset seed. Every support with
`||(I-P0)P||_infty<=sin(pi/8)` for a rank-2^q subset support P0 is excluded,
without any spectral assumption. The later half-rank proof excludes all
three-input, two-memory-qubit improvements, including indefinite compressions.

The [spectral-tail theorem](docs/LOW_RANK_ENTROPY_STABILITY.md) proves that,
for each fixed n, some delta_n>0 excludes entropy violations whenever
`1-lambda_1(rho)-lambda_2(rho)<delta_n`. It uses nonzero query-compression
gaps at the classified rank-two equality seeds and the entropy of an
orthogonal mixture. The uniform delta_n is existential. Separate explicit
tail criteria cover coherently rotated supports and arbitrary tail eigenvectors.
For an exact subset core sigma with an orthogonal tail tau of weight epsilon,
the score is at most `(1-epsilon)g(sqrt(sigma))+epsilon g(sqrt(tau))+2sqrt(2)epsilon`.
The linear coefficient is first-order sharp; the resulting entropy cutoffs
are sufficient bounds.

Two [exact fixed-support optima](docs/NONUNIFORM_SUPPORT_OPTIMA.md) show that
replacing a seed by the uniform state on its support can reduce its score,
including at the rank-four budget now covered by the half-rank theorem. They do not beat the subset
benchmark. The [SLD-route audit](docs/SLD_ENTROPY_ROUTE_AUDIT.md) gives exact
counterexamples to two local proof steps and separates the proposed global
SLD entropy bound from inspected convex-roof, tensorization, convolution and
influence theorems. That global bound remains unresolved for arbitrary n; the subsequent two-qubit result below settles n=2.

Sections 6–7 of the [spectral note](docs/ENTROPY_INEQUALITY_BOUNDARIES.md)
now optimize all eigenvectors exactly for a spectrum `(t,b,...,b)` at any n,
and `(a,a,b,b)` on two qubits. Product-diagonal states attain the maxima;
therefore every two-qubit state with at most two distinct eigenvalues,
counting zero, obeys the entropy inequality. This does not cover a general
rank-three spectrum `(t,b,b,0)`, which has three distinct values.
The [kernel converse](docs/TWO_QUBIT_KERNEL_CONVERSE.md) further proves
`g_2(rho)<=2sqrt(2)` whenever the kernel contains a maximally entangled
vector. It also gives kernel-and-spectrum certificates for arbitrary
rank-three eigenbases, including a spectrum-only exclusion at
`(1/2,1/4,1/4,0)`.

A proposed [sharp local entanglement calibration](docs/ENTANGLEMENT_CALIBRATION_OBSTRUCTION.md)
is refuted near a Bell state: any calibration bounded by half the mutual
information and sharp at the Bell endpoint must have infinite endpoint
slope. This leaves the existing weak squashed-entanglement converse intact.
The SLD audit additionally proves an all-spectrum commutator representation
and a graph reformulation, while identifying an exact nonphysical graph
that defeats a relaxation of the quantum constraints. Neither supplies a
new unrestricted rate bound.

The latest [exact-axis theorem](docs/EXACT_AXIS_SPECTRAL_REDUCTION.md)
allows separate X/Z accuracies, as in the one-qubit allocation region.
If every X query is exact, the optimal common Z contrast under dimension D
is `Lambda(n,D)/n`, where Lambda maximizes the adjacency spectral radius
of an induced Boolean-cube subgraph with at most D vertices. The proof
both constrains every collective branch and constructs a complete
trace-preserving translation instrument. An established graph theorem
then gives the exact value `sqrt(D-1)/n` for `100000<=D<=n`.

A star support on 31 inputs attains X contrast one and Z contrast
`1/sqrt(31)` with memory dimension 32 (five qubits). The entire precisely
defined original-site-retention class has contrast region
`sum_i w(eta_(i,X),eta_(i,Z))<=q`. The collective construction exceeds it,
even after reducing X contrast to `9999/10000`. The proof permits joint
measurements of discarded sites and arbitrary processing on retained sites
within that comparison class. The unrestricted operational model is
preserved. This unequal-accuracy advantage does not refute the original
common-accuracy subset conjecture or evaluate R(eta).

The [exact-axis rate theorem](docs/EXACT_AXIS_RATE.md) now sharpens that
family asymptotically: with all X exact and common Z contrast z,
`R_X(z)=f(z)`. It proves the finite heterogeneous converse
`log_2D>=sum_i f(z_i)` and uses truncated auxiliary Bernoulli distributions
in complete translation instruments to attain the rate. The truncation
does not postselect the unknown specimen, and exact X is preserved at
every finite block length. The rate curve and corresponding graph
asymptotics are established prior ingredients; the same curve is also
the dephasing-channel simulation cost under a stronger output requirement.
Here it is derived with the weaker single-query converse explicitly proved.
For every 0<z<1, f(z)<z, giving a strict saving over original-site retention.
At the fixed interior profile X=0.99, Z=0.5, collective rate at most
0.354579 beats that class's exact 0.39. The subsequent profile construction
above improves this upper bound to 0.3250660206...; the unrestricted
interior optimum is not claimed evaluated.

The [two-qubit SLD theorem](docs/TWO_QUBIT_SLD_SPECTRUM.md) minimizes the
local SLD sum exactly over every eigenbasis of every spectrum. Writing
`k_ab=(lambda_a-lambda_b)^2/(lambda_a+lambda_b)` for decreasing eigenvalues
(and zero for a zero denominator), its minimum is
`E_*=k_12+k_13+k_24+k_34`. It proves `I_XZ>=2-S(rho)` for all two-qubit
states. Its entropy-only consequence `g_2<=2sqrt(2+S)` remains weaker
than the sharp linear entropy target at intermediate entropy. No all-n
SLD claim follows.

The [spectral-tail continuation](docs/audits/TWO_QUBIT_SPECTRAL_TAIL_GATE.md)
retains the full `E_*` and proves the sharp target for every complex
two-qubit state with `lambda_3+lambda_4>=1/29`. The proof reduces arbitrary
ordered spectra to balanced spectra through a two-variable quadratic
comparison. A standard-library exact rational certificate checks 400
interval enclosures; the high-tail region is handled analytically. This
is a proof conditional on the supplied reductions, not floating-point
sampling. Any remaining witness has top-two weight greater than `28/29`.
The earlier existential low-rank neighborhood has no proved numerical
radius overlapping this cutoff, so the two results do not settle n=2.
The [core-stability theorem](docs/audits/TWO_QUBIT_CORE_STABILITY.md) now
makes one radius explicit: every two-qubit state with bottom-two weight
at most `2^-20` is entropy-valid. For tails through `1/29`, it separately
excludes all top-two cores with score above `10/3`, and all normalized core
spectra with smaller eigenvalue at most `1/5`. The high-score proof uses
the established Cheng--Hall monogamy and local-purity identities, finite
principal-angle estimates, and an exact scalar interval certificate.
Consequently any remaining witness has tail weight strictly between
`2^-20` and `1/29`, core score at most `10/3`, and smaller normalized core
eigenvalue greater than `1/5`. This does not cover every two-qubit state
or supply an arbitrary-block converse.

The [extended core theorem](docs/audits/EXTENDED_CORE_TRANSFER.md) now adds
`g(sigma)<=13/4` as a necessary witness condition whenever the tail weight
is at most `1/99`. It retains the stronger angular estimate
`L>=m(sqrt(u)-sqrt(v))^2`; a three-set anticommutation proof supplies the
decoder classification. An elementary argument proves the result through
`1/201`, and an exact one-variable certificate sharpens it to `1/99`.
The subsequent [curved-transfer theorem](docs/audits/CURVED_CORE_TRANSFER.md)
extends the same threshold through `1/29`: paired scalar-query gains and
the active/inactive score imbalance avoid the earlier inverse-bound loss.
Thus every remaining two-qubit witness has core score at most `13/4`.
No unrestricted all-size optimum or priority of the full two-parameter
profile is established.

Finally, [one-qubit stability](docs/ONE_QUBIT_STABILITY.md) supplies a
quantitative version of the equality characterization. A normalized seed
with deficit `delta<=1/48` has squared overlap at least `1-2delta/3`
with an exact subset seed, and squared Frobenius distance at most
`4delta/3` after phase alignment. Its branch-averaged consequence uses
the normalized Kraus weights; it does not assert channel-distance
closeness or input-independent physical branch probabilities.

The [primary-source audit](docs/audits/PROOF_AND_NOVELTY_AUDIT.md) establishes that the general framework [1,2] and exact endpoint [10] are prior. It gives an exact discrimination-task reduction, strict obstructions to importing full-outcome MUB or common-reconstruction converses, and a genuine achievability bridge from fixed-cap reconstruction codes [9]. It also identifies a false marginal-distortion invariance step in [9]; that is a source-proof gap, not a refutation of its theorem conclusion. See the [comparison ledger](docs/LITERATURE_COMPARISON.md) for locators and remaining novelty questions.

The [roof and joint-score continuation](docs/audits/ROOF_PROVENANCE_AND_JOINT_SCORE.md)
credits Vollbrecht–Werner's exact convex-roof principles, identifies the
whole Cope–Uola average-rank profile with incompatibility weight, and proves
that product repetition preserves an explicit local/joint score gap even
with collective readout. It reduces each two-qubit joint context to one
matrix-effect optimization, but does not solve the outer entropy problem.
This strengthens provenance and excludes particular proof routes; it
certifies neither publication originality nor unrestricted optimality.

## 9. Essential negative control: expectation estimation is easy classically

Suppose instead that the source can provide T independent copies of the same rho, and the desired outputs are estimates of the 2n expectation values. Apply the product POVM (3) to each copy. The estimators

\[
\widehat x_i=\sqrt2 a_i,\qquad \widehat z_i=\sqrt2 b_i
\]

are unbiased, and each has second moment 2. Within one copy the different sites' outcomes may be correlated; independence between copies suffices.

Hoeffding's inequality and a union bound imply that

\[
T\ge\frac4{\alpha^2}\ln\frac{4n}{\delta}
\tag{19}
\]

copies suffice to estimate all 2n means to additive accuracy alpha with total failure probability at most delta. No quantum memory need remain after the measurements. This elementary example lies in the broader measurement-record reuse territory of classical shadows [7]; general Pauli estimation and memory tradeoffs also have detailed existing theory [8].

The real-valued estimator can take values outside [-1,1], so it is not itself a physical binary decoder on one specimen. Repetition changes the resource model. Hence (19) does not contradict (17).

This control prevents a false claim of exponential sample savings. The proposed result is about preserving single-specimen future capabilities. It is not a general lower bound on estimating final solver outputs when fresh runs are available.

## 10. Reproducibility and limits of computation

`checks.py` uses only NumPy. It constructs all Kraus operators of the hybrid strategy for 1 <= n <= 4 and every 0 <= q <= n, then checks:

- parent POVM positivity, normalization, and marginals;
- trace preservation of the complete hybrid instrument;
- exact effective-observable identities for all local X/Z queries;
- unbiased estimator and second-moment identities;
- arithmetic values of the analytical lower and upper bounds.

Run:

```bash
python checks.py --max-n 4 --output checks.json
```

Recorded run: 14 (n,q) cases; largest input Hilbert dimension 16; maximum absolute matrix-entry residual 2.6645352591003757e-15, against tolerance 1e-10. Environment: Python 3.13.5, NumPy 2.3.5.

These checks verify an explicit construction at small size. They do not prove the lower bounds, test unrestricted optimality, establish novelty, or simulate a many-qubit hardware architecture. The general statements depend on the analytical proofs. New scripts check 43 one-qubit identities/examples and 10 product-diagonal cases, using Python 3.12.14 and NumPy 2.3.5. Commands, recorded residuals and limits are in [REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md).

## References and exact roles

[1] Marie Ioannou et al., *Simulability of high-dimensional quantum measurements*, arXiv:2202.12980; Physical Review Letters 129, 190401 (2022). Scenario/definition, Eqs. (1) and following: arbitrary-state compression by an instrument, free classical side channel, task-dependent decoder; purely classical case is joint measurability.

[2] Benjamin D. M. Jones et al., *Equivalence between simulability of high-dimensional measurements and high-dimensional steering*, arXiv:2207.04080; Physical Review A 107, 052425 (2023). Theorems 1–2 give dimensional measurement/steering relations; Section VI treats dimension witnesses including full-outcome mutually unbiased measurements. These should not be confused with the 2n binary local queries in this note.

[3] Andreas Bluhm, Lukas Rauber, Michael M. Wolf, *Quantum compression relative to a set of measurements*, arXiv:1708.04898. Essential compression precedent. Its reconstruction formulation must be checked against unrestricted query-dependent decoding rather than silently equated to it.

[4] Mario Berta, Matthias Christandl, Roger Colbeck, Joseph M. Renes, Renato Renner, *The Uncertainty Principle in the Presence of Quantum Memory*, arXiv:0909.0950; Nature Physics 6, 659–662 (2010). Eq. (2), plus the paper's Fano-based error-to-entropy argument, supplies the main ingredient of Section 5.

[5] Fernando G. S. L. Brandao, Matthias Christandl, Jon Yard, *Faithful Squashed Entanglement*, arXiv:1010.1750v5 (corrected 2012 version); Communications in Mathematical Physics 306, 805–830 (2011). Use the corrected **one-way LOCC** norm. Corollary 1 / Eq. (12) supplies the coefficient 1/(16 ln 2); Eq. (16) states monogamy.

[6] Matthias Christandl, Andreas Winter, *“Squashed Entanglement” — An Additive Entanglement Measure*, arXiv:quant-ph/0308088. Definition and basic entanglement-measure properties. Monogamy as used here is also explicitly stated with its attribution in [5].

[7] Hsin-Yuan Huang, Richard Kueng, John Preskill, *Predicting Many Properties of a Quantum System from Very Few Measurements*, arXiv:2002.08953; Nature Physics 16, 1050–1057 (2020). Context for reuse of classical measurement records across many observables. Equation (19) is derived directly above for this special workload.

[8] Sitan Chen, Weiyuan Gong, Qi Ye, *Optimal tradeoffs for estimating Pauli observables*, arXiv:2404.19105 (2024). Broad prior theory for Pauli estimation and memory–sample tradeoffs. Not a source for an asserted solution to the single-specimen rate R(eta).

[9] Igor Devetak, Toby Berger, *Quantum Rate-Distortion Theory for I.I.D. Sources*, arXiv:quant-ph/0011085v3. Fixed-length reconstruction with free classical side information and marginal entanglement-fidelity distortion. Theorem-level comparison, an achievability bridge and a Theorem 3 proof caveat are in audit Section 6.5. Its rate must not be identified with this binary-decoder optimum.

[10] Manuel A. Ballester, Stephanie Wehner, Andreas Winter, *State discrimination with post-measurement information*, arXiv:quant-ph/0608014v2. Section 5, Lemma 5.1 and Eq. (11), subsumes the exact endpoint. Audit Section 6.1 gives the exactly equivalent finite-error discrimination ensemble.

[11] Shuming Cheng, Michael J. W. Hall, *Anisotropic invariance and the distribution of quantum correlations*, arXiv:1610.09302v3; Physical Review Letters 118, 010401 (2017). Eq. (1) and Eqs. (13)–(14), with the following mixed-state extension, supply independent-setting three-qubit CHSH monogamy for the one-retained-qubit result. The publisher's note, PRL 118, 059901, does not alter that inequality.

[12] Thomas Cope, Roope Uola, *Quantifying the high-dimensionality of quantum devices*, arXiv:2207.05722v4. Eq. (7) compares worst-case compression; Section VI and Eqs. (20)–(22) give related state/assemblage entropy regularizations. Precise scope is compared in the entropy-rate note.

[13] Thomas Cope, *Entanglement cost for steering assemblages*, arXiv:2102.02333v2. Eqs. (5)–(6) define an asymptotic complete-assemblage task; this must not be identified with a single delayed local query.

[14] Salman Beigi, *Improved Quantum Hypercontractivity Inequality for the Qubit Depolarizing Channel*, arXiv:2105.00462v2 (9 December 2021). Theorem 2, Eqs. (6)–(7), printed p. 4, supplies the nonlinear entropy/Dirichlet bound. Theorem 4, p. 6, supplies a direct rank-constrained alternative. These are established ingredients.

[15] Koenraad M. R. Audenaert, Michael Nussbaum, Arleta Szkoła, Frank Verstraete, *Asymptotic Error Rates in Quantum Hypothesis Testing*, arXiv:0708.4282v1. Appendix A, Theorem 6, Eq. (55), printed p. 32, gives root fidelity squared at most affinity at exponent 1/2. Its use here is a matrix inequality, not an i.i.d. input assumption.
