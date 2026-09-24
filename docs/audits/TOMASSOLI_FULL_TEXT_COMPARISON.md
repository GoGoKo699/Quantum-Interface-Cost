# Tomassoli's two-correlator thesis: full-text comparison

Date: 2026-09-24. Reviewed main:
`c2857e9b912ceae47d3067a62aa1f07f4acb1cf2` (PR #27).
Reviewed tree: `5bfe2ecc4c6c348ab2fad628c9644a18bbcd6282`.

**Finding:** the user supplied the previously inaccessible thesis. Its
main result concerns one scalar witness score on two qubits, with fixed
orthogonal Pauli readouts on both sides. Its concurrence boundary is
correct; its negativity boundary needs a factor of two under its own
definition. We prove the exact calibrated two-parameter extension below
and compare that stronger benchmark, not merely the source's title or
number of plotted variables. It does not evaluate our optimized-readout
formation profile C. Its exact-axis family overlaps with our generators
and must be credited. This closes the specified source-access comparison,
not exhaustive originality or unrestricted equal-accuracy optimality.

## 1. Source and exact scope

Giacomo Tomassoli, *Certificatori di Entanglement per due qubit con due
correlatori* / *Quantitative Entanglement Witness for two qubits with two
correlators*, Università degli Studi di Padova, bachelor's thesis,
academic year 2024/2025, supervisor Pietro Silvi.
[Institutional record](https://hdl.handle.net/20.500.12608/84769);
[advertised PDF](https://thesis.unipd.it/bitstream/20.500.12608/84769/1/Tomassoli_Giacomo.pdf.pdf).

This audit reads the user-supplied 27-page PDF, 3,085,312 bytes, SHA-256
`0c84d0246528c900559b678c54a1f63393f6d18e54be377b88fa653254c2b7ab`.
Its title and authorship match the institutional record; we have not
verified byte identity against a separately downloaded institutional copy.
All page references below are **printed** pages; main-text PDF pages are
five higher. The PDF is not redistributed in this repository.

| Locator | Actual statement or assumption |
|---|---|
| Section 1.2, Eqs. (1.7)–(1.8), p. 6 | Minimize an entanglement measure over two-qubit states at one specified scalar expectation of a fixed witness. |
| Section 1.3, Eq. (1.9), p. 7 | Two Pauli operators on each qubit, with each local pair orthogonal. Neither side's readouts are optimized. |
| Eqs. (1.14)–(1.17), p. 9 | Ordinary negativity N=(norm of the partial transpose minus 1)/2, and two-qubit concurrence. Formation entropy is background, not the quantity evaluated in Chapter 2. |
| Eqs. (2.2)–(2.3), p. 10 | W=XX+YY, with XX+ZZ as a locally unitarily equivalent example. |
| Section 2.1, pp. 11–15 | Haar sampling, a numerical convex hull, inferred attaining states, and a scalar boundary. |
| Eq. (2.15), p. 15; Section 2.2, p. 16 | b(s)=(abs(s+1)+abs(s-1)-2)/2=[abs(s)-1]_+, for concurrence and the plotted negativity. |
| Eq. (2.14), p. 15 | An exact-axis pure-state family, also a generator in our profile construction. |
| Sections 2.3–2.4, pp. 16–18 | Comparison of the two measures and additional three-correlator examples; no independently constrained two-parameter formation evaluation. |

The source's sampled convex hull is not the formation convexification
over orthogonally flagged sectors. Nor does sampling prove a universal
lower bound. The following reconstruction supplies an exact all-state
proof for the correctly normalized result.

## 2. Reconstruct the result, including its strongest calibrated lift

Write c for concurrence, V=2N, and

$$
f(v)=h_2\!\left(\frac{1-\sqrt{1-v^2}}2\right).
$$

The relation E_F=f(c) for every two-qubit state is Wootters' prior
theorem, [quant-ph/9709029](https://arxiv.org/abs/quant-ph/9709029).
The reductions below are elementary consequences, not proposed novelties.

**Scalar benchmark.** For W=XX+YY or XX+ZZ and -2<=s<=2,

$$
\min c=[|s|-1]_+,\qquad
\min N=\tfrac12[|s|-1]_+,\qquad
\min E_F=f([|s|-1]_+).
\tag{1}
$$

For XX+YY, bilateral Pauli twirling is a random local-unitary channel
that preserves both correlations and cannot increase any of these
entanglement measures. In the resulting Bell-diagonal state,
s=2(p_{Psi+}-p_{Psi-}), so p_max>=|s|/2. Its concurrence and V both
equal [2p_max-1]_+. This proves the lower bounds. For 1<=s<=2 the
state (s/2)|Psi+><Psi+|+(1-s/2)|Phi+><Phi+| attains them all;
for negative s replace s by |s| in the weights and Psi+ by Psi-.
For |s|<=1, product-state
mixtures attain the score. Monotonicity of f proves the entropy line.
Local unitary equivalence gives XX+ZZ.

**Two independent calibrated correlations.** Fix x=<XX> and z=<ZZ>.
For every (x,z) in [-1,1]^2 the exact simultaneous minima are

$$
c_{\rm cal}=V_{\rm cal}=[|x|+|z|-1]_+,\qquad
N_{\rm cal}=c_{\rm cal}/2,\qquad
G(x,z):=E_{F,\rm cal}=f(c_{\rm cal}).
\tag{2}
$$

Independent Pauli sign changes reduce to x,z>=0. Twirling preserves
both constraints. For any resulting Bell probabilities,
x+z=2(p_{Phi+}-p_{Psi-}), implying p_max>=(x+z)/2. If x+z>=1,
the Bell probabilities in the order (Phi+,Phi-,Psi+,Psi-) given by

$$
\left(\frac{x+z}{2},\frac{1-x}{2},\frac{1-z}{2},0\right)
\tag{3}
$$

are nonnegative, sum to one, give the prescribed separate correlations,
and attain all three minima. If x+z<=1, the separable mixture
x|++><++|+z|00><00|+(1-x-z)I/4 does so. Thus (2) is not just a
scalar bound with unattainable individual data. In this calibrated
problem all resource minima share an optimizer; its efficient
formation/negativity frontier is a single point.

Even allowing **all weighted calibrated witnesses** leaves the
distinction below intact. For a>=b>0 and s=<aXX+bZZ>, (2) implies
|s|<=a+b c and |s|<=a+b V. Exact-axis states with x=1,z=v attain
the upper boundary; separable states cover |s|<=a. Consequently the
full weighted family has minimum c=V=[(|s|-a)/b]_+ and minimum
E_F=f([(|s|-a)/b]_+) for |s|<=a+b. Exchange x,z when b>a.
These weighted and independently constrained extensions are supplied
deductions, not statements attributed to the thesis.

## 3. Compare equal assumptions, then identify the actual obstruction

Our [two-correlation theorem](TWO_CORRELATION_FORMATION.md) fixes only
Bob's qubit X,Z, allows Alice arbitrary binary contractions A_0,A_1,
and minimizes E_F at <A_0 X>=x and <A_1 Z>=z. It gives

$$
E_2(x,z)=\gamma(x,z)
=f\!\left(\sqrt{[x^2+z^2-1]_+}\right),\qquad
E_d(x,z)=C(x,z)\quad(d\ge3).
\tag{4}
$$

The first equality is already a consequence of Verstraete–Wolf; it is
not claimed new. The candidate evaluation is the full profile C and
its optimizer/phase structure. Realization dimension d counts flags
here; this differs from free classical records in the interface model.

| Optimization feature | Thesis and calibrated extension (2) | Profile C |
|---|---|---|
| Trusted operators | Fixed orthogonal Pauli pairs on both sides | Only Bob's X,Z fixed; Alice's readouts optimized |
| Hilbert spaces | Two qubits | Trusted qubit and arbitrary finite Alice dimension; a qutrit suffices |
| Given data | One scalar in the thesis; separate x,z in our stronger comparison (2) | Separate x,z |
| Separable region in the positive square | Triangle x+z<=1 | Quarter disk x^2+z^2<=1 |
| Formation minimum | f([x+z-1]_+) | Convexified disk-plus-axis profile C |
| Simultaneous minimum E_F and N | Always attainable by (3) or a separable state | Impossible at noisy nonclassical interior points with C<w; exact axes have common minimizers |

**A rational separating example suffices.** At x=z=2/3, let Alice's
state be |0>, A_0=A_1=Z, and let Bob have Bloch vector (2/3,0,2/3).
The product state is valid since the squared Bloch length is 8/9. It
has both requested correlations and E_F=N=0. Thus gamma=C=0. Fixed
orthogonal XX,ZZ instead require c>=1/3, N>=1/6, E_F>=f(1/3)>0.
This refutes an unchanged substitution of the thesis's formula into
our problem, even before any dimension-three flag advantage is used.

Conversely, the overlap on the axes is exact. The positive branch of
Eq. (2.14), p. 15,

$$
|\psi_\theta\rangle=\cos\theta|\Phi^+\rangle
+\sin\theta|\Psi^+\rangle,\qquad 0\le\theta\le\pi/4,
$$

has x=1, z=cos(2theta)=v, E_F=f(v), V=v. This is precisely the
(1,v,f(v),v) atom in our formation/negativity construction. It is
prior material, not evidence of a new state family. The calibrated
function G also coincides with the exact benchmark already
derived in the [fixed qubit-output channel comparison](TENSOR_FORMATION_AND_CHANNEL_COMPARISON.md);
it should not be sold as a new scalar formula.

There is a second reason not to base novelty on merely using two
parameters. The thesis cites Eisert–Brandao–Audenaert,
[quant-ph/0607167v4](https://arxiv.org/abs/quant-ph/0607167v4).
Their Eqs. (1)–(2), printed pp. 1–2, already pose minimization with a
collection of fixed witness expectations in arbitrary fixed dimensions; Eqs.
(24)–(30), p. 4, give the formation-entropy problem and tight optimized
Legendre bounds. Their Eq. (6), p. 2, uses V=2N. Joint use of data and
convex duality are established machinery. In particular, their framework
applies directly to our fixed qutrit pair A_0=1 direct-sum Z and
A_1=1 direct-sum X. To satisfy its witness convention literally, write
O_0=A_0 tensor X and O_1=A_1 tensor Z, then use
W_1=sqrt(2)I-O_0-O_1 and W_2=sqrt(5)I-2O_0-O_1. For product states
the trusted-qubit Bloch bound makes both expectations nonnegative;
the entangled two-qubit block gives negative expectations. Their two
scores invertibly encode x,z. Thus its abstract constrained minimum gives C
after the supplied block evaluation and unrestricted-readout comparison.
The source does not supply that evaluated profile, phase boundary or
scalar root; a further subsumption argument is not excluded merely by
different presentation. The [joint-resource source comparison](JOINT_RESOURCE_FRONTIER.md#5-what-is-established-prior-art-and-what-was-supplied-here)
also explains why the convex-roof shortcut needs extra care for mixed
states when the objective includes ordinary negativity.

## 4. Material proof qualifications in the thesis

These defects do not erase its correct scalar concurrence result or
axis construction. They do prevent treating every printed formula or
sampled boundary as a certified theorem.

* **Normalization:** Eq. (1.14), p. 9, defines ordinary N, but Eq.
  (2.15), p. 15, and the plots use the boundary for V=2N. At s=2 a
  Bell state has N=1/2, while the printed b(s) is 1. Equation (1)
  is the correction. Pure-state concurrence equals V, not N.
* **Spin flip:** Eq. (1.16), p. 9, visibly omits complex conjugation
  of rho. Its printed expression returns concurrence one for the
  product state |+y,+y>, whereas the correct spin flip and its own
  pure-state Eq. (1.17) return zero. No code was supplied, so this
  is a finding about the printed formula, not its implementation.
* **Attainment versus exclusivity:** the rank-two mixtures used in
  (1) also attain the lower boundary for 1<|s|<2. The inference on
  p. 17 that minimizers must be pure therefore fails. Existence of
  the displayed pure attainers remains correct.
* **An additional saturation claim:** Eq. (2.18), p. 18, gives
  cos(theta)|Psi->+sin(theta)|Phi+>. Its concurrence is one and N=1/2
  for every theta. At theta=pi/4 its XX+YY+ZZ score is -1, also
  achievable by a product state. The caption's claim that this
  witness completely quantifies that family is false, independently
  of the normalization issue; the orange horizontal plot itself
  shows the mismatch.

The exact proof in Section 2, rather than the thesis's finite convex
hull, establishes the correctly normalized minima over all states.

## 5. Verdict, remaining bottleneck and verification

**Established ingredients:** concurrence-to-formation conversion,
quantitative witnesses with several data constraints, convex duality,
the thesis's scalar calibrated boundary and exact-axis family, and
the previously identified steering-formation framework.

**Actual deductions supplied here:** the exact independently constrained
calibrated benchmark and its full weighted extension, simultaneous
attainers, the rational assumption separator, and explicit checks of
material printed errors. These are short comparison arguments, not
a proposed new publication result.

**Scoped non-subsumption:** this source does not supply the full
optimized-readout two-parameter C evaluation or its nontrivial joint
E_F/N frontier. The distinction holds for the strongest calibrated
extension above, not just the thesis's equal-weight slice.

**Still unresolved:** exhaustive prior subsumption and publication
significance of those evaluated profiles; the arbitrary-state seed
entropy inequality and unrestricted equal-accuracy rate. Nothing here
allows summing single-site formation costs when sites share one quantum
register. The remaining central proof target is still

$$
\sum_{i,b}\|\sqrt\rho P_{i,b}\sqrt\rho\|_1
\le\sqrt2\,n+(2-\sqrt2)S(\rho).
$$

The original contract remains one unknown specimen, encoding before
one delayed local query, unrestricted collective encoding, unlimited
finite classical records, worst-case quantum dimension and uniform
error over every state and query. This comparison supplies no new
memory converse and substitutes no estimation task.

All 27 pages were read. Defining equations and disputed formulas were
checked against rendered PDF pages, not text extraction alone. Two
independent workspace reconstructions checked the twirl, Bell weights,
sign relabelings, axis family and counterexamples; this is not external
peer review. The proofs use exact algebra, with no state simulation,
solver, or inferred numerical universal bound. Repository links and
whitespace were checked; LICENSE and the original commit-pinned audit
are preserved byte for byte. The user's upload resolves the specific
human-access request recorded in the [previous report](BAYES_RANK_PRIOR_COMPARISON.md#3-the-remaining-human-access-request).
