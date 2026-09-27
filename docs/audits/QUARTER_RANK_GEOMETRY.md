# Quarter-rank geometry and the flat-seed retention converse

Research base: `ecdfc7d6ad3ee16e66ba6f6de8802974bb558ee2` (PR #51).
Status: supplied analytical proofs, independently reconstructed within this
workspace. This is internal mathematical review, not external peer review or
a publication-priority assessment.

For four input qubits and memory dimension four, every flat seed obeys the
retention bound `4+2sqrt(2)`. Equality requires two pure local X/Z bisectors
and two maximally mixed retained sites. Every seed of rank at most three
also obeys a strict bound, without a flat-spectrum assumption. The remaining
finite case consists of nonflat rank-four seeds.

The proof extends the [half-rank argument](HALF_RANK_RETENTION_CONVERSE.md)
by keeping the top quarter of the singleton Pauli spectrum. It also proves
the sharp squared-score budget six for all rank-at-most-four seeds and two
local deficit inequalities. All statements concern the original seed problem;
no product structure, pinching, or restriction on collective encoders is
imposed on the arbitrary-spectrum results.

## 1. Exact top-quarter spectrum

Let S be positive on four qubits, with `Tr(S^2)=1` and `rank(S)<=4`.
Write

$$
u=\frac{\mathrm{Tr}S}{2}\le1,\qquad v=\sqrt{1-u^2}.
$$

Use the orthonormal Pauli basis `sigma/4`. Rotate each local X/Z plane so
that the singleton part of S is

$$
L=\frac{aB_1+bB_2+cB_3+dB_4}{4},\qquad
a\ge b\ge c\ge d\ge0,\qquad
T=a^2+b^2+c^2+d^2=\mathrm{Tr}(SL).
$$

The B_i are unit local X/Z directions. Sorting their lengths only relabels
the original sites. Put

$$
R=\max\left\{b,\frac{b+c+d}{2}\right\}.
$$

The four greatest eigenvalues of L, multiplied by four, are

$$
a+b+c+d,\quad a+b+c-d,\quad a+b-c+d,\quad a+|b-c-d|.
$$

For the fourth entry, only `a+b-c-d` and `a-b+c+d` can compete; every
first-negative sign sum is bounded by the latter because `a>=b`.
Their mean and centered squared sum are exactly

$$
\mu=\frac{a+R}{4},\qquad
\sum_{j=1}^4(\lambda_j(L)-\mu)^2=\frac{T-a^2-R^2}{4}.
\qquad\text{(1)}
$$

Indeed their uncentered square sum is `(T+2ab)/4` when `b>=c+d`,
and `(T+a(b+c+d))/4` otherwise. This also covers every tie.

Apply Hermitian trace rearrangement to the four eigenvalues of S, padded
by zeros, then centered Cauchy--Schwarz. Equation (1) gives

$$
\boxed{2T\le u(a+R)+v\sqrt{T-a^2-R^2}.}
\qquad\text{(2)}
$$

Here `R^2<=b^2+c^2+d^2`. Cauchy--Schwarz on the three coordinates
`a,R,sqrt(T-a^2-R^2)` consequently implies

$$
\boxed{T\le\frac{1+u^2}{4}.}
\qquad\text{(3)}
$$

When T=0 this is immediate; otherwise divide
`2T<=sqrt(T)sqrt(2u^2+v^2)` by `sqrt(T)`.

## 2. The sharp affinity and squared-score budgets

For the eight local queries A define

$$
a_A=\mathrm{Tr}(SASA),\qquad F_A=\|SAS\|_1.
$$

The established fidelity--affinity comparison gives `F_A^2<=a_A`;
see [the sourced proof](../STRONG_ENTROPIC_CONVERSE.md#3-root-fidelity-affinity-and-the-two-pauli-energy).
The Pauli-conjugation sum has eigenvalue eight on the identity, six on
singleton X/Z words, and at most four on all other Pauli words. The identity
coefficient is u/2. Equations (2)--(3) therefore prove

$$
\boxed{\sum_A F_A^2\le\sum_A a_A
\le4+u^2+2T\le\frac92+\frac32u^2\le6.}
\qquad\text{(4)}
$$

Both maxima are exactly six. Equality in the affinity budget forces
`u=1,T=1/2`, and equality in (2)--(3) forces `a=R=1/2` and
`T=a^2+R^2`. The branch `R=(b+c+d)/2` cannot satisfy
`R^2=b^2+c^2+d^2` at positive R, since the squared sum of three numbers is
at most three times their sum of squares. Thus `b=1/2,c=d=0`.

The trace equality u=1 makes `S=P/2` for a rank-four projector P.
Trace-rearrangement equality then puts P on the top eigenspace of
`L=(B_1+B_2)/8`, exactly the joint +1 eigenspace of B_1 and B_2. Hence
the complete equality family is

$$
\boxed{\rho=S^2=|\beta_1\rangle\langle\beta_1|\otimes
|\beta_2\rangle\langle\beta_2|\otimes\frac{I_4}{4},}
\qquad\text{(5)}
$$

up to original-site permutations. The two pure states have arbitrary unit
Bloch directions in their local X/Z planes. Conversely every state (5)
attains both squared budgets term by term: each pure site's two squared
scores sum to one, and each retained site's two scores equal one. Equality
in the original squared-score budget must also attain the affinity budget,
so it has exactly the same family.

If `rank(S)<=3`, then `u^2<=3/4`. Cauchy--Schwarz and (4) give the strict
arbitrary-spectrum exclusion

$$
\sum_A F_A\le\sum_A\sqrt{a_A}\le\sqrt{45}<4+2\sqrt2.
\qquad\text{(6)}
$$

For general rank four, (4) alone gives `sqrt(48)`, which exceeds the
retention value. Its equality classification does not close that gap.

## 3. Two local rank and spectral bounds

The following statements hold in any dimension `d_0=2^n`. Let S be positive,
`Tr(S^2)=1`, `rank(S)<=r`, and `kappa=||S||`. In normalized Pauli coordinates
put `b_i=sqrt(s_Xi^2+s_Zi^2)` and define

$$
W_i=2-\mathrm{Tr}(SX_iSX_i)-\mathrm{Tr}(SZ_iSZ_i).
$$

Then

$$
\boxed{W_i\ge\frac{d_0}{r}b_i^2,\qquad
W_i\ge1-\kappa\bigl(\mathrm{Tr}S-\sqrt{d_0}\,b_i\bigr).}
\qquad\text{(7)}
$$

An orthogonal rotation of the X/Z plane preserves both b_i and W_i:
on expanding the two affinities, the mixed coefficients cancel and each
squared column sums to one. Choose the rotated Z axis along the singleton
bias and write

$$
S=\begin{pmatrix}A&C\\C^*&D\end{pmatrix},\qquad
\mathrm{Tr}(A-D)=\sqrt{d_0}\,b_i\ge0.
$$

The positive blocks A,D have rank at most r and satisfy `A<=kappa I`.
Direct expansion gives the two equivalent identities

$$
\begin{aligned}
W_i&=\|A-D\|_2^2+6\|C\|_2^2-2\mathrm{Re}\mathrm{Tr}(C^2)\\
&=1-2\mathrm{Tr}(AD)+4\|C\|_2^2
       -2\mathrm{Re}\mathrm{Tr}(C^2).
\end{aligned}
\qquad\text{(8)}
$$

Since `Re Tr(C^2)<=||C||_2^2`, the first line is at least `||A-D||_2^2`.
The positive inertia of A-D is at most `rank(A)<=r`; consequently

$$
\mathrm{Tr}(A-D)\le\mathrm{Tr}(A-D)_+
\le\sqrt r\,\|(A-D)_+\|_2\le\sqrt r\,\|A-D\|_2.
$$

This proves the first bound in (7). The second line of (8) is at least
`1-2Tr(AD)>=1-2kappa Tr(D)`, which proves the second bound.

The first bound has explicit equality cases. If b_i>0, equality forces
`C=0` and A-D to be a positive flat rank-r matrix. Since then
`rank(A)+rank(D)<=r`, it forces `D=0,A=P/sqrt(r)` with P a rank-r
projector. Thus `S=|beta><beta|_i tensor P/sqrt(r)`, with beta a pure
X/Z direction. Such cases exist when `r<=d_0/2`. If b_i=0, equality is
equivalent to `C=0,A=D`, or `S=I_i tensor A` with the stated normalization
and rank bound.

## 4. Every flat quarter-rank seed obeys the retention bound

It remains to consider a flat rank-four seed, since (6) covers all lower
ranks. Now `S=P/2`, so `u=1,kappa=1/2`. Positivity gives every singleton
length at most `Tr(S)/4=1/2`, while (7) becomes

$$
W_i\ge2b_i.
\qquad\text{(9)}
$$

Write `y=2T`, `s=a+b+c+d`, and `D_0=sum_i W_i`. Equation (4) gives
`D_0>=3-y`.

First suppose `R=b`. Put `p=a+b<=1`. Equation (2) gives `y<=p`, and
(9) gives `W:=W_1+W_2>=2p`. Apply Cauchy--Schwarz to the four queries
on these two sites and the other four, then tangent bounds at `W=2`
and `D_0-W=0`. With `r_0=sqrt(2)-1`,

$$
\sum_A\sqrt{a_A}\le4+2\sqrt2+
\frac{r_0(2-W)-(D_0-2)}2.
$$

Its excess numerator is at most

$$
2r_0(1-p)-(1-y)\le(2r_0-1)(1-p)\le0.
\qquad\text{(10)}
$$

Second suppose `R=(b+c+d)/2`. Equation (2) gives `y<=(a+s)/2`.
Since `a<=1/2`, (9) implies

$$
D_0\ge2s\ge4y-1,\qquad D_0\ge3-y,
\qquad D_0\ge\frac{11}{5}.
$$

Thus this branch has the strict bound

$$
\sum_A\sqrt{a_A}\le\sqrt{\frac{232}{5}}<4+2\sqrt2,
\qquad\text{(11)}
$$

where the last comparison uses `sqrt(2)>7/5`. Either branch may handle a
tie. Equations (6), (10)--(11) prove the flat-seed theorem.

Equality in the root-sum bound requires p=y=1 and `D_0=2`, hence equality
in (4). The family (5) therefore contains every maximizer. Its root-sum, and its original score,
equal `4+|x_1|+|z_1|+|x_2|+|z_2|`. They attain `4+2sqrt(2)` exactly
when both pure sites are X/Z bisectors. This classifies normalized seeds,
up to output isometries, and does not assert uniqueness of instruments.

## 5. Verification and remaining scope

Independent readers reconstructed the top-four ordering and both variances,
rank-deficient trace inequality, local block and inertia bounds, flat-seed
branches, and all equality cases. Reproduce the targeted checks with

```bash
python tools/check_quarter_rank_geometry.py --output results/quarter_rank_geometry.json
```

Finite fixed checks supplement these proofs; they do not certify an
unrestricted optimum or publication originality. Standard trace
rearrangement and the sourced fidelity--affinity comparison are prior
ingredients; the supplied rank and deficit argument has not received an
exhaustive theorem-level novelty audit.

The unrestricted target `Gamma(4,4)=4+2sqrt(2)` remains open for nonflat
rank-four seeds. The squared budget gives the valid upper bound
`Gamma(4,4)<=4sqrt(3)`. More precisely, Cauchy--Schwarz and (4) give
`sum_A F_A<=sqrt(36+12u^2)`, so a possible violation must satisfy

$$
u^2>\frac{4\sqrt2-3}{3},\qquad u=\frac{\mathrm{Tr}\sqrt\rho}{2}.
\qquad\text{(12)}
$$

No marginal-rank tensorization is assumed: a global
rank cap does not impose the needed rank caps on two-site marginals.
The original task still has one unknown specimen, one delayed local query,
arbitrary collective encoding, classical records of unrestricted finite size, and
worst-case quantum memory. The general entropy inequality and asymptotic
common-accuracy rate also remain open.
