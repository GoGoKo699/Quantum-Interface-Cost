# Conserved symmetries force a classical two-mode channel

Research base: main `eb88f82db5bfd4acd7b687ca209fc094fc5df2ea`.
Date: 27 September 2026.
Status: supplied analytical proof, independently reconstructed within this
workspace. This is internal review, not external peer review or a claim of
publication priority.

## The family and conclusion

On memory Q=A tensor B define the real symmetric Pauli subspaces

\[
\mathcal L_1=\operatorname{span}_{\mathbb R}\{X_A,Z_A,Y_AY_B\},\qquad
\mathcal L_2=\operatorname{span}_{\mathbb R}\{Z_B,X_AX_B,Z_AX_B\}.
\]

Let B1,D1 be arbitrary Hermitian contractions in L1 and B2,D2 arbitrary
Hermitian contractions in L2. Equivalently, each of the four coefficient
rows lies in a closed three-dimensional unit ball, since the three
generators in each subspace anticommute pairwise. Set

\[
H_0=X_1B_1+Z_1D_1+X_2B_2+Z_2D_2.
\]

Then, for **every** third pair of Hermitian contractions B3,D3 on Q,

\[
\boxed{\|H_0+X_3B_3+Z_3D_3\|\le5<4+\sqrt2.}
\]

Common memory-unitary conjugates of this family have the same conclusion.
The four reflection spheres form an eight-angle continuous subfamily; the
proof covers the balls, not just their sphere boundaries. The two-plane subfamily
`span{Z_A,X_A}`, `span{Z_B,Z_A X_B}` is included. The result does not
cover all ququart pairs of traceless reflections, and does not settle any
entire remaining reflection signature.

## 1. Two anticommuting symmetries force even eigenvalue multiplicity

In tensor order R1,R2,A,B define

\[
S_1=Y_1Y_AZ_B,\qquad S_2=Y_2Y_B,\qquad \Gamma=Y_1Y_2.
\]

Both S1,S2 are real symmetric reflections, they anticommute with each
other, and each commutes with H0. These assertions follow term by term
from the Pauli relations. Q1=Y_A Z_B anticommutes with all three first-site
memory generators and commutes with all three second-site generators.
Q2=Y_B has the reverse relations. Their accompanying reference Y factors
anticommute with both query axes at their own site. All six memory words
are real symmetric, including Y_A Y_B (two imaginary Pauli factors).

Every eigenspace of H0 is consequently an invariant representation of two
anticommuting reflections, so has even dimension. In particular its two
largest eigenvalues obey U=m. The [sharp two-mode support bound](SHARP_TWO_MODE_SUPPORT.md) gives

\[
U\le2\sqrt3.
\]

All matrices in H0 are real symmetric, and Gamma anticommutes with H0.
The [positive-eigenvalue square budget](TWO_MODE_RESOLVENT.md#1-a-universal-bound-on-the-third-eigenvalue) is at most 32.
If U>3, the positive U eigenspace cannot have dimension four:
that would contribute at least 4U^2>36>32 to this budget. Thus for U>3
its top eigenspace has exactly dimension two. This handles all possible
degeneracies needed below without a generic-angle assumption. For U<=3,
the triangle bound already proves the claimed bound of five.

The next eigenvalue ell also has even multiplicity, so the same square
budget gives the useful stronger spectral constraint

\[
\boxed{U^2+\ell^2\le16.}
\]

## 2. Every isolated positive rank-two eigenspace has an EB channel

This part applies to any positive eigenvalue with multiplicity exactly
two, not just the top eigenvalue. Let P be its projector and choose a real
isometry V from a head qubit onto its range. The restrictions of S1,S2 are
real symmetric anticommuting reflections; an orthogonal change of head
basis makes

\[
S_1V=VX_h,\qquad S_2V=VZ_h.
\]

The head channel is Phi(omega)=Tr_R(V omega V^*). Define

\[
Q_1=Y_AZ_B,\qquad Q_2=Y_B.
\]

Tracing out the reference factors of S1,S2 gives the exact covariance
relations

\[
\Phi(X_h\omega X_h)=Q_1\Phi(\omega)Q_1,\qquad
\Phi(Z_h\omega Z_h)=Q_2\Phi(\omega)Q_2.
\tag{A}
\]

### 2.1. The average output is flat

Phi(I) is real symmetric and commutes with Q1,Q2. Their joint commutant
has Pauli basis

\[
I,\quad Y_A,\quad X_AY_B,\quad Z_AY_B.
\]

All three nonidentity words are imaginary Hermitian matrices, hence have
zero coefficient in the real symmetric Phi(I). Since Phi preserves trace,

\[
\boxed{\Phi(I)=I_Q/2.}
\tag{B}
\]

### 2.2. The third head Pauli is killed

Because V is real, Phi(Y_h) is imaginary Hermitian. Covariance (A) says
that it anticommutes with both Q1,Q2. Of the six imaginary two-qubit Pauli
words, only Y_A X_B has both anticommutations. Hence Phi(Y_h)=cY_AX_B.

The signs in the following identity fix normalization explicitly:

\[
S_1S_2=-i\Gamma Y_AX_B,\qquad X_hZ_h=-iY_h,
\qquad VY_h=\Gamma Y_AX_BV.
\]

It follows that

\[
4c=\operatorname{Tr}[Y_AX_B\Phi(Y_h)]
=\operatorname{Tr}(P\Gamma)=0.
\]

The final equality uses positivity of the selected eigenvalue: Gamma
maps its eigenspace to the orthogonal negative eigenspace, so P Gamma P=0.
Thus

\[
\boxed{\Phi(Y_h)=0.}
\tag{C}
\]

### 2.3. Rank four forces the two remaining outputs to commute

Let J be the normalized Choi state of Phi. Its rank is at most four,
because V has reference environment dimension four. Equations (B),(C)
give

\[
J=\frac{I_8}{8}+\frac14\left[X_h\otimes\Phi(X_h)+
 Z_h\otimes\Phi(Z_h)\right].
\tag{D}
\]

Conjugating by Y_h changes J to I_8/4-J. Thus eigenvalues pair as
lambda,1/4-lambda. Positivity and rank at most four force exactly four
eigenvalues 1/4 and four zeros: equivalently

\[
J^2=J/4.
\]

Write M=Phi(X_h),N=Phi(Z_h). Substituting (D) into J^2=J/4 gives

\[
M^2+N^2=I_Q/4,\qquad [M,N]=0.
\tag{E}
\]

These commuting Hermitian matrices have a common orthonormal eigenbasis
{v_j}. Every output of Phi is diagonal in that basis by (B),(C). The
positive operators E_j=Phi^*(|v_j><v_j|) sum to I_h, and

\[
\Phi(\omega)=\sum_j\operatorname{Tr}(E_j\omega)
 |v_j\rangle\langle v_j|.
\]

This is an explicit measure-and-prepare representation, proving that Phi
is entanglement breaking. The argument invokes no PPT separability theorem.

The EB implication is also a corollary of established prior work:
Theorem 2 of M. Lewenstein, J. I. Cirac and S. Karnas,
[*Separability and entanglement in 2 x N composite quantum systems*](https://arxiv.org/abs/quant-ph/9903012)
(1999), proves separability when a state is invariant under partial
transpose on its qubit factor. Equation (C) makes J invariant in exactly
this way. That separability criterion is not a new result here. The
direct rank argument above additionally gives commuting outputs and
the orthogonal-record representation used below; the readout-symmetry
reduction and norm estimate are supplied separately in this note.

The channel has an explicit rectangular-POVM form. Covariance (A) flips
the signs of the joint eigenvalues (m,n) of M,N independently, while
(E) puts them on m^2+n^2=1/4. If both coordinates are nonzero, their
four-point orbit fills Q. If one coordinate is zero, the imaginary
reflection that fixes (m,n) preserves its real joint eigenspace, so this
eigenspace has dimension at least two: an imaginary Hermitian reflection
cannot act on a one-dimensional real space. The two-point orbit therefore
fills Q with multiplicity two. After permuting a real common eigenbasis,

\[
\boxed{\Phi(\omega)=\sum_{a,b=\pm1}
 \operatorname{Tr}(E_{ab}\omega)|ab\rangle\langle ab|,
\quad E_{ab}=\frac{I+a\alpha X_h+b\beta Z_h}{4},
\quad \alpha,\beta\ge0,\quad\alpha^2+\beta^2=1.}
\]

The endpoint cases have repeated effects. Operationally this is an equal
random choice between two projective axes, followed by an orthogonal
memory record. The square POVM from maximal support is the special case
alpha=beta=1/sqrt(2).

## 3. The full norm bound of five

If U<=3, chirality implies ||H0||=U and ||h3||<=2, so the conclusion is
the triangle inequality. Assume U>3. Sections 1--2 give an isolated
rank-two top eigenspace P and its actual EB head channel. The actual-tail
envelope is H0<=ell I+(U-ell)P, with

\[
3<U\le2\sqrt3,\qquad 0\le\ell\le r:=\sqrt{16-U^2}<\sqrt7.
\]

Set t=5-ell>5-sqrt(7)>2. The [two-mode Schur criterion](TWO_MODE_RESOLVENT.md#4-exact-four-by-four-schur-condition) and
[pure-memory last-query theorem](EXACT_LAST_QUERY_RESOLVENT.md#1-the-readout-elimination-theorem) give

\[
K_t\le(U-\ell)F(t)I,\qquad
F(t)=\begin{cases}
[2(\sqrt{2t^2-4}-t)]^{-1},&2<t\le3\sqrt2,\\
(t-\sqrt2)^{-1},&t\ge3\sqrt2.
\end{cases}
\]

Here only the EB measure-and-prepare representation is used to apply the
pure-memory bound; there is no approximation to the actual head channel.
If t>=3sqrt(2), the criterion follows strictly from U<=2sqrt(3)<5-sqrt(2).
The last strict comparison follows from 2sqrt(3)<7/2 and sqrt(2)<3/2.

On the other branch the desired strict inequality is equivalent to

\[
U+10-3\ell<2\sqrt{2(5-\ell)^2-4}.
\]

Its left side is positive because U>3 and ell<sqrt(7)<8/3. Squaring
therefore reduces it exactly to

\[
Q(U,\ell):=U^2+20U-84+(20-6U)\ell+\ell^2<0.
\]

For fixed U the quadratic is convex in ell. It suffices to bound the
endpoints ell=0 and ell=r. The first satisfies

\[
Q(U,0)\le40\sqrt3-72<0.
\]

At the second,

\[
Q(U,r)=20U-68+(20-6U)\sqrt{16-U^2}=:G(U).
\]

This function increases on [3,2sqrt(3)]. Its derivative is

\[
G'(U)=20-6r-(20-6U)U/r.
\]

For 3<=U<=10/3, use r<=sqrt(7)<8/3, r>=2, 20-6U<=2, U<=10/3:
G'(U)>20-16-10/3=2/3. For 10/3<=U<=2sqrt(3), the last displayed term is
nonnegative and G'(U)>20-16=4. Consequently

\[
Q(U,r)\le G(2\sqrt3)=16\sqrt3-28<0.
\]

The strict scalar comparisons use 4800<5184 and 768<784, respectively.
Both endpoints are strictly negative, proving K_t<I and hence
||H0+h3||<5 throughout the U>3 branch. Together with the triangle branch
this proves the universal bound five. The constant is a proved upper
bound; its attainment and optimality are not asserted.

No small stability radius, generic parameter assumption, or parameter
scan enters this proof. Chirality of H0+h3 converts the upper-eigenvalue
bound into the operator-norm bound.

## 4. Scope and weighted support boundary

The [weighted support construction](SHARP_TWO_MODE_SUPPORT.md#3-exact-support-for-arbitrary-query-weights)
uses complementary reflections

\[
F=(aX_1+bZ_1)Z_E+(cX_2+dZ_2)X_E,
\qquad a^2+b^2+c^2+d^2=1.
\]

Put r=sqrt(a^2+b^2), s=sqrt(c^2+d^2). When r,s>0, the same copying-basis
purification as in the balanced construction gives original-axis
correlation matrices

\[
\begin{aligned}
4C_{X_1}&=(aZ_A+bsX_A)/r,&4C_{Z_1}&=(bZ_A-asX_A)/r,\\
4C_{X_2}&=(cZ_B+drZ_AX_B)/s,&4C_{Z_2}&=(dZ_B-crZ_AX_B)/s.
\end{aligned}
\]

When these are nonzero, their polar signs belong to the two-plane
subfamily of Section 1 and are therefore covered by the norm bound five.
The r=0 or s=0 endpoints with all correlations nonzero follow by continuity:
aligned purifications have convergent memory-unitary subsequences, and
invertible Hermitian polar signs vary continuously. If a correlation is
zero, an arbitrary polar completion may leave the stated family; only
completions within it are included.

A weighted-support state need not be the leading eigenspace of the
unweighted Hamiltonian using its polar decoders. The proof above derives
the actual top channel directly, so does not require that identification.

The third pair can be arbitrary complex Hermitian contractions and need
not preserve either conserved symmetry. The real coefficient condition
applies to the four earlier readouts in the stated common memory basis.
All three complete remaining reflection signatures, the unrestricted
three-input converse and publication originality remain open. The constant
five is a sufficient upper bound, without an attainment or optimality claim.

The proof's ingredients are finite-dimensional symmetries, rank and
positivity, the established sharp two-mode support budget, and the exact
last-query resolvent formula. No parameter scan enters the universal bound.

Reproduce the targeted exact constants and fixed matrix identities with

```bash
python tools/check_head_structure_converses.py --output results/head_structure_converses.json
```

The checker records its source hash and this proof note's hash. Its fixed
examples supplement the analytical proof; they do not establish the result
by scanning readout parameters or certify publication novelty.
