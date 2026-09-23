# Coherent core transfer: exact obstructions and one sufficient target

Reviewed main: `fab95daf5e1f9a7d42ef778e3494330fa8e1c73f` (PR #23).
Date: 2026-09-23. This continues, without replacing, the
[initial audit](PROOF_AND_NOVELTY_AUDIT.md) and
[flat-core theorem](SHARP_SUBSPACE_AND_FLAT_CORE.md).

**Outcome:** a two-line matrix bound preserves unequal-core coherence;
one exact physical example refutes three stronger proposed intermediates.
Keeping the tail's actual entropy permits a larger gain relative to its
actual score. The new target remains unproved. No additional state family
is excluded here, and neither unrestricted optimality nor publication
originality is established.

## 1. Setting and evidence labels

For two input qubits, write

    g(rho)=sum_{U=X_A,Z_A,X_B,Z_B} ||sqrt(rho) U sqrt(rho)||_1,
    c=2-sqrt(2), Delta(rho)=2sqrt(2)+c S(rho)-g(rho),

with entropy in bits. Let P be the top-two spectral support, Q=I-P, and

    rho=q sigma direct-sum epsilon tau, q=1-epsilon,
    spec(sigma)=(1-m,m), 0<m<=1/2.

Both sigma and tau are normalized. The tail may have rank one. All support
bases and eigenvectors may be complex. Define the proved rank-two envelope

    G(m)=sqrt(2)+sqrt[4-2(1-2m)^2],
    delta_m=2sqrt(2)+c h_2(m)-G(m)>=0.

The [rank-two theorem](../ENTROPY_INEQUALITY_BOUNDARIES.md) also gives
`g(tau)<=2sqrt(2)+c S(tau)`. Existing exclusions reduce any remaining
two-qubit witness to

    2^-20<epsilon<1/29, 1/5<m<1/2, g(sigma)<=10/3.

These are proof coordinates for the original problem: one unknown specimen,
one delayed local query, unrestricted collective encoding, unlimited finite
classical records, worst-case quantum dimension and uniform error over every
input and query. No operational projection onto P or postselection is used.
Even a complete n=2 entropy proof would not establish the all-n conjecture.

| Statement below | Status |
|---|---|
| Coherent block bound (1) | Elementary trace-norm consequence; supplied proof |
| Retaining the tail entropy in (3) | Exact bookkeeping plus the proved rank-two bound |
| Three quadratic shortcuts in Section 4 | Incorrect; one exact counterexample |
| Finite support-function inequality (4) | Unproved sufficient target |
| Conditional margin from (4) | Derived and independently checked |
| Numerical screening | Local falsification attempt only |
| Publication originality | Unresolved; the matrix inequality is not proposed as new |

## 2. Keep coherence with a two-line block bound

For any Hermitian block matrix, including singular and complex blocks,

\[
\left\|\begin{pmatrix}A&B\\B^\dagger&D\end{pmatrix}\right\|_1
\leq \operatorname{Tr}\sqrt{A^2+4BB^\dagger}+\|D\|_1. \tag{1}
\]

Indeed set `N=[[A/2,B],[0,0]]`. The matrix on the left is
`N+N^dagger+diag(0,D)`. The triangle inequality gives
`2||N||_1+||D||_1`, exactly the right side of (1).

For one query define maps in the P,Q support bases,

    L_U=sqrt(sigma) PUP sqrt(sigma),
    X_U=sqrt(sigma) PUQ sqrt(tau),
    T_U=sqrt(tau) QUQ sqrt(tau).

The query matrix is `[[q L_U,sqrt(q epsilon) X_U],
[sqrt(q epsilon) X_U^dagger,epsilon T_U]]`. Thus

\[
g(\rho)\leq\epsilon g(\tau)+q\sum_U
\operatorname{Tr}\sqrt{L_U^2+(4\epsilon/q)X_UX_U^\dagger}. \tag{2}
\]

At zero tail, the sum is exactly `g(sigma)`. No pinching of sigma, inverse
compression, or replacement of its eigenvalues by 1/2 occurs. In particular,
singular query compressions cause no divergence in (2). The obstacle is now
bounding the **joint four-query sum**; four independently optimized terms
discard the compatibility of their common physical support.

## 3. One bounded-parameter target is enough

Suppose a bound of the form

    g(rho)<=q G(m)+epsilon g(tau)+K(epsilon)

is available. The exact orthogonal-mixture entropy identity gives

\[
\Delta(\rho)\geq q\delta_m+c h_2(\epsilon)-K(\epsilon). \tag{3}
\]

This keeps the tail entropy and score paired. Using `g(tau)<=2+sqrt(2)`
while independently replacing `S(tau)` by zero loses `c epsilon` of slack.
For example, a gain bound `K<=7 epsilon/2` already suffices on the remaining
tail range. The older formulation in the flat-core report used coefficient
3 with a fixed worst-case tail score; the two right sides are not pointwise
ordered for every tail. The improvement is the gain budget relative to
the tail's actual score.

The following finite support-function inequality would suffice:

\[
\boxed{\mathcal S_t(\sigma,\tau):=
\sum_U\left\|\begin{pmatrix}
L_U&(t/2)X_U\\(t/2)X_U^\dagger&0
\end{pmatrix}\right\|_1
\leq G(m)+\frac38\bigl(1-\sqrt{1-4t^2}\bigr).} \tag{4}
\]

**Equation (4) is unproved.** Its sufficient domain is
`0<=t<=1/sqrt(7)`, `1/5<=m<=1/2`, arbitrary orthogonal rank-two supports
and arbitrary normalized tail. A proof restricted further to
`g(sigma)<=10/3` would also suffice by the existing high-score-core gate.

To verify the implication, put `t=2sqrt(epsilon/q)` and split off the
tail diagonal block by the trace-norm triangle inequality. Equation (4)
would give

    g(rho)<=q G(m)+epsilon g(tau)+K(epsilon),
    K(epsilon)=3q[1-sqrt(1-16epsilon/q)]/8
              =6epsilon/[1+sqrt(1-16epsilon/q)].

For `0<epsilon<=1/29`, this has

    K(epsilon)/epsilon<=6/[1+sqrt(3/7)]<40/11,

since `sqrt(3/7)>13/20`. Also `h_2(epsilon)/epsilon` is decreasing, and

    h_2(1/29)/(1/29)>34/7+280/203=1266/203,
    c>41/70,
    (41/70)(1266/203)>73/20.

The logarithmic bounds use `29^7>2^34`, `ln(29/28)>1/29` and
`ln(2)<7/10`; the latter follows from the first five positive terms of
`exp(7/10)>2`. The bound on c uses `sqrt(2)<99/70`.
Consequently (4) would prove the strict margin

\[
\Delta(\rho)>q\delta_m+\frac{3}{220}\epsilon. \tag{5}
\]

Together with the existing spectral gates, this would settle n=2. This
conditional conclusion is not entered as a proved entropy theorem.

### Why a stronger global quadratic is unnecessary

Let arbitrary Hermitian decoder contractions have blocks
`D_U=[[A_U,B_U],[B_U^dagger,C_U]]`, and put

    a=sum_U Tr(L_U A_U),
    b=|sum_U Tr(X_U B_U^dagger)|, d=G(m)-a>=0.

Trace-norm duality gives `S_t=max_D(a+t Re sum Tr(X_U B_U^dagger))`.
The factor t/2 in (4) is essential: the two off-diagonal traces together
produce t, not 2t. A common phase on the tail sector permits optimizing
the absolute value b.

The global relation `b^2<=3d+4d^2` would imply (4), by maximizing
`-d+t sqrt(3d+4d^2)` over `d>=0`. The maximum is
`(3/8)[1-sqrt(1-4t^2)]`. But (4) is only needed on its stated finite t
interval; proving the global quadratic over all decoder deficits is a
stronger obligation. Neither statement has been proved here.

## 4. One exact physical obstruction to three shortcuts

In the two-qubit computational basis define four orthonormal vectors

    e1=(00+11)/sqrt(2), e2=(01-10)/sqrt(2),
    e3=(00+01+10-11)/2, v=(00-01-10-11)/2.

Put `u=(e2+e3)/sqrt(2)`.

Take `sigma=(3/4)|u><u|+(1/4)|e1><e1|` and `tau=|v><v|`.
Use the core memory coordinates 0,1 and tail coordinate 2. The unused
fourth memory coordinate, if included, can have decoder value +1.
Let `w=(1,2,-2)/3`, `D=-I+2ww^T`, and use the reflections

    D_XA=D,
    D_ZA=-S D S,    S=diag(1,-1,-1),
    D_XB=-S' D S',  S'=diag(1,-1,1),
    D_ZB=S'' D S'', S''=diag(1,1,-1).

In physical coordinates `(u,e1,v)`, the X_A compression is

    [[-1/sqrt(2), 1/2,          -1/2],
     [1/2,        0,          -1/sqrt(2)],
     [-1/2,      -1/sqrt(2),    0]].

The other query compressions have exactly the same signed conjugations
as their decoders. Direct multiplication in the definitions above yields

    a=7sqrt(2)/6+4sqrt(3)/9,
    b=[4sqrt(3)+8sqrt(2)]/9,
    d=sqrt(14)/2-sqrt(2)/6-4sqrt(3)/9.

Here `b>2` and `0<=d<87/100`. These follow, for instance, from
`sqrt(3)>173/100`, `sqrt(2)>141/100`, and `sqrt(14)<749/200`.
Using `sqrt(2)<283/200` gives

    3d<261/100<4<b^2,
    2sqrt(2)d+2d^2<39759/10000<4<b^2.

Thus all three proposals

    b^2<=3d,
    b^2<=2sqrt(2)d+d^2,
    b^2<=2sqrt(2)d+2d^2

are false, already at `m=1/4` in the remaining core range. As a separate
exact check, the residual of the coefficient-2 proposal is

    [-442+112sqrt(6)-108sqrt(7)+72sqrt(42)]/81 >22/405.

For the final inequality use `sqrt(6)>12/5`, `sqrt(7)<8/3`,
`sqrt(42)>97/15`, each verified by squaring positive numbers.
This example refutes only proposed intermediates. Its core expectation
is well below G(m); it supplies no entropy violation or better interface.

## 5. Primary-source comparison and the novelty boundary

Holevo and Shirokov, *Log-Sobolev inequality, von Neumann entropy and
Entanglement of Formation*, [arXiv:2609.12667v1](https://arxiv.org/abs/2609.12667v1),
11 September 2026, Proposition 1, Eqs. (14)–(15), printed p. 6, gives
`S(P/d)-S(sigma)<=K_d[1-F(P/d,sigma)]`, with natural-log entropy and
**squared** root fidelity, and `K_2=2`. The same-support rank-two case,
whose proof is the first paragraph on p. 6, becomes exactly

    1-h_2(m)<=[1-2sqrt(m(1-m))]/ln(2).

Only that same-support case is used in this comparison. It is an
established scalar entropy estimate, not a joint Pauli score bound.
It controls the entropy lost upon moving away from a flat core, but supplies
no lower bound on the accompanying score loss. Hence it does not by itself
transfer the flat-core theorem or prove (4). Equation (1), separately, is
an elementary norm inequality and is not proposed as a novel theorem.

Neither of these ingredients evaluates the full two-parameter steering
formation profile. The [profile comparison](PROFILE_NOVELTY_AND_STEERING_REDUCTION.md)
and [publication assessment](PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md)
remain the relevant targeted comparisons. This continuation supplies no
exhaustive originality conclusion and no new theorem claimed to meet a
publication threshold.

## 6. Verification and reproducibility

The block inequality, decoder normalization, physical counterexample and
conditional entropy implication were independently reconstructed by other
agents within this workspace. This is internal checking, not external review.
The [exact checker](../../tools/check_coherent_transfer.py) verifies the
physical matrix identities and rational certificates; it does not certify (4).
Run `python tools/check_coherent_transfer.py` or
`python -O tools/check_coherent_transfer.py` from the repository root.
Both Python 3.12.14 runs produce the same
[recorded output](../../results/coherent_transfer_check.json), using only
standard-library rational and multiquadratic arithmetic.

A bounded local falsification check tested (4) at `t=1/sqrt(7)` for
`m=.2,.25,.3,.4,.5`, pure and flat tails, product supports and complex
perturbations of the obstruction support. Twenty local exact-support-function
optimizations and two row-bound optimizations found no violating point;
the largest observed gap was about `-0.03186054`. One optimization reported
precision loss. These observations are discovery notes, not a continuum
certificate, and are not used in any displayed proof. No large simulation
was performed.

Main and open PRs were checked before branching; none duplicated this work.
All local Markdown links in the changed documents resolve, and
`git diff --check` passes. LICENSE and the historical initial audit are
preserved. The preceding
flat-core theorem remains unchanged. The next substantive task is a proof
or counterexample for (4), retaining the four queries' common support.
