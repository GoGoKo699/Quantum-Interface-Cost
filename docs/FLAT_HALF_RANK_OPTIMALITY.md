# Flat half-rank seed optimum through four input qubits

Date: 22 September 2026. Research base:
`87b6432cdd1f29bc4981f24bd6732bb933741193`.

**Status:** supplied analytical deduction, independently reconstructed within
this workspace. The proof covers every rank-four orthogonal projector on
three qubits and every rank-eight orthogonal projector on four qubits,
including entangled subspaces and nonmaximally mixed complementary
marginals. A stated restriction on the singleton Pauli coefficients gives
a further extension to arbitrary n. The result does not cover general
nonflat states and does not certify publication novelty.

For a density matrix rho on n qubits, write

$$
g(\sqrt\rho)=\sum_{i=1}^n\sum_{b=X,Z}
\|\sqrt\rho\,P_{i,b}\sqrt\rho\|_1.
$$

The [normalized-seed reduction](COLLECTIVE_ENCODING_REDUCTION.md) identifies
this score with the unrestricted operational objective after optimization
over Gram matrices of the permitted rank. Restricting the Gram matrix to a
flat spectrum is a restriction of that optimization, not an assumption
about the original physical encoder.

## 1. Theorem and its exact scope

**Theorem.** Let P be any rank-`2^(n-1)` orthogonal projector on n qubits,
with `1<=n<=4`. For `rho=P/2^(n-1)`,

$$
\boxed{g(\sqrt\rho)\le 2(n-1)+\sqrt2.}
\tag{1}
$$

Equality holds if and only if, for some input site i,

$$
P=|\beta\rangle\langle\beta|_i\otimes I_{\mathrm{rest}},
\tag{2}
$$

where beta is a pure X/Z bisector: its Bloch vector has zero Y component
and X and Z components each of absolute value `1/sqrt(2)`.

**Extension.** The same bound and equality statement hold at every n if
the single-site X/Z Pauli coefficients of `2P-I` are nonzero on at most
four input sites. There is no restriction on its higher-weight Pauli
coefficients.

Because `S(rho)=n-1`, (1) is also the conjectured seed entropy inequality
for these flat half-rank states. The theorem includes projectors not
covered by the earlier requirement that `Tr_i P=I` for at least one i.
Its proof uses the reflection constraint to show that a seed with a
large score must have a large single-site Pauli component.

The unrestricted finite-budget statement

$$
\Gamma(3,4)\le4+\sqrt2
$$

still requires control of general states of rank at most four. Section 6
also excludes the lower flat ranks in this three-qubit block; any violating
Gram matrix must therefore be nonflat, of rank three or four. The same
section excludes every flat rank at most eight at n=4; nonflat states
leave the unrestricted `(n,q)=(4,3)` problem open. The theorem below does not permit
replacing a general Gram matrix by the normalized projector onto its
support.

## 2. Pauli weights and the compression bound

Let `d=2^n`, `r=d/2`, put `tau(A)=Tr(A)/d`, and introduce the reflection

$$
S=2P-I.
$$

Here S denotes an operator, not von Neumann entropy. It obeys
`S=S^dagger`, `S^2=I`, and `tau(S)=0`. Expand in the orthonormal Pauli
basis:

$$
S=\sum_{a\ne I}s_a\sigma_a,
\qquad s_a\in\mathbb R,
\qquad \sum_a s_a^2=1.
\tag{3}
$$

For each of the 2n local X/Z queries U, define its anticommuting weight

$$
w_U=\sum_{a:\{\sigma_a,U\}=0}s_a^2.
$$

The associated score term satisfies

$$
F_U:=\frac1r\|PUP\|_1\le\sqrt{1-w_U}.
\tag{4}
$$

Indeed, `PUP` acts on an r-dimensional subspace. Trace-norm versus
Hilbert--Schmidt Cauchy--Schwarz gives

$$
F_U\le\sqrt{\frac{\operatorname{Tr}[(PUP)^2]}r}.
$$

Since `tau(SUSU)=1-2w_U`, cyclicity of trace gives

$$
\operatorname{Tr}[(PUP)^2]
=\operatorname{Tr}(PUPU)
=\frac d4\bigl[1+\tau(SUSU)\bigr]
=r(1-w_U),
$$

which proves (4).

Let T be the total squared Pauli weight on the 2n single-site X/Z
strings:

$$
T=\sum_{i=1}^n(s_{X_i}^2+s_{Z_i}^2),\qquad 0\le T\le1.
\tag{5}
$$

Each of those strings anticommutes with exactly one query. Every other
nonidentity Pauli string anticommutes with at least two queries: a local
Y contributes two, while each nonidentity X or Z factor contributes one.
Therefore

$$
\sum_U w_U\ge T+2(1-T)=2-T.
\tag{6}
$$

For any specified site i, its two-query deficit obeys

$$
w_{X_i}+w_{Z_i}\ge s_{X_i}^2+s_{Z_i}^2.
\tag{7}
$$

These estimates alone do not give (1). The additional constraint on the
distribution of singleton weight is decisive.

## 3. A four-sign constraint from the reflection

Define the singleton part of S by

$$
L=\sum_{i=1}^n(s_{X_i}X_i+s_{Z_i}Z_i)
=\sum_{i=1}^n\beta_i B_i,
\qquad
\beta_i=\sqrt{s_{X_i}^2+s_{Z_i}^2}\ge0.
\tag{8}
$$

When `beta_i>0`, `B_i` is the corresponding unit Pauli direction in
the local X/Z plane. For `beta_i=0`, its choice is immaterial. Different
`B_i` commute, each has eigenvalues `+1,-1`, and their normalized joint
spectral law is uniform on the sign strings. Orthogonality of Pauli strings
and the trace-norm duality inequality imply

$$
T=\tau(SL)\le\tau|L|,
\tag{9}
$$

because `||S||_infinity=1`.

By hypothesis at most four beta coefficients are nonzero. Order those
coefficients, padding with zeros if needed, as `a>=b>=c>=d>=0`.
For four independent uniform signs the elementary exact expression is

$$
\begin{aligned}
\tau|L|
&=\mathbb E|a\varepsilon_1+b\varepsilon_2+c\varepsilon_3+d\varepsilon_4|\\
&=\frac{\max(a,b+c+d)+\max(a,b+c-d)+2a}{4}\\
&=\max\left\{a,\frac{3a+b+c+d}{4},\frac{a+b+c}{2}\right\}.
\end{aligned}
\tag{10}
$$

To verify it, first average over the first sign, using
`(|a+x|+|a-x|)/2=max(a,|x|)`. The four remaining magnitudes, up to
a simultaneous sign reversal, are `b+c+d`, `b+c-d`, `b-c+d`, and
`|b-c-d|`. The last two are at most a. Resolving the two remaining
maxima gives the last line of (10).

The coefficient vectors of the second and third linear expressions
in (10) both have Euclidean norm `sqrt(3)/2`. Thus

$$
\tau|L|\le\max\left\{\beta_{\max},\frac{\sqrt{3T}}2\right\}.
$$

For `T>3/4` the second argument is strictly smaller than T.
Equations (9)--(10) consequently force

$$
\boxed{\beta_{\max}\ge T\qquad(T>3/4).}
\tag{11}
$$

In particular, one site carries singleton squared weight at least
`T^2`. This uses the operator-norm constraint on S; it is false for
an arbitrary unit vector of Pauli coefficients without that constraint.

The restriction to four singleton-active sites is needed for this
particular sign-sum estimate. For five coefficients
`(7,2,2,2,2)/sqrt(65)`, their squared sum is one but

$$
\mathbb E\left|\frac{7\varepsilon_1+
2(\varepsilon_2+\varepsilon_3+\varepsilon_4+\varepsilon_5)}{\sqrt{65}}\right|
=\frac{57}{8\sqrt{65}}
>\max\left\{\frac7{\sqrt{65}},\frac{\sqrt3}{2}\right\}.
$$

To obtain the expectation, average over the first sign: the result is
7 except when all four other signs agree, an event of probability
`1/8`, when it is 8, before dividing by `sqrt(65)`. This refutes a
five-sign extension of the intermediate estimate. It does not produce
a valid reflection with these coefficients or refute the general flat
seed conjecture.

## 4. Proof of the optimum

The cases n=1 and n=2 already follow, with their equality statements,
from the qubit Bloch-ball bound and the independently checked
[one-retained-qubit theorem](ONE_QUBIT_OPTIMALITY.md), respectively.
For the rest of the proof let `n>=3` and `m=2n`.

First suppose `T<=3/4`. Applying Cauchy--Schwarz to all m terms in
(4), followed by (6), gives

$$
g(\sqrt\rho)
\le\sqrt{m\left(m-\sum_Uw_U\right)}
\le\sqrt{m(m-2+T)}
\le\sqrt{m(m-5/4)}
<m-2+\sqrt2.
\tag{12}
$$

The strict final inequality follows by squaring: with `c=2-sqrt(2)`,
the difference of the squared right sides is
`m(5/4-2c)+c^2>0`, since `5/4>2c`.

Now suppose `T>3/4`. Choose the site furnished by (11). Let W be
the sum of its two query deficits and V the sum of the other `m-2`.
Equations (6)--(7) and (11) give

$$
W\ge T^2,\qquad W+V\ge2-T.
\tag{13}
$$

Cauchy--Schwarz separately on the two groups gives

$$
g(\sqrt\rho)
\le\sqrt{2(2-W)}+\sqrt{(m-2)(m-2-V)}.
\tag{14}
$$

The right side decreases with either group deficit. Its maximum subject
to (13) is therefore attained on `W+V=2-T`: if the total is larger,
one can reduce V or reduce W as far as its lower bound, increasing the
right side. This is possible because `T^2<=2-T` for `0<=T<=1`.
On that line the right side becomes

$$
h_T(W)=\sqrt{4-2W}+\sqrt{(m-2)(m-4+T+W)}.
$$

Its derivative is nonpositive whenever `nW>=2-T`. Here

$$
nT^2\ge3T^2\ge2-T
$$

holds because `T>3/4>2/3`. Consequently the maximum occurs at
`W=T^2`, giving

$$
g(\sqrt\rho)\le B_n(T):=
2\sqrt{1-T^2/2}
+\sqrt{(m-2)(m-4+T+T^2)}.
\tag{15}
$$

The function `B_n` is strictly increasing on `[0,1]`. Since
`T+T^2<=2`, its derivative obeys

$$
\begin{aligned}
B_n'(T)
&=\frac{\sqrt{m-2}(1+2T)}{2\sqrt{m-4+T+T^2}}
-\frac{T}{\sqrt{1-T^2/2}}\\
&\ge\frac{1+2T}{2}-\frac{T}{\sqrt{1-T^2/2}}>0.
\end{aligned}
$$

Both terms being compared are nonnegative. The difference after
cross-multiplication and squaring is

$$
\begin{aligned}
&(1+2T)^2(1-T^2/2)-4T^2\\
&\quad=1+4T-\frac12T^2-2T^3-2T^4\\
&\quad\ge1+4T-\frac92T^2\ge\frac12>0.
\end{aligned}
\tag{16}
$$

The first inequality uses `T^3,T^4<=T^2`; the second follows because
the concave quadratic has endpoint values 1 and `1/2` on `[0,1]`.
Thus (15) yields

$$
g(\sqrt\rho)\le B_n(1)=m-2+\sqrt2,
$$

proving (1).

## 5. Equality

Equation (12) is strict. In the other regime, strict monotonicity of `B_n`
forces `T=1` at equality. Equation (11) then gives
`beta_max>=1`; since the squared beta coefficients sum to one,
exactly one coefficient is nonzero. There is no Pauli weight outside
the singleton subspace. Therefore

$$
S=aX_i+bZ_i,\qquad a^2+b^2=1
$$

for one site i. The other `2(n-1)` query scores equal one, and the local
two scores equal `|a|,|b|`. Their sum reaches `sqrt(2)` exactly when
`|a|=|b|=1/sqrt(2)`, which is precisely (2). Conversely every
projector in (2) attains the bound.

This proves the exact optimum and equality characterization for the stated
half-rank family.

## 6. Lower flat ranks through four input qubits

A separate elementary estimate is useful here. For every rank-r projector
P on n qubits, set `d=2^n`, `rho=P/r`, and `S=2P-I` as before. Now the
identity Pauli coefficient of S is

$$
s_0=\tau(S)=\frac{2r}{d}-1,
$$

and the total nonidentity squared Pauli weight is `1-s_0^2`. Define
`w_U` using only the anticommuting nonidentity Pauli strings. The trace
calculation changes to

$$
\begin{aligned}
\operatorname{Tr}[(PUP)^2]
&=\frac d4\left[1+2s_0+\tau(SUSU)\right]\\
&=r-\frac d2w_U.
\end{aligned}
$$

Hence, for each query,

$$
F_U=\frac{\|PUP\|_1}{r}
\le\sqrt{1-\frac{d}{2r}w_U}.
$$

Every nonidentity string anticommutes with at least one query, so
`sum_U w_U>=1-s_0^2`. Cauchy--Schwarz therefore yields the general
flat-rank estimate

$$
\boxed{
g(\sqrt{P/r})
\le\sqrt{2n\left(2n-2+\frac{2r}{d}\right)}.
}
\tag{17}
$$

At n=3 and `r<=3` this is at most `sqrt(57/2)`, strictly below
`4+sqrt(2)`. Together with the half-rank theorem, it excludes every
flat Gram matrix of rank at most four from improving the finite
`(n,q)=(3,2)` subset strategy. The independently established unrestricted
rank-at-most-two theorem then leaves only **nonflat rank-three or
rank-four states** as possible finite-block witnesses.

### Flat rank-three states on three qubits also satisfy the entropy bound

The preceding estimate alone addresses the finite-budget threshold.
A sharper singleton estimate proves the entropy inequality for this
particular lower-rank family as well. For n=3 and r=3, order the singleton
coefficients of L as `a>=b>=c>=0`. Its three largest eigenvalues are
`a+b+c`, `a+b-c`, and `a-b+c`. Since `Tr L=0`,

$$
T=\tau(SL)=\frac14\operatorname{Tr}(PL)
\le\frac{3a+b+c}{4}
\le\frac{\sqrt{11T}}4,
$$

so `T<=11/16`. The first inequality follows by writing P in an eigenbasis
of L: its diagonal entries lie in `[0,1]` and sum to three, so the trace
is at most the sum of L's three largest eigenvalues. The nonidentity
Pauli mass is `1-s_0^2=15/16`. Consequently

$$
\sum_U w_U\ge2\left(\frac{15}{16}\right)-\frac{11}{16}
=\frac{19}{16},
$$

and the general compression bound gives

$$
\boxed{
g(\sqrt{P/3})\le\sqrt{6\left(6-\frac43\frac{19}{16}\right)}
=\sqrt{\frac{53}{2}}
<3\sqrt2+(2-\sqrt2)\log_2 3.
}
\tag{18}
$$

The strict entropy comparison is exact: `3^7>2^11` gives
`log_2(3)>11/7`, so the entropy line is greater than
`(22+10sqrt(2))/7`. The square of this last expression minus `53/2`
is `(880sqrt(2)-1229)/98>0`, using `sqrt(2)>7/5`. Thus every flat
rank-three three-qubit Gram matrix is also excluded as an entropy-based
rate witness. No flat rank-three optimality claim is made.

### Completing the lower flat ranks at four input qubits

At n=4, (17) excludes `r<=6` by the strict bound
`g<=sqrt(54)<6+sqrt(2)`. The remaining lower flat rank r=7 requires
one further elementary observation. Here

$$
s_0=-\frac18,\qquad
u:=1-s_0^2=\frac{63}{64},\qquad
\frac{d}{2r}=\frac87.
$$

For each singleton axis `B_i` in (8), its coefficient obeys

$$
\beta_i=\tau(SB_i)=\frac{2\operatorname{Tr}(PB_i)}{16}
\le\frac{2r}{16}=\frac78.
$$

This uses `Tr B_i=0`, `B_i<=I`, and `P>=0`. The argument in
Section 3 does not require `tau(S)=0`: Pauli orthogonality still gives
`tau(SL)=T` and `||S||_infinity=1`. Thus `T>3/4` still forces
`T<=beta_max<=7/8`; for `T<=3/4` the same final upper bound is automatic.
Counting one anticommutation for singleton X/Z strings and at least two
for the other nonidentity strings now gives

$$
\sum_Uw_U\ge2u-T
\ge\frac{63}{32}-\frac78=\frac{35}{32}.
$$

The general compression bound and Cauchy--Schwarz yield

$$
g(\sqrt{P/7})
\le\sqrt{8\left(8-\frac87\sum_Uw_U\right)}
\le\sqrt{54}<6+\sqrt2.
\tag{19}
$$

For n=2, the only smaller flat rank is r=1, and (17) gives
`sqrt(10)<2+sqrt(2)`. For n=1 there is no smaller positive rank.
Consequently, for **every `1<=n<=4` and every `1<=r<=2^(n-1)`**, a
flat rank-r seed has score at most `2(n-1)+sqrt(2)`. Equality requires
`r=2^(n-1)` and the bisector projector (2). This is an exact finite-budget
optimum over all allowed flat spectra in those blocks. It does not prove
the entropy bound for every lower flat rank, nor does it exclude nonflat
states in the unrestricted optimization.

## 7. Remaining scope

The proof is a finite Pauli-coefficient and trace-norm argument. It
does not assume a stabilizer encoder, a balanced complementary marginal,
product eigenvectors, a classical input description, extra specimens,
average memory, or postselected success. The original operational
quantifiers remain those of the seed reduction. Nonflat finite-block
optimality and the general seed entropy inequality remain open. No prior theorem is
claimed to be novel, and a theorem-level literature comparison is still
needed before claiming that this flat-spectrum result is new.
