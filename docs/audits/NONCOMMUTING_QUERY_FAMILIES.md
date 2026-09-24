# Noncommuting query families: two finite converse theorems

**Reviewed main:** `e8fffa3ccac4b03b354d354101e20302fc934616`,
the merge of PR #38. **Date:** 2026-09-24.
**Status:** supplied analytic deductions, independently reconstructed
inside the audit workspace; not external peer review or a priority claim.
The historical [proof and novelty audit](PROOF_AND_NOVELTY_AUDIT.md)
is preserved.

Two continuous families with genuinely noncommuting query algebras now
obey the three-input/two-qubit-memory retention benchmark. Neither
result assumes a flat seed or a product encoder.

- The sharp inequality `P_1+P_2+P_3<=5I/2` holds when the three
  memory subsystems are obtained by arbitrary independent partial
  SWAPs of two memory qubits. Equality forces two subsystem choices
  to coincide and the third to be complementary. Its physical-score
  consequence also assumes equal spectra within each site's two
  Jordan blocks.
- Two sharp internally anticommuting query pairs require only the
  two mixed cross commutators to vanish. Their same-axis cross
  commutators may both be nonzero; the third binary query pair is
  unrestricted.

The first proof reduces five qubits to a two-dimensional positive
matrix. The second preserves a maximally entangled top eigenvector
under a two-parameter memory interaction. These are finite-family
converses. They close no complete remaining reflection signature and
do not evaluate unrestricted `Gamma(3,4)`.

## 1. Exact continuous-family statement

Let Q=A tensor B consist of two qubits and S be their SWAP. On each
reference qubit R_i and Q, define

$$
P_i=e^{i\theta_i S}
  (|\mathrm{singlet}\rangle\langle\mathrm{singlet}|_{R_iA}
   \otimes I_B)e^{-i\theta_i S}.
$$

All reference spectator identities are implicit. The three real angles
are arbitrary and independent. Then

$$
\boxed{P_1+P_2+P_3\le \frac52 I.}
$$

The constant is attained when two angles are zero and the third is pi/2:
the two coincident A-subsystem Bell edges have norm 3/2, and the independent
B-subsystem edge has norm one.

A common unitary on Q and arbitrary independent unitaries on the three
references preserve the theorem. Thus using singlets instead of standard
Bell states is immaterial. Generic angle choices give query algebras
that are pairwise noncommuting. This proves a continuous family inside
the unresolved geometry, not the general independent-U(4) conjecture.

## 2. Reduction by total spin

Each singlet projector and S commutes with the simultaneous SU(2)
rotation of all five qubits. Consequently the sum splits into total
spins 5/2, 3/2, and 1/2, with multiplicities one, four, and five.
The spin representation factors are spectators.

For the memory, split A B into its triplet and singlet spaces. S is
+1 on the former and -1 on the latter. Thus conjugating a projector
by exp(i theta_i S) preserves its two diagonal blocks and multiplies
its upper-right off-diagonal block by

$$z_i=e^{2i\theta_i}.$$

The all-symmetric total-spin-5/2 space has zero singlet projection and
therefore contributes eigenvalue zero.

The two remaining multiplicity matrices are given explicitly below.
Their diagonal blocks can also be obtained from

$$
K_{\mathrm{triplet}}=\frac34 I-\frac12 J_R\cdot J_{AB},
\qquad K_{\mathrm{singlet}}=\frac34 I.
$$

Here K denotes the full sum, J_R is the total spin of the three
references, and J_AB is the memory triplet spin.

## 3. Spin 3/2: a stronger bound of two

Order the triplet-memory multiplicities first: the reference spin 3/2
copy, then its two spin 1/2 copies. Put the reference-spin-3/2 times
memory-singlet copy last. The matrix is

$$
K_{3/2}=
\begin{pmatrix}
\operatorname{diag}(5/4,1/2,1/2)&m\\
m^\dagger&3/4
\end{pmatrix},
$$

where, in consistent reference bases,

$$
m=
\begin{pmatrix}
-\sqrt{5/48}(z_1+z_2+z_3)\\
(-z_1+z_2)/4\\
(-z_1-z_2+2z_3)/(4\sqrt3)
\end{pmatrix}.
$$

Writing Z=z_1+z_2+z_3, direct orthogonal decomposition of
(z_1,z_2,z_3) gives

$$
|m_2|^2+|m_3|^2=\frac38-\frac{|Z|^2}{24}.
$$

The positive Schur-complement criterion for K_(3/2)<=2I is

$$
\frac43|m_1|^2+\frac23(|m_2|^2+|m_3|^2)\le\frac54.
$$

Its left side equals 1/4+|Z|^2/9, at most 5/4 since |Z|<=3.
Thus this entire sector is bounded by two.

## 4. Spin 1/2: the two-dimensional inequality

Order triplet-memory multiplicities as reference spins 3/2, 1/2, 1/2;
the two singlet-memory reference-spin-1/2 copies come last. Then

$$
K_{1/2}=
\begin{pmatrix}
\operatorname{diag}(2,5/4,5/4)&N\\
N^\dagger&(3/4)I_2
\end{pmatrix},
$$

with

$$
N=
\begin{pmatrix}
(z_1-z_2)/(2\sqrt2)&(z_1+z_2-2z_3)/(2\sqrt6)\\
\sqrt3 z_3/4&(-z_1+z_2)/4\\
(-z_1+z_2)/4&(2z_1+2z_2-z_3)/(4\sqrt3)
\end{pmatrix}.
$$

A common phase of the z_i only changes the relative basis phase of
the two diagonal sectors. Set z_3=1 and write

$$
z_1=e^{i(\alpha+\beta)},\quad z_2=e^{i(\alpha-\beta)},
\quad c=\cos\beta,\quad x=\cos\alpha.
$$

The Schur complement for K_(1/2)<=5I/2 says exactly that

$$
B=\frac74I_2-N^\dagger
       \operatorname{diag}(2,4/5,4/5)N\ge0.
$$

With s=z_1+z_2 and t=z_1-z_2, its entries are

$$
B_{11}=\frac{4+3|s|^2}{10},\qquad
B_{22}=\frac{12-|s|^2+4\operatorname{Re}s}{10},\qquad
B_{12}=-\frac{\sqrt3}{20}\,[\bar t(s-3)-t].
$$

In particular, B_11=2(1+3c^2)/5>0. Its determinant is

$$
\det B=\frac{F(c,x)}{25},
$$

$$
F(c,x)=9(1-c^2)x^2+2c(7+9c^2)x+c^2(41-9c^2).
$$

The simultaneous substitution (c,x)->(-c,-x) preserves F, so take
0<=c<=1 without loss of generality.

For 0<=c<=2/3, completing the square gives

$$
F(c,x)=9(1-c^2)
  \left[x+\frac{c(7+9c^2)}{9(1-c^2)}\right]^2
  +\frac{64c^2(5-9c^2)}{9(1-c^2)}\ge0.
$$

For 2/3<=c<=1, the derivative in x on [-1,1] is bounded below by

$$
\partial_x F(c,-1)
=2(9c^3+9c^2+7c-9)\ge\frac{14}{3}>0.
$$

Thus

$$
F(c,x)\ge F(c,-1)
=(1-c)(9c^3+27c^2-5c+9)\ge0,
$$

where the cubic is positive: 9c^3+27c^2>=0 and 9-5c>=4.
Both pieces include their endpoints; c=1 uses the second case, so
no vanishing denominator is inverted. The Schur complement has only
the fixed positive denominators 1/2, 5/4 and 7/4.
Since B_11>0 and det B>=0, B is positive semidefinite. This proves
K_(1/2)<=5I/2 and completes the theorem.

The same proof identifies equality in the projector norm. In the first
positivity range, F can vanish only at c=0,x=0; in the second, only at
c=1,x=-1. Including the simultaneous sign symmetry and restoring the
common phase, this says precisely that the three z_i occupy two opposite
phase values, both used. Equivalently, the three memory subalgebras are
assigned to two complementary factors, with two queries on one factor
and the remaining query on the other. Every other partial-SWAP angle
triple has projector-sum norm strictly less than 5/2. There is no
uniform positive gap over triples approaching the equality set.

## 5. Reconstructing the displayed matrices

Here is a fully specified basis for checking the Clebsch coefficients.
Use |0> as spin-up. On R_1 R_2 R_3 set

$$
t_{3/2}=|000\rangle,\quad
t_{1/2}=(|001\rangle+|010\rangle+|100\rangle)/\sqrt3,\quad
t_{-1/2}=(|011\rangle+|101\rangle+|110\rangle)/\sqrt3,
$$

$$
a_+=(|010\rangle-|100\rangle)/\sqrt2,\quad
a_-=(|011\rangle-|101\rangle)/\sqrt2,
$$

$$
b_+=(2|001\rangle-|010\rangle-|100\rangle)/\sqrt6,\quad
b_-=(|011\rangle+|101\rangle-2|110\rangle)/\sqrt6.
$$

On A B write w_+=|00>, w_0=(|01>+|10>)/sqrt(2), w_-=|11>,
and w_s=(|01>-|10>)/sqrt(2).
For highest-weight total spin 1/2 the five basis vectors are

$$
v_1=t_{3/2}w_-/\sqrt2-t_{1/2}w_0/\sqrt3
       +t_{-1/2}w_+/\sqrt6,
$$

$$
v_2=\sqrt{2/3}\,a_-w_+-a_+w_0/\sqrt3,\quad
v_3=\sqrt{2/3}\,b_-w_+-b_+w_0/\sqrt3,\quad
v_4=a_+w_s,\quad v_5=b_+w_s.
$$

For highest-weight total spin 3/2 the four basis vectors are

$$
w_1=\sqrt{3/5}\,t_{3/2}w_0-\sqrt{2/5}\,t_{1/2}w_+,\quad
w_2=a_+w_+,\quad w_3=b_+w_+,\quad w_4=t_{3/2}w_s.
$$

Each unrotated projector is (I-SWAP_(R_i,A))/2. These real,
orthonormal highest-weight vectors give the matrices in Sections 3–4
by direct inner products. Global SU(2) invariance supplies the other
magnetic quantum numbers with identical multiplicity matrices.
The five-qubit dimension check is 6*1+4*4+2*5=32.

The exact-arithmetic verifier `tools/check_partial_swap_basis.py` checks
these highest-weight bases and coefficient matrices. The separate
NumPy diagnostic reconstructs the full physical operators. The proof
of the continuous angle dependence and determinant positivity is the
analytic argument above.

## 6. Consequence for equal-within-pair spectra

Suppose each original site's two Jordan blocks have equal nonnegative
spectra u_i,v_i, with u_i^2+v_i^2=4 and
2>=u_i>=sqrt(2)>=v_i>=0. Assume their combined top Bell subspaces
admit the partial-SWAP geometry above. The local exact spectral cap is

$$
h_i\le v_i I+(u_i-v_i)P_i.
$$

For any unit test vector put p_i=<P_i>. The theorem gives
0<=p_i<=1 and sum p_i<=5/2. Maximizing a linear functional on
this polytope assigns unit weight to the two largest u_i-v_i and
weight 1/2 to the remaining one. Therefore, for the corresponding
ordering,

$$
\sum_i\langle h_i\rangle
\le u_{(1)}+u_{(2)}+\frac{u_{(3)}+v_{(3)}}2
\le4+\sqrt2.
$$

Conjugating all references by Y gives the full operator norm bound.
This permits arbitrary unequal spectra between sites, but equal
spectra within each site's two Jordan blocks. The factor geometry
is an additional stated condition and is not imposed on the original
unrestricted encoder model.

The projector constant 5/2 is sharp. This does not establish sharpness
of the induced physical bound 4+sqrt(2) within the balanced equal-block
readout family: equality of the positive spectral caps is an additional
condition, and no corresponding attainment is asserted here.


## 7. Two mixed cross commutators suffice

On four-dimensional Q let B1,D1,B2,D2 be Hermitian reflections with

    {B1,D1}={B2,D2}=0,     [B1,D2]=[D1,B2]=0.

No assumption is made on [B1,B2] or [D1,D2]. B3,D3 are arbitrary Hermitian
contractions. For three different trusted reference qubits,

    ||sum_i (Xi Bi + Zi Di)|| <= 4+sqrt(2).

The two corresponding-axis cross commutators may both be nonzero. Internal sharp anticommutation remains
an essential hypothesis of this proof. No encoder/seed restriction is used.

### 7.1. Complete algebraic classification in dimension four

The first sharp anticommuting pair identifies Q=A tensor B, both qubits,
with B1=XA, D1=ZA. This is the standard two-dimensional representation
of two anticommuting reflections, with multiplicity two.

Put Jx=B1 B2 and Jz=D1 D2. The two mixed cross commutations and the two
internal anticommutations give [Jx,Jz]=0: moving B2 across D1 has no sign,
while moving B1 past D1 and B2 past D2 contributes two minus signs.
Both Jx,Jz are unitaries. Commuting normal operators commute also with
one another's adjoints. Thus the four Hermitian parts

    A=(Jx+Jx†)/2, E=(Jx-Jx†)/(2i),
    C=(Jz+Jz†)/2, F=(Jz-Jz†)/(2i)

commute pairwise, and A²+E²=C²+F²=I.

Conjugation by B1 sends Jx to Jx†, while conjugation by D1 sends Jx
to -Jx. Similarly D1 sends Jz to Jz†, while B1 sends Jz to -Jz.
The Pauli decomposition on A therefore has exactly the forms

    A=XA tensor a, E=YA tensor e,
    C=ZA tensor c, F=YA tensor f,

for Hermitian 2-by-2 a,e,c,f. Pairwise commutation and the two square
identities become

    {a,c}={a,e}={a,f}={c,e}={c,f}=0, [e,f]=0,
    a²+e²=c²+f²=I.                                      (1)

These relations force a and c to be traceless. Indeed, if a anticommutes
with v, cyclicity gives Tr(av²)=Tr(vav)=-Tr(av²)=0; hence
Tr a=Tr[a(c²+f²)]=0. Similarly Tr c=Tr[c(a²+e²)]=0.

Suppose first that at least one of a,c is nonzero. A nonzero traceless
2-by-2 Hermitian matrix has opposite nonzero eigenvalues; every Hermitian
matrix anticommuting with it is traceless. Thus e,f are traceless too.
For traceless 2-by-2 matrices anticommutation means perpendicular Bloch
vectors and commutation means parallel Bloch vectors. Relations (1)
therefore permit a memory-B basis with

    a=A0 XB, c=C0 ZB, e=E0 YB, f=F0 YB,
    A0,C0>=0, A0²+E0²=C0²+F0²=1.                        (2)

If a or c vanishes, the unused axis is chosen to complete this frame;
the square identities supply a nonzero e or f when needed. If e=f=0,
the nonzero orthogonal a,c fix the frame. These cover all zero cases.

Since B2=B1 Jx and D2=D1 Jz, (2) gives

    B2=A0 XB-E0 ZA YB,   D2=C0 ZB+F0 XA YB.              (3)

Choose alpha,gamma in [-pi/4,pi/4] by

    A0=cos(2gamma), E0=sin(2gamma),
    C0=cos(2alpha), F0=sin(2alpha).

The complete nonexceptional normal form is therefore

    B2=U XB U†, D2=U ZB U†,
    U=exp[i(alpha XA XB+gamma ZA ZB)].                    (4)

The two terms in U's exponent commute.

The remaining case is a=c=0. Then e,f are commuting qubit reflections.
Diagonalize them together. On each of the two memory lines of B,

    B2=-e ZA, D2=f XA,   e,f in {+1,-1}.                 (5)

Thus H0=h1+h2 is a direct sum of two one-memory-qubit operators. A local
rotation/sign choice on R2 turns each into

    (X1+X2) XA + (Z1+Z2) ZA.

Rotating the Z axes to Y gives the three-qubit XY star. In its
one-excitation and two-excitation sectors the matrix is a three-vertex
star with two edge weights 2, with eigenvalues +2sqrt(2),0,-2sqrt(2).
The zero- and three-excitation sectors have eigenvalue zero. Therefore
||H0||=2sqrt(2), and ||H0+h3||<=2sqrt(2)+2<4+sqrt(2).
This exceptional representation is fully controlled and need not be
forced into (4).

### 7.2. Exact spectrum in the two-angle form

Assume (4), put V=U^(1/2), and use the orthonormal operator-Bell basis

    |V sigma>>/2,

where sigma runs over the 16 two-qubit Pauli matrices and vectorization
uses the trusted computational basis. Transposes of the trusted X and Z
are unchanged, so a term Pi tensor M acts as M V sigma Pi.

For each sigma define signs epsilon_A,epsilon_B,zeta_A,zeta_B through
its commutation with XA,XB,ZA,ZB. The four signs independently label
these 16 Pauli matrices. The X-pair terms act by

    V[(epsilon_A+epsilon_B) cos(gamma) I
       + i(epsilon_B-epsilon_A) sin(gamma) ZA ZB] sigma, (6)

and the Z-pair terms act by

    V[(zeta_A+zeta_B) cos(alpha) I
       + i(zeta_B-zeta_A) sin(alpha) XA XB] sigma.       (7)

These expressions follow from
XA V XA=V exp(-i gamma ZA ZB),
U XB U† V XB=V exp(+i gamma ZA ZB),
and the corresponding Z identities with alpha XA XB.

Let p=epsilon_A epsilon_B and q=zeta_A zeta_B. Multiplication by ZA ZB
flips both epsilon signs and preserves both zeta signs; multiplication
by XA XB does the converse. Thus (6) and (7) preserve p,q and commute.
Each joint (p,q) sector is four dimensional. When p=+1, the X part has
eigenvalues +/-2cos(gamma); when p=-1 it has eigenvalues
+/-2sin(gamma). Likewise the Z part has eigenvalues +/-2cos(alpha)
or +/-2sin(alpha) according as q=+1 or -1. To check multiplicities without choosing phases for this basis, write these
two commuting restrictions as T_X,T_Z. They square to their respective
scalar squared eigenvalues. Inside each sector,

    Tr T_X=Tr T_Z=Tr(T_X T_Z)=0.

Indeed each restriction is either diagonal in its residual sign or flips
only that sign. A flip gives zero diagonal. If both are diagonal, the
product trace is proportional to the sum of epsilon_A zeta_A over four
independent sign choices, which vanishes. For nonzero scalar magnitudes
k_X,k_Z, the joint projector
(I+s T_X/k_X)(I+t T_Z/k_Z)/4 therefore has trace one for every s,t=+/-1.
Thus all four eigenvalue sums occur once. Zero magnitudes follow by
continuity (and give the corresponding degeneracies).

Consequently the full 16 eigenvalues of H0 are the Cartesian sums
of the two four-entry lists

    {+2cos(alpha), -2cos(alpha), +2sin(alpha), -2sin(alpha)}
    {+2cos(gamma), -2cos(gamma), +2sin(gamma), -2sin(gamma)}. (8)

Signed angles make no difference to these multisets. Define

    u1=2cos(alpha), v1=2|sin(alpha)|,
    u2=2cos(gamma), v2=2|sin(gamma)|,
    U0=u1+u2, c=min(u1-v1,u2-v2), m=U0-c.

Here 2>=ui>=sqrt(2)>=vi>=0 and ui²+vi²=4.
At c>0 the top eigenvalue U0 is unique. Its vector is

    Omega=|V>>/2,                                      (9)

because sigma=I in (6),(7) gives the eigenvalue
2cos(gamma)+2cos(alpha). Since V is unitary, Omega is maximally
entangled across R1R2:Q. The next eigenvalue is exactly m, giving

    H0 <= m I + c |Omega><Omega|.                      (10)

At c=0, one ui equals sqrt(2), so ||H0||=U0<=2+sqrt(2) and the
triangle inequality with ||h3||<=2 proves the theorem.

### 7.3. Full third-query resolvent

At c>0 select the index attaining c. Put u=min(u1,u2),
v=sqrt(4-u²); monotonicity of u-sqrt(4-u²) implies c=u-v.
Then m=U0-u+v<=2+v. Thus, with r=sqrt(2),

    4+r-m >= t0=2+r-v > 2.

The existing full-resolvent argument now applies word for word:
with P=|Omega><Omega| tensor I_R3, it is enough to show
cP+h3<=t0 I. Because Omega is maximally entangled, the positive
rank-update criterion reduces this to

    (c/4) Tr_Q[(t0 I-h3)^(-1)] <= I_R3.                 (11)

Separate convexity reduces B3,D3 to reflections. Every 2D traceless
Jordan block contributes at most

    A(t)=t/(t²-4)+1/t

to the partial trace, and each scalar block at most 1/(t-r).
The two sufficient normalized scalar bounds are

    c/(t0-r)<=1,    c A(t0)/2<=1.

They follow from c<=2-v=t0-r and c<=2(r-v)=2(t0-2), exactly as in
[the separate-query report](COMMUTING_QUERY_ALGEBRAS.md). All-reference Y conjugation gives the
other spectral half. This proves the stated operator norm bound.

### 7.4. Scope

Both unassumed cross commutators may be nonzero. In (3),

    [B1,B2]=2i sin(2gamma) YA YB,
    [D1,D2]=2i sin(2alpha) YA YB.

Their signs depend on the normal-form convention; their magnitudes do not.
No claim follows for arbitrary nonzero mixed cross commutators, arbitrary
internal Jordan angles, a full signature sector, or unrestricted optimality.
Separate attenuation of each of the first four reflections in [-1,1]
is allowed by convexity over sign choices, which preserve all hypotheses.


## 8. Transfer to the original operational model

Let `h_i=X_i B_i+Z_i D_i` on distinct reference qubits and a
four-dimensional memory. The pure-state variational identity is

\[
 \sum_i\operatorname{Tr}(B_i L X_iL^\dagger+D_i L Z_iL^\dagger)
 =\langle\!\langle L|H|L\rangle\!\rangle,\qquad \|L\|_F=1.
\]

Thus either applicable theorem bounds the **actual decoder score**
by `4+sqrt(2)` for every normalized complex seed. A full trace-norm
score is bounded by this argument only if a score-attaining family
of optimal readouts satisfies the stated hypotheses. It is not
legitimate to impose those hypotheses on an arbitrary optimum.

For a general collective instrument, refine the classical record to
a Kraus index `a`, discard zero Kraus operators, and set

\[
p_a=\|K_a\|_F^2/8,\qquad L_a=K_a/\|K_a\|_F,\qquad \sum_a p_a=1.
\]

If each branch's actual readouts are covered by either theorem, even
with branch-dependent memory coordinates and covered family, uniform
contrast `eta` implies

\[
6\eta\le\sum_a p_a s_a\le4+\sqrt2.
\]

This preserves one unknown specimen, one delayed original-site X/Z
query, arbitrary entangled inputs and collective encoding, unlimited
finite classical records, worst-case branch dimension four, and
uniform binary total-variation error `epsilon=(1-eta)/2`. No averaging
of memory cost, postselected success, or fresh copies is introduced.

The general normalized-seed reduction remains unchanged: achievability
requires a complete orbit instrument, not a seed used as a successful
postselection branch. The entropic and squashed-entanglement bounds
remain in force but are not strengthened by the present finite
decoder-family theorems.

## 9. Primary-source novelty comparison

The quantum random-access interpretation and entanglement-monogamy
strategy are established. The target needing proof is the joint
constraint on *different qubit subsystems of the same ququart*.

Sakharwade–Studziński–Eckstein–Horodecki, *Two instances of random
access code in the quantum regime*, NJP 25, 053038 (2023),
[2208.14422v3](https://arxiv.org/pdf/2208.14422v3), Section VI,
Eqs. (35)–(39), printed pp. 12–13, and Proposition 3 / Eq. (48),
p. 14, is close prior work: bounded shared entanglement and unlimited
classical communication. Its p. 13 larger-dimension reduction tests
a single embedded rank-one Bell projector after a unitary correction.
Our subsystem decoder tests `Phi tensor I_aux`, a rank-two projector.
Projecting onto one output subspace discards a positive contribution;
that reduction does not establish the needed bound.

An exact separator makes the distinction concrete. On
`rho=Phi_(R1,A) tensor Phi_(R2,B)`, the two subsystem decoders recover
their respective qubits with fidelities one. Either marginal
`rho_(Ri,Q)` has nonzero eigenvalues `1/2,1/2`; its overlap with
any normalized rank-one Bell projector is at most one half. This is
a difference between tested quantities, not a counterexample to the
source's rank-one-overlap statement. The ordinary one-common-qubit
monogamy theorem cannot be applied separately to incompatible
subsystem decoders.

Other inspected primary statements also do not supply the missing
general bound:

| Source and exact locator | Why the displayed result does not close this instance |
|---|---|
| Dupuis–Fawzi–Wehner, [1305.1316v3](https://arxiv.org/pdf/1305.1316v3), Theorem 9, printed p. 16 | The arbitrary-reference-state recovery bound assumes `n>d^2`; three qubits violate this hypothesis. |
| Dupuis–Fawzi–Renner, [1607.01796v2](https://arxiv.org/pdf/1607.01796v2), Definition 5.3 and Theorem 5.4 / Eq. (58), pp. 26–27 | Substituting three message qubits, two code qubits and one requested qubit gives `2^(3-1/225)>1`. This displayed fidelity bound is vacuous here, before addressing the free classical record. |
| Svegborn–Pauwels–Tavakoli, [2504.00162v2](https://arxiv.org/html/2504.00162v2), Section IV.2 / Figure 4, version 6 April 2026 | The nearby three/four-input, one/two-ebit cases are numerical lower bounds with two-bit communication, not a converse for unlimited classical records. |

Established ingredients used here are spin addition, Pauli algebra,
Schur complements, Jordan's lemma and maximally entangled resolvent
compression. The supplied deductions are the continuous partial-SWAP
bound and its equality classification, and the two-mixed-commutator
classification plus converse. This focused comparison establishes no
exhaustive originality or PRL-level significance.

## 10. Review outcome and remaining target

Independent internal reconstruction checked the exact spin bases and
all coefficients, the scalar positivity proof and equality cases,
the complete four-dimensional algebra classification, the Cartesian
spectrum, the top-vector marginal, and the arbitrary-third-query
resolvent. The finite construction checks are documented in
[REPRODUCIBILITY](../REPRODUCIBILITY.md); they supplement the supplied
proofs.

The general projector conjecture remains

\[
 \sum_{i=1}^3 U_i(\Phi_{R_iA}\otimes I_B)U_i^\dagger
 \stackrel{?}{\le}\frac52I
 \qquad\text{for independently arbitrary }U_i\in U(4).
\]

Proving it would remove the partial-SWAP geometry condition from
Section 6; unequal Jordan-block spectra would still require another
argument. The three unrestricted signatures `(22)^2(11)`,
`(22)^2(12)` and `(22)^3` remain open. General equal-accuracy
optimality, the complete entropy inequality, and publication
originality remain unresolved. There is no physical counterexample
in this report.
