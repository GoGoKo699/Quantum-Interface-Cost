# Audit of a proposed SLD entropy converse

Date: 2026-09-22. Latest research base:
`358d887058eb9fa2fe8bb899d0261ec811d42fa6`.
The original audit used base
`6ddc97a549316ed9edb7a14a110ceee70b87bdf9`.
Status: targeted primary-source comparison, supplied exact reductions and
explicit obstructions to proposed proof routes. The global inequality below
remains unproved; neither the counterexamples nor the inspected prior results
settle it. Publication novelty remains unresolved.

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

In fact no finite universal coefficient repairs the single-pinching claim.
For the pure state `sqrt(1-epsilon)|0>+sqrt(epsilon)|1>` and P=Z, the
entropy increase is `h_2(epsilon)` whereas the SLD term is
`4epsilon(1-epsilon)`. Their ratio diverges as
`(1/4)log_2(1/epsilon)` when epsilon tends to zero. Thus
`S(E_P(rho))-S(rho)<=C I_rho(P)` fails for every fixed finite C.
The same family's global X/Z information sum is one, so this stronger
local obstruction still does not refute (2).

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

### Further entropy comparisons

Two further primary comparisons clarify possible entropy transfers.
Liu, [2303.01952v5](https://arxiv.org/pdf/2303.01952v5), 31 August 2025,
Definition 3.1, printed p. 13, and Theorem 3.4 with footnote 22, printed
p. 14, distinguish quantum triangular
discrimination with a geometric eigenvalue kernel from its measured
variant with the SLD harmonic kernel. The theorem upper-bounds quantum
Jensen–Shannon divergence by the former. Replacing it by the measured
variant is not a stated conclusion. The pure pinching family above already
rules out the needed universal linear entropy/SLD transfer.

Cheng–Hsieh, [1506.06801v2](https://arxiv.org/pdf/1506.06801v2),
2 May 2019, Corollary 8, printed p. 10, gives a matrix-valued
logarithmic-Sobolev inequality with a `ln(d)` defect. With normalized
trace, substitute the classical Pauli-orbit function
`f(a,b)=sqrt(d) X^a Z^b sqrt(rho) Z^b X^a`. Its average square is I,
and `Ent(f^2)=ln(d)-S_nats(rho)`. The defect is exactly ln(d), so the
conclusion becomes `-S_nats(rho)<=2 E(f)`, which is vacuous. Dropping
the dimension defect would change the cited theorem. This is a mathematical
orbit substitution, not a many-copy physical encoding assumption.

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

A more recent comparison is Chang–Li,
[2601.01900v2](https://arxiv.org/pdf/2601.01900v2), 17 February 2026,
Corollary 4.1 / Eq. (36), printed pp. 23–24. Its proof and Theorem 3.1's
constants at p=2 give the Boolean-case coefficient 1/2. Substituting
`A=2P-I` and `t=r/2^n`, for `0<t<1` its consequence in this note's
normalization is

$$
\frac12\sum_{i,U=X,Y,Z}I_{P/r}(U_i)
\ge(1-t)\left[1+\frac12\ln\frac1{4t(1-t)}\right].
$$

This does not reach the requested `log_2(1/t)` coefficient; as t tends
to zero, its leading logarithmic coefficient is 1/2 rather than `1/ln(2)`.
The inspected Talagrand consequence therefore does not establish (10).
No literature-wide nonexistence claim follows from these comparisons.
At t=1 the right-hand side is extended by zero; the source's Remark 4.2
separately treats zero variance.

## 5. Exact commutator integral and an unrestricted workload comparison

The flat-state comparison (9) extends to every density matrix. The argument
below is a supplied deduction; it does not establish the entropy target (2).
All Hilbert--Schmidt norms in this section use the unnormalized trace.

For `a,b>=0` with `a+b>0`, direct integration gives

$$
\int_0^\infty(ae^{-ta}-be^{-tb})^2\,dt
=\frac{a+b}{2}-\frac{2ab}{a+b}
=\frac{(a-b)^2}{2(a+b)}.
\tag{11}
$$

The integrand is zero when both a and b vanish. Define the positive
Hermitian operator `f_t=rho exp(-t rho)`. Evaluating its commutator in an
eigenbasis of rho and using (11) term by term proves

$$
\boxed{I_\rho(P)=\int_0^\infty\|[f_t,P]\|_2^2\,dt.}
\tag{12}
$$

This includes singular rho without a full-rank approximation. Only finitely
many nonnegative spectral terms occur.

For any Hermitian f, write `f=sum_w f_w sigma_w` in the n-qubit Pauli basis,
where `f_w=Tr(sigma_w f)/d` and `d=2^n`. Pauli orthogonality gives

$$
\|[f,X_i]\|_2^2+\|[f,Z_i]\|_2^2-\|[f,Y_i]\|_2^2
=8d\sum_{w:w_i=Y}|f_w|^2\ge0.
\tag{13}
$$

Apply (13) inside (12), then sum over the sites. With `N_Y(w)` denoting
the number of Y factors,

$$
\boxed{
\mathcal I_{XZ}(\rho)-\frac12\sum_{i,U=X,Y,Z}I_\rho(U_i)
=4d\int_0^\infty\sum_wN_Y(w)|f_w(t)|^2\,dt\ge0.
}
\tag{14}
$$

In particular, `I_rho(X_i)+I_rho(Z_i)>=I_rho(Y_i)` holds sitewise for
arbitrary spectra and eigenvectors. For rho=P/r,
`f_t=r^(-1)exp(-t/r)P`, so (14) reduces exactly to (9).
Consequently the three-Pauli inequality
`(1/2)sum_{i,U=X,Y,Z}I_rho(U_i)>=n-S(rho)` would suffice for (2) on all
states. This is a rigorous reduction to a stronger proposed inequality,
not a proof of that inequality or a substitution of the operational queries.

## 6. Exact spectral-graph formulation and its limits

Fix a full orthonormal eigenbasis `|a>` of rho, including its kernel, and
put

$$
W_{ab}=\sum_{i=1}^n\sum_{U=X,Z}|\langle a|U_i|b\rangle|^2.
\tag{15}
$$

Then W is symmetric and entrywise nonnegative, every row sums to 2n, and
(2) is exactly the rational logarithmic-Sobolev inequality

$$
\frac12\sum_{a,b:\lambda_a+\lambda_b>0}
W_{ab}\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}
\ \stackrel{?}{\ge}\ \log_2d-H(\lambda).
\tag{16}
$$

This must hold uniformly over the graphs induced by the conjugated local
Paulis. It is not enough to establish it for one product eigenbasis.
Two further necessary graph constraints are

$$
W_{aa}\le n,\qquad
L:=2nI_d-W\succeq2\left(I_d-\frac Jd\right),
\tag{17}
$$

where `I_d` is the d-dimensional identity matrix and J is the
all-ones matrix. The diagonal bound follows from the Bloch-vector bound
`<X_i>^2+<Z_i>^2<=1` on each pure eigenvector. To check the second bound,
for any real vector x let `A=sum_a x_a|a><a|`. Then

$$
x^TLx=\frac12\sum_{i,U=X,Z}\|[A,U_i]\|_2^2
\ge2\left(\operatorname{Tr}A^2-
\frac{(\operatorname{Tr}A)^2}{d}\right).
\tag{18}
$$

The last step follows by expanding A in Pauli words: each nonidentity
word contributes at least two times its squared Hilbert--Schmidt norm.

These generic constraints do not imply (16). For an exact counterexample
to that relaxation, take n=3, d=8, partition the vertices into four pairs,
and set

$$
W_{aa}=3,\qquad W_{a,\operatorname{partner}(a)}=\frac32,
\qquad W_{ab}=\frac14\quad\text{for the other six vertices }b.
\tag{19}
$$

This symmetric nonnegative matrix has row sum 6 and diagonal 3. If K is
the permutation matrix exchanging the members of each pair, then
`W=J/4+11I_d/4+5K/4`. Its Laplacian `6I_d-W` has eigenvalues
0 once, 2 three times, and 9/2 four times, so (17) holds exactly.
Let lambda be uniform on one pair and zero elsewhere. Each supported
vertex has total weight 3/2 to the other pairs; hence

$$
\frac12\sum_{a,b}\!'
W_{ab}\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}
=\frac32<2=3-H(\lambda).
\tag{20}
$$

The prime omits zero-denominator terms. This is a counterexample to using
only symmetry, nonnegativity, row sums, the diagonal bound and the
spectral-gap bound to prove (16). It is not a quantum-state counterexample.
Indeed, equality `W_aa=n` for every a would force all the eigenvectors to
be products of pure states in the X/Z plane. Between two such orthogonal
products, local-query matrix elements vanish unless the products are
orthogonal at exactly one site. In that case, the squared X/Z transition
sum is 1 at that site, multiplied by squared overlaps at the other sites,
so `W_ab<=1`. The entries 3/2 in (19) are therefore impossible. A successful
graph proof must retain further structure of the induced graphs.

## 7. Research conclusion

The proved trace-norm/SLD estimate remains useful, but the proposed
unrestricted entropy bound requires a new argument or a different
applicable prior theorem. Both local shortcuts above are false. The
source comparisons identify distinct metrics, operator averages and
influence norms that cannot be interchanged without proof. The exact
commutator integral now supplies an unrestricted comparison with the
three-Pauli workload; the induced spectral-graph formulation identifies
additional structure that a sharp proof must use. Neither deduction closes
the entropy inequality or improves the established memory-rate bounds.

All of this analysis concerns virtual normalized seeds of the existing
model. It preserves one arbitrary unknown specimen, one delayed query,
unrestricted collective encoding, unlimited finite classical records,
worst-case quantum dimension and uniform arbitrary-input error. It
introduces no many-copy estimation, average-memory, joint-decoder or
postselection assumption.
