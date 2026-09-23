# Sharp two-qubit subspace bounds and the flat-core entropy theorem

**Reviewed main:** `fa2443ca413a5c1935722db1c1415be0c7ad7266` (PR #22).
**Date:** 2026-09-23. **Branch:** `audit/sharp-subspace-bound`.

This continuation replaces a numerical tail subdivision by a common-subspace
inequality and one scalar polynomial majorant. Its entropy consequence is
simple: **every complex two-qubit state with equal largest two eigenvalues
satisfies the sharp seed entropy bound.** The unequal-core case and the
all-block-size conjecture remain open.

The operational contract is unchanged: one unknown specimen, one delayed
local query, unrestricted collective encoding, unlimited finite classical
records, worst-case quantum dimension, and uniform input/query error.
Projectors, pinching maps and spectral tails below are mathematical devices
for bounding normalized seeds, not restrictions or postselection in an
encoder. Here epsilon denotes spectral tail weight, not operational error.

| Statement | Verdict |
|---|---|
| Canonical form of arbitrary complex two-dimensional two-qubit subspaces | Established ingredient: Niu–Griffiths (1999), exact reference below |
| Exact minimum subspace coupling for each local-unitary orbit; universal constant 7/8 | Derived with proof; independently reconstructed within this workspace |
| Sharp relation between mean coupling and its state dependence, coefficient 2/sqrt(3) | Derived with proof and exact attainer; independently reconstructed |
| Sharp entropy inequality for every spectrum with lambda_1=lambda_2 | Derived using the new scalar proof and the previously proved high-score/tail gates |
| Unequal-core transfer, full two-qubit inequality, all-size subset optimality | Unresolved; a specific lost-coherence obstruction is stated below |
| Publication originality | Unresolved; the canonical machinery is explicitly prior, and the exact optimizations are not certified absent from prior work |

All eigenvalues are ordered decreasingly. Write

\[
g(\rho)=\sum_{U\in\{X_A,Z_A,X_B,Z_B\}}
 \|\sqrt\rho U\sqrt\rho\|_1,\qquad c_0=2-\sqrt2.
\]

The entropy target is `g(rho)<=2sqrt(2)+c_0 S(rho)`, with entropy in bits.
The historical [initial audit](PROOF_AND_NOVELTY_AUDIT.md) remains unchanged.

## 1. Sharp common-subspace inequalities

Let P be any complex rank-two projector on C^2 tensor C^2, Q=I-P, and

    H=sum_{U in {X_A,Z_A,X_B,Z_B}} QUPUQ, acting on Q.

Write the Pauli expansion of R=2P-I as

    R=a_vec.sigma tensor I+I tensor b_vec.sigma
        +sum T_ij sigma_i tensor sigma_j.

Let s1>=s2>=0 be the two possibly nonzero singular values of T, and put

    delta=(Tr_Q H)/2-1=I_XZ(P/2)-1.

Then the following exact statements hold:

1. H >= [1+s1^2+3s2^2-4s1s2] I_Q >= (7/8) I_Q.
   The first constant is the exact minimum over local orientations of the
   query frames for each fixed local-unitary orbit of P. The universal
   constant 7/8 is attained.

2. ||H-(1+delta)I_Q||_infinity <= (2/sqrt(3)) delta.
   The coefficient 2/sqrt(3) is optimal.

These are operator inequalities on the two-dimensional complement. They
are not statements of the full entropy-versus-readout theorem.

### 1.1 Common canonical calculation

From R^2=I, Pauli multiplication gives

    T b_vec=0, T^T a_vec=0, a_vec b_vec^T=cof(T),
    |a_vec|^2+|b_vec|^2+||T||_F^2=1.

Thus rank T<=2. Proper local rotations yield the canonical form

    R=a ZI+b IZ+c XX+d YY,
    a^2+b^2+c^2+d^2=1, ab=cd, |c|>=|d|.

For rank T=2 the local vectors lie in its one-dimensional left/right null
spaces. For rank T=1 at most one local vector is nonzero; its direction
can be placed along Z within the corresponding null plane. Rank T=0 is
a product support. Signed coefficients absorb any orientation signs, so
no real-state restriction has been introduced. Here |c|=s1, |d|=s2.

Let n_A,n_B be the excluded unit Pauli direction at each site in this
canonical basis. Define z=c^2+d^2 and

    d_A=a^2 n_A,z^2+c^2 n_A,x^2+d^2 n_A,y^2,
    d_B=b^2 n_B,z^2+c^2 n_B,x^2+d^2 n_B,y^2.

Direct Pauli expansion gives

    delta=z+d_A+d_B >=0.                                (1)

For a fully explicit compression calculation choose angles M,D with

    a=cos M cos D, b=-sin M sin D,
    c=sin M cos D, d=-cos M sin D.

The even and odd parity blocks of R are unit involutions with angles
M+D and M-D. Taking their negative eigenvectors as a basis of Q gives

    Q Z_A Q=-a I-b tau_z, Q Z_B Q=-b I-a tau_z,
    Q X_A Q=-sin M tau_x, Q Y_A Q=-sin D tau_y,
    Q X_B Q= cos D tau_x, Q Y_B Q=-cos M tau_y.           (2)

In particular the sign of the final Y_B formula is negative in this
common parity basis. The six-query cross-frame minus the two excluded
queries has the form

    H=(1+delta)I+w_A.tau+w_B.tau.                         (3)

For site A, set t=n_A,z^2 and h=c^2 n_A,x^2+d^2 n_A,y^2. Then

    |w_A|^2=4a^2[b^2(1-t)+t h], d_A=a^2t+h.              (4)

For example w_A=(2a sin M n_A,z n_A,x,
                 2a sin D n_A,z n_A,y,
                -2ab(1-n_A,z^2)).

The identity sin^2 M=b^2+c^2 and sin^2 D=b^2+d^2 proves (4).
The corresponding B formula exchanges a,b. These norm identities, not
individual coordinate signs, are all that the inequalities below need.

The canonical subspace reduction and compressed Pauli maps are
established ingredients; compare Niu--Griffiths, arXiv:quant-ph/9810008v2,
Sec. II.A, Eq. (2.5), and Sec. III, Eqs. (3.5)--(3.7). The new deductions
below require their own novelty comparison.

### 1.2 Exact bound from the correlation singular values

For either site write

    s=|cd|, r=d^2, k=2s-r,
    w=1-t, u=a^2t, h=c^2 n_x^2+d^2 n_y^2.

For site B use u=b^2t. Since |c|>=|d|, k>=s>=0, h>=r w,
and (4) becomes

    |w_A|^2=4(s^2 w+u h).

We claim

    |w_A|<=u+h+k=d_A+k.                                  (5)

Its squared difference is

    F(u)=(u+h+k)^2-4u h-4s^2w.

If h<=k, F is increasing for u>=0. At u=0,

    h+k>=r w+2s-r>=2s sqrt(w),

because 2s>=r(1+sqrt(w)). Thus F(0)>=0. If h>=k, the minimum
of F over u>=0 occurs at u=h-k and equals

    4kh-4s^2w>=4k^2-4s^2w>=0.

This proves (5), also when coefficients vanish. Applying it to both sites
and using (1)--(3),

    lambda_min(H)>=1+delta-d_A-d_B-2k
                  =1+c^2+3d^2-4|cd|.                    (6)

For fixed canonical a,b,c,d, choose both excluded directions along Y.
Then delta=c^2+3d^2, w_A=w_B=(0,0,-2ab), and

    spec_Q(H)={1+c^2+3d^2-4|cd|,
               1+c^2+3d^2+4|cd|}.

So (6) is attained for every admissible pair s1,s2.

Finally x=|c|+|d|<=1 since

    x^2=c^2+d^2+2|cd|<=c^2+d^2+a^2+b^2=1.

Writing y=|c|-|d| gives

    1+c^2+3d^2-4|cd|
       =1+2(y-x/4)^2-x^2/8 >=7/8.                       (7)

Equality is attained by

    a=b=sqrt(15)/8, c=5/8, d=3/8,
    R=a ZI+b IZ+c XX+d YY,

with the actual X/Z queries. This has delta=13/16 and H spectrum
{7/8,11/4}.

### 1.3 Sharp linear anisotropy bound

Divide the correlation weight evenly between sites:

    D_A=z/2+d_A, D_B=z/2+d_B, D_A+D_B=delta.

For site A put q=c^2, r=d^2, x=n_A,x, y=n_A,y,

    w=x^2+y^2=1-t, h=q x^2+r y^2, u=a^2t.

Equation (4) and ab=cd give

    |w_A|^2=4(qrw+u h), D_A=(q+r)/2+h+u.

But

    D_A^2-3(qrw+u h)
       =[(q+r)/2+h]^2-3qrw+u(q+r-h)+u^2 >=0,            (8)

because q+r>=h and

    (q+r)/2+h
       =[q(1+2x^2)+r(1+2y^2)]/2
       >=sqrt[qr(1+2x^2)(1+2y^2)]>=sqrt(3qrw).

The last inequality is exactly

    (1+2x^2)(1+2y^2)-3(x^2+y^2)
       =1-x^2-y^2+4x^2y^2 >=0.

Hence |w_A|<=2D_A/sqrt(3), and similarly for B. Therefore

    ||H-(1+delta)I||=|w_A+w_B|<=2delta/sqrt(3).           (9)

An exact attainer is

    a=c=sqrt(6)/4, b=d=sqrt(2)/4,
    R=a ZI+b IZ+c XX+d YY,

again with the actual X/Z queries. Here delta=3/4 and

    spec_Q(H)={7/4-sqrt(3)/2,7/4+sqrt(3)/2}.

Thus the coefficient 2/sqrt(3) in (9) is optimal. This attainer differs
from the universal 7/8 attainer because the two bounds optimize different
quantities.

### 1.4 Consequence for CS scalar moments

For a flat core P/2 and arbitrary normalized tail tau on Q, let t_j denote
the eight singular values of PUP across the four queries. Let theta_j be
the corresponding diagonal weights of tau in each query's complementary
CS basis. Then

    sum_j theta_j=4,
    sum_j t_j^2=6-2delta,
    sum_j theta_j(1-t_j^2)=Tr(tau H).

Writing L=2/sqrt(3), the upper half of (9) implies the scalar constraint

    sum_j[((1+L)/2)-theta_j]t_j^2<=3L.                   (10)

The universal 7/8 lower bound, combined with Tr H=2+2delta, separately
implies

    sum_j(1-theta_j)t_j^2<=25/8.                         (11)

The weaker consequence H>=(1-delta)I also gives

    sum_j(3/2-theta_j)t_j^2<=6.                          (12)

These statements are exact for complex supports and complex tails. They
supply compatibility between the four query-specific CS decompositions;
no common CS basis is being assumed.

## 2. Complete flat-core entropy theorem

Let rho=(1-epsilon)P/2+epsilon tau on two qubits, with P any complex rank-two orthogonal projector, Q=I-P, and tau any state supported on Q. If 0<=epsilon<=1/29 and g(P/2)<=10/3, then

    g(rho) <= 3277/960 + (595/192) epsilon
           <= 2sqrt(2)+(2-sqrt(2))[1-epsilon+h_2(epsilon)]
           <= 2sqrt(2)+(2-sqrt(2))S(rho).

No spectral assumption on tau is made. Combining this result with the [high-score-core theorem](TWO_QUBIT_CORE_STABILITY.md) and
[spectral-tail gate](TWO_QUBIT_SPECTRAL_TAIL_GATE.md) proves the desired entropy inequality for every two-qubit state whose two largest eigenvalues are equal. Pure/rank-two and zero-tail endpoints are included by continuity or their existing theorem. This does not prove the nonflat-core case or the all-block-size conjecture.

### 2.1 Exact one-query CS/pinching bound

For U one of the four query Pauli operators, its block form relative to P,Q satisfies U=U^dagger and U^2=I. The CS decomposition pairs the two core coordinates with two tail coordinates, with core compression eigenvalues of magnitudes t_1,t_2 in [0,1]. If theta_j are the diagonal entries of tau in this complementary basis, then theta_1+theta_2=1.

Pinch by simultaneous signs on the two paired coordinates. This pinching commutes with U and preserves the flat core. Joint concavity of root fidelity, or its monotonicity under the pinching channel, gives

    ||sqrt(rho) U sqrt(rho)||_1
       <= sum_j sqrt[(a-epsilon theta_j)^2 t_j^2+4a epsilon theta_j],
    a=(1-epsilon)/2.

The right side follows from the two-dimensional identity F_root(A,UAU)^2=Tr(AUAU)+2det(A), with A=diag(a,epsilon theta). Coordinates with t=1 cause no difficulty: they decouple and contribute a+epsilon theta.

Write t_j,theta_j for all eight query indices, and T=sum t_j^2, W=sum theta_j t_j^2. Then

    sum t_j = 2g(P/2) <=20/3,
    T<=6,
    sum theta_j=4.

For delta=3-T/2, the trace identity Tr_Q H_P=2+2delta and H_P >=(1-delta)Q imply H_P <=(1+3delta)Q. Consequently

    4-W=Tr(tau H_P)<=1+3delta,
    W >= (3/2)T-6.                                    (A)

### 2.2 A single scalar majorant

For 0<=t<=1 and 0<=y<=1/14, define

    c=7/20, r=7/8, D=299/80, E=45/16,
    phi(t)=t+c(t-r)^2,
    psi(t)=D-E t^2.

Then

    sqrt[(1-y)^2 t^2+4y] <= phi(t)+y psi(t).             (B)

Here phi>=0 and psi>=37/40>0, so squaring preserves the inequality. Put

    Q0=phi^2-t^2,
    Q1=2phi psi+2t^2-4,
    Q2=psi^2-t^2,
    B1=Q0+Q1/28,
    B2=Q0+Q1/14+Q2/196.

The squared difference has the identity, with s=14y in [0,1],

    Q0+y Q1+y^2 Q2 = (1-s)^2 Q0+2s(1-s)B1+s^2 B2.

Each coefficient polynomial is nonnegative on [0,1]. First,

    Q0=c(t-r)^2[2t+c(t-r)^2]>=0.

Define the standard Bernstein basis b_{k,d}(t)=binom(d,k)t^k(1-t)^(d-k). Direct rational polynomial multiplication gives

    B1 = sum_{k=0}^4 p_k b_{k,4}(t) / 34406400,
    p=(16797,2692965,2208145,225921,205461),

and

    B2 = (1-t) sum_{k=0}^3 q_k b_{k,3}(t) / 240844800
         +(2743/11468800)t^4,
    q=(105747,33423588,55698550,61633548).

All nine listed integers are positive. These are exact identities, not interval estimates, sampled checks, or numerical optimization evidence. They prove (B) on the whole rectangle without case splitting.

### 2.3 Sum the majorant

Since epsilon<=1/29, y=epsilon theta/a<=1/14. Applying (B) to every query index gives

    g(rho)<=a sum phi(t_j)+epsilon sum theta_j psi(t_j).

Write phi=A+B t+c t^2, where A=cr^2 and B=1-2cr>0. From (A),

    g(rho)<=a(8A+B sum t_j)+(ac-3epsilon E/2)T
              +epsilon(4D+6E).

The coefficient ac-3epsilon E/2 is positive throughout epsilon in [0,1/29]; its minimum is (14c-3E/2)/29=(109/160)/29>0. Using sum t_j<=20/3 and T<=6 therefore gives

    g(rho)<=(1-epsilon)U+epsilon(4D-3E),
    U=4A+(10/3)B+3c=3277/960,
    4D-3E=521/80.

Thus g(rho)<=3277/960+(595/192)epsilon, as claimed.

### 2.4 Compare with entropy using only endpoint arithmetic

S(rho)=h_2(epsilon)+(1-epsilon)+epsilon S(tau), so the minimum entropy at a fixed epsilon is 1-epsilon+h_2(epsilon). The entropy target is concave in epsilon. It suffices to compare our affine upper bound at epsilon=0 and epsilon=1/29.

At zero, 3277/960<2+140/99<2+sqrt(2), since 140^2<2*99^2.

At epsilon=1/29, use the exact elementary bounds

    log_2(29)>34/7, since 29^7=17249876309>2^34=17179869184;
    1/ln(2)>10/7, since exp(7/10)>sum_{j=0}^4(7/10)^j/j!
                                  =482921/240000>2;
    -ln(1-x)>=x+x^2/2 for 0<=x<1;
    sqrt(2)>140/99.

Let x=1/29 and

    h_low=(34/7)x+(10/7)(1-x)(x+x^2/2),
    K=1-x+h_low.

Here K=201690/170723<2, so the entropy target at x is at least
2K+(2-K)(140/99). Direct rational arithmetic gives

    2K+(2-K)(140/99)-[3277/960+(595/192)x]
        =151/23312520>0.

Concavity finishes the comparison for every epsilon between the endpoints.


## 3. The remaining bottleneck, in one inequality

The newly excluded face is `lambda_1=lambda_2`, not a license to uniformize
an arbitrary core. Let

    epsilon=lambda_3+lambda_4, q=1-epsilon,
    m=lambda_2/q, sigma=(lambda_1|v_1><v_1|+lambda_2|v_2><v_2|)/q,
    G(m)=sqrt(2)+sqrt[4-2(1-2m)^2], Gamma=2+sqrt(2).

One sufficient next lemma would be

\[
\boxed{g(\rho)\le qG(m)+\epsilon\Gamma+3\epsilon,
       \qquad 0\le\epsilon\le1/29.} \tag{C}
\]

**Equation (C) is a conjectural sufficient bound, not a proved result.**
A proof would close every remaining **two-qubit** case without further
tail cutoffs.

Indeed put `d(m)=2sqrt(2)+c_0 h_2(m)-G(m)>=0`, as proved in the
[rank-two spectral theorem](../ENTROPY_INEQUALITY_BOUNDARIES.md).
Orthogonal core/tail decomposition and `S(tau)>=0` would give

    2sqrt(2)+c_0 S(rho)-g(rho)
        >=q d(m)+c_0 h_2(epsilon)-(3+c_0)epsilon.

For positive epsilon at most 1/29, `h_2(epsilon)/epsilon` is decreasing,
and at the right endpoint it exceeds

    34/7+280/203=1266/203>31/5>
        4+(3/2)sqrt(2)=(3+c_0)/c_0.

Here use `29^7>2^34`, `ln(29/28)>1/29`, `ln(2)<7/10`, and
`sqrt(2)<10/7`. This would prove a strict entropy margin. Together with
the existing tail gate, it would settle n=2; it would not prove every n.

The precise obstruction to reusing Section 2 is within-core coherence.
For a nonflat sigma, query-specific CS pinching need not preserve its
zero-tail score. Even take the already entropy-valid product example

    P=I_A tensor |beta><beta|,
    sigma=rho_A tensor |beta><beta|,

where beta and rho_A's Bloch direction are both X/Z bisectors and rho_A
has eigenvalues 7/10,3/10. The actual core score is

    g(sigma)=sqrt(2)+2sqrt(23)/5<10/3.

Pinching separately in each active query's eigenbasis raises its score
to 1, so the total pinched score is `2+sqrt(2)>10/3`. Thus the moment cap
used in Section 2 cannot be carried over using only the actual core score.
This example refutes that transfer step, not the entropy conjecture.
A successful proof must control the four trace norms jointly while keeping
this coherence loss; scalar spectral bounds alone have not supplied it.

Combining proved exclusions, any two-qubit entropy witness must now have

    2^-20<epsilon<1/29,
    1/5<m<1/2,
    g(sigma)<=10/3,

in addition to all previously documented eigenbasis and kernel conditions.
No such witness has been established.

## 4. Primary-source comparison and novelty boundary

Niu and Griffiths, *Two-qubit copying machine for economical quantum
eavesdropping*, [arXiv:quant-ph/9810008v2](https://arxiv.org/abs/quant-ph/9810008v2),
29 April 1999, contains the exact prior structural reduction: the unnumbered
theorem in Section II.A, Eq. (2.5), printed p. 4, gives a canonical basis
for every complex two-dimensional subspace; Eq. (2.10), p. 5, includes
arbitrary local and input unitaries. Equations (3.5)–(3.7), p. 6, give its
compressed local Pauli maps. The current HTML renders these as Eqs. (5),
(10), and (17)–(19). Appendix A supplies the canonical-form proof.

The source's isometry V onto Q maps a local Pauli to `V^dagger U V`, which
is exactly the compression used here. The input/output naming and harmless
basis signs do not change that identity. Rotating to the canonical support
also rotates both query planes; it does not justify fixing their orientation.
We explicitly retain the two excluded directions n_A,n_B. The inspected
canonical and Bloch-map statements therefore supply the coordinates but do
not themselves state the all-plane minimization in Section 1.2 or the sharp
mean-versus-state-dependence bound in Section 1.3. Those evaluations have
separate supplied proofs here; their exhaustive originality remains open.

The universal 7/8 inequality has a narrow operational interpretation:
a state in any two-dimensional subspace leaves it with probability at least
7/32 under a uniformly selected member of the four X/Z errors. This is
escape before recovery, not a bound on recovered logical error or on
interface memory by itself. The entropy consequence additionally requires
fidelity pinching, the common-frame moment relation, the scalar majorant,
and the previously proved gates.

This is a useful sharp supporting theorem and an entropy-family closure.
It does not settle the publication status of the project's full two-parameter
formation profile, nor establish unrestricted equal-accuracy optimality.
The [profile comparison](PROFILE_NOVELTY_AND_STEERING_REDUCTION.md) and
[publication assessment](PUBLICATION_AND_OPTIMALITY_ASSESSMENT.md) retain
those separate open questions.

## 5. Verification and scope of evidence

The canonical compression, both sharp operator inequalities and their
attainers, and the CS/pinching reduction were independently reconstructed
by another agent in this workspace. The final scalar identities and entropy
comparison were separately checked. This is internal mathematical review,
not external peer review.

Run the standard-library exact checker:

```sh
python tools/check_two_qubit_flat_core.py
python -O tools/check_two_qubit_flat_core.py
```

It multiplies rational polynomials, verifies the positive Bernstein
expansions and coefficient signs, and checks the rational entropy endpoint
margin `151/23312520`. The normal and optimized Python 3.12.14 runs give identical output;
the recorded output is [two_qubit_flat_core_check.json](../../results/two_qubit_flat_core_check.json).
There is no interval partition, matrix scan, eigensolver or numerical
acceptance tolerance. The displayed proof supplies the reductions that the
checker does not certify. A small scalar optimization helped discover the
majorant; it is not used as evidence. Its auxiliary fractions are not
claimed optimal.

All 175 local file links in the changed Markdown documents resolve, and
`git diff --check` passes. The protected LICENSE and initial audit are unchanged. Main was checked
before branching; no open PR duplicated this work. The report is pinned
to the reviewed commit above, rather than describing future main as reviewed.
