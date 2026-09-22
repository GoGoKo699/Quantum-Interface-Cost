# Exact-axis spectral reduction and unequal-accuracy collective advantage

Date: 22 September 2026. Research base:
`f761bbca3ba3c1b263a1914175e3bdab94be70a7`.

**Status:** supplied deductions with complete proofs, independently
reconstructed within this workspace. The graph extremal problem and the
graph theorem used in Section 4 are established prior mathematics.
Publication novelty of the operational deductions remains unresolved.

The single arbitrary unknown n-qubit specimen, delayed single local X/Z
query, unlimited finite classical record, worst-case quantum dimension,
and uniform arbitrary-input statistics are unchanged. As in the
[one-qubit allocation note](ONE_QUBIT_ALLOCATION_REGION.md), different
queries may have different specified contrasts. The separation below is
for unequal X/Z accuracies; it does not settle the original common-accuracy
optimization or the seed entropy conjecture.

## 1. An exact graph formula when all X queries are exact

Let `1<=D<=2^n` be the quantum dimension allowed in every branch. Require
the effective observables to be

$$
A_{i,X}=X_i,\qquad A_{i,Z}=zZ_i\quad(1\le i\le n).
\tag{1}
$$

For a nonempty set `S` of vertices of the Boolean cube, let `A_S` be
the adjacency matrix of the induced graph: two vertices are adjacent
exactly when they differ in one coordinate. Define

$$
\Lambda(n,D)=\max_{\substack{S\subseteq\{0,1\}^n\\1\le|S|\le D}}
\lambda_{\max}(A_S).
$$

**Theorem 1.** The exact optimum under (1) is

$$
\boxed{z_{\max}(n,D\mid X\text{ exact})=\frac{\Lambda(n,D)}n.}
\tag{2}
$$

The converse allows every collective encoder and every finite classical
record. The construction proving attainment is a complete instrument.

### 1.1 Exact X statistics force a diagonal branch Gram matrix

Refine an arbitrary instrument into Kraus matrices `K_a`; the added label
is classical and free. Outputs of smaller dimension can be embedded into
dimension D. With `d=2^n`, completeness and exact X readout give

$$
\sum_aK_a^\dagger K_a=I_d,\qquad
\sum_aK_a^\dagger B_{a,i}K_a=X_i,
$$

where each Hermitian decoder `B_{a,i}` is a contraction. For each fixed i,

$$
\begin{aligned}
\sum_a(B_{a,i}K_a-K_aX_i)^\dagger(B_{a,i}K_a-K_aX_i)
&=\sum_aK_a^\dagger B_{a,i}^2K_a-I_d\\
&\le0.
\end{aligned}
\tag{3}
$$

Every summand on the left is positive semidefinite, so each vanishes.
Consequently

$$
B_{a,i}K_a=K_aX_i,
\qquad [K_a^\dagger K_a,X_i]=0
\quad\text{for every }a,i.
\tag{4}
$$

The second statement follows by multiplying the first identity by
`K_a^dagger` and comparing its adjoint. This step uses exact effective
observables, without assuming that the encoder's physical outcomes are
input independent.

For each nonzero branch set

$$
\omega_a=\frac{\|K_a\|_F^2}{d},\qquad
L_a=\frac{K_a}{\|K_a\|_F},\qquad
\rho_a=L_a^\dagger L_a.
\tag{5}
$$

Then `sum_a omega_a=1`. The simultaneous X eigenbasis is nondegenerate:
write `X_i|x>_X=(-1)^{x_i}|x>_X`. Equation (4) implies

$$
\rho_a=\sum_x p_{a,x}|x\rangle_X\langle x|,
\qquad p_{a,x}\ge0,\quad\sum_xp_{a,x}=1,
\qquad|\operatorname{supp}p_a|\le D.
\tag{6}
$$

Indeed, the nonzero columns of `L_a` in this basis are mutually
orthogonal, so their number cannot exceed its output dimension.

### 1.2 The Z score is the cube Rayleigh quotient

Suppress the branch index. Orthogonality of the nonzero columns allows
the representation

$$
L=\sum_{x\in S}\sqrt{p_x}\,|u_x\rangle\langle x|_X,
\qquad\langle u_x|u_y\rangle=\delta_{xy}.
$$

In the X basis, `Z_i` sends x to `x+e_i`, with addition modulo two.
Each compression `LZ_iL^dagger` is a disjoint union of two-by-two
off-diagonal blocks. Therefore

$$
F_i(p):=\|LZ_iL^\dagger\|_1
=\sum_{x\in\{0,1\}^n}\sqrt{p_xp_{x+e_i}}.
\tag{7}
$$

Here p is extended by zero outside S. Both orientations of each edge
appear in (7), exactly as they do in an adjacency-matrix quadratic form.
With `v_x=sqrt(p_x)`,

$$
\sum_iF_i(p)=v^TA_Sv\le\lambda_{\max}(A_S)\le\Lambda(n,D).
\tag{8}
$$

Let `C_{a,i}` be the actual Z decoder, another Hermitian contraction.
Taking the normalized Hilbert--Schmidt inner product of its effective
observable with `Z_i` gives

$$
z_i=\frac1d\sum_a\operatorname{Tr}(C_{a,i}K_aZ_iK_a^\dagger)
\le\sum_a\omega_aF_i(p_a).
\tag{9}
$$

This also proves the stronger necessary condition `sum_i z_i<=Lambda`
when the Z contrasts differ. In the common-Z case, summing (9) proves
`nz<=Lambda(n,D)`. The weights in (5) are actual outcome probabilities
only on the maximally mixed input; the proof does not assign them that
meaning on arbitrary inputs.

## 2. Complete attainment from a nonnegative graph eigenvector

Choose a support S and nonnegative unit vector v on it, put `p_x=v_x^2`,
and form L as above using orthogonal output labels. For each binary string
t, let `Z^t=product_i Z_i^{t_i}` and define

$$
\boxed{K_t=LZ^t,\qquad t\in\{0,1\}^n.}
\tag{10}
$$

There is **no additional scalar prefactor** in (10). Since `Z^t`
translates the X basis,

$$
\sum_tK_t^\dagger K_t
=\sum_tZ^t\rho Z^t
=\sum_y\left(\sum_t p_{y+t}\right)|y\rangle_X\langle y|
=I_d.
\tag{11}
$$

Thus the complete collection is a trace-preserving instrument. Its
quantum output dimension is at most `|S|<=D`, and its classical outcome
alphabet is finite. It does not select a favorable branch.

Define output contractions, set to zero outside the span of the labels,

$$
D_i=\sum_{x\in S}(-1)^{x_i}|u_x\rangle\langle u_x|,
\qquad
C_i=\sum_{\substack{x\in S\\x+e_i\in S}}
|u_x\rangle\langle u_{x+e_i}|.
\tag{12}
$$

The second operator swaps the endpoints of each matching edge and is
zero on unmatched labels. It is Hermitian with norm at most one.
For an X query in branch t, use `(-1)^{t_i}D_i`. Because
`L^dagger D_i L=rho X_i`,

$$
\sum_tK_t^\dagger((-1)^{t_i}D_i)K_t=X_i.
\tag{13}
$$

For a Z query use `C_i` in every branch. Directly,

$$
L^\dagger C_iL
=\sum_x\sqrt{p_xp_{x+e_i}}|x\rangle_X\langle x+e_i|,
$$

and translating every term gives

$$
\sum_tK_t^\dagger C_iK_t
=F_i(p)\sum_y|y\rangle_X\langle y+e_i|
=F_i(p)Z_i.
\tag{14}
$$

Choose S maximizing Lambda and a nonnegative unit top eigenvector of
`A_S`; such a vector exists by Perron--Frobenius, allowing zero entries
on other components. Equations (8) and (14) attain total Z contrast
Lambda. Independent uniform randomization over the n cyclic coordinate
permutations, with the permutation stored classically and the query
relabelled, makes every Z contrast `Lambda/n`. Every X contrast remains
one. Each randomized component has the same dimension cap, completing
the proof of Theorem 1. Lower Z contrasts follow by output flips.

The completion contains `2^n` translations, or at most `n2^n` branches
after coordinate randomization. This can be a large classical record
space, which the operational model permits. No claim of an efficient
laboratory implementation or a small explicit circuit is needed for (2).

## 3. The entire original-site-retention subclass and a strict separation

### 3.1 Definition of the comparison class

Fix an integer `0<=q<=n`. Call a protocol an **original-site-retention
protocol** when its instrument admits a Kraus refinement in which every
nonzero branch has the form

$$
K_a=M_a\otimes\langle v_a|,
\qquad T_a\subseteq[n],\quad |T_a|\le q.
\tag{15}
$$

The tensor decomposition in (15) is across the original input sites
`T_a` and its complement. The map `M_a` can process the retained sites
arbitrarily; the bra on the complementary sites can be entangled across
those sites. The output dimension is at most `2^q`. The retained set,
map, and bra may depend on the refined classical branch, and physical
branch probabilities can depend on the input. Arbitrary contractions
are permitted at decoding. Completeness is imposed on the whole
instrument. Convex mixtures and further classical refinements are
included. Coherent encoding across the two parts of this input split
is not assumed to have form (15).

This precisely defined class contains the usual random-subset strategy
and allows much more general discarded-site measurements and retained
processing. It is a comparison class, not a restriction on Theorem 1.

Set

$$
w(x,z)=\bigl[x+z-1-\sqrt{2(1-x)(1-z)}\bigr]_+,
\quad (x,z)\in[0,1]^2.
\tag{16}
$$

**Theorem 2.** The exact nonnegative contrast region of this entire
subclass is

$$
\boxed{\sum_{i=1}^n w(\eta_{i,X},\eta_{i,Z})\le q.}
\tag{17}
$$

Equivalently, for `a_i,b_i>=0`, write
`r_i=sqrt(a_i^2+b_i^2)` and `d_i=a_i+b_i-r_i`. If
`d_(1)>=...>=d_(n)` is their decreasing ordering, the exact support
function is

$$
\max\sum_i(a_i\eta_{i,X}+b_i\eta_{i,Z})
=\sum_i r_i+\sum_{j=1}^q d_{(j)}.
\tag{18}
$$

An empty last sum is zero. For q=1 this agrees with the previously
proved unrestricted dimension-two region; that coincidence does not
extend to every q.

### 3.2 Converse and convex description

Normalize each branch of (15) as in (5). After absorbing scalar factors,
its Gram matrix is `tau_T tensor |v><v|`, with `Tr tau_T=1` and
`||v||=1`. At a retained site, both normalized trace norms are at most
one: for any Hermitian unitary P,
`||LPL^dagger||_1<=||L||_F||PL^dagger||_F=1`.
At a discarded site the two trace norms equal the absolute X and Z
expectations of its reduced state in `|v>`. Its Bloch vector gives

$$
a_i\|LX_iL^\dagger\|_1+b_i\|LZ_iL^\dagger\|_1
\le\begin{cases}a_i+b_i,&i\in T,\\r_i,&i\notin T.\end{cases}
\tag{19}
$$

This uses no product assumption on v. Weighted trace-norm duality,
followed by the normalized Kraus average, bounds the actual profile
by the right side of (18).

Let `D_0={(x,z)>=0:x^2+z^2<=1}` and `S_0=[0,1]^2`. For every fixed
T with `|T|<=q`, retaining those sites and using compatible local
measurements elsewhere realizes the product region with `S_0` on T
and `D_0` outside T. In fact the four-outcome local POVM

$$
G_{s,t}=\tfrac14(I+s uX+t vZ),\qquad s,t\in\{\pm1\},
\quad(u,v)\in D_0
\tag{20}
$$

has the required two marginals. Its spectral Kraus refinement has
form (15). On retained sites independent output noise realizes the
square. Every identity holds on arbitrary, including entangled, inputs.
Their convex hull K is therefore feasible in the subclass, and its
support function is exactly (18): choose the q largest d values,
the corner `(1,1)` there, and `(a_i/r_i,b_i/r_i)` elsewhere.

The set K is compact and downward closed in the nonnegative orthant.
If a nonnegative profile lies outside K, separation gives a real
direction h excluding it. Downward closure gives `h_K(h)=h_K(h_+)`,
while the profile's pairing with `h_+` is at least its pairing with h.
Thus a nonnegative support direction also excludes it. Equation (18)
rules out every such profile, proving that K is the exact region.

### 3.3 Explicit criterion and finite implementation

For a single pair `(x,z)`, the least p permitting
`(x,z)=p s+(1-p)d`, with `s in S_0` and `d in D_0`, equals (16).
Necessity follows from

$$
\|((x,z)-p(1,1))_+\|_2\le1-p.
\tag{21}
$$

Inside the disk p=0 works. Outside it the smaller quadratic root of
`(x-p)^2+(z-p)^2=(1-p)^2` is
`p_*=x+z-1-sqrt(2(1-x)(1-z))`. It lies in `[0,min(x,z)]`.
For `p<p_*` neither positive part in (21) truncates a coordinate and
the inequality fails. At `p=p_*` it holds, using `s=(1,1)` and
`d=((x,z)-p_*(1,1))/(1-p_*)` if `p_*<1`.
The case `p_*=1` is exactly `(x,z)=(1,1)`.

For every convex mixture defining K, let p_i be the probability that
site i is retained. Then `sum_i p_i<=q`; aggregation at each site
expresses its pair as a square/disk mixture, so `w_i<=p_i`.
This proves necessity of (17).

Conversely, put `p_i=w_i` and assume (17). The polytope
`{p in [0,1]^n:sum_i p_i<=q}` is the convex hull of incidence vectors
of subsets of size at most q. To see this directly, a vertex cannot
have a fractional coordinate with slack in the sum constraint, because
that coordinate can be perturbed both ways. If the sum equals the
integer q and a coordinate is fractional, at least two are fractional;
opposite perturbations of those two again contradict extremality.
Every vertex is therefore an incidence vector of an allowed subset.

Take a finite distribution on these subsets with marginals p_i. Retain
the sampled subset, use contrasts `(1,1)` on it, and use (20) at each
discarded site with pair
`((eta_(i,X),eta_(i,Z))-p_i(1,1))/(1-p_i)`.
The preceding calculation places this pair in the disk. If p_i=1,
the site is always retained and its discarded pair is unused.
Averaging gives the desired profile exactly, proving (17), including
finite classical storage and the worst-case q-qubit cap.

### 3.4 A five-qubit encoding beyond every such retention protocol

Take the star support

$$
S=\{0,e_1,\ldots,e_n\},\qquad
p_0=\tfrac12,\quad p_{e_i}=\tfrac1{2n}.
\tag{22}
$$

Its square-root probability vector is a top eigenvector of the star,
with eigenvalue `sqrt(n)`. More directly, (7) gives
`F_i=2sqrt(p_0p_(e_i))=1/sqrt(n)` for each i.
The complete instrument in Section 2 has dimension n+1 and implements

$$
\eta_{i,X}=1,\qquad\eta_{i,Z}=1/\sqrt n.
\tag{23}
$$

For `n=31`, the dimension is exactly `32=2^5`. But
`w(1,z)=z`, so (17) would require `sqrt(31)<=5`, which is false.
Thus a collective five-qubit encoder strictly exceeds the entire
original-site-retention subclass on this unequal-accuracy task.

The separation also holds away from exact X readout. Multiply each
X decoder in the same construction by `9999/10000`; Z is unchanged.
Both contrasts are now strictly between zero and one:

$$
x=\frac{9999}{10000},\qquad z=\frac1{\sqrt{31}}.
\tag{24}
$$

The corresponding uniform per-query errors are
`epsilon_X=1/20000` and `epsilon_Z=(1-1/sqrt(31))/2`.
An entirely analytic separation follows from
`z>1796/10000` and
`sqrt((2/10000)(1-z))<13/1000`. Therefore

$$
w(x,z)=z-\frac1{10000}
-\sqrt{\frac2{10000}(1-z)}
>\frac{1665}{10000},\qquad
31w(x,z)>5.1615>5.
\tag{25}
$$

The numerical value `31w(x,z)` is approximately `5.167575127329441`,
but (25), not numerical precision, establishes the strict inequality.
Only the 32-vertex support and its scalar data are needed to describe
this example; no full `2^31` input matrix or list of `2^31` Kraus
branches has been numerically built.

This proves an unequal-accuracy collective advantage. It gives neither
an optimality certificate at `(n,D)=(31,32)` nor an improvement for the
original common contrast. Symmetrizing (23) over X/Z yields common
contrast `(1+1/sqrt(31))/2`, below the classical common-contrast
threshold. The product-diagonal entropy bound is therefore unaffected.

## 4. An exactly evaluated family from a prior graph theorem

Bollobas--Lee--Letzter, *Eigenvalues of subgraphs of the cube*,
[author manuscript](https://www.homepages.ucl.ac.uk/~ucahsle/papers/cube-evals.pdf),
dated 7 August 2020, Theorem 2 on printed p. 3, proves the star bound
for induced subgraphs with m vertices in an n-dimensional cube when
`105<=m<=n`. Combining that established theorem with (2) gives

$$
\boxed{z_{\max}(n,D\mid X\text{ exact})=\frac{\sqrt{D-1}}n,
\qquad105\le D\le n.}
\tag{26}
$$

For completeness, a support smaller than D can be padded to D vertices.
Its adjacency matrix is a principal submatrix of the padded one, so
its largest eigenvalue cannot increase when passing back to the smaller
support. The prior bound therefore controls every support allowed in
Lambda. A D-vertex star exists because `D-1<=n`, attains `sqrt(D-1)`,
and Section 2 equalizes its coordinate contrasts, proving equality.

For `D=2^q`, `q>=7`, and `n>=2^q`, this gives the exact law
`z_max=sqrt(2^q-1)/n`. The subclass (17) on this face has exact optimum
`q/n`, so the gap is strict. Here `2^q-1>q^2` follows at q=7 and
persists by induction since the increment `2^q` exceeds `2q+1`.

**Version qualification.** Theorem 2 in
[arXiv:1605.06360v1](https://arxiv.org/pdf/1605.06360v1), whose arXiv
stamp is 20 May 2016, instead prints the literal threshold 103. The
later author manuscript prints 105. We use the common range `D>=105`.
Neither range covers the 31-input, 32-dimensional example: it also
fails `D<=n`. That example's construction and separation require no
graph optimality theorem.

## 5. Theorem-level provenance and remaining novelty question

The ingredients, deductions, and possible subsumption should be separated.

| Primary source and locator | Established result and scope of the comparison |
|---|---|
| Bollobas--Lee--Letzter, author manuscript cited above, Question 1 on p. 2; Section 2 on p. 4; Theorem 5 on p. 3 | The graph extremal problem and its support-constrained Rayleigh formulation are prior. Fixed-radius Hamming balls are optimal once the cube dimension is sufficiently large. The latter existential threshold supplies no certificate for n=31. Equation (26) is an application of their graph bound. |
| Avni--Samorodnitsky, [2411.14597v1](https://arxiv.org/pdf/2411.14597v1), 21 November 2024, Corollary 1.8 on p. 6; Example 1.12 on p. 8; Corollary 1.15 on p. 11 | The Hamming-ball top eigenvalue is expressed by the first root of a Krawtchouk polynomial; the star spectrum is explicitly evaluated. Further asymptotic spectral estimates are available. The star eigenvalue in (22) is not new graph theory. These graph results do not by themselves establish the operational reduction or complete the quantum instrument. |
| Guerini--Quintino--Aolita, [1904.08435v4](https://arxiv.org/pdf/1904.08435v4), 14 October 2019, Theorems 2--3 on p. 4 | Trusted unknown quantum inputs and delayed measurement sampling already have an operational incompatibility interpretation. Their classical-communication equivalence and witnesses cover the classical endpoint. These statements do not evaluate the present worst-case quantum-dimension boundary. |
| Lobo--Balanzo-Juando--Pironio, [2605.16151v1](https://arxiv.org/pdf/2605.16151v1), 15 May 2026, Definition 1 / Eqs. (2)--(3) on p. 2; Definition 2 / Eqs. (9)--(11) on p. 3 | Partial-input joint measurability fixes which settings are answered from classical data, while other settings can use a residual quantum system without this paper's dimension cap. It supplies the relevant classicalization framework, not an identification of every dimension-D protocol with a retained-site mixture. |

For the last comparison, if both queries outside a specified set T must
be classicalized, their local contrast pairs must belong to the disk:
restrict a compatible parent to one input qubit by fixing all other
inputs. Conversely, the product parent (20), leaving T untouched,
implements every disk/square product used above. Thus the convex
geometric region in Theorem 2 has a partial-classicalization reading.
What fails beyond one qubit is identifying this convex region with all
encoders of dimension `2^q`: (23)--(25) explicitly refute that extension.

The supplied operational deductions are the exact unrestricted
dimension-to-support reduction (2), its complete translation-instrument
attainment, the converse for all refined branches in (15), and the
resulting unequal-accuracy separation. Standard graph, compatibility,
and convexity ingredients are credited above. The inspected primary
statements do not establish that these combined operational conclusions
were already proved. This limited comparison is not evidence that no
other source subsumes them, and no publication-novelty certification is
claimed. The original uniform-accuracy rate and entropy targets remain
separate unresolved questions.
