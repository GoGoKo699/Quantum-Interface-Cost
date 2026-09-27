# Quantitative stability at the sharp two-mode boundary

Research base: `3d230411930a2ac198cdb7f2ef9ad86701face1a` (PR #46).
Status: derived with the proofs below; the component arguments were
independently reconstructed within this workspace. This is internal
mathematical review, not external peer review or a priority claim.

The [sharp support theorem](SHARP_TWO_MODE_SUPPORT.md) proved
`U+m<=4sqrt(3)` and classified its equality boundary. Here that boundary
has an explicit neighborhood. For arbitrary ququart binary-POVM
readouts, put

```math
H_0=X_1\otimes B_1+Z_1\otimes D_1+
    X_2\otimes B_2+Z_2\otimes D_2,
\qquad \epsilon=4\sqrt3-(U+m),
\tag{1}
```

where `U>=m` are the two largest eigenvalues and the four memory
operators are Hermitian contractions. For every third such pair,
`h_3=X_3 tensor B_3+Z_3 tensor D_3`, we prove

```math
\boxed{\epsilon\le2^{-32}
\quad\Longrightarrow\quad
\|H_0+h_3\|<\frac{16}{3}<4+\sqrt2.}
\tag{2}
```

A larger sufficient width is available when the second eigenvalue is
above the one-mode threshold:

```math
\boxed{m\ge2+\sqrt2,\quad\epsilon\le2^{-24}
\quad\Longrightarrow\quad
\|H_0+h_3\|<4+\sqrt2.}
\tag{3}
```

Both widths are conservative constants, not optimal stability radii.
Equation (2) has no assumption on `m`. Neither statement covers the
whole remaining spectral strip or settles the unrestricted converse.

## 1. Deficits of an actual two-mode head

Let `V:C^2 -> R_1 R_2 Q` identify two leading orthonormal eigenvectors,
and set `sigma=VV^*/2`. Purify sigma by a qubit E and trace out Q to
obtain `rho` on `R_1 R_2 E`. Thus

```math
\operatorname{rank}\rho\le4,\qquad
\rho_E=I_E/2.
```

Write `S=sqrt(rho)`, let Pi be its support projection, and let
`A` run over `X_1,Z_1,X_2,Z_2`, with identity factors understood.
The Schmidt-transpose identity from the support theorem gives

```math
C_A=\operatorname{Tr}_R(A\sigma),\qquad
f_A=\|C_A\|_1=\|SAS\|_1.
```

Set

```math
\eta=3-\sum_A f_A^2,\qquad
\eta_0=\frac{\sqrt3}{2}\epsilon,\qquad q=\sqrt{\eta_0}.
\tag{4}
```

The actual energy and the squared support budget imply

```math
\sum_A f_A\ge2\sqrt3-\epsilon/2,\quad
0\le\eta\le\eta_0-\epsilon^2/16\le\eta_0,\quad
\sum_A(f_A-\sqrt3/2)^2\le\eta_0.
\tag{5}
```

The middle bound follows by Cauchy--Schwarz; for the last, expand the
square and use `sum f_A^2<=3`. All subsequent estimates retain both
the squared-budget deficit and the equal-weight score information.
The case `epsilon=0` is already covered by the sharp equality theorem.
In the strict quantitative comparisons in Sections 3--6 we therefore
assume `epsilon>0`, so q is positive. The flatness lemma below also
includes eta zero.

## 2. A flatness estimate from chirality

For any flat rank-two head as above, independently of its readouts,

```math
\eta\le\frac9{100}
\quad\Longrightarrow\quad
\operatorname{rank}\rho=4,\qquad
d:=\|S-\Pi/2\|_2\le\frac34\sqrt\eta,
\qquad \|\rho-\Pi/4\|_1\le\frac32\sqrt\eta.
\tag{6}
```

Here and below `||.||_2` is the Hilbert--Schmidt norm. To prove (6),
put `T=Tr_R S` and `d_0=1-Tr(T^2)/2`. The affinity, Pauli-conjugation
and marginal AM--GM steps of the support proof give the exact
nonnegative decomposition

```math
\eta=\sum_A\bigl[\operatorname{Tr}(SASA)-f_A^2\bigr]
 +\left[2+\frac12\operatorname{Tr}T^2
              -\sum_A\operatorname{Tr}(SASA)\right]+d_0.
\tag{7}
```

The marginal step gives `Tr(T^2)<=rank(rho)/2`, hence
`eta>=1-rank(rho)/4`. In particular the rank is four if `eta<1/4`.

Let `Gamma=Y_1Y_2 tensor I_E`, `S'=Gamma S Gamma`, and

```math
E_0=(S+S')/2-I_R\otimes T/4,\qquad
a_0=2\|E_0\|_2^2,\qquad o=\operatorname{Tr}(SS').
```

The nonidentity reference words in E_0 have Pauli-conjugation gap at
least two. Orthogonality of the reference Pauli coefficients gives

```math
\eta\ge a_0+d_0,\qquad o=a_0-d_0\ge0.
\tag{8}
```

Squaring `S+S'=I_R tensor T/2+2E_0` and partially tracing over R
is useful because `Tr_R E_0=0`. The mixed terms vanish exactly:

```math
T^2+4\operatorname{Tr}_R E_0^2
 =I_E+\operatorname{Tr}_R(SS'+S'S).
\tag{9}
```

Squared root fidelity is at most affinity, so
`||SS'||_1^2<=Tr(SS')=o`. Thus

```math
\|T^2-I\|_1\le2a_0+2\sqrt o.
\tag{10}
```

Write the eigenvalues of `T^2` as `1-d_0+r,1-d_0-r`, where `r>=0`.
Then `r<=a_0+sqrt(o)`. Equations (8) imply
`0<=o<=eta`, `d_0<=(eta-o)/2`, and `a_0<=(eta+o)/2`.
Consequently `lambda_min(T^2)>=1-eta-sqrt(eta)>=61/100>9/16`,
so `T>=3I/4` for the stated range. Since the rank is four,

```math
d^2=2-\operatorname{Tr}T
 =d_0+\frac12\|T-I\|_2^2
 \le d_0+\frac{16}{49}
       \left[d_0^2+(a_0+\sqrt o)^2\right].
\tag{11}
```

For fixed o the last expression increases with d_0, with
`a_0=o+d_0`. Substitute `d_0=(eta-o)/2`. Its bracket is
`N=o+(eta+o)sqrt(o)+(eta^2+o^2)/2`. The elementary estimates

```math
\eta\sqrt o\le\tfrac32\eta^2+o/6,\qquad
o\sqrt o\le3o/10,\qquad o^2/2\le9o/200
```

give `N<=(907/600)o+2eta^2<=(49/32)o+2eta^2`. Therefore
`d^2<=eta/2+(32/49)eta^2<=9eta/16`; the last comparison uses
`eta<=9/100<49/512`. Schatten Cauchy--Schwarz gives
`||rho-Pi/4||_1<=2d`, completing (6).

This flatness lemma applies throughout the strip `m>=2+sqrt(2)`:
there `(U+m)/2>=2+sqrt(2)`, so
`eta<=3/2-sqrt(2)<9/100`. It does not by itself construct a nearby
channel: the approximation `Pi/4` need not have E marginal `I/2`.

## 3. A quantitative affinity equality statement

The standard squared-fidelity/affinity inequality is the same prior
ingredient used in [STRONG_ENTROPIC_CONVERSE.md](../STRONG_ENTROPIC_CONVERSE.md),
Section 3, and in the sharp support proof. The following remainder
estimate uses only Hilbert--Schmidt Cauchy--Schwarz.

For one A put `f=||SAS||_1`, `a=Tr(SASA)`, `delta=a-f^2`.
Choose `W=sign(SAS)` as a Hermitian unitary preserving Pi, with any
unitary sign extension on its kernel. Set
`J=S^(1/2) A S^(1/2)` and `K=S^(1/2) W S^(1/2)`.
Then `Tr(JK)=f`, `||J||_2^2=a`, and `||K||_2^2<=1`.
It follows that

```math
\|J-fK\|_2^2\le\delta,
\qquad
\|\Pi A\Pi-fW\Pi\|_2
 \le\frac{\sqrt\delta}{s_{\min}(S)}.
\tag{12}
```

The second step is congruence by `S^(-1/2)` on its support.
For `q<=2^-12`, (6) gives `s_min(S)>=1/2-d>=1/2-3q/4`.
Also `delta<=eta_0` by (7). Using (5), multiplying the difference
in (12) to compare squares yields

```math
\left\|(\Pi A\Pi)^2-\frac34\Pi\right\|_2
 \le\left[\frac{2}{1/2-3q/4}+2\sqrt3+2q\right]q
 <8q.
\tag{13}
```

The factor two in the scalar-square term is `||Pi||_2=2`.
This direct remainder estimate avoids taking a further square root
of the flatness error.

## 4. Round the complementary state to a balanced channel

Assume from now on `q<=2^-12`. We prove that, after a memory unitary,
the actual head channel `Phi(omega)=Tr_R(V omega V^*)` satisfies

```math
\inf_{\Psi\ \mathrm{EB}}\|\Phi-\Psi\|_\diamond\le1500q.
\tag{14}
```

The diamond norm is not divided by two. The approximating channel
will be one of the balanced square-POVM channels in Section 4 of
[SHARP_TWO_MODE_SUPPORT.md](SHARP_TWO_MODE_SUPPORT.md).

Set `F=2Pi-I`, and project it onto just the four nonidentity reference
words:

```math
L=\sum_A A\otimes M_A,\qquad R=F-L,\qquad a=\|R\|_2.
```

Let N be the part of S outside the reference span
`I,X_1,Z_1,X_2,Z_2`. The Pauli gap gives `||N||_2<=q/sqrt(2)`.
Writing `Delta=S-Pi/2`, exact marginal normalization gives
`T-I=Tr_R(S-2S^2)=-2Tr_R(S Delta)` and hence
`||T-I||_2<=2(1+2d)d`. Projection and the triangle inequality now give

```math
a\le4\|N\|_2+8d+8d^2\le9q,\qquad
b:=\|L^2-I\|_2\le a(2+a)\le19q.
\tag{15}
```

Each `M_A=(1/4)Tr_R(AF)` is a Hermitian contraction: its expectation
in any E vector is the normalized trace pairing of A with a reference
compression of the contraction F. The distinct reference-Pauli
coefficients of `L^2-I` give

```math
\|[M_{X_i},M_{Z_i}]\|_2\le b/2,\qquad
\|\{M_A,M_B\}\|_2\le b/2\quad(A,B\text{ on different sites}).
\tag{16}
```

For a query A let `D=A_opp tensor M_opp`, the opposite-axis term
on its site. The exact identity
`AFA=F-2D+(ARA-R)`, together with (16), gives

```math
\|\{F,D\}-2I_R\otimes M_{\rm opp}^2\|_2
 \le\sqrt3 b+2a.
```

Compress with `Pi=(I+F)/2`. The same three coefficient relations
also control the commutator with `M_opp^2`; explicitly they give

```math
\begin{split}
\|(\Pi A\Pi)^2-[\Pi-\Pi(I_R\otimes M_{\rm opp}^2)\Pi]\|_2
 &\le\sqrt3 b/2+2a\le35q,\\
\|[\Pi,I_R\otimes M_{\rm opp}^2]\|_2
 &\le\sqrt3 b+a\le42q.
\end{split}
\tag{17}
```

For clarity, in the second line one expands `[L,M_opp^2]` and uses
`[M,M_opp^2]=[M,M_opp]M_opp+M_opp[M,M_opp]` at the same site,
or `[M,M_opp^2]={M,M_opp}M_opp-M_opp{M,M_opp}` across sites.
Orthogonality of the three reference words contributes `sqrt(3)`;
the R term contributes a. The first line follows by substituting the
displayed anticommutator into the compressed conjugation identity.

Put `K_0=I_R tensor(M_opp^2-I/4)`. Equations (13) and (17) give
`||Pi K_0 Pi||_2<=43q` and `||[Pi,K_0]||_2<=42q`.
The diagonal and off-diagonal blocks are orthogonal, so

```math
\|K_0\Pi\|_2\le\sqrt{43^2+42^2}\,q<61q.
```

Moreover `||Pi-4rho||_2<=6d`, so
`||Tr_R Pi-2I||<=12d<=9q` and `Tr_R Pi>=1.9I`.
Taking the partial trace in `||K_0Pi||_2^2` therefore gives

```math
\|M_A^2-I/4\|_2\le45q\qquad\text{for every A}.
\tag{18}
```

The numerical comparisons used here are
`sqrt(43^2+42^2)<61` and `61/sqrt(1.9)<45`.
For `q<=2^-12`, (18) puts both eigenvalue magnitudes of each M_A
strictly between `.48` and `.52`. Such an M_A cannot be definite:
for a coefficient M_B on the other site, definiteness would imply
`||{M_A,M_B}||_2>=2(.48)^2 sqrt(2)`, contrary to (16).
Thus each M_A has one eigenvalue of each sign. Define

```math
N_A=\tfrac12\operatorname{sign}(M_A)
    =\tfrac12\boldsymbol n_A\cdot\boldsymbol\sigma_E.
```

Scalar spectral calculus and (18) give `||M_A-N_A||_2<46q`:
the denominator `|lambda(M_A)|+1/2` exceeds `.98`.
Transferring (16) to the N_A introduces at most
`(1.04+1)46q` extra error. Since half-Pauli commutators and
anticommutators have Hilbert--Schmidt norms respectively
`|n cross n'|/sqrt(2)` and `|n dot n'|/sqrt(2)`, we obtain

```math
|\boldsymbol n_{X_i}\mathbin\times\boldsymbol n_{Z_i}|\le147q,
\qquad
|\boldsymbol n_A\cdot\boldsymbol n_B|\le147q
\quad(A,B\text{ on different sites}).
\tag{19}
```

Here `(19/2+2.04*46)sqrt(2)<147`. Choose the first site's axis
as `n_X1`, and the second as the normalized perpendicular projection
of `n_X2`. Nearest-sign alignment within each site changes a half
Pauli by at most `147q` in Hilbert--Schmidt norm; the perpendicular
projection costs at most another `147q`. All projections are nonzero
because `147q<1/2`. We obtain exact coefficients `M_A^*` of magnitude
one half, parallel within each site and orthogonal across sites.
Consequently `F^*=sum_A A tensor M_A^*` is a balanced reflection and

```math
\|F-F^*\|_2
 \le9q+4(46+294)q=1369q.
\tag{20}
```

The factor four here is the Hilbert--Schmidt norm of the four-term
Pauli expansion when each coefficient error is bounded by `340q`:
`||sum_A A tensor E_A||_2^2=4 sum_A||E_A||_2^2`.

Let `Pi^*=(I+F^*)/2` and `rho^*=Pi^*/4`. Then `rho_E^*=I/2`.
Diagonalizing the two reference bisectors shows that its head channel
measures the four-outcome square POVM and prepares four orthogonal
memory states; it is entanglement breaking. Uhlmann's overlap theorem
permits a memory unitary aligning purifications with vector distance
at most

```math
x:=\|\sqrt\rho-\sqrt{\rho^*}\|_2
 \le d+\|F-F^*\|_2/4\le343q.
\tag{21}
```

Both complements have rank four, so the memory alignment uses Q itself.
Tracing out R bounds the normalized Choi trace distance by `2x`.
For qubit input, diamond distance is at most twice that trace distance.
Thus it is at most `4d+||F-F^*||_2<=1372q<1500q`, proving (14).
These are coherent channel bounds; no cross-mode blocks were discarded.

## 5. The unconditional explicit neighborhood

Assume `epsilon<=2^-32`, so `q<=2^-16`. Use the memory alignment in
(21) and the corresponding balanced flat head `sigma^*`.
Trace-norm contraction gives `||sigma-sigma^*||_1<=2x`.
Trace-norm duality for the reference partial trace therefore yields

```math
\|C_A-C_A^*\|_2\le\|C_A-C_A^*\|_1\le2x.
\tag{22}
```

The balanced construction in Section 4 of the sharp support theorem has
`|C_A^*|=(sqrt(3)/8)I`, for each of the four original queries, including
all the within-site signs in the rounding above. Since
`x<=343/65536<1/64`, every C_A is invertible and
`lambda_min|C_A|>1/8`, while `lambda_min|C_A^*|>1/5`.

We use an elementary Hermitian sign estimate. If invertible Hermitian
C and C' have minimum eigenvalue magnitudes mu and mu', then

```math
\|\operatorname{sign}C-\operatorname{sign}C'\|_2
 \le\frac{2}{\mu+\mu'}\|C-C'\|_2.
\tag{23}
```

In eigenbases of C and C', each matrix entry satisfies this divided
difference bound: entries with equal eigenvalue signs vanish, and
opposite signs have `|lambda-lambda'|>=mu+mu'`.
Equations (22)--(23) imply
`||sign C_A-sign C_A^*||_2<13x`.

Let B_A denote the actual decoder for query A, and put
`delta_A=f_A-Tr(B_A C_A)>=0`. Actual head energy and the global
support bound give `sum_A delta_A<=epsilon/2`. For a Hermitian
contraction B_A and `W_A=sign C_A`, expansion of the square gives

```math
\frac18\|B_A-W_A\|_2^2
 \le\operatorname{Tr}|C_A|(B_A-W_A)^2
 \le2\delta_A.
\tag{24}
```

The last inequality uses `B_A^2<=I` and that W_A commutes with
`|C_A|`. Cauchy--Schwarz now yields
`sum_A||B_A-W_A||_2<=sqrt(32 epsilon)<6sqrt(epsilon)<7q`.

Define the allowed balanced Hamiltonian
`H_0^*=sum_A A tensor sign(C_A^*)`. It is exactly one of the equality
decoders classified in the sharp support theorem. Combining (21)--(24),

```math
\|H_0-H_0^*\|
 \le52x+7q\le17843q<18000q<\frac13.
\tag{25}
```

The last comparison uses `54000<65536`. The same arbitrary h_3 is
allowed with H_0^*, and its established equality-boundary estimate is

```math
\|H_0^*+h_3\|\le\frac{4+2\sqrt5}{\sqrt3}<5.
```

The triangle inequality proves (2). This proof never infers
`m>=2+sqrt(2)` from a small sum deficit. It controls the four actual
readouts through their trace-norm optimality gaps instead.

## 6. Larger width on the high-second-eigenvalue strip

The [robust head-channel converse](ROBUST_HEAD_CHANNEL_CONVERSE.md)
proves that `m>=2+sqrt(2)` and diamond distance at most `2/5` to an
entanglement-breaking channel suffice for the actual-tail two-mode
envelope to pass every last-query test, strictly. Its proof centers the
resolvent before taking the channel difference and uses two elementary
quadratic estimates; it needs no equality of the two leading energies.

If additionally `epsilon<=2^-24`, then `q<=2^-12`, so (14) gives
`dist_diamond(Phi,EB)<=1500/4096<2/5`. This proves (3).
The stronger width in (3) is conditional on the stated m threshold;
the smaller width in (2) is unconditional.

## 7. The zero squared-deficit boundary and its exceptional branch

There is a simple exact dichotomy:

```math
\eta=0\quad\Longrightarrow\quad
\Phi\text{ is entanglement breaking}
\quad\text{or}\quad \sum_A f_A\le2+\sqrt2.
\tag{26}
```

Indeed (6) makes `rho=Pi/4`, and the vanishing Pauli gap makes
`F=2Pi-I=sum_A A tensor M_A`. Its coefficients commute within each
site and anticommute across sites, with `sum_A M_A^2=I`.
Thus the four full summands pairwise anticommute, and each `M_A^2`
commutes with Pi. The zero-deficit case of (12), together with the
exact counterpart of (17), yields
`(Pi A Pi)^2=f_A^2 Pi=Pi-Pi(I tensor M_opp^2)Pi`.
Since `Tr_R Pi=2I`, faithfulness gives

```math
M_{\rm opp}^2=(1-f_A^2)I.
\tag{27}
```

Every nonzero Hermitian qubit coefficient is therefore scalar or
traceless. A nonzero scalar coefficient forces both coefficients on
the other site to vanish by anticommutation. If the remaining squared
magnitudes are `a^2,b^2`, then `a^2+b^2=1` and the fidelity profile
is `(a,b,1,1)` up to order, giving the second alternative in (26).
Otherwise all coefficients are traceless; commutation makes their
Bloch axes parallel within sites and perpendicular between nonzero
sites. This is the weighted Clifford form
`F=(aX_1+bZ_1) tensor n.sigma_E+(cX_2+dZ_2) tensor n'.sigma_E`,
where `a^2+b^2+c^2+d^2=1`. Diagonalizing its two commuting reference
factors expresses `(I+F)/8` as four pure-E blocks of weight one fourth.
Their purification is measure and prepare, proving the EB alternative.
In particular `m>2+sqrt(2)` excludes the exceptional branch exactly
at eta zero; (26) asserts no quantitative extension.

The exceptional branch is physical. The readouts
`B_1=D_1=I`, `B_2=X_A`, `D_2=Z_A` have
`U=m=2+sqrt(2)` and head channel `Phi(omega)=I_A/2 tensor omega_B`.
Its complement is
`rho=|n+><n+|_(R_1) tensor I_(R_2)/2 tensor I_E/2`, where
`n=(X+Z)/sqrt(2)`. Thus eta is zero, with
`(f_X1,f_Z1,f_X2,f_Z2)=(1/sqrt(2),1/sqrt(2),1,1)`.
Its full diamond distance from EB channels is exactly one: the Bell
Choi state on E,B has trace distance at least one from any separable
state, while comparison with dephasing B gives the matching upper
bound. An arbitrary-state use of eta alone cannot imply EB proximity.
Equation (5)'s equal-weight score information is essential above.

## 8. Scope and verification

The present result quantifies the earlier compactness neighborhood.
The widths are explicit sufficient constants obtained by rounded
inequalities, not an estimate of the true distance to a violation.
The full two-mode strip, the three complete remaining reflection
signatures, unrestricted optimality and publication originality remain
unresolved. No numerical scan is used in any proof above.

Independent readers reconstructed the full integrated argument,
including the squared-chirality identity, affinity remainder,
coefficient rounding, scalar constants, sign stability and the
distinction between (2) and (3).

Reproduce the targeted checks from the repository root with

```bash
python tools/check_quantitative_two_mode.py --output results/quantitative_two_mode.json
```

The [checker](../../tools/check_quantitative_two_mode.py) evaluates
exact rational constant comparisons and floating-point identities for
seven fixed matrix constructions: three specified nonclassical-family
points and four specified head perturbations. It does not scan a
parameter space or replace the universal proofs. The
[result record](../../results/quantitative_two_mode.json) stores
`source_sha256` and the two entries of `proof_note_sha256`, tying it to
both reports. Repeated execution is expected to reproduce the same
record for the same files and runtime environment; floating-point
eigenvectors or residuals can differ across environments. These checks
do not certify an unrestricted converse or publication novelty.
