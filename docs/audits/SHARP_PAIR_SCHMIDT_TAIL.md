# Sharp pairs require a nonzero Schmidt tail

**Research base:** main `9fc2be03587986d85341aa3f766653e6ba94bb75`. **Date:** 24 September 2026.

For two internally anticommuting sharp readout pairs, every state of
Schmidt rank at most two across references versus memory has score at most
three. This is attained. Applied to an actual top eigenvector, it gives
a joint constraint on its Hamiltonian eigenvalue and its Schmidt tail.
It excludes the full-rank synthetic obstruction in the preceding
[joint-spectrum report](JOINT_SPECTRUM_NORMAL_FORM.md), Section 5.
The companion [two-sharp-pair converse](TWO_SHARP_PAIR_CONVERSE.md)
combines these constraints with the exact last-readout theorem and an
exact scalar certificate to prove the bound `4+sqrt(2)` for two such
sharp pairs and one arbitrary third pair.

The proof uses an elementary operator inequality for two positive
operators with a common maximally mixed **center** marginal. This is the
opposite marginal orientation from the mixed-Choi inequality used in
[the single-double-block report](SINGLE_DOUBLE_BLOCK_CONVERSE.md),
Section 3. That earlier inequality is not substituted for this one.

**Status:** supplied proof with independent internal reconstruction.
Publication priority remains unresolved. These are intermediate necessary
constraints on actual joint data; their sufficient combination is proved
in the companion converse. The unrestricted interface optimum, arbitrary
earlier Jordan angles, and the remaining complete reflection signatures
remain open.

## 1. A common-qubit-center inequality

Let Q be a qubit and let E on R1 tensor Q and F on R2 tensor Q satisfy

\[
E,F\ge0,\qquad
\operatorname{Tr}_{R_1}E=\operatorname{Tr}_{R_2}F=I_Q/2.
\tag{1}
\]

Spectator identities are implicit. Then

\[
\boxed{E+F\le\tfrac32 I.}
\tag{2}
\]

The leaves may have arbitrary finite dimensions; only qubit leaves are
needed below. The proof depends on the center dimension through (1).

Both operators have trace one. Put p=||E|| and q=||F||. If either
is at most 1/2, (2) follows from the other's norm being at most one.
Otherwise p,q>1/2, and their top eigenvectors v,w are unique. All
other eigenvalues of E are at most 1-p, and likewise for F, so

\[
E\le(1-p)I+(2p-1)|v\rangle\langle v|,
\quad
F\le(1-q)I+(2q-1)|w\rangle\langle w|.
\tag{3}
\]

Let P and R be those rank-one projectors with their respective spectator
identities inserted. Partial tracing `p|v><v|<=E` and its counterpart gives

\[
\|\operatorname{Tr}_{R_1}|v\rangle\langle v|\|
\le\frac1{2p},\qquad
\|\operatorname{Tr}_{R_2}|w\rangle\langle w|\|
\le\frac1{2q}.
\tag{4}
\]

Write V and W for their coefficient matrices, with leaf indices as rows
and the common center as columns. The cross matrix of the two insertion
isometries is `W V^dagger`, up to the ordering of its input and output
indices. Consequently

\[
\|PR\|\le\|V\|\|W\|\le\frac1{2\sqrt{pq}}.
\tag{5}
\]

For positive a,b, the two-projection Gram bound is

\[
\|aP+bR\|\le
\frac{a+b+\sqrt{(a-b)^2+4ab\|PR\|^2}}2.
\tag{6}
\]

For completeness, use the insertion maps to express the nonzero spectrum
as that of a two-by-two block Gram matrix with diagonal blocks aI,bI
and off-diagonal norm `sqrt(ab)||PR||`. Its quadratic form is bounded by
the corresponding scalar two-by-two matrix, giving (6).

Substitute (5) into (6), with `a=2p-1,b=2q-1`, and add the scalar
baseline in (3). This gives

\[
\|E+F\|\le 1+\frac12
\sqrt{4(p-q)^2+(2-1/p)(2-1/q)}\le\frac32.
\tag{7}
\]

The last inequality is elementary. Set x=2p-1 and y=2q-1 in [0,1]
and assume x>=y by symmetry. Both summands below increase with x on
[y,1], so

\[
(x-y)^2+\frac{4xy}{(1+x)(1+y)}
\le(1-y)^2+\frac{2y}{1+y}
=1-\frac{y^2(1-y)}{1+y}\le1.
\tag{8}
\]

This proves (2), including the endpoint cases already separated above.
Two Bell projectors attain 3/2. A Bell projector together with
`|0><0|` on the other leaf tensored with `I_Q/2` also attains it.

## 2. Sharp score on every two-dimensional memory subspace

Now let memory Q have dimension four, and let

\[
H_0=h_1+h_2,\qquad
h_i=X_i\otimes B_i+Z_i\otimes D_i,
\tag{9}
\]

where B_i,D_i are anticommuting Hermitian reflections. The operators
`S_i=X_i tensor B_i` and `T_i=Z_i tensor D_i` are commuting reflections.
Their joint positive projector is

\[
\Pi_i=\frac{(I+S_i)(I+T_i)}4.
\]

Examining their four possible joint signs and tracing the reference gives

\[
h_i=S_i+T_i\le2\Pi_i,\qquad
\operatorname{Tr}_{R_i}\Pi_i=I_Q/2.
\tag{10}
\]

The second identity follows because S_i, T_i and S_iT_i each have a
traceless reference Pauli factor. No subsystem representation is needed.

Choose any two-dimensional memory subspace, with isometry
`W:C^2 -> Q`. Its compressed Bell operators

\[
E_i=(I_{R_i}\otimes W^\dagger)\Pi_i(I_{R_i}\otimes W)
\]

satisfy (1) on the same compressed center. Thus (2) and (10) imply

\[
\boxed{(I_R\otimes W^\dagger)H_0(I_R\otimes W)\le3I.}
\tag{11}
\]

Every normalized state of Schmidt rank at most two across `(R1 R2):Q`
lies in such a subspace. Hence its expectation of H_0 is at most three.
The statement covers arbitrary Schmidt coefficients and arbitrary
reference and memory Schmidt vectors. No shared memory factorization
for the two readout pairs is assumed.

The constant is attained: choose Q=A tensor B, both readout pairs to be
the X/Z Paulis on their respective memory qubits, and use

\[
|\Phi^+\rangle_{R_1A}\otimes|0\rangle_{R_2}\otimes|0\rangle_B.
\]

The first pair contributes two and the second contributes one. The state
has Schmidt rank two across references versus memory. This attaining
state need not be a top eigenvector of the full four-dimensional-memory
Hamiltonian; the latter has a different top state in this example.

### 2.1. Equality forces a flat Bell core and a pure spectator

The pure states attaining score three have a simple form. Identify their
occupied two-dimensional memory with a logical qubit. Up to interchanging
the references, they are

\[
|\mathrm{Bell}\rangle_{R_1,\mathrm{logical}}\otimes|\chi\rangle_{R_2},
\qquad \langle\chi|Y|\chi\rangle=0.
\]

The Bell vector is matched to the first pair's compressed Pauli frame.
In particular the two nonzero Schmidt eigenvalues are both 1/2.

To see this, score three forces equality in (2). The norm envelope and
the equality cases of (8) restrict the two top Choi eigenvalues to
`(p,q)=(1,1),(1,1/2),(1/2,1)`. If both are one, both compressed
operators are Bell projectors, so their corresponding readouts are
traceless qubit Pauli pairs. The three-qubit Cheng--Hall correlation
inequality bounds the sum of the four squared X/Z correlations by two.
Cauchy--Schwarz then bounds the score by `2sqrt(2)<3`, excluding this
case. The precise prior ingredient is Cheng--Hall,
[*Anisotropic invariance and the distribution of quantum correlations*,
arXiv:1610.09302v3](https://arxiv.org/pdf/1610.09302), Eq. (14),
`M_AB+M_AC<=2`, with M the sum of the two largest squared correlation
singular values. The relevant qubit deduction is also given in the
[antiunitary report](ANTIUNITARY_READOUT_BOUND.md), Section 2.

Thus, after relabeling, E is a Bell projector and F has norm 1/2.
Equality forces unit expectation of E and expectation 1/2 of F. The
state consequently factors as the Bell vector times a pure reference
state chi. Its logical-memory marginal is I/2, so expectation 1/2 of F
forces all of F's unit trace onto `|chi> tensor logical`. Positivity and
the fixed center marginal imply `F=|chi><chi| tensor I/2`. Reading its
X/Z coefficients shows that the second pair's score is
`<X>_chi^2+<Z>_chi^2=1-<Y>_chi^2`. It reaches one exactly in the X/Z
plane. This classifies the state and the compressed readouts; it does
not require the full memory algebras to commute outside that support.

## 3. A chiral compression lemma

The following linear-algebra statement transfers compression bounds to
actual top eigenvectors. Suppose a Hermitian H anticommutes with an
involution Gamma and has chiral block form

\[
H=\begin{pmatrix}0&C\\C^\dagger&0\end{pmatrix}.
\]

Let U>0 be the largest singular value of C and m the second largest,
counted with multiplicity. Choose unit singular vectors u,v with
`Cv=Uu`, `C^dagger u=Uv`, so `Omega=(u+v)/sqrt(2)` is a top eigenvector.
Let Pi be an orthogonal projection commuting with Gamma. If

\[
\|\Pi H\Pi\|\le k,\qquad U-m\le k,
\tag{12}
\]

and `w=<Omega|Pi|Omega>`, `tau=1-w`, then

\[
\boxed{Uw-m\tau\le k.}
\tag{13}
\]

To prove this, write `a=||Pi u||^2=w+z` and
`b=||Pi v||^2=w-z`. Necessarily `|z|<=min(w,tau)`. Remove one top
singular component:

\[
C=U|u\rangle\langle v|+C',\quad
C'v=0,\quad C'^\dagger u=0,\quad \|C'\|\le m.
\]

If a,b>0, test the compressed C between the normalized vectors Pi u
and Pi v. The unnormalized residuals `Pi u-a u` and `Pi v-b v`
have norms `sqrt(a(1-a))` and `sqrt(b(1-b))`. Dividing their product
by sqrt(ab) bounds the normalized C' contribution. Consequently

\[
k\ge U\sqrt{ab}-m\sqrt{(1-a)(1-b)}
=U\sqrt{w^2-z^2}-m\sqrt{\tau^2-z^2}.
\tag{14}
\]

If `mw>=U tau`, then w>=tau and the right side of (14) is
nondecreasing in z^2: its derivative is

\[
\frac12\left[\frac{m}{\sqrt{\tau^2-z^2}}
-\frac{U}{\sqrt{w^2-z^2}}\right]\ge0.
\]

Indeed the ratio of the square roots is at least w/tau, with zero
endpoints handled by continuity. Thus (14) is at least `Uw-m tau`,
proving (13) in this case. If `mw<U tau`, then
`tau>m/(U+m)`, and directly

\[
Uw-m\tau=U-(U+m)\tau<U-m\le k.
\]

If a or b is zero, w<=1/2 and therefore
`Uw-m tau <= (U-m)/2 <= k`. This covers the cases in which the
normalized compression test is undefined. The proof also covers a
degenerate U, for which m=U.

## 4. The sharp-pair top-state bounds

For H_0 in (9), conjugation by `Gamma=Y_1 Y_2 tensor I_Q` sends H_0
to -H_0. The chiral positive and negative spaces both have dimension
eight. Thus its top two eigenvalues U,m are the top two singular values
of its chiral off-diagonal block.

The established sharp-pair inequalities give `U<=4` and `m>=2`, hence
`U-m<=2`. For m>=2, compress reference R2 onto a Y eigenstate: its own
pair vanishes, and the remaining h_1 has eigenvalue two with multiplicity
two. Interlacing gives the claim. The norm bound U<=4 is the triangle
inequality. These arguments do not assume a common memory subsystem.

Let Omega be a normalized top eigenvector and let its ordered memory
marginal eigenvalues be lambda_1,...,lambda_4. Choose Pi on memory as
the projector onto its two leading Schmidt vectors, so

\[
\tau=\lambda_3+\lambda_4,\qquad w=1-\tau.
\]

This memory projection commutes with Gamma. Equation (11) and chiral
symmetry give `||Pi H_0 Pi||<=3`. Applying (13) with k=3 yields

\[
\boxed{\lambda_3+\lambda_4\ge
\max\left\{0,\frac{U-3}{U+m}\right\}.}
\tag{15}
\]

In particular an actual top state at U>3 has Schmidt rank at least
three. In the nontrivial interface range U>2+sqrt(2), the bound forces
a positive quantitative tail; no limit of rank-two top states can
reach that range.

There is a companion rank-one bound. For a fixed unit memory vector q,
antico-mmutation gives
`<B_i>_q^2+<D_i>_q^2<=1`: every real linear combination of the two
reflections has norm equal to the Euclidean norm of its coefficients.
The compressed pair is therefore a reference-qubit field of norm at
most one. The two sites together have compressed norm at most two.
Apply (13) with k=2 to the leading memory Schmidt vector to obtain

\[
\boxed{\lambda_1\le\frac{2+m}{U+m}.}
\tag{16}
\]

The hypothesis `U-m<=k` holds in both applications. No simplicity of U
or nondegeneracy of the memory spectrum is required. Any corresponding
top vector and any choice among tied leading Schmidt vectors can be used.
The conclusions depend on its actual eigenvector relation to H_0; they
are not constraints on an unrelated state with the same eigenvalues.

### 4.1. A stronger two-eigenvalue circle

There is also a stronger replacement for the earlier linear spectral-sum
bound:

\[
\boxed{(U-2)^2+(m-2)^2\le4.}
\tag{17}
\]

Use the two projectors Pi_i from (10), now with their spectator reference
identities. Each has rank four on the 16-dimensional full space, and

\[
\operatorname{Tr}(\Pi_1\Pi_2)
=\operatorname{Tr}_Q[(I_Q/2)(I_Q/2)]=1.
\]

The squared principal cosines c_1^2,...,c_4^2 of their ranges therefore
sum to one, with c_1>=c_2>=...>=0. The two greatest eigenvalues of
Pi_1+Pi_2 are 1+c_1 and 1+c_2. Since `H_0<=2(Pi_1+Pi_2)`, eigenvalue
monotonicity gives `U<=2+2c_1` and `m<=2+2c_2`. Both U and m are at
least two. Squaring and summing proves (17).

Cauchy--Schwarz recovers `U+m<=4+2sqrt(2)` from (17); the circle
retains information that the sum discards. The independent-memory-pair
point `(U,m)=(4,2)` attains the circle. The sharp example with
`U=m=2+sqrt(2)` in the preceding report, Section 7, also attains it.
No claim is made here that every point on the circular arc is realizable.

## 5. Both supplied synthetic failures are now excluded

The preceding report's synthetic tuple

\[
\lambda=(29,29,1,1)/60,\quad U=7/2,\quad m=1/2+2\sqrt2
\]

cannot arise as actual top data. It has tau=1/30, while (15) requires

\[
\tau\ge\frac{1/2}{4+2\sqrt2}>\frac1{30}.
\]

For example the weaker consequence `U(1-2tau)<=3`, following from
(15) because m<=U, already fails with left side 49/15. The circle
also excludes it: its left side minus four is `(17-12sqrt(2))/2>0`.

A second full-rank synthetic tuple was found while testing whether the
Schmidt bounds alone supplied the missing constraint:

\[
\lambda=(87,87,13,13)/200,\quad U=37/10,\quad m=3/10+2r,
\qquad r=\sqrt2.
\tag{18}
\]

It passes (15)--(16), since tau=13/100 and

\[
\begin{aligned}
(U+m)\tau-(U-3)&=(13r-9)/50>0,\\
(2+m)-(U+m)\lambda_1&=14/25+(113/100)r>0.
\end{aligned}
\]

It also passes the preceding six-Pauli condition, with
`E_*=1369/2500` and gap `453/800-E_*=373/20000>0`, and the exact
unrestricted fixed-spectrum score bound, since
`3631/1250-(17/10)^2=37/2500>0`.

Nevertheless the circle excludes this tuple as well:

\[
(U-2)^2+(m-2)^2-4=\frac{489-340r}{50}>0,
\qquad 489^2-2(340)^2=7921>0.
\]

For completeness it really does fail the resolvent criterion before
this exclusion. With `t=37/10-r`, `c=U-m=2(t-2)`, the fixed allowed
block `a=b=1` in both extreme eigenvalue pairs gives

\[
c\sum_j\Phi_t(\lambda_j,\lambda_{5-j})-1
\ge\frac{4883-3440r}{500t(t+2)}>0,
\]

where `4883^2-2(3440)^2=176489>0`. The explicit lower witness is
approximately `1.0036963291152832`; all strict signs above have exact
arithmetic proofs in the diagnostic.

These examples demonstrate why each additional necessary constraint
must be checked. Both are synthetic data now analytically ruled out for
the sharp-pair Hamiltonian. Neither is a counterexample to the combined
current constraints, the actual rank-one certificate, or the physical
retention conjecture. The companion [converse](TWO_SHARP_PAIR_CONVERSE.md)
now proves that (15)--(17), the preceding SLD bounds, and scalar bounds on
the exact resolvent suffice for two internally anticommuting sharp pairs
and an arbitrary third pair. General nonorthogonal earlier pairs remain
outside that theorem. No realizable resolvent failure is supplied.

## 6. Verification, provenance, and operational scope

The proof uses spectral ordering, positive partial trace, coefficient
matrix singular norms, and a two-projection Gram estimate. These are
established linear-algebra ingredients. The bound in (2) is proved here
in full for the required fixed-center orientation. Its publication
priority and relation to other recovery-monogamy theorems have not been
settled. In particular, Renes's opposite-direction recovery region and
the prior separate-leaf unital-map argument are not cited as proving (2).

The [deterministic diagnostic](../../tools/check_sharp_pair_schmidt_tail.py)
and [recorded output](../../results/sharp_pair_schmidt_tail.json) check
the exact scalar identities and the synthetic exclusion, general positive
fixed-center operators, sharp-pair compressions, the rank-two attainer,
and both top-vector tail inequalities. All matrices are at most 16 by 16;
no optimizer is used. Floating checks supplement the supplied proof and
do not establish a universal inequality by sampling.

The run contains 231 exact rational scalar pairs, 48 complex positive
fixed-center pairs, two explicit fixed-center attainers, and 40 sharp-pair
families with 80 rank-two and 80 rank-one compressions. It also checks the
singular-remainder and normalized compression steps in Section 3, the
spectral circle, and the score-three Schmidt-rank-two attainer. The
largest fixed-center marginal residual is below `7.78e-15`; the singular
remainder norm exceeds m by at most `4.45e-15` in floating arithmetic.
The configured tolerance is `3e-10`. These finite checks are not an
optimization, an interval certificate, or external review.

The operational model remains one arbitrary unknown quantum specimen,
one delayed local X/Z query, collective encoding, unrestricted classical
records, and worst-case bounded retained quantum dimension. The memory
subspace and reference purifications used above are mathematical proof
devices. No extra specimen, memory, entanglement, physical reaccess,
sequential query, or postselected success condition is introduced.
