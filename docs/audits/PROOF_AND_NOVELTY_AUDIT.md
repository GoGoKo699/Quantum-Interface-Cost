# Proof and novelty audit

**Reviewed commit:** [`eaf085a8cb299e6b297b11d2dc3c85e24f02779e`](https://github.com/GoGoKo699/Quantum-Interface-Cost/commit/eaf085a8cb299e6b297b11d2dc3c85e24f02779e)  
**Review date:** 22 September 2026  
**Branch:** `audit/proof-novelty-eaf085a`  
**Coordination:** [issue #1](https://github.com/GoGoKo699/Quantum-Interface-Cost/issues/1); Research Lead owns [issue #2](https://github.com/GoGoKo699/Quantum-Interface-Cost/issues/2) and integration.

This is an independent reconstruction and source comparison of the pinned dossier, not external peer review or a certification of publication novelty. The initial inspection found no audit report, open pull request, or comments on issues #1–#2. All files requested in `WORKSPACE_REVIEW_BRIEF.md`, that brief itself, and `AGENTS.md` were read. LICENSE is unchanged. This PR adds the report only; it does not revise the research problem or merge any conclusions into main.

## 1. Findings that affect the research decision

1. **The supplied baseline proofs and normalized-seed reduction survive this audit.** In particular, neither the entropic proof nor the squashed-entanglement proof assumes simultaneous execution of the local decoders. The seed is completed to a trace-preserving instrument, with the correct normalization and no postselection.
2. **There is an earlier direct precedent beyond the dossier's starting bibliography.** Ballester–Wehner–Winter (2006), Section 5, Lemma 5.1 and Eq. (11), subsumes the exact endpoint `q=n`. Their postmeasurement-information discrimination problem also contains an optimization equivalent to the present finite-error task after symmetry averaging. Section 6.1 below gives the reduction. This does not evaluate its intermediate-memory optimum.
3. **The distinction from reconstruction and full-outcome MUB problems is substantive and demonstrable.** At one qubit and zero quantum memory, a common reconstructed state permits equal X/Z contrast at most `1/2`, whereas the present task attains `1/sqrt(2)`. At two qubits and one retained qubit, the local protocol exceeds a published full-outcome MUB visibility bound without contradicting it.
4. **I.i.d. source averaging alone does not exclude rate-distortion achievability.** A finite-block reconstruction channel for the maximally mixed source can be symmetrized into a uniform arbitrary-input interface, retaining its worst-case memory dimension. The reverse implication fails. The precise bridge and a source-proof caveat are in Section 6.5.
5. **Two primary-source proof shortcuts need care.** Jones et al.'s transpose-composition shortcut has an elementary Kraus-conjugation repair. A unitary-invariance equality used in Devetak–Berger's Theorem 3 is false for their marginal distortion; an exact two-qubit counterexample is supplied below. These findings are not counterexamples to either theorem's conclusion, and do not invalidate the repository's independently reconstructed proofs.
6. **The sharp intermediate trade-off remains unresolved by this review.** No result inspected here establishes the candidate subset inequality, a strict collective advantage, or publication-level novelty of the positive-rate corollary. Failure to locate a settling theorem is not proof of its absence.

## 2. Operational model and quantifiers

Write `d=2^n`, `D=2^q`, with integer qubit budget `q>=0` and `n>=1`. An admissible encoder is a finite instrument `E_c: M_d -> M_D`, with `sum_c E_c` trace preserving. Smaller branch spaces can be embedded in the same D-dimensional output. The record alphabet is finite for each protocol but has no fixed bound. A binary decoder is a Hermitian contraction `B_(c,j)`; its effects are `(I ± B_(c,j))/2`. Thus its input observable is

$$
A_j=\sum_c\mathcal E_c^*(B_{c,j}).
$$

Only one query `j=(i,X/Z)` is executed. The requirement is the operator identity `A_j=eta P_j`, equivalent to the prescribed statistics for **every density operator on the whole n-qubit input**, including internally entangled inputs. No assumption of independent input qubits is used. The virtual reference introduced in proofs is not an operational resource.

The binary TV distance for a fixed input is `|Tr rho(A_j-P_j)|/2`; maximizing over states gives `||A_j-P_j||_infinity/2`. Pauli conjugation and matching sign relabeling project `A_j` onto `lambda_j P_j`, with

$$
\lambda_j=d^{-1}\operatorname{Tr}(P_jA_j)\ge1-2\epsilon.
$$

The last inequality follows from trace/operator-norm duality and `||P_j||_1=d`. Permutations and independent local Hadamards act transitively on the query set. Recording their random choice makes every coefficient equal to the average lambda. It remains at least `1-2epsilon`, and output flips reduce it to that exact target. All randomness and instrument outcomes fit in a finite free record. Conversely, `eta P_j` has worst-case TV error `(1-eta)/2`, attained on an eigenstate. The equivalence holds for `0<=epsilon<=1/2`; it is an equivalence of optimal memory costs, not a claim that every approximate protocol was already a depolarizing channel.

Neither arbitrary collective encoders nor any quantum system crossing the boundary may be removed from the optimization. Preshared entanglement, extra specimens, source reaccess, favorable-branch conditioning and average-memory accounting remain excluded throughout this report.

## 3. Claim-by-claim verdicts

| Pinned claim | Verdict | Evidence and qualification |
|---|---|---|
| Note §2: uniform TV / symmetric contrast equivalence | Correct as stated | Both finite twirls and output degradation preserve the resource bound; Section 2 above. |
| Note §3: `q=0` iff `eta<=1/sqrt(2)` | Correct as stated; established threshold | Positive parent POVM and separable witness give both directions. |
| Note §4: random-subset achievable contrast and ceiling | Correct as stated | Fixed-size subsets charge q on every branch; unconditional marginals are operator identities. |
| Note §5: entropic bound and exact endpoint | Correct as stated; standard-theorem corollary | Independent entropy derivation below; exact endpoint additionally subsumed by BWW. |
| Note §6: positive-rate lower bound | Correct as stated | Corrected one-way norm, factor, direction, monogamy and free-flag bound all check. |
| Note §6: `Theta(n)` above threshold | Correct with the stated fixed-eta qualification | Constants depend on eta; no uniform linear constant as eta approaches the threshold with n. |
| Note §7: integer rounding and rate limit | Correct under integer-qubit convention | Tensor-product protocols remain valid on entangled inputs; Fekete applies. |
| Seed reduction §§1–3 | Correct as stated | Full unrestricted converse and finite deterministic orbit completion; Section 5. |
| Seed reduction §4: spectral expression | Correct as stated | Complex vectorization and trace-norm duality; no convex optimization certificate implied. |
| `Gamma(n,2^q)<=2q+sqrt(2)(n-q)` | Unresolved | A candidate inequality only. The tests do not address global optimality. |
| Note §9: many-copy estimator | Correct as stated, for its different task | Range, second moment, copy independence and Hoeffding coefficient check. |
| Sharp-rate or collective-advantage novelty | Unresolved | General framework and several endpoints are prior results; exact remaining obstacle is Section 8. |

No incorrect theorem in the pinned repository was identified. Source-proof caveats are separately labeled in Section 6; a faulty argument is not automatically a false conclusion.

## 4. Independent checks of the converses and asymptotics

### 4.1 Entropic bound

For `omega_RB=(id_R tensor E)(Phi_RS)` and `B=CQ`, channel duality gives

$$
\operatorname{Tr}\omega(P_{R_i}\otimes B_{i,P})
=d^{-1}\operatorname{Tr}(P_i^T\mathcal E^*(B_{i,P}))=\eta.
$$

Here X and Z are real. Measuring either reference Pauli and the corresponding binary decoder gives disagreement probability `epsilon=(1-eta)/2`. Data processing followed by binary Fano yields `H(X_i|B)<=h2(epsilon)` and the analogous Z bound. On the state obtained by measuring all reference qubits in X,

$$
H(\mathsf X^n|B)=\sum_i H(\mathsf X_i|B\mathsf X_{<i})
\le\sum_i H(\mathsf X_i|B).
$$

Its single-site marginals are the ones just bounded: tracing out the other measured reference outcomes is the same as tracing out those reference systems. This is strong subadditivity on states, not a simultaneous decoder construction. Repeat separately for Z.

The two full reference bases have overlap `c=2^{-n}`. Applying Berta et al. [S4], Eq. (2), gives `H(X^n|B)+H(Z^n|B)>=n+H(R|B)`. Since C is classical,

$$
H(R|CQ)=\sum_c p_cH(R|Q)_{\omega^c}\ge-\log_2 D\ge-q.
$$

Consequently `q>=n[1-2h2(epsilon)]`. Every branch is included. This proves the claimed bound and, with retention of the full input, `q_min(n,1)=n`.

### 4.2 Squashed-entanglement bound

For `W_i=X_(R_i) tensor B_(i,X)+Z_(R_i) tensor B_(i,Z)`, the actual expectation is `2eta`. On every product state across `R_i:B`, the Bloch coordinates satisfy `x^2+z^2<=1` and decoder means satisfy `|u|,|v|<=1`; hence `xu+zv<=sqrt(2)`. Convexity extends this bound to all separable states across that cut, even if B contains arbitrary internal correlations.

The effect `T_i=I/2+W_i/4` is implemented by choosing X or Z uniformly, measuring R_i, sending basis and sign **from R_i to B**, and accepting agreement with the corresponding decoder. For `Delta=omega-sigma`, its trace is zero, and the binary measurement norm convention gives

$$
\|\Delta\|_{\mathrm{LOCC}\to}\ge2|\operatorname{Tr}T_i\Delta|
\ge\eta-1/\sqrt2
$$

when the final expression is positive. There is no extra factor of two. The corrected BCY Corollary 1 [S5] then gives `E_sq(R_i:B)>=(eta-eta0)^2/(16 ln2)`. The published erratum explicitly allows either one-way direction; an unrestricted-round LOCC norm must not replace it.

For clarity, the needed monogamy direction follows directly, for every extension F, from

$$
\tfrac12 I(B:R_1\cdots R_n|F)
=\tfrac12\sum_i I(B:R_i|FR_{<i})
\ge\sum_i E_{\rm sq}(B:R_i).
$$

Infimize over F and use symmetry. Each `FR_<i` is a legitimate extension of that marginal; reference independence is unnecessary. Koashi–Winter [S7] supplies the original monogamy theorem.

Finally choose the extension copying the classical record:

$$
\widetilde\omega_{RCQF}=\sum_c p_c\omega^c_{RQ}
\otimes|c\rangle\langle c|_C\otimes|c\rangle\langle c|_F.
$$

Then `E_sq(R:CQ)<=I(R:CQ|F)/2=sum_c p_c I(R:Q)_c/2<=log2 D<=q`. In particular, one must not use `log dim(CQ)` as the charged resource. Combining the inequalities proves the positive-part bound in Eq. (12) of the note. This is a valid application of established ingredients; the audit does not certify novelty of the application.

### 4.3 Finite size, limit, and negative control

The subset construction always retains exactly q physical qubits. Measuring the other sites and summing all outcomes is trace preserving, so it cannot change the unconditional retained-site marginal. Ceiling the needed q and degrading the contrast therefore works, including on entangled inputs.

For fixed eta, the tensor product of optimal block instruments yields the target local effects on either block tensored with the identity on the other block. Hence `q_min(n+m,eta)<=q_min(n,eta)+q_min(m,eta)` for arbitrary cross-block entanglement. Since `0<=q_min(n,eta)<=n`, Fekete's lemma gives the stated limit and infimum. The exact contrast target is retained at every block size; the rate definition has not been changed into average fidelity or an expected branch dimension.

For the many-copy control, `sqrt(2)a_i` and `sqrt(2)b_i` have range length `2sqrt(2)`, unbiased means and second moment 2. Hoeffding bounds each tail by `2 exp(-T alpha^2/4)`; a union bound over `2n` means gives the stated `T>=4 ln(4n/delta)/alpha^2`. Correlations across sites of one copy do not matter. These estimators take values outside `[-1,1]` and are not physical one-specimen binary answers.

## 5. Normalized-seed reduction

**Converse.** Finite input/output dimensions and a finite record allow finite Kraus refinement, with each `K_a` a D-by-d matrix. The old decoder can be retained on every refinement; permitting a better decoder only enlarges the optimization. Completeness gives `sum_a ||K_a||_F^2=d`. For nonzero branches put `L_a=K_a/||K_a||_F`. Taking the inner product of every effective-observable identity with its Pauli gives

$$
2n\eta=\frac1d\sum_{a,j}\operatorname{Tr}(B_{a,j}K_aP_jK_a^\dagger)
\le\sum_a\frac{\|K_a\|_F^2}{d}g(L_a)\le\Gamma(n,D).
$$

The weights really sum to one. No product, isometry, real-matrix, or flat-spectrum assumption has entered.

**Completion.** Given any normalized complex L, let `m=4^n` and `K_U=sqrt(d/m)LU` over Pauli representatives. The Pauli average of `L^dagger L` is `I/d`, so these Kraus operators are complete. For `B_j=sign(LP_jL^dagger)`, including sign zero equal to zero, trace-norm duality gives `v_j=||LP_jL^dagger||_1`. Character orthogonality gives

$$
\frac1m\sum_U s_{U,j}U^\dagger A U
=\frac{\operatorname{Tr}(P_jA)}d P_j.
$$

Multiplying by the Kraus prefactor d cancels the denominator exactly, producing `v_jP_j`. Schatten Hölder gives `0<=v_j<=1`, so these are physical contrasts. The outcome U is an **instrument outcome**, whose probability generally depends on the input; it is not independent randomness or a success flag. Every outcome is retained.

The additional independent permutation/Hadamard choice equalizes the v_j to `g(L)/(2n)`. This requires at most `4^n 2^n n!` classical labels, finite for each n, and quantum dimension at most D on every branch. Thus

$$
\eta_{\max}(n,q)=\Gamma(n,2^q)/(2n).
$$

Compactness of the complex Frobenius unit sphere and continuity give an actual maximizing seed. The finite orbit therefore establishes attainment even though the original classical alphabet had no prescribed size.

**Spectral form.** In input-then-output order define `|L>>=sum_(k,a) L_(a,k)|k>|a>`. Then

$$
\langle\!\langle L|(P_j^T\otimes B_j)|L\rangle\!\rangle
=\operatorname{Tr}(B_jLP_jL^\dagger).
$$

Both optimizations are maxima over compact independent domains, so they may be interchanged. Rayleigh–Ritz produces the displayed spectral expression. Real P_j does not justify restricting L or B_j to real matrices. A seesaw gives lower bounds on the maximum, not a global converse.

For `0<=q<=n`, the subset seed's score is `2q+sqrt(2)(n-q)`. Nothing above establishes that every seed lies below it. The reduction is a correct supplied specialization of known instrument/steering machinery; its independent novelty is unestablished.

## 6. Primary-source comparisons and deductions

All locators below refer to the exact versions in Section 7. A source's memory-dimension parameter is denoted D here, to avoid confusing it with the number n of input qubits.

### 6.1 Ballester–Wehner–Winter: direct earlier problem and exact endpoint

[S8] defines arbitrary ensembles indexed by a signal and a delayed classical label, with a q-qubit storage bound and unrestricted classical measurement records (pp. 2–3). Its Section 5, Lemma 5.1 (p. 20) and Eq. (11) (p. 21) characterize perfect prediction by the commutant of signal support projectors. The specialized two-label theorem is Theorem 6.3 (p. 24), not a theorem for an arbitrary number of delayed labels.

**Reduction derived in this audit.** Choose uniform prior `p_(s,j)=1/(4n)` and states

$$
\rho_{s,j}=(I+sP_j)/d.
$$

For any instrument and decoder with input observables A_j, the discrimination success is

$$
p_{\rm succ}=\frac12+\frac{1}{4nd}\sum_j\operatorname{Tr}(P_jA_j).
$$

The Pauli/query symmetry twirls preserve this score and yield uniform contrast `eta=2p_succ-1`. Conversely a contrast-eta protocol attains `(1+eta)/2` on this ensemble. The optimal discrimination score is therefore exactly equivalent to our uniform-error optimization, with unchanged timing and worst-case dimension. The ensemble is a mathematical comparison, not a replacement promise on the operational input.

At perfect success, Lemma 5.1 forces every refined effect `K_a^dagger K_a` to commute with `(I±P_j)/2` for all j. Local X_i,Z_i generate the full matrix algebra, whose commutant consists of scalars. Every nonzero effect thus has rank d, requiring `D>=d`. This is a direct prior-theorem corollary. The two-label/one-qubit theorem does not contradict it: our delayed label includes the site, giving `2n` labels.

**Novelty implication:** add this source to the Research Lead's main comparison ledger. Neither the general delayed-information framing nor the exact endpoint is a defensible novelty claim. The inspected evaluated cases do not determine the finite-error optimum for this `2n`-label ensemble.

### 6.2 Ioannou et al.: exact operational framework

[S1], published Eq. (1), p. 190401-2, is precisely the required instrument simulation when its dimensions are `d=2^n`, `D=2^q` and its effects are `(I+s eta P_j)/2`. The arbitrary-state statistics, branch-dependent decoder and classical side channel coincide. Published Result 1, Eq. (6), treats noisy MUBs. Result 2, Eq. (9), and Result 3, Eqs. (12)–(13), concern broader unitary symmetry/all-projective-measurement workloads.

**Deduction:** coarse-graining the two full product-basis outcomes to a chosen bit transfers their MUB construction to our task, with visibility `(d+D-2)/(2(d-1))`. At `(n,q)=(2,1)` it is `2/3`, below the hybrid construction. Coarse-graining transfers this achievability, not a converse in the reverse direction. The finite set of local X/Z queries does not have full-unitary invariance, so those covariance results cannot authorize flat-spectrum or projective seeds here.

**Novelty implication:** the simulation model is fully subsumed; these inspected formulae do not evaluate the local-query optimum.

### 6.3 Jones et al.: established steering correspondence; MUB obstruction

[S2], Theorems 1–2 and Eqs. (5)–(11), p. 052425-4, identify dimensional simulability with assemblage preparability. Taking `sigma_(s|j)=M^eta_(s|j)/d` gives full-rank marginal `I/d`. This is the applicable established correspondence; its rank-Kraus characterization is Lemma 1 in the published Appendix A. Section VI, Eqs. (20)–(21), p. 052425-6, instead bounds **two full d-outcome MUBs**.

**Concrete obstruction derived here:** for `d=4,D=2`, Eq. (21) bounds that full-outcome visibility by

$$
\frac{5\sqrt2-1}{3(\sqrt2+1)}=\frac{11-6\sqrt2}{3}\simeq0.838240.
$$

The local binary task attains `(1+1/sqrt(2))/2≈0.853553`. Thus the full-outcome bound cannot be imported into this task. Decoders for several local marginals need not form one executable joint decoder.

**Source-proof repair:** after Eq. (11), the proof treats composition of a partially entanglement-breaking channel with transpose as a channel of the same kind. This is false in general: the identity channel composed with transpose is not CP. Transpose invariance of simulability nevertheless follows directly from

$$
M^T=\sum_a K_a^T N_a^T\overline K_a
=\sum_a(\overline K_a)^\dagger N_a^T\overline K_a.
$$

Conjugated Kraus operators preserve completeness and rank; transposed POVMs are valid. This repairs the shortcut without changing the theorem or the repository reduction. No novelty is claimed for the repair.

### 6.4 Bluhm–Rauber–Wolf: reconstruction is an additional constraint

[S3], Definition 4.1 (pp. 5–6), requires compression and a common CPTP decompression map. Its Theorem 6.1 (p. 9) is an algebraic lower bound in that model. Section 9.1 (p. 26) explicitly distinguishes arbitrary query-dependent compressed effects and explains why they permit stronger compression. Accordingly, its reconstruction converses are not automatically converses here.

**Workload-specific obstruction derived here:** at `n=1,q=0`, a reconstructed-state channel is measure-and-prepare. Write its effects as `G_c=alpha_c(I+r_c·sigma)`, with `sum alpha_c=1`, `|r_c|<=1`, and prepared Bloch vectors t_c with `|t_c|<=1`. Equal X/Z transfer coefficients satisfy

$$
2\eta=\sum_c\alpha_c(r_{cx}t_{cx}+r_{cz}t_{cz})\le1.
$$

This bound is attained by randomly measuring and repreparing X or Z. Our physical binary decoders attain `eta=1/sqrt(2)` instead. Thus even for the present observables, requiring a common reconstruction is a strict finite-accuracy restriction. The exact endpoint has a valid direct route through [S8]; no unjustified reconstruction assumption is needed.

### 6.5 Devetak–Berger: a real achievability bridge, not a converse identification

[S9], Eqs. (12)–(14), p. 4, uses fixed-length compression/decompression of an i.i.d. source and the average of marginal entanglement-fidelity distortions. Its free-classical construction uses outcome-conditioned compression. Theorem 2 (pp. 10–11) handles diagonal operations; Theorem 3 (p. 13) asserts the isotropic-source extension. Eqs. (22)–(24), p. 7, give the achievable isotropic curve `f(delta)=h2(1/2+sqrt(delta(1-delta)))` for `0<=delta<=1/2`. These are statements about reconstructed quantum outputs, not independently selectable binary decoders.

**Bridge derived here.** Let N be any actual finite-block reconstructed channel with input maximally mixed, fixed quantum bottleneck dimension D, and distortion

$$
\delta=\frac1n\sum_i\bigl(1-F_e(I/2,N_i)\bigr).
$$

Define `t_(i,P)=d^{-1}Tr[P_i N^*(P_i)]`. For each marginal,
`F_e=(1+t_(i,X)+t_(i,Y)+t_(i,Z))/4`. Pauli twirling removes unwanted input coefficients. Independent local Clifford twirls and site permutations equalize all the displayed diagonal coefficients. They can be implemented before encoding and in the decoder with a finite classical flag. The resulting effective X/Z observables are exactly

$$
\left(1-\frac{4\delta}{3}\right)P_j.
$$

The operator identities hold on every input, including entangled inputs, and the bottleneck D is unchanged. Thus the achievable source curve gives `R(eta)<=f(3(1-eta)/4)` in particular for the nonclassical range of this project. For asymptotic distortion, use strict slack above the desired contrast and then output degradation; an expected branch entropy alone is not a fixed-dimensional protocol. Atypical outcomes must be handled by a trace-preserving fixed-cap code, not discarded or allowed extra memory. This is a legitimate achievable bound, not an identification of the optimum.

The reconstruction obstruction in Section 6.4 blocks identifying the reverse direction. Also, X/Z statistics alone place no required value on the Y transfer coefficient in entanglement fidelity. Therefore even an exact reconstruction rate curve cannot simply be relabeled as `R(eta)`.

**Source-proof caveat, with an exact counterexample.** The proof of Theorem 3 asserts `d_e(E_A)=d_e(E_(VUD))` for `A=UDV`, with arbitrary unitaries U,V and positive diagonal D. Under the source's own marginal distortion this equality fails. Take two qubits, `A=I tensor Z`, `D=I_4`, `V=CNOT` (first qubit controls the second), and `U=(I tensor Z)CNOT`. Then `UDV=A` but `VUD=Z tensor Z`. The first channel has marginal entanglement fidelities `(1,0)` and distortion `1/2`; the second has `(0,0)` and distortion `1`. Both are trace-preserving unitary channels, so normalization and selective branches are not the issue. Global entanglement fidelity would be invariant under this conjugation, but the average marginal fidelity in Eqs. (12)–(13) is not.

The failure is not limited to degenerate singular values: with the same U,V and `D=diag(1,3/4,1/2,1/4)`, the source's normalized marginal fidelities are `(5/6,1/30)` for UDV and `(2/15,1/30)` for VUD, giving distortions `17/30` and `11/12`. These trace-decreasing single-Kraus operations are allowed at that proof step, which explicitly drops trace preservation.

This refutes the displayed invariance step, **not** the claimed optimal curve. The examples do not contradict the subsequent inequality against D, and a different proof could establish the theorem. Achievable single-qubit constructions and the bridge above remain usable. The later rate-distortion treatment [S13], Theorem 10, gives a regularized entanglement-of-formation characterization with a common reconstructed output. Its Theorem 12 restates the isotropic curve but explicitly imports the single-letter reduction from [S9]; that passage does not repair the identified step. This review does not certify that converse from these arguments. Locating a replacement proof is a precise remaining literature task if the Research Lead wishes to use it.

### 6.6 Bounded/noisy storage and random-access codes

| Source and exact locator | Resource/error map | Conclusion for this project |
|---|---|---|
| König–Wehner–Wullschleger [S10], §I.C p. 2; Theorem III.3 p. 12 | Arbitrary preprocessing, free classical record and storage channel; choosing the identity storage channel matches a q-qubit bound. The theorem controls smooth min entropy of a whole BB84 string after its basis string is revealed. | Relevant machinery, but whole-string unpredictability does not bound a single chosen binary answer at the claimed sharp rate. Multiplying marginal guessing probabilities is unjustified. |
| Dupuis–Fawzi–Wehner [S11], Theorem 15 p. 22; Theorem 9 p. 16 | Strong whole-string weak-string-erasure bounds; a separate theorem concerns fidelity of recovery of k quantum subsystems. | Neither displayed theorem is a local binary-decoder trade-off. The Theorem 9 bound on squared fidelity, with its `sqrt(n^2+1)` prefactor, is vacuous for the single-qubit-subsystem use proposed here. This does not exclude a more sophisticated future reduction. |
| Nayak [S12], Theorem 2.3 p. 2 | Encodes known classical strings; charges the total message dimension for random bit retrieval. | Substituting q while ignoring the unlimited input-dependent record C is invalid: a known classical string could simply be stored in C. It is not a converse for an unknown quantum specimen with free classical output. |

The inspected storage results do not silently grant simultaneous local decoders. They should remain part of the novelty search, with the success criterion translated explicitly.

## 7. Exact primary sources inspected

Page numbers are printed pages unless article-number pagination is given. ArXiv and published numbering sometimes differ.

- **[S1]** Ioannou et al., *Simulability of high-dimensional quantum measurements*. [arXiv:2202.12980v1](https://arxiv.org/abs/2202.12980v1), 25 February 2022; [published PRL 129, 190401 (2022), author-hosted PDF](https://access.archive-ouverte.unige.ch/access/metadata/ca3f97fb-c9eb-4b5c-ac93-1f8d12ab7343/download). Published Eq. (1), Result 1/Eq. (6), Result 2/Eq. (9), Result 3/Eqs. (12)–(13), Claim 5/Eq. (16). ArXiv v1 calls Results 1–3 Claims and numbers Claim 5's formula (17).
- **[S2]** Jones et al., *Equivalence between simulability of high-dimensional measurements and high-dimensional steering*. [arXiv:2207.04080v1](https://arxiv.org/abs/2207.04080v1), 8 July 2022; [published PRA 107, 052425 (2023), author-hosted PDF](https://access.archive-ouverte.unige.ch/access/metadata/d77fd1bd-22e0-450d-8d69-36effc95d1ac/download). Theorems 1–2 and Proposition 1, p. 052425-4; Eqs. (20)–(21), p. 052425-6; Lemma 1, Appendix A, p. 052425-8 (Proposition 3 in arXiv v1).
- **[S3]** Bluhm–Rauber–Wolf, *Quantum compression relative to a set of measurements*. [arXiv:1708.04898v4](https://arxiv.org/abs/1708.04898v4). Definition 4.1, Theorem 6.1, §9.1, and the surrounding reconstruction definitions were inspected in the 40-page text.
- **[S4]** Berta et al., *The Uncertainty Principle in the Presence of Quantum Memory*. [arXiv:0909.0950v4](https://arxiv.org/abs/0909.0950v4), 1 March 2011. Eq. (2), p. 2, and the Fano-based error bound on that page. These are the precise prior ingredients used in Section 4.1.
- **[S5]** Brandão–Christandl–Yard, *Faithful Squashed Entanglement*. [arXiv:1010.1750v5](https://arxiv.org/abs/1010.1750v5), 20 July 2012. One-way norm and Theorem Eq. (9), p. 4; Corollary 1/Eq. (12), p. 5; monogamy Eq. (16), p. 6. Also both pages of the [published erratum, CMP 316, 287–288 (2012)](https://link.springer.com/content/pdf/10.1007/s00220-012-1584-y.pdf), especially p. 287 Eq. (1). The erratum keeps `1/(8 ln2)` for conditional mutual information, hence `1/(16 ln2)` for squashed entanglement. The stronger-looking coefficient in v5 Eq. (97) is inconsistent with its theorem/corollary and must not be used to strengthen this project bound.
- **[S6]** Christandl–Winter, *“Squashed Entanglement” — An Additive Entanglement Measure*. [quant-ph/0308088v3](https://arxiv.org/abs/quant-ph/0308088v3), 23 November 2003. Definition 1 p. 1; Proposition 3 p. 2; Proposition 4 p. 3.
- **[S7]** Koashi–Winter, *Monogamy of entanglement and other correlations*. [quant-ph/0310037v1](https://arxiv.org/abs/quant-ph/0310037v1). Theorem 8/Eq. (13), p. 6, is a direct monogamy citation.
- **[S8]** Ballester–Wehner–Winter, *State Discrimination with Post-Measurement Information*. [quant-ph/0608014v2](https://arxiv.org/abs/quant-ph/0608014v2), 5 September 2006. General problem pp. 2–3; §5, Lemma 5.1 p. 20, Eqs. (8)–(11) p. 21; Theorem 6.3 p. 24.
- **[S9]** Devetak–Berger, *Quantum Rate-Distortion Theory for I.I.D. Sources*. [quant-ph/0011085v3](https://arxiv.org/abs/quant-ph/0011085v3), 1 March 2002. Eqs. (12)–(16), pp. 4–5; Eqs. (22)–(24), p. 7; Theorems 2–3, pp. 10–13; physical coding construction §5, p. 14.
- **[S10]** König–Wehner–Wullschleger, *Unconditional security from noisy quantum storage*. [arXiv:0906.1030v4](https://arxiv.org/abs/0906.1030v4). §I.C p. 2 and Theorem III.3 p. 12.
- **[S11]** Dupuis–Fawzi–Wehner, *Entanglement sampling and applications*. [arXiv:1305.1316v3](https://arxiv.org/abs/1305.1316v3). Theorems 9 and 15, pp. 16 and 22.
- **[S12]** Nayak, *Optimal lower bounds for quantum automata and random access codes*. [quant-ph/9904093v3](https://arxiv.org/abs/quant-ph/9904093v3). Theorem 2.3, p. 2.
- **[S13]** Wilde–Datta–Hsieh–Winter, *Quantum Rate Distortion Coding with Auxiliary Resources*. [arXiv:1212.5316v3](https://arxiv.org/abs/1212.5316v3), 26 June 2013. Theorem 10/Eq. (14), p. 6; Theorem 12 and its explicit reliance on [S9], p. 9.

This is a targeted theorem-level audit of these sources and their relevant connections, not an exhaustive proof that no later paper settles the candidate rate.

## 8. Narrowest defensible next target

Keep the exact unrestricted finite-block problem in issue #2. The first concrete target is to determine whether

$$
\max_{L\in\mathbb C^{2\times4},\,\|L\|_F=1}
\sum_{P\in\{X_1,Z_1,X_2,Z_2\}}\|LPL^\dagger\|_1
=2+\sqrt2.
$$

A strict violating seed must be explicit and completed by the audited instrument; a numerical seesaw value should first be treated as a candidate. A proof of equality must cover every complex seed and singular-value spectrum. The equivalent BWW ensemble gives an additional precise formulation for the next literature search. Solving only this block is a useful diagnostic, not a proof of the asymptotic curve.

For a publishable theorem-led project, the broader result must establish a genuinely new sharp region, an unrestricted collective advantage, or a quantitatively useful converse beyond the existing ingredients, with its closest prior comparisons resolved. The positive-rate result is mathematically supported here but has not independently cleared that novelty gate. Do not replace the workload with reconstruction, many-copy estimation, average memory, or a restricted encoder class to obtain an easier theorem under the same name.

Recommended integration changes for the Research Lead: add [S8] and its exact-endpoint corollary to the literature/status ledger; mark the supplied proofs and seed reduction as checked by this internal audit; retain the unresolved optimality and novelty labels; record the one-way rate-distortion bridge and the source-proof caveats. The audit does not recommend changing the model or claiming manuscript readiness.

## 9. Actual execution and evidence limits

Environment: Linux x86_64, Python **3.12.14**, NumPy **2.3.5**, CPU only. The repository scripts were inspected and run unchanged. Output JSONs were written outside the checkout; no recorded baseline was overwritten.

```bash
python checks.py --max-n 4 --output /workspace/scratch/8da5d91e801c/baseline-audit.json
python tools/check_seed_twirl.py --output /workspace/scratch/8da5d91e801c/seed-audit.json
```

| Actual check | Result |
|---|---|
| All 14 baseline `(n,q)` constructions, n through 4 | PASS; max absolute matrix-entry residual `2.6645352591003757e-15` |
| All 10 seed-twirl constructions, n=1,2; fixed seed 20260922 | PASS; max residual `3.1086244689504383e-15` |
| Tolerance in both runs | `1e-10` |
| Independent two-qubit source-counterexample calculation | `UDV=A` residual 0; `VUD=Z tensor Z` exactly; marginal fidelities `(1,0)` and `(0,0)` up to floating-point rounding, confirming exact distortions `1/2` and `1` |

The main construction residuals match the pinned recorded runs despite the Python patch/minor-version difference. No solver, optimization search, large simulation, hardware experiment, or hosted CI was used to support this report. The scripts do not test the lower-bound arguments or novelty. Those verdicts rest on the derivations and theorem-level comparisons above.
