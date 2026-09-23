# An entropy bound for product-diagonal seeds

Date: 2026-09-22. Research base: `df45e2eaceb5669cfff9ac063d3da845d622dac3`.
Status: supplied analytical deduction, independently checked within this
workspace; publication novelty not certified.

The subsequent [profile-rate theorem](PRODUCT_DIAGONAL_PROFILE_RATE.md)
evaluates the full two-parameter asymptotic rate for this Gram family.
It recovers the common-accuracy subset bound below and identifies precisely
where unequal X/Z accuracies permit a lower rate than original-site retention.
Both results keep the unrestricted encoder problem separate from this family.

This note proves a restricted-family bound inside the unrestricted
[normalized-seed formulation](COLLECTIVE_ENCODING_REDUCTION.md). It does
not restrict the operational problem, prove the unrestricted candidate
inequality, or assume that an optimal collective encoder belongs to this
family. Here "product-diagonal" means diagonal in a **fixed tensor product
of one-qubit bases**. A generic matrix has an eigenbasis, but an entangled
eigenbasis is outside this condition.

## 1. Statement

Let L be a complex D-by-2^n matrix with Tr(L^dagger L)=1, and put

$$
\rho=L^\dagger L,\qquad
g(L)=\sum_{i=1}^n
\bigl(\|L X_iL^\dagger\|_1+\|L Z_iL^\dagger\|_1\bigr).
$$

Logarithms and entropies are in bits. Suppose rho is diagonal in the product
eigenbasis of the local bisectors B_i=(X_i+Z_i)/sqrt(2). Then

$$
\boxed{g(L)\le\sqrt2\,n+(2-\sqrt2)S(\rho).}
\tag{1}
$$

The eigenvalues of rho may have arbitrary correlations and zeros. They do
not have to factorize or be uniform. L itself need not be real, square,
positive, an isometry, or a tensor product.

Since S(rho)<=log_2 rank(rho)<=log_2 D, this gives

$$
g(L)\le\sqrt2\,n+(2-\sqrt2)\log_2 D.
\tag{2}
$$

Section 5 extends (1) to any fixed tensor product of one-qubit bases. It
still makes no claim for a general collective seed.

## 2. A single-bit inequality

For every 0<=lambda<=1,

$$
\sqrt{1+4\lambda(1-\lambda)}
\le 1+(\sqrt2-1)h_2(\lambda).
\tag{3}
$$

Equality holds for lambda=0, 1/2, 1. To prove this, symmetry lets us take
lambda=(1-t)/2 with 0<=t<=1. Define

$$
F(t)=h_2\!\left(\frac{1-t}{2}\right)
-\frac{\sqrt{2-t^2}-1}{\sqrt2-1}.
$$

Both endpoint values are zero. For 0<t<1, its derivative has the sign of
K-H(t), where

$$
K=\frac{\ln2}{\sqrt2-1},\qquad
H(t)=\frac{\sqrt{2-t^2}}{t}\operatorname{atanh}t.
$$

In detail,

$$
F'(t)=\frac{t}{\ln2\sqrt{2-t^2}}\bigl(K-H(t)\bigr).
$$

The derivative H'(t) is strictly positive exactly when

$$
J(t):=\frac{t(2-t^2)}{1-t^2}-2\operatorname{atanh}t>0.
$$

This follows from J(0)=0 and

$$
J'(t)=\frac{t^2+t^4}{(1-t^2)^2}>0.
$$

Moreover, H(0+)=sqrt(2)<K and H(1-)=infinity. Thus F' changes sign
exactly once, from positive to negative. With both endpoint values zero,
F is nonnegative and is strictly positive in the interior. This proves
(3), with equality only at the three stated values of lambda.

## 3. Reduction to classical edges

The polar decomposition L=V sqrt(rho), with V a partial isometry, gives

$$
\|L P L^\dagger\|_1
=\|\sqrt\rho\,P\sqrt\rho\|_1
\tag{4}
$$

for every Hermitian P: the operator on the right is supported on the initial
space of V, where V preserves its nonzero singular values.

Write

$$
\rho=\sum_{x\in\{0,1\}^n}p(x)|x_B\rangle\langle x_B|
$$

in the product bisector basis. Fix i and all other coordinates y=x_-i.
Let p=p(0,y), r=p(1,y), w=p+r. In this two-dimensional block the matrices
sqrt(rho) X_i sqrt(rho) and sqrt(rho) Z_i sqrt(rho) have the forms

$$
\frac1{\sqrt2}
\begin{pmatrix}p&\sqrt{pr}\\\sqrt{pr}&-r\end{pmatrix},
\qquad
\frac1{\sqrt2}
\begin{pmatrix}p&-\sqrt{pr}\\-\sqrt{pr}&-r\end{pmatrix},
$$

up to an irrelevant exchange of signs or axes. Their determinants are -pr
and their traces are (p-r)/sqrt(2). Each trace norm is consequently

$$
\frac1{\sqrt2}\sqrt{(p+r)^2+4pr}.
$$

The formula also holds when p or r vanishes. If w>0, set lambda_y=p/w;
blocks with w=0 contribute zero. Additivity of trace norm on orthogonal
blocks gives the exact site score

$$
g_i(L)=\sqrt2\sum_y w_y
\sqrt{1+4\lambda_y(1-\lambda_y)}.
\tag{5}
$$

Using (3) in each block, and interpreting p(x) as the probability law of
classical variables U_1,...,U_n, gives

$$
g_i(L)\le\sqrt2+(2-\sqrt2)H(U_i\mid U_{-i}).
\tag{6}
$$

These variables label a spectral decomposition used in the proof. This is
not an assumption that the physical input specimen is classical.

## 4. Entropy tensorization and equality

Conditioning reduces classical entropy, so, for the fixed ordering 1,...,n,

$$
\sum_{i=1}^n H(U_i\mid U_{-i})
\le\sum_{i=1}^n H(U_i\mid U_1,...,U_{i-1})
=H(U_1,...,U_n)=S(\rho).
\tag{7}
$$

Combining (6) and (7) proves (1). Zero probabilities cause no problem;
conditional terms on zero-probability events are assigned weight zero.

For any integer 0<=q<=n, choose

$$
\rho=(I/2)^{\otimes q}\otimes
\bigl(|0_B\rangle\langle0_B|\bigr)^{\otimes(n-q)}.
$$

Its entropy is q, its rank is 2^q, and its site scores are 2 at each mixed
factor and sqrt(2) at each pure bisector factor. Thus

$$
g(L)=2q+\sqrt2(n-q)
$$

for a seed with this Gram matrix. The Pauli-orbit completion and symmetry
equalization in the seed-reduction note turn it into a deterministic
interface with uniform contrast

$$
\eta=\frac1{\sqrt2}
+\frac qn\left(1-\frac1{\sqrt2}\right).
$$

Hence the subset benchmark is optimal within the product-diagonal seed
family when D=2^q. This conclusion is about that family, not unrestricted
encoders.

## 5. Extension to arbitrary local product bases

Suppose instead that rho is diagonal in the product eigenbasis of
N_i=nu_i dot (X_i,Y_i,Z_i), with each nu_i a real unit vector. The eigenvalue
law p(x) and the conditional entropies in (7) are unchanged.

For a local Pauli P and an edge with weights p,r, let a be its diagonal
coefficient in this basis: a=nu_i dot e_P. The off-diagonal coefficient of
P has squared modulus 1-a^2. Thus the corresponding edge matrix has trace
a(p-r), determinant -pr, and trace norm

$$
\sqrt{4pr+(p-r)^2a^2}.
$$

Put a=nu_i dot e_X and b=nu_i dot e_Z. Since a^2+b^2<=1, concavity and
monotonicity of the square root give

$$
\begin{aligned}
&\sqrt{4pr+(p-r)^2a^2}
+\sqrt{4pr+(p-r)^2b^2}\\
&\quad\le
2\sqrt{4pr+\frac12(p-r)^2}
=\sqrt2\sqrt{(p+r)^2+4pr}.
\end{aligned}
$$

Therefore (5) becomes an upper bound, and the rest of the proof applies
unchanged. Arbitrary correlations among eigenvalues and arbitrary choices
of the individual local bases still cannot improve the subset benchmark.

The condition is stronger than separability: a separable state need not be
diagonal in one fixed local product basis. No result for all separable Gram
matrices, or all Gram matrices, is proved here.

## 6. An obstruction to a tempting unrestricted proof

For a pure vectorization of L on R_1...R_n Q, one might try to establish
the single-site inequality

$$
\|\operatorname{Tr}_A(X_A\sigma_{AB})\|_1
+\|\operatorname{Tr}_A(Z_A\sigma_{AB})\|_1
\stackrel{?}{\le}
\sqrt2-(2-\sqrt2)H(A\mid B)_\sigma,
\tag{8}
$$

then use entropy duality and strong subadditivity to sum it. Equation (8)
is false even when A and B are qubits. Consider

$$
\sigma_{AB}=\frac45|\Phi^+\rangle\langle\Phi^+|
+\frac15\frac{I_{AB}}4.
$$

The two trace norms on the left are both 4/5. The state has eigenvalues
17/20,1/20,1/20,1/20 and a maximally mixed B marginal, so

$$
H(A\mid B)=H(17/20,1/20,1/20,1/20)-1
\simeq-0.15241532.
$$

The right-hand side of (8) is approximately 1.50350, strictly below the
left-hand side 1.6. This counterexample rules out that local
conditional-entropy route. It does **not** refute an unrestricted global
bound of the form (1): in a purification, the other reference sites may
contribute compensating deficits.

## 7. Scope of the deduction

The proof uses elementary trace-norm algebra, the explicitly proved
single-bit inequality, and the classical entropy chain rule. The
seed-to-interface step invokes the separately stated normalized-seed
reduction. This note supplies an analytical exclusion of a broad structured
family; a literature audit of this restricted bound is still required.

In particular, correlated spectra, arbitrary local basis rotations, and
Schmidt-typical truncations that preserve a product eigenbasis cannot
produce a collective advantage over the hybrid line. A possible advantage
must use Gram matrices outside this class. The unrestricted rate and
unrestricted entropy inequality remain unresolved.

`tools/check_product_diagonal_bound.py` compares full-matrix trace norms with
the edge formulas in ten finite cases, including correlated spectra, zero
eigenvalues, and local bases with Y components. The recorded output is
`results/product_diagonal_bound.json`; these diagnostics are not a proof of
the general statement or a numerical search over unrestricted encoders.
