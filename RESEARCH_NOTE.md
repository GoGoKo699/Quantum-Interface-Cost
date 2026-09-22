# Q1 — Delayed local readout through a bounded quantum interface

**Version:** 0.3, 2026-09-22

**Project:** Falling / Q1  
**Status:** Baseline proofs and seed reduction independently checked within the audit workspace. New analytical results give the exact one-retained-qubit optimum for every block size, an entropy bound for product-diagonal seeds, and a regularized entropy characterization of the asymptotic rate. Further work supplies a logarithmic-Sobolev memory converse and the exact score at every rank-two spectrum. General rate evaluation and publication novelty remain unresolved. This is a research dossier, not external peer review or a claim of a new framework.

## 1. Origin, scope, and claim ledger

Page 24 of the user-supplied *【马兆】坠落.pdf* describes a fictional progression from a quantum solver to a quantum-resident workflow because repeated classical–quantum interfaces become costly. The present model is our proposed scientific extraction; its assumptions and conclusions are not claims made by the fiction.

The general compression problem below is already present in the dimensional measurement-simulability framework of Ioannou et al. [1]. Connections between that framework, steering assemblages, and Schmidt number are established by Jones et al. [2]. Earlier quantum compression relative to measurements is also essential prior art [3]. We therefore do **not** propose a new definition of quantum interface cost as the contribution.

| Item | Status and provenance |
|---|---|
| Arbitrary quantum encoding, unlimited classical side information, delayed measurement choice | Established framework [1,2]. |
| Classical simulability equals joint measurability | Established framework [1,2]; elementary qubit construction below. |
| Exact preservation of all local X/Z readouts requires n retained qubits | Derived below; also subsumed by Ballester–Wehner–Winter [10], Lemma 5.1. |
| Uniform-random-subset hybrid construction | Explicit elementary achievable strategy; optimal for q=1 by the subsequent all-n theorem, and at the endpoints. General optimality unresolved. |
| Exact optimum and maximizing seeds with one retained qubit | Derived and independently checked from Cheng–Hall monogamy [11]; see Section 8 and the full proof. |
| Entropy bound for product-diagonal Gram matrices | Derived and independently checked, allowing correlated spectra and arbitrary local bases; does not restrict unrestricted encoders. |
| Entropic finite-error lower bound | Direct application of Berta et al. [4], Fano, and conditional-entropy inequalities. |
| Stronger logarithmic-Sobolev converse throughout the nonclassical region | Derived and independently checked from Beigi [14] and the root-fidelity inequality [15]; unrestricted encoder bound. |
| Exact maximum score at any rank-two spectrum | Derived and independently checked for arbitrary eigenvectors; excludes all rank-two entropy witnesses. |
| Positive linear memory for every fixed contrast above 1/sqrt(2) | Derivation below using a two-setting witness and faithful, monogamous squashed entanglement [5,6]. Independent novelty not established. |
| Regularized entropy characterization of the asymptotic rate | Derived and independently checked; fixed-cap coding and scalar-contrast continuity are proved; no closed-form evaluation. |
| Sharp evaluation of the asymptotic memory rate, or a strict collective-coding improvement | Candidate research target; not solved here and not yet certified absent from the literature. |
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

No lower bound in this note assumes that the optimum retains individual input qubits. Arbitrary collective coding is allowed. The new theorem in Section 8 settles q=1; the general intermediate-memory optimization in (6) remains unresolved.

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

Then, with `L_new(eta)=max{L(eta),b(eta)}`,

$$
q_{\min}(n,\eta)\ge\lceil n L_{\rm new}(\eta)\rceil.
$$

This deduction applies Beigi's improved quantum logarithmic-Sobolev inequality [14, Theorem 2] to a normalized seed's square root, combines root fidelity squared with affinity [15, Appendix A, Theorem 6], and uses a Pauli-Fourier comparison. Each refined branch has entropy at most q, so the proof preserves worst-case dimension and unrestricted collective encoding. No typical-input promise or additional specimen is used. The hybrid construction still gives (6).

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

| Worst-case TV error epsilon | Contrast eta | Earlier baseline lower bound | Strengthened lower bound | Achievable upper bound |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 |
| 0.01 | 0.98 | 0.8384137282 | 0.8872964169 | 0.9317157288 |
| 0.05 | 0.90 | 0.4272060858 | 0.4929364851 | 0.6585786438 |
| 0.10 | 0.80 | 0.0620088128 | 0.1414405425 | 0.3171572875 |
| 0.14 | 0.72 | 0.0000149892 | 0.0043926999 | 0.0440202025 |
| epsilon_0 | eta_0 | 0 | 0 | 0 |

The wide gap near eta_0 is real in the bounds, not evidence that the true rate is small or that the upper curve is optimal. For t down to zero, the new lower bound has

$$
b(\eta_0+t)=4t^2\log_2(1/t)+O(t^2),
\qquad b(1-t)=1-\frac4{\ln2}t+O(t^2).
$$

It improves the near-threshold quadratic baseline by a logarithmic factor and gives a linear approach to the exact-readout endpoint. These are asymptotics of a necessary bound, not an evaluation of R.

## 8. Exact one-qubit result and the remaining target

The subsequent [one-qubit theorem](docs/ONE_QUBIT_OPTIMALITY.md) proves, for every n>=1,

$$
\eta_{\max}(n,1)=\frac1{\sqrt2}+\frac1n\left(1-\frac1{\sqrt2}\right),
\qquad \Gamma(n,2)=2+\sqrt2(n-1).
$$

The proof reduces extreme qubit decoders to scalar signs or Bloch observables, then uses Cheng–Hall's three-qubit CHSH monogamy [11]. Their theorem permits different measurement settings on the common qubit and mixed states, exactly as required for site-dependent decoders and three-qubit marginals. Equality forces every maximizing normalized seed to retain one site and project the rest onto product bisectors, up to output unitaries. This characterizes refined branch maps, without assuming that the retained site is chosen independently of the input.

Thus the former n=2,q=1 diagnostic is settled, including the entire two-input-qubit memory function. For general n, the first nonclassical interval has exact memory one. The argument does not extend to a higher-dimensional central memory: two Bell pairs provide an explicit counterexample to its key pair inequality.

A separate [entropy argument](docs/COMMUTING_SEED_BOUND.md) proves

$$
g(L)\le\sqrt2\,n+(2-\sqrt2)S(L^\dagger L)
\le\sqrt2\,n+(2-\sqrt2)\log_2\operatorname{rank}(L)
$$

whenever the Gram matrix is diagonal in a fixed product of local one-qubit bases. Its eigenvalues may be correlated and nonuniform, and the axes may have Y components. Consequently, this entire structured family cannot improve the subset benchmark. The unrestricted problem has not been narrowed by assumption. A proposed extension using a local quantum conditional-entropy inequality is false; the note gives a two-qubit counterexample, separately from the unresolved global inequality.

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

The smallest remaining finite-block diagnostic is n=3,q=2, with subset seed score `4+sqrt(2)`. The main target remains a sharp rate evaluation, or a proven collective advantage with meaningful converses. These deductions have independently checked proofs within the workspace, but their publication novelty is unestablished.

The [primary-source audit](docs/audits/PROOF_AND_NOVELTY_AUDIT.md) establishes that the general framework [1,2] and exact endpoint [10] are prior. It gives an exact discrimination-task reduction, strict obstructions to importing full-outcome MUB or common-reconstruction converses, and a genuine achievability bridge from fixed-cap reconstruction codes [9]. It also identifies a false marginal-distortion invariance step in [9]; that is a source-proof gap, not a refutation of its theorem conclusion. See the [comparison ledger](docs/LITERATURE_COMPARISON.md) for locators and remaining novelty questions.

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
