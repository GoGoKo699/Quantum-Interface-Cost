# Exact finite-block retention and a collective advantage

**Integrated proof exposition, 27 September 2026.** Research base:
`38fd9d3f2c3e38ef5e8a7c5d6b2c041955678d8a`. This note connects the three
operational results selected in [SCIENTIFIC_SCOPE](SCIENTIFIC_SCOPE.md).
Its component proofs have been independently reconstructed internally;
its integration review is recorded in [the review note](audits/INTEGRATED_CORE_REVIEW.md).
It is not a manuscript, external peer review, or a publication-priority claim. The
[focused prior comparison](CORE_PRIOR_COMPARISON.md) and
[evidence map](CORE_EVIDENCE_MAP.md) give source and verification details.

One qubit of memory has an exact allocation rule: every feasible local
X/Z accuracy profile admits an implementation that randomly retains at
most one original qubit. For equal accuracies, random subset retention
is optimal at every integer memory budget through four inputs, including
arbitrary collective encoders and nonuniform seed spectra. At larger
budgets, collective encoding can help: a complete five-qubit-memory
instrument strictly exceeds the original-site-retention class for an
unequal-accuracy task. All three statements concern one unknown specimen
and one query chosen after encoding.

## 1. The task and the normalized-seed reduction

An encoder receives an arbitrary unknown n-qubit state, including states
entangled across the inputs. It outputs a quantum register and an
unrestricted finite classical record. Only then is one query
$U\in\mathcal U=\{X_i,Z_i:1\le i\le n\}$ revealed, and its decoder
returns a binary outcome. Write $d=2^n$ for the input dimension and
$D=2^q$ for the maximum quantum dimension on **every** branch.
There are no extra copies, source reaccess, free quantum bypass,
preshared entanglement, or postselected success. Decoders are arbitrary
binary POVMs, equivalently Hermitian contractions.

The requested effective observables are $x_iX_i,z_iZ_i$, with
$0\le x_i,z_i\le1$; their effects are $(I\pm x_iX_i)/2$ and
$(I\pm z_iZ_i)/2$. Their uniform binary total-variation errors are
$(1-x_i)/2,(1-z_i)/2$. Conversely, a protocol meeting these error
tolerances can be put in this exact form: finite Pauli twirling removes
unwanted coefficients, and classical output noise attenuates excess
contrast. The coefficient along U is at least its requested contrast
because the uniform error bounds the effective observable's operator-norm
distance from U. This preserves the arbitrary-input quantifiers.

### 1.1 From physical instruments to one density matrix

Refine the instrument into Kraus operators $K_c:\mathbb C^d\to\mathbb C^D$.
For every nonzero branch set

$$
p_c=\|K_c\|_F^2/d,\qquad L_c=K_c/\|K_c\|_F,\qquad
\rho_c=L_c^\dagger L_c,\qquad S_c=\sqrt{\rho_c}.
$$

Completeness gives $\sum_cp_c=1$. These are proof weights, equal to
branch probabilities on the maximally mixed input; physical branch
probabilities need not be input independent. Each $\rho_c$ has trace
one and rank at most D. For any such density matrix set $S=\sqrt\rho$ and define

$$
F_U(\rho)=\|SUS\|_1,\qquad g(\rho)=\sum_{U\in\mathcal U}F_U(\rho),
\qquad \Gamma(n,D)=\max_{\mathrm{rank}\rho\le D}g(\rho).
\qquad\text{(1)}
$$

The polar decomposition $L=VS$ preserves each trace norm:
$\|LUL^\dagger\|_1=\|SUS\|_1$. Here V is an isometry on the support
of $\rho$, also when its rank is smaller than D. If the effective
observable for U is $\eta_UU$, trace-norm duality gives

$$
\eta_U=\frac1d\sum_c\mathrm{Tr}(B_{c,U}K_cUK_c^\dagger)
\le\sum_cp_c F_U(\rho_c).
\qquad\text{(2)}
$$

The same inequality holds after summing with any nonnegative query weights.
Thus seed inequalities bound arbitrary instruments, without a flat-spectrum
assumption or a restriction on how their classical records are organized.

### 1.2 Every seed gives a complete protocol

Every density matrix of rank at most D admits $L=V_0\sqrt\rho$, with $V_0$
an isometry from its support into $\mathbb C^D$. Conversely take any
normalized $D\times d$ seed L, put $\rho=L^\dagger L$, and let V
range over the $m=4^n$ Pauli representatives. Set
$K_V=\sqrt{d/m}\,LV$. Pauli averaging gives $\sum_VK_V^\dagger K_V=I$.
Choose $B_U=\mathrm{sign}(LUL^\dagger)$, with zero on its kernel;
zero is a fair binary output. If $VUV^\dagger=s_{V,U}U$, decode with
$s_{V,U}B_U$. The Pauli character identity

$$
\frac1m\sum_Vs_{V,U}V^\dagger AV=\frac{\mathrm{Tr}(UA)}d\,U
$$

shows that the effective observable is exactly $F_U(\rho)U$.
All branches are accepted and have dimension at most D. Finite random
site permutations and independent local Hadamards, recorded classically,
equalize the 2n contrasts without changing their sum. Therefore

$$
\eta_{\max}(n,q)=\Gamma(n,2^q)/(2n),\qquad
\varepsilon_{\min}(n,q)=(1-\eta_{\max}(n,q))/2.
\qquad\text{(3)}
$$

The [seed-reduction note](COLLECTIVE_ENCODING_REDUCTION.md) gives the
full instrument argument. Equality classifications below concern normalized
seed Grams $\rho=L^\dagger L$, up to output isometry, not every physical
encoder implementing an optimal profile.

## 2. The exact one-qubit theorem

Define

$$
w(x,z)=\left[x+z-1-\sqrt{2(1-x)(1-z)}\right]_+,
\qquad [a]_+=\max\{a,0\}.
$$

**Theorem.** An unrestricted encoder with $D\le2$ realizes a requested
profile if and only if $\sum_iw(x_i,z_i)\le1$. In particular,

$$
\eta_{\max}(n,1)=\frac1{\sqrt2}+\frac{1-1/\sqrt2}{n}.
\qquad\text{(4)}
$$

This covers every n, with arbitrary site-dependent X and Z accuracies.

### 2.1 The weighted converse

For nonnegative $\alpha_i,\beta_i$, put
$r_i=\sqrt{\alpha_i^2+\beta_i^2}$ and
$\delta_i=\alpha_i+\beta_i-r_i$. The sharp support inequality is

$$
\sum_i(\alpha_ix_i+\beta_iz_i)\le\sum_i r_i+\max_i\delta_i.
\qquad\text{(5)}
$$

By (2), it suffices to bound a normalized dimension-two seed. Choose
extreme Hermitian contractions attaining its trace norms; on a qubit
these are scalar signs or traceless Pauli observables. Vectorizing L
gives a normalized virtual state of n reference qubits and the memory
qubit, on which the site's weighted score is

$$
f_i=\langle h_i\rangle,\qquad
h_i=\alpha_iX_i\otimes B_{i,X}+\beta_iZ_i\otimes B_{i,Z}.
$$

If either decoder is scalar, anticommutation gives $h_i^2=r_i^2I$,
so $f_i\le r_i$. Otherwise the two reference directions
$(\alpha_iX_i\pm\beta_iZ_i)/r_i$ make $2h_i/r_i$ a CHSH operator.
Cheng–Hall's monogamy inequality, allowing independently chosen memory
directions and mixed three-qubit marginals, implies
$(f_i/r_i)^2+(f_j/r_j)^2\le2$ for any two such sites.
Zero-weight sites are omitted. At most one site exceeds its r-value,
and always $f_i\le\alpha_i+\beta_i$. Summing proves (5).
The reference is a proof device; no two delayed decoders are executed together.

### 2.2 Attainment and the local weight

The compatible disk $\mathcal D=\{(x,z)\ge0:x^2+z^2\le1\}$ is
achievable with classical memory: measure
$G_{s,t}=(I+s xX+t zZ)/4$, store $(s,t)$, and answer the later query.
Retaining a site realizes the square $[0,1]^2$ there; every other site
can realize a disk point. These product instruments are valid also on
entangled inputs. Their convex hull has support function (5), obtained
by retaining a site maximizing $\delta_i$. The hull is compact and
downward closed, so its nonnegative support directions characterize it.
The converse therefore identifies the entire unrestricted feasible region.

For one pair, w is the least p with
$(x,z)\in p[0,1]^2+(1-p)\mathcal D$. Outside the disk it is the
smaller root of $(x-p)^2+(z-p)^2=(1-p)^2$, lying in $[0,\min(x,z)]$.
Necessity follows because every such decomposition obeys
$\|((x,z)-p(1,1))_+\|_2\le1-p$, which fails when $p<w$.
Inside the disk the minimum is zero. Thus any retention mixture has
$\sum_iw_i\le1$. Conversely choose site i with probability
$p_i=w(x_i,z_i)$ and retain it perfectly. Whenever it is discarded,
use the disk point $((x_i,z_i)-p_i(1,1))/(1-p_i)$; use an all-classical
branch with the remaining probability. If $p_i=1$, that site's
discarded formula is unnecessary. This proves the complete allocation
rule. It guarantees an attaining retention implementation, not that
every optimal encoder must physically retain a site. See the
[allocation proof](ONE_QUBIT_ALLOCATION_REGION.md) for its convex details.

## 3. Exact equal-accuracy retention through four inputs

**Theorem.** For integers $1\le n\le4$, $0\le q\le n$,

$$
\boxed{\Gamma(n,2^q)=2q+\sqrt2(n-q),\qquad
\eta_{\max}(n,q)=\frac{q+(n-q)/\sqrt2}{n}.}
\qquad\text{(6)}
$$

Retain q original sites and use the compatible bisector POVM on the
others; randomize the subset to attain equal contrasts. The corresponding
seed is a tensor product of pure X/Z bisectors on discarded sites and
$I/2^q$ on retained sites. At $q=0$, a rank-one seed's score is
$\sum_i(|\langle X_i\rangle|+|\langle Z_i\rangle|)\le\sqrt2n$
by the local Bloch bound. At $q=n$, each $F_U\le1$, and $I/d$
attains $2n$. Together with (4), the only additional budgets to prove
are $(n,q)=(3,2),(4,2),(4,3)$. The following two converses include
all allowed ranks and spectra. This is every **integer q** through four
inputs, not a claim about every non-power-of-two dimension D.

### 3.1 All but one input qubit

Fix $n\in\{2,3,4\}$, $k=d/2$, $\mathrm{rank}\rho\le k$,
and $S=\sqrt\rho$. Write $a_U=\mathrm{Tr}(SUSU)$.
The established squared-root-fidelity/affinity inequality
$F_U(\rho)^2\le a_U$ follows directly from Schatten Hölder:
put $A=USU$, so $\mathrm{Tr}A^2=\mathrm{Tr}S^2=1$, and

$$
F_U(\rho)=\|SA\|_1
\le\|S^{1/2}\|_4\|S^{1/2}A^{1/2}\|_2\|A^{1/2}\|_4
=\sqrt{\mathrm{Tr}(SA)}.
$$

The [sourced lemma](STRONG_ENTROPIC_CONVERSE.md#3-root-fidelity-affinity-and-the-two-pauli-energy)
therefore reduces the claim to the stronger bound
$\sum_U\sqrt{a_U}\le2n-2+\sqrt2$.
Expand S in the orthonormal Pauli basis $\sigma/\sqrt d$, and write
its singleton X/Z part as $J=\sum_i b_iB_i/\sqrt d$, where
$b_i\ge0$ and each $B_i$ is a unit X/Z-plane Pauli direction. Put

$$
u=\mathrm{Tr}S/\sqrt k,\quad v=\sqrt{1-u^2},\quad
T=\sum_i b_i^2,\quad y=2T,\quad
M=\mathbb E\left|\sum_i b_i\epsilon_i\right|.
$$

The independent signs are uniform. Rank gives $u\le1$; positivity
gives $T=\mathrm{Tr}(SJ)\le\|J_+\|_2=\sqrt{T/2}$, hence
$y\le1$. For $T>0$, put $m=M/\sqrt T$. Pauli conjugation
has eigenvalue $2n$ on the identity,
$2n-2$ on singleton X/Z words and at most $2n-4$ elsewhere, so

$$
\sum_Ua_U\le2n-4+2u^2+y,\qquad
\sqrt y\le um+v\sqrt{1-m^2}.                         \qquad\text{(7)}
$$

For the second inequality, the largest k eigenvalues of J have mean
$M/\sqrt d$ and centered squared sum $(T-M^2)/2$. Pair them with
the eigenvalues of S, padded by zeros, and apply trace rearrangement
then centered Cauchy–Schwarz. Thus (7) retains spectral nonuniformity.
The cases $T=0$ or $u\le\sqrt3/2$ are already strictly below
the target by the first inequality and Cauchy–Schwarz.

Order and pad the b's to four entries. Their exact sign mean is

$$
M=\max\left\{b_1,\frac{3b_1+b_2+b_3+b_4}{4},
                       \frac{b_1+b_2+b_3}{2}\right\}.       \qquad\text{(8)}
$$

If either latter form attains M, including a tie, $m\le\sqrt3/2$.
Equation (7) gives $2u^2+y\le(3+\sqrt7)/2$, so
$\sum_U\sqrt{a_U}\le\sqrt{2n(2n-4+(3+\sqrt7)/2)}<2n-2+\sqrt2$.
Otherwise $M=b_i$ at one site. Let $\Delta=\sum_U(1-a_U)$
and $W=(1-a_{X_i})+(1-a_{Z_i})$. The elementary case $u^2+y<1$
is strict by (7); in the remaining case its circle constraint yields

$$
\Delta\ge E:=4-2u^2-y,\qquad
W\ge w:=y[u\sqrt y-v\sqrt{1-y}]^2.
$$

Separate Cauchy bounds for that site and the other sites, followed by
concave tangents at $W=1,\Delta-W=0$, give, with $r=\sqrt2-1$,

$$
\sum_U\sqrt{a_U}-(2n-2+\sqrt2)
\le\{r(1-W)-(\Delta-1)\}/2\le0.                         \qquad\text{(9)}
$$

Indeed, writing $z=\sqrt{1-y}$,
$(E-1)-r(1-w)\ge(2-r)v^2-2rvz+(1-2r)z^2\ge0$.
The quadratic is positive definite, with determinant $10-7\sqrt2>0$.
Equality forces $u=y=m=1$, then Pauli equality gives

$$
\rho=|\beta\rangle\langle\beta|_i\otimes I_{\rm rest}/2^{n-1},
\qquad\text{(10)}
$$

where beta has zero Bloch Y component and X,Z magnitudes $1/\sqrt2$.
These seeds attain equality in the original score too. The
[full half-rank proof](audits/HALF_RANK_RETENTION_CONVERSE.md) supplies
the equality steps and the elementary comparisons at the strict branches.

### 3.2 Two retained qubits out of four

Here $d=16$, $\mathrm{rank}S\le4$, $\mathrm{Tr}S^2=1$.
We prove $\sum_U\sqrt{a_U}\le4+2\sqrt2$, so $\Gamma(4,4)=4+2\sqrt2$.
Order the four singleton lengths as $a\ge b\ge c\ge e\ge0$, put
$T=a^2+b^2+c^2+e^2$, $y=2T$, $u=\mathrm{Tr}S/2$,
$v=\sqrt{1-u^2}$, and $W_i=2-a_{X_i}-a_{Z_i}$,
$\Delta=\sum_iW_i$. Evaluation of the four largest eigenvalues of J,
followed by the same centered rearrangement, gives

$$
R=\max\{b,(b+c+e)/2\},\qquad
y\le u(a+R)+v\sqrt{T-a^2-R^2},\quad
y\le(1+u^2)/2,\quad \Delta\ge4-u^2-y.                  \qquad\text{(11)}
$$

If the target is reached or exceeded, these inequalities imply
$u^2\ge\alpha=(4\sqrt2-3)/3$, $v^2+1-y\le r^2$,
$u>15/16$, $y\ge2r+v^2$, and every singleton length is at most
$u/2$. In particular rank is exactly four: rank at most three would
give $u^2\le3/4<\alpha$. For $\kappa=\|S\|$, spectral Cauchy
gives $\kappa\le(u+\sqrt3v)/2$. A local two-block calculation gives
$W_i\ge1-(u+\sqrt3v)(u-2b_i)$, where $b_i$ denotes that site's
singleton length. These reductions are derived in the
[quarter-rank geometry](audits/QUARTER_RANK_GEOMETRY.md) and
[nonflat converse, Sections 1–2](audits/NONFLAT_QUARTER_RANK_CONVERSE.md).

**Pair-dominant branch, $b\ge c+e$.** Set $p=a+b$,
$Q=c^2+e^2$, $w=u-p\ge0$, $\delta=v^2+1-y$,
$x=2(u+\sqrt3v)w$, and $h=\sqrt{uw}$. Equation (11) gives
$y\le up+v\sqrt Q$, $p^2+2Q\le y$,
$Q\le y(1-y)$, and $\delta\ge3v^2/2+h^2-vh/\sqrt2$.
Also $\Delta\ge2+\delta$, $W_1+W_2\ge2-x$, $0\le x<9/10$.
Grouped Cauchy and its monotonicity therefore give

$$
\sum_U\sqrt{a_U}\le2\sqrt{2+x}+2\sqrt{4-\delta-x}.
$$

This is at most $4+2\sqrt2$ when
$\delta\ge H(x)=2(2+\sqrt2)(\sqrt{2+x}-\sqrt2)-2x$.
Rationalizing gives $H(x)\le rx-6x^2/25$; the required bound follows
from the explicit sum of squares

$$
\delta-rx+\frac6{25}x^2\ge
\frac32\left(v-\frac h{3\sqrt2}-\frac8{15}h^2\right)^2
+\frac8{15}h^2\left(h-\frac1{2\sqrt2}\right)^2+\frac{h^2}{60}\ge0.
\qquad\text{(12)}
$$

Equality forces $u=y=1$, $a=b=1/2$, $c=e=0$.

**Other branch, $b\le c+e$.** In local blocks
$S=\left(\begin{smallmatrix}A&C\\C^\dagger&E\end{smallmatrix}\right)$,
retaining $\|C\|_2^2$ and the smallest positive eigenvalue $m_0$
improves the local bound: $\kappa-m_0\le\sqrt2v$ gives
$W_i\ge1-2(u-2b_i)(\sqrt2v+u-2b_i)$.
Put $\mu=u-2a$, $\zeta=b+c+e$, $k_0=u+\sqrt3v$,
$x=2\mu(\sqrt2v+\mu)$, $\lambda=2r/3$, and $B=4-4\sqrt2/3$.
The actual deficits and the top-four constraint imply

$$
\begin{gathered}
W_1\ge1-x,\quad \Delta\ge4-u^2-y,\quad
\Delta\ge4-3uk_0-k_0\mu+2k_0\zeta,\\
H\le u\zeta+v\sqrt{J-\zeta^2},\qquad
H=2y-u(u-\mu),\quad J=2y-(u-\mu)^2.
\end{gathered}                                                    \qquad\text{(13)}
$$

Set $\Delta_*=B+\lambda x(1-x)$, $Y=4-u^2-\Delta_*$.
If $y<Y$, already $\Delta>\Delta_*$. Otherwise a putative
$\Delta\le\Delta_*$ forces the fixed upper bound
$\zeta\le\zeta_0=(3u+\mu)/2-(u^2+Y)/(2k_0)$.
At $y=Y$, write $H_0,J_0$ for H,J. Analytically $H_0>1/2$;
the exact certificate gives

$$
C_0=uH_0-\zeta_0>0,\qquad
C_0^2-v^2(J_0-H_0^2)>0.                               \qquad\text{(14)}
$$

As y increases, H increases and $J-H^2$ decreases. If
$J_0-H_0^2<0$, no $y\ge Y$ is feasible. Otherwise (14) gives
$\zeta_0<uH_0-v\sqrt{J_0-H_0^2}$, the lower feasible circle root.
That root increases until its radicand becomes negative, after which
feasibility fails. Holding $\zeta_0$ at Y is essential. Equation (13)
is incompatible with its proposed upper bound, proving $\Delta>\Delta_*$.

For precision, (14)'s two positivity claims reduce under
$\tau=v/u,m=\mu/u$ to the polynomials C,P in
[the certificate definition](audits/NONFLAT_QUARTER_RANK_CONVERSE.md#5-the-exact-rational-certificate),
on the single box $[0,9/25]^2$. Their denominators are positive.
Their 35 and 99 tensor Bernstein coefficients are bounded below by
$4/25$ and $1/10000$, respectively, using rational arithmetic and
integer-verified radical enclosures. Nonnegative Bernstein basis functions
sum to one, so these are whole-box proofs, not sampled sign checks.
The reproducible [exact checker](../tools/check_nonflat_quarter_rank_certificate.py)
and [certificate report](../results/nonflat_quarter_rank_certificate.json)
are essential parts of this finite reduction; the full note derives
$H_0>1/2$ and the box bounds before applying the certificate.

Finally grouped Cauchy gives
$\sum_U\sqrt{a_U}\le\sqrt{4-2W_1}+\sqrt{36-6\Delta+6W_1}$.
For $x<1-1/\sqrt2$, monotonicity allows $W_1=1-x$ and
$\Delta=\Delta_*$; its exact target threshold is
$B+\lambda x-2(1+\sqrt2)x^2/[3(\sqrt{1+x}+1)^2]\le\Delta_*$.
For $1-1/\sqrt2\le x<21/32$, instead
$\Delta_*\ge5-2\sqrt2$, and Cauchy over all eight queries suffices.
Strict $\Delta>\Delta_*$ makes this branch strict. Only the first
branch can attain equality; its Pauli equality conditions give precisely

$$
\rho=|\beta_1\rangle\langle\beta_1|\otimes
|\beta_2\rangle\langle\beta_2|\otimes I_4/4,             \qquad\text{(15)}
$$

up to original-site permutation, with both pure states X/Z bisectors.
Equations (1)–(3) now finish (6), including its arbitrary-instrument scope.

## 4. A collective advantage with five memory qubits

Take $n=31,q=5,D=32$. Label the X-basis by bit strings, put
$\mathcal C=\{0,e_1,\ldots,e_n\}$, and use orthogonal output labels
for its 32 elements. Set

$$
p_0=\tfrac12,\quad p_{e_i}=\tfrac1{2n},\qquad
L=\sum_{u\in\mathcal C}\sqrt{p_u}\,|u\rangle_Q\langle u|_X,
\qquad K_s=LZ^s\quad(s\in\{0,1\}^n).
\qquad\text{(16)}
$$

Store s classically. No normalization factor is missing: translating the
diagonal seed gives $\sum_sK_s^\dagger K_s=I$, since $\sum_up_u=1$.
All outcomes are accepted and every branch has quantum dimension 32.
For X use the diagonal output signs $(-1)^{u_i+s_i}$. For Z use
$|0\rangle\langle e_i|+|e_i\rangle\langle0|$, zero on the other
output states. This is a Hermitian contraction; zero means a fair output,
not a discarded event. Direct translation sums give

$$
\sum_sK_s^\dagger B_{s,i,X}K_s=X_i,\qquad
\sum_sK_s^\dagger B_{s,i,Z}K_s=2\sqrt{p_0p_{e_i}}Z_i=Z_i/\sqrt{31}.
\qquad\text{(17)}
$$

These operator identities establish the advertised arbitrary-input
statistics without a 31-qubit numerical simulation.

For comparison, an **original-site-retention** instrument admits a Kraus
refinement in which every nonzero branch factors as
$K_c=M_c\otimes\langle v_c|$ across original sites $T_c$ and their
complement, with $|T_c|\le q$ and output dimension at most $2^q$.
All factors and the retained set may depend on c, and the refined
operators obey $\sum_cK_c^\dagger K_c=I$. The vectors $v_c$ may be
entangled across discarded sites, so their measurement may be joint.
Decoders are arbitrary contractions, and outcome probabilities may
depend on the input. This definition includes random subset retention
and joint processing of discarded sites, but not all collective encoders.

Normalize $v_c$ and absorb its norm into $M_c$. Each normalized Gram
is then $\tau_{T_c}\otimes|v_c\rangle\langle v_c|$, with
$\mathrm{Tr}\tau_{T_c}=1$ and $\langle v_c|v_c\rangle=1$.
For uniform nonnegative weights $a,b$, a retained site's weighted
score is at most $a+b$. A discarded site's is at most
$\sqrt{a^2+b^2}$, by its reduced Bloch vector even when $v_c$ is
entangled. Equation (2) therefore gives the class-wide bound

$$
\sum_i(ax_i+bz_i)\le q(a+b)+(n-q)\sqrt{a^2+b^2}.          \qquad\text{(18)}
$$

With all $x_i=1$, set $b=1$ and let a tend to infinity: (18)
implies $\sum_i z_i\le q$. The complete collective instrument (16)
instead has $\sum_i z_i=\sqrt{31}>5$. It strictly separates the
entire stated class under the same branch cap. The
[exact-axis note](EXACT_AXIS_SPECTRAL_REDUCTION.md) gives the broader
weighted class region $\sum_iw(x_i,z_i)\le q$ and the spectral context.
The separation does not establish an unrestricted optimum at (31,32),
an equal-accuracy improvement, or an efficient implementation.

## 5. A separate all-size structural companion

The [balanced-spectrum theorem](audits/BALANCED_SPECTRUM_OPTIMALITY.md)
fixes the spectrum rather than the memory rank. For every n, every
traceless Hermitian reflection R, and $0\le t\le1$, set
$\rho_t=(I+tR)/d$. Then

$$
\max_R g(\rho_t)=2n-2+\sqrt{4-2t^2}.                    \qquad\text{(19)}
$$

For $t>0$, maximizers are exactly
$\rho_t=(I+tB_i)/2\otimes I_{\rm rest}/2^{n-1}$, where
$B_i=(\pm X_i\pm Z_i)/\sqrt2$ acts on the chosen site; at $t=1$
its local state is pure. At $t=0$ there is just the maximally mixed
state. In particular, every flat rank-$d/2$ seed
obeys the retention converse for every n. This does not assert that
an unrestricted half-rank optimizer has a flat spectrum.

The [stability theorem](audits/BALANCED_SPECTRUM_STABILITY.md) gives a
dimension-independent statement: a flat half-rank seed with score gap
$\epsilon$ from $2n-2+\sqrt2$ lies within full trace-norm distance
$16\sqrt{2\epsilon}$ of a seed (10). Its square-root exponent is
necessary. It also gives an arbitrary-support spectral neighborhood:
for $k=d/2$, $\mathrm{rank}\rho\le k$,

$$
\sqrt{2\left(1-\frac{\mathrm{Tr}\sqrt\rho}{\sqrt k}\right)}
\le\frac1{4096n}\quad\Longrightarrow\quad g(\rho)\le2n-2+\sqrt2.
\qquad\text{(20)}
$$

Equality requires retention. The radius is sufficient, not optimal.
These companion results supply all-size structure and limited nonflat
control; they are not prerequisites for the three operational theorems.

## 6. Attribution and the remaining boundary

The framework is established. Ioannou et al.'s dimension-constrained
measurement simulation and Jones et al.'s steering/Schmidt correspondence
precede this analysis. Sekatski's *The bottleneck dimension of quantum
operations*, arXiv:2608.25010v1, Definition 3 and Sections III.B–IV.A,
also contains this model as measurement d-simulability with classical
records. Its universal noisy-channel converse concerns quantum outputs;
it does not automatically give the present restricted-readout thresholds.

Ballester–Wehner–Winter's postmeasurement-information framework is
equivalent here: for the uniform ensemble $(I+sU)/d$, delaying U
until after storage gives $p_{\rm success}=(1+\eta)/2$ after the
same symmetries. The site label is part of our delayed query. Bluhm–Rauber–Wolf
also study approximate measurement-relative compression. Their common
CPTP reconstruction requirement differs from query-dependent binary
readout; their Section 9.1 explicitly discusses unrestricted compressed
effects. Neither framework is claimed as new. Exact source locators are
in [CORE_PRIOR_COMPARISON](CORE_PRIOR_COMPARISON.md); the BWW reduction is
derived in [the original audit, Section 6.1](audits/PROOF_AND_NOVELTY_AUDIT.md#61-ballesterwehnerwinter-direct-earlier-problem-and-exact-endpoint).

| Proof ingredient | Established source and use here |
|---|---|
| Independent-setting CHSH monogamy | Cheng–Hall, arXiv:1610.09302v3, Eqs. (13)–(14): the weighted dimension-two converse. |
| Orthogonal-qubit compatibility; incompatibility weight | Yu–Liu–Li–Oh, arXiv:0805.1538v2, Theorem 1 gives the disk; Pusey, arXiv:1502.03010v2, Section III defines the weight. The local disk geometry evaluates w here. |
| Squared root fidelity bounded by affinity | Audenaert–Nussbaum–Szkoła–Verstraete, arXiv:0708.4282v1, Appendix A, Theorem 6 at s=1/2: the finite half/quarter-rank relaxation. |
| Cube-star spectrum | Avni–Samorodnitsky, arXiv:2411.14597v1, Example 1.12: prior spectral mathematics underlying (16). |

The supplied deductions are the complete all-n one-qubit allocation
rule, the unrestricted integer-budget optimum through four inputs,
and the complete collective instrument with its precise retention-class
separation. The focused source comparison is not an exhaustive priority
search. The balanced and stability notes separately locate their
fidelity-response and quantum-FKN antecedents.

Unrestricted equal-accuracy retention remains open outside the proved
ranges, beginning at $(n,q)=(5,2)$; the unequal-accuracy separation
does not decide it. The general sharp entropy bound and asymptotic
common-accuracy rate also remain open. The
[affinity-method limit](audits/AFFINITY_METHOD_LIMIT.md) proves that the
finite proof's stronger affinity bound cannot extend universally, while
the [spectral-layer comparison](audits/SPECTRAL_LAYER_SCORE_BOUND.md)
retains decoder information with a nonzero error term. These are future
research boundaries, not missing premises of the operational results above.
