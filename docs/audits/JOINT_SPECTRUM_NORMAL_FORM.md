# Joint spectral data: complete sharp-pair coordinates and a failed relaxation

**Research base:** `0f10c57dec2f54a4a8d7e9293f0a1a19bc99c1f1`, the merge of
PR #41. **Date:** 24 September 2026.

The [last-readout theorem](EXACT_LAST_QUERY_RESOLVENT.md) leaves a question
about the spectrum and actual top memory marginal of two earlier sharp
query pairs. This report supplies a complete seven-parameter representation
of those pairs, with an eight-dimensional singular-value formula for the
joint data. It covers every sharp-pair configuration, including boundary
cases, using established two-qubit Cartan decomposition.

A separate exact example proves that the known spectral inequalities,
the two-qubit SLD bound, a stronger six-Pauli bound, and even the known
exact fixed-spectrum score bound do **not** jointly imply the desired
resolvent certificate. The example has a strictly positive spectrum.
It supplies no actual Hamiltonian realizing that combination of data.

**Status:** derived and independently reconstructed internally. No
realizable failure of the rank-one strategy, new interface converse,
complete signature closure, or publication-originality claim is established.
The original one-specimen, one-delayed-query model is unchanged.

## 1. Complete normal form

Let Q have dimension four and let R1,R2 be qubits. For i=1,2 let B_i,D_i
be Hermitian reflections satisfying `{B_i,D_i}=0`. Put

\[
H_0=X_{R_1}\otimes B_1+Z_{R_1}\otimes D_1
    +X_{R_2}\otimes B_2+Z_{R_2}\otimes D_2.
\]

Spectator identities are implicit. Define memory qubits A,B only as a
coordinate identification of Q, and let

\[
V(\alpha)=\exp i(\alpha_x X_AX_B+\alpha_yY_AY_B+
                    \alpha_zZ_AZ_B),\qquad
P(n)=I_3-nn^{\mathsf T},\quad n\in S^2.
\]

Every H_0 is unitarily equivalent, by a common memory unitary and
independent reference unitaries, to

\[
\boxed{
\mathcal H(\alpha,n_1,n_2)=
\sum_{a,b=x,y,z}P(n_1)_{ab}\,\sigma_{R_1}^{a}\sigma_A^b
+
\sum_{a,b=x,y,z}P(n_2)_{ab}\,\sigma_{R_2}^{a}
 V(\alpha)(\sigma_A^b\otimes I_B)V(\alpha)^\dagger.
}
\tag{NF1}
\]

The domain

\[
(\alpha_x,\alpha_y,\alpha_z)\in[-\pi/2,\pi/2]^3,
\qquad n_1,n_2\in S^2
\tag{NF2}
\]

covers every case, including degenerate gates and coincident/complementary
memory subsystems. It has seven real parameters: three angles and two
sphere directions. It is intentionally redundant. In particular n and
-n give the same plane, and the angular boundary points can be identified.
No uniqueness or global smooth coordinate chart is asserted. Conversely,
every point of (NF2) describes two sharp pairs after independent changes
of reference frame.

The transformations preserve every eigenvalue of H_0. They also preserve
the spectrum of the actual memory marginal of a corresponding normalized
eigenvector, because they are local across `(R1 R2):Q`. Thus this is a
complete reduction of the joint data `(U,m,spec rho_Q)` used by the
last-query resolvent criterion, rather than a replacement of rho_Q by
unrelated spectral variables.

## 2. Coverage proof

Two anticommuting reflections generate the two-dimensional Pauli algebra.
In dimension four its representation has multiplicity two. A common
memory unitary therefore puts the first ordered pair at `(X_A,Z_A)`.
The second ordered pair has the form
`(U X_A U^dagger,U Z_A U^dagger)` for some U in U(4).
An overall phase of U has no effect.

The established two-qubit Cartan decomposition gives

\[
U=(a\otimes b)V(\alpha)(c\otimes d),
\tag{NF3}
\]

with a,b,c,d single-qubit unitaries. Conjugate the entire Hamiltonian on
memory by `(a tensor b)^dagger`. The first memory pair becomes
`(a^dagger X a,a^dagger Z a) tensor I`, while the second becomes
`V(c X c^dagger tensor I)V^dagger` and
`V(c Z c^dagger tensor I)V^dagger`. The factor d disappears because the
second reference pair initially acts only on A.

Next conjugate R1 by a^dagger and R2 by c. In each term, the two orthogonal
Bloch directions of the reference now equal the two pre-V memory Bloch
directions. Define n1,n2 by

\[
n_1\cdot\sigma=a^\dagger Y a,\qquad
n_2\cdot\sigma=cYc^\dagger.
\]

For any orthonormal frame `(u,n,v)` obtained by rotating `(x,y,z)`,
`u u^T+v v^T=I-nn^T`. Summing the X and Z terms therefore gives exactly
(NF1). Every sphere direction admits such an orthonormal frame, proving
the converse as well. Frame choices within a plane change only a local
reference basis.

Each individual Cartan angle can be reduced modulo pi because
`exp(i pi sigma_a tensor sigma_a)=-I_4`. This proves coverage by the
closed cube (NF2) without a genericity assumption or a special choice of
Weyl chamber. A complementary B subsystem is included, since SWAP is,
up to phase, `V(pi/4,pi/4,pi/4)`.

No physical factorization of the retained memory or restriction on an
encoder is imposed: A,B are coordinates after an allowed mathematical
unitary conjugation. The explicit restrictions are that the two earlier
pairs are sharp and internally anticommuting. Arbitrary reflection pairs
with unequal Jordan angles do not satisfy this hypothesis automatically.

## 3. Direct operator without matrix exponentials

Set `c_a=cos(2 alpha_a)` and `s_a=sin(2 alpha_a)`. For each cyclic
permutation `(a,b,c)` of `(x,y,z)`, put

\[
T_a=c_b c_c\,\sigma_a\otimes I
+s_b s_c\,I\otimes\sigma_a
+s_b c_c\,\sigma_c\otimes\sigma_b
-c_b s_c\,\sigma_b\otimes\sigma_c.
\tag{NF4}
\]

Then `T_a=V(sigma_a tensor I)V^dagger`. For example,

\[
T_x=c_yc_z XI+s_ys_z IX+s_yc_z ZY-c_ys_z YZ.
\]

This follows by two applications of
`e^(itP) Q e^(-itP)=cos(2t)Q+i sin(2t)PQ` when P,Q are anticommuting
Pauli products; the third Cartan generator commutes with the initial
operator. Substituting T_b in the second sum of (NF1) gives a polynomial
operator in the sphere coordinates and sine/cosine variables. Replacing
the latter by real variables constrained by `c_a^2+s_a^2=1` is an exact
algebraic representation, although it does not solve the universal
inequality over that domain.

## 4. Full spectrum and actual marginal from an eight-dimensional map

The normal form anticommutes with the reference-only involution

\[
\Gamma=(n_1\cdot\sigma_{R_1})(n_2\cdot\sigma_{R_2})\otimes I_Q.
\tag{NF5}
\]

Indeed, each reference vector selected by P(n_i) is perpendicular to n_i.
The projectors E_+=(I+Gamma)/2 and E_-=(I-Gamma)/2 have rank eight on the
full reference-memory space, and

\[
\mathcal H=\begin{pmatrix}0&C\\C^\dagger&0\end{pmatrix},
\qquad C=E_+\mathcal H E_-:
\operatorname{ran}E_-\longrightarrow\operatorname{ran}E_+.
\tag{NF6}
\]

Its spectrum consists of the positive and negative singular values of C,
with zero multiplicities included. In particular U is the largest
singular value and m the second-largest singular value when discussing
the two largest eigenvalues of this Hamiltonian.

For a simple U>0, choose unit singular vectors u,v with
`Cv=Uu`, `C^dagger u=Uv`, and u in ran E_+, v in ran E_-. Then

\[
\Omega=(u+v)/\sqrt2,
\qquad
\boxed{\rho_Q=\tfrac12\left(
\operatorname{Tr}_{R_1R_2}|u\rangle\langle u|
+\operatorname{Tr}_{R_1R_2}|v\rangle\langle v|
\right).}
\tag{NF7}
\]

The cross terms vanish under the partial trace because E_+ and E_- select
orthogonal reference parity spaces. This is an exact reconstruction of
the actual marginal; it does not discard the lower spectrum or assert
that the two rank-at-most-two summands are flat, complementary, or
independent. Degenerate U causes no failure of the parameterization: one
must retain the relevant top eigenspace and choose corresponding singular
vectors. In the nontrivial range U>2+sqrt(2), the previous two-eigenvalue
bound already ensures simplicity.

Equations (NF1)--(NF7) supply a globally covering finite parameter target
for the earlier joint spectral question. A proof that every such tuple
passes the rank-one resolvent certificate would imply the corresponding
sharp-two-pair converse. The normal form alone proves neither that
assertion nor the general three-pair retention bound. If that certificate
fails at a valid tuple, the complete operator (NF1), or its full singular
spectrum (NF6), remains available; no physical counterexample follows
merely from failure of a spectral upper bound.

## 5. Exact obstruction to separate score–spectrum constraints

Write `r=sqrt(2)` and choose

\[
\lambda=\frac1{60}(29,29,1,1),\qquad
U=\frac72,\qquad m=\frac12+2r.
\]

Then `2<m<U<4`, `U+m=4+2r`, and

\[
t=4+r-m=\frac72-r>2,\qquad
c=U-m=3-2r=2(t-2)>0.
\]

Both extreme eigenvalue pairs are `(x,y)=(29/60,1/60)`.
Their combined imbalance is

\[
\delta=\frac{x-y}{x+y}=\frac{14}{15}.
\]

For the kernel `k(a,b)=(a-b)^2/(a+b)`, the exact two-qubit SLD
spectral minimum is

\[
E_*(\lambda)=k_{12}+k_{13}+k_{24}+k_{34}
=2\frac{(28/60)^2}{30/60}
=\frac{196}{225}=\delta^2.
\]

The ordinary spectrum-dependent correlation condition holds strictly:

\[
E_* = \frac{196}{225}<\frac{15}{16}
=4-\frac{U^2}{4}.
\]

The stronger necessary condition derived in Section 6 also holds:

\[
E_* = \frac{196}{225}<\frac{29}{32}
=2+U-\frac{3U^2}{8}.
\]

Finally, Section 7 of `docs/ENTROPY_INEQUALITY_BOUNDARIES.md` proves
the exact maximum score over all two-qubit eigenbases at this spectrum:

\[
g_{\max}(\lambda)=2+\sqrt{4-2\delta^2}
=2+\frac{2\sqrt{127}}{15}>\frac72=U.
\]

The strict final comparison follows from `508>2025/4` after squaring
the positive quantities. Thus replacing the SLD bound by this exact
fixed-spectrum upper bound would still not eliminate these synthetic
data. This asserts only that a necessary upper bound is respected;
it does not assert realization by two sharp readout pairs.

### 5.1. Failure without optimizing a block angle

Use the allowed Jordan parameter `a=1`, hence `b=1`, in both
extreme-eigenvalue pairs. The two scalar resolvent eigenvalues are

\[
f=\frac{t-1}{t(t-2)},\qquad
g=\frac{t+1}{t(t+2)}.
\]

Since Phi is the maximum over all allowed blocks,

\[
\begin{aligned}
\sum_{j=1}^{2}\Phi_t(\lambda_j,\lambda_{5-j})
&\ge 2\left(\frac{29}{60}f+\frac1{60}g\right)\\
&=\frac{29}{30}f+\frac1{30}g\\
&=\frac{t^2-2+(14/15)t}{t(t^2-4)}.
\end{aligned}
\]

Multiplying by `c=2(t-2)` gives

\[
\begin{aligned}
c\sum_{j=1}^{2}\Phi_t(\lambda_j,\lambda_{5-j})-1
&\ge \frac{t^2-(2/15)t-4}{t(t+2)}\\
&=\boxed{\frac{587-412\sqrt2}{60t(t+2)}}>0.
\end{aligned}
\]

The denominator is positive. The numerator is strictly positive
because `587>0`, `412>0`, and

\[
587^2-2\cdot412^2=5081>0.
\]

The explicit lower witness is approximately `1.008495604658788`.
The strict conclusion uses exact arithmetic, not that decimal.

For a general doubly repeated spectrum
`((1+delta)/4,(1+delta)/4,(1-delta)/4,(1-delta)/4)` on the
boundary `U+m=4+2r`, this same fixed `a=1` block already fails whenever

\[
\delta>1+\frac2t-\frac t2,\qquad t=U-r>2.
\]

This is a sufficient failure condition for one explicit block, not an
exact formula for the scalar-branch transition of Phi.

## 6. A stronger necessary six-Pauli condition still does not suffice

Suppose an actual Hamiltonian is
`H_0=sum_{i=1}^2 (X_i tensor B_i+Z_i tensor D_i)`, where each
`B_i,D_i` is a pair of anticommuting Hermitian reflections. Let Omega
be a normalized top eigenvector with eigenvalue `U>2+r`, and let
rho be its two-qubit reference marginal, with eigenvalues lambda.

Set

\[
S_i=X_i\otimes B_i,\quad T_i=Z_i\otimes D_i,\quad
s_i=\langle S_i+T_i\rangle_\Omega,
\quad e_i=\langle S_iT_i\rangle_\Omega.
\]

The two tensor reflections commute: the reference and memory factors
each anticommute. Hence `(I-S_i)(I-T_i)` is positive, and

\[
e_i\ge s_i-1.
\]

Also `s_i<=2` and `s_1+s_2=U`, so `s_i>=U-2>r>1`.
In particular both lower bounds `s_i-1` are positive and may be
squared. The product is itself a Pauli correlation:

\[
S_iT_i=Y_i\otimes F_i,\qquad F_i=-iB_iD_i,
\]

where `F_i` is another Hermitian reflection.

For any reference Pauli P and any memory contraction C, purification
and trace-norm duality give

\[
|\langle P\otimes C\rangle_\Omega|
\le\|\sqrt\rho P\sqrt\rho\|_1,
\]

and the proved trace-norm/SLD estimate bounds the square of the right
side by `1-I_rho(P)`. Put `x_i=<S_i>`, `z_i=<T_i>`. Summing this
inequality for all six local reference Paulis and using
`sum_{i,P=X,Y,Z} I_rho(P)=2J(rho)>=2E_*(lambda)` yields

\[
2E_*(\lambda)
\le 6-\sum_i(x_i^2+z_i^2+e_i^2).
\]

Now `x_i^2+z_i^2>=s_i^2/2` and `e_i^2>=(s_i-1)^2`, so

\[
\begin{aligned}
\sum_i(x_i^2+z_i^2+e_i^2)
&\ge\frac32\sum_i s_i^2-2U+2\\
&\ge\frac34U^2-2U+2.
\end{aligned}
\]

Therefore every such actual Hamiltonian obeys

\[
\boxed{E_*(\lambda)\le 2+U-\frac38U^2.}
\]

This condition is stronger than `E_*<=4-U^2/4` for `U<4`, with
difference `(4-U)^2/8`. The example above obeys it and still fails
the rank-one certificate. Consequently, these separate scalar
constraints do not replace the missing joint constraint on the top
state and the remainder of the Hamiltonian's spectrum.

## 7. The earlier spectral-sum bound is physically sharp

A uniformly smaller constant cannot replace `U+m<=4+2sqrt(2)`.
On Q=A tensor B choose

$$
B_1=X_A,\quad D_1=Z_A,\qquad B_2=Z_B,\quad D_2=X_AX_B.
$$

Both pairs are anticommuting reflections. Set
`A=X_1X_A`, `C=X_2Z_B`, `B=Z_1Z_A`, `D=Z_2X_AX_B`.
The operators A,C commute with each other and with B,D; B,D anticommute.
Each simultaneous A,C eigenspace has dimension four. On it B,D are
anticommuting reflections, so B+D has eigenvalues +/-sqrt(2), each twice.
Therefore the complete H_0 spectrum is

$$
\{\,a+c+s\sqrt2:a,c,s\in\{-1,1\}\,\},
$$

with each sign combination counted twice. Its top two eigenvalues are
both `2+sqrt(2)`. This is a valid sharp-pair Hamiltonian at the already
triangle-controlled boundary; it is not a resolvent failure. It rules out
repairing the separate-data approach by simply decreasing the universal
constant in that spectral-sum bound.

## 8. Primary source and provenance

Kraus and Cirac, *Optimal Creation of Entanglement Using a Two-Qubit Gate*,
Phys. Rev. A 63, 062309 (2001), arXiv:quant-ph/0011050v1,
https://arxiv.org/pdf/quant-ph/0011050 . Section III, Eqs. (11)--(12),
PDF page 3, state the arbitrary two-qubit decomposition used in (NF3);
Appendix A, PDF pages 6–7, supplies its proof. The sign convention in their exponential
is absorbed in the unrestricted real angles here. Their smaller
parameter domain in Eq. (13) is justified for their entanglement objective
using extra symmetries; the cube (NF2) avoids importing those extra
symmetries into this problem.

The normal form is an application of established KAK machinery. The
chiral reduction is elementary block linear algebra. These are not new
general decomposition or spectral theorems. Their use here preserves the
actual joint spectral data for the full sharp-pair class. The normal form,
operator expansion, marginal reconstruction, and exact obstruction received
independent internal reconstructions. This is not external review or an
exhaustive priority assessment.

## 9. Verification and the next proof target

The [deterministic checker](../../tools/check_joint_spectrum_normal_form.py)
and [recorded output](../../results/joint_spectrum_normal_form.json) verify
the relaxation example with exact rational arithmetic in Q(sqrt(2)). They
also check 40 small normal-form constructions, including boundary angles,
identity and SWAP Cartan factors, complex local rotations, the Pauli
expansion, the full singular spectrum, and the marginal reconstruction.
The top is simple in 37 of those cases; comparison of its marginal to
direct diagonalization is restricted to those cases. A separate Pauli
matrix check reproduces Section 7's full spectrum. No optimizer is used.
These diagnostics verify identities, not the universal inequality.

The next target is now a statement on the complete domain (NF2): for
`U>2+sqrt(2)`, compute U,m and the actual rho_Q by (NF6)–(NF7), set
`c=U-m`, `t=4+sqrt(2)-m`, and prove or disprove

$$
c\sum_{j=1}^2\Phi_t(\lambda_j,\lambda_{5-j})\le1.
$$

The preceding report proves that these t exceed two and U is simple in
this range. Phi retains its exact quartic/cubic test there. A proof would
settle the case of two internally sharp anticommuting pairs and one
arbitrary third pair. A valid failure would disprove that rank-one-envelope
strategy at that Hamiltonian, and require retaining more of its lower
spectrum. Section 5's synthetic tuple does neither. Unequal Jordan-block
angles and the unrestricted three-input optimum remain separate open
obligations. The full normal form is available to address the actual
joint constraint; independent scalar bounds cannot be substituted for it.
