# Q1 — Delayed local readout through a bounded quantum interface

**Version:** 0.1, 2026-09-22  
**Project:** Falling / Q1  
**Status:** Explicit model, proved baseline bounds, deterministic construction checks. Main finite-accuracy rate and publication novelty remain unresolved. This is a research dossier, not a manuscript or a claim of a new framework.

## 1. Origin, scope, and claim ledger

Page 24 of the user-supplied *【马兆】坠落.pdf* describes a fictional progression from a quantum solver to a quantum-resident workflow because repeated classical–quantum interfaces become costly. The present model is our proposed scientific extraction; its assumptions and conclusions are not claims made by the fiction.

The general compression problem below is already present in the dimensional measurement-simulability framework of Ioannou et al. [1]. Connections between that framework, steering assemblages, and Schmidt number are established by Jones et al. [2]. Earlier quantum compression relative to measurements is also essential prior art [3]. We therefore do **not** propose a new definition of quantum interface cost as the contribution.

| Item | Status and provenance |
|---|---|
| Arbitrary quantum encoding, unlimited classical side information, delayed measurement choice | Established framework [1,2]. |
| Classical simulability equals joint measurability | Established framework [1,2]; elementary qubit construction below. |
| Exact preservation of all local X/Z readouts requires n retained qubits | Derived below from standard uncertainty relations; not a novelty claim. |
| Uniform-random-subset hybrid construction | Explicit elementary achievable strategy; not asserted optimal or novel. |
| Entropic finite-error lower bound | Direct application of Berta et al. [4], Fano, and conditional-entropy inequalities. |
| Positive linear memory for every fixed contrast above 1/sqrt(2) | Derivation below using a two-setting witness and faithful, monogamous squashed entanglement [5,6]. Independent novelty not established. |
| Exact asymptotic memory rate, or a strict collective-coding improvement | Candidate research target; not solved here and not yet certified absent from the literature. |
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

No lower bound in this note assumes that the optimum retains individual input qubits. Arbitrary collective coding is allowed and is precisely the issue left unresolved by (6).

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

This proof is an application of established uncertainty and entropy results, not a new uncertainty relation. The entropic coefficient is positive only in the smaller-error part of the nonclassical region; a different argument is needed immediately above eta_0.

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

This derivation has not received independent proof review. The cited entanglement theorems are established; the derivation in this task and its novelty status are separate matters. The coefficient is weak and is not offered as an optimal rate.

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

Then q_min(n,eta) >= ceil[n L(eta)]. The hybrid construction gives (6).

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
L(\eta)\le R(\eta)\le\frac{\eta-\eta_0}{1-\eta_0}.
\tag{18}
\]

Numerical evaluation of these proved formulas, not simulation data:

| Worst-case TV error epsilon | Contrast eta | Necessary asymptotic rate lower bound | Achievable rate upper bound |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 |
| 0.01 | 0.98 | 0.8384137282 | 0.9317157288 |
| 0.05 | 0.90 | 0.4272060858 | 0.6585786438 |
| 0.10 | 0.80 | 0.0620088128 | 0.3171572875 |
| 0.14 | 0.72 | 0.0000149892 | 0.0440202025 |
| epsilon_0 | eta_0 | 0 | 0 |

The wide gap near eta_0 is real in the bounds, not evidence that the true rate is small or that the upper curve is optimal.

## 8. Candidate contribution and decisive next question

The specific candidate is **the sharp asymptotic quantum-interface rate for delayed local complementary readouts, with unlimited classical storage and arbitrary collective encoders**.

A useful next result would either show that collective coding beats the uniformly random subset construction or prove an optimal tradeoff over a nontrivial interval. The smallest diagnostic is n=2, q=1: the explicit construction gives eta=(1+1/sqrt(2))/2. Failure to improve it by a restricted ansatz would not prove optimality.

The publication decision remains gated by a theorem-level novelty audit. The general framework [1], the state/measurement/steering equivalence [2], and the use of standard uncertainty or entanglement measures are not sufficient contributions on their own. Priority comparisons include bounded/noisy quantum storage, quantum random-access encodings, one-way steering dimension bounds, and quantum rate-distortion with free classical side information. In particular, Devetak and Berger [9] is an important additional lead; its entanglement-fidelity distortion and source model cannot be silently identified with the task-specific decoder model here. A full theorem-level translation has not yet been completed.

The present dossier gives a stable problem and checked proofs worth versioning. It does not establish that the remaining rate question is absent from all prior work, nor that the baseline threshold by itself warrants publication.

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

These checks verify an explicit construction at small size. They do not prove the lower bounds, test unrestricted optimality, establish novelty, or simulate a many-qubit hardware architecture. The general statements depend on the proofs in Sections 3–7.

## References and exact roles

[1] Marie Ioannou et al., *Simulability of high-dimensional quantum measurements*, arXiv:2202.12980; Physical Review Letters 129, 190401 (2022). Scenario/definition, Eqs. (1) and following: arbitrary-state compression by an instrument, free classical side channel, task-dependent decoder; purely classical case is joint measurability.

[2] Benjamin D. M. Jones et al., *Equivalence between simulability of high-dimensional measurements and high-dimensional steering*, arXiv:2207.04080; Physical Review A 107, 052425 (2023). Theorems 1–2 give dimensional measurement/steering relations; Section VI treats dimension witnesses including full-outcome mutually unbiased measurements. These should not be confused with the 2n binary local queries in this note.

[3] Andreas Bluhm, Lukas Rauber, Michael M. Wolf, *Quantum compression relative to a set of measurements*, arXiv:1708.04898. Essential compression precedent. Its reconstruction formulation must be checked against unrestricted query-dependent decoding rather than silently equated to it.

[4] Mario Berta, Matthias Christandl, Roger Colbeck, Joseph M. Renes, Renato Renner, *The Uncertainty Principle in the Presence of Quantum Memory*, arXiv:0909.0950; Nature Physics 6, 659–662 (2010). Eq. (2), plus the paper's Fano-based error-to-entropy argument, supplies the main ingredient of Section 5.

[5] Fernando G. S. L. Brandao, Matthias Christandl, Jon Yard, *Faithful Squashed Entanglement*, arXiv:1010.1750v5 (corrected 2012 version); Communications in Mathematical Physics 306, 805–830 (2011). Use the corrected **one-way LOCC** norm. Corollary 1 / Eq. (12) supplies the coefficient 1/(16 ln 2); Eq. (16) states monogamy.

[6] Matthias Christandl, Andreas Winter, *“Squashed Entanglement” — An Additive Entanglement Measure*, arXiv:quant-ph/0308088. Definition and basic entanglement-measure properties. Monogamy as used here is also explicitly stated with its attribution in [5].

[7] Hsin-Yuan Huang, Richard Kueng, John Preskill, *Predicting Many Properties of a Quantum System from Very Few Measurements*, arXiv:2002.08953; Nature Physics 16, 1050–1057 (2020). Context for reuse of classical measurement records across many observables. Equation (19) is derived directly above for this special workload.

[8] Sitan Chen, Weiyuan Gong, Qi Ye, *Optimal tradeoffs for estimating Pauli observables*, arXiv:2404.19105 (2024). Broad prior theory for Pauli estimation and memory–sample tradeoffs. Not a source for an asserted solution to the single-specimen rate R(eta).

[9] Igor Devetak, Toby Berger, *Quantum Rate-Distortion Theory for I.I.D. Sources*, arXiv:quant-ph/0011085. Additional audit lead: quantum compression with classical side information and entanglement-fidelity distortion. Abstract-level screening completed; full theorem comparison with the present target remains to be done.
