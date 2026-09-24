# Exact elimination of one original site's binary readout pair

Date: 24 September 2026. Reviewed main:
`3befc9a6ad1ec64859ffd5d36a4a98ea32488cf9`, the merge of PR #40.

**Verdict.** In every even memory dimension, an entire arbitrary binary
readout-pair optimization has an exact spectral formula. Pair the largest
memory-marginal eigenvalue with the smallest, then the next largest with
the next smallest. Each pair contributes one explicit scalar function.
Its comparison with any proposed bound reduces to a strictly convex
quartic and one cubic root.

This removes all readout orientations and permits general binary POVMs.
It is not another restricted family of memory embeddings. Its application
to the remaining interface converse is an exact test for a specified
rank-one spectral upper bound, which can lose information about the
original Hamiltonian. No further complete signature pattern or unrestricted
optimum is settled. Publication originality remains unresolved.

The filename's “last query” means the last **original site's pair of
possible X/Z readouts in a virtual score Hamiltonian**. The physical
protocol still receives exactly one delayed query; it never answers a
sequence of queries on the same specimen.

## 1. The readout-elimination theorem

Let Q have even dimension `M=2d`, and let rho be a density matrix on Q
with eigenvalues

$$
\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_M\ge0.
$$

For `t>2` and arbitrary Hermitian contractions B,D on Q define

$$
\begin{aligned}
h&=X\otimes B+Z\otimes D,\\
R_t(\rho;B,D)
&=\operatorname{Tr}_Q\!\left[
(I\otimes\sqrt\rho)(tI-h)^{-1}(I\otimes\sqrt\rho)
\right].
\end{aligned}
\tag{1}
$$

This is a positive operator on a qubit. Put `r=sqrt(2)` and
`s_0=1/(t-r)`. For `1<=a<=r`, set `b=sqrt(2-a^2)` and

$$
f_a=\frac{t-a}{(t-a)^2-b^2},\qquad
g_a=\frac{t+a}{(t+a)^2-b^2}.
\tag{2}
$$

For `x>=y>=0` define

$$
\Phi_t(x,y)=\max\left\{
(x+y)s_0,\ \max_{1\le a\le r}(xf_a+yg_a)
\right\},
\tag{3}
$$

and extend Phi symmetrically to all nonnegative x,y.

**Theorem.**

$$
\boxed{
\sup_{-I\le B,D\le I}\|R_t(\rho;B,D)\|_\infty
=\sum_{j=1}^{d}\Phi_t(\lambda_j,\lambda_{M+1-j}).
}
\tag{4}
$$

The supremum is attained by reflections on Q itself. No real-matrix
condition, fixed memory plane, tensor factorization, or additional quantum
memory is assumed. Section 5 gives an exact algebraic decision rule for
Phi; numerical angle optimization is unnecessary.

## 2. General binary POVMs reduce to reflections

For every positive definite A,

$$
v^\dagger A^{-1}v
=\sup_z\left[2\operatorname{Re}(v^\dagger z)-z^\dagger Az\right].
\tag{5}
$$

The right side is a supremum of affine functions of A. Hence inversion
is operator convex. The inverse in (1) is well defined because
`||h||<=2<t`. The rho-weighted partial trace is a positive linear map,
and the largest eigenvalue is monotone and convex. Thus the objective
in (4) is convex separately in B and D.

Every Hermitian contraction is a convex combination of reflections in
its own spectral algebra: its eigenvalue vector lies in the cube
`[-1,1]^M`, which is the convex hull of sign vectors. Replacing B, then
D, by suitable vertices cannot decrease the objective. This uses the
same memory dimension, without a dilation. Compactness and continuity
ensure attainment.

## 3. One Jordan block has an exact two-eigenvalue description

Jordan's lemma decomposes two reflections into scalar and traceless
2D blocks. Set `S=(X+Z)/r` and `T=(X-Z)/r`. A memory rotation puts a
2D block's Hamiltonian in the form

$$
h=aS\otimes Z+bT\otimes X,
\qquad a\ge b\ge0,\quad a^2+b^2=2,
\tag{6}
$$

possibly with S and T interchanged. For an upper bound, maximize the
reference direction separately in each block. For attainment, choose
the readouts so that the larger coefficient is on S in every block.
These are allowed choices in the supremum, not transformations claimed
to leave a fixed Hamiltonian unchanged.

In coordinates `S=Z_R,T=X_R`, put

$$
s=t^2-2,\qquad \Delta=s^2-4a^2b^2>0.
$$

For a reference state with Bloch components `(z,x,y)`, the compressed
resolvent `A_chi=<chi|(tI-h)^(-1)|chi>` has scalar coefficient
`ts/Delta` and memory Bloch coefficients, up to the sign of its last
component,

$$
\frac{za(s+2b^2)}\Delta,\qquad
\frac{xb(s+2a^2)}\Delta,\qquad
\frac{2taby}\Delta.
\tag{7}
$$

This follows by multiplying `(tI+h)(t^2I-h^2)^(-1)`. The first scale
is largest:

$$
\begin{aligned}
a^2(s+2b^2)^2-b^2(s+2a^2)^2&=(a^2-b^2)\Delta\ge0,\\
a^2(s+2b^2)^2-(2tab)^2&=a^2\Delta>0.
\end{aligned}
\tag{8}
$$

The trace is independent of the reference state, and the eigenvalue
spread is maximal at `S=+1`. The two eigenvalues there are exactly
`f_a,g_a` in (2), also obtained directly from the parity blocks of
(6). Every other reference choice therefore has an eigenvalue vector
majorized by `(f_a,g_a)`. Its greatest trace against ordered nonnegative
weights `x>=y` is at most `xf_a+yg_a`.

A scalar block contributes at most `s_0`, attained at the **same** state
`S=+1` by choosing B=D=+1. Thus all block extrema are simultaneously
attainable at one reference state. There is no incompatible collection
of reference-state optimizations hidden in (4).

## 4. Pair the extreme eigenvalues

For fixed block eigenvalues, the trace rearrangement inequality aligns
the memory eigenvectors with those of rho in the maximizing order.
An arbitrary such unitary is allowed in B,D. A pair of scalar blocks
contributes the first branch of (3); a 2D block contributes the second.
Since M is even, the number of scalar blocks is even. The optimization
therefore becomes a maximum over perfect matchings of the eigenvalues,
with Phi as the value of a matched pair.

Phi is symmetric, convex and homogeneous of degree one: it is a maximum
of the scalar linear form and the forms `xf_a+yg_a` and `xg_a+yf_a`.
On positive arguments it is the perspective

$$
\Phi_t(x,y)=y\,k(x/y)
$$

of a convex function k. At differentiability points,

$$
\partial_x\partial_y\Phi_t(x,y)
=-\frac{x}{y^2}k''(x/y)\le0.
\tag{9}
$$

The same decreasing-differences inequality follows for nonsmooth k
by integrating its monotone one-sided slopes, or by convex smoothing
and a limit. Thus, for `A>=B>=C>=E>0`,

$$
\begin{aligned}
\Phi(A,E)+\Phi(B,C)&\ge\Phi(A,C)+\Phi(B,E),\\
\Phi(A,E)+\Phi(B,C)&\ge\Phi(A,B)+\Phi(C,E).
\end{aligned}
\tag{10}
$$

These are rectangle inequalities, using symmetry in the second line.
Continuity includes zeros.

In any matching that does not join the largest and smallest eigenvalues,
apply (10) to the two edges incident on those eigenvalues. Replace them
by the extreme pair and a pair of their previous partners, without
reducing the value. Repeat on the remaining M-2 eigenvalues. Induction
gives the matching `(lambda_j,lambda_(M+1-j))`. Section 3 supplies a
common attaining reference state and memory alignment. This proves (4)
in every even dimension.

## 5. Exact algebraic test for the scalar function

Fix `x>=y>=0`, put `w=x+y`, `delta=x-y`, and test a proposed upper
bound K. First require

$$
K\ge\frac{w}{t-r}.
\tag{11}
$$

For `w>0`, this implies K>0. Clearing the positive denominator in
`xf_a+yg_a<=K` gives the exact equivalent condition

$$
P_K(a)\ge0\quad(1\le a\le r),
\tag{12}
$$

where

$$
\begin{aligned}
P_K(a)={}&4Ka^4+2\delta a^3-8Ka^2
-\delta(t^2+2)a\\
&+K(t^2-2)^2-wt(t^2-2).
\end{aligned}
\tag{13}
$$

The simplifying fact is strict convexity on the whole interval:

$$
P_K''(a)=48Ka^2+12\delta a-16K>0.
\tag{14}
$$

Its derivative is the cubic

$$
16Ka^3+6\delta a^2-16Ka-\delta(t^2+2)=0.
\tag{15}
$$

This cubic has exactly one positive root z, with `z>=1`. Its own
first derivative increases strictly on the positive axis and crosses
zero once. The cubic starts nonpositive, decreases until that crossing,
then increases to infinity. For delta=0 its unique positive root is
one. For delta>0, its value at one is `delta(4-t^2)<0`, so z>1.
Therefore the unique minimum of P on the interval is at

$$
a_* = \min\{z,r\}.
\tag{16}
$$

Equations (11) and `P_K(a_*)>=0` are an **exact algebraic decision rule**
for `Phi_t(x,y)<=K`. For algebraic input parameters, the unique cubic root can be
represented as a real algebraic number; the inequality remains exact
for arbitrary real parameters. This is a finite scalar test, not an
endpoint assumption or an optimization over measurement matrices.

If `2<t<=2+r`, (11) also gives `P_K'(r)>0`. For `t^2<=10` this is
immediate. Otherwise

$$
P_K'(r)\ge\frac{16rw}{t-r}+w(10-t^2)>0
$$

on this interval. Thus the delta>0 root is strictly interior in the
interface application. For arbitrary `t>2`, the clipped rule (16)
remains valid.

The zero case is separate: `Phi_t(0,0)=0`, so K>=0 is the entire
comparison. At x=y=K=0 the polynomial is identically zero; no strict
convexity or unique-root claim is made there.

## 6. Exact test for a rank-one spectral upper bound

Let H_0 act on earlier reference systems A and memory Q. Suppose it has
a unique largest eigenvalue U, second eigenvalue m, and normalized top
vector Omega. Put

$$
c=U-m>0,\qquad \rho=\operatorname{Tr}_A|\Omega\rangle\langle\Omega|.
$$

Then `H_0<=mI+c|Omega><Omega|`. Let Lambda be the desired upper bound,
`t=Lambda-m>2`, and
`P=|Omega><Omega| tensor I_R` for one further reference qubit. Positivity
of `tI-h` and the positive rank-update criterion give

$$
\begin{aligned}
cP+h\le tI\text{ for every }B,D
\quad\Longleftrightarrow\quad
c\sum_{j=1}^{d}\Phi_t(\lambda_j,\lambda_{M+1-j})\le1.
\end{aligned}
\tag{17}
$$

The compression to Omega is exactly (1), with its actual, potentially
nonflat memory marginal. Thus (17) is necessary and sufficient for
**this spectral upper bound** to control every additional readout pair.
It is sufficient for `H_0+h<=Lambda I`. It is not necessary for the
original H_0, since replacing all lower eigenvalues by m can lose
information. No flat-top-vector assumption remains.

Equivalently, introduce scalar bounds K_j satisfying

$$
\sum_jK_j\le1/c,\qquad
K_j\ge\frac{\lambda_j+\lambda_{M+1-j}}{t-r},\qquad
P_{K_j}(a_{*,j})\ge0.
\tag{18}
$$

Each nonzero-weight pair uses the unique clipped cubic root above.
A zero-weight pair imposes only K_j>=0 and uses no cubic root. This
eliminates all additional-decoder matrices, orientations and Jordan
angles. For M=4, set `K_1+K_2=1/c`; just one allocation variable remains,
in the interval

$$
\frac{\lambda_1+\lambda_4}{t-r}
\le K_1\le
\frac1c-\frac{\lambda_2+\lambda_3}{t-r}.
\tag{19}
$$

Two convex-quartic tests decide whether the spectral upper bound
succeeds. A failed test need not indicate a physical interface advantage.
For the actual Hamiltonian built from original X/Z terms, conjugating
every trusted reference by Y sends the Hamiltonian to its negative.
An upper bound Lambda therefore also gives the matching operator-norm
bound. The generic H_0 statement by itself asserts only the upper
operator inequality.

## 7. The remaining sharp-pair problem and its precise missing input

For two ququart pairs of sharp anticommuting readouts, set `H_0=h_1+h_2`.
Their two greatest eigenvalues always obey

$$
m\ge2,\qquad U+m\le4+2\sqrt2,\qquad U\le4.
\tag{20}
$$

For the first inequality, compress the second reference to a Y
eigenstate. Its X,Z expectations vanish, leaving h_1 on `R_1 tensor Q`.
That compression has eigenvalue two with multiplicity two. Cauchy
interlacing gives m>=2.

For the second, let Pi_i be h_i's positive-eigenvalue Bell projector,
including the other reference's identity. It has rank four and
`h_i<=2Pi_i`. Its partial trace over its own reference is `I_Q/2`, so

$$
\operatorname{Tr}(\Pi_1\Pi_2)
=\operatorname{Tr}_Q[(I_Q/2)(I_Q/2)]=1.
$$

The squared principal cosines between these two rank-four ranges sum
to one. Their two largest cosines therefore sum to at most sqrt(2),
and the two largest eigenvalues of `Pi_1+Pi_2` sum to at most
`2+sqrt(2)`. Ky Fan monotonicity proves the middle inequality in (20).
Neither argument assumes a common memory factorization for the pairs.

If `U<=2+sqrt(2)`, the triangle bound with `||h_3||<=2` already proves
the benchmark `4+sqrt(2)`. Otherwise (20) automatically implies

$$
m<U,\qquad 2<t=4+\sqrt2-m\le2+\sqrt2.
$$

Thus the top vector is unique and all inverses above are valid in
every case requiring further work. The interval (19) is nonempty,
since `c<=t-r` is equivalent to U<=4.

The unresolved statement is now explicit: **does the actual top
marginal of every such H_0 admit an allocation in (19) passing the two
quartic tests?** No unproved Schmidt-coefficient conjecture is assumed.
Failure would disprove this rank-one-upper-bound strategy for that H_0,
not automatically disprove retention optimality.

There is an exact reason to retain the relation between eigenvalues and
the marginal. Synthetic data `U=4,m=2,rho pure` satisfy all three
inequalities (20), yet fail (17). At `t=2+r,c=2`,

$$
\Phi_t(1,0)=\frac1{2(\sqrt{2t^2-4}-t)}>\frac12.
\tag{21}
$$

Here f_a is maximized at
`a=t-sqrt((t^2-2)/2)`, which lies in `(1,r)`. The strict comparison is
equivalent to `t^2-2t-5=2r-3<0`.

These are synthetic relaxation data, not the marginal of a valid sharp
H_0 at U=4. Actual saturation forces every one of its four correlations
to equal one. For each generating Pauli P_j, saturation gives
`(P_j tensor I)Omega=(I tensor B_j)Omega`. Tracing out Q shows that the
trusted two-qubit marginal commutes with all four generators and is
`I_4/4`; its pure-state memory marginal is flat as well. Equation (21) refutes only a proof using (20) together
with an unrelated density matrix. The remaining bottleneck is their
joint constraint.

## 8. Operational quantifiers and status

For an arbitrary normalized collective seed L, the actual decoded score
is the expectation of the corresponding virtual Hamiltonian. The full
trace-norm score is

$$
g(L)=\sum_{i,U=X_i,Z_i}\|LUL^\dagger\|_1
=\max_{\{B_{i,U}\}}\sum_{i,U}
\operatorname{Tr}(B_{i,U}LUL^\dagger),
\qquad \|L\|_F=1.
$$

A Hamiltonian bound supplied by (17) bounds every seed for that fixed
earlier readout family and every last-site pair. If the earlier readouts
have a score-attaining family passing the certificate, it also bounds
the optimized trace-norm score. The existence of such a family is not
assumed for an arbitrary seed.

For a complete instrument, omit zero refined Kraus branches and use
`L_a=K_a/||K_a||_F` and `p_a=||K_a||_F^2/2^n`. The p_a sum to one;
they are normalization weights, not asserted input-independent outcome
probabilities. Define the actual decoded branch score
`s_a=sum_j Tr(B_(a,j) L_a P_j L_a^dagger)`. If every branch's actual
earlier readouts pass the certificate with bound Lambda, eliminating
the last site's arbitrary pair gives
`2n eta<=sum_a p_a s_a<=Lambda`. Separately, one may replace s_a by
g(L_a) in this chain if every seed admits a score-attaining readout
family passing the certificate. Neither optimality hypothesis is
silently imposed on actual decoders. Branch-dependent memory
orientations and classical records remain free.

The memory dimension M in the theorem is the actual mathematical memory
space under consideration. A smaller output may be represented with
unused zero coordinates inside an already permitted `2^q`-dimensional
space; the result grants no extra physical memory. Scalar or odd smaller
spaces need no unproved odd-dimensional extension of (4).

The original model is unchanged: one arbitrary unknown quantum specimen,
one delayed local X/Z query, arbitrary collective encoding, unlimited
finite classical records, worst-case retained quantum dimension, and
uniform binary total-variation error. No source reaccess, many-copy
estimation, average-memory substitution, free entanglement, quantum
bypass, sequential-query demand, or postselection is introduced.

Jordan decomposition, inverse convexity, trace rearrangement, spectral
interlacing and principal-angle identities are established ingredients.
The supplied deduction is their combination into the exact readout
elimination formula and its algebraic certificate. Components received
independent internal reconstructions; this is not external peer review
or a publication-priority conclusion. All three complete remaining
signature patterns and unrestricted equal-accuracy optimality stay open.

## 9. Verification

[The deterministic diagnostic](../../tools/check_last_query_resolvent.py)
and [its recorded output](../../results/last_query_resolvent.json) check
64 attaining constructions in dimensions 2,4,6,8 with complex memory
rotations, scalar and interior-block optima, zero eigenvalues, and the
clipped-root endpoint. They also check direct inverse and quartic
identities, all small matching alternatives, contraction convexity, and
four explicit passing/failing rank-one updates.

The script uses no optimizer: support values are approximated numerically by monotone
bisection in K, with the convex-quartic/cubic decision at each step.
The script also checks six inverse identities and 24 quartic identities
with exact rational arithmetic. The floating bisections are not interval
certificates. These diagnostics supplement the proof and certify no
unrestricted interface optimum or novelty. Exact counts, source hash,
environment and rerun record belong in
[REPRODUCIBILITY.md](../REPRODUCIBILITY.md#exact-last-query-resolvent).
LICENSE and the historical `PROOF_AND_NOVELTY_AUDIT.md` are unchanged.

## 10. Two exact controls on proposed global shortcuts

The preceding theorem concerns the actual X/Z Hamiltonian. A tempting
alternative was a general Bell-recovery budget

$$
\sum_{i=1}^n P_i\stackrel{?}{\le}
\frac{n+\log_2 M}{2}I,
\qquad
P_i=U_i(\Phi_{R_iA}\otimes I_{M/2})U_i^\dagger.
\tag{22}
$$

It would imply the desired `n=3,M=4` projector bound, but the general
statement is false, even with genuine subsystem projectors.

Take `n=64,M=128`, with memory basis `|0>,...,|127>` and reference
single-excitation words e_i. The normalized state is

$$
|\psi\rangle=\frac1{\sqrt2}|0^{64}\rangle|0\rangle
+\frac1{\sqrt{128}}\sum_{i=1}^{64}|e_i\rangle|i\rangle.
$$

For query i, identify one qubit-factor plane with the ordered pair
`(|0>,|i>)`. Pair each of the other 63 occupied memory labels with a
distinct unused label in `65,...,127`, putting the occupied label in the
output-zero position. These 64 ordered planes partition the full memory
basis, so they define a unitary identification with a qubit times a
64-dimensional auxiliary. No extra memory or success condition is used.

For its Bell-subspace projector, the vacuum and i-th excitation interfere
in the first plane; the other 63 terms contribute on distinct spectator
reference strings. Hence

$$
\langle P_i\rangle
=\frac14(1+1/8)^2+\frac{63}{256}
=\frac9{16},\qquad
\left\langle\sum_iP_i\right\rangle=36>\frac{71}{2}.
\tag{23}
$$

This is an operator-inequality counterexample, not an interface protocol
beating retention. Its normalized seed maps the vacuum to `|0>/sqrt(2)`
and e_i to `|i>/sqrt(128)`. Direct compression gives

$$
\|LZ_iL^\dagger\|_1=1,\qquad
\|LX_iL^\dagger\|_1=\frac18,\qquad g(L)=72.
$$

That is below `14+57sqrt(2)`, and even below the zero-memory benchmark
`64sqrt(2)`. Thus the auxiliary Bell budget was stronger than the
original task requires. Neither `n=3,M=4` nor unrestricted X/Z retention
optimality is refuted.

The vacuum-plus-excitation support is an ordinary cube star. Its
square-root spectral behavior is established graph mathematics:
Bollobás–Lee–Letzter, [arXiv:1605.06360v1](https://arxiv.org/pdf/1605.06360v1),
Section 1, pp. 2–3, and the fixed-support adjacency variational formulation
at the start of Section 2, p. 4. Their large-support optimality theorem is
not needed and is not asserted for this 65-vertex example. The deduction
here is the explicit unitary completion refuting (22), with no novelty
claim for the graph construction.

A possible replacement,
`sum_i(2P_i-I)<=(M/2)I`, would still give the required ququart constant.
It remains unproved. Its enlargement to arbitrary CPTP recovery is
already false at `n=9,M=4`. Partition the nine sites into three groups
of three, with group label c(i), and set

$$
|\chi\rangle=\frac15\left(
4|0^9\rangle|0\rangle+\sum_{i=1}^9|e_i\rangle|c(i)\rangle
\right).
$$

For i in group a, use Kraus maps
`A_0=|0><0|+|1><a|` and `A_b=|0><b|` for the other two group labels.
Their adjoint products sum to I_4. The coherent vacuum/i pair contributes
`25/50` to Bell recovery; the six excitations in other groups contribute
`6/50`. The remaining same-group terms contribute zero. Consequently

$$
F_i=\frac{31}{50},\qquad
\sum_i(2F_i-1)=\frac{54}{25}>2=M/2.
\tag{24}
$$

These maps send the maximally mixed ququart to `diag(3/4,1/4)`.
They are not unitary-plus-discard decoders, whose output on that input
is maximally mixed. Their Bell effects are neither projectors nor balanced
in the reference marginal. The example therefore rules out that broader
CPTP proof route; it does not resolve a balanced-CPTP relaxation or the
subsystem-projector conjecture. Both controls were independently
reconstructed by exact amplitude arithmetic, without large matrices.

## 11. Primary-source comparison and the next proof target

The binary-block reduction is established. Masanes,
[*Asymptotic Violation of Bell Inequalities and Distillability*,
quant-ph/0512153v3](https://arxiv.org/pdf/quant-ph/0512153v3),
the unnumbered Lemma on p. 2, gives simultaneous scalar or two-dimensional
blocks for two binary projective measurements. Result 1's proof also
uses binary POVMs as mixtures of projective measurements. Those statements
do not evaluate a weighted resolvent; here convexity of this objective
justifies choosing reflection vertices without changing memory dimension.

Inverse convexity is also established. Hansen–Pedersen,
[*Jensen's Operator Inequality*, math/0204049v1](https://arxiv.org/pdf/math/0204049v1),
Theorem 2.1, Eq. (5), p. 3, supplies the general operator Jensen framework.
Equation (5) of this report proves the inverse special case directly;
it is not proposed as an original convexity principle.

Trace alignment is the usual eigenvalue rearrangement. Verstraete–Wolf,
[*Entanglement versus Bell Violations and Their Behavior under Local
Filtering Operations*, quant-ph/0112012v1](https://arxiv.org/pdf/quant-ph/0112012v1),
Theorem 4's proof, Eq. (17), p. 4, derives it from doubly stochastic
eigenbasis overlaps. Their fixed-spectrum CHSH theorem concerns a linear
two-qubit expectation, rather than the compressed inverse in (1).

Once submodularity is verified, largest-smallest pairing is an established
rearrangement consequence: Lorentz,
[*An Inequality for Rearrangements* (1953)](https://www.math.toronto.edu/mccann/assignments/477/Lorentz53.pdf),
unnumbered theorem, p. 176, Eqs. (2)–(3). Reversing the second ordered
list turns the submodular cost into the source's supermodular form.
Even dimension makes reversal a perfect matching. Section 4 supplies
the elementary uncrossing proof and does not claim new rearrangement
mathematics.

The specific deduction is the block support function, simultaneous
common-reference attainment, and resulting exact spectral formula over
all binary readouts, together with its algebraic decision rule. The
inspected ingredient statements do not state that formula. This focused
comparison does not establish publication priority or PRL significance.

The next central target is a joint constraint on the spectrum of the
earlier query Hamiltonian and the memory marginal of its actual top
eigenvector, sufficient to imply (17). Equation (21) shows why separate
bounds on those quantities do not suffice. An analytic failure of the
criterion for a realizable H_0 would instead show that its lower spectrum
must be retained. Either outcome would resolve a specific proof obstacle,
without another search over arbitrary final decoders. The original
unrestricted optimum, unequal block spectra and publication originality
remain open.

## 12. Material correction found during the source audit

The earlier exact-axis corollary misread superscripts in
Bollobás–Lee–Letzter Theorem 2, p. 3. The arXiv v1 threshold is
`10^3=1000`; the [author manuscript](https://www.homepages.ucl.ac.uk/~ucahsle/papers/cube-evals.pdf)
dated 7 August 2020 uses `10^5=100000`. Both page images were inspected.
The repository's common-range conclusion must therefore require
`100000<=D<=n`, or `q>=17` when `D=2^q`, not `D>=105` or `q>=7`.

The exact-axis note and its README, research-note, status and literature
summaries are corrected together. The claimed optimum in the formerly
included range is withdrawn for lack of the cited upper bound, not
disproved. The operational graph reduction, explicit star construction,
separation from original-site retention, independently proved asymptotic
rate and the present resolvent theorem do not depend on that incorrectly
extended range.
