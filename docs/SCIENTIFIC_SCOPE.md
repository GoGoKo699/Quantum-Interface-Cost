# Scientific scope and completion gates

Consolidation checkpoint: 27 September 2026. Research base:
`357a4dfd523e0b895dbeead46fb1e3190c7afd78` (PR #57).
This document selects a bounded scientific package from the research
record. It changes neither theorem statements nor their proof status.
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

| Gate | State at this checkpoint | Completion condition |
|---|---|---|
| G1. Scope and attribution | Claim map selected; focused comparisons recorded, including the recent bottleneck-dimension framework | Reconcile every selected claim and citation with the integrated proof exposition; narrow any claim if the source comparison requires it |
| G2. Integrated proof exposition | Individual proof notes and internal reconstructions exist; the core argument is readable but still contains research continuations | Produce one consistent exposition of the selected theorems with complete assumptions, notation, equality scope and essential arithmetic appendices; internally review that exact version |
| G3. Asymmetric comparison | Full comparison class and construction are explicitly recorded | Retain this class definition beside the separation wherever it is stated; do not replace it with an unrestricted-optimality claim |
| G4. Evidence freeze | Minimal proof/checker/report map pinned to the research base; historical reports preserved | Freeze the integrated claim ledger and evidence manifest at one reviewed commit, resolving discrepancies before manuscript drafting |

The next task is G2: consolidate and review the selected proof exposition,
using G1's source map while doing so. This is an editorial and verification
pass over proved results. Manuscript drafting follows the completed gates.
Passing diagnostics is not a substitute for proof review or prior comparison.

## 6. Stopping rule and future work

Stop exploratory theorem development for this package. Make corrections
needed for the selected claims and their sources, then move to drafting
after the completion gates are closed. No additional input size, spectral
neighborhood, or decoder family is needed merely to enlarge the result list.

The unrestricted all-n retention conjecture, the sharp general entropy
inequality, and the asymptotic common-accuracy rate remain open. The
smallest unresolved equal-accuracy case is `(n,q)=(5,2)`. They are future
work rather than prerequisites for this bounded paper. The failed general
root-affinity bound cannot be reused as a proof of any of them.
