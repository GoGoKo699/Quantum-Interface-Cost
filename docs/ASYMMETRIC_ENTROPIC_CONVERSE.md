# An asymmetric entropy converse and linear onset of memory cost

Date: 22 September 2026. Research base:
`9697d4d72cc34c52f4680fbf0c588b39af5c0471`.

**Status:** supplied analytical deduction, independently reconstructed within
this workspace. The entropy, discrimination and convexity ingredients are
established mathematics. Publication novelty and possible prior subsumption
of the resulting operational bound remain under comparison.

The physical task remains one arbitrary unknown n-qubit specimen, one delayed
local X/Z query, unrestricted collective encoding, unlimited finite classical
records, and a worst-case quantum dimension cap. Separate prescribed contrasts
`x_i,z_i in [0,1]` mean the effective observables are `x_i X_i,z_i Z_i`
for every input density matrix. No pure-state promise or many-copy source is
introduced by the auxiliary ensemble used in the proof.

## 1. The profile bound

Write h for binary entropy in bits, and define

$$
f(c)=h\!\left(\frac{1-\sqrt{1-c^2}}2\right),\qquad 0\le c\le1,
\tag{1}
$$

$$
a(x,z)=f(z)-h\!\left(\frac{1-x}2\right),\qquad
\kappa(x,z)=\max\{0,a(x,z),a(z,x)\}.
\tag{2}
$$

**Theorem 1.** Every admissible interface whose quantum output dimension
is at most D on every refined branch satisfies

$$
\boxed{\log_2D\ge\sum_{i=1}^n\kappa(x_i,z_i).}
\tag{3}
$$

In particular, q retained qubits require
`q>=sum_i kappa(x_i,z_i)`. This charges a worst-case dimension, irrespective
of how much classical information is retained or how branch probabilities
depend on the physical input.

The proof first establishes `log_2D>=sum_i a(x_i,z_i)`. Arbitrary choices
of X/Z orientation and restriction to selected sites then give (3).

## 2. A classical entropy inequality

The function f is increasing and convex. To verify convexity directly,
put `s=sqrt(1-c^2)` for `0<c<1`. Differentiation gives

$$
f'(c)=\frac{c}{s\ln2}\operatorname{artanh}(s),\qquad
f''(c)=\frac{\operatorname{artanh}(s)-s}{s^3\ln2}\ge0.
\tag{4}
$$

The last inequality follows by integrating `1/(1-s^2)>=1` from zero to s.
The endpoints follow by continuity. In particular f is not being assumed
concave; its convexity is essential in both Jensen steps below.

Let p be an arbitrary probability distribution on n binary coordinates,
with zeros allowed, and let

$$
C_i(p)=\sum_{u\in\{0,1\}^n}\sqrt{p_u p_{u+e_i}}.
\tag{5}
$$

Then

$$
\boxed{H(p)\ge\sum_i f(C_i(p)).}
\tag{6}
$$

To prove this, condition bit i on all other coordinates. If a conditioning
value v has probability r_v, write its conditional probabilities as
`t_v,1-t_v`; values with r_v=0 are omitted. The corresponding conditional
entropy and overlap are

$$
H(U_i\mid U_{-i})=\sum_v r_v h(t_v),\qquad
C_i(p)=\sum_v r_v\,2\sqrt{t_v(1-t_v)}.
$$

The identity `h(t)=f(2sqrt(t(1-t)))` and convexity give
`H(U_i|U_-i)>=f(C_i(p))`. Finally the chain rule and conditioning imply

$$
H(U^n)=\sum_i H(U_i\mid U_{<i})
\ge\sum_i H(U_i\mid U_{-i}),
$$

which proves (6). No independence assumption on p has been used.

## 3. The normalized-seed inequality

Let L be any `D by 2^n` matrix with `Tr L^dagger L=1`. Set

$$
\rho=L^\dagger L,\qquad
F_i^X=\|LX_iL^\dagger\|_1,\qquad
F_i^Z=\|LZ_iL^\dagger\|_1.
$$

Each F belongs to [0,1]. We claim

$$
\boxed{S(\rho)\ge
\sum_i\left[f(F_i^Z)-h\!\left(\frac{1-F_i^X}2\right)\right].}
\tag{7}
$$

Choose the simultaneous product X eigenbasis, so
`X_i|u>_X=(-1)^{u_i}|u>_X`, and write the columns of L as
`l_u=L|u>_X=sqrt(p_u)|v_u>`, with normalized v_u when p_u>0.
The following classical-quantum state is an auxiliary mathematical object:

$$
\omega_{U^nQ}=\sum_{u:p_u>0}p_u|u\rangle\langle u|
\otimes|v_u\rangle\langle v_u|.
\tag{8}
$$

Its conditional signal states are pure because they are individual matrix
columns. This does not assert that the physical unknown input is pure.
Its Q marginal is `LL^dagger`, which has the same nonzero eigenvalues as
rho. Thus

$$
H(U^n\mid Q)_\omega=H(p)-S(\rho).
\tag{9}
$$

For bit i, the difference of its two subnormalized signal states is

$$
\sum_u(-1)^{u_i}p_u|v_u\rangle\langle v_u|=LX_iL^\dagger.
$$

Binary minimum-error discrimination consequently has error
`e_i=(1-F_i^X)/2`. This formula permits unequal bit priors. Let the optimal
binary measurement produce a guess `\widehat U_i`. Data processing and
binary Fano give

$$
H(U_i\mid Q)\le H(U_i\mid\widehat U_i)\le h(e_i).
\tag{10}
$$

For completeness, the last step follows by setting the binary error
variable `E_i=U_i+\widehat U_i mod2`: conditioned on the guess, U_i and E_i
carry the same entropy, which is at most `H(E_i)=h(e_i)`.
The quantum conditional chain rule and strong subadditivity give

$$
H(U^n\mid Q)=\sum_i H(U_i\mid U_{<i}Q)
\le\sum_i H(U_i\mid Q)
\le\sum_i h\!\left(\frac{1-F_i^X}2\right).
\tag{11}
$$

The entropy-discrimination step (9)–(11) is already contained in
Wehner–Christandl–Doherty, Lemma I.1 and Corollary I.2, cited precisely
in Section 6. We have supplied its specialization to the column ensemble.
These are separate marginal entropy bounds. The proof neither performs
all optimal decoders on the same Q nor assumes that they commute.

The other query flips one X-basis bit. Its compression is
`LZ_iL^dagger=sum_u |l_u><l_(u+e_i)|`. The triangle inequality for the
trace norm of rank-one operators gives

$$
F_i^Z\le\sum_u\|l_u\|\,\|l_{u+e_i}\|=C_i(p).
\tag{12}
$$

Combining (6), (9), (11), (12), and monotonicity of f proves (7).
This works for arbitrary spectra and eigenvectors of rho, including
singular matrices. It is a different, weaker state inequality than the
still-unresolved sharp linear seed-entropy conjecture.

## 4. Averaging arbitrary Kraus branches

Refine an arbitrary instrument into finitely many individual Kraus maps
`K_a:C^(2^n)->C^D`, storing the refinement label classically. Embed smaller
outputs into D if necessary. Completeness and uniformity imply

$$
\sum_aK_a^\dagger K_a=I,\qquad
\sum_aK_a^\dagger B_{a,i,X}K_a=x_iX_i,\qquad
\sum_aK_a^\dagger B_{a,i,Z}K_a=z_iZ_i,
$$

where every B is a Hermitian contraction. Omit zero Kraus maps and put

$$
\omega_a=\frac{\|K_a\|_F^2}{2^n},\qquad
L_a=\frac{K_a}{\|K_a\|_F},\qquad \rho_a=L_a^\dagger L_a.
$$

Then `sum_a omega_a=1` and `S(rho_a)<=log_2D` for every a.
Taking the normalized Hilbert--Schmidt pairing of each effective observable
with its Pauli and using trace-norm duality gives

$$
x_i\le\overline F_i^X:=\sum_a\omega_aF_i^X(L_a),\qquad
z_i\le\overline F_i^Z:=\sum_a\omega_aF_i^Z(L_a).
\tag{13}
$$

Convexity of f and concavity of h applied to (7) now yield

$$
\begin{aligned}
\log_2D
&\ge\sum_a\omega_aS(\rho_a)\\
&\ge\sum_i\left[f(\overline F_i^Z)
-h\!\left(\frac{1-\overline F_i^X}2\right)\right]\\
&\ge\sum_i\left[f(z_i)-h\!\left(\frac{1-x_i}2\right)\right].
\end{aligned}
\tag{14}
$$

The last inequality uses monotonicity: f increases, whereas
`h((1-u)/2)` decreases for `0<=u<=1`. The weights omega_a are actual branch
probabilities only for the maximally mixed input; no such interpretation
is assigned to arbitrary inputs. The entropy upper bound is imposed on
each branch before averaging, preserving the worst-case dimension cap.

To obtain (3), select the sites on which kappa is positive. Fix all other
physical input sites in any known pure product state. Appending these fixed
states is an isometry V; the induced Kraus maps `K_a V` still satisfy
completeness, have the same output dimension cap, and implement exactly
the same selected-site contrasts on every remaining input state. This is
a restriction of a converse test, not a promise imposed on the original
unknown specimen.

At each selected site, interchange X and Z by a local Hadamard whenever
`a(z_i,x_i)>a(x_i,z_i)`. The uniform operator identities transform
accordingly and the memory cap is unchanged. Apply (14) to the induced
interface with these chosen orientations. Its right side is precisely
the sum of the positive maxima in (3). If no site is selected, (3) is
simply `log_2D>=0`. This completes the proof.

## 5. The common-accuracy rate has linear onset

For common contrast eta define

$$
\ell(\eta)=\left[f(\eta)-h\!\left(\frac{1-\eta}2\right)\right]_+.
\tag{15}
$$

Then

$$
q_{\min}(n,\eta)\ge\lceil n\ell(\eta)\rceil,
\qquad R(\eta)\ge\ell(\eta).
\tag{16}
$$

The bracket in (15) vanishes at `eta_0=1/sqrt2`, is negative below it,
and positive above it: its first term increases and its second decreases.
At perfect contrast `ell(1)=1`.

A stronger qualitative conclusion follows near the classical threshold.
The unclipped expression is convex, differentiable near eta_0, and has
there the derivative

$$
c_0=\log_2\!\left(\frac{1+1/\sqrt2}{1-1/\sqrt2}\right)
=2\log_2(1+\sqrt2)\simeq2.5431066063.
\tag{17}
$$

Its supporting tangent gives the global bound

$$
\ell(\eta)\ge c_0(\eta-\eta_0),\qquad \eta_0\le\eta\le1.
\tag{18}
$$

Together with the existing random-subset construction this implies, for
`0<=t<=1-eta_0`,

$$
\boxed{c_0t\le R(\eta_0+t)\le(2+\sqrt2)t.}
\tag{19}
$$

More precisely `ell(eta_0+t)=c_0t+O(t^2)`. Hence the optimal memory rate
has **linear onset**, `R(eta_0+t)=Theta(t)` as t decreases to zero.
The exact leading coefficient and the intermediate common-accuracy rate
remain unresolved. The result improves the earlier lower-bound scale
`t^2 log(1/t)`; it does not prove the subset strategy optimal.

The following are scalar evaluations of supplied formulas, not simulation:

| Contrast eta | New ell(eta) | Earlier logarithmic-Sobolev b(eta) | Subset rate upper bound |
|---:|---:|---:|---:|
| 0.72 | 0.03309037 | 0.00439270 | 0.04402020 |
| 0.75 | 0.11249312 | 0.03699741 | 0.14644661 |
| 0.80 | 0.25293250 | 0.14144054 | 0.31715729 |
| 0.90 | 0.57183892 | 0.49293649 | 0.65857864 |
| 0.95 | 0.75981775 | 0.72860252 | 0.82928932 |
| 0.98 | 0.89044992 | 0.88729642 | 0.93171573 |
| 0.9999 | 0.99906921 | 0.99942299 | 0.99965858 |

Retain the maximum of all proved lower bounds. The table explicitly shows
that ell does not dominate the [logarithmic-Sobolev bound](STRONG_ENTROPIC_CONVERSE.md)
everywhere. An admissible combined lower coefficient is

$$
\max\left\{0,\ell(\eta),b(\eta),
1-2h((1-\eta)/2),\frac{(\eta-\eta_0)_+^2}{16\ln2}\right\}.
\tag{20}
$$

### An unrestricted seed-score consequence

Let `g(L)=sum_i(F_i^X+F_i^Z)`. Averaging (7) with its globally X/Z-swapped
version and applying convexity of the unclipped function
`f(u)-h((1-u)/2)` gives

$$
S(L^\dagger L)\ge n\ell\!\left(\frac{g(L)}{2n}\right).
\tag{21}
$$

Indeed the averaged right side is one half the sum of that unclipped
function at all 2n individual contrasts; Jensen gives its value at their
mean. Entropy nonnegativity permits the clipping in (21). Its supporting
tangent at the classical threshold therefore proves the global linear
inequality

$$
\boxed{g(L)\le\sqrt2 n+
\frac{S(L^\dagger L)}{\log_2(1+\sqrt2)}.}
\tag{22}
$$

The entropy coefficient is approximately `0.78643970`; it is weaker than
the conjectured sharp coefficient `2-sqrt2`, approximately `0.58578644`.
Thus (22) is a proved unrestricted linear seed-entropy bound, while the
sharper target remains open.

## 6. Provenance and limits

The binary minimum-error formula, quantum conditional-entropy chain rule,
strong subadditivity, data processing, and binary Fano bound are established
ingredients. Equations (4), (6), and (10) supply elementary proofs of the
scalar convexity, classical entropy comparison, and binary Fano steps in
the precise form used here. The normalized Kraus accounting is the existing
[seed reduction](COLLECTIVE_ENCODING_REDUCTION.md).

The following primary comparisons delimit the deduction.

| Source and exact locator | Established content and role here |
|---|---|
| Wehner–Christandl–Doherty, *A lower bound on the dimension of a quantum system given measured data*, [arXiv:0808.3960v2](https://arxiv.org/pdf/0808.3960v2), version stamp 20 November 2008, Lemma I.1 begins printed p. 2; proof and Corollary I.2, printed p. 3 | These allow correlated, nonuniform classical strings and separately chosen coordinate decoders. The lemma's proof already gives `H(Q)>=H(U^n)-sum_i H(U_i|Q)`; its corollary applies Fano. Under (8), their ensemble priors are our column norms squared, their signals are the normalized columns, `H(Q)=S(L^dagger L)`, and optimal bit errors are `(1-F_i^X)/2`. This is exactly the discrimination-entropy ingredient in (9)–(11), not a new random-access-code theorem. |
| Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, [arXiv:quant-ph/9709029v2](https://arxiv.org/pdf/quant-ph/9709029v2), version stamp 13 September 1997, Eq. (8) and following discussion, printed p. 4 | The same scalar function f is established there, together with its monotonicity and convexity. Here it is used as an elementary binary-entropy function; no identification of the general seed with two-qubit concurrence is made. |

The first source's displayed PDF header is dated 25 October 2018; its arXiv
version stamp is recorded above to remove ambiguity. Both primary statements
were read directly. The classical cube step (6) has an elementary proof above
and should also be treated as established entropy/convexity mathematics,
not a claim of a new tensorization principle.

More specifically, Samorodnitsky,
[0807.1679v1](https://arxiv.org/pdf/0807.1679v1), Theorem 1.2 / Eq. (7),
printed p. 5, gives the corresponding nonlinear scalar cube entropy bound
after averaging coordinates. The exact normalization and its sharp
support-cardinality consequence are mapped in
[EXACT_AXIS_RATE.md](EXACT_AXIS_RATE.md), Section 7. Thus both the
quantum decoding penalty and classical entropy curve have explicit prior
theorems; the contribution asserted here is their operational deduction.

The supplied operational deduction combines those ingredients with the
cube-flip trace-norm comparison (12), normalized Kraus averaging, and
uniformity under restriction of input sites. It yields (3), (19), and (22).
The auxiliary labels are columns of a mathematical seed; this is not a
many-copy estimation or source-compression assumption. An independent
reconstruction within this workspace is not external peer review. The
inspected statements identify substantial prior ingredients but do not
resolve whether the combined operational corollary already appears
elsewhere. Publication novelty remains unresolved.

The subsequent [entropy trade-off audit](ENTROPY_TRADEOFF_PRIOR_AUDIT.md)
supplies a second exact derivation of (7) from established entropy-of-mixture
and coherence-of-formation theorems. It also identifies the separately
evaluated product-diagonal profile envelope with a prior steering resource.
This strengthens the ingredient-level subsumption map; it does not improve
the unrestricted bound or certify novelty of its operational combination.
