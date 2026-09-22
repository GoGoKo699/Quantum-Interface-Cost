# Exact asymptotic memory rate with exact X readout

Date: 22 September 2026. Research base:
`9697d4d72cc34c52f4680fbf0c588b39af5c0471`.

**Status:** supplied deduction with a complete proof, independently
reconstructed within this workspace. The scalar cube entropy
and spectral bounds are established prior mathematics; the operational
conclusion is a corollary of those ingredients and the
[exact-axis reduction](EXACT_AXIS_SPECTRAL_REDUCTION.md). Publication novelty
of the operational specialization remains unresolved.

## 1. Statement and quantifiers

One arbitrary unknown n-qubit specimen is encoded before one delayed local
X/Z query. The encoder is unrestricted and collective, its classical record
is finite but unbounded, and every quantum branch has dimension at most D.
There are no extra specimens, postselection, or quantum bypasses. Require
all X queries to be exact and the Z-query effective observables to be z_i Z_i,
with 0 <= z_i <= 1. Define

$$
f(c)=h_2\!\left(\frac{1-\sqrt{1-c^2}}2\right),\qquad 0\le c\le1,
$$

where h_2 is binary entropy in bits.

**Finite converse.** Every admissible protocol satisfies

$$
\boxed{\log_2D\ge\sum_{i=1}^n f(z_i).}
\tag{1}
$$

In particular, with common Z contrast z and D <= 2^q,

$$
q\ge n f(z),\qquad q\ge\lceil n f(z)\rceil.
\tag{2}
$$

Let q_X(n,z) be the smallest integer q achieving exact X and common Z
contrast z. Then the limit exists and is exactly

$$
\boxed{R_X(z):=\lim_{n\to\infty}\frac{q_X(n,z)}n=f(z).}
\tag{3}
$$

These conclusions also hold if the Z requirement is formulated as a
uniform total-variation error at most epsilon_i=(1-z_i)/2, rather than
requiring the effective observable to be exactly a scalar multiple of Z_i.
The necessity proof below permits this weaker requirement; the constructions
satisfy the stronger operator identities exactly.

Exact X statistics are an assumption at every finite n in this rate
definition. The accompanying [asymmetric converse](ASYMMETRIC_ENTROPIC_CONVERSE.md)
controls nonzero X error through an explicit binary-entropy penalty; no
error-free assumption is silently applied to noisy X protocols.

## 2. Elementary entropy inequality

For a probability distribution p on the Boolean cube put

$$
F_i(p)=\sum_x\sqrt{p_xp_{x+e_i}}.
$$

The following refinement suffices:

$$
\boxed{H(p)\ge\sum_i f(F_i(p)).}
\tag{4}
$$

To prove it, first check the binary function. For 0<c<1 and
s=sqrt(1-c^2), differentiation gives

$$
f'(c)=\frac{c\operatorname{atanh}s}{s\ln2}>0,
\qquad
f''(c)=\frac{\operatorname{atanh}s-s}{s^3\ln2}>0.
\tag{5}
$$

Together with continuity and f(0)=0,f(1)=1, this shows that f is increasing
and strictly convex on [0,1]. Also, for every t in [0,1], symmetry of h_2 gives

$$
h_2(t)=f(2\sqrt{t(1-t)}).
\tag{6}
$$

Fix i and write y for the other n-1 bits. Let m_y=p_(0,y)+p_(1,y).
When m_y>0 put t_y=p_(1,y)/m_y; omit zero-mass y. Then

$$
H(X_i\mid X_{-i})
=\sum_y m_y f(2\sqrt{t_y(1-t_y)})
\ge f\!\left(\sum_y 2m_y\sqrt{t_y(1-t_y)}\right)
=f(F_i(p)).
\tag{7}
$$

Conditioning reduces Shannon entropy, so the chain rule implies

$$
\sum_i H(X_i\mid X_{-i})
\le\sum_i H(X_i\mid X_1,\ldots,X_{i-1})=H(p).
\tag{8}
$$

Combining (7) and (8) proves (4). This includes distributions with zeros;
no full-support assumption or limiting regularization is needed.

For common target z, (4) and Jensen imply

$$
H(p)\ge n f\!\left(\frac1n\sum_iF_i(p)\right).
\tag{9}
$$

The scalar inequality is sharp at every entropy: take the product of
Bernoulli distributions of parameter a=(1-sqrt(1-z^2))/2. Then
F_i=2sqrt(a(1-a))=z and H(p)=n h_2(a)=nf(z). More generally, independent
Bernoulli parameters a_i give equality in (4) for any prescribed profile
F_i=z_i. This is an exact entropy optimization, not a finite-rank attainment:
for all 0<z_i<1 the product distribution has full support.

## 3. Arbitrary instruments and the branch average

The [exact-axis reduction](EXACT_AXIS_SPECTRAL_REDUCTION.md), Section 1, proves that every refined Kraus branch K_b
satisfies [K_b^dagger K_b,X_i]=0 for every i. Thus its normalized Gram matrix
has a probability distribution p_b in the simultaneous product X basis,
with support size at most D. With d=2^n and
omega_b=Tr(K_b^dagger K_b)/d, completeness gives sum_b omega_b=1. The
trace-norm decoder bound gives

$$
z_i\le\sum_b\omega_b F_i(p_b).
\tag{10}
$$

Therefore monotonicity and convexity of f, followed by (4), give

$$
\begin{aligned}
\sum_i f(z_i)
&\le\sum_i f\!\left(\sum_b\omega_b F_i(p_b)\right)\\
&\le\sum_b\omega_b\sum_i f(F_i(p_b))\\
&\le\sum_b\omega_b H(p_b)\le\log_2D.
\end{aligned}
\tag{11}
$$

The last bound holds branch by branch from the support cap. It therefore
uses worst-case quantum dimension; it does not substitute average quantum
memory. The omega_b are outcome probabilities on the maximally mixed input,
not asserted to be the physical probabilities on arbitrary inputs.

For the uniform-error formulation, let A_i be the actual Hermitian
contraction for a Z query. The error condition is
||A_i-Z_i||_infinity <= 1-z_i. Consequently

$$
\frac1d\operatorname{Tr}(Z_iA_i)
=1+\frac1d\operatorname{Tr}(Z_i(A_i-Z_i))\ge z_i.
$$

Trace-norm duality bounds this coefficient above by the right side of (10).
The same proof of (11) applies, even if A_i has components other than Z_i.
The equivalence between the operator norm condition and uniform binary TV
error follows by maximizing the magnitude of the difference in one outcome
probability over input density matrices.

## 4. Complete finite construction and explicit bound

For 0<a<1/2 and 0<t<=1/2-a, start with the auxiliary product distribution

$$
p(x)=a^{|x|}(1-a)^{n-|x|},\quad
B=\{x:|x|\le\lfloor n(a+t)\rfloor\},\quad
\epsilon=p(B^c).
$$

The set B is nonempty. Define p'(x)=p(x)1_B(x)/(1-epsilon). This distribution
is used to define the encoder's seed; no physical success event is selected.

The support and tail estimates are

$$
|B|\le2^{n h_2(a+t)},\qquad
\epsilon\le e^{-2nt^2}.
\tag{12}
$$

For completeness, the support estimate follows by setting b=k/n with
k=floor n(a+t): for each j<=k and b<=1/2,
b^j(1-b)^(n-j)>=b^k(1-b)^(n-k)=2^(-n h_2(b)). Summing these binomial
probability terms gives |B|2^(-n h_2(b))<=1. For k=0 the estimate is direct.
Monotonicity of h_2 on [0,1/2] gives (12). The second estimate is the usual
Bernoulli Hoeffding inequality; it may instead be replaced by the elementary
Chebyshev estimate epsilon<=a(1-a)/(nt^2) without changing the rate theorem.
Flooring causes no issue: the event |x|>floor n(a+t) is exactly |x|>n(a+t)
for integer |x|.

Let v_x=sqrt(p_x) and v'_x=sqrt(p'_x). These unit vectors have overlap
sqrt(1-epsilon). For the coordinate-flip permutation T_i, which has norm one,
F_i(p)=<v,T_i v> and F_i(p')=<v',T_i v'>. The trace norm of the difference of
their pure-state projectors is 2sqrt(epsilon), so

$$
F_i(p')\ge2\sqrt{a(1-a)}-2\sqrt\epsilon
\ge2\sqrt{a(1-a)}-2e^{-nt^2}.
\tag{13}
$$

Both p and B are invariant under coordinate permutations. Thus all F_i(p')
are equal, with no additional coordinate randomization needed.

Use the complete translation instrument of the exact-axis note with seed

$$
L=\sum_{x\in B}\sqrt{p'_x}|u_x\rangle\langle x|_X,
\quad K_s=LZ^s\quad(s\in\{0,1\}^n),
$$

where the u_x are orthonormal output labels. There is no prefactor on K_s.
The entire collection obeys sum_s K_s^dagger K_s=I. The established signed
diagonal X decoders and matching-swap Z decoders implement

$$
A_{i,X}=X_i,\qquad A_{i,Z}=F_i(p')Z_i
$$

as operator identities on every input. Every branch has dimension |B|,
and the finite classical record has 2^n possibilities. If the right side
of (13) is at least z, multiply each Z decoder by z/F_i(p') to obtain
exact contrast z. Hence

$$
\boxed{
q_X(n,z)\le\lceil n h_2(a+t)\rceil
\quad\text{whenever}\quad
z\le2\sqrt{a(1-a)}-2e^{-nt^2}.
}
\tag{14}
$$

The same reasoning with Chebyshev gives the entirely variance-based
certificate z<=2sqrt(a(1-a))-2sqrt(a(1-a)/(nt^2)). Neither certificate
requires simulating the input Hilbert space or enumerating all Kraus matrices.

## 5. Exact limit and endpoints

Fix 0<z<1 and arbitrary rate tolerance delta>0. Let
alpha=(1-sqrt(1-z^2))/2. By continuity choose alpha<a<1/2 and t>0 with
a+t<1/2 and h_2(a+t)<f(z)+delta. Since c_a=2sqrt(a(1-a))>z,
(14) applies to every

$$
n\ge t^{-2}\ln\frac{2}{c_a-z}.
$$

Thus limsup q_X(n,z)/n<=f(z)+delta. Let delta decrease to zero.
The finite converse supplies liminf>=f(z), proving (3).

At z=0, measuring all X observables stores their outcomes classically and
answers Z with a fair bit, so q_X(n,0)=0. At z=1, (2) requires q>=n and
retaining the entire specimen achieves equality, so q_X(n,1)=n. These
endpoints need no continuity assertion or approximate exact-axis argument.

## 6. Consequences and comparison with the common-accuracy theorem

The [original-site-retention theorem](EXACT_AXIS_SPECTRAL_REDUCTION.md),
Section 3, uses the local weight

$$
w(x,z)=[x+z-1-\sqrt{2(1-x)(1-z)}]_+.
$$

Its exact region is sum_i w(x_i,z_i)<=q. It restricts this face to
nz<=q because w(1,z)=z. Its asymptotic memory rate is exactly z: select a
random q-element subset, measure X on discarded sites, and tune Z output
noise to contrast z when q/n>=z. Since f is strictly convex and has values
0 and 1 at the endpoints,

$$
\boxed{R_X(z)=f(z)<z=R_{X,\mathrm{retention}}(z),\qquad0<z<1.}
$$

Thus collective encoding gives a strict asymptotic memory saving for every
nontrivial Z accuracy when every X query must remain exact. This turns the
previous finite separation into an exactly evaluated asymptotic family.
It does not settle the original common-X/Z-contrast rate R(eta), since
symmetrizing X and Z changes the target and cannot transfer optimality.

The [entropy-rate characterization](ENTROPY_RATE_CHARACTERIZATION.md) uses
virtual seed truncation to convert entropy into worst-case rank. Here the
exact-axis commutation condition evaluates the entropy problem explicitly,
and diagonal truncation preserves exact X. The original all-axis entropy
conjecture is untouched. Typicality concerns only an auxiliary probability
distribution used to specify a complete encoder; the specimen remains one
arbitrary quantum state, including arbitrary entanglement among its sites.

### 6.1 A fixed interior separation

The asymptotic advantage survives fixed nonzero X error. Start with an
exact-X protocol at Z contrast z, and multiply each X decoder by x in
[0,1]. The quantum dimension is unchanged and every effective observable
becomes exactly x X_i or z Z_i. Consequently the unrestricted asymptotic
memory rate for this profile is at most f(z), whereas the exact
original-site-retention region requires rate at least w(x,z).

For every 0<z<1, write r=f(z). Since r<z, elementary algebra gives

$$
w(x,z)>r
\quad\Longleftrightarrow\quad
x>r+\sqrt{(1-z)(1+z-2r)}.
\tag{15}
$$

The threshold is strictly less than one. To check (15), set u=1-x and
c=z-r>0. The condition is c-u>sqrt(2(1-z)u). At equality the permitted
root is u=1-r-sqrt((1-z)(1+z-2r)), which lies in [0,c); the left-minus-right
side is strictly decreasing in u. This proves both the threshold and its
strictness. Thus there is a constant neighborhood of x=1 with a positive
asymptotic memory gap for each fixed interior z, without an X error that
must shrink with n.

For example, take

$$
x=\frac{99}{100},\qquad z=\frac12,
\qquad \epsilon_X=\frac1{200},\quad\epsilon_Z=\frac14.
\tag{16}
$$

Here w(x,z)=39/100 exactly, while

$$
f(1/2)=h_2\!\left(\frac{2-\sqrt3}{4}\right)
\approx0.3545789026652717<0.39.
\tag{17}
$$

The strict inequality need not rely on this decimal. Put
alpha=(2-sqrt(3))/4<7/100. The elementary bound
h_2(alpha)<=alpha log_2(e/alpha), monotonicity of the last expression for
0<alpha<1, and e<3 give

$$
f(1/2)<\frac7{100}\log_2\frac{300}{7}
<\frac7{100}\frac{11}{2}=\frac{77}{200}
<\frac{39}{100}.
$$

The middle inequality follows by squaring 300/7<sqrt(2048). Hence for all
sufficiently large n the collective construction uses strictly fewer qubits
than every protocol in the defined retention class. Its actual asymptotic
fraction is at most about 0.354579, compared with exactly 0.39 in that class.
This does not evaluate the unrestricted interior optimum: a collective
protocol with both axes noisy might do better still.

## 7. Primary-source novelty boundary

Samorodnitsky, [arXiv:0807.1679v1](https://arxiv.org/pdf/0807.1679),
10 July 2008, Theorem 1.2, Eq. (7), printed p. 5, contains the scalar
entropy inequality equivalent to (9). With v=sqrt(p), its Dirichlet quotient
is 2(n-sum_i F_i), and its normalized entropy parameter is
ln 2-H_nat(p)/n. Substitution recovers (9).

Theorem 1.4, Eq. (10), printed p. 7 (heading begins p. 6), gives the
corresponding support-cardinality bound and asymptotic Hamming-ball
tightness. Combined with the repository's exact operational graph formula,
these established results already imply the common-z rate (3). Consequently
(3) is a sharp operational corollary, not a new cube spectral or
logarithmic-Sobolev theorem. The elementary conditional-entropy proof and
explicit complete instruments make its resource and error quantifiers
transparent. Publication novelty of this operational specialization remains
unresolved.

The same curve also appears in asymptotic channel-simulation cost theory.
Wilde, [arXiv:1807.11939v3](https://arxiv.org/pdf/1807.11939v3), revision
31 October 2018 (PDF print date 2 November), Section IV.B, printed p. 10,
Eqs. (62)--(65), evaluates the entanglement cost of a dephasing channel as
$h_2(1/2+\sqrt{p(1-p)})$. With $p=(1-z)/2$ and Hadamard conjugation,
this is exactly f(z) for a channel fixing X and contracting Z by z.
Its simulation definitions, Section II.A, printed pp. 3--4, concern
arbitrary inputs under uniform diamond-norm error and a fixed Schmidt-rank
resource; the inputs need not be independent. The prior reconstruction
converse is not a lower bound for this weaker local-query task, and an
approximate channel simulator need not preserve X exactly at each finite
block. Our proof supplies those missing task-specific directions. It does
not claim a new dephasing cost formula or a new binary entropy curve.
The broader exact-axis operational novelty comparisons remain those in
[EXACT_AXIS_SPECTRAL_REDUCTION.md](EXACT_AXIS_SPECTRAL_REDUCTION.md).
