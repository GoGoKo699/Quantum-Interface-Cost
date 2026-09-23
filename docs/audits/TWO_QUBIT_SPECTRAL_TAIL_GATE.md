# Two-qubit entropy bound outside a quantified low-rank region

Date: 2026-09-23. Reviewed main:
`07f557be8d5863f27304b1060274a14bfee1cd50` (PR #20), tree
`de1570ec31021b198ffc5b53c93e9c447b550b98`.

**Status:** derived and independently reconstructed within this workspace,
including the exact rational certificate. This is a partial converse for
arbitrary complex eigenvectors. The unrestricted two-qubit entropy inequality,
all-block equal-accuracy optimality, and publication originality remain open.
Internal independent reconstruction is not external peer review.

## 1. Result and operational scope

Put \(c_0=2-\sqrt2\), use entropy in bits, and define

$$
g_2(\rho)=\sum_{i=1}^2\sum_{P=X,Z}
\|\sqrt\rho P_i\sqrt\rho\|_1.
$$

**Theorem.** For every two-qubit density matrix with ordered eigenvalues
\(a\ge b\ge c\ge d\ge0\), if \(\epsilon=c+d\ge1/29\), then

$$
\boxed{g_2(\rho)\le2\sqrt2+c_0S(\rho).}                 \tag{1}
$$

No eigenbasis restriction is imposed. Both rank-three and full-rank states
are covered. Consequently, any two-qubit counterexample to (1) must have
\(a+b>28/29\). If \(\sigma\) is its normalized top-two spectral truncation,
then \(\tfrac12\|\rho-\sigma\|_1=\epsilon<1/29\).

The result concerns virtual normalized seeds in the
[collective reduction](../COLLECTIVE_ENCODING_REDUCTION.md). It leaves intact
one arbitrary unknown specimen, one delayed local query, unrestricted
collective encoding, unlimited finite classical records, worst-case quantum
dimension, and error uniform over all states and queries. Spectral truncation
is a proof device; it is not postselection of the physical input.

The only seed inequality used as input is the already proved
[two-qubit SLD envelope](../TWO_QUBIT_SLD_SPECTRUM.md), Eqs. (3) and (22):

$$
g_2(\rho)\le2\sqrt{4-E_*(a,b,c,d)},\qquad
E_*=k(a,b)+k(a,c)+k(b,d)+k(c,d),                         \tag{2}
$$

where \(k(x,y)=(x-y)^2/(x+y)\) and \(k(0,0)=0\).
Its all-eigenbasis proof uses two-qubit spin flip and a doubly stochastic
assignment bound; it does not assume the physical seed is product-diagonal.
The present deduction proves that the spectrum-dependent first bound in (2)
implies (1) throughout the stated region. Merely replacing \(E_*\) by
\(2-S\) would lose the required conclusion.

## 2. Exact spectral parametrization

Ordering implies \(0\le\epsilon\le1/2\). In the theorem's region set

$$
t=\frac{a-b}{1-\epsilon},\qquad s=\frac{c-d}{\epsilon},
\qquad m=(1-\epsilon)t+\epsilon s.
$$

Here \(0\le t,s\le1\). The ordering \(b\ge c\) also gives

$$
(1-\epsilon)(1-t)\ge\epsilon(1+s),\qquad
t\le t_{\max}=\frac{1-2\epsilon}{1-\epsilon},\qquad
s\le\min\!\left(1,\frac{1-2\epsilon}{\epsilon}\right).    \tag{3}
$$

Define \(\delta(u)=1-h_2((1+u)/2)\),
\(H_0=1+h_2(\epsilon)\), and \(E_0=(1-2\epsilon)^2\).
The entropy chain rule and direct algebra yield

$$
S(\rho)=H_0-[(1-\epsilon)\delta(t)+\epsilon\delta(s)],    \tag{4}
$$

$$
E_*=E_0+(1-\epsilon)t^2+\epsilon s^2+
\frac{4\epsilon^2(1-\epsilon)^2(t-s)^2}{1-m^2}.          \tag{5}
$$

For clarity, the within-row terms in (2) are
\((1-\epsilon)t^2+\epsilon s^2\). The other two sum to

$$
\frac{(1-2\epsilon+m')^2}{2(1+m)}+
\frac{(1-2\epsilon-m')^2}{2(1-m)}
=E_0+\frac{[m'-(1-2\epsilon)m]^2}{1-m^2},
$$

where \(m'=(1-\epsilon)t-\epsilon s\). Since
\(m'-(1-2\epsilon)m=2\epsilon(1-\epsilon)(t-s)\), this proves
(5). There is no singular denominator: \(\epsilon>0\) and ordering
imply \(b>0\), hence \(m=a-b+c-d<1\).

## 3. Reduction to a quadratic comparison

Let

$$
\alpha(\epsilon)=c_0\sqrt{3+4\epsilon-4\epsilon^2},\quad
K(\epsilon)=4\epsilon^2(1-\epsilon)^2,\quad
r(u)=\frac{\delta(u)}{u^2},\quad r(0)=\frac1{2\ln2}.
$$

The convergent positive series

$$
\delta(u)=\frac1{\ln2}\sum_{j=1}^{\infty}
\frac{u^{2j}}{2j(2j-1)}                               \tag{6}
$$

shows that \(r\) increases on \([0,1]\) and \(r(1)=1\).
Using (3)--(5), together with \(1/(1-m^2)\ge1\), gives

$$
(E_*-E_0)-\alpha(H_0-S)
\ge A t^2+B s^2+K(t-s)^2,                              \tag{7}
$$

where \(A=(1-\epsilon)[1-\alpha r(t_{\max})]\) and
\(B=\epsilon(1-\alpha)\). Section 5 gives an exact rational certificate
that the matrix

$$
M(\epsilon)=\begin{pmatrix}A+K&-K\\-K&B+K\end{pmatrix}  \tag{8}
$$

is positive semidefinite for every \(\epsilon\in[1/29,9/25]\).

For \(\epsilon\ge9/25\), (3) implies both \(t,s\le7/9\).
Since \(3^{12}>2^{19}\), we have \(\log_2 3>19/12\), and therefore

$$
r(7/9)=\frac{81}{49}\left(\frac{11}{3}-2\log_2 3\right)
<\frac{81}{98}.
$$

Also \(\alpha\le2c_0\) and \(2c_0(81/98)<1\). Thus (4)--(5)
give \(E_*-E_0\ge\alpha(H_0-S)\) directly in this remaining interval,
without its nonnegative cross term. Combining both regions proves

$$
E_*-E_0\ge\alpha(\epsilon)(H_0-S).                     \tag{9}
$$

Concavity of \(x\mapsto2\sqrt{4-x}\) now yields

$$
2\sqrt{4-E_*}\le2\sqrt{4-E_0}-\frac{E_*-E_0}{\sqrt{4-E_0}}
\le2\sqrt{4-E_0}-c_0(H_0-S).                           \tag{10}
$$

It remains to prove the desired bound for the balanced spectrum
\(((1-\epsilon)/2,(1-\epsilon)/2,\epsilon/2,\epsilon/2)\).

## 4. Balanced spectra

Put \(x=1-2\epsilon\), so \(0\le x\le27/29\). The balanced bound is
\(2\sqrt{4-x^2}\le4-c_0\delta(x)\). It is equality at \(x=0\).
For \(x>0\), rationalization makes it equivalent to

$$
c_0r(x)[2+\sqrt{4-x^2}]\le2.                          \tag{11}
$$

The product \(q(x)=r(x)[2+\sqrt{4-x^2}]\) is increasing. Indeed (6)
gives \(r'(x)\ge x/(6\ln2)\), while \(r(x)\le1\). With
\(z=\sqrt{4-x^2}\ge\sqrt3\),

$$
q'(x)\ge x\left[\frac{2+z}{6\ln2}-\frac1z\right]\ge0,
$$

because \(z(2+z)\ge3+2\sqrt3>6>6\ln2\). The endpoint at one is
understood by continuity. It therefore suffices to check (11) at
\(x=27/29\). The following rational certificate does so with positive
margin. Equations (2), (10), and (11) prove the theorem.

## 5. Exact finite certificate and independent review

The implementation is
[tools/certify_two_qubit_tail.py](../../tools/certify_two_qubit_tail.py).
It uses Python's standard-library `Fraction` and integer square root only.
All acceptance decisions use exact arithmetic. Decimal margins are printed
after the checks and have no role in acceptance. Explicit exceptions keep
the checks active even under `python -O`.

First form the strict rational lower bound

$$
L=2\sum_{j=0}^{23}\frac1{(2j+1)3^{2j+1}}<\ln2
$$

from \(\ln2=2\operatorname{atanh}(1/3)\). For rational \(0\le u\le1\),
(6) implies

$$
r(u)\le R_N(u):=u^{2N}+\frac1L\sum_{j=1}^N
\frac{u^{2j-2}-u^{2N}}{2j(2j-1)}.                      \tag{12}
$$

Every omitted power is at most \(u^{2N}\), and the full coefficient sum
is \(\ln2\). The remaining finite sum is nonnegative, so replacing
\(\ln2\) by \(L\) preserves the upper bound. The code uses \(N=40\).

Partition \([1/29,9/25]\) into 400 equal closed rational intervals
\([\ell,h]\). For a nonnegative rational \(v\), let \(\sqrt v_-\) and
\(\sqrt v_+\) enclose its square root with denominator \(10^{25}\).
Integer square roots and exact squared comparisons construct these
outward enclosures. Put

$$
\begin{aligned}
c_+&=2-\sqrt2_-,&
\alpha_+&=c_+\sqrt{3+4h-4h^2}_+,\\
r_+&=R_{40}\!\left(\frac{1-2\ell}{1-\ell}\right),&
A_-&=(1-h)(1-\alpha_+r_+),\\
B_-&=h(1-\alpha_+),&
K_-&=4\ell^2(1-\ell)^2.
\end{aligned}                                        \tag{13}
$$

For every cell the code verifies

$$
A_-\ge0,\qquad B_-+K_-\ge0,\qquad
A_-B_-+K_-(A_-+B_-)\ge0.                              \tag{14}
$$

These are sufficient principal-minor conditions for
\(M_- = \operatorname{diag}(A_-,B_-)+K_-\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\)
to be positive semidefinite. They are lower bounds throughout the cell:
\(\alpha\) increases, \(t_{\max}\) decreases, and \(r\) increases.
The checked sign \(A_-\ge0\) permits multiplication by
\(1-\epsilon\ge1-h\). Also \(\alpha\ge c_0\sqrt3>1\): squaring
reduces the last strict inequality to \(17>12\sqrt2\), since
\(17^2>288\). Hence \(B\ge h(1-\alpha_+)\) with the stated sign.
Finally, \(K\) increases on \([0,1/2]\).

Thus \(M(\epsilon)-M_-\) is a sum of nonnegative multiples of the
two diagonal coordinate projectors and
\(\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\), all positive semidefinite.
The certificate covers every point of every cell, rather than its sampled
endpoints. Adjacent cells share endpoints and cover the closed interval.

The same script checks (11) using \(c_+,R_{40}(27/29)\) and the upper
square-root enclosure. It also checks \(3^{12}>2^{19}\) and
\(1-2c_+(81/98)>0\) for the high-tail argument. The observed diagnostic
minima, rounded for display, are

| Quantity | Positive margin |
|---|---:|
| Interval determinant | 0.00007866733984615593 |
| Interval \(A_-\) | 0.027139762266965805 |
| Interval \(B_-+K_-\) | 0.003114200077104584 |
| Balanced endpoint | 0.003513637500858673 |
| High-tail ratio | 0.03165915412695304 |

The authoring derivation, a separate agent's adversarial reconstruction,
and the integrating agent's check agree on the identities, tangent-bound
direction, rounding, series remainder, matrix order, and endpoints.
The supplied script was independently run. This is a finite exact certificate
conditional on the analytical reductions above, not an inference from
floating-point searches or a claim that passing unrelated tests proves (1).

## 6. What remains open, and provenance

The [low-rank stability theorem](../LOW_RANK_ENTROPY_STABILITY.md) already
proves an entropy-valid open neighborhood of the rank-at-most-two set at
fixed block size. It does not give a uniform numerical radius reaching
\(1/29\). Therefore that theorem and this one do **not** close the gap by
overlap. A possible two-qubit counterexample must lie outside the proved
neighborhood while satisfying \(0<\epsilon<1/29\), as well as every
other known exclusion. Small tail weight alone supplies no bound sharp
enough on the score increase for every support orientation and core spectrum.

This continuation pursued that remaining stability estimate but obtained
neither a complete bound nor an admissible violating seed. In particular,
leading-order graph calculations and bounded searches are not substituted
for a uniform finite-neighborhood proof. Even a full two-qubit theorem
would still require an additional argument for arbitrary block size before
settling unrestricted equal-accuracy optimality.

The cutoff \(1/29\) is sufficient, not asserted sharp. For example, the
balanced spectrum \((29,29,1,1)/60\) gives a numerical excess of about
\(1.10\times10^{-5}\) of the SLD bound over the desired target. This
exploratory value is not needed by the certificate; it cautions against
replacing the certified threshold by \(1/30\). Those balanced states
already satisfy the entropy bound by the separate exact spectrum theorem.

The SLD envelope and its established spin-flip, inversion, and ordered-kernel
ingredients are credited in the [parent theorem's source comparison](../TWO_QUBIT_SLD_SPECTRUM.md#6-primary-source-comparison-and-novelty-boundary).
The additional supplied deduction here is the scalar implication
\(\epsilon\ge1/29\Rightarrow\)(1), with an explicit rational certificate.
Entropy chain rules, the binary entropy series, concavity, and interval
arithmetic are standard ingredients. This partial corollary does not
establish a new general information inequality or certify publication
originality. It makes no additional claim to distinguish the separate
two-parameter steering-formation evaluation from all prior work; those
unresolved comparisons remain in the [literature ledger](../LITERATURE_COMPARISON.md).
