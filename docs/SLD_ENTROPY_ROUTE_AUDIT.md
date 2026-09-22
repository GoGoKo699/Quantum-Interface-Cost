# Audit of a proposed SLD entropy converse

Date: 2026-09-22. Research base:
`6ddc97a549316ed9edb7a14a110ceee70b87bdf9`.
Status: targeted primary-source comparison and explicit obstructions to two
proof routes. The global inequality below remains unproved; neither the
counterexamples nor the inspected prior results settle it. Publication
novelty remains unresolved.

## 1. The precise missing inequality

For any n-qubit density matrix rho, define

$$
I_\rho(P)=\frac12\sum_{a,b:\lambda_a+\lambda_b>0}
\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}|P_{ab}|^2,
\qquad
\mathcal I_{XZ}(\rho)=\sum_{i=1}^n[I_\rho(X_i)+I_\rho(Z_i)].
\tag{1}
$$

The entries are in an eigenbasis of rho. This is one quarter of the usual
symmetric-logarithmic-derivative quantum Fisher information for each
unitary generator P. Entropies in this note are in bits.

The proposed intermediate target is

$$
\boxed{\mathcal I_{XZ}(\rho)\ \stackrel{?}{\ge}\ n-S(\rho).}
\tag{2}
$$

The [spectral-condition proof](SPECTRAL_CONDITION_ENTROPY_BOUND.md),
Section 2, already proves by weighted Cauchy--Schwarz that

$$
F_P^2\le1-I_\rho(P),\qquad
F_P=\|\sqrt\rho P\sqrt\rho\|_1.
\tag{3}
$$

Thus (2), if proved, would imply

$$
\frac{g(\sqrt\rho)}{2n}
\le\sqrt{\frac{1+S(\rho)/n}{2}},
\qquad
g(\sqrt\rho)=\sum_{i,b=X,Z}F_{P_{i,b}}.
\tag{4}
$$

The seed reduction would then give
`q >= n max(0,2 eta^2-1)` and the same necessary bound on the asymptotic
rate. These are conditional deductions, not new proved memory bounds.
Even (4) would leave a gap above the subset contrast at intermediate
entropy; it would not establish the sharp linear entropy conjecture.

For pure states, (2) does hold: SLD information equals variance and
`<X_i>^2+<Z_i>^2<=1` gives `I(X_i)+I(Z_i)>=1`.
The maximally mixed state also satisfies it with equality. These checks
do not establish the mixed-state statement.

## 2. Two exact failed local arguments

### 2.1 Conditional entropy cannot be charged site by site this way

An apparently sufficient local claim is

$$
I_\rho(X_A)+I_\rho(Z_A)
\stackrel{?}{\ge}1-S(A\mid B)_\rho.
\tag{5}
$$

Consider the two-qubit pure state

$$
|\psi\rangle=\frac3{\sqrt{10}}|00\rangle
+\frac1{\sqrt{10}}|11\rangle.
$$

Its A marginal has Bloch coordinate `z=4/5` and `x=0`. Since the global
state is pure,

$$
I_\psi(X_A)+I_\psi(Z_A)
=1+\left(1-\frac{16}{25}\right)=\frac{34}{25}=1.36,
$$

whereas

$$
1-S(A\mid B)_\psi=1+h_2(1/10)=1.4689955935\ldots.
$$

This disproves (5). The same state satisfies (2): its two-site information
sum is `68/25>2=n-S(psi)`. Entanglement does not supply a counterexample
to the global candidate here.

### 2.2 Entropy increase under pinching is not bounded by one SLD term

For a Hermitian unitary P, let
`E_P(rho)=(rho+P rho P)/2`. Another possible proof would charge this
pinching's entropy increase to `I_rho(P)` with unit coefficient.

Take the single-qubit pure state

$$
|\phi\rangle=\frac3{\sqrt{10}}|0\rangle
+\frac1{\sqrt{10}}|1\rangle,\qquad P=Z.
$$

Then

$$
S(\mathcal E_Z(\phi))-S(\phi)=h_2(1/10)
=0.4689955935\ldots
>\frac9{25}=I_\phi(Z).
\tag{6}
$$

This is an exact obstruction to that entropy-telescoping argument. The
global one-qubit candidate again holds: `I_phi(X)+I_phi(Z)=1`.
The two counterexamples concern proposed intermediate inequalities;
they do not invalidate the established spectral-condition theorem.

## 3. Which prior Fisher-information statements apply?

### Convex roofs: one observable at a time

Sixia Yu, [arXiv:1302.5311v1](https://arxiv.org/pdf/1302.5311v1),
21 February 2013, Eq. (1) and Eq. (4), printed p. 1, proves

$$
I_\rho(P)=\min_{\rho=\sum_kp_k\psi_k}
\sum_kp_k\operatorname{Var}_{\psi_k}(P).
$$

This supplies the established convex-roof interpretation of (1).
Different observables can require different minimizing decompositions.
In particular, summing the minima gives a quantity at most the minimum
of the summed variances. A pure-state lower bound on that latter minimum
does not imply a lower bound on the separate minima in (2).

### Tensorization of a different metric

Yu Cao and Jianfeng Lu,
[arXiv:1904.06562v2](https://arxiv.org/pdf/1904.06562v2),
23 October 2019, Theorem 1, Eq. (4), printed p. 2, tensorize
strong-data-processing constants for quantum chi-square divergences at
a full-rank product reference state whose local channel images are also
full rank. Their unrestricted-channel case
uses the weight `kappa(x)=x^(-1/2)`; their second case requires
`kappa>=x^(-1/2)` and quantum-to-classical channels.

SLD instead corresponds to `kappa_SLD(x)=2/(1+x)`, the `kappa_min`
identified in their Section 5.1, p. 17. Except at x=1,

$$
\frac2{1+x}<x^{-1/2}.
$$

Neither hypothesis supplies an SLD tensorization theorem. Moreover,
contraction of a divergence around a product reference is not the
state-dependent entropy production inequality (2). An additional
argument is needed for either transfer; the title alone does not give it.

### Local X/Z labels with divergence Fisher information

Kaifeng Bu, Weichen Gu and Arthur Jaffe,
[arXiv:2302.07841v3](https://arxiv.org/pdf/2302.07841v3),
18 June 2023, Section IV.B, printed p. 5, define

$$
J(\rho;H)=\left.\frac{d^2}{d\theta^2}
D(\rho\Vert e^{i\theta H}\rho e^{-i\theta H})\right|_{\theta=0}
=\operatorname{Tr}\rho[H,[H,\log\rho]].
$$

Their Eq. (12) sums this quantity over the spectral projectors of local
X/Z operators. Theorem 15, Eq. (13), bounds its decrease under their
specified convolution of two states. This is divergence-based Fisher
information, not SLD; its eigenvalue kernel involves logarithms rather
than `(lambda_a-lambda_b)^2/(lambda_a+lambda_b)`. The local labels
therefore do not identify the two functionals. A convolution theorem
also does not implement our one-specimen encoder or supply a memory
converse without a separate reduction.

### Averaging all observables does not preserve this workload

Geza Toth, [arXiv:1701.07461v5](https://arxiv.org/pdf/1701.07461v5),
21 August 2018, Observation 3, Eqs. (9)--(10), printed p. 2, and
Section V, pp. 6--8, studies averages over all traceless Hermitian
directions. Those spectrum-dependent averages do not equal the sum
over our `2n` fixed local queries. Section V's Eq. (69), p. 7, describes
an approximate relation between a harmonic-mean statistic and the
exponential of entropy; it is not an exact entropy inequality usable
in (2). These results do not settle the missing local sum.

## 4. The flat-projector subproblem and its normalization

Let rho=P/r, where P is an orthogonal projection of rank r. For any
Hermitian unitary U, (1) simplifies to

$$
I_{P/r}(U)=1-\frac{\operatorname{Tr}(PUPU)}r.
\tag{7}
$$

Write `Tr_i` for the unnormalized partial trace. The local Pauli-twirl
identity gives

$$
\frac12\sum_{i=1}^n\sum_{U=X,Y,Z}I_{P/r}(U_i)
=2n-\frac1r\sum_i\operatorname{Tr}[(\operatorname{Tr}_iP)^2].
\tag{8}
$$

For clarity, let `d=2^n`, expand `P=sum_w p_w sigma_w`, and let `N_Y(w)`
count its Y factors. Pauli orthogonality then gives

$$
\mathcal I_{XZ}(P/r)
-\frac12\sum_{i,U=X,Y,Z}I_{P/r}(U_i)
=\frac{2d}{r}\sum_wN_Y(w)|p_w|^2\ge0.
\tag{9}
$$

Consequently,

$$
\frac1r\sum_i\operatorname{Tr}[(\operatorname{Tr}_iP)^2]
\stackrel{?}{\le}n+\log_2r
\tag{10}
$$

would be sufficient for (2) on flat states. Equation (10) is equivalent
to the three-Pauli energy bound from (8), not to the X/Z bound itself.
This distinction prevents a factor or workload substitution.

Rouze, Wirth and Zhang,
[arXiv:2209.07279v3](https://arxiv.org/pdf/2209.07279v3),
3 April 2024, Theorem 6.12, Eq. (6.6), printed p. 34, bounds the
maximum sitewise L1 influence of a projection, with an unspecified
universal constant. Their influence is the normalized Schatten norm of
`P-E_i(P)`. Equation (10) instead requests a sharp sum of squared
L2 influences with a rank-dependent coefficient. The preceding sharp
edge-isoperimetric formula, Eq. (6.5), p. 33, is stated for the classical
cube. Remark 6.13, p. 34, separately presents an L2 maximum-influence
variant as a conjecture. None of these inspected statements supplies
(10). This is a scoped comparison, not a claim that (10) is absent from
every prior source or equivalent to their conjecture.

## 5. Research conclusion

The proved trace-norm/SLD estimate remains useful, but the proposed
unrestricted entropy bound requires a new argument or a different
applicable prior theorem. Both local shortcuts above are false. The
source comparisons identify distinct metrics, operator averages and
influence norms that cannot be interchanged without proof.

All of this analysis concerns virtual normalized seeds of the existing
model. It preserves one arbitrary unknown specimen, one delayed query,
unrestricted collective encoding, unlimited finite classical records,
worst-case quantum dimension and uniform arbitrary-input error. It
introduces no many-copy estimation, average-memory, joint-decoder or
postselection assumption.
