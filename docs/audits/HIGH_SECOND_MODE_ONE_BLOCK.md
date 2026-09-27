# A high second mode permits any one-block last pair

Research base: `eb88f82db5bfd4acd7b687ca209fc094fc5df2ea`.
Date: 27 September 2026.

**Status:** supplied analytical theorem, independently reconstructed within
this workspace. The complete high-second-mode region is now safe when the
last pair has at most one noncommuting Jordan block. This does not close
any whole remaining reflection signature, prove the unrestricted
retention conjecture, or certify publication originality.

Let Q have dimension four and

```math
H_0=X_1B_1+Z_1D_1+X_2B_2+Z_2D_2,
\qquad -I\le B_i,D_i\le I.
```

Write U >= m >= ell for its three highest eigenvalues, and set

```math
r=\sqrt2,\quad k=2+r,\quad \Lambda=4+r,
\quad \delta=2-r.
```

**Theorem.** If m >= k and the last reflection pair has at most one
noncommuting two-dimensional Jordan block, then

```math
\|H_0+X_3B_3+Z_3D_3\|<\Lambda.
```

The earlier pairs may be arbitrary binary POVMs; no cross commutation,
common Jordan basis, or head-channel separability is assumed. In
particular this closes the high-m part of both remaining signatures
`(22)^2(11)` and `(22)^2(12)`, as well as the corresponding one-block
boundary of `(22)^3`. It does not close any whole remaining signature.

Equivalently, any potential violating `(22)^2(11)` or `(22)^2(12)` tuple
must have m < k after its one-block query is placed last. The same holds
for any tuple with a one-block query. Its rank-one last-query resolvent is
then strictly positive, although no uniform positive gap is asserted over
the remaining region. The two-leading-mode obstruction can therefore
persist only when the last pair also has two active blocks. This reduction
does not assert that the rank-one certificate always passes there.

## 1. A Bell-projector compression from the actual channel moment

Let V:C^2 -> R1 R2 Q be an isometry onto the two leading modes,
Phi(A)=Tr_(R1 R2)(V A V^dagger), and E=Phi^*. The [two-mode theorem](TWO_MODE_RESOLVENT.md), Section 3.1, gives

```math
\Phi(\operatorname{diag}(U^2,m^2))\le8I_Q.
```

Complete positivity therefore implies Phi(I_2) <= (8/m^2) I_Q.
For any Bell vector supported on R3 and a memory plane, let Pi denote
its rank-one projector. If W:C^2 -> Q is its defining isometry, then

```math
T=(\operatorname{id}_2\otimes\mathcal E)(\Pi)\ge0,
\qquad
\operatorname{Tr}_{\rm head}T
=\frac12[W^\dagger\Phi(I_2)W]^T
\le\frac4{m^2}I_2.
```

Every positive operator T on A tensor C^d obeys
T <= d (Tr_(C^d) T) tensor I_d. One direct proof is to establish this
for rank-one summands using a Schmidt decomposition and Cauchy--Schwarz,
then sum. With d=2 this proves

```math
\boxed{(\operatorname{id}_2\otimes\mathcal E)(\Pi)
\le\frac8{m^2}I_4.}
\tag{1}
```

The transpose depends on the chosen Bell-vector basis and does not affect
the operator bound. The factor 8/m^2 is dimension two on the head,
not a missing Bell normalization.

## 2. The last-query envelope

The [one-block spectral majorant](JORDAN_BLOCK_CONVERSE.md), Section 2, gives

```math
h_3\le rI+\delta\Pi.
```

Here Pi is the unique positive Bell projector of the active block; if
there is no active block, any Bell projector gives a weaker valid cap.
The other eigenvalues, including all scalar blocks, are at most r.

Let t=Lambda-ell > 2. Operator monotonicity of inversion gives

```math
(tI-h_3)^{-1}
\le\frac I{t-r}
+\frac{\delta}{(t-r)(t-2)}\Pi.
\tag{2}
```

With Delta=diag(U-ell,m-ell), sandwich the E-compression by sqrt(Delta)
and use (1). The exact two-mode envelope test obeys

```math
K\le
\frac{U-\ell}{t-r}
\left(1+\frac{8\delta}{m^2(t-2)}\right)I_4.
\tag{3}
```

It is enough to prove the displayed scalar strictly below one.

## 3. An elementary certificate over the entire high-m region

The [sharp support theorem](SHARP_TWO_MODE_SUPPORT.md) and the
[two-mode chiral second moment](TWO_MODE_RESOLVENT.md) give

```math
U+m\le4\sqrt3,
\qquad U^2+m^2+\ell^2\le32.
```

Since m >= k,

```math
k\le U\le u_*:=4\sqrt3-k,
\qquad 0\le\ell\le e(U):=\sqrt{32-k^2-U^2}.
```

Define

```math
C=\frac{8\delta}{k^2}=40-28\sqrt2.
```

Replacing 8delta/m^2 by C in (3), the desired inequality is exactly

```math
(4-U)(k-\ell)-C(U-\ell)>0.
\tag{4}
```

All denominators previously multiplied are positive. The coefficient
4-U-C is positive, so the left side decreases with ell. It therefore
suffices to prove positivity of

```math
H(U)=(4-U)(k-e(U))-C(U-e(U)).
```

On the entire interval [k,u_*], the following safe rational bounds hold:

```math
\frac{17}5<k<\frac{683}{200},\quad
\frac25<C<\frac{403}{1000},\quad
U<\frac{1757}{500}<\frac{18}5,\quad
\frac{14}5<e(U)<3.
\tag{5}
```

In particular 4-U-C > 83/1000. Differentiating gives

```math
H'(U)=e(U)-k-C+(4-U-C)\frac U{e(U)}
<-\frac45+\frac15\frac{18/5}{14/5}
=-\frac{19}{35}<0.
```

Thus only U=u_* needs checking. There

```math
u_*<\frac{1757}{500},\qquad
k>\frac{1707}{500},\qquad
e(u_*)<\frac{57}{20},\qquad C<\frac{403}{1000}.
```

Using the monotonicity of (4) in each of its four arguments within these
ranges gives the strictly positive rational lower bound

```math
H(u_*)>
\left(4-\frac{1757}{500}\right)
\left(\frac{1707}{500}-\frac{57}{20}\right)
-\frac{403}{1000}
\left(\frac{1757}{500}-\frac{57}{20}\right)
=\frac{407}{62500}>0.
\tag{6}
```

For fully elementary verification of the radical bounds, use

```math
\frac{141421}{100000}<\sqrt2<\frac{99}{70},\qquad
\frac{433}{250}<\sqrt3<\frac{1732051}{1000000}.
```

All four follow by squaring positive rationals. They imply
351/100 < u_* < 1757/500 and 341/100 < k < 683/200.
Consequently the upper endpoint bound for e follows from

```math
\left(\frac{57}{20}\right)^2
-\left[32-\left(\frac{351}{100}\right)^2
-\left(\frac{341}{100}\right)^2\right]
=\frac{707}{10000}>0.
```

The lower bound e(U)>14/5 follows from

```math
32-\left(\frac{1757}{500}\right)^2
-\left(\frac{683}{200}\right)^2
-\left(\frac{14}{5}\right)^2
=\frac{149579}{1000000}>0.
```

The upper bound e(U)<3 follows from U>=k>17/5. The two bounds on C
follow immediately from C=40-28sqrt(2) and the same rational bounds.

Equations (3)--(6) imply K<I. The two-mode positive-update equivalence
therefore gives H0+h3<Lambda I. Conjugation by Y on all three references
reverses the Hamiltonian, giving the strict operator-norm statement.

## 4. Extensions and limitations

The same theorem holds for a last binary-POVM pair which is block
diagonal on one fixed memory plane and scalar on its two-dimensional
complement (or on a further scalar splitting of that complement).
Decompose both Hermitian contractions into extreme points within this
fixed block algebra. Every resulting reflection pair has at most one
active two-dimensional block, and convexity of operator norm proves
the claim. This does not include arbitrary contraction pairs merely
because a particular non-extreme decomposition looks favorable.

The proof is driven by the actual weighted channel moment and the fact
that one active last block produces one Bell projector. It does not
replace the full head channel by its diagonal entries and does not
claim that it is entanglement breaking. The assumption m>=k is essential
to this supplied argument. The full low-m portions of the signature
problems remain open.


## 5. Verification and model scope

The operator proof and scalar monotonicity argument above received an
independent internal reconstruction. This means review by another agent
in this workspace, not external peer review. The targeted diagnostic is

```bash
python tools/check_head_structure_converses.py --output results/head_structure_converses.json
```

It checks the positive Bell compression, the actual channel moment, the
one-block resolvent comparison, and the rational inequalities used in
the proof on small deterministic constructions. Its finite matrix checks
supplement the proof; they do not establish the universal theorem or
publication novelty by sampling. The result and rerun status are recorded
in [reproducibility](../REPRODUCIBILITY.md).

The setup remains one arbitrary unknown specimen, one delayed local X/Z
query, unrestricted collective encoding, unlimited classical side information, and
worst-case retained quantum dimension. The leading-mode channel and Bell
compression are proof devices, not extra physical resources.
