# Full weighted allocation for the decoder algebra

Date: 24 September 2026. Reviewed main:
`98fa6f4bb9849d6d8317cd93cc14626d288a9ec5`.

**Verdict.** The pairwise commuting/anticommuting readout theorem extends
to every nonnegative query weighting and every integer memory budget.
Consequently its entire separate-accuracy region equals original-site
retention. The encoder remains arbitrary. The proof below was reconstructed
independently within this workspace; publication originality is not asserted.

This strengthens the weighted `q=n-1` result in the
[preceding report](DECODER_ALGEBRA_AND_THREE_INPUT.md). It does not remove
the readout hypothesis or resolve unrestricted equal-accuracy optimality.

## 1. Statement and short argument

Let `0<=q<=n` be an integer. On a memory of dimension `D<=2^q`, let
`B_(i,X),B_(i,Z)` be Hermitian reflections, every two of which either
commute or anticommute. Scalar signs are allowed. For `a_i,b_i>=0`, put

$$
H=\sum_i\bigl(a_iX_i\otimes B_{i,X}+b_iZ_i\otimes B_{i,Z}\bigr),
\qquad
\delta_i=a_i+b_i-\sqrt{a_i^2+b_i^2}.
$$

Order the deficits as `delta_(1)<=...<=delta_(n)`. Then

$$
\boxed{\|H\|_\infty\le
\sum_i(a_i+b_i)-\sum_{i=1}^{n-q}\delta_{(i)}
=\sum_i\sqrt{a_i^2+b_i^2}
 +\sum_{i=n-q+1}^{n}\delta_{(i)}.}
\tag{1}
$$

Empty sums vanish. Maximizing over the stated readout class and
`D<=2^q` attains (1), using `D=2^q` if needed. Attainment is not asserted
for every fixed smaller memory dimension.

**Core argument.** First normalize every site's deficit to one. Assign
each query coefficient c the positive label `sqrt(2)(c-1)`; the two
labels at any site multiply to one. Edges saving less than one become
strictly triangular after multiplication by the original site matching.
The memory dimension bound then forces `n-q` disjoint anticommuting
edges saving at least one each. For arbitrary deficits, decompose H into
finitely many levels of these normalized pairs. Triangle inequality sums
the level bounds to exactly the sum of the `n-q` smallest deficits.

Different levels may use different matchings. There is no assertion that
one matching attains the total weighted saving.

## 2. Algebra and a threshold lemma

Enumerate the `2m` queries on any chosen m sites, and let J be the binary
adjacency matrix pairing their X and Z queries. If M is the memory
commutation matrix, the full terms `T_j=P_j tensor B_j` have matrix

$$
A=J+M,\qquad \operatorname{rank}_{\mathbb F_2}M\le2q.
\tag{2}
$$

The rank bound is prior graph-Clifford representation theory: rank `2r`
requires a nonzero representation of dimension at least `2^r`. It also
holds after selecting any subset of query pairs. See Section 6 for sources.

We use the elementary fact that a binary alternating adjacency matrix of
rank `2r` has a matching of size r. A nonsingular principal `2r` minor
exists by alternating symmetric elimination. In its determinant over
`F_2`, cycles of length at least three cancel with their reversals; the
remaining terms are perfect matchings. A nonzero determinant therefore
supplies one. This argument and (2) do not require an irreducible memory.

Write `d(u,v)=u+v-sqrt(u^2+v^2)`. Suppose all m original pairs have
`d(c_j,c_(j*))>=t>0`, where j* is j's partner. The graph A contains a
matching of at least `m-q` edges with `d(c_j,c_k)>=t`, when `m>q`.

To prove this, all coefficients exceed t, and squaring gives

$$
d(u,v)\ge t\quad\Longleftrightarrow\quad
(u-t)(v-t)\ge t^2/2\qquad(u,v>t).
$$

Set `s_j=sqrt(2)(c_j-t)/t>0`. Original partners satisfy
`s_j s_(j*)>=1`. Split A into disjoint binary adjacency matrices `N+E`,
with N containing the edges for which `s_j s_k<1`, and E the others.
If `(JN)_(jk)=N_(j*,k)` is nonzero, then

$$
s_k<1/s_{j^*}\le s_j.
$$

Ordering vertices by their labels makes JN strictly triangular, including
when labels tie. Thus `J+N=J(I+JN)` is invertible over `F_2`. Since
`M=(J+N)+E`,

$$
\operatorname{rank}E\ge2m-\operatorname{rank}M\ge2(m-q).
$$

The matching fact supplies the claimed edges. Equality in the threshold
belongs to E, which is essential to strict triangularity of JN.

For each such edge, the two full reflections anticommute, so

$$
\|c_jT_j+c_kT_k\|_\infty=\sqrt{c_j^2+c_k^2}.
$$

Grouping disjoint edges and bounding all remaining terms individually
saves at least `(m-q)t`. Different groups need not commute. In particular,
when every original deficit is one, the bound is

$$
\left\|\sum_j c_jT_j\right\|_\infty
\le\sum_j c_j-(m-q)_+.
\tag{3}
$$

For `m<=q`, (3) is simply triangle inequality.

## 3. Arbitrary weights by finite levels

Write H as `sum_i H_i` with the weighted site terms from Section 1.
Let `0=d_0<d_1<...<d_k` be the distinct positive values among the deficits.
For each level define

$$
S_\ell=\{i:\delta_i\ge d_\ell\},\qquad
K_\ell=\sum_{i\in S_\ell}\frac{H_i}{\delta_i}.
$$

Homogeneity makes every original deficit in `K_ell` exactly one. The
restricted commutation matrix still obeys (2), so (3) gives

$$
\|K_\ell\|_\infty\le
\sum_{i\in S_\ell}\frac{a_i+b_i}{\delta_i}
-(|S_\ell|-q)_+.
$$

The exact finite decomposition is

$$
H=H_0+\sum_{\ell=1}^k(d_\ell-d_{\ell-1})K_\ell,
\qquad H_0=\sum_{i:\delta_i=0}H_i.
$$

A site of deficit `d_j` appears in levels 1 through j; their coefficients
sum to `d_j/d_j=1`. Zero deficit means `a_i b_i=0`, and
`||H_0||<=sum_(delta_i=0)(a_i+b_i)`. Triangle inequality consequently gives

$$
\|H\|_\infty\le\sum_i(a_i+b_i)
-\sum_{\ell=1}^k(d_\ell-d_{\ell-1})(|S_\ell|-q)_+.
$$

The last sum is exactly `sum_(i=1)^(n-q) delta_(i)`: discard the q largest
deficits; at each positive level, precisely `(|S_ell|-q)_+` of those
remaining lie above the level. This proves (1), including zero weights,
repeated deficits, and both endpoint budgets.

These levels are an operator decomposition. They introduce no physical
measurement stages, copies, selection of successful branches, or change
to the encoder.

## 4. Attainment and the complete operational region

Retain the q sites with largest deficits. On them use their memory Pauli
readouts; on every other site use scalar readouts. The site Hamiltonians
act on disjoint reference/memory factors. Their largest eigenvalues are
`a_i+b_i` on retained sites and `sqrt(a_i^2+b_i^2)` on the others, so
their sum attains (1). Operationally, on a discarded site with
`r_i=sqrt(a_i^2+b_i^2)>0`, use the compatible parent POVM with marginal
contrasts `(a_i/r_i,b_i/r_i)` and store its outcomes classically. At
`r_i=0` any compatible disk point suffices. A bare projective measurement
along one weighted axis would require the established Pauli twirl to
produce these exact X/Z marginal effects.

For an arbitrary admissible instrument, refine each branch into Kraus
maps K_c and use normalized seeds `L_c=K_c/||K_c||_F` with weights
`p_c=||K_c||_F^2/2^n`. These weights sum to one; they are not assumed to
be input-independent branch probabilities. Vectorization and (1) bound
each branch's weighted score, and averaging bounds
`sum_i(a_i x_i+b_i z_i)` by the same right side. Finite Pauli twirling
preserves the readout algebra and transfers uniform binary-TV guarantees
to the contrast formulation, as in the audited seed reduction.

Thus, for nonnegative contrasts `0<=x_i,z_i<=1`, the region is exactly

$$
\boxed{\sum_i w(x_i,z_i)\le q,\qquad
w(x,z)=\left[x+z-1-\sqrt{2(1-x)(1-z)}\right]_+.}
\tag{4}
$$

Here the [existing retention-region proof](../EXACT_AXIS_SPECTRAL_REDUCTION.md)
supplies the matching convex geometry and construction. The class permits
finite classical mixtures of admissible reflection families; put the
mixture choice in the free record. Attenuation uses classically flagged
output flips, which preserve the commutation signs. Consequently all
downward profiles in (4), not just exposed boundaries, are attainable.

The resource contract is unchanged: one arbitrary unknown specimen,
including internally entangled states; encoding before one delayed query;
arbitrary collective encoders; unlimited finite classical records;
dimension at most `2^q` on every branch; uniform input/query errors. All
crossing quantum systems count. There is no free entanglement, bypass,
source reaccess, extra specimen, or postselected success.

## 5. What remains unresolved

The readout condition is explicit. The preceding report gives a seed
whose unique optimal readouts neither commute nor anticommute. Therefore
(4) cannot be silently applied to unrestricted protocols. The ten
continuous nonscalar sectors for `Gamma(3,4)` remain unresolved.

This continuation also explored the all-balanced sector through the
candidate inequality `sum_j f_j^2<=4`, where
`f_j=lambda_1(C_j)+lambda_2(C_j)-lambda_3(C_j)-lambda_4(C_j)` and
`C_j=L P_j L^dagger`, with descending eigenvalues. No universal nonflat
proof or admissible violation was obtained. It is not used in (1)–(4).
An attempted shortcut would lower-bound
`sum_j[(lambda_1-lambda_2)^2+(lambda_3-lambda_4)^2]` by
`4 Tr(rho^2)-1`, where `rho=L^dagger L`. It is false: for a pure
three-qubit GHZ seed all C_j vanish, whereas the proposed lower bound
is three. This refutes that shortcut, not the balanced-sector candidate
or the unrestricted benchmark.

## 6. Provenance and verification

The representation ingredient is Khovanova,
[arXiv:0810.3322v1](https://arxiv.org/pdf/0810.3322v1), Section 2, p. 2;
Corollary 7.4, p. 9; Lemma 8.1/Corollary 8.2, p. 10. Multiplying our
reflections by i matches the source's generators squaring to -1.
McNulty, [arXiv:2511.15954v1](https://arxiv.org/pdf/2511.15954v1),
Definition 1/Eq. (4), p. 3, and Appendix B Remark 1/Eq. (B4), p. 15,
states the same minimum dimension for complete commute/anticommute
patterns and credits that algebra. The detailed scope comparison is in
the preceding report, Section 8.

Generic weighted graph-norm methods are also prior. Xu, Wang, Ye,
Koßmann, Schwonnek and Winter,
[arXiv:2511.13531v1](https://arxiv.org/html/2511.13531v1), Section IX.1,
Eq. (37), gives

$$
\left\|\sum_j c_jT_j\right\|_\infty
\le\inf_{u_j>0}\sqrt{\left(\sum_jc_j^2/u_j\right)\beta(A,u)},
$$

where Definition 1/Eq. (1) defines the weighted quadratic expectation
parameter. Theorem 8 and Appendix A.3 give the minimum Pauli-string length
`rank(A)/2`. Anticommuting-pair grouping fits that general norm framework.
The inspected results do not directly evaluate the smallest original-pair
deficits subject to `A=J+M` and `rank(M)<=2q`; the threshold ordering and finite
levels supply that step here. Their Section IX.2 encodes graph problems
into Hamiltonians, rather than storing an unknown specimen for a delayed
query. These exact HTML locators specify a bounded comparison, not a
priority certification.

The matrix-rank fact, determinant/matching fact, anticommuting-pair norm,
triangle inequality, and finite level decomposition are established
ingredients. The threshold ordering and their combination into (1)–(4)
are the supplied deduction. Neither a new algebraic framework nor
exhaustive publication originality is claimed.

Independent internal reconstructions checked the triangular argument,
threshold equality, restriction to active sites, finite decomposition,
zero/repeated deficits, endpoint budgets, weighted attainment, and
normalized Kraus transfer. No optimizer or numerical certificate is
needed for this theorem. The unsuccessful sector investigations supply
no converse. The original audit and LICENSE are preserved unchanged.
