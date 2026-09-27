# A complete converse for two query pairs coupled by a controlled phase

Research base: `7cb964b47b8aa13a604a3ab5df663d4f399fa6f4` (PR #49).
Date: 27 September 2026.
**Status:** supplied analytical theorem, independently reconstructed within
this workspace. This is internal review, not external peer review or a
claim of publication priority.

## 1. The readout family and sharp bound

Let memory Q=A tensor B consist of two qubits. Choose a,b,c,d>=0 with

$$
a^2+b^2=c^2+d^2=2
$$

and any real phase theta. Put

$$
W_\theta=\cos\theta\,X_B+\sin\theta\,Z_AY_B.
$$

The two summands anticommute, so W_theta is a Hermitian reflection.
Equivalently,

$$
W_\theta=e^{-i\theta Z_AZ_B/2}X_B e^{i\theta Z_AZ_B/2}.
$$

The family therefore starts with queries on separate memory qubits and
conjugates the second query algebra by a controlled-phase interaction.
The original readout pairs may have independent, nonorthogonal angles.
Consider the original readout pairs

$$
B_1=(aZ_A+bX_A)/\sqrt2,\qquad
D_1=(aZ_A-bX_A)/\sqrt2,
$$

$$
B_2=(cZ_B+dW_\theta)/\sqrt2,\qquad
D_2=(cZ_B-dW_\theta)/\sqrt2.
\qquad\text{(1)}
$$

They are reflections because Z_A anticommutes with X_A, and Z_B
anticommutes with W_theta. The two Jordan blocks at each site have the
same angle, but the angles at the two sites can differ arbitrarily.
All zero coefficients and all phases are included. Common memory-unitary
conjugates obey the same conclusion.

**Theorem.** For every third pair of Hermitian contractions B3,D3,

$$
\boxed{\left\|\sum_{i=1}^3(X_i\otimes B_i+Z_i\otimes D_i)\right\|
\le4+\sqrt2.}
\qquad\text{(2)}
$$

The constant is attained at a=b=c=d=1, theta=0, B3=D3=I.
This is a complete continuous family theorem, not an assertion for every
ququart reflection pair. No cross commutation of the two query algebras
or preservation of their symmetries by the third pair is assumed.

For the proof, use bisector reference coordinates
Z_i=(X_i^old+Z_i^old)/sqrt(2), X_i=(X_i^old-Z_i^old)/sqrt(2) for i=1,2.
Then the earlier Hamiltonian is

$$
H_0=aZ_1Z_A+bX_1X_A+cZ_2Z_B+dX_2W_\theta.
\qquad\text{(3)}
$$

Signs of a,b,c,d can be absorbed by independent reference-axis sign
changes; in the original coordinates these are signed exchanges of the
two readouts. Thus nonnegative coefficients do not exclude a distinct
sign case. The phase theta remains unrestricted.

Write r=sqrt(2), k=2+r, Lambda=4+r. Since ||h3||<=2, U:=||H0||<=k is
immediately safe. Also U<=a+b+c+d<=4. We henceforth assume U>k.

## 2. Four copying sectors and the exact spectrum

The two parities Z1 Z_A and Z2 Z_B commute with H0 and with each other.
Each joint parity sector (alpha,beta) has dimension four. Identify it
with Q by the copying isometry

$$
J_{\alpha\beta}|ab\rangle_Q
=|a\mathbin\oplus e_\alpha,b\mathbin\oplus e_\beta\rangle_R
 |ab\rangle_Q,
\qquad e_+=0,\quad e_-=1.
$$

On that sector the Hamiltonian is

$$
J_{\alpha\beta}^\dagger H_0J_{\alpha\beta}
=(\alpha a+\beta c)I+F,
\qquad F=bX_A+dW_\theta.
\qquad\text{(4)}
$$

The square-loop hopping operator F obeys

$$
F^2=(b^2+d^2)I+2bd\cos\theta\,X_AX_B.
$$

It commutes with K=X_A X_B and anticommutes with Z_A Z_B. On either
two-dimensional K sector it is traceless, so its spectrum is

$$
\{q,p,-p,-q\},\qquad
q=\sqrt{b^2+d^2+2bd|\cos\theta|},\quad
p=\sqrt{b^2+d^2-2bd|\cos\theta|}.
$$

Set

$$
A=a+c,\quad D=|a-c|,\quad v=D+q.
$$

The top two energies and the main scalar identity are

$$
\boxed{U=A+q,\qquad m=\max\{A+p,D+q\},\qquad
A^2+D^2+p^2+q^2=8.}
\qquad\text{(5)}
$$

The U>k assumption implies a,c>0. Indeed, if c=0, then d=r and
U<=a+b+d<=2+r; the a=0 case is identical. Thus the top eigenspace lies
entirely in the (+,+) copying sector. It has dimension one when q>p,
and dimension two when q=p. The latter case will be covered by the
two-mode argument below. The case q=0 cannot occur when U>k.

### 2.1. A simple top vector has exactly flat memory marginal

When q>p, its eigenvector in the (+,+) sector is the unique positive-q
eigenvector of F. Within either K sector use the two basis vectors
(|00>+epsilon|11>)/sqrt(2) and
(|01>+epsilon|10>)/sqrt(2). Anticommutation with Z_A Z_B makes F
off diagonal in this basis. A nonzero eigenvector therefore has equal
magnitudes on these two vectors, hence magnitude 1/2 on each memory
computational basis vector. Copying and tracing the references yields

$$
\boxed{\rho_Q=I_4/4.}
\qquad\text{(6)}
$$

This is valid for either sign of cos(theta), with the corresponding K
sector selected. It makes no real-vector assumption.

## 3. A flat top vector settles the first two spectral cases

For a flat ququart marginal, the
[exact last-query theorem](EXACT_LAST_QUERY_RESOLVENT.md#1-the-readout-elimination-theorem) gives

$$
F_{\rm flat}(t)=
\max\left\{\frac1{t-r},\frac{t^2-2}{t(t^2-4)}\right\},\qquad t>2.
\qquad\text{(7)}
$$

This also follows directly from its scalar pair formula: equal active
weights maximize the block-resolvent trace at a=b=1, while scalar blocks
give 1/(t-r). The [rank-one spectral envelope](EXACT_LAST_QUERY_RESOLVENT.md#6-exact-test-for-a-rank-one-spectral-upper-bound) is sufficient exactly when

$$
(U-m)F_{\rm flat}(\Lambda-m)\le1.
\qquad\text{(8)}
$$

### 3.1. The second eigenvalue is at most three

If m<=3, the top is simple since U>k>3. Put t=Lambda-m>=1+r. On this
range the second branch in (7) is no larger than the first. Indeed this
comparison is equivalent to t^2-r t-2>=0, and at t=1+r its left side
is r-1>0 and then increases. Therefore

$$
(U-m)F_{\rm flat}(\Lambda-m)
=\frac{U-m}{4-m}\le1
$$

because U<=4. This proves (2) in this case.

### 3.2. The second eigenvalue comes from another parity sector

Suppose m>3 and m=v=D+q. Let w=min(a,c), so U-m=2w. Relabel the two
coefficient pairs in the following scalar estimate if needed, so w=c.
Then

$$
m=a-c+q\le a+b+d-c\le2+\sqrt{2-w^2}-w.
$$

Consequently

$$
\gamma:=k-m\ge r-\sqrt{2-w^2}+w\ge w>0.
\qquad\text{(9)}
$$

The top is simple in this case. A tie A+p=D+q with m>3 is impossible:
the two sums would imply A^2+p^2+D^2+q^2>=m^2>9, contradicting (5).
Thus (6) applies. The rank-one parameter t=2+gamma satisfies
0<gamma<r-1 and 2<t<1+r. Each branch of (7) obeys

$$
\frac{2\gamma}{t-r}<1,
\qquad
2\gamma\frac{t^2-2}{t(t^2-4)}
=\frac{2(t^2-2)}{t(t+2)}<1.
$$

For the first use gamma<r-1<2-r, following from 2r<3. For the second
use t^2-2t-4<0 on 2<t<1+r<1+sqrt(5). Since U-m=2w<=2gamma,
(8) follows strictly.

## 4. The remaining two leading modes have a classical channel

It remains that m=A+p>3. The two selected leading eigenvectors lie in
the same (+,+) copying sector, including the degeneracy q=p. For any
isometry V onto their span, tracing out the reference copy makes

$$
\Phi(\omega)=\mathrm{Tr}_R(V\omega V^\dagger)
$$

diagonal in the memory computational basis for every input omega.
Thus the actual head channel is measure and prepare, hence entanglement
breaking. No coherences of the actual channel have been discarded.

The third energy is

$$
\ell=\max\{A-p,D+q\}.
\qquad\text{(10)}
$$

The identity (5) gives useful coarse bounds with no phase dependence:

$$
\boxed{0\le\ell<\sqrt7<3,\qquad U+\ell<6,\qquad U<79/20.}
\qquad\text{(11)}
$$

For the first, both candidate tails have squared value at most 16-m^2:
(A-p)^2=2(A^2+p^2)-m^2<=16-m^2 and
(D+q)^2<=2(D^2+q^2)<=16-m^2. Since m>3, the claim follows. In particular
v<3<m, so the two-mode head is isolated even at q=p; p=0 would force
m=A<=2sqrt(2)<3 and is excluded.

For the second, put A=m/2+x and p=m/2-x. Then
2x^2+D^2+q^2=8-m^2/2. The two possibilities for U+ell are
m/2+3x+q and m/2+x+D+2q. Weighted Cauchy--Schwarz gives the same bound
for both:

$$
U+\ell\le\frac{m+\sqrt{11(16-m^2)}}2
<\frac{3+\sqrt{77}}2<6.
$$

The middle function decreases for m>=3, and sqrt(77)<9. Finally
U+m=2A+p+q<=sqrt(6)sqrt(A^2+p^2+q^2)<=4sqrt(3), recovering the
[sharp support bound](SHARP_TWO_MODE_SUPPORT.md) directly in this family. Hence
U<4sqrt(3)-3<79/20; the last comparison follows from
3*80^2<139^2.

### 4.1. Two quadratic endpoint checks complete the converse

Use the actual-tail envelope

$$
H_0\le\ell I+V\mathrm{diag}(U-\ell,m-\ell)V^\dagger.
$$

Since its actual head is EB, the
[exact pure-memory last-query bound](EXACT_LAST_QUERY_RESOLVENT.md#1-the-readout-elimination-theorem) and
the [positive-update criterion](TWO_MODE_RESOLVENT.md#4-exact-four-by-four-schur-condition) show that it suffices to prove

$$
(U-\ell)F_{\rm pure}(\Lambda-\ell)<1,
\qquad
F_{\rm pure}(t)=
\begin{cases}
[2(\sqrt{2t^2-4}-t)]^{-1},&2<t\le3r,\\
(t-r)^{-1},&t\ge3r.
\end{cases}
\qquad\text{(12)}
$$

Here t=Lambda-ell>Lambda-3=1+r>2. If t>=3r, (12) follows from U<4.
Otherwise, its positive quantities can be squared, and the condition is
equivalent to

$$
Q(U,\ell):=U^2+4\Lambda U-4\Lambda^2+16
+(4\Lambda-6U)\ell+\ell^2<0.
$$

The pre-squaring left side U+2Lambda-3ell is positive by U>k and ell<3.
The polynomial Q increases in U throughout this range. Use
U<=min{79/20,6-ell} from (11).

For 0<=ell<=41/20, Q(79/20,ell) is convex in ell, so its maximum occurs
at an endpoint. Both endpoints are strictly negative:

$$
Q(79/20,0)=\frac{9121}{400}-\frac{81}{5}r<0,
\qquad
Q(79/20,41/20)=\frac{561}{50}-8r<0.
$$

The common rational witness r>141/100 follows from 141^2<2*100^2.
For 41/20<=ell<sqrt(7),

$$
Q(6-\ell,\ell)=8\ell^2-48\ell+76-8r
$$

decreases because ell<3. Its largest value is the same already negative
endpoint Q(79/20,41/20). This proves (12), hence the strict norm bound
below Lambda in the remaining case. Reference chirality changes H0+h3
to its negative, so the upper spectral bound is the operator-norm bound.

The three cases cover every phase, unequal coefficient angles, endpoints,
and leading degeneracies in (1). They prove the complete theorem (2).

## 5. Scope

The proof uses the actual copying-sector channel, not an assumption that
every real or every ququart two-mode channel is classical. Rank-one
envelopes are used only in the two ranges where the scalar argument
certifies them; two positive modes are retained in the remaining range.
Indeed a one-mode envelope can fail within this family near m=k, despite
the top vector having flat memory marginal.

The third binary-POVM pair is arbitrary, including complex matrices and
two active Jordan blocks. This theorem does not close any entire remaining
reflection signature or prove the unrestricted interface converse. Its
scalar inequalities are analytical; no parameter grid is a proof step.


## 6. Verification and model scope

Independent internal reconstructions checked the full spectrum, the flat
leading vector, every degeneracy and endpoint case, the actual copying
channel, the three scalar branches, and sharp attainment. Reproduce the
[targeted diagnostics](../../tools/check_direct_resolvent_and_channel.py)
with

```bash
python tools/check_direct_resolvent_and_channel.py --output results/direct_resolvent_and_channel.json
```

The [recorded result](../../results/direct_resolvent_and_channel.json)
supplements the proof with exact scalar comparisons and fixed matrix
identities. It does not certify the theorem by parameter sampling or
establish publication novelty. Reproduction details are recorded in
[reproducibility](../REPRODUCIBILITY.md).

The model remains one arbitrary unknown specimen, one delayed local X/Z
query, unrestricted collective encoding, unlimited classical side
information, and worst-case retained quantum dimension. The copying
sectors are virtual eigenspaces used in the proof; they do not copy the
physical input or supply additional memory. The controlled-phase condition
is an explicit readout-family hypothesis, not an extra restriction silently
imposed on the unrestricted interface problem.
