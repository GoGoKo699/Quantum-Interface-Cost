# A sharp spectral-layer comparison for the original query score

Research base: `26a126a729fb483897c8a2e356dc733089c0d2a0` (PR #54).
Status: derived below and independently reconstructed internally. This
note gives a dimension-independent stability statement for the original
trace-norm score. It does not prove the general retention or entropy
conjecture, and makes no publication-originality claim.

The [affinity-method limit](AFFINITY_METHOD_LIMIT.md) shows that replacing
the original score by its affinity surrogate cannot prove the conjectured
general rank bound. Its exact optimal-decoder gap nevertheless controls
a different operation: replacing a seed by its canonical convex mixture
of nested flat spectral seeds. The error has a sharp square-root bound,
without any minimum eigenvalue separation.

## 1. The spectral layers and the comparison theorem

Let rho be a density matrix of rank r on n input qubits. List its positive
eigenvalues with multiplicity as lambda_1 >= ... >= lambda_r > 0, put
lambda_{r+1}=0, and choose corresponding orthonormal eigenvectors. Let
P_k project onto the first k vectors. Define

$$
\sigma_k=\frac{P_k}{k},\qquad
w_k=k(\lambda_k-\lambda_{k+1}).
\tag{1}
$$

Then w_k >= 0, sum_k w_k=1, and rho=sum_k w_k sigma_k. Choices inside
a degenerate eigenspace do not affect this mixture, because the weights
at cuts through that eigenspace vanish. Every constituent has rank at
most r. This is a spectral decomposition used in an inequality, with
no modification of the one-specimen operational model.

For an original query U in {X_i,Z_i}, write S=sqrt(rho), P=supp(rho),
B=PUP on ran(P), and

$$
F_U=\|SBS\|_1,\quad
a_U=\operatorname{Tr}(SBSB),\quad
\delta_U=a_U-F_U^2.
\tag{2}
$$

Choose a Hermitian unitary extension J_U of sign(SBS), including its
zero eigenspace, and set b_U=Tr(SJ_USJ_U). The previously proved gap
identity gives

$$
0<b_U\le1,\qquad F_U^2\le a_U b_U,\qquad
1-b_U=\frac12\|[S,J_U]\|_2^2.
\tag{3}
$$

**Theorem.** For every original query, its loss under the spectral-layer
mixture satisfies

$$
\boxed{
0\le d_U:=F_U(\rho)-\sum_k w_k F_U(\sigma_k)
\le\sqrt{2a_U(1-b_U)}\le\sqrt{2\delta_U}.}
\tag{4}
$$

Consequently, with g(rho)=sum_U F_U(rho),
E=sum_U a_U(1-b_U), and Delta=sum_U delta_U,

$$
\sum_U d_U^2\le2E\le2\Delta,\qquad
0\le g(\rho)-\sum_k w_k g(\sigma_k)
\le2\sqrt{nE}\le2\sqrt{n\Delta}.
\tag{5}
$$

The constants and square-root order in (4) and (5) are sharp, already
for one input qubit. No eigenvalue gap, condition number, or ambient
dimension appears beyond the explicit number of queries. In particular,
the mean score loss is at most sqrt(2 times the mean delta_U). The
comparison uses the original trace norms on both sides, not an affinity
objective for the flat seeds.

## 2. Proof

All matrices in the proof act on ran(P), where S is invertible. First,
define A_k=sqrt(lambda_k-lambda_{k+1}) P_k S^{-1}. They satisfy
sum_k A_k^* A_k=P. For every Hermitian H, positivity and the decomposition
of H into its positive and negative parts give

$$
\sum_k\|A_k H A_k^*\|_1
\le\sum_k\operatorname{Tr}(A_k|H|A_k^*)
=\|H\|_1.
\tag{6}
$$

Taking H=SBS yields A_kHA_k^*=(lambda_k-lambda_{k+1})P_kBP_k.
Since w_k F_U(sigma_k)=(lambda_k-lambda_{k+1})||P_kBP_k||_1,
(6) proves d_U >= 0. This is also an instance of root-fidelity joint
concavity; (6) supplies a direct proof for the present comparison.

For the upper bound, omit the query subscript and use the optimal J in
(3). Let s_i=sqrt(lambda_i), so S is diagonal in the chosen eigenbasis.
The compression P_kJP_k is a Hermitian contraction, and trace-norm
duality therefore gives

$$
\sum_k w_kF_U(\sigma_k)
\ge L:=\sum_k(\lambda_k-\lambda_{k+1})
\operatorname{Tr}(P_kBP_kJ).
\tag{7}
$$

For indices i,j, summing the layer weights in (7) gives
sum_{k>=max(i,j)}(lambda_k-lambda_{k+1})=min(lambda_i,lambda_j).
Thus, using F=Tr(SBSJ),

$$
F-L=\sum_{i,j}
\bigl(s_i s_j-\min(s_i^2,s_j^2)\bigr)B_{ij}J_{ji}
=\sum_{i,j}\min(s_i,s_j)|s_i-s_j|B_{ij}J_{ji}.
\tag{8}
$$

This expression is real; applying complex Cauchy--Schwarz to its
absolute value gives

$$
\begin{aligned}
|F-L|^2
&\le\left(\sum_{i,j}\min(s_i,s_j)^2|B_{ij}|^2\right)
\left(\sum_{i,j}(s_i-s_j)^2|J_{ij}|^2\right)\\
&\le\left(\sum_{i,j}s_i s_j|B_{ij}|^2\right)
\|[S,J]\|_2^2
=2a(1-b).
\end{aligned}
\tag{9}
$$

Equations (7)--(9) imply d_U<=sqrt(2a_U(1-b_U)). By (3),
delta_U=a_U-F_U^2>=a_U(1-b_U), completing (4). Summing its squares
and applying Cauchy--Schwarz over the 2n original queries proves (5).
Queries with B=0 have a_U=F_U=d_U=0 and require no separate limit.

Keeping the first factor of (9) gives the sharper finite estimate

$$
c_U:=\sum_k w_k a_U(\sigma_k)
=\sum_{i,j}\min(\lambda_i,\lambda_j)|B_{ij}|^2\le a_U,
\qquad d_U^2\le2c_U(1-b_U).
\tag{9a}
$$

The same proof gives the weighted version. For any nonnegative query
weights omega_U,

$$
0\le\sum_U \omega_U F_U(\rho)
-\sum_k w_k\sum_U \omega_U F_U(\sigma_k)
\le\sum_U \omega_U\sqrt{2\delta_U}
\le\sqrt{2\Bigl(\sum_U \omega_U\Bigr)
\Bigl(\sum_U \omega_U\delta_U\Bigr)}.
\tag{10}
$$

## 3. Sharpness at one qubit

For 0<epsilon<1/2, take
rho_epsilon=(I+2 epsilon Y)/2 and t=sqrt(1-4 epsilon^2). Its spectral
layers are sigma_1=|Y+><Y+| and sigma_2=I/2, with weights
w_1=2 epsilon and w_2=1-2 epsilon. Both original queries U=X,Z obey

$$
F_U(\rho_\epsilon)=a_U=b_U=t,\qquad
\delta_U=t(1-t),\qquad
\sum_k w_k F_U(\sigma_k)=1-2\epsilon.
\tag{11}
$$

Indeed, U interchanges the two Y eigenvectors, and SBS is
(t/2)U in that eigenbasis. Hence the optimal J equals U; the weighted
Cauchy residual in the exact gap identity vanishes. The deficit is
d_U=t-1+2 epsilon, so

$$
\lim_{\epsilon\downarrow0}
\frac{d_U}{\sqrt{2\delta_U}}=1,\qquad
\lim_{\epsilon\downarrow0}
\frac{g(\rho_\epsilon)-\sum_k w_k g(\sigma_k)}
{2\sqrt{\Delta}}=1.
\tag{12}
$$

In this family c_U=1-2 epsilon and
d_U^2=2c_U(1-b_U) exactly for every epsilon in (0,1/2), so the
refined finite estimate (9a) is attained throughout the family.

The numerator in the first ratio is 2 epsilon+O(epsilon^2), and
delta_U=2 epsilon^2+O(epsilon^4). Thus neither the coefficient in (4)
nor the square-root dependence can be improved uniformly. The second
ratio shows simultaneous sharpness for the full original workload.
Equivalently, the exact rational parametrization
epsilon=v/(1+v^2), 0<v<1, gives t=(1-v^2)/(1+v^2) and

$$
\frac{d_U^2}{2\delta_U}=\frac{1-v}{1+v}\longrightarrow1
\quad\text{as }v\downarrow0.
\tag{12a}
$$

These states satisfy the already established one-qubit converse; the
example concerns the error of the spectral-layer comparison.

## 4. What transfers from flat seeds

Let M_n(r) be the supremum of g(Q/rank(Q)) over nonzero orthogonal
projectors Q of rank at most r. Equation (5) immediately gives

$$
g(\rho)\le M_n(r)+2\sqrt{n\Delta}.
\tag{13}
$$

Thus a seed with a small total fidelity--affinity gap is close in score
to a convex mixture of flat seeds obeying its original rank cap. This
is not a comparison with the single flat state P/r on the same support;
that replacement need not preserve or increase the score.

There is also a conditional entropy transfer. Put c=2-sqrt(2). If the
sharp flat-seed inequality g(Q/rank(Q))<=sqrt(2)n+c log_2 rank(Q)
holds for every projector of rank at most r, then

$$
g(\rho)\le\sqrt2\,n+c\sum_k w_k\log_2 k+2\sqrt{n\Delta}
\le\sqrt2\,n+cS(\rho)+2\sqrt{n\Delta}.
\tag{14}
$$

For the last step, choose K with probabilities w_k and then choose I
uniformly from {1,...,K}. Its marginal is Pr(I=i)=lambda_i, so the
elementary inequality H(I)>=H(I|K) gives
S(rho)>=sum_k w_k log_2 k. Also S(rho)<=log_2 r.

The flat-seed hypothesis in (14) is not established for arbitrary n,r,
and the positive error term remains even when that hypothesis is
available. Therefore this theorem does not prove the unrestricted rank
or entropy conjecture. The stability estimate stays uniform when
distinct eigenvalues approach one another.

## 5. Prior ingredients and verification scope

Spectral threshold decompositions and dimension-independent rounding
from commutators have established precedents. Vidick,
[arXiv:2103.02468v3](https://arxiv.org/pdf/2103.02468v3), Section 2.4,
printed p. 10, Lemmas 2.11--2.12, records the threshold integral and a
Frobenius-norm spectral-projection comparison. He attributes these
ingredients to Connes and to Slofstra--Vidick,
[arXiv:1711.10676v2](https://arxiv.org/pdf/1711.10676v2), printed
pp. 20--21, Lemmas 5.5--5.6. Vidick's Theorem 3.1 is a more general
flat-strategy rounding theorem. These sources supply the established
methodological context; no claim that spectral layering or
dimension-independent rounding is new is made here.

The present proof evaluates the nested-layer loss for the fixed
original trace-norm query profile, using the exact optimal-decoder
gap from [the preceding note](AFFINITY_METHOD_LIMIT.md), Section 3.
The finite eigenbasis calculation (8)--(9), the weighted and entropy
consequences, and the sharp example (11)--(12a) were reconstructed
independently within this workspace. This is not external peer review.
Bounded matrix checks are diagnostics of these formulas, not a
replacement for the quantified proof or an originality audit.

The [checker](../../tools/check_spectral_layer_score_bound.py) verifies
the layer identities, query and aggregate bounds, degeneracies, zero
query compressions, and exact rational sharpness instances:

```sh
python tools/check_spectral_layer_score_bound.py --output results/spectral_layer_score_bound.json
```

The [result record](../../results/spectral_layer_score_bound.json) pins
the checker and proof-note hashes. Its matrices have dimension at most
16; no search or numerical optimization enters the argument.
