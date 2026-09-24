# A sharp purity bound for spin-flip invariant seeds

Date: 24 September 2026. Reviewed main:
`e97d0d4a164c73c8ce1d945febadc1d267c0b6d5`.

**Verdict.** A supplied sum-of-squares proof controls every nonuniform
rank-at-most-four three-qubit seed invariant under global spin flip.
The bound is sharp at every allowed purity. It also proves the exact
uniform score `2sqrt(6)` for four-dimensional readouts sharing a common
odd antiunitary of square -I. Independent internal reconstructions checked
both statements. General balanced readouts and unrestricted `Gamma(3,4)`
remain open; publication originality is not asserted.

The symmetry is a condition on this class of seeds or readouts, not an
assumption added to the interface model. Antiunitary transformations are
used algebraically; no physical spin-flip channel is introduced.

## 1. Statement

Let `Theta=(Y tensor Y tensor Y)K`, where K is computational complex
conjugation. It has `Theta^2=-I` and negates every local Pauli under
conjugation. For a normalized density matrix rho define

$$
f_U(\rho)=\|\sqrt\rho\,U\sqrt\rho\|_1
=F_{\rm root}(\rho,U\rho U),\qquad
\mathcal F(\rho)=\sum_{i=1}^3\sum_{U=X_i,Z_i}f_U(\rho)^2.
$$

**Theorem.** If `rank(rho)<=4` and `Theta rho Theta^-1=rho`, then

$$
\boxed{\mathcal F(\rho)\le5-4\operatorname{Tr}\rho^2\le4.}
\tag{1}
$$

Every purity in `[1/4,1/2]` is possible and has an attaining state.
The six individual scores need not be equal in that construction.
Cauchy–Schwarz consequently gives the interface seed exclusion

$$
g(\rho)=\sum_U f_U(\rho)
\le\sqrt{6(5-4\operatorname{Tr}\rho^2)}
\le2\sqrt6<4+\sqrt2.
\tag{2}
$$

Thus an unrestricted three-input, two-qubit-memory advantage would
require a seed that breaks this symmetry. This is a necessary condition,
not a classification of every remaining witness.

## 2. The spectrum has one imbalance parameter

An antiunitary of square -I pairs orthogonal eigenvectors of any invariant
Hermitian operator. Every eigenspace of rho therefore has even dimension.
Choose an invariant rank-four projector P containing its support. There
is an invariant Hermitian S such that

$$
\rho_r=\frac{P+rS}{4},\quad -1\le r\le1,\qquad
S^2=P,\quad PS=SP=S,\quad\operatorname{Tr}S=0.
\tag{3}
$$

The eigenvalues on P are `(1+r)/4` twice and `(1-r)/4` twice. Rank-two
states are the endpoints, with an additional invariant pair completing P.
In particular `Tr(rho_r^2)=(1+r^2)/4`.

Put `R=2P-I`. Both R and S are traceless and spin-flip invariant. In three
qubits this means that their Pauli expansions contain only weight-two
words: invariance removes odd weights and tracelessness removes the
identity. Write

$$
R=\sum_w r_w W_w,\qquad S=\sum_w s_w W_w,
\qquad \operatorname{Tr}(W_vW_w)=8\delta_{vw}.
$$

Let `e_w` count Y factors in the weight-two word w, and define

$$
u=\sum_w e_w r_w^2,\qquad v=\sum_w e_w s_w^2.
\tag{4}
$$

These are nonnegative scalar quantities. No restriction to real matrices
or to Pauli words without Y is made.

## 3. The six-term score is exactly quadratic

On the four-dimensional range of P, set `K_U=PUP`. It is odd under the
restricted antiunitary, so its eigenvalues are `alpha,beta,-beta,-alpha`,
with `alpha,beta>=0`. The same pairing holds for
`C_U(r)=sqrt(rho_r) U sqrt(rho_r)` on P. Such a Hermitian matrix satisfies

$$
\|C\|_1^2=2\operatorname{Tr}C^2+8\sqrt{\det C}.
\tag{5}
$$

All determinants here are on P. Since `sqrt(det rho_r)=(1-r^2)/16`,

$$
f_U(\rho_r)^2=
\frac{\operatorname{Tr}K_U^2
+2r\operatorname{Tr}(S K_U^2)
+r^2\operatorname{Tr}(S K_U S K_U)}8
+\frac{1-r^2}{2}\sqrt{\det K_U}.
\tag{6}
$$

The identity includes singular compressions and the rank-two endpoints
by continuity. Hence `mathcal F(r)=F_0+b r+c r^2` exactly.

A weight-two word with `e_w` Y factors anticommutes with `2+e_w` of the
six queried Paulis. Define `V_R=sum_w e_w r_w W_w` and similarly V_S.
Then

$$
\sum_U U R U=2R-2V_R,\qquad
\sum_U U S U=2S-2V_S.
$$

Compression and Pauli orthogonality give

$$
\sum_U K_U^2=4P-PV_RP,\qquad
\sum_U\operatorname{Tr}K_U^2=16-4u,
$$

$$
\sum_U\operatorname{Tr}(S K_U S K_U)=8-16v.
$$

Writing `d=sum_U sqrt(det K_U)`, the coefficients in (6) are therefore

$$
F_0=2-u/2+d/2,\qquad b=-2\sum_w e_w r_w s_w,
\qquad c=3-F_0-u/2-2v.
\tag{7}
$$

At the flat point, four-dimensional Hilbert–Schmidt Cauchy–Schwarz gives

$$
F_0=\sum_U\frac{\|K_U\|_1^2}{16}
\le\frac14\sum_U\operatorname{Tr}K_U^2=4-u.
$$

Consequently `delta=4-F_0>=u`. Substitution into (7) gives the exact
certificate

$$
\boxed{
4-r^2-\mathcal F(\rho_r)
=\left(\delta-\frac u2\right)(1-r^2)
+2\sum_w e_w\left(r s_w+\frac{r_w}{2}\right)^2\ge0.}
\tag{8}
$$

This proves (1). It neither replaces a nonuniform spectrum by a flat one
nor invokes the conjectured entropy bound. The flat estimate controls a
coefficient of the full nonuniform polynomial.

## 4. Sharpness at every purity

Take the independent commuting Paulis

$$
A=X_1Z_2,\qquad B=X_1X_3,\qquad AB=Z_2X_3,
$$

and put `P=(I+A)/2`, `S=(B+AB)/2`. Then `S^2=P`, `PS=S`, and

$$
\rho_r=\frac{I+A+r(B+AB)}8
\tag{9}
$$

is an invariant density matrix with the spectrum in Section 2. Its scores
are

$$
f_{X_1}=f_{Z_2}=f_{X_3}=1,\qquad
f_{Z_1}=f_{X_2}=0,\qquad f_{Z_3}=\sqrt{1-r^2}.
$$

The zero scores follow from anticommutation with A. The three unit scores
follow from commuting with rho. Finally Z_3 preserves P and exchanges
the two eigenspaces of S. Thus `mathcal F=4-r^2`, proving sharpness at
every permitted purity.

## 5. A sharp continuous readout class

Suppose six four-dimensional reflection readouts share one antiunitary
`Theta_Q=U_Q K` satisfying

$$
\Theta_Q^2=-I,\qquad \Theta_Q B_U\Theta_Q^{-1}=-B_U.
\tag{10}
$$

They are automatically balanced: each has two positive and two negative
eigenvalues. No pairwise commute/anticommute hypothesis is imposed.
For every real weight vector w,

$$
\boxed{\left\|\sum_U w_U U\otimes B_U\right\|_\infty
\le2\left(\sum_Uw_U^2\right)^{1/2}.}
\tag{11}
$$

**Proof.** Write `Theta=U_R K`. The joint antiunitary
`T=(U_R tensor U_Q)K` has square +I and commutes with the Hamiltonian H
in (11). Choose a unit vector in an extremal eigenspace fixed by T;
every T-invariant eigenspace has such a vector. Its reference reduction
rho is invariant under Theta and has rank at most four. Schmidt
decomposition and trace-norm duality imply

$$
|\lambda|\le\sum_U|w_U|f_U(\rho)
\le\|w\|_2\sqrt{\mathcal F(\rho)}\le2\|w\|_2.
$$

This bounds the operator norm. The actual protocol seed need not possess
the symmetry: the argument chooses a symmetry-fixed extremal eigenvector
to bound H on every vector.

The exact equal-weight maximum for (10) is `2sqrt(6)`. For attainment set

$$
R=\frac{X_1Z_2+X_2Z_3+X_3Z_1}{\sqrt3},\qquad P=(I+R)/2.
$$

Its three Pauli terms anticommute, and each query anticommutes with
exactly one of them. Therefore `(PUP)^2=(2/3)P` and `Tr(PUP)=0`.
The flat seed `rho=P/4` has six scores `sqrt(2/3)`. Its sign readouts
inherit (10) from Theta restricted to P, so their sum is `2sqrt(6)`.
This also proves sharpness of the Euclidean constant in (11).

Normalized Kraus averaging transfers the bound to protocols whose branch
readouts satisfy (10), allowing a different antiunitary on each branch
and finite classical mixtures. Their common contrast is at most
`sqrt(2/3)`. The complete Pauli-orbit construction of the cyclic seed
attains it explicitly. Let V be an isometry from C^4 onto ran P and
`L=V^dagger/2`. For all 64 three-qubit Pauli words W, set

$$
K_W=LW/\sqrt8,\qquad
D_{W,U}=\chi_W(U)\operatorname{sign}(LUL^\dagger),
\qquad WUW^\dagger=\chi_W(U)U.
$$

Pauli averaging and `(PUP)^2=(2/3)P` give

$$
\sum_WK_W^\dagger K_W=I,\qquad
\sum_WK_W^\dagger D_{W,U}K_W=\sqrt{2/3}\,U.
$$

Each branch readout remains odd under the inherited antiunitary on C^4.
The construction accepts every branch with the same quantum dimension
cap; a filtered seed alone is not the channel.

The single unknown specimen, delayed single query, unrestricted collective
encoding, unlimited finite classical records, worst-case quantum dimension,
and uniform input/query errors retain their original meanings.

## 6. Boundaries of the result

Balanced spectrum does not imply a common antiunitary. For example, the
six balanced ququart reflections

$$
X\otimes I,\quad Z\otimes I,\quad Y\otimes I,\quad
I\otimes X,\quad I\otimes Z,\quad X\otimes X
$$

cannot all be odd under any common antiunitary. Negating `X tensor I`
and `I tensor X` preserves their product `X tensor X`, a contradiction.
Thus (11) does not settle the entire balanced sector or the other nine
continuous sectors of the unrestricted problem.

The state symmetry in (1) is also essential. The ordinary retention seed
`rho=I_4/4 tensor |beta><beta|`, with beta an X/Z bisector, has purity
1/4 but `mathcal F=5`, exceeding the proposed right side four if symmetry
were omitted. Its root-fidelity scores differ from its balanced-decoder
scores. This is not a counterexample to the separate, still-open balanced
quadratic conjecture.

## 7. Primary-source comparison

The antiunitary construction itself is established. Uhlmann, *Fidelity
and concurrence of conjugated states*, **PRA 62, 032307 (2000)**,
[published author-hosted PDF](https://www.physik.uni-leipzig.de/~uhlmann/PDF/Uh00c.pdf),
defines root fidelity and conjugation fidelity in Eqs. (3), (5),
p. 032307-2. Theorem 1/Eq. (11), p. 032307-3, proves the individual
concave-roof formula. Section VI, Example 3, Eq. (42), p. 032307-7,
already uses `U theta tensor theta tensor theta` and its permutations.
Taking U=X or Z gives our six conjugations `P_j Theta`, up to phase.
On invariant rho their conjugated states equal `P_j rho P_j`.

The published paper and corrected arXiv v4, rather than only v2, were
checked. Its Eq. (8), p. 032307-3, assumes product rank at most two and
does not supply the rank-four identity (5). Nor do individual optimal
roof decompositions automatically give a common decomposition for the
six scores. The inspected results do not state (1) or (11).

Kramers pairing, Pauli spin-flip parity, trace-norm duality, and Cauchy–
Schwarz are established ingredients. The supplied deduction is the joint
six-score purity bound, its explicit certificate (8), sharp family, and
readout consequence. A bounded comparison does not establish exhaustive
priority or publication significance. No new antiunitary resource or
physical time-reversal operation is claimed.

## 8. Verification

Independent internal reconstructions checked the paired spectrum,
rank-two completion, support determinants, every quadratic coefficient,
the sum-of-squares identity, all-purity attainment, and the operator and
complete-instrument consequences. This is internal proof review, not
external peer review.

The small deterministic construction checks are in
[`check_spin_flip_purity.py`](../../tools/check_spin_flip_purity.py) and
[`spin_flip_purity.json`](../../results/spin_flip_purity.json). They test
complex invariant supports, nonuniform spectra, the exact identity,
attaining families and the asymmetric negative control. They contain no
optimization and do not certify originality. The analytic proof stands
independently of those checks.

All 47 constructions (46 invariant states and one excluded negative
control) passed at tolerance 1e-10 in Python 3.12.14 with NumPy 2.3.5.
The maximum identity error was 7.105427357601002e-15; the maximum positive
inequality residual was 3.1086244689504383e-15. The parent workspace
independently reran the script and reproduced the JSON byte-for-byte.
