# Balanced-spectrum rigidity and an all-input near-flat converse

Research base: `8e38f704b1d8e74344c87ee83748d1f4dc45fcaf` (PR #56).
Status: supplied analytical deductions, independently reconstructed internally.
No publication-originality claim is made.

The [balanced-spectrum theorem](BALANCED_SPECTRUM_OPTIMALITY.md) evaluated
every flat half-rank seed at every input size. This continuation gives a
uniform neighborhood in which the same retention bound holds for arbitrary
nonzero spectra and arbitrary supports. It also quantifies how a balanced
seed whose score is close to optimal must approach an original-site
bisector state. The unrestricted half-rank converse outside this
neighborhood, other intermediate memory budgets and the general entropy
conjecture remain unresolved.

## 1. An explicit spectral neighborhood at every input size

Let n>=1, d=2^n, k=d/2 and K_n=2n-2+sqrt(2). For a density matrix rho
of rank at most k, define

$$
\eta^2=2\left(1-\frac{\operatorname{Tr}\sqrt\rho}{\sqrt k}\right).
\tag{1}
$$

**Theorem.** If

$$
\boxed{\eta\le\frac1{4096n},}
\tag{2}
$$

then the original query score obeys

$$
\boxed{g(\rho):=\sum_{i,U=X,Z}\|\sqrt\rho U_i\sqrt\rho\|_1
\le K_n.}
\tag{3}
$$

Equality holds exactly for a pure original-site X/Z bisector tensored
with the maximally mixed state of the other n-1 sites.

The hypothesis is purely spectral. Equivalently,
Tr(sqrt(rho))/sqrt(k)>=1-1/(2^25 n^2). If P is any rank-k projector
containing supp(rho), then

$$
\eta=\|\sqrt\rho-P/\sqrt k\|_2.
\tag{4}
$$

Thus eta measures distance from a flat half-rank root and is independent
of the choice of completion when rank(rho)<k. No local basis, support
orientation or decoder condition is imposed. The radius has inverse
linear dependence on n; there is no additional factor 2^n. Its constant
is conservative and is not asserted optimal.

The proof combines quantitative balanced-spectrum rigidity with a
nonflat dominant-site lemma. Both ingredients are supplied below.

## 2. Quantitative rigidity of the balanced response

Let R be a traceless Hermitian unitary, tau=Tr/d, and use

$$
q_U=\frac14\tau([R,U]^*[R,U]),\qquad
\mathcal R_z(R)=\sum_U\sqrt{1-zq_U},
$$

$$
\epsilon_z=2n-2+2\sqrt{1-z/2}-\mathcal R_z(R),\qquad 0<z\le1.
\tag{5}
$$

Expand R in Pauli words and write
W=sum_i(r_{X_i}^2+r_{Z_i}^2), b=max_i(r_{X_i}^2+r_{Z_i}^2).
When W>0 put A=b/W. The balanced-spectrum theorem proves epsilon_z>=0.
Its proof gives the stronger estimates

$$
\boxed{\epsilon_z\ge\frac z{128}(1-b),}
\tag{6}
$$

and, for a site attaining b, with singleton coefficients u,v,

$$
\epsilon_z\ge\frac{z^2}{16}(u^2-v^2)^2.
\tag{7}
$$

To prove (6), retain r=sqrt(2)-1 and c=2-sqrt(2). In the diffuse
case W=0 or A<=3/4, the preceding theorem gives W<81/100. Its linear
deficit estimate therefore gives

$$
\epsilon_z>z\left(\sqrt2-\frac{281}{200}\right)
>\frac z{128}\ge\frac z{128}(1-b).
\tag{8}
$$

For the second strict inequality, sqrt(2)>1413/1000 and 1/125>1/128
suffice. In the dominant case A>=3/4, set x=1-A and a=81/256. The
fourth-moment tail bound from the preceding note yields

$$
m^2\le1-x+x\left(\frac{2ax}{A}+\frac{a^2x^3}{A^3}\right)
\le1-\kappa x,\qquad
\kappa=1-\frac{2a}{3}-\frac{a^2}{27}
=\frac{51469}{65536}\ge\frac{25}{32}.
\tag{9}
$$

Here m is the normalized Rademacher first moment and W<=m^2, as in
the preceding proof. Put delta=1-W. Then delta>=kappa x, and

$$
\begin{aligned}
c-W+rb&=c\delta-rWx\ge(c-r/\kappa)\delta\\
&\ge\frac{c\kappa-r}{1+\kappa}(1-b)
\ge\frac5{256}(1-b).
\end{aligned}
\tag{10}
$$

For the middle step, 1-b=delta+Wx<=delta+x<=delta(1+1/kappa).
The last step uses r<5/12, c>7/12, kappa>=25/32 and kappa<=1.
The dominant grouped bound in the preceding theorem gives
epsilon_z>=z(c-W+rb)/2, which proves (6).

For (7), put f_z(x)=1-sqrt(1-zx). Its second derivative is at least
z^2/4 on the interior of [0,1]; the corresponding strong-convexity
inequality extends to the endpoints by continuity. Therefore

$$
J_z:=f_z(u^2)+f_z(v^2)-2f_z(b/2)
\ge\frac{z^2}{16}(u^2-v^2)^2.
$$

The proof of the grouped bound gives

$$
\epsilon_z-J_z
\ge\frac z2(2-W-b)+2f_z(b/2)-2f_z(1/2)\ge0.
\tag{11}
$$

The final inequality is the established dominant gate when A>=3/4.
In the diffuse case, 2f_z(b/2)>=zb/2 makes its first two terms at
least z(2-W)/2, already greater than 2f_z(1/2). Thus subtracting J_z
is justified in both branches, including W=0. This proves (7).

Choose the signed original-site bisector B at this maximizing site,
aligning the signs of u and v. Then

$$
\boxed{\tau((R-B)^2)\le\frac{512\epsilon_z}{z^2}.}
\tag{12}
$$

Indeed, its overlap with R is ell=(|u|+|v|)/sqrt(2). If b>=1/2,
the inequality 1-ell<=1-ell^2 gives

$$
\begin{aligned}
\tau((R-B)^2)&=2(1-\ell)
\le2(1-b)+(|u|-|v|)^2\\
&\le2(1-b)+2(u^2-v^2)^2
\le\frac{288\epsilon_z}{z^2}.
\end{aligned}
$$

If b<1/2, (6) gives epsilon_z>z/256, while the squared distance is
at most two. This proves (12). The chosen site and aligned signs do
not depend on z.

## 3. Original-score and affinity distances

For 0<t<=1 let rho_t=(I+tR)/d, and define its gaps from the established
balanced-spectrum optima. Here the root-affinity score is

$$
\mathcal A(\rho)=\sum_U
\sqrt{\operatorname{Tr}(\sqrt\rho U\sqrt\rho U)}.
$$

Put

$$
e_g=2n-2+2\sqrt{1-t^2/2}-g(\rho_t),
$$

$$
e_{\mathcal A}=2n-2+\sqrt{2+2\sqrt{1-t^2}}-\mathcal A(\rho_t).
$$

The preceding theorem proves
epsilon_{t^2}<=e_g and epsilon_{1-sqrt(1-t^2)}=e_A. For the same
signed bisector B chosen above, put rho_{t,B}=(I+tB)/d. Normalized
Schatten Cauchy gives
||rho_t-rho_{t,B}||_1=t tau(|R-B|)<=t sqrt(tau((R-B)^2)). Hence

$$
\boxed{\|\rho_t-\rho_{t,B}\|_1
\le\frac{16\sqrt2}{t}\sqrt{e_g},}
\tag{13}
$$

$$
\|\rho_t-\rho_{t,B}\|_1
\le\frac{16\sqrt2(1+\sqrt{1-t^2})}{t}\sqrt{e_{\mathcal A}}.
\tag{14}
$$

These are full trace norms. The convention of trace distance with a
factor 1/2 halves the right sides. At t=0 the state is already maximally
mixed; its parametrizing reflection R requires no rigidity conclusion.

At t=1, a flat half-rank seed whose original score is epsilon below
K_n is within full trace norm 16sqrt(2epsilon) of a retention seed.
The same conclusion holds using its root-affinity score gap. The
constants are independent of input size.

## 4. A nonflat dominant-site converse

The following lemma retains the seed spectrum and holds for every n.
It supplies the bridge from the preceding flat result to (2).

Let S>=0, Tr(S^2)=1, rank(S)<=k. Expand S in the orthonormal basis
sigma_p/sqrt(d), let b_i be the lengths of its local X/Z coefficient
pairs, and put T=sum_i b_i^2. If T>0 and

$$
A:=\frac{\max_i b_i^2}{T}\ge\frac34,
\tag{15}
$$

then

$$
\mathcal A(S^2)\le K_n.
\tag{16}
$$

Equality is exactly a retention seed. This is a sufficient local
coefficient condition, not a hypothesis imposed on the main theorem.

For a self-contained proof, write
u=Tr(S)/sqrt(k), v=sqrt(1-u^2), y=2T and
m=E|sum_i(b_i/sqrt(T))epsilon_i|. The singleton part L of S has a
symmetric spectrum. Its top k eigenvalues have mean
sqrt(T)m/sqrt(d) and centered squared sum T(1-m^2)/2. Applying
Hermitian trace rearrangement and centered Cauchy to the k eigenvalues
of S, padded by zeros, gives

$$
\sqrt y\le um+v\sqrt{1-m^2}.
\tag{17}
$$

In particular y<=1. If d_U=1-Tr(SUSU), the Pauli energy decomposition
gives, for a site attaining the maximum in (15),

$$
D:=\sum_Ud_U\ge4-2u^2-y,\qquad
d_{X_i}+d_{Z_i}\ge yA.
$$

The zero-singleton case T=0 is also strictly below retention: the same
Pauli energy bound gives D>=4-2u^2>=2, so its affinity score is at most
sqrt(2n(2n-2))<K_n. Consequently any half-rank seed
that exceeds retention must have T>0 and A<3/4.

Write w=d_{X_i}+d_{Z_i}. Cauchy for the selected pair, followed by
the square-root tangent at w=1, gives
sqrt(1-d_{X_i})+sqrt(1-d_{Z_i})<=sqrt(2(2-w))
<=sqrt(2)+(1-w)/sqrt(2). Applying the tangent at zero deficit to
each remaining query bounds their sum by 2n-2-(D-w)/2. Combining
these inequalities and the preceding bounds on D,w gives, with
r=sqrt(2)-1 and c=1-r,

$$
\mathcal A(S^2)
\le K_n+\frac{2u^2+(1-rA)y-(2+c)}2.
\tag{18}
$$

When n=1 the complementary group is empty and contributes zero;
the same pair tangent applies.

By (17), the expression 2u^2+(1-rA)y is at most the largest eigenvalue
of the two-by-two matrix

$$
\begin{pmatrix}2&0\\0&0\end{pmatrix}
+(1-rA)
\begin{pmatrix}m\\\sqrt{1-m^2}\end{pmatrix}
\begin{pmatrix}m&\sqrt{1-m^2}\end{pmatrix}.
$$

Its largest eigenvalue is at most 2+c whenever

$$
m^2\le\Psi(A):=
\frac{c(2-r+rA)}{2(1-rA)}.
\tag{19}
$$

Indeed, subtracting the matrix from (2+c)I gives positive trace and
determinant c(2+c)-(1-rA)(c+2m^2). It remains to verify (19) on
[3/4,1]. The fourth-moment tail bound gives, with x=1-A in [0,1/4],

$$
m^2\le1-x+\frac{27}{32}x^2+\frac{243}{1024}x^4,
\qquad
\Psi(1-x)=\frac{1-rx/2}{1+x/\sqrt2}.
$$

The difference between the latter expression and the former bound
is x f(x), where

$$
f(x)=1-\frac{\sqrt2-1/2}{1+x/\sqrt2}
-\frac{27}{32}x-\frac{243}{1024}x^3.
$$

This function is strictly concave on [0,1/4], since

$$
f''(x)=-\frac{\sqrt2-1/2}{(1+x/\sqrt2)^3}
-\frac{1458}{1024}x<0.
$$

Both endpoint values are positive:

$$
f(0)=\frac32-\sqrt2>0,\qquad
f(1/4)=\frac{51469}{65536}-\frac{34\sqrt2-24}{31}>0.
$$

For the last comparison, sqrt(2)<99/70 makes the second term less
than 843/1085, and
51469*1085-843*65536=597017>0. Thus (19) is strict for A<1.
At A=1, m=1 and (17) gives y<=u^2. Equality in (18) therefore
requires u=y=1. The identity and one site's X/Z coefficients exhaust
Tr(S^2)=1, so S=(I+B_i)/sqrt(2d). Equality in the selected-pair
tangent requires the two coefficient magnitudes to agree. This proves
(16), including its equality statement. The established fidelity--affinity
comparison transfers it to g(S^2).

## 5. Proof of the spectral neighborhood theorem

Choose any rank-k projector P containing supp(rho), put sigma=P/k,
S=sqrt(rho), S_0=P/sqrt(k), and let
epsilon=K_n-g(sigma). The flat half-rank theorem gives epsilon>=0.
The identity (4) follows directly by taking the Hilbert--Schmidt
inner product of S and S_0.

If epsilon>1/1024, trace-norm continuity gives

$$
g(\rho)\le g(\sigma)+4n\eta<K_n,
$$

because 4n eta<=1/1024. For each query this continuity bound follows
by expanding SUS-S_0US_0 into two terms and applying Schatten Holder;
each normalized root has Hilbert--Schmidt norm one.

Otherwise epsilon<=1/1024. For R=2P-I, (6) at z=1 gives
b_R>=1-128epsilon>=7/8. The local coefficient pairs of S_0 are those
of R divided by sqrt(2). Orthogonal projection onto Pauli coefficients
does not increase Hilbert--Schmidt distance. At a site attaining b_R,
the coefficient-pair length for S is therefore at least
sqrt(7)/4-eta; its total singleton coefficient norm is at most
1/sqrt(2)+eta. Since eta<=1/(4096n)<1/100,

$$
\sqrt7/4-\eta>\frac{13}{20},\qquad
1/\sqrt2+\eta<\frac{18}{25},\qquad
\left(\frac{13/20}{18/25}\right)^2
=\left(\frac{65}{72}\right)^2>\frac34.
$$

Thus S satisfies (15), and the nonflat dominant-site lemma proves
g(rho)<=K_n. Its equality classification gives exactly the family
stated in Section 1. This completes the proof for rank(rho)<=k,
including rank-deficient seeds and n=1.

## 6. Necessary dependence on the score gap and spectral bias

The constants above are not sharp, but the square-root dependence on
the score gap cannot be improved uniformly. Already at n=1,t=1, let
B=(X+Z)/sqrt(2), C=(X-Z)/sqrt(2) and
R_theta=cos(theta)B+sin(theta)C for 0<theta<pi/4. The nearest bisector
is B, and

$$
g(\rho_\theta)=\sqrt2\cos\theta,\qquad
\|\rho_\theta-\rho_B\|_1^2
=2(1-\cos\theta)=\sqrt2\,e_g.
\tag{20}
$$

The factor 1/t in (13) is also necessary in its order as t tends to
zero. Take R=X at one qubit. Then the distance to the nearest balanced
bisector state is t sqrt(2-sqrt(2)), whereas, putting v=sqrt(1-t^2),

$$
e_g=2\sqrt{1-t^2/2}-1-\sqrt{1-t^2}
=\frac{(1-v)^2}{2\sqrt{(1+v^2)/2}+1+v}
=\frac{t^4}{16}+O(t^6).
\tag{21}
$$

Thus a bound proportional to sqrt(e_g) with a constant independent of
t is impossible, and any uniform prefactor must grow at least as 1/t.
These examples respect the established one-qubit optimum; they test
stability scaling, not optimality violations.

## 7. Scope and verification status

Dimension-independent rigidity toward a single-qubit observable has
established precedents. Montanaro--Osborne,
[arXiv:0810.2435v5](https://arxiv.org/pdf/0810.2435v5), Section 9.3,
Theorem 60, printed p. 32 (Theorem 9.7 in the published numbering),
give a quantum Friedgut--Kalai--Naor theorem. Blecher--Gao--Xu,
*Geometric influences on quantum Boolean cubes*, give an alternative
proof in [arXiv:2409.00224v1](https://arxiv.org/pdf/2409.00224v1),
Section 6, Theorem 6.2, printed pp. 34--35. These results turn small
Fourier mass above degree one into squared normalized Hilbert--Schmidt
closeness of the same order to a single-qubit observable or a constant.
Here the hypothesis is an original-query score gap, and the conclusion
also fixes the local X/Z bisector orientation. For example, R=X_i has
zero Fourier mass above degree one but squared distance 2-sqrt(2) from
the nearest bisector. The cited Fourier rigidity theorems therefore
do not supply that orientation conclusion on their own. No new general
quantum rigidity principle or exhaustive priority audit is asserted.

The argument uses the supplied balanced-spectrum theorem, Pauli
orthogonality, an elementary fourth-moment tail bound, a two-by-two
spectral estimate and trace-norm continuity. The centered rank constraint
in (17) is the same one used in the earlier
[finite-input half-rank converse](HALF_RANK_RETENTION_CONVERSE.md),
but (19) handles arbitrarily many small singleton coefficients.
The proof above includes the needed scalar estimate and does not
assume a finite sign-pattern classification.

The near-flat hypothesis is a sufficient spectral condition, not a
restriction on the operational encoding model. The one-specimen input,
worst-case quantum dimension, unrestricted finite classical record and
uniform delayed-query requirements remain those of the project.
The general nonflat half-rank optimum outside (2) remains unresolved.
The proof and its equality statements were independently reconstructed
within this workspace; this is not external peer review.

The [checker](../../tools/check_balanced_spectrum_stability.py) verifies
the exact rational comparisons and fixed matrix instances of the
rigidity, dominant-site and spectral-neighborhood conclusions:

```sh
python tools/check_balanced_spectrum_stability.py --output results/balanced_spectrum_stability.json
```

The [result record](../../results/balanced_spectrum_stability.json)
pins the proof-note and checker hashes. Matrices have dimension at most
32. These bounded diagnostics do not replace the quantified proofs;
no grid, random sampling or optimizer is used to establish the claims.
