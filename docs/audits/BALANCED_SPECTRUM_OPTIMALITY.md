# Exact optimality for balanced two-level spectra at every input size

Research base: `18550b3b9ab5617a788b3b5d43d575dbf6e5a39e` (PR #55).
Status: supplied analytical proof, independently reconstructed internally.
No publication-originality claim is made.

This note evaluates the original query score at every spectrum consisting
of two equally repeated eigenvalues, for every number of input qubits.
The flat endpoint proves the half-rank retention value for **all flat
half-rank seeds**. Arbitrary nonflat half-rank seeds are outside this
theorem; the unrestricted general retention and entropy conjectures
remain open.

## 1. Exact score and equality

Let d=2^n, n>=1, and let R be a traceless Hermitian unitary on the input
space. For 0<=t<=1, define rho_t=(I+tR)/d. These are exactly the states
with eigenvalues (1+t)/d and (1-t)/d, each repeated d/2 times. For the
original queries U in {X_i,Z_i}, put

$$
g(\rho)=\sum_U\|\sqrt\rho U\sqrt\rho\|_1,\qquad
\mathcal A(\rho)=\sum_U
\sqrt{\operatorname{Tr}(\sqrt\rho U\sqrt\rho U)}.
$$

**Theorem.** Over all complex eigenbases at this fixed spectrum,

$$
\boxed{\max_R g(\rho_t)=2n-2+2\sqrt{1-t^2/2}.}
\tag{1}
$$

At t>0, equality holds precisely when R is an original-site bisector
reflection, tensored with the identity on all other sites:
R=(s_X X_i+s_Z Z_i)/sqrt(2), where s_X,s_Z belong to {+1,-1}.
At t=0 all choices give the same maximally mixed state.

The affinity profile at the same fixed spectrum is also exact:

$$
\boxed{\max_R\mathcal A(\rho_t)
=2n-2+\sqrt{2+2\sqrt{1-t^2}}.}
\tag{2}
$$

Its equality family is the same for t>0. In particular, every rank-d/2
orthogonal projector P satisfies

$$
\boxed{g(P/(d/2))\le2n-2+\sqrt2,}
\tag{3}
$$

with equality exactly at a pure original-site bisector times the
maximally mixed state of the remaining n-1 sites. This extends the
earlier [flat half-rank theorem](../FLAT_HALF_RANK_OPTIMALITY.md) beyond
its finite input sizes; it does not remove the flat-spectrum assumption.

Every state in (1) also satisfies the sharp seed entropy inequality

$$
g(\rho_t)\le\sqrt2\,n+(2-\sqrt2)S(\rho_t).
\tag{4}
$$

It is strict for 0<t<1. At t=1 equality has the bisector family in (3),
and at t=0 it is the maximally mixed state.

## 2. A reflection response inequality

Write tau=Tr/d and set

$$
C_U=\frac14[R,U]^*[R,U],\qquad
q_U=\tau(C_U)\in[0,1],\qquad
\mathcal R_z(R)=\sum_U\sqrt{1-zq_U}.
$$

The main geometric statement is

$$
\boxed{\mathcal R_z(R)\le2n-2+2\sqrt{1-z/2},
\qquad 0\le z\le1.}
\tag{5}
$$

For z>0 its equality cases are precisely the bisector reflections from
Section 1. To prove it, expand R in the orthonormal Pauli-word basis.
Its real coefficients have squared sum one and no identity coefficient.
Let W=sum_i(r_{X_i}^2+r_{Z_i}^2) be the total singleton X/Z mass. Each
X or Z letter contributes one to sum_U q_U, and each Y letter contributes
two. All remaining nonidentity words have contribution at least two.
Consequently

$$
E_R:=\sum_U q_U\ge2-W.
\tag{6}
$$

If W>0, put b=max_i(r_{X_i}^2+r_{Z_i}^2), A=b/W, and
a_i=sqrt(r_{X_i}^2+r_{Z_i}^2)/sqrt(W). Then sum_i a_i^2=1 and
max_i a_i^2=A. For independent Rademacher signs epsilon_i, let
m=E|sum_i a_i epsilon_i|. The singleton part H of R has commuting
terms on distinct sites, so

$$
W=\tau(RH)\le\tau|H|=\sqrt W\,m,
\qquad W\le m^2.
\tag{7}
$$

The following elementary estimates are proved in Section 3. Put
r=sqrt(2)-1 and c=2-sqrt(2)=1-r. Then

$$
A\le3/4\ \Longrightarrow\ m<9/10,
\qquad
A\ge3/4\ \Longrightarrow\ m^2(1-rA)\le c.
\tag{8}
$$

The second inequality is strict when A<1.

Let f_z(x)=1-sqrt(1-zx). It is increasing and convex, and
f_z(x)>=zx/2. If W=0 or A<=3/4, (6)--(8) give W<2r; indeed
81/100<2r follows, for example, from sqrt(2)>141/100. Therefore,
for z>0,

$$
\sum_U f_z(q_U)\ge\frac z2(2-W)>cz
\ge2f_z(1/2).
\tag{9}
$$

The last inequality follows from convexity in z and the endpoint
2f_1(1/2)=c. This proves (5), strictly, in this case.

For A>=3/4, choose a site attaining b, with singleton coefficients
u,v, so u^2+v^2=b. Its two query energies satisfy q_X>=v^2 and
q_Z>=u^2. The function f_z(x)-zx/2 is increasing. Applying it to these
two queries, using the linear tangent for all others, and then convexity
at the selected site gives

$$
\sum_U f_z(q_U)
\ge\frac z2(E_R-b)+f_z(u^2)+f_z(v^2)
\ge\frac z2(2-W-b)+2f_z(b/2).
\tag{10}
$$

Subtract 2f_z(1/2) and divide by z>0. The resulting lower bound
H(z) is nonincreasing in z: for h_z(x)=f_z(x)/z,

$$
\partial_z h_z(x)
=\frac{x^2}{2\sqrt{1-zx}(1+\sqrt{1-zx})^2}
$$

is increasing in x on [0,1/2], and b<=1. It suffices to evaluate H(1).
The tangent inequality 2sqrt(1-b/2)<=(3-b)/sqrt(2) gives

$$
H(1)\ge\frac{c-W+rb}{2}\ge0,
\tag{11}
$$

because W-rb=W(1-rA)<=m^2(1-rA)<=c. This proves (5).
If A<1, (8) makes (11) strict. If A=1 but W<1, then
W(1-rA)=cW<c. Thus equality requires A=W=b=1. The entire Pauli
expansion then lies on that site's X/Z plane. Strict convexity in
(10), at z>0, further requires u^2=v^2=1/2. These conditions also
suffice, proving the equality statement.

## 3. The elementary Rademacher estimates

Here sum_i a_i^2=1, A=max_i a_i^2, and m=E|sum_i a_i epsilon_i|.
This section supplies a self-contained proof of (8).

First suppose A<=1/2. Define s=11/4 and p=3/2. The even polynomial

$$
P(x)=\frac{x^6-(85/8)x^4+(13465/256)x^2+1305/64}{3993/64}
$$

majorizes |x|. For x>=0, the exact factorization is

$$
P(x)-x=
\frac{(x-3/4)^2(x-2)^2(x^2+2sx+s^2+p)}{2s^3p}\ge0,
\qquad 2s^3p=3993/64.
\tag{12}
$$

Evenness handles x<0. For X=sum_i a_i epsilon_i, put
K=sum_i a_i^4 and L=sum_i a_i^6. The exact moments are
E X^2=1, E X^4=3-2K and E X^6=15-30K+16L. Since L<=AK,

$$
m\le\mathbb E P(X)
\le\frac{14365}{15972}
+\frac{(16A-35/4)K}{3993/64}
\le\frac{14365}{15972}<\frac9{10}.
\tag{13}
$$

For the remaining intervals choose a_1=sqrt(A) and
Y=sum_{i>1}a_i epsilon_i. Averaging the first sign gives
m=E max(sqrt(A),|Y|). The pointwise bounds

$$
(x-a)_+\le\frac{x^2}{4a},\qquad
(x-a)_+\le\frac{27x^4}{256a^3}
\quad(x\ge0,\ a>0)
$$

and E Y^2=1-A, E Y^4<=3(1-A)^2 imply

$$
m\le\frac{1+3A}{4\sqrt A},\qquad
m\le H_4(A):=\sqrt A+
\frac{81(1-A)^2}{256A^{3/2}}.
\tag{14}
$$

On [1/2,9/16], the first bound is increasing and is at most
43/48<9/10. On [9/16,3/4], the sign of H_4'(A) is the sign of
337A^2+162A-243. This polynomial increases on the interval, so H_4
has no interior maximum. Its endpoint values are 915/1024 and
265sqrt(3)/512, both less than 9/10. This proves the first part of (8).

For A>=3/4, put x=1-A and k=81/256<1/3. Equation (14) gives
m<=sqrt(A)(1+kx^2/A^2). At A=1 the desired bound is equality.
For x>0, the available slack is

$$
c-A(1-rA)=r^2x+rx^2.
$$

The correction from the squared bracket, divided by x, is bounded by

$$
(1-rA)\left(\frac{2kx}{A}+\frac{k^2x^3}{A^3}\right)
<\frac7{10}\left(\frac29+\frac1{243}\right)
=\frac{77}{486}<\frac4{25}<r^2.
\tag{15}
$$

Here x/A<=1/3 and 1-rA<7/10 follow from A>=3/4 and r>2/5.
The rational comparison is 1925<1944, and r>2/5 follows from
sqrt(2)>7/5. This proves the second part of (8), strictly for A<1.

## 4. Passing to the two score profiles

For rho_t, the established direct weighted-Cauchy inequality
F_U(rho)^2<=1-I_rho(U), where

$$
I_\rho(U)=\frac12\sum_{a,b}
\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}|U_{ab}|^2,
$$

is proved in [SPECTRAL_CONDITION_ENTROPY_BOUND](../SPECTRAL_CONDITION_ENTROPY_BOUND.md),
Section 2. Terms with zero denominator are zero. At the present binary
spectrum, direct substitution gives I_{rho_t}(U)=t^2q_U. Therefore
$g(\rho_t)\le\mathcal R_{t^2}(R)$, and (5) proves the upper bound in (1).
The bisector reflection gives a one-qubit state times maximally mixed
spectators, and directly attains the displayed value. Equality in the
response bound supplies necessity without any restriction on decoders.

Similarly, writing sqrt(rho_t)=alpha I+beta R gives directly

$$
\operatorname{Tr}(\sqrt{\rho_t}U\sqrt{\rho_t}U)
=1-\bigl(1-\sqrt{1-t^2}\bigr)q_U.
$$

Thus $\mathcal A(\rho_t)=\mathcal R_{1-\sqrt{1-t^2}}(R)$, proving (2)
and its equality cases. At t=1, R=2P-I runs over every rank-d/2
projector, giving (3).

## 5. Entropy consequence

The entropy is S(rho_t)=n-e(t), where e(t)=1-h_2((1+t)/2). The
attainer in (1) is product diagonal. The already proved scalar
inequality in [COMMUTING_SEED_BOUND](../COMMUTING_SEED_BOUND.md),
Section 2, equation (3), applied with lambda=(1-t)/2, gives

$$
2\bigl(1-\sqrt{1-t^2/2}\bigr)\ge c\,e(t).
\tag{16}
$$

That scalar inequality is strict for 0<t<1. Applying it to the exact
maximum in (1) proves (4), including its equality statements.

## 6. Prior context and verification

Quantitative Rademacher first-moment control has established prior
results. König--Schütt--Tomczak-Jaegermann, *Projection constants of
symmetric spaces and variants of Khintchine's inequality*, J. reine
angew. Math. 511 (1999), Theorem 2, equation (1.3), gives

$$
\left|\mathbb E\left|\sum_i a_i\epsilon_i\right|
-\sqrt{2/\pi}\,\|a\|_2\right|
\le(1-\sqrt{2/\pi})\|a\|_\infty.
$$

See the [author-uploaded text](https://www.researchgate.net/publication/238882030_Projection_constants_of_symmetric_spaces_and_variants_of_Khintchine%27s_inequality)
and [DOI record](https://doi.org/10.1515/crll.1999.511.1). The elementary
factorized polynomial in Section 3 supplies the constants needed here
without invoking that theorem; it is not a claim of a new general
Khintchine stability principle.

The individual fidelity response is also an established object. Roga,
Giampaolo and Illuminati, *Discord of response*,
[arXiv:1401.8243v2](https://arxiv.org/pdf/1401.8243v2), equation (9),
printed p. 3, optimize the root fidelity between a fixed state and a
local-unitary perturbation whose unitary spectrum is prescribed. Here
the objective instead sums 2n prescribed original X/Z responses while
varying the global state eigenbasis at a fixed balanced state spectrum.
These are different optimization variables and objectives; the source
comparison is not an exhaustive priority audit.

The Pauli expansion, Rademacher moment identities, spectral trace-norm
bound and one-qubit entropy comparison are established elementary or
previously recorded ingredients. The present supplied proof combines
them into the quantified response inequality (5), the all-n balanced
spectral profiles, and their equality classification. It does not claim
that these conclusions are absent from the literature. The proof and
its equality statements were independently reconstructed within this
workspace; this is not external peer review.

The [checker](../../tools/check_balanced_spectrum_optimality.py) verifies
the exact polynomial and rational comparisons, plus deliberately chosen
reflection and binary-spectrum examples:

```sh
python tools/check_balanced_spectrum_optimality.py --output results/balanced_spectrum_optimality.json
```

The [result record](../../results/balanced_spectrum_optimality.json)
pins the proof-note and checker hashes. Matrices have dimension at most
32. These bounded diagnostics do not replace the quantified proof;
there is no grid, numerical search, or optimizer in the argument.
