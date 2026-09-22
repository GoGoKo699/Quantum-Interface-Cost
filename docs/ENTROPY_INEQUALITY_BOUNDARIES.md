# Further boundaries of the seed entropy inequality

Date: 22 September 2026. Research base:
`f9a5fc72d15e9d314f6deae65096605e955a2051`.

**Status:** supplied analytical deductions, independently checked within this
workspace. These are restricted-family results inside the unrestricted
operational problem. They do not certify publication novelty or settle the
unrestricted entropy inequality.

The [entropy-rate characterization](ENTROPY_RATE_CHARACTERIZATION.md) makes
optimality of the random-subset rate equivalent to

$$
g(\sqrt\rho):=\sum_{i=1}^n\sum_{b=X,Z}
\|\sqrt\rho\,P_{i,b}\sqrt\rho\|_1
\le \sqrt2\,n+(2-\sqrt2)S(\rho)
\tag{1}
$$

for every n-qubit density matrix rho. Entropies are in bits. The
[product-diagonal theorem](COMMUTING_SEED_BOUND.md) already proves (1) when
rho is diagonal in a fixed tensor product of local qubit bases, with
arbitrarily correlated eigenvalues. Here are four further families:

| Family | Result | Scope |
|---|---|---|
| Rank at most two, any eigenbasis | Exact maximum at each nonzero spectrum, implying (1) | All n; eigenvectors may be entangled |
| Flat rank three on two qubits | Exact maximum over its missing eigenvector, strictly below (1) | Every state `(I-|v><v|)/3` |
| Stabilizer eigenbasis | Stronger entropy-deficit bound with optimal coefficient `ln(2)` | Any fixed joint eigenbasis of a maximal commuting Pauli group; arbitrary eigenvalues |
| Flat half-rank projector with one maximally mixed complementary marginal | Subset bound, hence (1) | `rho=P/2^(n-1)` and `Tr_i P=I` for at least one i |

The families overlap and are not assumptions about the physical encoder.
The model remains one unknown quantum specimen, one delayed local query,
arbitrary collective encoding, unlimited finite classical records,
worst-case quantum dimension, and uniform statistics on every input state.
The seed reduction turns any violating Gram matrix into an operational
asymptotic improvement; no such violation is established here.

## 1. Exact optimum at every rank-two spectrum

**Theorem.** Let rho have rank at most two and nonzero spectrum
`lambda,1-lambda`, allowing an endpoint eigenvalue to vanish. Then

$$
\boxed{
 g(\sqrt\rho)\le \sqrt2(n-1)
 +\sqrt2\sqrt{1+4\lambda(1-\lambda)}.
}
\tag{2}
$$

For every lambda, equality is attained by

$$
\rho=\left(\lambda|\beta_+\rangle\langle\beta_+|
 +(1-\lambda)|\beta_-\rangle\langle\beta_-|\right)
 \otimes(|\beta_+\rangle\langle\beta_+|)^{\otimes(n-1)},
\tag{3}
$$

where beta signs are the two eigenstates of `(X+Z)/sqrt(2)`. Thus (2) is
an exact maximum at fixed spectrum, including arbitrary entangled
eigenvectors in the optimization.

### A two-qubit correlation lemma

For a two-qubit state sigma on A,Q, let r be the Bloch vector of its Q
marginal. If `A_0,A_1` are orthogonal Pauli directions on A and
`B_0,B_1` are unit traceless qubit observables on Q, then

$$
\operatorname{Tr}\sigma(A_0\otimes B_0+A_1\otimes B_1)
\le\sqrt{4-2|r|^2}.
\tag{4}
$$

For a pure two-qubit state, use Schmidt coefficients
`cos(theta),sin(theta)`. In Schmidt bases its correlation matrix is
`diag(c,-c,1)`, with `c=sin(2 theta)` and `c^2=1-|r|^2`. Local basis
changes rotate the correlation matrix T and preserve its singular values
`1,c,c`. If `a_0,a_1` are the two orthonormal reference directions, the
correlation in (4) is at most

$$
\begin{aligned}
\|T^Ta_0\|+\|T^Ta_1\|
&\le\sqrt{2\bigl(\|T^Ta_0\|^2+\|T^Ta_1\|^2\bigr)}\\
&\le\sqrt{2(1+c^2)}=\sqrt{4-2|r|^2}.
\end{aligned}
$$

The second inequality follows by diagonalizing `TT^T`: its trace against
a rank-two orthogonal projector is at most the sum of its two largest
eigenvalues.

For a mixed state choose any pure decomposition
`sigma=sum_s p_s |phi_s><phi_s|`, and write `r_s` for its marginal Bloch
vectors. The observables remain fixed during this decomposition. Linearity,
Cauchy–Schwarz, and convexity of squared Euclidean norm give

$$
\begin{aligned}
\operatorname{Tr}\sigma(A_0\otimes B_0+A_1\otimes B_1)
&\le\sum_s p_s\sqrt{4-2|r_s|^2}\\
&\le\sqrt{4-2\sum_s p_s|r_s|^2}\\
&\le\sqrt{4-2\left|\sum_s p_s r_s\right|^2}.
\end{aligned}
$$

Since `sum_s p_s r_s=r`, this proves (4). No mixed-state entanglement
formula is needed.

### Proof of the spectrum theorem

Choose a two-row seed L with `L^dagger L=rho`. Its normalized pure
vectorization on `R_1...R_n Q` has Q marginal eigenvalues
`lambda,1-lambda`. Choose extreme Hermitian decoder contractions attaining
all trace norms for this L. As in
[the one-qubit proof](ONE_QUBIT_OPTIMALITY.md), each decoder is `+I`, `-I`,
or a unit traceless Pauli direction. Call site i active when both its
decoders are traceless, and set

$$
h_i=X_i\otimes B_{i,X}+Z_i\otimes B_{i,Z},
\qquad f_i=\langle h_i\rangle.
$$

An inactive site has `h_i^2=2I`, so `f_i<=sqrt(2)`. For any two active
sites i,k, Cheng–Hall's three-qubit CHSH monogamy theorem gives

$$
f_i^2+f_k^2\le4.
\tag{5}
$$

The independently chosen common-qubit settings and mixed-state extension
required for (5) are established in Cheng–Hall,
[arXiv:1610.09302v3](https://arxiv.org/abs/1610.09302v3), Eq. (1), PDF p. 1,
and Eqs. (13)–(14) with the following paragraph, PDF p. 3. The exact
application and its limitations are detailed in
[ONE_QUBIT_OPTIMALITY.md](ONE_QUBIT_OPTIMALITY.md), Sections 2–4.

If there are at least two active sites, summing (5) and applying
Cauchy–Schwarz bounds their total by their number times `sqrt(2)`.
Together with the inactive sites this gives `g<=n sqrt(2)`. The same
bound holds with no active sites. Both cases satisfy (2).

With exactly one active site i, apply (4) to the possibly mixed marginal
on `R_i Q`. Its Q Bloch vector has length `|2lambda-1|`, so

$$
f_i\le\sqrt{4-2(2\lambda-1)^2}
=\sqrt2\sqrt{1+4\lambda(1-\lambda)}.
$$

The remaining sites each contribute at most `sqrt(2)`, proving (2).
For (3), the two-by-two edge formula in the product-diagonal note gives
the displayed nontrivial local score, and every pure bisector factor
contributes `sqrt(2)`. This proves achievability.

### Entropy consequence

The explicitly proved scalar inequality from
[COMMUTING_SEED_BOUND.md](COMMUTING_SEED_BOUND.md), Section 2, is

$$
\sqrt{1+4\lambda(1-\lambda)}
\le1+(\sqrt2-1)h_2(\lambda).
$$

Together with `S(rho)=h_2(lambda)`, it proves (1) for **every rank-two
state**, including arbitrary entangled eigenbases. The scalar inequality
is strict except at `lambda=0,1/2,1`. Consequently equality in (1) at
rank two requires a flat nonzero spectrum; that case's maximizing seeds
are already classified in the one-qubit note. This excludes all rank-two
seeds from an entropy-based asymptotic advantage, beyond their previously
known finite one-qubit bound.

## 2. All flat rank-three two-qubit states

Let

$$
\rho=\frac{I_4-|v\rangle\langle v|}{3},\qquad \langle v|v\rangle=1,
\qquad P=I_4-|v\rangle\langle v|.
$$

For a local Pauli U, its positive and negative eigenspaces each have
dimension two. Compression to `v`'s orthogonal complement leaves an
eigenvector with eigenvalue +1 in the positive eigenspace, and one with
eigenvalue -1 in the negative eigenspace. The last eigenvalue is fixed by
trace:

$$
\operatorname{Tr}(PUP)=\operatorname{Tr}U-\langle v|U|v\rangle
=-\langle v|U|v\rangle.
$$

This includes the case that v lies in one eigenspace, either directly by
counting multiplicities or by continuity. Therefore

$$
\|\sqrt\rho\,U\sqrt\rho\|_1
=\frac{2+|\langle v|U|v\rangle|}{3},
$$

and hence

$$
\boxed{
 g(\sqrt\rho)
 =\frac{8+\sum_{i,b}|\langle v|P_{i,b}|v\rangle|}{3}
 \le\frac{8+2\sqrt2}{3}.
}
\tag{6}
$$

The last step uses the Bloch-ball inequality
`|<X_i>|+|<Z_i>|<=sqrt(2)` on each reduced qubit. A product of pure
bisectors attains (6), so the maximum over v is exact. Numerically,

$$
\frac{8+2\sqrt2}{3}\simeq3.609476
<2\sqrt2+(2-\sqrt2)\log_2 3\simeq3.756877.
$$

Since `S(rho)=log_2 3`, every flat rank-three two-qubit state satisfies
(1) strictly. A rank-three counterexample would require nonuniform
nonzero eigenvalues.

## 3. States diagonal in a stabilizer eigenbasis

**Theorem.** Suppose

$$
\rho=C\operatorname{diag}(p)C^\dagger,
$$

where C is any global n-qubit Clifford unitary and p is any probability
law on binary n-tuples. Equivalently, rho is diagonal in a joint eigenbasis
of n independent commuting Pauli operators. Eigenvalues may be correlated,
nonflat, or zero. Then

$$
\boxed{
 g(\sqrt\rho)\le2n-\ln(2)\,[n-S(\rho)].
}
\tag{7}
$$

Since `ln(2)>2-sqrt(2)`, this implies (1), strictly whenever `S(rho)<n`.
The coefficient `ln(2)` in (7) is optimal for this family.

### From Pauli queries to classical translations

Clifford conjugation sends each original local query to a Pauli monomial,

$$
Q_j=C^\dagger P_jC,\qquad
Q_j|x\rangle=\omega_j(x)|x+v_j\rangle,
$$

where `v_j` is a binary n-vector, addition is modulo two, and
`|omega_j(x)|=1`. The sandwiched matrix is a weighted monomial matrix,
so its singular values are `sqrt(p_x p_(x+v_j))`. Consequently

$$
F_j:=\|\sqrt\rho\,P_j\sqrt\rho\|_1
=\sum_x\sqrt{p_xp_{x+v_j}}.
\tag{8}
$$

This number belongs to `[0,1]`; it is one when `v_j=0`.

The 2n binary Pauli labels of the original `X_i,Z_i` form a basis of the
full `2n`-dimensional binary Pauli space. Clifford conjugation is an
invertible linear transformation there, and projection onto translation
labels is surjective. Therefore the 2n vectors `v_j` span the n-dimensional
translation space. Choose n independent ones, let T be the binary matrix
with those columns, and relabel `x=T u`. The selected translations become
the individual coordinate flips `u -> u+e_i`. The relabeled law of U
has entropy `H(U)=H(p)=S(rho)`.

### Binary affinity and entropy

For every `0<=lambda<=1`,

$$
1-2\sqrt{\lambda(1-\lambda)}
\ge\ln(2)\,[1-h_2(\lambda)].
\tag{9}
$$

To prove it, put `t=|1-2lambda|`. The difference between the two sides is

$$
D(t)=1-\sqrt{1-t^2}
-\frac{(1+t)\ln(1+t)+(1-t)\ln(1-t)}2.
$$

We have `D(0)=0`, and

$$
D'(t)=\frac{t}{\sqrt{1-t^2}}-\operatorname{atanh}t,
\qquad
D''(t)=(1-t^2)^{-3/2}-(1-t^2)^{-1}>0
$$

for `0<t<1`. Since `D'(0)=0`, the desired inequality follows, with the
endpoint covered by continuity. Equality holds only at `lambda=1/2`.

For a selected coordinate i, group the classical law into edges with
fixed `y=U_-i`. Write `w_y=p(0,y)+p(1,y)` and
`lambda_y=p(0,y)/w_y` when the weight is positive; zero-weight edges
contribute zero. Equation (8) becomes

$$
F_{j_i}=\sum_y w_y\,2\sqrt{\lambda_y(1-\lambda_y)}.
$$

By (9),

$$
1-F_{j_i}\ge\ln(2)\,[1-H(U_i\mid U_{-i})].
$$

Conditioning reduces classical entropy, so

$$
\sum_i H(U_i\mid U_{-i})
\le\sum_i H(U_i\mid U_1,\ldots,U_{i-1})=H(U).
$$

All unselected query deficits are nonnegative. Therefore

$$
\begin{aligned}
2n-g(\sqrt\rho)
&\ge\sum_i(1-F_{j_i})\\
&\ge\ln(2)\left[n-\sum_iH(U_i\mid U_{-i})\right]\\
&\ge\ln(2)\,[n-S(\rho)],
\end{aligned}
$$

which proves (7).

### Sharpness within this family

Take `C=I` and

$$
\rho_t=\operatorname{diag}\left(\frac{1+t}2,\frac{1-t}2\right)
\otimes(I/2)^{\otimes(n-1)}.
$$

Only the first X query has a nonzero deficit. Thus

$$
\frac{2n-g(\sqrt{\rho_t})}{n-S(\rho_t)}
=\frac{1-\sqrt{1-t^2}}{1-h_2((1+t)/2)}
\longrightarrow\ln2\qquad(t\longrightarrow0).
$$

No larger coefficient can replace `ln(2)` in (7). This is a limiting
sharpness statement; the nonuniform states need not saturate (7).
The proof is an explicit binary entropy argument after a stabilizer
translation reduction, not an assumption that an optimal seed is a
stabilizer state.

## 4. Flat half-rank projectors with a balanced marginal

Put `d=2^n`, `r=d/2`, and let P be a rank-r orthogonal projector. Consider

$$
\rho=P/r,\qquad S=2P-I.
$$

Here S denotes a traceless Hermitian unitary, not the entropy function
`S(rho)`. These states have `S(rho)=n-1`, so (1) reduces to the subset
bound `g<=2(n-1)+sqrt(2)`.

### A balanced compression identity

For every Hermitian unitary U,

$$
\|PUP\|_1=\frac14\|\{S,U\}\|_1.
\tag{10}
$$

Indeed, in the `P/(I-P)` decomposition write

$$
U=\begin{pmatrix}A&B\\B^\dagger&D\end{pmatrix}.
$$

Unitarity gives `A^2=I-BB^dagger` and `D^2=I-B^dagger B`. The two
blocks have the same dimension r, so these squares have the same spectrum,
and `Tr|A|=Tr|D|`. The anticommutator is `diag(2A,-2D)`, proving (10).
The equal block dimensions are essential to this identity.

### Exact converse under one marginal condition

**Theorem.** If `Tr_i P=I` on the other n-1 input sites for at least one
i, then

$$
\boxed{g(\sqrt\rho)\le2(n-1)+\sqrt2.}
\tag{11}
$$

The hypothesis is equivalent to `Tr_i S=0`. Expand

$$
S=X_i\otimes A+Y_i\otimes B+Z_i\otimes C.
$$

Normalized partial trace of `S^2=I` gives `A^2+B^2+C^2=I`. By (10),

$$
\frac{\|PX_iP\|_1}{r}=\frac{\operatorname{Tr}|A|}{r},
\qquad
\frac{\|PZ_iP\|_1}{r}=\frac{\operatorname{Tr}|C|}{r}.
$$

Cauchy–Schwarz and `A^2+C^2<=I` bound their sum by `sqrt(2)`.
Each of the other `2(n-1)` compressed Pauli terms has normalized trace
norm at most one. Summing proves (11).

Equality holds precisely for

$$
P=|\beta\rangle\langle\beta|_i\otimes I_{\mathrm{rest}},
\tag{12}
$$

where beta is one of the four X/Z bisectors. To prove necessity, every
query on the other sites must have normalized compression score one.
Since every singular value of a compressed unitary is at most one, all r
of them must then equal one. Thus the off-diagonal block vanishes,
`PU(I-P)=0`, and P commutes with that query. Commutation with every local
X and Z on the other sites gives `P=P_i tensor I_rest`. Its rank forces
`P_i` to be a rank-one qubit projector; saturation of its local X/Z
Bloch-ball bound makes it a bisector. Conversely (12) attains (11).

This family contains states outside every fixed product-diagonal basis.
For example, for n at least two let

$$
S=\frac{X_1+Z_1Z_2}{\sqrt2}\otimes I_{3\ldots n},\qquad P=(I+S)/2.
$$

The two summands anticommute, so S is a traceless reflection and
`Tr_1 P=I`. If P were diagonal in a fixed local product basis it would
commute with a nontrivial local Pauli axis on site 1. Linear independence
of `I_2` and `Z_2` would force that axis to commute with both `X_1` and
`Z_1`, which is impossible. The marginal condition nevertheless remains
a restriction on flat half-rank seeds.

### Quantitative obstruction away from the balanced marginal

For a general flat half-rank projector expand at site i as

$$
S=I_i\otimes A_0+X_i\otimes A_x+Y_i\otimes A_y+Z_i\otimes A_z.
$$

Then

$$
A_0=\operatorname{Tr}_i P-I,\qquad
A_0^2+A_x^2+A_y^2+A_z^2=I.
$$

Equation (10) and Hilbert–Schmidt Cauchy–Schwarz give

$$
\begin{aligned}
g_{i,X}&\le\sqrt{\operatorname{Tr}(A_0^2+A_x^2)/r},\\
g_{i,Z}&\le\sqrt{\operatorname{Tr}(A_0^2+A_z^2)/r},\\
g_{i,X}+g_{i,Z}
&\le\sqrt{2\left[1+\operatorname{Tr}(A_0^2)/r\right]},
\end{aligned}
\tag{13}
$$

where `g_{i,b}=||P P_(i,b)P||_1/r`. For example,
`{S,X_i}=2(X_i tensor A_0+I_i tensor A_x)` has squared
Hilbert–Schmidt norm `8 Tr(A_0^2+A_x^2)` and dimension `2r`, yielding
the first inequality with (10).

If a flat seed has score `g=2(n-1)+sqrt(2)+delta` with delta greater
than zero, every site must therefore satisfy

$$
\frac{\operatorname{Tr}[(\operatorname{Tr}_iP-I)^2]}r
\ge\sqrt2\,\delta+\frac{\delta^2}{2}>0.
\tag{14}
$$

This follows because all the other sites together contribute at most
`2(n-1)`. The nonstrict first inequality is intentional: delta is the
exact excess above the subset score.

### A necessary Pauli-concentration condition at n=3

Expand the traceless reflection in Pauli strings,

$$
S=\sum_{a\ne I}s_a\sigma_a,\qquad \sum_a s_a^2=1,
$$

and, for each local X/Z query U_j, define

$$
w_j=\sum_{a:\{\sigma_a,U_j\}=0}s_a^2.
$$

A direct trace expansion of `P=(I+S)/2` gives

$$
\frac{\operatorname{Tr}[(PU_jP)^2]}r=1-w_j,
\qquad g_j\le\sqrt{1-w_j}.
$$

Every nonidentity Pauli string anticommutes with at least one local X/Z
query, so `sum_j w_j>=1`. Hence

$$
g(\sqrt\rho)\le\sqrt{2n\left(2n-\sum_jw_j\right)}
\le\sqrt{2n(2n-1)}.
\tag{15}
$$

At n=3 the last bound is `sqrt(30)`, which is **above** `4+sqrt(2)` and
does not settle the finite block. A flat rank-four violation would require

$$
\sum_j w_j<3-\frac{4\sqrt2}{3}.
$$

Only the six single-site X/Z strings have anticommutation count one;
every other nonidentity string has count at least two. Thus the total
squared Pauli coefficient outside those six strings must be strictly less
than

$$
2-\frac{4\sqrt2}{3}\simeq0.114382.
\tag{16}
$$

Conditions (14) and (16) narrow the flat-projector search. They neither
produce a violation nor cover nonflat rank-four seeds.

## 5. Distinct remaining targets

A violation of (1) would certify an asymptotic improvement by the existing
entropy characterization. The first possible input size is n=2. Rank at
most two is now excluded, and the flat rank-three case is excluded. Thus
**nonuniform rank-three two-qubit states** are a minimal remaining entropy
witness family; **full-rank two-qubit states also remain unresolved** outside
the proved families. This is not a claim that a witness must have rank three.

The first unresolved finite integer-qubit budget is different:
`n=3,q=2`, or `Gamma(3,4)>4+sqrt(2)`. Such a witness may be flat or
nonflat; Section 4 applies only to the stated flat subset. A flat witness
must have a nonmaximally mixed complementary marginal at every site and
obey the Pauli-concentration condition. Artificially imposing either
flatness or a stabilizer eigenbasis on the general optimization would
change the question.

The deductions use the already identified Cheng–Hall theorem, elementary
matrix algebra, and classical entropy identities. The unrestricted entropy
inequality, its sharp rate consequence, and publication novelty remain open.
