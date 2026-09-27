# The unrestricted half-rank retention converse through four inputs

Research base: `3aad8227ed448eadfaa5ebc4d33bfc9845dd4f8c` (PR #50).
Status: derived with the supplied analytical proof and independently
reconstructed within this workspace, including the integrated theorem,
rank-deficient cases and equality classification. This is internal
mathematical review, not external peer review or a publication-priority
claim.

For two, three or four unknown input qubits, retaining all but one site
is optimal at quantum memory dimension `2^(n-1)`, even with arbitrary
collective encoding and unrestricted binary-POVM readouts:

$$
\boxed{\Gamma(n,2^{n-1})=2n-2+\sqrt2\qquad(n=2,3,4).}
\tag{1}
$$

The [normalized-seed reduction](../COLLECTIVE_ENCODING_REDUCTION.md)
therefore gives the exact common contrast and minimum uniform binary
sampling error at these memory budgets:

$$
\boxed{\eta_{\max}(n,n-1)=\frac{2n-2+\sqrt2}{2n},\qquad
\varepsilon_{\min}(n,n-1)=\frac{2-\sqrt2}{4n}.}
\tag{2}
$$

In particular `Gamma(3,4)=4+sqrt(2)` and `Gamma(4,8)=6+sqrt(2)`.
At three inputs, the contrast is `(4+sqrt(2))/6` and the error is
`(2-sqrt(2))/12`. This closes all three previously unresolved
three-input reflection signatures and their general binary-POVM
formulation. The two-input conclusion also follows from the earlier
[one-retained-qubit theorem](../ONE_QUBIT_OPTIMALITY.md).
The proof uses no Jordan angle, commutation, subsystem, flat-spectrum or
channel hypothesis.
It retains the original model: one unknown specimen, one delayed local
X/Z query, arbitrary collective encoding, classical records of unrestricted
finite size, worst-case quantum dimension and uniform arbitrary-input
statistics. It does not evaluate the general asymptotic memory rate.

## 1. A stronger affinity inequality

Fix `n in {2,3,4}`, put `d=2^n` and `k=d/2`, and let rho be any
n-qubit density matrix of rank at most k. Set `S=sqrt(rho)` and write

$$
\mathcal A=\{X_i,Z_i:1\le i\le n\},\qquad
a_A=\operatorname{Tr}(SASA).
$$

We will prove the stronger bound

$$
\boxed{\sum_{A\in\mathcal A}\sqrt{a_A}\le2n-2+\sqrt2.}
\tag{3}
$$

The standard squared-root-fidelity/affinity comparison gives
`||SAS||_1^2<=a_A`. Its primary-source attribution and a supplied proof
are in [STRONG_ENTROPIC_CONVERSE, Section 3](../STRONG_ENTROPIC_CONVERSE.md#3-root-fidelity-affinity-and-the-two-pauli-energy).
Consequently (3) bounds the original normalized-seed score
`g(S)=sum_A||SAS||_1`. This is a bound on every admissible seed, including
arbitrary nonflat spectra, not a replacement of a seed by its flat support.

Throughout the proof `S>=0`, `Tr(S^2)=1` and `rank(S)<=k`.
Positivity and Hilbert--Schmidt Cauchy--Schwarz imply `0<=a_A<=1`.

## 2. Positivity bounds the local Pauli mass

Use the orthonormal Pauli basis `sigma_p/sqrt(d)`. Define

$$
t=\operatorname{Tr}S,\qquad u=t/\sqrt k,\qquad v=\sqrt{1-u^2}.
\tag{4}
$$

The rank bound gives `0<u<=1`. The identity coefficient is
`t/sqrt(d)=u/sqrt(2)`. Write the part of S on the 2n queried Pauli words as

$$
L=\frac1{\sqrt d}\sum_{i=1}^n b_i B_i,\qquad
b_i=\sqrt{s_{X_i}^2+s_{Z_i}^2},\qquad
B_i=\frac{s_{X_i}X_i+s_{Z_i}Z_i}{b_i},
$$

and put

$$
T=\sum_i b_i^2=\operatorname{Tr}(L^2)=\operatorname{Tr}(SL),
\qquad y=2T.
\tag{5}
$$

When `b_i=0`, the unit X/Z-plane direction B_i may be chosen arbitrarily.
The B_i commute, and the spectrum of L consists of all d sign sums
`(sum_i +-b_i)/sqrt(d)`. It is symmetric, so the positive
part satisfies `Tr(L_+^2)=T/2`. Positivity of S now gives

$$
T=\operatorname{Tr}(SL)
\le\operatorname{Tr}(SL_+)
\le\|S\|_2\|L_+\|_2=\sqrt{T/2}.
$$

Thus `0<=T<=1/2`, or `0<=y<=1`.

The Pauli-conjugation operator `K -> sum_A AKA` has eigenvalue 2n
on the identity, `2n-2` on these local X/Z words, and at most `2n-4`
on every other Pauli word. The squared Pauli coefficients of S sum
to one. Therefore

$$
\sum_A a_A\le2n-4+4\frac{t^2}{d}+2T=2n-4+2u^2+y.
\tag{6}
$$

If `T=0`, Cauchy--Schwarz gives
`sum_A sqrt(a_A)<=sqrt(2n(2n-2))`.
If `u<=sqrt(3)/2`, it gives
`sum_A sqrt(a_A)<=sqrt(2n(2n-3/2))`.
Both are strictly below `2n-2+sqrt(2)`, as follows by squaring and
using `3/2>4-2sqrt(2)`.
It remains to consider `T>0` and `u>sqrt(3)/2`.

## 3. Half rank preserves the direction of the local mass

Order the b_i and pad by zeros to four entries
`b_1>=b_2>=b_3>=b_4>=0`. For four independent uniform signs, the
exact mean is

$$
M:=\mathbb E\left|\sum_{i=1}^4 b_i\epsilon_i\right|
=\max\left\{b_1,\frac{3b_1+b_2+b_3+b_4}{4},
                 \frac{b_1+b_2+b_3}{2}\right\}.
\tag{7}
$$

Indeed, averaging first over the first sign gives
`[2b_1+max(b_1,b_2+b_3+b_4)+max(b_1,b_2+b_3-b_4)]/4`.
Resolving the two maxima gives (7), as in the earlier flat half-rank
proof. Each of its two nonlargest-coordinate linear forms has Euclidean
coefficient norm `sqrt(3)/2`. In particular `0<M<=sqrt(T)`.

Let `l_1>=...>=l_k` be the k largest eigenvalues of L. They form
its nonnegative half, including zeros when necessary. Their mean and
centered squared sum are

$$
\mu=\frac1k\sum_{j=1}^k l_j=\frac{M}{\sqrt d},\qquad
\sum_{j=1}^k(l_j-\mu)^2=\frac{T-M^2}{2}.
\tag{8}
$$

Let `lambda_1,...,lambda_k` be the eigenvalues of S in decreasing
order, padded by zero if its rank is smaller than k. The standard
Hermitian trace rearrangement inequality, followed by centered
Cauchy--Schwarz, yields

$$
\begin{aligned}
T=\operatorname{Tr}(SL)
&\le\sum_{j=1}^k\lambda_j l_j\\
&\le t\mu+
\sqrt{1-t^2/k}\sqrt{(T-M^2)/2}.
\end{aligned}
$$

With `c=M/sqrt(T)`, divide by `sqrt(T/2)` to obtain

$$
\boxed{\sqrt y\le uc+v\sqrt{1-c^2}.}
\tag{9}
$$

This is the rank-sensitive step. It keeps the direction of the local
Pauli coefficients together with the spectral nonuniformity v.
A bound on the sum of the affinities alone would lose that relation.

## 4. The sum branch has a strict gap

Suppose either nonlargest-coordinate expression in (7) attains M,
including a tie.
Then `c<=sqrt(3)/2`. Since `u>sqrt(3)/2`, the right side of (9)
increases with c on that interval. Hence

$$
y\le\frac{(\sqrt3u+v)^2}{4}.
$$

Using `u^2+v^2=1`, the largest eigenvalue of

$$
\begin{pmatrix}11/4&\sqrt3/4\\\sqrt3/4&1/4\end{pmatrix}
$$

is `(3+sqrt(7))/2`. Thus (6) and Cauchy--Schwarz give

$$
2u^2+y\le\frac{3+\sqrt7}{2},\qquad
\sum_A\sqrt{a_A}
\le\sqrt{2n\left(2n-4+\frac{3+\sqrt7}{2}\right)}
<2n-2+\sqrt2.
\tag{10}
$$

The squared gap in the final strict comparison is
`n(4sqrt(2)-3-sqrt(7))+6-4sqrt(2)>0`.
Its first coefficient is positive because
`(3+sqrt(7))^2=16+6sqrt(7)<32`, using `63<64`.

## 5. The dominant-site branch reduces to one positive quadratic

It remains that `M=b_i` for a chosen site i. Define the actual
affinity deficits

$$
d_A=1-a_A,\qquad W=d_{X_i}+d_{Z_i},\qquad D=\sum_A d_A.
$$

For each A, `1-a_A` equals twice the total squared Pauli coefficient
mass of S on words anticommuting with A. The local mass at site i
contributes to exactly one of its two queries. Equations (5)--(6)
therefore imply

$$
W\ge2b_i^2=yc^2,\qquad D\ge4-2u^2-y=:E.
\tag{11}
$$

If `u^2+y<1`, (6) gives `sum_A a_A<2n-3+u^2<=2n-2`, which already proves
the strict bound. Assume instead `u^2+y>=1`. The unit-circle constraint
(9) implies

$$
c\ge u\sqrt y-v\sqrt{1-y}\ge0,
\qquad
W\ge w:=y\bigl[u\sqrt y-v\sqrt{1-y}\bigr]^2.
\tag{12}
$$

For completeness, write `u=cos(theta)`, `c=cos(phi)` and
`sqrt(y)=cos(alpha)`, with angles in `[0,pi/2]`. Equation (9) says
`cos(theta-phi)>=cos(alpha)`, hence `|theta-phi|<=alpha` and
`c>=cos(theta+alpha)`. The assumed `u^2+y>=1` makes this last
cosine nonnegative, allowing its square in (12).

Apply Cauchy--Schwarz separately to the two selected queries and the
other `2n-2`. Here `0<=W<=2` and `0<=D-W<=2n-2`.
The concave square-root tangents at `W=1` and `D-W=0`
then give

$$
\begin{aligned}
\sum_A\sqrt{a_A}
&\le\sqrt{2(2-W)}+\sqrt{(2n-2)(2n-2-D+W)}\\
&\le\sqrt2+\frac{1-W}{\sqrt2}+2n-2-\frac{D-W}{2}\\
&=2n-2+\sqrt2+
\frac{(\sqrt2-1)(1-W)-(D-1)}2.
\end{aligned}
\tag{13}
$$

Put `r=sqrt(2)-1` and `z=sqrt(1-y)`. In the notation above,
`w=y cos^2(theta+alpha)`, so

$$
1-w=z^2+y\sin^2(\theta+\alpha)
\le z^2+(v+z)^2=v^2+2vz+2z^2,
\qquad E-1=2v^2+z^2.
$$

The middle estimate follows explicitly from
`sqrt(y) sin(theta+alpha)=vy+u sqrt(y)z<=v+z`.
Consequently

$$
\begin{aligned}
(E-1)-r(1-w)
&\ge(2-r)v^2-2rvz+(1-2r)z^2\\
&\ge0.
\end{aligned}
\tag{14}
$$

The quadratic form is positive definite: its diagonal entries are
positive and its determinant is

$$
(2-r)(1-2r)-r^2=3-7r=10-7\sqrt2>0,
$$

where the final sign follows from `100>98`. Since `D>=E` and
`W>=w`, equation (14) makes the excess in (13) nonpositive.
This proves (3) in every case.

## 6. Equality and the original operational optimum

The strict cases in Sections 2 and 4 cannot attain (3). In the
remaining case, equality in (14) forces `v=z=0`, hence `t=sqrt(k)`
and `T=1/2`. The identity and local X/Z coefficients then exhaust
`Tr(S^2)=1`, so S has no other Pauli coefficients. Equation (9)
forces `c=1`. In the dominant branch this means only the selected
site has a nonzero coefficient. It follows that

$$
S=\frac{I+B_i}{\sqrt{2d}},\qquad
B_i=xX_i+zZ_i,\qquad x^2+z^2=1.
$$

Equality in the two-query Cauchy--Schwarz step in (13) requires
`x^2=z^2=1/2`. Conversely these choices attain both (3) and the
original fidelity score. Thus the complete set of maximizing normalized
Gram states is

$$
\boxed{\rho=|\beta\rangle\langle\beta|_i\otimes
\frac{I_{\mathrm{rest}}}{2^{n-1}},}
\tag{15}
$$

where i is any original input site and beta is an X/Z bisector, with
either sign of each Bloch component and zero Y component. Every
maximizer is flat on a `2^(n-1)`-dimensional support; flatness was a
conclusion, not a hypothesis. A normalized Kraus seed with this Gram
matrix is determined up to its output unitary. This classifies normalized
seeds, not every possible classical organization of an instrument.

The score of (15) is `2n-2+sqrt(2)`: all `2n-2` queries on the retained
sites have value one, and the two discarded-site queries have value
`1/sqrt(2)`. Together with the fidelity comparison in Section 1 and
the exact normalized-seed reduction, this proves (1).

Operationally, retain `n-1` sites, perform the standard four-outcome
joint X/Z measurement of contrast `1/sqrt(2)` on the discarded site,
and randomize the choice of discarded site. The existing seed twirl,
or this direct randomized construction, makes the contrast uniform and
attains (2). The quantum dimension is always
`2^(n-1)`.
The converse applies to arbitrary collective encoding and arbitrary
allowed readouts, so it also gives
`||sum_i(X_i tensor B_i+Z_i tensor D_i)||<=2n-2+sqrt(2)` for all
`2n` Hermitian contractions on that memory. No claim is made that the failed
one-mode spectral envelopes become valid; this proof bypasses them.

## 7. Proof provenance and verification scope

The fidelity--affinity comparison and Hermitian trace rearrangement
are standard ingredients. The local Pauli decomposition and the
four-sign mean are elementary. The earlier
[flat half-rank theorem](../FLAT_HALF_RANK_OPTIMALITY.md) used a
related sign-mean argument for projectors. Here (9) keeps spectral
nonuniformity through the centered top-half eigenvalues, and (14)
absorbs it by a single positive quadratic. This supplies the unrestricted
half-rank conclusion through four inputs without a numerical parameter scan or a
classification of decoder orientations.

Independent readers reconstructed the integrated argument, including
the positive-half spectral normalization, four-sign branches, centered
rank constraint, tangent estimates, equality cases and operational
translation. Reproduce the accompanying targeted checks from the
repository root with

```bash
python tools/check_half_rank_retention.py --output results/half_rank_retention.json
```

The [checker](../../tools/check_half_rank_retention.py) verifies exact
rational scalar comparisons and floating-point matrix identities for
13 fixed constructions at n=2,3,4. These include equality, nonflat,
rank-deficient, complex, zero-local-mass and four-active-site cases.
The [result record](../../results/half_rank_retention.json) stores
`source_sha256` and `proof_note_sha256`, tying the checks to their source
and this note. They are finite diagnostics, not parameter scans, interval
certificates or optimization proofs. Repeated runs are expected to
reproduce the same record for the same files and runtime environment;
floating-point residuals may differ across environments.

These checks supplement the analytical proof and do not establish
publication novelty. A targeted theorem-level literature comparison
remains necessary before claiming originality. The bound on the
nonlargest-coordinate sign-mean branches
used here is specific to at most four coefficients; no all-n extension
is inferred. The general all-n finite-budget problem and asymptotic
rate evaluation remain separate questions.
