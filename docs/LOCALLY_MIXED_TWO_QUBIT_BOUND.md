# An entropy bound for locally maximally mixed two-qubit seeds

Date: 22 September 2026. Research base:
`87b6432cdd1f29bc4981f24bd6732bb933741193`.

**Status:** supplied analytical deduction, independently reconstructed within
this workspace, with publication novelty unresolved.
The hypothesis concerns a family of seed Gram matrices; the operational
encoder remains unrestricted.

## 1. Statement

Let rho be any two-qubit density matrix whose two one-qubit marginals are
both `I/2`. Define

$$
g_2(\rho)=\sum_{P\in\{X_A,Z_A,X_B,Z_B\}}
\|\sqrt\rho\,P\sqrt\rho\|_1.
$$

Then

$$
\boxed{
 g_2(\rho)\le4-\kappa\,[2-S(\rho)],
 \qquad \kappa=2(2-\sqrt2)\ln2\simeq0.8120724353.
}
\tag{1}
$$

Since `kappa>2-sqrt(2)`, every such state satisfies the proposed global
entropy inequality

$$
g_2(\rho)\le2\sqrt2+(2-\sqrt2)S(\rho),
\tag{2}
$$

strictly unless `rho=I/4`. This excludes nonuniform rank-three and general
full-rank states within the stated family. Neither (1) nor its coefficient
is claimed sharp.

The proof allows arbitrary local rotations of a Bell-diagonal state,
including rotations outside the Clifford group. The earlier
[stabilizer-eigenbasis bound](ENTROPY_INEQUALITY_BOUNDARIES.md), Section 3,
does not by itself cover those rotations of the query axes.

## 2. Reduction to a Bell-diagonal state with rotated queries

The two marginal conditions give the Pauli expansion

$$
\rho=\frac14\left(I\otimes I+
\sum_{a,b\in\{x,y,z\}}T_{ab}\,\sigma_a\otimes\sigma_b\right),
\qquad T\in\mathbb R^{3\times3}.
$$

A real singular-value decomposition, with signs absorbed into the diagonal
entries when necessary, supplies proper rotations `R_A,R_B` such that
`R_A T R_B^T` is diagonal. Proper rotations are implemented by local qubit
unitaries. After this change of basis, rho therefore has the form

$$
\rho_{\mathrm{Bell}}=
\frac14\left(I\otimes I+\sum_a t_a\,\sigma_a\otimes\sigma_a\right).
\tag{3}
$$

The three displayed Pauli products commute and have the Bell basis as a
joint eigenbasis. Thus (3) is diagonal with a nonnegative spectrum
`lambda=(lambda_1,...,lambda_4)` summing to one. No condition beyond the
positivity of the original state has been imposed.

Unitary conjugation preserves the sandwiched trace norms if the queries
are conjugated as well. The original X/Z pair on each site becomes some
two orthogonal Pauli directions on that site. The problem is therefore to
bound the four scores of a Bell-diagonal rho for two arbitrary orthogonal
query directions on each side. Entropy remains `H(lambda)`.

## 3. The score is a quadratic norm of each query direction

For Bell-diagonal rho, set

$$
F_a=\|\sqrt\rho\,(\sigma_a\otimes I)\sqrt\rho\|_1,
\qquad a\in\{x,y,z\}.
$$

For every real unit vector v,

$$
\boxed{
 \|\sqrt\rho\,(v\cdot\sigma\otimes I)\sqrt\rho\|_1^2
 =\sum_a v_a^2F_a^2.
}
\tag{4}
$$

The same formula, with the same three numbers F_a, holds for queries on B.

To prove it, use the antiunitary spin flip
`J=(Y tensor Y) K`, where K is complex conjugation in the computational
basis. Each Bell projector is invariant under J. In addition,

$$
J(v\cdot\sigma\otimes I)J^{-1}
=-(v\cdot\sigma\otimes I).
$$

Consequently the Hermitian matrix

$$
M_v=\sqrt\rho\,(v\cdot\sigma\otimes I)\sqrt\rho
$$

satisfies `J M_v J^(-1)=-M_v`. Its eigenvalues can be written as
`a,-a,b,-b` with `a,b>=0`, including zero eigenvalues. The determinant
of the local Pauli query, acting on four dimensions, is +1, so
`det(M_v)=det(rho)`. It follows that

$$
\|M_v\|_1^2
=2\operatorname{Tr}(M_v^2)+8\sqrt{\det\rho}.
\tag{5}
$$

The argument works for singular rho as written; alternatively the same
identity follows by continuity from positive definite states.

For distinct a,b,

$$
\operatorname{Tr}\left[
 \rho(\sigma_a\otimes I)\rho(\sigma_b\otimes I)\right]=0.
$$

Indeed, conjugation by `sigma_a tensor sigma_a` fixes rho and the first
local Pauli, and reverses the sign of the second. Expanding the trace in
(5) thus gives a diagonal quadratic form in v. Since `sum_a v_a^2=1`,
the determinant term is the same weighted sum of its three axial values.
This proves (4).

A local Pauli on either side permutes the four Bell vectors by the same
translation of their two-bit labels, up to phases. Therefore the axial
trace norms on B equal F_a as well. The same spin-flip argument proves
(4) there.

Order these three axial fidelities as `F_1>=F_2>=F_3`. For any orthogonal
unit vectors v,w, Cauchy--Schwarz followed by the rank-two variational
bound for a diagonal matrix gives

$$
\begin{aligned}
F(v)+F(w)
&\le\sqrt{2\left(v^TDv+w^TDw\right)}\\
&\le\sqrt{2(F_1^2+F_2^2)},
\qquad D=\operatorname{diag}(F_x^2,F_y^2,F_z^2).
\end{aligned}
\tag{6}
$$

For the second step, `vv^T+ww^T` is a rank-two orthogonal projector; its
trace against D is at most the sum of D's two largest eigenvalues. Applying
(6) independently on the two sites yields

$$
g_2(\rho)\le2\sqrt2\sqrt{F_1^2+F_2^2}.
\tag{7}
$$

Thus arbitrary rotations are controlled explicitly, rather than treated
as Clifford operations.

## 4. Bell translations and entropy

Label the Bell basis by the two binary Pauli exponents defining it from
`|Phi+>`. The three nontrivial local Pauli operators translate that label
by the three nonzero vectors of `F_2^2`. For a translation v, its axial
fidelity is

$$
F_v=\sum_{x\in\mathbb F_2^2}\sqrt{\lambda_x\lambda_{x+v}}.
\tag{8}
$$

The two translations corresponding to F_1 and F_2 are distinct nonzero
vectors, hence linearly independent. Relabeling the four probabilities by
an invertible binary map turns these two translations into the two coordinate
flips. The entropy of the relabeled law `(U_1,U_2)` is `S(rho)`.

The binary inequality

$$
1-2\sqrt{t(1-t)}\ge\ln2\,[1-h_2(t)]
\tag{9}
$$

is proved explicitly in
[ENTROPY_INEQUALITY_BOUNDARIES.md](ENTROPY_INEQUALITY_BOUNDARIES.md), Section 3.
Apply (9) to each conditional binary law along a coordinate edge and average
over the other coordinate. Equation (8) gives

$$
1-F_i\ge\ln2\,[1-H(U_i\mid U_{3-i})],\qquad i=1,2.
$$

Since

$$
H(U_1\mid U_2)+H(U_2\mid U_1)
=H(U_1,U_2)-I(U_1:U_2)\le H(U_1,U_2),
$$

we obtain

$$
2-F_1-F_2\ge\ln2\,[2-S(\rho)].
\tag{10}
$$

Zeros in lambda are allowed; conditional edges of zero weight contribute
zero. The selection of the two largest fidelities does not change the
argument because every pair of distinct nonzero translations is independent.

## 5. Combining the two estimates

For all `0<=a,b<=1` and `c=2-sqrt(2)`, the elementary inequality

$$
\sqrt2\sqrt{a^2+b^2}\le2-c(2-a-b)
\tag{11}
$$

holds. To verify it, the convex function
`sqrt(2) sqrt(a^2+b^2)-c(a+b)` is at most its largest value at a vertex
of the unit square. That value is `2-2c` at each of `(1,0),(0,1),(1,1)`;
the remaining vertex has value zero. This proves (11).

All root fidelities of normalized states belong to `[0,1]`, so (7), (11),
and (10) give

$$
\begin{aligned}
g_2(\rho)
&\le2\sqrt2\sqrt{F_1^2+F_2^2}\\
&\le4-2c(2-F_1-F_2)\\
&\le4-2c\ln2\,[2-S(\rho)],
\end{aligned}
$$

which proves (1). Since `2ln2>1`, its deficit coefficient is strictly larger
than c. For every nonmaximally mixed rho, `S(rho)<2`, so (2) is strict.
At `rho=I/4`, all four scores are one and (2) is an equality.

## 6. Scope

The theorem permits entangled eigenvectors, arbitrary spectra, and arbitrary
local rotations. It nevertheless requires both one-qubit marginals to be
maximally mixed. A possible two-qubit entropy witness must fail at least one
of those marginal conditions, as well as evade the other proved families.
States with only one maximally mixed marginal are not covered by this note.

The argument combines elementary two-qubit canonical form and spin-flip
algebra with the binary entropy inequality already used in the repository.
It supplies a family-specific deduction, not a novel claim about fidelity,
Bell states, or entropy tensorization. The unrestricted entropy theorem,
finite-budget problem, and publication novelty remain unresolved.
