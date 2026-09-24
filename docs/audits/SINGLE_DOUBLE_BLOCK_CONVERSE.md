# One double-block pair cannot beat retaining two qubits

Date: 24 September 2026. Reviewed main:
`ac5863e1e026a8a9432a27385e6ee9491b423e92`, the merge of PR #36.

**Verdict.** Three more complete ququart readout-signature patterns obey
the retention benchmark. Together with the preceding four-pattern
exclusion, this reduces the unresolved nonscalar patterns from six to
three. The proof permits unequal Jordan angles, arbitrary complex
memory orientations, and arbitrary normalized seeds. It does not
evaluate unrestricted `Gamma(3,4)`, prove the entropy conjecture, or
establish publication originality.

The simple step is to keep both leading positive eigenvalues of the
exceptional query pair. The other two queries obey a monogamy bound on
their combined top subspace and a tighter bound on either individual
top vector. A resolvent comparison combines those two bounds. The
monogamy ingredient is an established-theorem corollary, explicitly
credited below; the supplied deduction is the resulting sector closure.

## 1. Statement and operational scope

Let `R_1,R_2,R_3` be reference qubits and let Q have dimension four.
For arbitrary Hermitian reflection readouts on Q, put

$$
h_i=X_i\otimes B_i+Z_i\otimes D_i,\qquad H=h_1+h_2+h_3.
\tag{1}
$$

Assume at most one original pair `(B_i,D_i)` has two noncommuting
two-dimensional Jordan blocks. Every other pair has at most one such
block. Their memory planes need not coincide.

**Theorem.**

$$
\boxed{\|H\|_\infty\le4+\sqrt2.}
\tag{2}
$$

This is an unweighted three-input theorem. No extension to every
weighted support or to arbitrary contractions preserving a block
condition is asserted.

The [normalized-seed reduction](../COLLECTIVE_ENCODING_REDUCTION.md)
uses the full trace-norm score

$$
g(L)=\sum_{i=1}^3
\left(\|LX_iL^\dagger\|_1+\|LZ_iL^\dagger\|_1\right),
\qquad L:\mathbb C^8\longrightarrow\mathbb C^4,\quad
\|L\|_F=1.
\tag{3}
$$

Each trace norm has a maximizing reflection, with arbitrary signs on a
zero eigenspace. If one score-attaining family satisfies the theorem's
block condition, vectorization and (2) give `g(L)<=4+sqrt(2)`.
Thus a violating seed must have at least two double-block pairs in
**every** score-attaining reflection family. This is a necessary
condition obtained inside the unrestricted optimization, not an
encoder restriction imposed on the original problem.

For a complete refined instrument, omit zero Kraus branches and use
`p_a=||K_a||_F^2/8` and `L_a=K_a/||K_a||_F`. Completeness gives
`sum_a p_a=1`, and the normalized-Kraus converse gives
`6 eta<=sum_a p_a g(L_a)`. Consequently any strict improvement must
contain a branch whose score exceeds the benchmark and whose optimal
readouts evade (2). No branch is postselected. The original single
unknown specimen, one delayed local query, arbitrary collective
encoding and entangled input, unlimited finite classical records,
worst-case quantum dimension and uniform error quantifiers are
unchanged. The virtual references are proof devices, not extra
specimens or a free quantum channel.

## 2. Retain the exceptional pair's positive spectrum

Write

$$
r=\sqrt2,\qquad \delta=2-r,\qquad T=4-r.
\tag{4}
$$

Relabel sites so pairs 2 and 3 have at most one noncommuting block.
The local spectral cap from the
[one-block converse](JORDAN_BLOCK_CONVERSE.md), Section 2, gives

$$
h_2+h_3\le2rI+\delta K,\qquad K=\Pi_2+\Pi_3,
\tag{5}
$$

where each Pi is a rank-one Bell projector between its reference and
a memory plane. All spectator identities are understood. If a pair
has no noncommuting block, its Hamiltonian is at most rI and any
such Bell projector may be used in the weaker cap (5).

If pair 1 also has at most one active block, the previous theorem
already proves (2). Otherwise both its reflections are balanced:
each of its two noncommuting blocks contributes one positive and one
negative eigenvalue. Its two block spectra are

$$
\{\pm u_0,\pm v_0\},\quad \{\pm u_1,\pm v_1\},\qquad
2\ge u_0\ge u_1=u\ge r,\qquad
v_k=\sqrt{4-u_k^2},\quad v=v_1\ge v_0.
\tag{6}
$$

Let P_0 and P_1 be their top Bell projectors, on orthogonal memory
planes, and put P=P_0+P_1. All other eigenvalues are at most v. Hence

$$
h_1\le vI+C,\qquad
C=(u_0-v)P_0+(u-v)P_1.
\tag{7}
$$

P has rank two on `R_1 tensor Q`, and rank eight after the two
spectator reference identities. The proof always preserves these
multiplicities.

Commuting endpoints cause no gap. A balanced pair with one active
block has two remaining scalar blocks with opposite signs for both
reflections, so they form a traceless commuting two-dimensional
block. If every block is scalar, the joint sign counts satisfy
`n_(++)=n_(--)` and `n_(+-)=n_(-+)`, allowing the same grouping.
In a commuting block choose a Bell basis inside the degenerate
top eigenspace; equivalently use continuity. Thus (6)–(7) also
describe every endpoint of the balanced family.

## 3. Two compression bounds from established monogamy

Bell insertion maps belonging to distinct references have overlap
norm at most one half, including different complex memory planes.
The two-projector Gram bound and its squared-overlap consequence give

$$
0\le K\le\tfrac32I,\qquad
P_0KP_0\le\tfrac12P_0.
\tag{8}
$$

For the second inequality each of the two summands is at most P_0/4.
The same bound holds with P_1. On their combined subspace there is
the further bound

$$
\boxed{PKP\le\tfrac34P.}
\tag{9}
$$

To see it, write the two Bell vectors in a fixed reference basis
as `sum_a |a> V_k|a>/sqrt(2)`. The isometries V_0,V_1 have
orthogonal ranges, so the four vectors `V_k|a>` form an orthonormal
basis of Q. Identifying these with `|a>_A|k>_B` gives

$$
Q=A\otimes B,\qquad P=\Phi_{R_1A}\otimes I_B,
\tag{10}
$$

where A and B are qubits. No common subsystem choice for the other
queries is being assumed. Under the insertion isometry with range P,

$$
P\Pi_jP\ \simeq\ \tfrac12\rho_{R_jB},\qquad
\rho_{R_jB}=\operatorname{Tr}_A\Pi_j,\qquad
\operatorname{Tr}_B\rho_{R_jB}=I_{R_j}/2.
\tag{11}
$$

Here each Pi_j on the right is first expressed in the memory basis
of (10). Each rho has trace one. For two such mixed Choi operators
sharing a qubit B,

$$
\rho_{R_2B}+\rho_{R_3B}\le\tfrac32 I.
\tag{12}
$$

This is a direct prior-monogamy corollary, not a new ingredient.
For completeness, in equal dimension d use the output-first
unnormalized Choi convention
`J(S)=sum_ab S(|a><b|) tensor |a><b|`.
Define CP maps by `J(S)=d rho` and `J(U)=d sigma`.
The fixed leaf marginals give `S(I)=U(I)=I`, so both maps are unital.
Apply `S tensor U tensor id` to

$$
\Phi_{R_2'B}+\Phi_{R_3'B}\le(1+1/d)I.
\tag{13}
$$

The maps act on different leaves; a single positive unital map
therefore preserves the entire inequality. At d=2 the result is
(12), and (11) gives (9). A pure-state mixture of isometric Choi
vectors is neither required nor assumed. Equation (13) itself also
follows directly from the Bell-projector overlap 1/d.

## 4. A resolvent comparison closes unequal angles

It remains to show `h_1+delta K<=T I`. Set
`ell=3/2` and `z=T-v`. Since `v<=r`,

$$
z\ge T-r=2\delta>\ell\delta,\qquad T-u_k\ge\delta>0.
\tag{14}
$$

The scalar convex function `x -> 1/(z-delta x)` lies below its
endpoint chord on `[0,ell]`. Functional calculus with (8) yields

$$
(zI-\delta K)^{-1}
\le \frac Iz+\frac{\delta K}{z(z-\ell\delta)}.
\tag{15}
$$

The desired inequality `C+delta K<=zI` is equivalent by positive
congruence and the equality of nonzero Gram spectra to

$$
C^{1/2}(zI-\delta K)^{-1}C^{1/2}\le I_P.
\tag{16}
$$

Using (15), subtracting C/z, and conjugating by
`(I_P-C/z)^(-1/2)` shows it suffices that

$$
\|\sqrt D(PKP)\sqrt D\|\le\frac{z-\ell\delta}{\delta},
\quad
D=d_0P_0+d_1P_1,\quad
d_0=\frac{u_0-v}{T-u_0},\quad
d_1=\frac{u-v}{T-u}.
\tag{17}
$$

In particular `d_0>=d_1>=0`. No inverse of C or D is used, so
zero coefficients and degeneracies are allowed.

Put A=PKP. Both compression estimates are now needed:

$$
\begin{aligned}
\|\sqrt D A\sqrt D\|
&=\|\sqrt A D\sqrt A\|\\
&\le d_1\|A\|+(d_0-d_1)\|\sqrt A P_0\sqrt A\|\\
&\le\tfrac34d_1+\tfrac12(d_0-d_1)
=\tfrac12d_0+\tfrac14d_1.
\end{aligned}
\tag{18}
$$

The last line uses `||sqrt(A)P_0 sqrt(A)||=||P_0 A P_0||<=1/2`.
For fixed v, d_0 increases with u_0; using `u_0<=2` gives
`delta d_0<=2-v`. Also `u^2+v^2=4` implies `u+v<=2r`, and
`T-u>=delta`, so

$$
\delta d_1\le u-v\le2(r-v).
\tag{19}
$$

Consequently

$$
\delta(\tfrac12d_0+\tfrac14d_1)
\le\frac{2-v}{2}+\frac{r-v}{2}
=1+\frac r2-v
=z-\tfrac32\delta.
\tag{20}
$$

This proves (17), hence `h_1+delta K<=T I`.
Adding the baseline in (5) gives
`H<=(2r+T)I=(4+r)I`. Conjugation by Y on all three references
sends H to -H, proving the operator-norm bound (2).
The asymmetric operator `h_1+delta K` is not assumed to have a
symmetric spectrum.

## 5. Exactly which patterns are now excluded?

The digits in a signature are the minority eigenspace ranks of the
two reflections, after independent sign choices. A `(11)` or
`(12)` pair has at most one noncommuting Jordan block, since each
such block consumes one minority direction of each reflection.
Only `(22)` can have two.

| Complete pattern | Status |
|---|---|
| `(11)^3`, `(11)^2(12)`, `(11)(12)^2`, `(12)^3` | Excluded by the preceding one-block theorem |
| `(22)(11)^2`, `(22)(11)(12)`, `(22)(12)^2` | Excluded by (2), for all angles and complex orientations |
| `(22)^2(11)`, `(22)^2(12)`, `(22)^3` | Still unresolved as complete continuous optimizations |

Scalar-readout cases were already bounded by the retention benchmark.
Even in a remaining signature, (2) excludes every family whose
actual Jordan decompositions have at most one double-block pair.
The [all-block scalar certificate](JORDAN_SPECTRAL_BUDGET.md),
Section 3, additionally excludes continuous regions in all three.
Its failure remains necessary, not sufficient, for a physical violation.

Combining these facts with the prior rank-three and flat-seed results,
any strict `(n,q)=(3,2)` improvement requires a nonflat rank-four
seed and at least two optimal query pairs with two noncommuting
blocks. This does not prove the unrestricted benchmark.

The precise remaining bottleneck is to control the interaction of
two or three rank-two positive Bell subspaces, potentially defining
different qubit subsystems of the same memory. Here (11) reduces two
rank-one corrections to trace-one mixed Choi operators. With another
double-block pair those corrections become sums of two such operators;
simply repeating (12) loses the needed constant. The next target is
an inequality retaining their common four-dimensional memory
constraint, or an explicit violating normalized seed.

## 6. Primary-source comparison and status

| Ingredient or claim | Primary locator / verdict |
|---|---|
| A rank-two maximally entangled subspace of a qubit–ququart space has a qubit-subsystem representation | Gour–Wallach, *Entanglement of subspaces and error correcting codes*, [0704.0251v2](https://arxiv.org/pdf/0704.0251), Proposition 3, printed pp. 3–4; Corollary 4, p. 4. Equation (10) is its elementary orthogonal-plane instance, with a direct construction above. Established ingredient. |
| Equal-dimensional pure Bell-star bound | Jorquera et al., *Monogamy of Entanglement Bounds and Improved Approximation Algorithms for Qudit Hamiltonians*, Quantum 10, 2088 (2026), [2410.15544v4](https://arxiv.org/pdf/2410.15544), Proposition 3.6, Eq. (18), printed p. 8; PDF dated 20 April 2026. Two edges give `1+1/d`. The source also treats stronger pseudo-state/SOS bounds; no extension of those certificates is asserted here. |
| Required mixed qubit-Choi bound (12) | Elementary separate-leaf unital CP pullback of that established operator bound. It is a prior-theorem corollary, even though a direct proof is short. |
| Independent recovery-monogamy route to (12) | Renes, *Better bounds on optimal measurement and entanglement recovery, with applications to uncertainty and monogamy relations*, PRA 96, 042328 (2017), [1707.01114v1](https://arxiv.org/pdf/1707.01114), Section 3.2, Eqs. (17)–(18), printed p. 4; recovery convention in Section 2.2/Eq. (6), p. 2. Choose the recovery channels to be the adjoints of S and U above and apply to an arbitrary tripartite test state. Its two fixed recovery fidelities are the two Choi expectations. The stronger optimized-recovery region implies their sum is at most `1+1/d`. |
| Equations (7), (9), (17)–(20) and three complete sector exclusions | Supplied deduction, independently reconstructed within this workspace. The source comparisons identify ingredients, not an exhaustive priority determination for their interface application. |
| Unrestricted optimum, sharp entropy inequality, equal-accuracy rate, publication priority/significance | Unresolved. No human peer review, journal acceptance judgment, or exhaustive literature claim is asserted. |

The earlier nonlinear-CHSH subsumption of the profile-support
characterization remains in force. This finite-block deduction does not
re-establish novelty of that characterization or of the full
two-parameter explicit evaluation.

## 7. Verification and preserved files

Two separate audit agents reconstructed the complete proof, including
the Choi bound, endpoint choices, positive denominators, resolvent
congruences, spectator multiplicities, and operational transfer. The
integrating workspace independently checked the same steps. These are
internal mathematical checks, not external peer review.

The deterministic
[diagnostic](../../tools/check_single_double_block.py) and
[recorded output](../../results/single_double_block.json) check 48
families: three new signature patterns, four angle choices including
commuting and maximally noncommuting endpoints and unequal angles,
and four orientations including independent dense complex rotations.
They check both local caps, the three compression bounds, the resolvent
chord, weighted comparison, scalar conclusion, and actual Hamiltonian
bound. Four mixed-Choi constructions additionally check the direct
Gram calculation below. The largest Hamiltonian has dimension 32.
Actual environment, residuals, source hash and rerun details are in
[REPRODUCIBILITY.md](../REPRODUCIBILITY.md#single-double-block-converse).

Finite diagnostics supplement the symbolic proof; they do not certify
all matrices or originality. There is no optimizer in the diagnostic.
The original `PROOF_AND_NOVELTY_AUDIT.md` and LICENSE are preserved
byte for byte. Earlier commit-pinned reports remain historical records;
the current status ledger contains the updated three-pattern count.

## Appendix: direct mixed-Choi Gram check

This also explains the diagnostic with a center larger than a qubit.
Let leaves A,C have dimension d and let B have arbitrary finite
dimension. Suppose rho_AB and sigma_CB are density operators with
`Tr_B rho=I_A/d` and `Tr_B sigma=I_C/d`. Choose vectorized Kraus
representations

$$
\rho=\frac1d\sum_\alpha|K_\alpha\rangle\rangle
\langle\langle K_\alpha|,\qquad
\sigma=\frac1d\sum_\beta|L_\beta\rangle\rangle
\langle\langle L_\beta|,\qquad
\sum_\alpha K_\alpha^\dagger K_\alpha
=\sum_\beta L_\beta^\dagger L_\beta=I_d.
\tag{21}
$$

Let F insert `|K_alpha>>/sqrt(d)` on AB, leaving C untouched,
and let G insert `|L_beta>>/sqrt(d)` on CB, leaving A untouched.
Then `FF^dagger=rho_AB tensor I_C` and
`GG^dagger=sigma_CB tensor I_A`, with cross entries

$$
(F^\dagger G)_{\alpha c,\beta a}
=\frac1d\sum_b\overline{K_\alpha[b,a]}L_\beta[b,c].
\tag{22}
$$

With the Stinespring isometries
`V_K|a>=sum_(alpha,b) K_alpha[b,a]|alpha,b>` and similarly V_L,
the complex conjugate of `d F^dagger G` is, up to tensor ordering,
`(I_(E_K) tensor V_L^dagger)(V_K tensor I_(E_L))`.
It is an isometry followed by a coisometry, so
`||F^dagger G||<=1/d`. Both diagonal Gram blocks have norm at
most one, because rho and sigma are trace-one positive operators.
The two-by-two scalar Gram estimate therefore gives

$$
\|\rho_{AB}\otimes I_C+\sigma_{CB}\otimes I_A\|\le1+1/d.
\tag{23}
$$

This uses complex conjugation, not an unsupported partial-transpose
norm identity. The interface proof only needs `dim B=d=2`,
already subsumed as explained above. The arbitrary-center extension
is supplied algebra; its separate priority is not established and
it is not proposed as a publication claim.
