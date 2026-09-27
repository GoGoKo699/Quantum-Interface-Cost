# The unrestricted four-input, two-qubit retention converse

Research base: `c8b2e88d6721cb9208c797788f334d7f8b1e1848` (PR #52).
Status: supplied analytical proof with an exact rational polynomial
certificate, independently reconstructed within this workspace. This
internal mathematical review is not external peer review or a
publication-priority assessment.

For every positive S on four qubits with rank at most four and
Tr(S^2)=1,

$$
\boxed{\sum_{A=X_1,Z_1,\ldots,X_4,Z_4}
\sqrt{\operatorname{Tr}(SASA)}\le4+2\sqrt2.}
\tag{1}
$$

Consequently the original unrestricted interface problem has

$$
\boxed{\Gamma(4,4)=4+2\sqrt2,\qquad
\eta_{4,4}=\frac{2+\sqrt2}{4},\qquad
\epsilon_{4,4}=\frac{2-\sqrt2}{8}.}
\tag{2}
$$

Every maximizing normalized seed is, up to a permutation of the original
sites,

$$
\rho=S^2=|\beta_1\rangle\langle\beta_1|\otimes
|\beta_2\rangle\langle\beta_2|\otimes\frac{I_4}{4},
\tag{3}
$$

where both pure states are X/Z bisectors. Output isometries remain free;
this does not classify all physical instruments. The model permits
arbitrary collective encoders and classical records of unrestricted finite
size, with worst-case quantum dimension four. No flat-spectrum or readout
algebra assumption is imposed.

The [quarter-rank geometry](QUARTER_RANK_GEOMETRY.md) supplies the exact
singleton spectrum and two local block estimates. The new proof combines
that geometry with curvature of the square root. A short sum of squares
handles one spectral branch; one polynomial certificate handles the other.

## 1. Geometry and the necessary high-score region

Expand S in the orthonormal Pauli basis sigma/4. Orient its singleton
coefficient in each local X/Z plane and order the four lengths as

$$
a\ge b\ge c\ge d\ge0,\quad
T=a^2+b^2+c^2+d^2,\quad y=2T,\quad
u=\frac{\operatorname{Tr}S}{2},\quad v=\sqrt{1-u^2}.
$$

For the original eight queries set

$$
a_A=\operatorname{Tr}(SASA),\qquad
W_i=2-a_{X_i}-a_{Z_i},\qquad D=\sum_iW_i.
$$

Each a_A lies in [0,1]. The established top-quarter spectrum gives, with
R=max{b,(b+c+d)/2},

$$
y\le u(a+R)+v\sqrt{T-a^2-R^2},\qquad
y\le\frac{1+u^2}{2},\qquad
D\ge4-u^2-y.
\tag{4}
$$

In particular sum_A a_A<=9/2+3u^2/2. To prove (1), it suffices to
consider a seed whose root-affinity sum is at least 4+2sqrt(2).
Cauchy--Schwarz then forces

$$
u^2\ge\alpha:=\frac{4\sqrt2-3}{3},\qquad
\delta:=v^2+1-y\le r^2,\qquad r=\sqrt2-1.
\tag{5}
$$

Thus u>15/16, y>=2r+v^2, and rank(S)=4. The first strict comparison
uses sqrt(2)>1443/1024, certified by
2(1024)^2-(1443)^2=14903>0. Positivity gives every singleton length
at most u/2.

Write kappa=||S||. Centering the four eigenvalues of S gives

$$
\kappa\le\frac{u+\sqrt3v}{2}.
$$

The local block inequality from the preceding note therefore gives

$$
W_i\ge1-(u+\sqrt3v)(u-2b_i),
\quad (b_1,b_2,b_3,b_4)=(a,b,c,d).
\tag{6}
$$

## 2. The pair-dominant branch: a sum of squares

Suppose b>=c+d. Put p=a+b, Q=c^2+d^2 and w=u-p>=0. Equation (4)
and elementary Cauchy give

$$
y\le up+v\sqrt Q,\qquad
p^2+2Q\le y,\qquad Q\le y(1-y)\le1-y.
\tag{7}
$$

For the last inequality, square the first by uncentered Cauchy to obtain
y^2<=p^2+Q<=y-Q. Let W=W_1+W_2 and define

$$
x=2(u+\sqrt3v)w.
$$

Equations (4) and (6) give D>=2+delta and W>=2-x. With z=sqrt(1-y),

$$
uw\le z^2-v^2+vz\le\frac98(v^2+z^2)=\frac98\delta.
$$

The last difference, multiplied by eight, is
(z-4v)^2+v^2>=0. Since delta<=r^2<3/16 and u>15/16, it follows that
w<9/40 and x<9/10, using u+sqrt(3)v<=2. Hence

$$
2-x>\frac{11}{10}>\frac{35}{32}>\frac{2+\delta}{2}.
$$

Group the four queries on sites 1,2 and the other four. Cauchy gives
2sqrt(4-W)+2sqrt(4-D+W). First lower D to 2+delta; the expression
increases. At that value it decreases with W throughout W>=2-x by
the preceding strict inequality. Therefore

$$
\sum_A\sqrt{a_A}\le2\sqrt{2+x}+2\sqrt{4-\delta-x}.
\tag{8}
$$

The coupled inequalities (7) also imply

$$
y\le up+\frac{v^2}{4}
 +\frac v4\sqrt{v^2+8p(u-p)}.
$$

Indeed, if y>up, square y-up<=v sqrt((y-p^2)/2) and take the upper
quadratic root; if y<=up the displayed bound is automatic. Substituting
p=u-w and writing h=sqrt(uw) gives

$$
\delta\ge\frac74v^2+uw-
\frac v4\sqrt{v^2+8uw-8w^2}
\ge\frac32v^2+h^2-\frac{vh}{\sqrt2}.
\tag{9}
$$

The second inequality uses sqrt(v^2+8uw-8w^2)<=v+2sqrt(2)h.
The exact condition for the right side of (8) to be at most 4+2sqrt(2)
is delta>=H(x), where

$$
\begin{aligned}
H(x)&=2(2+\sqrt2)(\sqrt{2+x}-\sqrt2)-2x\\
&=rx-\frac{(1+\sqrt2)x^2}{(\sqrt{2+x}+\sqrt2)^2}
\le rx-\frac6{25}x^2.
\end{aligned}
\tag{10}
$$

All squaring is legitimate because 2+sqrt(2)-sqrt(2+x)>0. For the last
bound, x<=1 gives a denominator at most 5+2sqrt(6)<10, while
1+sqrt(2)>12/5. Also

$$
r^2>\frac16,\qquad \frac{2\sqrt3r}{u}<\frac85,
\qquad x=2(1+\sqrt3v/u)h^2\ge2h^2.
$$

Here r^2>1/6 follows from sqrt(2)<17/12; and
2sqrt(3)r/u<(32/15)sqrt(3)r<8/5 follows from r^2<3/16.
Consequently (9) proves

$$
\begin{aligned}
\delta-rx+\frac6{25}x^2
&\ge\frac32v^2-\frac{vh}{\sqrt2}
 +\frac16h^2-\frac85vh^2+\frac{24}{25}h^4\\
&=\frac32\left(v-\frac{h}{3\sqrt2}-\frac8{15}h^2\right)^2
 +\frac8{15}h^2\left(h-\frac1{2\sqrt2}\right)^2
 +\frac{h^2}{60}\ge0.
\end{aligned}
\tag{11}
$$

This proves (1) in this branch. Equality forces h=v=0, hence u=p=1.
The bounds a,b<=1/2 then force a=b=1/2; (4) forces c=d=0,y=1.

## 3. A local bound retaining the spectral spread

The other branch uses a stronger form of the same block calculation.
Rotate the queried plane at one site along its singleton direction and
write S=[[A,C],[C*,E]]. Put mu=Tr(E)=u-2b_i, and let m0 be the
smallest positive eigenvalue of S. Then

$$
\begin{aligned}
W_i
&=1-2\operatorname{Tr}(AE)+4\|C\|_2^2
 -2\operatorname{Re}\operatorname{Tr}(C^2)\\
&\ge1-2\kappa\mu+2\|C\|_2^2.
\end{aligned}
$$

Since S^2>=m0 S, the lower diagonal block gives
||C||_2^2>=m0 mu-Tr(E^2)>=m0 mu-mu^2. Thus

$$
W_i\ge1-2\mu(\kappa-m_0+\mu).
$$

Centering the four eigenvalues of S bounds their largest-minus-smallest
gap by sqrt(2)v. Therefore, throughout (5),

$$
\boxed{W_i\ge1-2(u-2b_i)(\sqrt2v+u-2b_i).}
\tag{12}
$$

This argument keeps the off-diagonal block C. It requires neither a
pinching step nor a rank bound on an individual marginal.

## 4. The other branch: reduce to one polynomial rectangle

Suppose b<=c+d; ties may be handled by either branch. Put

$$
\mu=u-2a,\quad q=b+c+d,\quad k=u+\sqrt3v,\quad
x=2\mu(\sqrt2v+\mu).
$$

Equations (4), (6) and (12) give

$$
D\ge4-u^2-y,\qquad
D\ge4-3uk-k\mu+2kq,\qquad W_1\ge1-x.
\tag{13}
$$

The exact top-four inequality becomes

$$
H\le uq+v\sqrt{J-q^2},\quad
H=2y-u(u-\mu),\quad J=2y-(u-\mu)^2.
\tag{14}
$$

Define

$$
\lambda=\frac{2(\sqrt2-1)}3,\qquad
B=4-\frac{4\sqrt2}3,\qquad
D_*=B+\lambda x(1-x),\qquad Y=4-u^2-D_*.
\tag{15}
$$

We prove the strict bound D>D_*. If y<Y the first inequality in (13)
already gives it. For y>=Y, a putative D<=D_* and the second inequality
in (13) imply the fixed threshold

$$
q\le q_0:=\frac{3u+\mu}{2}-\frac{u^2+Y}{2k}.
\tag{16}
$$

The threshold q0 is held fixed as y varies; replacing Y by y in (16)
would not follow from the proposed failure D<=D_*.

At y=Y let H0,J0 be the values in (14). The exact polynomial certificate
below proves

$$
C_0:=uH_0-q_0>0,\qquad
F_0:=C_0^2-v^2(J_0-H_0^2)>0.
\tag{17}
$$

Moreover H0>1/2. Indeed, (5) and ordering give a>5/16, mu<3/8 and
sqrt(2)v<1/2, hence 0<=x<21/32<1. Thus x(1-x)<=1/4 and

$$
H_0=2Y-u^2+u\mu
\ge\frac{7\sqrt2-8}{3}>\frac12.
\tag{18}
$$

The lower bound a>5/16 uses a^2>=y/8>=r/4>1/10>25/256.

For y>=Y, H increases while Delta=J-H^2 strictly decreases, since
H'=2 and Delta'=2-4H<0. If Delta becomes negative, (14) is impossible
by Cauchy. Otherwise its lower feasible q boundary is

$$
q_{\min}(y)=uH-v\sqrt{J-H^2},
$$

which increases with y. At Y, (17) gives q0<q_min(Y). If Delta(Y)<0,
there is no feasible y>=Y in the first place. In either case (16)
contradicts (14). This proves D>D_*.

For clarity about the circle root, C0>0 puts q0 below uH0; F0>0 then
puts it below the lower root, rather than above the upper root. All
feasible q<=q0 have H-uq>=v^2H>0, with the non-strict version when v=0,
so the underlying squared inequality is legitimate.

## 5. The exact rational certificate

Set

$$
\tau=v/u,\quad m=\mu/u,\quad d_0=1+\tau^2,\quad
h_0=1+\sqrt3\tau,\quad t=2m(\sqrt2\tau+m).
$$

Every potentially extremal seed in (5) lies in the single closed box

$$
0\le\tau,m\le\frac9{25}.
\tag{19}
$$

For tau, use alpha>625/706, equivalent to
sqrt(2)>3993/2824, with positive-square difference 5903. For m, ordering
and y>=2r+v^2 give
m=1-2a/u<=1-sqrt(y/(2u^2))<=1-sqrt(r)<9/25.
The last strict comparison follows from r>256/625, whose radical
square comparison has difference 5089.

Define the following polynomials over Q(sqrt(2),sqrt(3)):

$$
\begin{aligned}
Z&=\left(\frac{4\sqrt2d_0}{3}-1\right)d_0
 -\lambda t(d_0-t),\\
Q_0&=h_0(3+m)d_0-d_0-Z,\\
A_0&=2h_0[2Z-(1-m)d_0]-Q_0,\\
C&=2h_0[2Z-(1-m)d_0]-d_0Q_0,\\
P&=A_0^2-\tau^2\left\{
4h_0^2[2Zd_0-(1-m)^2d_0^2]-Q_0^2\right\}.
\end{aligned}
\tag{20}
$$

Their relation to the preceding section is exactly

$$
Y=Z/d_0^2,\qquad
C_0=\frac{C}{2h_0d_0^{5/2}},\qquad
F_0=\frac{P}{4h_0^2d_0^4}.
\tag{21}
$$

The checker expands C and P, converts them to the tensor Bernstein basis
on (19), and proves that every coefficient has respectively the lower
bounds

$$
C:\ \frac4{25},\qquad P:\ \frac1{10000}.
\tag{22}
$$

C has bidegree (6,4), and P has bidegree (10,8): there are 35 and 99
coefficients. Since the Bernstein basis is nonnegative and sums to one,
(22) proves strict positivity on the entire rectangle, including its
boundary. There are no subdivisions or sampled evaluations in this
certificate.

For reproducibility, if p(tau,m)=sum p_ij tau^i m^j has bidegree (N,M),
its Bernstein coefficient with indices k,l on [0,L]^2 is

$$
\sum_{i\le k,\ j\le l}
p_{ij}L^{i+j}\frac{\binom{k}{i}}{\binom{N}{i}}
\frac{\binom{l}{j}}{\binom{M}{j}},\qquad L=9/25.
\tag{23}
$$

The script uses integer and Fraction arithmetic. Each algebraic coefficient
is enclosed using rational bounds for sqrt(2) and sqrt(3), whose validity
is checked by integer squaring; interval multiplication encloses their
products. Thus (22) is an exact finite
positivity certificate, not floating-point evidence for a universal claim.

## 6. Finish the other branch and classify equality

Group the two queries at site 1 and the other six. For any actual D,W1,

$$
\sum_A\sqrt{a_A}\le
\sqrt{4-2W_1}+\sqrt{36-6D+6W_1}.
$$

If 0<=x<1-1/sqrt(2), then W1>=1-x>1/sqrt(2)>D_*/4; here
D_*<=B+lambda/4<5/2<2sqrt(2). Lowering D
to D_* and then W1 to 1-x therefore increases this expression. The
exact threshold making the resulting expression at most 4+2sqrt(2) is

$$
D_{\rm crit}(x)=B+\lambda x-
\frac{2(1+\sqrt2)x^2}{3(\sqrt{1+x}+1)^2}
\le B+\lambda x-\lambda x^2=D_*.
\tag{24}
$$

The last comparison holds for 0<=x<=1, with its coefficient minimum
at x=1. The strict inequality D>D_* thus proves a strict score bound.

For 1-1/sqrt(2)<=x<21/32<1/sqrt(2), directly
D_*>=5-2sqrt(2); this is the quadratic inequality
lambda x(1-x)>=5-2sqrt(2)-B on that interval. Therefore D>D_* and
Cauchy over all eight queries again give a strict score bound. This
case split avoids using a single-site deficit below the monotonicity
threshold D/4. Branch B has no equality case.

In branch A, equality in (11) already forced u=1,y=1 and
(a,b,c,d)=(1/2,1/2,0,0). Equality in (1) also forces D=2, so the sharp
sum-affinity budget in the preceding note is attained. Its equality
classification gives (3) with both pure states in their X/Z planes.
Their root-affinity sum is
4+|x_1|+|z_1|+|x_2|+|z_2|, which reaches the target exactly at the two
bisectors. This proves the complete normalized-seed equality statement.

Finally, the established fidelity--affinity inequality
||SAS||_1^2<=Tr(SASA), sourced in
[the entropic converse](../STRONG_ENTROPIC_CONVERSE.md#3-root-fidelity-affinity-and-the-two-pauli-energy),
and the [normalized-seed reduction](../COLLECTIVE_ENCODING_REDUCTION.md)
turn (1) into the unrestricted upper bound in (2). Retaining two original
qubits and applying the compatible four-outcome X/Z POVM at contrast
1/sqrt(2) to each other site attains the seed value. Randomizing the
retained pair, or applying the established seed twirl, gives equal contrast
on all eight queries and the stated error.

## 7. Verification and scope

The finite exact certificate proves only the explicit scalar inequalities
(22); the preceding analytical reduction is needed to connect them to all
positive rank-four seeds. Separate fixed-matrix diagnostics check the
normalizations and selected equality, nonflat, and boundary constructions.
They are not numerical optimization or a substitute for the proof.

Independent readers reconstructed the branch-A root elimination and sum
of squares, the coherent local block bound, the branch-B fixed-threshold
circle argument, the certificate scaling, the grouped curvature comparison,
and all equality and operational conclusions.

Reproduce the exact scalar certificate and the separate fixed-construction
checks with

```bash
python tools/check_nonflat_quarter_rank_certificate.py --output results/nonflat_quarter_rank_certificate.json
python tools/check_nonflat_quarter_rank.py --output results/nonflat_quarter_rank.json
```

The reports record the source and proof-note hashes. An independent rerun
of the exact certificate must reproduce its rational conclusions; finite
floating-point construction checks are interpreted within their stated
tolerances. The theorem settles this finite n=4, dimension-four case. It does not settle the general
sharp entropy inequality, the common-accuracy asymptotic rate, or arbitrary
larger input blocks. An exhaustive theorem-level novelty comparison for
this supplied proof has not been completed.
