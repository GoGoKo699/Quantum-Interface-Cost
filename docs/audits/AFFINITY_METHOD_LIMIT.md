# The limit of the affinity method

Date: 27 September 2026. Research base:
`ced383d1a4ad8d9c13fbd4ebe1befd3c6284519a`.
Status: supplied deductions, internally independently reconstructed;
integrated internal review complete. This is not external peer review or a
publication-priority claim. The entropy-energy and Faber–Krahn inequalities
used below are established results of Beigi and their classical antecedents.

The affinity surrogate used in the finite converse proofs cannot obey the
retention bound in all dimensions. An explicit 15-qubit seed of rank 16
violates that proposed surrogate bound, while its original trace-norm
score stays strictly below retention. We also evaluate the surrogate's
exact entropy profile and asymptotic rank-rate profile, and identify the
decoder information discarded by the relaxation.

For a positive seed root S with Tr(S²)=1 write

```math
G(S)=\sum_{i=1}^n\sum_{U=X_i,Z_i}
\sqrt{\mathrm{Tr}(SUSU)},\qquad
g(S)=\sum_{i=1}^n\sum_{U=X_i,Z_i}\|SUS\|_1.
\qquad\text{(1)}
```

The established fidelity–affinity comparison gives g≤G. The sharp
rank conjecture for g remains open beyond the proved cases; replacing
g by G in that conjecture is false.

## 1. A finite star counterexample

Let B=(X+Z)/√2, and label its local eigenvectors by 0 and 1. In their
n-fold product basis define

```math
S_n=\frac1{\sqrt2}|0^n\rangle_B\langle0^n|
+\frac1{\sqrt{2n}}\sum_{i=1}^n|e_i\rangle_B\langle e_i|.
\qquad\text{(2)}
```

This is positive, has rank n+1, and satisfies Tr(S_n²)=1. The star
support and central/leaf weights are the same elementary construction
used in [EXACT_AXIS_SPECTRAL_REDUCTION](../EXACT_AXIS_SPECTRAL_REDUCTION.md),
Section 3.4, now in the bisector product basis. No new star eigenvalue or
graph extremal theorem is asserted.

For a diagonal S with amplitudes s_x, both original local queries satisfy

```math
\mathrm{Tr}(SX_iSX_i)=\mathrm{Tr}(SZ_iSZ_i)
=\frac12\left(\sum_xs_x^2+\sum_xs_xs_{x\oplus e_i}\right).
```

Only the center/leaf edge contributes to the second sum in (2), so

```math
a_{X_i}=a_{Z_i}=\frac12\left(1+\frac1{\sqrt n}\right),
\qquad G(S_n)=n\sqrt{2+\frac2{\sqrt n}}.
\qquad\text{(3)}
```

At n=15 the rank is 16=2⁴, and

```math
G(S_{15})^2-(8+11\sqrt2)^2
=144+30\sqrt{15}-176\sqrt2>\frac{46}{7}>0.
\qquad\text{(4)}
```

The exact witnesses are √15>19/5 and √2<10/7, verified by
15·25−19²=14 and 10²−2·7²=2. Thus the proposed implication

```math
\mathrm{rank}S\le2^q\quad\Longrightarrow\quad
G(S)\le2q+\sqrt2(n-q)
\qquad\text{(5)}
```

fails at (n,q)=(15,4). No minimality of n is claimed.

For two adjacent diagonal amplitudes a,b, the corresponding query block
is, up to signs and diagonal unitaries,

```math
\frac1{\sqrt2}\begin{pmatrix}a^2&ab\\ab&-b^2\end{pmatrix},
```

with trace norm √(a⁴+6a²b²+b⁴)/√2. At a fixed site in (2), one block
has a²=1/2,b²=1/(2n), while the other n−1 leaves each contribute
1/(2n√2). Therefore

```math
g(S_n)=\frac{\sqrt{n^2+6n+1}+n-1}{\sqrt2},\qquad
g(S_{15})=\sqrt2(7+\sqrt{79})<16\sqrt2<8+11\sqrt2.
\qquad\text{(6)}
```

The last comparisons use 79<81 and 50<64. The existing
[product-diagonal entropy theorem](../COMMUTING_SEED_BOUND.md), which
allows correlated eigenvalues and zeros, also bounds this original score.
Thus this is neither an operational advantage nor an entropy-conjecture
counterexample. Tensor powers give the same strict separation at
(n,q)=(15m,4m): both scores add, and the rank is 2⁴ᵐ. These tensor factors
are distinct input sites in one seed, not repeated unknown specimens.

The general star formulas give the stronger obstruction

```math
G(S_n)-\sqrt2n\sim\sqrt{n/2},\qquad
g(S_n)-\sqrt2n\longrightarrow\sqrt2,\qquad
\log_2\mathrm{rank}S_n=\log_2(n+1).
\qquad\text{(6a)}
```

Indeed, the exact rationalizations are

```math
G(S_n)-\sqrt2n=
\frac{\sqrt2\sqrt n}{\sqrt{1+1/\sqrt n}+1},\qquad
g(S_n)-\sqrt2n=
\frac{2\sqrt2n}{\sqrt{n^2+6n+1}+n+1}<\sqrt2.
```

Thus no finite universal constant C can make
G(S)≤√2n+C log₂(rank S) valid for all n and S. This excludes every
linear logarithmic-rank charge for the surrogate, not just the
retention coefficient in (5). Taking n=2^q−1 makes the rank exactly
2^q, so the obstruction also applies to integer qubit caps.

## 2. The sharp entropy and asymptotic rank profiles

Let h₂ be binary entropy in bits, p_R=h₂⁻¹(R) in [0,1/2], and

```math
\Phi(R)=\sqrt{\frac12+\sqrt{p_R(1-p_R)}}.
```

For every n and 0≤R≤1, the exact fixed-entropy surrogate optimum is

```math
\max_{\substack{S\ge0,\ \mathrm{Tr}S^2=1\\
S_{\rm vN}(S^2)=nR}}G(S)=2n\Phi(R).
\qquad\text{(7)}
```

Its exact asymptotic rank-rate profile is

```math
\boxed{\lim_{n\to\infty}\frac1{2n}
\max_{\substack{S\ge0,\ \mathrm{Tr}S^2=1\\
\mathrm{rank}S\le2^{\lfloor Rn\rfloor}}}G(S)=\Phi(R).}
\qquad\text{(8)}
```

These are elementary corollaries of Beigi's established inequalities and
matching commuting constructions, not new Faber–Krahn inequalities.

For the upper bounds, put d=2ⁿ, τ=Tr/d, A=√d S and
K=Σᵢ(id−Eᵢ), where Eᵢ is normalized partial trace at i followed by
identity reinsertion. Beigi's Theorem 2 gives

```math
\mathcal D:=\tau(AK(A))\ge
n\left(\frac12-\sqrt{p(1-p)}\right),
\qquad\text{(9)}
```

where p=h₂⁻¹(S_vN(S²)/n). His Theorem 4 gives the same bound with
p=h₂⁻¹(log₂(rank S)/n). Expanding A=Σ_wc_wσ_w, with Σ_wc_w²=1,
direct Pauli conjugation gives

```math
\sum_{i,U=X_i,Z_i}\mathrm{Tr}(SUSU)
=2n-2\mathcal D-2\sum_wN_Y(w)c_w^2\le2n-2\mathcal D.
```

Cauchy proves both upper bounds, including the floor in (8), since Φ
is continuous and increasing.

For entropy equality, let

```math
\rho_p=\frac{I+(1-2p)B}{2},\qquad
S_n^{\rm prod}=(\sqrt{\rho_p})^{\otimes n}.
```

Its entropy is n h₂(p), and all 2n affinities equal

```math
\mathrm{Tr}(\sqrt{\rho_p}U\sqrt{\rho_p}U)
=\frac12+\sqrt{p(1-p)},\qquad U=X,Z.
\qquad\text{(10)}
```

There is no Pauli Y contribution, and scalar Cauchy is an equality.
This proves (7), including the endpoints.

For the rank lower bound, fix 0<p<a<1/2 with h₂(a)<R. In the B product
basis let Π_n retain strings of weight at most r_n=⌊an⌋, and set

```math
Z_n=\Pr\{\mathrm{Bin}(n,p)\le r_n\},\qquad
T_n=\frac{\Pi_n S_n^{\rm prod}}{\sqrt{Z_n}}.
\qquad\text{(11)}
```

This is positive and normalized. Its exact rank is

```math
\sum_{k=0}^{r_n}\binom nk\le2^{n h_2(a)}\le2^{\lfloor Rn\rfloor}
\quad\hbox{whenever }n(R-h_2(a))\ge1.
\qquad\text{(12)}
```

Indeed, every included string has Bernoulli(a) probability at least
$`2^{-n h_2(a)}`$, and these probabilities sum to at most one. This is a
deterministic rank cap, not an average memory allowance or a physical
postselection protocol. Pairing strings across a local edge gives

```math
\mathrm{Tr}(T_n X_iT_n X_i)
=\mathrm{Tr}(T_n Z_iT_n Z_i)
=\frac12+\sqrt{p(1-p)}\,
\frac{\Pr\{\mathrm{Bin}(n-1,p)\le r_n-1\}}{Z_n}.
\qquad\text{(13)}
```

Both probabilities tend to one. For example, Chebyshev gives
1−Z_n≤p(1−p)/[n(a−p)²]. Thus G(T_n)/(2n) converges to the right side
of (10) under its square root. Given 0<R<1, take p<a<p_R and then
let p↑p_R. This proves (8). At R=0 and R=1, respectively use a pure
bisector tensor power and S=I/√d.

Alternatively, the construction has the dimension-independent continuity
estimate

```math
\|T_n-S_n^{\rm prod}\|_2^2=2(1-\sqrt{Z_n})\le2(1-Z_n),
\qquad
\frac{|G(T_n)-G(S_n^{\rm prod})|}{2n}
\le2^{3/4}(1-Z_n)^{1/4}.
\qquad\text{(14)}
```

The second inequality follows from |Tr(SUSU)−Tr(TUTU)|≤2||S−T||₂
for normalized positive S,T, followed by the scalar square-root bound.

## 3. The decoder information discarded by the surrogate

Let ρ=S² have support projector P. Work on ran(P), so S is invertible,
and compress an original query U to B_U=PUP. Put

```math
F=\|S B_U S\|_1,\qquad a=\mathrm{Tr}(S B_U S B_U).
```

Choose a Hermitian unitary J extending sign(S B_U S) on its zero
eigenspace. The unitary extension is required below. Then F=Tr(S B_U S J).
Weighted Hilbert–Schmidt Cauchy, for the positive inner product
⟨C,D⟩_S=Tr(S C* S D), gives

```math
b:=\mathrm{Tr}(SJSJ)>0,\qquad
F^2\le ab,\qquad b=1-\frac12\|[S,J]\|_2^2\le1.
```

Consequently the squared gap has the exact nonnegative decomposition

```math
\boxed{a-F^2=a(1-b)+(ab-F^2),\qquad
ab-F^2=b\left\|S^{1/2}
\left(B_U-\frac FbJ\right)S^{1/2}\right\|_2^2.}
\qquad\text{(15)}
```

In particular, a−F²≥(a/2)||[S,J]||₂². The first term records the
decoder's mixing of unequal seed amplitudes; the second is the weighted
Cauchy residual. Both are lost on replacing F by √a.

The equality characterization is complete. If B_U=0 then a=F=0.
Otherwise F>0 and

```math
F^2=a\quad\Longleftrightarrow\quad
[B_U,\rho]=0\quad\hbox{and}\quad B_U^2=F^2P.
\qquad\text{(16)}
```

For necessity, equality in (15) forces b=1, [S,J]=0 and B_U=FJ.
Conversely, the right side of (16) gives |S B_U S|=Fρ and a=F².
There is also a simultaneous rigidity consequence. Write
ρ=Σ_kλ_kP_k for its distinct positive eigenvalues, r_k=rank P_k and
σ_k=P_k/r_k. If F_U²=a_U holds for every query, then (16) gives

```math
(P_kUP_k)^2=F_U^2P_k,\qquad
\|\sqrt{\sigma_k}U\sqrt{\sigma_k}\|_1=F_U
\quad\hbox{for every }k,U.
\qquad\text{(16a)}
```

Every flat spectral block therefore has exactly the same entire query
profile as ρ, and g(S)≤Γ(n,min_k r_k). A single simple positive
eigenvalue forces g(S)≤√2n. More generally, a nonflat seed of rank at
most 2^q that saturates all comparisons obeys $`g(S)\le\Gamma(n,2^{q-1})`$, since
there are at least two positive spectral blocks. These are conditional
statements about exact saturation, not an evaluation of the unrestricted
rank optimum.

For the mixed bisector state in (10), set t=2√(p(1−p)). Both queries have

```math
a=\frac{1+t}{2},\qquad F^2=\frac{1+t^2}{2},\qquad
b=\frac{1+t^3}{1+t^2},
```

```math
a-F^2=\frac{t(1-t)}2,
\quad a(1-b)=\frac{t^2(1-t^2)}{2(1+t^2)},
\quad ab-F^2=\frac{t(1-t)^2}{2(1+t^2)}.
\qquad\text{(17)}
```

At p=1/10, a=4/5, F²=17/25, b=76/85, and
3/25=36/425+3/85. These values persist for each local query under tensor
powers. Hence G(S_prod)=4n/√5, whereas g(S_prod)=2n√17/5.
The gap decomposition explains why the asymptotically sharp surrogate
profile need not evaluate the original score.

## 4. Prior comparison, scope and verification

Beigi, [arXiv:2105.00462v2](https://arxiv.org/pdf/2105.00462v2),
Theorem 2, equations (6)–(7), printed p. 4, is the entropy-energy theorem.
Remark 3, printed p. 5, explicitly records product saturation.
Theorem 4, printed p. 6, is the rank bound and records its established
commutative asymptotic sharpness at fixed log(rank)/n.
Samorodnitsky, [arXiv:0807.1679](https://arxiv.org/pdf/0807.1679),
Theorem 1.4, printed pp. 6–7, gives the classical fractional-edge-boundary
profile and asymptotic extremality of Hamming balls. In (9), the commuting
Dirichlet form is one quarter of his oriented-edge form. These results
allow nonconstant amplitudes; set-indicator edge isoperimetry cannot be
silently substituted for them. The ordinary fidelity–affinity comparison
and its prior source are recorded in
[STRONG_ENTROPIC_CONVERSE](../STRONG_ENTROPIC_CONVERSE.md), Section 3.

The finite affinity converses through four input qubits remain valid.
The universal rank retention conjecture for the original score g, the
general sharp entropy inequality, and the common-accuracy asymptotic rate
remain unresolved. Formula (8) concerns fixed R; it does not determine
the fixed-codimension regimes rank≤2ⁿ⁻¹ or rank≤2ⁿ⁻². The construction
and profile identify a limitation of the surrogate, not a collective
advantage for the original workload.

The finite formulas, profiles and gap identity have been independently
reconstructed internally. The bounded check

```sh
python tools/check_affinity_method_limit.py --output results/affinity_method_limit.json
```

checks explicit formulas and small matrix instances; the analytical
proofs above establish the quantified statements. The
[result record](../../results/affinity_method_limit.json) pins the source
and proof-note hashes; these finite checks do not establish the
quantified theorem or publication novelty.
