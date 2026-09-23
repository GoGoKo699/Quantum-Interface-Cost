# Tensor formation, query dimension, and channel completion

Date: 23 September 2026. Reviewed main:
`3a668f92afe5145e3273c5796ee74e0120214e1f`.

**Status:** supplied analytical deductions, independently reconstructed within
this workspace. No unrestricted optimum, tensor-formation additivity theorem,
or exhaustive originality certification is claimed. This continues the
[previous audit](PROFILE_NOVELTY_AND_STEERING_REDUCTION.md); the historical
[initial audit](PROOF_AND_NOVELTY_AUDIT.md) is preserved.

The original task still has one unknown quantum specimen, one delayed local
binary query, unrestricted collective encoding, unlimited finite classical
records, a quantum dimension cap in every branch, and uniform accuracy over
all input states and queries. The full-tuple and fixed-output-channel tasks
below are explicitly defined comparisons, not replacement models.

A subsequent [provenance audit](ROOF_PROVENANCE_AND_JOINT_SCORE.md), pinned
to the merge of this report, identifies Vollbrecht–Werner Eqs. (38)–(42)
as the direct prior source of the symmetry/roof method and the abstract
fixed-block affinity argument below. The moment coordinates and physical
applications are supplied deductions; the general principles are prior.
No theorem or proof below is withdrawn by this attribution refinement.

## 1. Findings and limits

| Statement | Verdict and implication |
|---|---|
| Exact full-tuple formation can be reduced to n moments and at most n+1 seed orbits | Derived below, retaining arbitrary collective decoders and classical flags. This is a finite reformulation, not an evaluated optimum. |
| At fixed n, one interior tensor-formation additivity point forces additivity at every contrast | Task-specific application of Vollbrecht–Werner Eq. (42), proved below. Failure of a specific joint-decoder entropy inequality instead gives strict savings at every interior contrast, at the same n. |
| One delayed local query and the full product of noisy queries can require different worst-case memory | Derived below. For n=2 at contrast (1+1/sqrt(2))/2, the exact retained dimensions are two and three, or one and two integer qubits respectively. This does not prove different formation entropies or rates. |
| A fixed qubit-output channel completion recovers the full profile cost C | Incorrect. Its minimum Choi formation entropy is G(x,z)=f([x+z-1]_+), strictly above C throughout x+z>1, x<1, z<1. The complete equality set is proved below. |
| The full two-parameter evaluation is original in all prior literature | Unresolved. The exact comparisons rule out specified reductions; they do not constitute a complete citation census or peer review. |
| Unrestricted equal-accuracy subset optimality | Unresolved. No violating seed or complete local-query entropy converse is supplied. |

## 2. Exact moment reduction for the stronger tuple problem

Write t=1/sqrt(2), delta=1-t, d=2^n, and let
`b in {X,Z}^n`, `s in {-1,+1}^n`. The trusted reference has n qubits.
For S a subset of sites, put `s_S=product_(i in S) s_i` and
`P_(S,b)=product_(i in S) P_(i,b_i)`. The full product assemblage is

$$
\Sigma^\eta_{\mathbf s|\mathbf b}
=\bigotimes_{i=1}^n\frac{I+s_i\eta P_{b_i}}4
=\frac1{d\,2^n}\sum_{S\subseteq[n]}
       \eta^{|S|}s_SP_{S,\mathbf b}.
\tag{1}
$$

Set `B_n(eta)=E_FA(Sigma^eta)`, using the established assemblage formation
entropy of Cope. A normalized seed is any collection of positive operators
`Gamma_(s|b)` with `sum_s Gamma_(s|b)=rho` for every b, where rho is a
density matrix. It has a quantum realization by a purification of rho:
the POVMs on its support are the transposes of
`rho^(-1/2) Gamma_(s|b) rho^(-1/2)`, with a kernel completion if necessary.
Its charged pure-state entropy is S(rho), in bits. No consistency condition
is imposed on proper outcome marginals when other entries of b change:
there is a single untrusted party receiving the whole tuple.

Define, for k=1,...,n,

$$
m_k(\Gamma)=\frac1{2^n\binom nk}
 \sum_{\mathbf b}\sum_{|S|=k}\sum_{\mathbf s}
 s_S\operatorname{Tr}(P_{S,\mathbf b}\Gamma_{\mathbf s|\mathbf b}).
\tag{2}
$$

**Moment theorem.** Exactly,

$$
B_n(\eta)=\min\left\{\sum_a p_aS(\rho_a):
 \sum_a p_am_k(\Gamma^a)=\eta^k\quad(1\le k\le n)\right\}.
\tag{3}
$$

At most n+1 seed orbits suffice. The finite symmetry orbit may itself have
many flagged branches; no bound on classical records is being charged.

**Proof.** Twirl independently by the Pauli group on every reference site,
with the corresponding sign relabels of s. Expand an arbitrary seed in
Pauli strings and outcome Fourier characters. A term survives precisely
when its string is P_(S,b) and its outcome character is s_S; the full Pauli
group eliminates every Y term and every mismatched character. Next twirl
by local Hadamards with X/Z setting relabels, and then by site permutations.
The result is

$$
\mathcal T(\Gamma)_{\mathbf s|\mathbf b}
=\frac1{d\,2^n}\left[I+\sum_{S\ne\varnothing}
    m_{|S|}(\Gamma)s_SP_{S,\mathbf b}\right].
\tag{4}
$$

Each group image retains its own flag and the same entropy S(rho).
Charging the entropy of the averaged marginal I/d would be erroneous.
Thus any ensemble in (3), completed by its finite orbits, is an exact
decomposition of (1) at the same cost. Every decomposition of (1), conversely,
obeys its linear moment equations. Permitting nonextremal seeds does not
change E_FA: extremal refinement cannot increase average marginal entropy.

The normalized seed set is compact, and its moment/entropy graph is compact
in R^(n+1). Its convex hull is compact, so the minimum exists. Caratheodory
initially gives n+2 graph points. If more than n+1 weights are positive,
their vectors `(1,m_1,...,m_n)` are dependent. A sufficiently small signed
weight perturbation preserves all constraints. Its cost slope must vanish
at a minimum, since otherwise one direction lowers the objective. Move
until a weight reaches zero and repeat. This proves the cardinality claim.

For clarity, this formulation does not silently make every component a
multisite nonsignalling assemblage. For n>=2 and eta<1, choose
`0<epsilon<(1-eta)^n`, and `h(X)=1,h(Z)=-1`. The two collections

$$
\Gamma^\pm_{\mathbf s|\mathbf b}
=\Sigma^\eta_{\mathbf s|\mathbf b}
 \mathbin\pm\frac{\epsilon s_1h(b_2)}{4^n}I
\tag{5}
$$

are strictly positive normalized quantum assemblages with marginal I/d.
Their average is the target, while each first-site outcome marginal depends
on b_2. Positivity follows from the target's minimum outcome eigenvalue
`(1-eta)^n/4^n`. Thus product structure of the target does not enforce these
additional linear identities on decomposition components. This observation
does not exclude existence of a specially structured optimal decomposition.

## 3. Fixed-block additivity has an all-or-nothing form

Define the jointly attainable first-moment score

$$
j_n(\rho)=\max_{\Gamma:\ \sum_{\mathbf s}
                  \Gamma_{\mathbf s|\mathbf b}=\rho}m_1(\Gamma).
\tag{6}
$$

The unrestricted single-query score from the seed reduction is

$$
f_n(\rho)=\frac1{2n}\sum_{i,b_i}
 \|\sqrt\rho P_{i,b_i}\sqrt\rho\|_1,
\qquad j_n(\rho)\le f_n(\rho).
\tag{7}
$$

The inequality follows from trace-norm duality for every context-dependent
marginal decoder. Equality is not assumed: separately optimal binary
decoders need not be marginals of a common tuple POVM.

**Fixed-block dichotomy.** For each fixed n, the following are equivalent:

1. `B_n(eta)=n(eta-t)/delta` for at least one eta in (t,1).
2. That equality holds for every eta in [t,1].
3. Every n-qubit density matrix satisfies

$$
S(\rho)\ge\frac{n[j_n(\rho)-t]}\delta.
\tag{8}
$$

If these statements fail, then `B_n(eta)<n(eta-t)/delta` for **every**
eta in (t,1), at the same block size n. This is a stronger fixed-block
statement than the previously established dichotomy for the regularized
local-query rate. It is not a proof that either alternative occurs.

**Proof.** For j=0,...,n, take a product seed with j maximally mixed factors
and n-j pure bisector factors, with local optimal readout. Its entropy is j.
Its symmetry orbit has moments

$$
v_{j,k}=\binom nk^{-1}\sum_\ell
       \binom j\ell\binom{n-j}{k-\ell}t^{k-\ell}.
\tag{9}
$$

These n+1 vectors are affinely independent. Their generating polynomials,
including v_(j,0)=1, are

$$
F_j(z)=\sum_{k=0}^n\binom nk v_{j,k}z^k
      =(1+z)^j(1+tz)^{n-j}.
\tag{10}
$$

A vanishing linear combination, divided by (1+tz)^n near zero, becomes a
polynomial in the nonconstant variable `(1+z)/(1+tz)`. All its coefficients
must vanish. For eta=t+delta p, 0<p<1, the target moment vector
`u=(eta,...,eta^n)` has strictly positive coordinates in this simplex:

$$
u=\sum_{j=0}^n\alpha_jv_j,\qquad
\alpha_j=\binom njp^j(1-p)^{n-j}.
\tag{11}
$$

This follows by expanding `(1+eta z)^n` using
`1+eta z=p(1+z)+(1-p)(1+tz)`. The affine function
`L(w)=n(w_1-t)/delta` satisfies L(v_j)=j and L(u)=np.

If a legal seed has moments w and entropy s<L(w), write its unique real
barycentric coordinates `w=sum_j beta_j v_j`, `sum_j beta_j=1`.
They need not be nonnegative. Choose

$$
0<\varepsilon<\min\left\{1,
             \min_{j:\beta_j>0}\frac{\alpha_j}{\beta_j}\right\}.
\tag{12}
$$

Mix this seed with weight epsilon and product atom j with weight
`alpha_j-epsilon beta_j`. These are nonnegative weights summing to one;
all target moments are restored exactly, while the entropy becomes

$$
np+\varepsilon[s-L(w)]<np.
\tag{13}
$$

Orbit completion in (4) makes this a full target decomposition. Failure
of (8) supplies such a seed by maximizing (6), proving strict savings at
every interior eta. Conversely, (8) lower-bounds every decomposition by
the average of L(m_1), which is np. The product atoms attain that bound.
This proves all three equivalences.

For n=2, compensation is completely explicit:

$$
\beta_0=\frac{w_2-2w_1+1}{\delta^2},\quad
\beta_1=\frac{2[(1+t)w_1-w_2-t]}{\delta^2},\quad
\beta_2=\frac{w_2-2tw_1+t^2}{\delta^2}.
\tag{14}
$$

Consequently the eta^2 constraint cannot protect additivity from a seed
violating (8). An exact affine supporting witness at an interior product
target must meet all n+1 product atoms, since their weights are positive.
Affine independence forces it to be L: higher-moment coefficients must
vanish. The constructive proof does not require assuming dual attainment.

The original missing inequality has f_n in place of j_n. Since only
`j_n<=f_n` is established, proving (8) alone would not establish the
unrestricted local-query converse. Conversely a violation of (8) would
also violate that converse and, by the previous audit, refute subset
optimality. These implications have not been reversed.

## 4. Strict separation of worst-case query dimensions

The tuple task requires the complete effects
`E_(s|b)=d Sigma_(s|b)^eta` exactly, uniformly over arbitrary input states.
The local task requires just `(I+s eta P_(i,b))/2`. Both allow unrestricted
collective instruments and unlimited free classical records, with the same
dimension cap on every branch. No error metric for the tuple distribution
is identified with the original binary TV error.

**Dimension theorem.** Let n>=2 and `eta_n=t+delta/n`. The local task has
optimal retained dimension two. The full tuple task cannot be simulated
with retained dimension at most two. In particular, for n=2 its exact
minimum dimension is three, versus two for the local task, at

$$
\eta_*=(1+1/\sqrt2)/2.
\tag{15}
$$

In integer-qubit units the two costs are two and one. A matching qutrit
instrument is supplied below. The theorem makes no claim that B_2 exceeds
A_2.

**Proof.** Use the previously proved [one-qubit theorem and rigidity](../ONE_QUBIT_OPTIMALITY.md),
whose essential prior ingredient is Cheng–Hall's independently optimized
three-qubit CHSH monogamy inequality. It gives

$$
f_n(\rho)\le t+\delta/n\quad(\operatorname{rank}\rho\le2),
\tag{16}
$$

and every equality seed, up to an output unitary and retained site r, is

$$
L=\frac1{\sqrt2}U\left(I_r\otimes
                      \bigotimes_{i\ne r}\langle\beta_i|\right),
\tag{17}
$$

where each beta_i has X and Z expectations `t a_(i,X),t a_(i,Z)` with
signs a_(i,b)=+/-1. This rigidity includes arbitrary complex seeds.

Suppose a full-tuple instrument with cap two realizes the target. Refine
its Kraus maps K_a and use weights `p_a=Tr(K_a^dagger K_a)/d` and normalized
seeds `L_a=K_a/sqrt(Tr(K_a^dagger K_a))`. These weights sum to one;
they are bookkeeping weights for the maximally mixed input, not an
assumption that physical branch probabilities are input independent.
Let N_(s|b)^a be the arbitrary tuple POVM on branch a. Its assemblage
component can be written `(L_a^dagger N_(s|b)^a L_a)^T`. X/Z strings are
real, so (2) is exactly the associated decoder correlation.

Every branch has `m_1<=f_n<=eta_n`, and their mean is eta_n. Thus every
nonzero branch saturates both bounds. Furthermore each individual
context-dependent marginal attains its trace-norm bound: all deficits in
the finite average are nonnegative. Rigidity therefore gives (17).

For a discarded site i and a retained site r, respectively,

$$
LP_{i,b_i}L^\dagger=\frac{t a_{i,b_i}}2I,
\qquad LP_{r,b_r}L^\dagger=\frac12UP_{b_r}U^\dagger.
\tag{18}
$$

These matrices are invertible. Their unique optimizing contractions are
`a_(i,b_i) I` and `U P_(b_r) U^dagger`. A scalar-sign marginal of a POVM
forces that output bit to be deterministic: the sum of all effects with
the opposite bit is zero, hence each such positive effect is zero.
Accordingly the tuple POVM consists of the sharp retained-site measurement
and deterministic outputs at every discarded site. Context dependence
provides no additional freedom at equality.

Its order-two correlation is t on each pair containing r, and t^2 on
each pair not containing r. For example, signs from the deterministic
outputs cancel the beta expectations in the sandwiched Pauli product;
the retained Pauli squared is I. Averaging over all pairs gives, on every
branch independently of r,

$$
m_2=t^2+\frac2n(t-t^2)
    =\eta_n^2-\frac{\delta^2}{n^2}<\eta_n^2.
\tag{19}
$$

This contradicts the target's second moment, proving impossibility.
The random-subset local protocol attains eta_n, and eta_n>t excludes zero
quantum memory.

**Matching qutrit construction for n=2.** Write a=eta_* and
`b=sqrt(a(1-a))=1/(2sqrt(2))`, and let `T=(X+Z)/sqrt(2)`. Define the
four-by-four seed

$$
L=\frac12\left[aI+b(T\otimes I+I\otimes T)
                     -(1-a)T\otimes T\right].
\tag{20}
$$

In the product T eigenbasis its eigenvalues are
`(1/sqrt(2),1/2,1/2,0)`. Hence it has rank three and Frobenius norm one.
For each of the sixteen two-qubit Pauli strings P, put `K_P=P L P/2`.
Pauli averaging gives
`sum_P K_P^dagger K_P=(1/4)sum_P P L^2 P=I`, so these maps form a
complete, trace-preserving instrument without postselection.

Writing `L=(1/2)sum_Q ell_Q Q`, Pauli character orthogonality gives
`sum_P K_P rho K_P^dagger=sum_Q ell_Q^2 Q rho Q`. The nonzero squared
coefficients are a^2 on II, a(1-a)/2 on XI,ZI,IX,IZ, and (1-a)^2/4 on
XX,XZ,ZX,ZZ. The resulting channel is exactly

$$
\Lambda_a\otimes\Lambda_a,\qquad
\Lambda_a(\omega)=a\omega+\frac{1-a}2(X\omega X+Z\omega Z),
\quad\Lambda_a^*(X)=aX,\quad\Lambda_a^*(Z)=aZ.
\tag{21}
$$

Only a qutrit crosses the interface: choose an isometry V_P from C^3
onto the range of K_P and retain the output of `V_P^dagger K_P`, with
P stored classically. When b is revealed, use the compressed product POVM
`V_P^dagger Pi_(s|b) V_P`, where
`Pi_(s|b)=tensor_i (I+s_i P_(b_i))/2`. Its effects sum to I_3. The induced
input effects equal the adjoint of (21) applied to Pi, namely
`tensor_i (I+s_i a P_(b_i))/2`, uniformly on every input state. This proves
the exact dimension-three upper bound, including internally entangled inputs.

The separation persists on some nonempty interval immediately below eta_*.
Indeed the set of normalized fixed-label assemblages whose marginal has
rank at most two is compact. Its convex hull, also compact in finite
dimension, is exactly the assemblages attainable with free flags and cap
two: purification proves one direction, and Kraus refinement proves the
other. The target at eta_* lies outside that closed set, so continuity of
the target gives an open excluded neighborhood. Restrict it to eta>t;
the local dimension remains two. Independent output flips reduce the
qutrit construction to any smaller nonnegative eta, so its minimum is
still three on this interval. No explicit width is asserted.

This strengthens the earlier single-branch joint-decoder obstruction to
a separation of optimal worst-case memory for the two exact targets. It
does not settle their optimized entropy roofs: the constructed rank-three
seeds have entropy 3/2, whereas the product formation upper bound at eta_*
is one, using a mixture that includes rank-four branches.

## 5. Fixed qubit-output channel completion gives a different full profile

For 0<=x,z<=1 let C(x,z) be the already evaluated one-qubit formation roof
in [the profile theorem](../PRODUCT_DIAGONAL_PROFILE_RATE.md), and put

$$
f(v)=h_2\!\left(\frac{1-\sqrt{1-v^2}}2\right).
\tag{22}
$$

Consider the distinct completion problem

$$
G(x,z)=\min_{\substack{\Lambda:\text{qubit CPTP}\\
                  \Lambda^*(X)=xX,\ \Lambda^*(Z)=zZ}}
 E_F(J_\Lambda),\qquad
J_\Lambda=(\mathrm{id}\otimes\Lambda)(\Phi_2).
\tag{23}
$$

Here the output is a single qubit with fixed X,Z readouts; Phi_2 is the
normalized Bell state. This is Choi formation entropy, not an asserted
unregularized formula for operational channel entanglement cost.

**Channel comparison theorem.**

$$
G(x,z)=f([x+z-1]_+),\qquad C(x,z)\le G(x,z),
\tag{24}
$$

with the complete equality set

$$
C(x,z)=G(x,z)
\quad\Longleftrightarrow\quad
x+z\le1\ \text{or}\ \max\{x,z\}=1.
\tag{25}
$$

In particular, at (3/5,4/5), C=0 but G=f(2/5)>0. The fixed-output
completion is inequivalent even at the zero-cost boundary, before any
asymptotic question arises.

**Proof of (24).** Pauli-twirl an arbitrary feasible channel by
`Lambda_bar(rho)=(1/4)sum_Q Q Lambda(Q rho Q) Q`. This preserves both
readout constraints and makes its Choi state a mixture of local-unitary
conjugates, so it cannot increase E_F. The resulting Pauli channel has
Bloch multipliers (x,y,z), with Bell weights

$$
(p_I,p_X,p_Y,p_Z)=\tfrac14
(1+x+y+z,\ 1+x-y-z,\ 1-x+y-z,\ 1-x-y+z).
\tag{26}
$$

Complete positivity is exactly
`x+z-1<=y<=1-|x-z|`. Wootters' established two-qubit formula gives
`E_F=f([2 max_mu p_mu-1]_+)`. If x+z<=1, y=0 is feasible and all Bell
weights are at most 1/2, giving zero. Otherwise y>0 and p_I is largest;
the concurrence `(x+y+z-1)/2` is minimized at y=x+z-1. Monotonicity of f
proves the formula, including originally nonunital or nondiagonal channels.

**Proof of the complete comparison.** The triangle x+z<=1 lies in the
compatibility disk, so C=G=0. On either exact axis, the established formula
is C(1,v)=C(v,1)=f(v), equal to G. For every remaining point, set
`v=x+z-1 in (0,1)`. On the segment with endpoints A=(1,v), B=(v,1),
both endpoint costs equal f(v). The midpoint M has

$$
C(M)=\left[\frac{1+v-\sqrt2}{2-\sqrt2}\right]_+<f(v).
\tag{27}
$$

For v<=sqrt(2)-1 this is immediate. Above that value, f is convex with
`f'(v)<=f'(1)=1/ln(2)<1/(2-sqrt(2))`. The difference between f and the
displayed affine function decreases strictly to zero at v=1, proving
strictness. The derivative comparison is analytic:
`ln(2)=2 atanh(1/3)>2/3>2-sqrt(2)`. Every nonendpoint point of AB is a
convex combination of M and one endpoint, with positive midpoint weight.
Convexity of C then proves C(x,z)<f(v)=G(x,z), as claimed.

Thus the full profile is not just a missing Pauli multiplier followed by
Wootters' formula. Enlarging the output to arbitrary quantum/classical
systems and allowing branch-dependent readouts removes this restriction,
but returns to the established steering formation optimization; it does
not itself evaluate that optimization.

## 6. Primary-source map and novelty boundary

The preceding proofs are supplied deductions. Their standard ingredients
and the inspected prior statements have the following exact scopes.

| Primary source and locator | Relevant statement and assumption map |
|---|---|
| Vollbrecht–Werner, [quant-ph/0010095v2](https://arxiv.org/abs/quant-ph/0010095v2), Section IV.A, Eqs. (38)–(41), pp. 10–11; IV.B, Eq. (42), p. 11 | Direct prior general symmetry/roof reduction and affinity over optimal decomposition atoms. Sections 2–3 specialize these principles to tuple moments and the product simplex; see the follow-up provenance audit. |
| Cope, [2102.02333v2](https://arxiv.org/abs/2102.02333v2), Eq. (10), Theorem 2, p. 3; Eqs. (5)-(6), p. 2 | The assemblage formation resource and realization interpretation are prior. B_n uses complete tuples, whereas the project's A_n uses 2n binary local settings. The preceding audit covers the full-profile comparison and credits the earlier mixture mechanism. |
| Cope–Uola, [2207.05722v4](https://arxiv.org/abs/2207.05722v4), Section IV.A, Eqs. (5)-(8), pp. 4-5; Section VI.A, Eqs. (20)-(22), p. 11 | Explicitly distinguishes decompression with fixed readouts from arbitrary direct readouts. Its average log-rank measure and smoothed full-tuple regularization are established frameworks; neither automatically evaluates worst-case single-query memory. |
| Cheng–Hall, [1610.09302v3](https://arxiv.org/abs/1610.09302v3), Eq. (1), p. 1, Eqs. (13)-(14), p. 3 | Three-qubit CHSH monogamy permits independently chosen common-qubit settings and mixed states. The repository's existing one-qubit rigidity, rechecked here, is the task-specific ingredient for the dimension separation. This is not a new monogamy theorem. |
| Terhal–Horodecki, [quant-ph/9911117v4](https://arxiv.org/abs/quant-ph/9911117v4), Eqs. (14)-(16) and following paragraph, p. 3; Fig. 1, p. 4 | Already constructs a two-qubit isotropic state whose tensor square still has Schmidt number two; its rank-three endpoint claim is explicitly numerical evidence. Tensor-product Schmidt-number compression and twirling are prior phenomena. Its isotropic Bell weights differ from the anisotropic weights in (21); that printed construction does not give the present target. |
| Wootters, [quant-ph/9709029v2](https://arxiv.org/abs/quant-ph/9709029v2), Eqs. (9)-(10), p. 4 | E_F=f(concurrence) for a two-qubit state. The minimization over Pauli completions in (23)-(26) is an elementary application. Arbitrary classical flags are not a two-qubit state. |
| Wilde, [1807.11939v3](https://arxiv.org/abs/1807.11939v3), Theorem 1, p. 8; Eq. (54) and following discussion, p. 9; Eqs. (63)-(65), p. 10 | Covariant-channel entanglement cost is the regularized cost of its Choi state, not automatically its E_F. The dephasing case does satisfy E_C=E_F and supplies the exact-axis function. These full-channel results cannot be substituted for the free-flag query profile. |
| Zhang–Zhang–Chitambar, [Quantum 9, 1902 (2025)](https://quantum-journal.org/papers/q-2025-10-31-1902/), Section 2, Eq. (2), p. 3; Definitions 1-2, p. 4 | The simulation resource is classical hidden-variable cardinality in an LHS model. It can be nontrivial for unsteerable assemblages, where E_FA is zero. Classical cardinality is free here; the similarly named resource does not evaluate C. |

This follows specific primary citation chains, not just keyword matches.
The fixed-channel calculation and its full equality set rule out a precise
subsumption route; the moment and dimension theorems distinguish the local
and tuple problems mathematically. None proves historical priority over
every possible steering or measurement-compression result. Symmetry
reduction, Caratheodory reduction, convexity and simplex compensation are
standard tools and are not independently proposed novelties. In particular,
the qutrit upper bound is an elementary construction proving a task-specific
separation; originality of that construction is not claimed. The inspected
isotropic rank-three numerical endpoint would give Pauli visibility
`(2sqrt(3)-1)/3<eta_*`, so even treating that numerical statement as an
attainment would not directly reach the present contrast.

The defensible candidate remains the **complete analytic evaluation of the
two independently noisy orthogonal-qubit formation profile, with optimizer
and phase boundary, and its proved product-diagonal fixed-cap operational
rate**. The resource, free-flag framework, compatibility threshold,
exact-axis curve and compatible/partially entangled mixture mechanism are
prior ingredients. Publication originality still requires further assessment
of that precise evaluation and tensorization claim.

## 7. Verification and the remaining mathematical gate

The main SHA, existing reports, issue comments #1-#2 and open PR list were
checked before editing. The normalized Kraus weights, moment twirl,
simplex argument, one-qubit equality conditions, decoder uniqueness,
rank-three orbit instrument, channel twirl and all profile boundaries were
independently reconstructed
within this workspace. This is internal mathematical review, not external
peer review. No large simulation, new matrix optimization, or new numerical
certificate was used. Earlier unchanged diagnostics were not treated as
proofs or rerun merely to accumulate passing tests. LICENSE and the
historical initial audit remain unchanged.

The exact remaining local-query gate is still

$$
\sum_{i,b}\|\sqrt\rho P_{i,b}\sqrt\rho\|_1
\le\sqrt2\,n+(2-\sqrt2)S(\rho)
\quad\text{for every n and every n-qubit density matrix.}
\tag{28}
$$

A complete proof or a certified violation is needed. For the narrower
full-tuple route, (8) is now an equivalent fixed-block gate; a certified
violating seed yields an explicit decomposition at every interior eta via
(9)-(13). At n=2, only three seed orbits and two moment constraints are
needed. A fixed-rho linear search is four four-outcome SDPs, but the entropy
optimization over rho remains nonconvex and unresolved. Neither a solver's
local optimum nor the present reformulation is a global certificate.

The finite dimension separation does not decide (28), and the channel
comparison does not certify originality. Both prevent specific unsupported
identifications while leaving the original scientific question intact.
