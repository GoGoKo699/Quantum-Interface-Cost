# A sharp readout bound from one parity symmetry

Reviewed main: `ef3a6c9f62f7b9b591b56503ba5d24e0b10d2c12` (PR #24).
Date: 2026-09-23. This continues the
[coherent-transfer audit](COHERENT_TRANSFER_AUDIT.md).

**Proved:** one product-parity symmetry gives an exact local-readout envelope
at every block size. Its proof uses one binary measurement and the established
measurement characterization of fidelity. It excludes a further two-qubit
entropy-witness family: states whose top-two spectral subspace is a locally
rotated parity sector, with arbitrary unequal core eigenvalues and complex
coherences. The general coherent-transfer bound remains unproved.

## 1. Sharp theorem at every block size

Use `g_n(rho)=sum_{i,U=X,Z} ||sqrt(rho) U_i sqrt(rho)||_1`.
Let `R_i` be any single-qubit Pauli axis, including axes with a Y component,
and put `R=R_1 tensor ... tensor R_n`. Suppose

    [rho,R]=0, q=Tr[rho(I+R)/2], r=2q-1.

Thus q and 1-q are the two parity weights. Neither block need be flat,
separable, or real. For any local unit Pauli observable U_i, write
`z=Tr(R_i U_i)/2`. With root fidelity,

\[
\boxed{\|\sqrt\rho U_i\sqrt\rho\|_1
\leq\sqrt{1-r^2(1-z^2)}.} \tag{1}
\]

The state `rho_q=(I+rR)/2^n`, uniform inside each parity sector, attains
(1) for **every local Pauli direction simultaneously**. Thus (1) is the
exact envelope at fixed R and q, not merely an upper estimate.

For the actual local X/Z queries this gives

\[
\boxed{g_n(\rho)\leq n\sqrt{2+8q(1-q)}.} \tag{2}
\]

It is attained by rho_q when each R_i is an X/Z bisector. In particular,
a seed contained entirely in one parity sector has

    g_n(rho)<=sqrt(2)n,

regardless of its rank or entanglement. Such a seed cannot exceed the
classical score in the normalized-seed optimization.

### One binary measurement proves (1)

For `s=sqrt(1-z^2)>0`, define the Hermitian observable

    A=(R-U_i R U_i)/(2s).

The local Pauli identity gives

    {R,U_i R U_i}=2(2z^2-1)I, A^2=I, U_i A U_i=-A.

Since rho commutes with R, cyclicity of trace then gives

    Tr(rho U_i R U_i)=(2z^2-1)r, Tr(rho A)=sr.

Consequently measuring `(I+A)/2,(I-A)/2` on rho and U_i rho U_i gives
the swapped binary laws `(1+sr,1-sr)/2` and `(1-sr,1+sr)/2`.
Quantum root fidelity is at most the classical fidelity of any measurement;
the latter is `sqrt(1-s^2 r^2)`. This proves (1). If s=0, simply use
root fidelity at most one. No invertibility or real-state assumption occurs.

The measurement is a mathematical witness, not an added operational query.
The original task still has one unknown specimen, one delayed query,
arbitrary collective encoders, free finite classical records, worst-case
quantum dimension and uniform arbitrary-input error.

### Attainment and summation

Diagonalize the local R axes only as proof coordinates. For rho_q, each
fixed string on the other n-1 sites leaves a qubit with Bloch vector `+r`
or `-r` along R_i. Direct two-dimensional fidelity evaluation yields
`sqrt(1-r^2(1-z^2))` in every normalized block. This proves simultaneous
attainment, including q=0,1 and singular rho_q.

For X_i,Z_i, their squared projections onto R_i sum to at most one.
Cauchy–Schwarz therefore gives

    F_Xi+F_Zi <=sqrt(2[2(1-r^2)+r^2(z_Xi^2+z_Zi^2)])
              <=sqrt(4-2r^2)=sqrt(2+8q(1-q)).

Summing proves (2). Bisector axes make both inequalities equalities for
rho_q. At q=1/2, all axes attain the score 2n; bisectors are not necessary.

## 2. A further complete two-qubit entropy family

**Corollary.** Suppose a projector onto two largest eigenvalues of a
two-qubit state can be written

    P=(I+R_1 tensor R_2)/2.

Then `g_2(rho)<=2sqrt(2)+(2-sqrt(2))S(rho)`. Degeneracies are allowed
provided such a top-two spectral projector exists. The remaining spectrum
and all complex coherences within P and its complement are unrestricted.

Write `epsilon=lambda_3+lambda_4`, `q=1-epsilon`,
`m=lambda_2/q`, and `rho=q sigma direct-sum epsilon tau`.
The [spectral-tail gate](TWO_QUBIT_SPECTRAL_TAIL_GATE.md) covers
epsilon>=1/29. The [unbalanced-core gate](TWO_QUBIT_CORE_STABILITY.md),
Section 10, covers m<=1/5. Rank-at-most-two states are already proved.
In the residual strip, (2) gives the elementary bound

    g_2(rho)<=2sqrt(2+8epsilon)<=2sqrt(66/29)<61/20.

The exact block entropy identity and monotonicity of h_2 give

    S(rho)=h_2(epsilon)+q h_2(m)+epsilon S(tau)
          >=(28/29)h_2(1/5)>(28/29)(2/3).

Here `h_2(1/5)=log_2(5)-8/5>2/3` follows from `5^15>2^34`.
Using `sqrt(2)>7/5` and `2-sqrt(2)>1/2`,

    2sqrt(2)+(2-sqrt(2))S(rho)>14/5+28/87.

The gap from the score bound is `25/348>1/16`. Thus this strip is
strictly entropy-valid. Combining the cases proves the corollary.

This is stronger than knowing that the **projector** P has maximally
mixed marginals: rho itself may have nonzero marginal Bloch vectors.
It includes nonflat rank-three and full-rank states, and does not require
a stabilizer eigenbasis. It does not cover every parity-commuting state:
its two largest eigenvectors may instead lie in different parity sectors.
Nor does (2) alone prove the all-n entropy bound for mixed parity weights.

For example, in the ordered parity basis `(00,11;01,10)`, the state

    rho=(99/100) sigma direct-sum (1/100) tau,
    sigma=[[11/20,i sqrt(3)/20],[-i sqrt(3)/20,9/20]],
    tau=diag(4/5,1/5)

has spectrum `(297/500,99/250,1/125,1/500)`, so epsilon=1/100 and
m=2/5. It has an unequal coherent core and nonzero local Bloch vectors;
the corollary covers it without removing that coherence.

## 3. The coherent-transfer target on parity supports

Use `L_U=sqrt(sigma)PUPsqrt(sigma)` and
`X_U=sqrt(sigma)PUQsqrt(tau)` from the preceding audit. For opposite
two-qubit parity supports P,Q and arbitrary normalized sigma,tau,

\[
\mathcal S_t=\sum_U\left\|\begin{pmatrix}
L_U&tX_U/2\\tX_U^\dagger/2&0
\end{pmatrix}\right\|_1
\leq2\sqrt{2+2t^2},\qquad 0\leq t\leq1. \tag{3}
\]

This bound is sharp, attained by flat core and tail and bisector parity
axes. It is not asserted sharp at each prescribed unequal core spectrum.

For a query on site 1, put `Omega=sigma+tau` and
`H=PUP+(t/2)(PUQ+QUP)`. Its block norm is the root fidelity
`F(Omega,H Omega H)` for positive operators. Dephasing site 2 in the R_2
basis commutes with H and can only increase this fidelity. Monotonicity
extends from states to positive operators by homogeneity; no normalization
or successful branch is discarded.

In the resulting two classical flags, let x_j,y_j be the sigma,tau
weights, with both sums one. The block norms are

    sqrt[z^2 x_j^2+t^2(1-z^2)x_j y_j].

Cauchy–Schwarz bounds their sum by `sqrt[z^2+t^2(1-z^2)]`.
The two orthogonal query projections satisfy `z_X^2+z_Z^2<=1`;
since t<=1, summing the queries gives (3). Flat parity blocks saturate
every step. This proof allows complex core/tail coherences before dephasing.

On the required domain `t<=1/sqrt(7)`, `m>=1/5`,

    S_t<=8/sqrt(7)<16/5<G(m),
    G(m)=sqrt(2)+sqrt[4-2(1-2m)^2].

Indeed G increases on [0,1/2] and
`G(1/5)=sqrt(2)+sqrt(82)/5>7/5+9/5`.
Thus the previous audit's Eq. (4) is **proved on parity supports**, even
without its positive increment. It is still unproved on arbitrary supports.

## 4. Primary-source provenance and novelty boundary

The short proof is a direct symmetry specialization of established
fidelity theory. Fuchs and van de Graaf, *Cryptographic Distinguishability
Measures for Quantum Mechanical States*,
[quant-ph/9712042v2](https://arxiv.org/abs/quant-ph/9712042v2), 3 April 1998,
Definition 8 / Eq. (23) and Proposition 4 / Eq. (24), printed p. 13, give
the minimum-over-measurements characterization of root fidelity, crediting
Fuchs–Caves. The source uses root fidelity B, not its square.

Equivalently, trace-norm duality for the same A gives
`D(rho,U_i rho U_i)>=|sr|`, where D is half trace distance. Their Theorem 1,
Eq. (46), p. 17, has `D<=sqrt(1-B^2)` and immediately yields (1).
The source's parity-coded ensembles in Section 7, pp. 22–25, are specified
mixtures of nonorthogonal product codewords; they should not be identified
with the optimization over all parity-commuting density matrices by name alone.

The explicit witness, simultaneous attainer and entropy-family consequence
are supplied deductions. The underlying fidelity inequality is prior, and
this elementary corollary is not proposed as a new general information
principle. A targeted source comparison is not a certification of originality.

The separate [mixed-decoder note](MIXED_DECODER_PATTERN_BOUND.md) proves
a sharper auxiliary operator envelope and a classification threshold below
sqrt(21/2). It does not extend the already certified high-score tail region.
Publication originality of that operator evaluation also remains unresolved.

## 5. Verification and remaining work

The original conditional-qubit proof and the shorter binary-witness proof
were reconstructed independently within the workspace. The equality state,
all-n summation, entropy case split and restricted transfer bound were also
checked independently. This is internal mathematical review, not peer review.

The standard-library checker `tools/check_parity_and_decoder.py` verifies
the exact rational entropy comparison and the companion operator note's
determinant and scalar identities. The recorded output and precise evidence
scope are linked from [reproducibility](../REPRODUCIBILITY.md). Neither this
finite algebra check nor exploratory numerical searches prove the unrestricted
transfer inequality. The theorem rests on the displayed analytical arguments.

No open PR duplicated this work at the reviewed commit. LICENSE and the
historical initial audit are unchanged. All 189 local file links in the
changed Markdown documents resolve, and `git diff --check` passes.
The remaining two-qubit witness
must additionally have no top-two spectral projector of the parity form
above. Generic unequal coherent cores remain; the full all-n entropy bound,
unrestricted equal-accuracy optimality and publication originality remain open.
