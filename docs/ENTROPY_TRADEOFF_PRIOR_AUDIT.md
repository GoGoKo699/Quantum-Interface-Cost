# Prior-source audit of the entropy tradeoffs

Date: 2026-09-23. Repository base inspected:
`3ebde02b2d9d5dcdcd0dd445e4a16b4f5aaf03b0`.
This note supplements the historical proof audit. It checks primary theorem
statements and gives the reductions below; it does not certify publication
novelty or a complete literature search. Page numbers are printed PDF pages.
No numerical search or simulation is used as evidence here.

## 1. Findings and status

1. The coordinatewise cube inequality in
   [ASYMMETRIC_ENTROPIC_CONVERSE.md](ASYMMETRIC_ENTROPIC_CONVERSE.md), Eq. (6),
   is a direct corollary of known coherence-of-formation superadditivity and
   the known qubit formula. It is not a new tensorization principle.
2. The quantum entropy penalty in that note also has an exact older
   entropy-production derivation, using the binary Holevo/fidelity bound
   of Roga–Fannes–Życzkowski. Combining these ingredients reproduces the
   asymmetric state bound, without invoking a simultaneous decoder.
3. The lower convex envelope of **all one-qubit seed entropy profiles** is
   exactly the existing steering entanglement of formation of the noisy
   orthogonal-Pauli assemblage. Section 4 proves this identification. An
   explicit evaluation of this envelope is consequently an evaluation of
   an established resource, not a new definition of measurement entropy.
4. The inspected information-combining theorems do not settle the sharp
   unrestricted seed inequality. Their independence assumptions and
   entropy orders prevent the direct substitutions described below.

These conclusions preserve one unknown specimen, one delayed local query,
arbitrary collective physical encoders, free finite classical records,
worst-case quantum dimension, and uniform input/query effects. A restriction
on Gram matrices, when explicitly made, defines a comparison class and does
not replace the unrestricted model.

## 2. Exact coherence provenance of the cube inequality

Use bits and

\[
f(c)=h_2\!\left(\frac{1-\sqrt{1-c^2}}2\right),\qquad
C_i(p)=\sum_u\sqrt{p_up_{u+e_i}}.
\]

| Primary source and exact version | Locator and established ingredient |
|---|---|
| Liu–Ding–Tong, *Superadditivity of convex roof coherence measures*, [1809.05475v1](https://arxiv.org/pdf/1809.05475v1), 14 September 2018 | Unnumbered theorem, Section 3, pp. 4–5; Section 4.1, Eqs. (4.1)–(4.5), pp. 5–6: coherence of formation satisfies \(C_f(\tau_{AB})\ge C_f(\tau_A)+C_f(\tau_B)\). |
| Yuan–Zhou–Cao–Ma, *Intrinsic randomness as a measure of quantum coherence*, [1505.04032v1](https://arxiv.org/pdf/1505.04032v1), version stamp 15 May 2015 | Convex-roof definition Eq. (6), p. 3; qubit formula Eq. (8) and following text, p. 4: \(C_f(\tau)=f(2|\tau_{01}|)\). Use the version stamp, not the PDF's later generated date header. |
| Winter–Yang, *Operational Resource Theory of Coherence*, [1506.07975v3](https://arxiv.org/pdf/1506.07975v3), 19 January 2016 | Theorem 9, p. 4, with proof p. 11 states tensor-product additivity. That statement alone is not the marginal superadditivity required here. |

The following reduction was reconstructed for this audit. Set

\[
|\psi_p\rangle=\sum_u\sqrt{p_u}|u\rangle,
\qquad \tau_i=\operatorname{Tr}_{-i}|\psi_p\rangle\langle\psi_p|.
\]

Then \(C_f(\psi_p)=H(p)\) and \(2|(\tau_i)_{01}|=C_i(p)\).
Iterating the first source's superadditivity and using the second source's
qubit formula gives exactly

\[
H(p)\ge\sum_i f(C_i(p)). \tag{1}
\]

This is the coordinatewise inequality, including correlated and nonuniform
distributions. It strengthens the provenance already supplied by the
Samorodnitsky comparison; it supplies no new unrestricted sharp coefficient.

## 3. Exact entropy-production derivation of the quantum penalty

Roga–Fannes–Życzkowski, *Universal bounds for the Holevo quantity, coherent
information and the Jensen–Shannon divergence*,
[1004.4782v1](https://arxiv.org/pdf/1004.4782v1), 27 April 2010, Corollary 4,
Lemma 5 and Eq. (26), p. 4, prove

\[
S((\rho+\sigma)/2)-\tfrac12S(\rho)-\tfrac12S(\sigma)
\le h_2((1-F(\rho,\sigma))/2). \tag{2}
\]

Here \(F\) denotes **root** fidelity. Their notation \(\sqrt F\) is our
\(F\), and their natural logarithms have been converted to bits.
Hirche–Reeb [1706.09752v2](https://arxiv.org/pdf/1706.09752v2), Theorem V.3,
Eq. (52), p. 8, and its proof p. 9 reproduce this ingredient and cite that
earlier source.

Here is the audit's application. Let
\(\Delta_i\rho=(\rho+X_i\rho X_i)/2\),
\(\Delta=\Delta_n\cdots\Delta_1\), and let \(p\) be the diagonal of
\(\rho\) in the product X basis. Pinching gives
\(S(\Delta_i\rho)-S(\rho)=D(\rho\Vert\Delta_i\rho)\).
The channels commute. Relative-entropy data processing followed by
telescoping therefore gives

\[
H(p)-S(\rho)
\le\sum_i D(\rho\Vert\Delta_i\rho)
\le\sum_i h_2((1-F_{X_i})/2), \tag{3}
\]

where \(F_P=F(\rho,P\rho P)\); the last step is (2).
Fidelity data processing under \(\Delta\), which commutes with conjugation
by \(Z_i\), gives

\[
F_{Z_i}\le F(\Delta\rho,Z_i\Delta\rho Z_i)=C_i(p).
\]

Combining this with (1), (3), and monotonicity of \(f\) recovers

\[
S(\rho)\ge\sum_i\left[f(F_{Z_i})-h_2((1-F_{X_i})/2)\right]. \tag{4}
\]

Thus both nontrivial entropy ingredients have precise prior sources. The
combination, its application to arbitrary refined seeds, and the conversion
to the project's fixed-cap operational converse are deductions to assess
separately. No source inspected here was found to state that complete
operational consequence; this is a scoped finding, not a literature-absence
claim. The generalized random-access-code derivation already credited to
Wehner–Christandl–Doherty remains an equally valid route.

## 4. The one-qubit convex envelope is an existing assemblage resource

Cope, *Entanglement cost for steering assemblages*,
[2102.02333v2](https://arxiv.org/pdf/2102.02333v2), Eq. (10), p. 3, defines
steering entanglement of formation \(E_{FA}\); Theorem 2 on that page
identifies it with minimum state entanglement of formation over compatible
realizations. Its tensor-copy definition, Eqs. (28)–(31), pp. 8–9, requires
complete setting and outcome tuples. Eqs. (25)–(27), pp. 5–6, optimize
equal-entropy decompositions with one exact measurement; their orthogonal
special case supplies the atom \((1,v)\) at cost \(f(v)\). They are not an
explicit evaluation of the entire two-contrast family below.

Define \(C_{\rm seed}(x,z)\) as the infimum of
\(\sum_a p_aS(\rho_a)\) over finite ensembles of normalized one-qubit seed
Gram matrices, with average root-fidelity profiles at least \((x,z)\).
It is the lower convex monotone envelope of all one-qubit seed entropy
profiles. For the assemblage

\[
\sigma_{s|X}=\frac{I+sxX}{4},\qquad
\sigma_{s|Z}=\frac{I+szZ}{4},\qquad s\in\{-1,+1\},
\]

the audit establishes the exact identification

\[
\boxed{C_{\rm seed}(x,z)=E_{FA}(\sigma^{x,z}).} \tag{5}
\]

This equation is an independently supplied reduction, not a quoted formula
from Cope's paper. The proof also fixes the relevant transpose convention.

For a decomposition \(\sigma=\sum_a p_a\tau^a\), write
\(\rho_a=\sum_s\tau^a_{s|j}\), independently of \(j\). Define

\[
K_a=\sqrt{2p_a}\sqrt{\rho_a^T},\qquad
N^a_{s|j}=\left(\rho_a^{-1/2}\tau^a_{s|j}\rho_a^{-1/2}\right)^T.
\]

Inverses act on the support; extend each POVM arbitrarily on its orthogonal
complement. Since \(\sum_a p_a\rho_a=I/2\), the Kraus maps satisfy
\(\sum_a K_a^\dagger K_a=I\), and

\[
\sum_a K_a^\dagger N^a_{s|j}K_a=2\sigma_{s|j}^T=M_{s|j}.
\]

Conversely any refined qubit-input instrument gives

\[
p_a=\operatorname{Tr}(K_a^\dagger K_a)/2,\qquad
\tau^a_{s|j}=\frac{(K_a^\dagger N^a_{s|j}K_a)^T}
{\operatorname{Tr}(K_a^\dagger K_a)}.
\]

Zero-weight branches can be discarded. Their marginals are normalized
Gram matrices, transposed, and have the same entropy. Restricting the
assemblage infimum to extremal decompositions does not alter this argument:
refinement can only lower the average marginal entropy, by concavity.

Let \(L_a=K_a/\sqrt{\operatorname{Tr}K_a^\dagger K_a}\).
Trace-norm duality bounds each branch's X/Z correlation by its
\(F_X,F_Z\). Therefore any exact target instrument has average seed profile
at least \((x,z)\), so its average entropy is at least
\(C_{\rm seed}(x,z)\). In the reverse direction, apply the complete Pauli
orbit to every seed, choosing its separate trace-norm-optimal decoders.
The orbit has exact unbiased Pauli contrasts \((F_X,F_Z)\), unchanged
entropy, and total Kraus effect \(I\). Convex mixing and independent output
flips attain any dominated profile. This proves (5).

The [profile theorem](PRODUCT_DIAGONAL_PROFILE_RATE.md) proves that the
one-qubit envelope is generated by the free disk \(x^2+z^2\le1\), at cost
zero, and the exact-axis curves \((1,v),(v,1)\), at cost \(f(v)\).
It therefore explicitly evaluates the existing \(E_{FA}\) on this family.
Its weighted support formula

\[
\max\left\{\sqrt{a^2+b^2},\ a+\sup_{0\le v\le1}[bv-tf(v)]\right\},
\qquad a\ge b\ge0,\ t\ge0,
\]

has that established resource interpretation. Its elementary optimization
proof and the extension to correlated product-diagonal Gram matrices are
separate supplied deductions. Equation (5) alone does not prove either,
nor does it extend the comparison class to arbitrary many-qubit Gram matrices.

The fixed-cap construction additionally uses the profile theorem's own
virtual-seed compression and complete-orbit proof. An average entanglement
cost in (5) is not, by definition alone, a worst-case quantum-memory rate.

## 5. Cope–Uola's dimension measure is different

Cope–Uola, *Quantifying the high-dimensionality of quantum devices*,
[2207.05722v4](https://arxiv.org/pdf/2207.05722v4), 21 June 2023, Eq. (8),
p. 5, charges worst-input **branch-averaged log rank**. Its qubit SDP is
Eq. (13), pp. 7–8; Eq. (14), p. 8, is the related incompatibility-weight
SDP. Its entropic convex roof is instead the assemblage quantity in
Eq. (20), p. 11. These statements must not be combined into an attributed
measurement-entropy theorem that the source does not state.

An explicit distinction follows on the exact-X slice. Symmetry averaging
the qubit SDP makes the free part scalar and yields
\(D_M(1,v)=v\). Indeed an exact X effect forces the free parent components
into X eigenspaces, whose Z contrast is zero; the remaining component must
carry at least weight \(v\), and mixing exact X/classical Z with full memory
attains that value. The entropy envelope instead has
\(C_{\rm seed}(1,v)=f(v)<v\) for \(0<v<1\).
This is an audit-derived separation, not a quotation of an evaluated curve.

## 6. Conditional Mrs. Gerber and BB84 comparisons

| Primary theorem inspected | Exact assumptions and obstacle to a direct subsumption |
|---|---|
| Hirche–Reeb, [1706.09752v2](https://arxiv.org/pdf/1706.09752v2), 24 August 2017; Theorem VI.1, Eqs. (53)–(54), pp. 9–10; Theorem VI.3, Eqs. (64)–(66), p. 12 | Bounds XOR entropy of independent binary cq states with uniform priors; the latter further assumes identical states. The seed's column ensemble has correlated, possibly nonuniform coordinates and one shared quantum register. Assigning that register independently to both channels changes the state. The sharper formula is labeled Conjecture VII.1, Eq. (72), p. 15. |
| Hirche–Guan–Tomamichel, *Chain Rules for Rényi Information Combining*, [2305.02589v1](https://arxiv.org/pdf/2305.02589v1), 4 May 2023; Section V, Eqs. (V.3)–(V.6), p. 5; Propositions V.3–V.4, Eqs. (V.13)–(V.14), p. 7 | Exact combining identities concern order-2 sandwiched conditional entropy and its dual order-1/2 quantity for product binary-input cq channels. Neither is the von Neumann entropy of an arbitrary correlated seed. General-order extensions are Conjectures V.5–V.6 on p. 7, so cannot be imported as theorems at order one. |
| Masini–Pironio–Woodhead, *Simple and practical DIQKD security analysis via BB84-type uncertainty relations and Pauli correlation constraints*, [2107.08894v3](https://arxiv.org/pdf/2107.08894v3), 18 October 2022; entropy bounds (10)–(17), pp. 4–5 | Bounds entropy of an Alice measurement conditioned on an external adversary, using Pauli correlations and optional preprocessing. The desired resource here is the entropy of the entire seed. Separate local applications do not provide a sum charged once to that entropy; different query pairs need not admit a common decoder block decomposition. |

These are specific failures of direct reductions, not evidence that future
reductions are impossible. The inspected 2023 information-combining source
still labels the sharp general formula conjectural. This note makes no
claim that every later paper has been exhausted.

A second concrete obstacle concerns ordinary entanglement of formation.
For the pure three-qubit W state on \(A_1A_2B\), Wootters' two-qubit
concurrence formula ([quant-ph/9709029v2](https://arxiv.org/pdf/quant-ph/9709029v2),
Eq. (9), p. 4) gives

\[
S(B)=h_2(1/3)\simeq0.918296,
\qquad E_F(A_1:B)+E_F(A_2:B)=2f(2/3)\simeq1.100096.
\]

Thus a proposed proof cannot simply sum local formation costs and bound
them by \(S(B)\). This is an independently calculated counterexample to
that proof step, not to the global seed conjecture. Coherence
superadditivity applies to the constructed amplitude state in Section 2
and charges \(H(p)\); it does not supply this false entanglement inequality.

## 7. Narrow novelty boundary

The asymmetric bound combines established entropy ingredients. The explicit
one-qubit envelope evaluates a pre-existing assemblage resource.
Its restricted correlated-product-diagonal tensorization, exact support
formula, and fixed-cap operational achievability should be assessed as
separate deductions with those restrictions stated. Their presence in this
repository is not by itself evidence of originality.

The sharp unrestricted target remains a different claim:

\[
\sum_i(F_{X_i}+F_{Z_i})
\le\sqrt2\,n+(2-\sqrt2)S(\rho).
\]

None of the precise reductions supplied here proves it. Equation (4) gives
the weaker coefficient \(1/\log_2(1+\sqrt2)\), approximately 0.78644,
instead of \(2-\sqrt2\), approximately 0.58579. Claims about the full
common-accuracy rate must continue to distinguish this unresolved
unrestricted inequality from a proved formula in a Gram-matrix comparison
class.
