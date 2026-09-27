# Integrated core proof and source review

Research base: `38fd9d3f2c3e38ef5e8a7c5d6b2c041955678d8a` (PR #58).
Date: 27 September 2026. Paths below are relative to the repository root.

Reviewed exposition: [CORE_ARGUMENT.md](../CORE_ARGUMENT.md).
Its SHA-256 is
`15009f875db417d7926491376312cba8c0ac6cb56b68efcd29483c7eb9e12f45`.

**Verdict: PASS for the selected integrated exposition.** This is a
bounded internal analytical review, including independent reconstructions
of the finite-proof joins and a separate source-reconciliation read. It
is not external peer review, an exhaustive originality assessment, or a
review of a future manuscript. No frozen checker was imported or run;
the underlying frozen proofs, checkers and historical reports are unchanged.

The review covers the operational seed reduction, complete one-qubit
allocation argument, every integer memory budget through four inputs,
and the complete collective instrument with its precise retention-class
separation. The all-size spectral companions were checked for statement
and scope consistency with their frozen proofs; those proofs were not
repeated in this integration pass.

The finite conclusion is the original-score statement
`Gamma(n,2^q)=2q+sqrt(2)(n-q)`, for integers `1<=n<=4`, `0<=q<=n`.
The stronger affinity inequalities are tools at the stated finite ranks,
not a general replacement for the original objective.

## Reviewed joins and boundary cases

1. **Uniform error and normalized seeds.** The worst-case binary error is
   `||A_j-P_j||_infinity/2`. Pauli twirling leaves `lambda_j P_j`, with
   `lambda_j>=1-2epsilon`; finite query symmetrization and output noise
   preserve the worst-case quantum dimension. At zero target contrast,
   no division by a vanishing contrast is necessary. Finite Kraus
   refinement is admissible, zero Kraus operators are omitted before
   normalization, and the weights `||K_a||_F^2/d` sum to one without being
   assumed input-independent physical probabilities.

2. **Rectangular seed to density matrix.** For `rho=L^dagger L`, the polar
   factorization `L=V sqrt(rho)` preserves each query trace norm because V
   is isometric on the support of rho. Zero singular values and every
   rank at most the output cap are included. Conversely each such rho
   has a realization with that output dimension. The complete orbit
   `K_U=sqrt(d/4^n) L U` is trace preserving and realizes the seed's
   scores; the later query symmetrization equalizes them. No favorable
   outcome is selected.

3. **Original score versus affinity.** The sourced Schatten-(4,2,4)
   argument gives `||SUS||_1^2<=Tr(SUSU)` for `S=sqrt(rho)` and Hermitian
   unitary U, including singular rho. Root fidelity and its square are
   used with the correct conventions. Each affinity is in `[0,1]`.

4. **Half rank.** Zero singleton mass and the low-trace regime have strict
   Cauchy bounds. Zero-padding the singleton vector to four coordinates
   preserves the exact sign mean; ties in its maximum are covered. The
   top-half trace rearrangement pads the spectrum of S with zeros, so it
   requires rank at most half, not exactly half. The unit-circle
   inversion is squared only after `u^2+y>=1` makes its lower bound
   nonnegative. The selected-pair/rest tangents are on their physical
   domains. The final positive-definite quadratic has determinant
   `10-7sqrt(2)>0`; equality forces the claimed flat single-bisector Gram
   state. The proof is used only at `n=2,3,4`.

5. **Quarter-rank geometry and high-score reduction.** The top-four
   eigenvalue ordering and centered variance cover ties and padded zero
   eigenvalues. Rank at most three is strictly excluded by `sqrt(45)`.
   Under a putative score at least `4+2sqrt(2)`, Cauchy gives
   `u^2>15^2/16^2`, `delta<=r^2`, and rank exactly four. Thus the later
   smallest-positive-eigenvalue calculation is legitimate. The local
   block estimate preserves the off-diagonal block and uses the global
   rank only to bound the four positive eigenvalues' spread; it imposes
   no unproved rank bound on a marginal.

6. **Quarter-rank branch A.** `b>=c+d` includes its boundary. Positivity
   gives `w=u-a-b>=0`. The coupled inequalities bound Q and x before the
   grouped square-root monotonicity is used. The quadratic-root bound,
   the signs in the score-threshold squaring, and the displayed sum of
   squares reconstruct correctly. Its equality forces `u=y=1` and
   `(a,b,c,d)=(1/2,1/2,0,0)`.

7. **Quarter-rank branch B and exact certificate.** `b<=c+d` includes the
   same boundary. The threshold `q0` is fixed at Y while y varies. The
   proof establishes `H0>1/2`, so `J-H^2` decreases on the relevant
   interval; a negative radicand is infeasible. `C0>0` selects the lower
   circle root, and `F0>0` gives the strict exclusion. The substitution
   `tau=v/u`, `m=mu/u` covers the full closed box needed by all potentially
   extremal seeds; all denominators `d0` and `h0` are positive. Direct
   algebra reconstructs `Y=Z/d0^2`,
   `C0=C/(2h0 d0^(5/2))`, and `F0=P/(4h0^2 d0^4)`.
   The checker source implements the displayed C and P polynomials and
   the tensor Bernstein conversion using rational interval arithmetic.
   Its existing certificate, not a new execution here, supplies the
   coefficient positivity. The two final x intervals cover the full
   allowed range, including the switch point, and the grouped deficit
   is only lowered where its monotonicity direction is valid. This
   branch is strict, including `v=0`.

8. **Equality and operational assembly.** Attaining the original score
   must also attain the stronger affinity bound, so its equality family
   transfers. Conversely the bisector/retained-site seeds attain each
   comparison and the complete physical constructions achieve common
   contrast on arbitrary entangled inputs. These statements classify
   normalized seeds up to output isometries; they do not classify all
   instruments producing the same effects.

The exhaustive integer-budget assembly is:

| Input size | Memory budgets and proof |
|---|---|
| n=1 | q=0 classical; q=1 exact endpoint |
| n=2 | q=0 classical; q=1 all-n qubit theorem; q=2 exact endpoint |
| n=3 | q=0 classical; q=1 all-n qubit theorem; q=2 half rank; q=3 exact endpoint |
| n=4 | q=0 classical; q=1 all-n qubit theorem; q=2 quarter rank; q=3 half rank; q=4 exact endpoint |

At q=0, a rank-one seed has at most `sqrt(2)` score per site by its
local Bloch disk, attained by product bisectors. At q=n, each of the
2n query scores is at most one and full retention attains all of them.
The q=1 weighted monogamy argument and its zero-weight/one-site cases
supply the remaining entries without assumptions about real matrices,
flat spectra, simultaneous decoders, or product encoders.

## Reviewed sources

- `RESEARCH_NOTE.md`, Sections 2–4 (model, twirl, classical endpoint,
  direct retention construction).
- `docs/COLLECTIVE_ENCODING_REDUCTION.md`, Sections 1–4 (seed reduction
  and scope of solved finite cases).
- `docs/STRONG_ENTROPIC_CONVERSE.md`, Section 3 (only the root-fidelity/
  affinity lemma; no review of its wider entropy program).
- `docs/ONE_QUBIT_ALLOCATION_REGION.md`, weighted seed proof and finite
  operational construction; `docs/ONE_QUBIT_OPTIMALITY.md`, stated scope
  of the prior monogamy ingredient. The cited external paper was not
  reopened in this round.
- `docs/audits/HALF_RANK_RETENTION_CONVERSE.md`, Sections 1–6.
- `docs/audits/QUARTER_RANK_GEOMETRY.md`, top-quarter spectrum, squared
  budget/equality, and local block inequalities. Its historical open-case
  discussion is read at its recorded earlier base, not as current status.
- `docs/audits/NONFLAT_QUARTER_RANK_CONVERSE.md`, Sections 1–6.
- `tools/check_nonflat_quarter_rank_certificate.py`, read-only inspection
  of polynomial definitions, exact intervals, and Bernstein conversion;
  no import or execution.
- `docs/CORE_ARGUMENT.md`, Sections 1–3.2 (current finite proof narrative).

A separate internal reader independently checked items 1–3 at the same
base and reported pass. The remaining finite-converse joins were reconstructed separately for
this review.

## Allocation and collective-separation review

The final Section 2 was checked for the weighted CHSH conversion, scalar
extreme decoders, independently chosen common-qubit settings, mixed
three-qubit marginals, omitted zero weights, and the n=1 boundary. The
prior monogamy bound permits at most one site's weighted score to exceed
its compatible-disk support. Kraus averaging then bounds every physical
instrument. The matching convex hull has the same nonnegative support
function. Its disk/square decomposition gives the displayed local weight,
including the zero-weight and p=1 cases, and the explicit retention
mixture attains the complete region on arbitrary inputs.

The final Section 4 was checked for exact translation completeness,
32-dimensional output on every branch, both effective-observable
identities and fair outputs on decoder kernels. The retention comparison
class requires the existence of a factorizing Kraus refinement. Its
branch-dependent discarded vectors can be entangled; their reduced Bloch
vectors still give the stated support bound. Normalizing those vectors
and absorbing their norm into the retained factors makes the normalized
Gram factorization explicit. Taking the weighted limit at exact X
contrast proves `sum_i z_i<=q`, strictly exceeded by `sqrt(31)>5`.
Neither an unrestricted optimum, efficient implementation, nor an
unequal-to-equal-accuracy implication is claimed.

## Source reconciliation and companion boundaries

A separate internal source reader checked the final text against the
[focused comparison](../CORE_PRIOR_COMPARISON.md), without enlarging the
literature search. The simulability, steering and postmeasurement-information
frameworks remain prior work. The recent bottleneck formulation is
credited, and common CPTP reconstruction is distinguished from arbitrary
query-dependent binary decoding. The Ballester–Wehner–Winter equivalence
links to its actual derivation in the historical audit, Section 6.1.

Cheng–Hall supplies the independently optimized monogamy ingredient;
Pusey supplies the incompatibility-weight definition, while the local
disk geometry evaluates the displayed formula here. The checked
Avni–Samorodnitsky statement is identified as the cube-star spectrum.
The selected finite increments beyond endpoints and one-qubit memory
remain exactly `(3,2)`, `(4,2)` and `(4,3)`. The general all-size retention,
entropy and common-accuracy rate questions remain unresolved.

Section 5 preserves the distinction between constrained balanced spectra
and an unrestricted rank converse. Its explicit local state includes
the pure t=1 endpoint. The stability norm is the full trace norm, the
flat rank is exactly half, and the nonflat radius is a sufficient
condition with arbitrary support. The supplied constants are not claimed
optimal. This scope check does not replace the earlier independent
reviews recorded with the balanced and stability proofs.

## Corrections incorporated and next gate

The review resolved the following presentation issues before pinning the
final text: division by the singleton mass only when it is positive;
separation of the analytical `H0>1/2` bound from the two certified
polynomial signs; a nonnegative-radicand condition before the lower-root
expression; normalized retention factors; and the explicit pure endpoint.
The revised exposition also constructs a rectangular seed for every
rank-at-most-D density matrix and includes the short singular-state-valid
Schatten-Hölder proof. GitHub math delimiters and separated display blocks
preserve the equations.

The final finite-proof and source readers both checked the SHA-256 above.
The allocation/separation joins and companion scope were also read in that
same final text. No unresolved integration issue was found in these
selected claims. Changes to the mathematical text require a bounded delta
review; this verdict does not preapprove a later manuscript.

G1–G3 in [the scientific scope](../SCIENTIFIC_SCOPE.md) are complete for
this repository exposition. G4 remains: combine the integrated exposition
and minimal evidence map at one reviewed freeze, including one scoped
reproduction of the essential exact quarter-rank certificate. Existing
pass reports are preserved and are not represented as fresh executions.
