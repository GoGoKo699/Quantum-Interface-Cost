# A kernel-sensitive converse for two-qubit seeds

Date: 22 September 2026. Research base:
`358d887058eb9fa2fe8bb899d0261ec811d42fa6`.

**Status:** supplied analytical deduction, independently reconstructed within
this workspace; publication novelty remains unresolved. The results below give explicit
certificates for nonuniform rank-three spectra and arbitrary supported
eigenvectors. They do not prove the unrestricted two-qubit entropy inequality.

For a two-qubit density matrix rho, write

$$
\begin{aligned}
g_2(\rho)&=\sum_{P\in\mathcal Q}F_P,
&F_P&=\|\sqrt\rho P\sqrt\rho\|_1,\\
\mathcal Q&=\{X_A,Z_A,X_B,Z_B\},
&c&=2-\sqrt2.
\end{aligned}
$$

The proposed entropy bound is `g_2(rho)<=2sqrt(2)+cS(rho)`, with entropy
in bits. This note bounds the score using the kernel of rho and its spectrum.
It keeps all physical query axes fixed.

## 1. Statements and computable entropy certificates

Let rho have rank three, with ordered positive eigenvalues
`lambda_1>=lambda_2>=lambda_3>0`, and let its normalized kernel vector
be v. Define

$$
M(v)=\sum_{P\in\mathcal Q}|\langle v|P|v\rangle|.
$$

Both one-qubit marginals of the pure state v have the same Bloch-vector
length r_v. Equivalently,

$$
r_v=\sqrt{1-C(v)^2},
$$

where `C(v)=2|det V|` for the normalized coefficient matrix
`|v>=sum_{a,b}V_{ab}|ab>`. The latter identity follows directly from
its two Schmidt coefficients. In particular, `r_v=0` exactly when v
is maximally entangled, and `r_v=1` exactly when v is a product vector.

For the Pauli correlation coefficients
`T_ab=Tr(rho sigma_a tensor sigma_b)`, put

$$
\chi_Y(\rho)=T_{xy}^2+T_{zy}^2+T_{yx}^2+T_{yz}^2+2T_{yy}^2.
$$

**Theorem 1.** Every such rank-three state satisfies

$$
\boxed{
 g_2(\rho)^2
 \le 8-4\chi_Y(\rho)+16\lambda_1\lambda_2 M(v)
 \le 8-4\chi_Y(\rho)+32\sqrt2\lambda_1\lambda_2 r_v.
}
\tag{1}
$$

The nonnegative correlation correction can be discarded when only the
spectrum and kernel are known. Thus the readily checkable inequality

$$
8+16\lambda_1\lambda_2 M(v)
\le \bigl(2\sqrt2+cS(\rho)\bigr)^2
\tag{2}
$$

certifies the proposed entropy bound for every state with that spectrum
and kernel. A condition using only the kernel's entanglement and the
spectrum is

$$
\boxed{
8\lambda_1\lambda_2 r_v
\le cS(\rho)+\frac{c^2}{4\sqrt2}S(\rho)^2.
}
\tag{3}
$$

Strict inequality in either certificate implies a strict entropy bound.
Setting `r_v=1` in (3) supplies a spectrum-only sufficient condition,
valid for all choices of kernel and supported eigenvectors. For example,
the nonuniform spectrum `(1/2,1/4,1/4,0)` has entropy `3/2`; equation (1)
gives

$$
g_2(\rho)\le\sqrt{8+4\sqrt2}
<2\sqrt2+\frac32(2-\sqrt2).
$$

Consequently every state with that spectrum obeys the entropy inequality,
without a classicality or local-marginal hypothesis. The condition is
sufficient and does not cover all nonuniform rank-three spectra.
The strict squared-bound gap in the example is `3/2-sqrt(2)>0`.

**Corollary 2.** If any two-qubit density matrix has a maximally entangled
vector in its kernel, then

$$
\boxed{g_2(\rho)\le2\sqrt2.}
\tag{4}
$$

This permits arbitrary spectra and local rotations of the kernel vector.
The constant is sharp across this class: the product state
`|beta_+ beta_+><beta_+ beta_+|` has score `2sqrt(2)` and is orthogonal
to the singlet `(|01>-|10>)/sqrt(2)`, where beta_+ is the positive X/Z
bisector. This example does not assert attainment for every locally rotated
maximally entangled kernel with the query axes held fixed.

In the normalized-seed reduction, (4) means that such a seed cannot exceed
the zero-memory contrast `1/sqrt(2)`. It is a property of this class of
Gram matrices, not a restriction on admissible physical instruments.

## 2. A two-qubit aggregate identity

For any two-qubit density matrix, define

$$
Q_P=2\operatorname{Tr}(\rho P\rho P)
-\bigl(\operatorname{Tr}(\rho P)\bigr)^2.
$$

Then the following identity holds, without a rank assumption:

$$
\boxed{\sum_{P\in\mathcal Q}Q_P=2-\chi_Y(\rho).}
\tag{5}
$$

To verify it, expand

$$
\rho=\frac14\left(I+\sum_a a_a\sigma_a\otimes I
+\sum_b b_b I\otimes\sigma_b
+\sum_{a,b}T_{ab}\sigma_a\otimes\sigma_b\right).
$$

For a Pauli string W, let w(W) be the number of queries in Q that
anticommute with W. The sum of its four conjugation signs is
`4-2w(W)`. Pauli orthogonality therefore gives

$$
\begin{aligned}
\sum_{P\in\mathcal Q}\operatorname{Tr}(\rho P\rho P)
={}&1+\frac12(a_x^2+a_z^2+b_x^2+b_z^2)\\
&-\frac12(T_{xy}^2+T_{zy}^2+T_{yx}^2+T_{yz}^2)-T_{yy}^2.
\end{aligned}
$$

Here singleton X/Z strings have weight one, singleton Y and two-site
X/Z strings have weight two, strings with exactly one Y and one X/Z
have weight three, and YY has weight four. Meanwhile
`sum_P(Tr rho P)^2=a_x^2+a_z^2+b_x^2+b_z^2`. Subtracting that sum
from twice the preceding expression proves (5).

## 3. Kernel compression and the rank-three trace norm

Fix one query P and write `m=<v|P|v>`. Replacing P by minus P changes
neither its score nor Q_P, so first choose its sign so that `m>=0`.
Let `Pi=I-|v><v|` project onto the three-dimensional support. The
compression `Pi P Pi`, restricted to that support, has eigenvalues

$$
1,\quad -1,\quad -m.
\tag{6}
$$

Indeed, each of the full four-dimensional query's positive and negative
eigenspaces has dimension two. Its intersection with v's orthogonal
complement supplies a supported eigenvector with eigenvalue +1 or -1,
respectively. The remaining compressed eigenvalue is fixed by
`Tr(Pi P Pi)=Tr(P)-<v|P|v>=-m`. This also proves (6) when the last
eigenvalue coincides with either of the first two, or vanishes.

Let sigma be the strictly positive restriction of rho to its support.
Congruence by `sqrt(sigma)` preserves inertia, so the three supported
eigenvalues of `sqrt(rho)P sqrt(rho)` can be written

$$
a,\quad -b,\quad -d,
\qquad a>0,\quad b>0,\quad d\ge0.
$$

One of b,d can be zero when m is zero. The determinant and trace
identities give

$$
abd=\lambda_1\lambda_2\lambda_3 m,
\qquad
F_P^2=Q_P+4bd.
\tag{7}
$$

For the second equality, substitute `F_P=a+b+d` and
`Tr(rho P)=a-b-d` into Q_P. For m=0, the determinant identity forces
`bd=0`, so `F_P^2=Q_P` exactly.

The lone positive eigenvalue also satisfies `a>=lambda_3`. To see this,
choose a unit supported eigenvector u_+ of the compression with eigenvalue
+1 and evaluate the Rayleigh quotient at `sigma^(-1/2)u_+`:

$$
a\ge\frac{1}{\langle u_+|\sigma^{-1}|u_+\rangle}
\ge\lambda_3.
\tag{8}
$$

Together with (7), this proves

$$
F_P^2\le Q_P+4\lambda_1\lambda_2 |\langle v|P|v\rangle|.
\tag{9}
$$

Summing (9), using (5), and applying
`(sum_P F_P)^2<=4 sum_P F_P^2` proves the first bound in (1).
For each one-qubit marginal of v, its X/Z components obey
`|r_x|+|r_z|<=sqrt(2)sqrt(r_x^2+r_z^2)<=sqrt(2)r_v`.
Summing both marginals gives `M(v)<=2sqrt(2)r_v`, proving the second bound.
Expanding the entropy line's square gives certificates (2) and (3).

If v is maximally entangled, every local Pauli expectation m is zero;
(1) gives (4) for rank-three rho. To include lower ranks, replace rho by
`rho_delta=(1-delta)rho+delta Pi/3` with `0<delta<1`. This has rank
three, retains v in its kernel, and converges to rho. Continuity of the
matrix square root and trace norm gives (4) in the limit. This avoids any
assumption about the choice of eigenvectors inside a degenerate kernel.

## 4. A stronger support-and-spectrum certificate

Equation (8) can be retained in its first, more precise form. This yields
a refinement computable from one three-dimensional kernel operator.
For each P, put `m_P=|<v|P|v>|`, choose `P'=P` when its expectation
is nonnegative and `P'=-P` otherwise, and let

$$
E_{P,+}=\frac{I+P'}{2},
\qquad
K_{P,+}=E_{P,+}
-\frac{E_{P,+}|v\rangle\langle v|E_{P,+}}
{(1+m_P)/2}.
\tag{10}
$$

The denominator is positive, including when m_P=0. The matrix K_{P,+}
is the rank-one orthogonal projector onto the intersection of the
+1 eigenspace of P' with v's orthogonal complement. Thus it projects
onto the vector u_+ used in (8). Define

$$
T_v=\sum_{P\in\mathcal Q}m_P K_{P,+},
$$

and let `t_1>=t_2>=t_3>=0` be its three eigenvalues on v's orthogonal
complement. This operator depends on the actual kernel and the fixed
query axes, but not on the supported eigenvectors of rho. Its trace is
`M(v)`.

On the support, define the positive matrix

$$
D_\sigma=(\det\sigma)\sigma^{-1}.
$$

Its ordered eigenvalues are
`lambda_1 lambda_2`, `lambda_1 lambda_3`, and `lambda_2 lambda_3`.
Equations (7) and (8) give the pointwise refinement

$$
bd\le m_P\langle u_+|D_\sigma|u_+\rangle.
$$

Summing and using (5) as before gives

$$
\begin{aligned}
g_2(\rho)^2
&\le 8-4\chi_Y(\rho)+16\operatorname{Tr}(D_\sigma T_v)\\
&\le 8-4\chi_Y(\rho)
+16\bigl(\lambda_1\lambda_2 t_1
+\lambda_1\lambda_3 t_2+\lambda_2\lambda_3 t_3\bigr).
\end{aligned}
\tag{11}
$$

The final step is the eigenvalue trace inequality: in eigenbases of the
two positive matrices, their overlap-squared matrix is doubly stochastic,
and the rearrangement inequality maximizes the trace by pairing descending
eigenvalues. No simultaneous diagonalization of the actual two matrices
is assumed.

The refinement is at least as strong as the first scalar bound in (1),
because all eigenvalues of D_sigma are at most `lambda_1 lambda_2`
and `Tr T_v=M(v)`. A sufficient entropy certificate depending only on
the spectrum and the actual kernel is therefore

$$
\boxed{
8+16\bigl(\lambda_1\lambda_2 t_1
+\lambda_1\lambda_3 t_2+\lambda_2\lambda_3 t_3\bigr)
\le\bigl(2\sqrt2+cS(\rho)\bigr)^2.
}
\tag{12}
$$

Dropping chi_Y makes this a uniform certificate for every supported
eigenbasis with the specified spectrum and kernel. Retaining chi_Y
in (11) can certify additional individual states. The remaining
optimization over kernels is not solved here; in particular, no claim
that a product kernel maximizes every eigenvalue of T_v is used.

## 5. Scope and provenance

The proof uses Pauli orthogonality, compression inertia, a three-dimensional
determinant identity, a Rayleigh quotient, and elementary eigenvalue trace
inequalities. The exact seed interpretation and entropy target are supplied
by the [normalized-seed reduction](COLLECTIVE_ENCODING_REDUCTION.md) and
[entropy-rate characterization](ENTROPY_RATE_CHARACTERIZATION.md).
No new general fidelity theorem or publication novelty is asserted.

These results exclude every supported eigenbasis for certain nonuniform
rank-three spectra and exclude every seed with a maximally entangled
kernel from exceeding the classical contrast threshold. They complement
the [low-rank neighborhood theorem](LOW_RANK_ENTROPY_STABILITY.md), but
these two results have not been shown to cover every rank-three state.
The general two-qubit entropy inequality, and the separate three-input,
two-retained-qubit finite-budget problem, remain unresolved.

All conditions here refer to candidate seed Gram matrices. The physical
model continues to allow one arbitrary unknown quantum specimen, one
delayed query, unrestricted collective encoding, unlimited finite classical
records, worst-case quantum dimension, and uniform arbitrary-input error.
