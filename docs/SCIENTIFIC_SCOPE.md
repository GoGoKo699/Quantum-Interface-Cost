# Scientific scope and completion gates

Consolidation checkpoint: 27 September 2026. Initial consolidation base:
`38fd9d3f2c3e38ef5e8a7c5d6b2c041955678d8a` (PR #58).
This document selects a bounded scientific package from the research
record and tracks its integration. The mathematical theorem statements
are unchanged.
Internal proof reconstruction is not external peer review; the focused
source comparison does not certify the absence of all prior results.

## 1. The question and the selected contribution

**When is retaining original qubits optimal for delayed local X/Z readout?**

The selected answer has three parts. Original-site retention is optimal
for equal accuracy at every integer memory budget through four inputs.
With one memory qubit, it realizes the entire achievable accuracy region
at every input size. With larger memory and unequal accuracies, an
explicit collective encoder exceeds the full retention comparison class
defined below. The balanced-spectrum theorem supplies an all-size
structural companion, with stability as supporting material.

The operational setting is fixed: one unknown n-qubit specimen, arbitrary
collective encoding before one local X or Z query is revealed, unrestricted
finite classical storage, and quantum output dimension at most `2^q` on
every branch. Binary output probabilities must be correct to the stated
tolerance uniformly over every input state and every query. There are no
additional copies, source reaccess, free entanglement, or successful-branch
postselection. Average branch dimension and common-state reconstruction
are different resource models.

## 2. Claim map

Put `F_U(rho)=||sqrt(rho) U sqrt(rho)||_1`,
`g(rho)=sum_{U=X_i,Z_i} F_U(rho)`, and
`Gamma(n,D)=max_{rank(rho)<=D} g(rho)`, for density matrices rho.
The [seed reduction](COLLECTIVE_ENCODING_REDUCTION.md) gives
`eta_max(n,q)=Gamma(n,2^q)/(2n)` for common contrast eta.
The uniform binary total-variation error is `(1-eta)/2`.
For unequal accuracies, `x_i,z_i` are the target contrasts in `[0,1]`
for `X_i,Z_i`, respectively, and `[a]_+=max(a,0)`.

| Role | Exact statement | Proof and boundary |
|---|---|---|
| Main finite theorem | `Gamma(n,2^q)=2q+sqrt(2)(n-q)` for `1<=n<=4`, integer `0<=q<=n` | [Core argument, Section 3](CORE_ARGUMENT.md#3-exact-equal-accuracy-retention-through-four-inputs); arbitrary spectra, collective encoders and query-dependent decoders |
| Main allocation theorem | At every n, dimension two realizes precisely the profiles with `sum_i w(x_i,z_i)<=1`, where `w=[x+z-1-sqrt(2(1-x)(1-z))]_+` | [Allocation proof](ONE_QUBIT_ALLOCATION_REGION.md); an operational deduction using established Cheng–Hall monogamy and the local incompatibility weight |
| Main collective separation | At `n=31,q=5`, all `x_i=1`, `z_i=1/sqrt(31)` are achievable, whereas every protocol in the retention class with all `x_i=1` obeys `sum_i z_i<=5` | [Core argument, Section 4](CORE_ARGUMENT.md#4-a-collective-advantage-with-five-memory-qubits); establishes a separation, not the unrestricted optimum |
| Structural companion | For `rho=(I+tR)/2^n`, R any traceless Hermitian reflection, `max_R g(rho)=2n-2+sqrt(4-2t^2)` | [Balanced-spectrum proof](audits/BALANCED_SPECTRUM_OPTIMALITY.md); every n and `0<=t<=1`, unrestricted eigenvectors; this is a constrained spectral family |
| Supporting stability | Flat half-rank score gap epsilon implies full trace-norm distance at most `16sqrt(2epsilon)` from a retention seed | [Stability proof](audits/BALANCED_SPECTRUM_STABILITY.md); constant independent of n, square-root exponent necessary |
| Supporting nonflat extension | At rank at most `k=2^(n-1)`, `sqrt(2(1-Tr(sqrt(rho))/sqrt(k)))<=1/(4096n)` implies `g(rho)<=2n-2+sqrt(2)` | Same proof; a sufficient spectral neighborhood at every n, with equality only at retention seeds; the radius is not claimed optimal |

At `t>0`, every balanced-spectrum maximizer is the original-site state
`(I+tB)/2`, where `B=(+/-X +/-Z)/sqrt(2)`, tensored with maximally mixed
spectators. The two signs are independent. The flat endpoint
`t=1` covers every seed of the form `P/2^(n-1)` for a rank-`2^(n-1)`
projector P. It does not establish the unrestricted half-rank optimum
for arbitrary spectra at larger n.

The nontrivial finite increments beyond the classical/exact endpoints
and the all-n one-qubit theorem are exactly

| `(n,q)` | Exact Gamma | Essential converse |
|---|---|---|
| `(3,2)` | `4+sqrt(2)` | [Half-rank converse](audits/HALF_RANK_RETENTION_CONVERSE.md) |
| `(4,2)` | `4+2sqrt(2)` | [Nonflat quarter-rank converse](audits/NONFLAT_QUARTER_RANK_CONVERSE.md), using [quarter-rank geometry](audits/QUARTER_RANK_GEOMETRY.md) and its exact polynomial certificate |
| `(4,3)` | `6+sqrt(2)` | Half-rank converse |

Equality classifications concern maximizing normalized seeds. They do
not classify every physical instrument or say that every optimal encoder
literally retains original sites. The allocation theorem says that the
same achievable effects have a retention implementation.

## 3. The asymmetric comparison class

The separation allows branch-dependent retained sites and operations,
and joint measurements of discarded sites. Specifically, the instrument
admits a Kraus refinement in which every nonzero branch factors across a
subset T of the original sites as
`K_c=M_c tensor <v_c|`, with `|T|<=q`. The output dimension remains at
most `2^q`; T, M and v may depend on the classical branch. This is the
class for which the retention upper bound is proved. It is not the class
of all collective encoders.

For nonnegative a,b its normalized-seed argument gives
`sum_i(a x_i+b z_i)<=q(a+b)+(n-q)sqrt(a^2+b^2)`.
When all `x_i=1`, letting a grow with b=1 yields `sum_i z_i<=q`.
The complete 32-dimensional collective instrument has
`sum_i z_i=sqrt(31)>5`. Its zero decoder eigenvalues prescribe fair
binary outputs, not discarded branches. The proof uses exact operator
identities and requires no matrix simulation on 31 qubits.

This heterogeneous separation says nothing adverse about the proved
equal-accuracy optima. Nor does it settle the equal-accuracy conjecture
outside those finite ranges.

## 4. Proof and source organization

The finite theorem has one short dependency chain: operational twirl and
normalized-seed reduction; one-qubit allocation from monogamy; finite
half-rank and quarter-rank converses; assembly with the classical and
exact endpoints. The exact-axis construction is an independent branch.
Balanced optimality and stability are structural companions, not
dependencies of the finite theorem.

Use the [focused prior comparison](CORE_PRIOR_COMPARISON.md) to distinguish
the established framework and ingredients from the selected evaluations.
Use the [core evidence map](CORE_EVIDENCE_MAP.md) to locate proofs, exact
certificates and existing diagnostic reports. The long
[literature comparison](LITERATURE_COMPARISON.md),
[claim ledger](STATUS.md) and [reproducibility record](REPRODUCIBILITY.md)
remain the historical research record. Their earlier open-case statements
must be read at their recorded research bases.

The product-diagonal formation profile, extensive entropy exclusions,
and earlier decoder classifications are outside this paper's selected
core. They remain available in the repository. The affinity obstruction
and spectral-layer comparison can supply a short explanation of the open
general problem if needed; they are not additional headline claims.

## 5. Bounded completion gates

| Gate | State at this checkpoint | Evidence or next action |
|---|---|---|
| G1. Scope and attribution | Completed for the selected repository exposition | [Focused source map](CORE_PRIOR_COMPARISON.md) reconciled with the integrated argument; established frameworks and ingredients remain explicitly credited. This is a bounded comparison, not exhaustive priority certification |
| G2. Integrated proof exposition | Completed and internally reviewed | [Core argument](CORE_ARGUMENT.md) and [exact-text review](audits/INTEGRATED_CORE_REVIEW.md); consistent model and notation, connecting lemmas, all finite-case boundaries, and links to essential frozen proof appendices |
| G3. Asymmetric comparison | Completed in the integrated statement | The complete instrument, existence of a factorizing Kraus refinement for the comparison class, and strict separation are stated together in Section 4; no unrestricted optimum is asserted |
| G4. Evidence freeze | Completed for the selected scientific package | [Freeze record](SCIENTIFIC_EVIDENCE_FREEZE.md) and [manifest](../results/scientific_evidence_freeze.json) pin 36 files to the reviewed PR #59 base; one essential exact-certificate reproduction is byte-identical to the historical report, which remains unchanged |

All four gates are complete for this repository's selected scientific
package. The [freeze record](SCIENTIFIC_EVIDENCE_FREEZE.md) reconciles the
older evidence-map fingerprints and the exact-text integration review at
one scientific base. The package is prepared for manuscript drafting.
The manuscript must preserve the reviewed claims and source boundaries;
no further exploratory theorem campaign is a prerequisite. Internal
review and a successful reproduction do not certify publication originality
or preapprove the eventual manuscript.

## 6. Stopping rule and future work

Exploratory theorem development for this package is paused. Corrections
to the selected claims and their sources remain in scope. No additional input size,
spectral neighborhood, or decoder family is needed merely to enlarge the result list.

The unrestricted all-n retention conjecture, the sharp general entropy
inequality, and the asymptotic common-accuracy rate remain open. The
smallest unresolved equal-accuracy case is `(n,q)=(5,2)`. They are future
work rather than prerequisites for this bounded paper. The failed general
root-affinity bound cannot be reused as a proof of any of them.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s
self-directed learning. For discussion or potential collaboration, please
contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
