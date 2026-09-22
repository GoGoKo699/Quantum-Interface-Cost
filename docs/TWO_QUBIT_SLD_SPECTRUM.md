# Exact two-qubit SLD minimum at a fixed spectrum

Date: 2026-09-22. Research base:
`f761bbca3ba3c1b263a1914175e3bdab94be70a7`.
Status: derived with a complete supplied proof and primary-source comparisons.
Publication novelty remains unresolved. The result concerns every two-qubit
density matrix, including singular states and entangled eigenbases.

## 1. Statement and normalization

For a density matrix rho with eigenvalues lambda_a and a Hermitian operator
P, use the normalization from the [SLD-route audit](SLD_ENTROPY_ROUTE_AUDIT.md):

$$
I_\rho(P)=\frac12\sum_{a,b}k(\lambda_a,\lambda_b)
|\langle a|P|b\rangle|^2,
\qquad
k(x,y)=\begin{cases}(x-y)^2/(x+y),&x+y>0,\\0,&x=y=0.
\end{cases}
\tag{1}
$$

This is one quarter of the usual SLD quantum Fisher information for the
unitary generator P. Entropies are in bits. For two input qubits define

$$
\mathcal I_{XZ}(\rho)=\sum_{i=1}^2
[I_\rho(X_i)+I_\rho(Z_i)],\qquad
J(\rho)=\frac12\sum_{i=1}^2\sum_{P=X,Y,Z}I_\rho(P_i).
\tag{2}
$$

Order the four eigenvalues as
`lambda_1 >= lambda_2 >= lambda_3 >= lambda_4 >= 0`, with sum one, and put
`k_ab=k(lambda_a,lambda_b)`. Then

$$
\boxed{
\min_{U\in U(4)}J(U\operatorname{diag}(\lambda)U^\dagger)
=\min_{U\in U(4)}\mathcal I_{XZ}
(U\operatorname{diag}(\lambda)U^\dagger)
=E_*(\lambda):=k_{12}+k_{13}+k_{24}+k_{34}.
}
\tag{3}
$$

Both minima are attained by the diagonal state with the ordered eigenvalues
placed on `|00>, |01>, |10>, |11>` in that order. In particular, every
two-qubit state obeys

$$
\boxed{\mathcal I_{XZ}(\rho)\ge J(\rho)
\ge E_*(\lambda)\ge 2-S(\rho).}
\tag{4}
$$

The state is unrestricted: the diagonal state is an attainer of the
optimization, not an assumption in its converse. Equation (4) proves the
two-qubit case of the SLD entropy candidate. It does not establish the
all-n candidate or the sharper linear seed-entropy conjecture.

## 2. Spin flip determines the six-Pauli transition weights

All transposes and complex conjugates below use the computational basis.
For a two-by-two matrix A,

$$
Y A^T Y=(\operatorname{Tr}A)I-A.
\tag{5}
$$

Applying this identity on both tensor factors, with `V=Y tensor Y`, gives
the established two-qubit inversion formula

$$
\widetilde\sigma:=V\overline\sigma V
=I-\sigma_A\otimes I-I\otimes\sigma_B+\sigma
\tag{6}
$$

for a density matrix sigma. For a pure state `sigma=|b><b|`, define
`|tilde b>=V|bar b>`, so that `tilde sigma=|tilde b><tilde b|`.
The local Pauli-twirl identities yield

$$
\begin{aligned}
\sum_{P=X,Y,Z}P_1\sigma P_1&=2I\otimes\sigma_B-\sigma,\\
\sum_{P=X,Y,Z}P_2\sigma P_2&=2\sigma_A\otimes I-\sigma.
\end{aligned}
$$

Adding and substituting (6) proves

$$
\sum_{i=1}^2\sum_{P=X,Y,Z}P_i|b\rangle\langle b|P_i
=2(I-|\widetilde b\rangle\langle\widetilde b|).
\tag{7}
$$

Let U have the four eigenvectors `|a>` as its columns, including any
zero-eigenvalue vectors, and set

$$
K=U^\dagger V\overline U,\qquad B_{ab}=|K_{ab}|^2.
\tag{8}
$$

Since V is symmetric and unitary, K is symmetric and unitary. Thus B is
symmetric, entrywise nonnegative and doubly stochastic. Taking a diagonal
matrix element of (7) in `|a>` gives the exact transition formula

$$
W^{XYZ}_{ab}:=\sum_{i=1}^2\sum_{P=X,Y,Z}
|\langle a|P_i|b\rangle|^2=2(1-B_{ab}).
\tag{9}
$$

Here the number 1 on the right occurs for every entry, including a=b;
it is not a Kronecker delta. Consequently (1) and (2) give

$$
J(\rho)=\frac14\sum_{a,b}k_{ab}W^{XYZ}_{ab}
=\sum_{a<b}k_{ab}-\frac12\sum_{a,b}k_{ab}B_{ab}.
\tag{10}
$$

The factor one quarter includes both the SLD normalization and the
one-half in the definition of J. Formula (10) is the additional
two-qubit structure that is absent from a generic spectral graph.

## 3. The assignment maximum and exact attainer

For x,y>0 direct differentiation gives

$$
\frac{\partial^2 k}{\partial x\partial y}(x,y)
=-\frac{8xy}{(x+y)^3}\le0.
\tag{11}
$$

Integrating over a rectangle with `x>=x'` and `y>=y'` proves

$$
k(x,y)+k(x',y')\le k(x,y')+k(x',y).
\tag{12}
$$

Continuity extends this to nonnegative arguments, including the origin,
because `0<=k(x,y)<=x+y`. This kernel ordering is an established
ingredient; Section 6 identifies its explicit appearance in prior work.

For a permutation pi, consider `sum_a k(lambda_a,lambda_pi(a))`.
If `a<b` and `pi(a)<pi(b)`, swapping these two images cannot decrease the
sum, by (12). Repeated swaps sort the images into descending index order,
giving the reversal `pi(a)=5-a`. Thus

$$
\max_\pi\sum_a k_{a,\pi(a)}=2(k_{14}+k_{23}).
\tag{13}
$$

Every doubly stochastic matrix is a convex combination of permutation
matrices. Applying (13) to each term gives

$$
\sum_{a,b}k_{ab}B_{ab}\le2(k_{14}+k_{23}).
\tag{14}
$$

Substituting (14) into (10) proves `J(rho)>=E_*(lambda)`. Relaxing B to
all doubly stochastic matrices causes no loss here. For the ordered
computational product eigenbasis, spin flip exchanges `00<->11` and
`01<->10`, up to phases. Its B is precisely the reversal permutation,
so it attains (14).

To pass from J to the actual X/Z sum, the [SLD-route audit](SLD_ENTROPY_ROUTE_AUDIT.md),
Section 5, supplies the following identity for arbitrary density matrices.
For completeness, let `f_t=rho exp(-t rho)`. Spectral integration gives

$$
\int_0^\infty(ae^{-ta}-be^{-tb})^2\,dt
=\frac{(a-b)^2}{2(a+b)},\qquad
I_\rho(P)=\int_0^\infty\|[f_t,P]\|_2^2\,dt,
\tag{15}
$$

with the zero-zero term interpreted as zero. Write
`f_t=sum_w f_w(t) sigma_w` in the Pauli-word basis on d=4 dimensions,
using the unnormalized Hilbert--Schmidt norm. Pauli orthogonality gives

$$
\|[f_t,X_i]\|_2^2+\|[f_t,Z_i]\|_2^2-\|[f_t,Y_i]\|_2^2
=8d\sum_{w:w_i=Y}|f_w(t)|^2\ge0.
\tag{16}
$$

After integration and summation, (16) is exactly
`mathcal I_XZ(rho)>=J(rho)`. Singular spectra are covered directly by
the finite spectral sum in (15).

Finally, on the ordered diagonal state, both Z terms vanish. The X_1
transitions join 1 to 3 and 2 to 4; X_2 joins 1 to 2 and 3 to 4.
Their total information is E_*. Each Y term has the same transition
magnitudes as its corresponding X term. Thus `J=mathcal I_XZ=E_*` there,
completing both exact minimizations in (3).

## 4. Entropy consequence for every two-qubit state

The elementary binary inequality needed here is

$$
1-h_2(p)\le(2p-1)^2,\qquad 0\le p\le1.
\tag{17}
$$

One proof puts `t=2p-1` and expands

$$
1-h_2((1+t)/2)=\frac1{\ln2}
\sum_{m=1}^\infty\frac{t^{2m}}{(2m)(2m-1)}.
\tag{18}
$$

All coefficients are nonnegative and their sum is one, as follows by
evaluating at t=1. Since `t^(2m)<=t^2` for `|t|<=1`, (17) follows,
including the endpoints by continuity. Hence, for a,b>=0,

$$
k(a,b)\ge(a+b)\left[1-h_2\!\left(\frac a{a+b}\right)\right],
\tag{19}
$$

where a zero-weight pair contributes zero.

Regard the ordered eigenvalues as the classical distribution
`p_00=lambda_1`, `p_01=lambda_2`, `p_10=lambda_3`, `p_11=lambda_4` of
two binary variables A,B. Applying (19) to the horizontal and vertical
pairs gives

$$
\begin{aligned}
k_{12}+k_{34}&\ge1-H(B\mid A),\\
k_{13}+k_{24}&\ge1-H(A\mid B).
\end{aligned}
\tag{20}
$$

Classical subadditivity gives
`H(A|B)+H(B|A)=2H(A,B)-H(A)-H(B)<=H(A,B)`. Therefore

$$
E_*(\lambda)\ge2-H(A\mid B)-H(B\mid A)
\ge2-H(\lambda)=2-S(\rho).
\tag{21}
$$

The use of a classical distribution in this step is a scalar spectral
calculation. The preceding eigenbasis minimization makes (21) apply to
all two-qubit states, without assuming a classical physical input.

For comparison, the one-qubit case is immediate as well. If r is the
Bloch-vector length, then `I(X)+I(Z)=r^2+r_y^2>=r^2`, and (17) gives
`r^2>=1-h_2((1+r)/2)=1-S(rho)`. Thus the global SLD entropy candidate
is established for n<=2. No tensorization to higher n is supplied.

## 5. What this proves for interface seeds

For a normalized seed Gram matrix rho, define

$$
F_P=\|\sqrt\rho P\sqrt\rho\|_1,\qquad
g(\sqrt\rho)=\sum_{i=1}^2(F_{X_i}+F_{Z_i}).
$$

The already proved [trace-norm/SLD estimate](SPECTRAL_CONDITION_ENTROPY_BOUND.md)
is `F_P^2<=1-I_rho(P)`. Cauchy--Schwarz and (3)--(4) therefore imply

$$
\boxed{g(\sqrt\rho)\le2\sqrt{4-E_*(\lambda)}
\le2\sqrt{2+S(\rho)}.}
\tag{22}
$$

This is a spectrum-dependent seed bound with a weaker entropy-only
consequence. It does not prove the sharp target

$$
g(\sqrt\rho)\stackrel{?}{\le}
2\sqrt2+(2-\sqrt2)S(\rho).
\tag{23}
$$

Indeed, the square-root curve in (22) is strictly above the line in
(23) for `0<S<2`: the line is its chord between S=0 and S=2. Equation
(22) may be useful as a separate certificate for individual spectra,
but cannot be substituted for (23).

The exact n=2,q=1 operational optimum was already established by the
[all-n one-qubit theorem](ONE_QUBIT_OPTIMALITY.md). The present result
does not improve that memory value or evaluate the unrestricted
asymptotic rate. An all-n SLD entropy bound is still missing, as is the
sharp linear entropy bound for the remaining two-qubit spectra and
eigenbases.

These are inequalities on virtual normalized seeds in the existing
operational reduction. The physical model continues to use one arbitrary
unknown specimen, one delayed local X/Z query, arbitrary collective
encoding, unlimited finite classical records, worst-case quantum
dimension, and error uniform over all inputs and queries. There is no
many-copy estimation, average-memory or postselection assumption.

## 6. Primary-source comparison and novelty boundary

The following comparisons were checked in the identified primary versions.
They separate established ingredients from the supplied deductions;
they are not a literature-wide originality certificate.

**Spin flip and inversion are established.** Wootters,
[quant-ph/9709029v2](https://arxiv.org/pdf/quant-ph/9709029v2),
13 September 1997, Eqs. (4)--(5), printed p. 3, defines the spin flip used
in (6)--(8). Rungta, Buzek, Caves, Hillery and Milburn,
[quant-ph/0102040v2](https://arxiv.org/pdf/quant-ph/0102040v2),
10 June 2001, Eq. (2.11), printed p. 7, gives the bipartite universal
inversion formula. Setting its normalization factors to one and its
local dimensions to two gives (6). Equation (7) is its direct combination
with the local Pauli twirl, not a new inversion theorem.

**The spectral kernel ordering also has explicit prior art.** Fiderer,
Fraisse and Braun, [1905.06101v2](https://arxiv.org/pdf/1905.06101v2),
27 December 2019, Supplemental Lemma 3 and its proof, Eqs. (16)--(17),
printed p. 8, establish the ordered four-eigenvalue crossing inequality
for this same kernel. Our derivative proof (11)--(12) is another
elementary route to that ingredient. Their Theorem 1, Eq. (3), printed
p. 2, maximizes QFI for one fixed generator over a state's unitary orbit.
Their QFI is four times (1). Specializing the generator spectrum to
`(1,1,-1,-1)` gives `max I=k_14+k_23`. Our optimization minimizes the
sum for the fixed noncommuting local generators. The additional step is
the spin-flip identity (10), which converts the local-sum minimum into
the assignment maximum, followed by the simultaneous product-basis
attainer. Neither general fixed-spectrum QFI optimization nor the
kernel ordering should be presented as new.

**A local-QFI discord minimization is a different quantity.** Kim, Li,
Kumar and Wu, [1711.02323v5](https://arxiv.org/pdf/1711.02323v5),
19 March 2018, Eq. (6), printed p. 2, uses the normalization (1).
Section III.A's definition immediately before Theorem 1, printed p. 3,
minimizes a sum over one party's orthonormal rank-one projectors while
holding the bipartite state fixed. Equation (3) here varies the global
eigenbasis at fixed spectrum and keeps the local X/Z or X/Y/Z queries
fixed. These are not the same minimization: their quantity vanishes on
a pure product state, whereas our minimum at a pure spectrum is two.

The supplied deductions are the exact two-qubit local-sum envelope (3)
and its entropy consequence (4), with the limitations in Section 5.
These comparisons identify overlapping methods and distinguish the
inspected theorem statements. Further subsumption by a prior local-sum
or uncertainty theorem remains a publication-novelty question.
