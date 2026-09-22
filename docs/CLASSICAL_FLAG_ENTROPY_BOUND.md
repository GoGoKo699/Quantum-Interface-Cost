# Closure of the seed entropy bound under local classical flags

Date: 22 September 2026. Research base:
`87b6432cdd1f29bc4981f24bd6732bb933741193`.

**Status:** supplied analytical deduction, independently reconstructed within
this workspace. This note proves additional
restricted-family exclusions; it neither proves the unrestricted entropy
inequality nor establishes publication novelty.

Write

$$
g_n(\rho)=\sum_{i=1}^n\sum_{b=X,Z}
\|\sqrt\rho\,P_{i,b}\sqrt\rho\|_1,
\qquad c=2-\sqrt2.
$$

The target inequality is

$$
g_n(\rho)\le\sqrt2\,n+cS(\rho),
\tag{1}
$$

where entropy is measured in bits. The
[product-diagonal proof](COMMUTING_SEED_BOUND.md) assumes a fixed tensor
product of local eigenbases. We show that the family satisfying (1) is
closed under adjoining a local classical flag and under tensor products.
Consequently every two-qubit state that is classical on either qubit
satisfies (1), even when its conditional states on the other qubit do not
commute. A rank-three example below lies outside every fixed product basis.

These are statements about seed Gram matrices. The physical task still
allows arbitrary collective encoders acting on one unknown specimen,
unlimited classical records, a worst-case quantum dimension cap, and one
delayed query with uniform error on every input. None of the flag conditions
is imposed on that operational optimization.

## 1. A partial-trace fidelity inequality

Use root fidelity

$$
F(A,B)=\|\sqrt A\sqrt B\|_1
$$

for positive semidefinite matrices. If U is a Hermitian unitary, then

$$
F(\rho,U\rho U)=\|\sqrt\rho\,U\sqrt\rho\|_1.
\tag{2}
$$

Indeed, `sqrt(U rho U)=U sqrt(rho) U`, and multiplication by the rightmost
U preserves trace norm.

The established monotonicity of fidelity under partial trace gives

$$
F(\rho_{AB},\sigma_{AB})\le F(\rho_A,\sigma_A).
\tag{3}
$$

For completeness, the following elementary argument proves the exact
special case used here without importing an external theorem. The
variational formula is

$$
F(A,B)=\frac12\inf_{H>0}
\left(\operatorname{Tr}(AH)+\operatorname{Tr}(BH^{-1})\right).
\tag{4}
$$

For every positive definite H, trace-norm duality and Hilbert--Schmidt
Cauchy--Schwarz give

$$
\begin{aligned}
F(A,B)
&=\max_{V\ \mathrm{unitary}}
 |\operatorname{Tr}(\sqrt A V\sqrt B)|\\
&\le\sqrt{\operatorname{Tr}(AH)\operatorname{Tr}(BH^{-1})}\\
&\le\tfrac12\left(\operatorname{Tr}(AH)+\operatorname{Tr}(BH^{-1})\right).
\end{aligned}
$$

To see the middle step, cycle the trace into the product
`(H^(1/2) sqrt(A) V)(sqrt(B) H^(-1/2))`; the two squared
Hilbert--Schmidt norms are the two traces displayed. When A and B are
positive definite, the choice

$$
H=A^{-1/2}(A^{1/2}BA^{1/2})^{1/2}A^{-1/2}
$$

makes both traces equal to `F(A,B)`, proving (4). For semidefinite A and B,
apply this construction to `A+epsilon I,B+epsilon I`: their minimizing H
makes the unregularized expression no larger than its regularized value,
which tends to `F(A,B)`. Together with the lower bound this proves (4) in
the limit, without requiring attainment of the infimum.

Apply (4) to the joint matrices and restrict its minimization to
`H=H_A tensor I_B`. The two traces then depend only on the A marginals,
and another application of (4) proves (3). In particular, for a local
query U on A,

$$
\|\sqrt\rho\,(U\otimes I)\sqrt\rho\|_1
\le\|\sqrt{\rho_A}\,U\sqrt{\rho_A}\|_1.
\tag{5}
$$

The direction of this inequality is essential: discarding B increases
fidelity and therefore supplies an upper bound on the joint seed score.

## 2. Closure under a local classical flag

**Theorem.** Let i be one of n input qubits, let
`{|0_N>,|1_N>}` be any orthonormal basis on that qubit, and suppose

$$
\rho=\sum_{a=0}^1p_a|a_N\rangle\langle a_N|_i\otimes\sigma_a,
\qquad p_0+p_1=1.
\tag{6}
$$

The conditional states sigma_a on the other n-1 sites may be noncommuting,
entangled, or rank deficient. Assume that every positive-weight branch
satisfies

$$
g_{n-1}(\sigma_a)\le\sqrt2(n-1)+cS(\sigma_a).
\tag{7}
$$

Then rho satisfies (1).

**Proof.** For a query on a site other than i, the sandwiched observable is
block diagonal in the flag basis. Trace norm is additive on these orthogonal
blocks, so summing all those queries gives exactly

$$
\sum_{j\ne i}\sum_{b=X,Z}
\|\sqrt\rho\,P_{j,b}\sqrt\rho\|_1
=\sum_a p_a g_{n-1}(\sigma_a)
\le\sqrt2(n-1)+c\sum_a p_aS(\sigma_a).
\tag{8}
$$

For the two queries on i, apply (5). The flag marginal has eigenvalues
`p_0,p_1`. The single-qubit entropy inequality, proved in
[COMMUTING_SEED_BOUND.md](COMMUTING_SEED_BOUND.md), Sections 2 and 5,
gives

$$
\sum_{b=X,Z}\|\sqrt\rho\,P_{i,b}\sqrt\rho\|_1
\le g_1(\rho_i)\le\sqrt2+c h_2(p_0).
\tag{9}
$$

That scalar inequality allows any local eigenbasis, including an axis
with a Y component. Finally, the eigenvalues of rho are the eigenvalues
of the blocks `p_a sigma_a`; hence

$$
S(\rho)=h_2(p_0)+\sum_a p_aS(\sigma_a).
\tag{10}
$$

Adding (8) and (9) proves (1). A zero-weight branch contributes zero and
requires no definition of its conditional state. This completes the proof.

The theorem can be iterated. A further flag's site and local basis may
be chosen differently in each existing orthogonal branch: its conditional
state is tested by (7) separately. Thus a single globally fixed tensor
product eigenbasis is unnecessary. For example, taking all terminal
conditional states to be one-qubit states proves (1) for the entire class
obtained by recursively adjoining such flags. Alternatively, terminal
states may come from any other family already known to satisfy (1),
including the arbitrary-eigenbasis rank-two family.

This is a mathematical construction of seed states. It does not assume that
the unrestricted physical encoder is a sequence of local measurements.

## 3. Closure under tensor products

**Proposition.** If rho on n qubits and sigma on m qubits satisfy (1),
then so does `rho tensor sigma`.

For a query on the rho factor,

$$
\|\sqrt{\rho\otimes\sigma}\,(P\otimes I)
\sqrt{\rho\otimes\sigma}\|_1
=\|(\sqrt\rho P\sqrt\rho)\otimes\sigma\|_1
=\|\sqrt\rho P\sqrt\rho\|_1,
$$

since `||sigma||_1=1`. The analogous identity holds for the other factor.
Therefore

$$
g_{n+m}(\rho\otimes\sigma)=g_n(\rho)+g_m(\sigma),
\qquad S(\rho\otimes\sigma)=S(\rho)+S(\sigma),
\tag{11}
$$

and the claimed closure follows. These tensor powers and classical-flag
extensions cannot create an entropy witness from seeds that already satisfy
(1).

## 4. All two-qubit states classical on either site

**Corollary.** Every two-qubit state of the form

$$
\rho_{AB}=p|0_N\rangle\langle0_N|\otimes\sigma_0
 +(1-p)|1_N\rangle\langle1_N|\otimes\sigma_1
\tag{12}
$$

satisfies

$$
g_2(\rho_{AB})\le2\sqrt2+cS(\rho_{AB}).
$$

The conditional qubit states are arbitrary, so this follows directly from
the theorem and the one-qubit bound. The same statement holds with A and B
interchanged.

A concrete example beyond every fixed tensor product eigenbasis is

$$
\rho_{AB}=\frac12|0\rangle\langle0|\otimes|0\rangle\langle0|
 +\frac12|1\rangle\langle1|\otimes\frac{I+X/2}{2}.
\tag{13}
$$

Its spectrum is `(1/2,3/8,1/8,0)`: this is a nonuniform rank-three case.
If rho were diagonal in a fixed product basis, it would commute with some
nontrivial local Pauli axis `I tensor N_B`. Its two A blocks would then
force N_B to commute with both Z and X, which is impossible. Thus the new
exclusion is strictly broader than the fixed-product-basis condition.

The same argument provides full-rank examples by choosing
`sigma_0=(I+Z/2)/2`, `sigma_1=(I+X/2)/2`, and any `0<p<1` in (12).
The proof uses orthogonality on the flag site; it does not extend by simply
replacing those flag vectors with nonorthogonal states.

**Equality within this two-qubit family.** Equality in (1) holds exactly
for tensor products whose individual factors are `I/2` or pure X/Z
bisector states. Indeed, the scalar flag inequality (9) is strict unless
`p=0,1/2,1`. At an endpoint, the flag must be a pure bisector and the
other qubit must attain its own scalar bound. At `p=1/2`, equality requires
both flag fidelities to be one. Root fidelity between normalized states
is one exactly when the states coincide, as follows from the equality
case of Hilbert--Schmidt Cauchy--Schwarz in its trace-norm dual formula.
Thus rho commutes with both `X_A` and `Z_A`, forcing
`rho=I_A/2 tensor sigma_B`. The one-qubit equality cases again give the
stated factors. Every such product attains (1), by (11).

## 5. The local conditional-entropy route fails even on two qubits

A tempting stronger statement would replace the marginal entropy in (9)
by conditional entropy:

$$
\sum_{b=X,Z}\|\sqrt\rho\,P_{A,b}\sqrt\rho\|_1
\stackrel{?}{\le}\sqrt2+cH(A\mid B)_\rho.
\tag{14}
$$

Summing such inequalities would imply the desired global result. However,
(14) is false even for a two-qubit state of rank two, classical on A.
This strengthens the obstruction recorded in
[COMMUTING_SEED_BOUND.md](COMMUTING_SEED_BOUND.md), Section 6, by requiring
only a single qubit in the complementary reference system B.

For `1/2<=p<=1`, put

$$
|b_\pm\rangle=\sqrt p\,|0\rangle\pm\sqrt{1-p}\,|1\rangle,
\qquad
\rho_{AB}=\frac12|0\rangle\langle0|\otimes|b_+\rangle\langle b_+|
 +\frac12|1\rangle\langle1|\otimes|b_-\rangle\langle b_-|.
\tag{15}
$$

The two branches are orthogonal on A, so `S(AB)=1`. Its B marginal is
`diag(p,1-p)`, whence `H(A|B)=1-h_2(p)`. The Z_A query commutes with
rho and has score one. The X_A query exchanges the A branches; its two
nonzero singular values are each `|<b_+|b_->|/2`. Therefore

$$
F_{A,Z}=1,\qquad F_{A,X}=2p-1,
\qquad F_{A,X}+F_{A,Z}=2p.
\tag{16}
$$

At `p=9/10`, the proposed inequality would require

$$
1.8\le2-c h_2(9/10)\simeq1.725268742,
$$

which is false. Every dimension, probability, and trace norm here is exact;
no optimization or numerical certificate is involved in the counterexample.

This does not refute the global entropy inequality. In the same X/Z axes,
the B queries have scores `2sqrt(p(1-p))` and `2p-1`. At `p=9/10` their
sum is `1.4`, so the global score is `3.2`, below the entropy bound
`2+sqrt(2)`. The flag theorem and the previously proved rank-two theorem
both independently exclude this state as a global witness.

## 6. Remaining scope and novelty

For two input qubits, any entropy witness must now be outside both the
classical-on-A and classical-on-B families, as well as the previously
excluded rank-two, flat rank-three, product-diagonal, and stabilizer-basis
families. General nonuniform rank-three and full-rank states remain open.
The flag theorem does not cover every separable state, and nonclassical
correlations in a Gram matrix are not by themselves a certificate of an
operational advantage.

The ingredients are standard fidelity monotonicity, trace-norm block
additivity, and the entropy of an orthogonal classical--quantum mixture.
The new content supplied here is their direct application to the repository's
seed functional, its closure consequences, and the explicit two-qubit
counterexample to a proposed local proof route. No claim that these short
deductions are absent from prior literature is made.
