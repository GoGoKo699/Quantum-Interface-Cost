# A vanishing Pauli gap forces a classical head or low support

**Research base:** main `eb88f82db5bfd4acd7b687ca209fc094fc5df2ea`.
**Date:** 27 September 2026.

For a flat two-mode head, vanishing of the Pauli-conjugation gap alone
forces its complementary state to be flat. Its coefficients then have
three explicit forms. One gives an entanglement-breaking head channel;
the other two have support at most `2+sqrt(2)`. Unlike the preceding
[zero-deficit classification](QUANTITATIVE_TWO_MODE_STABILITY.md#7-the-zero-squared-deficit-boundary-and-its-exceptional-branch),
this result does not assume equality in the fidelity--affinity comparison.

**Status:** supplied analytical proof, independently reconstructed within
this workspace. The high-second-mode consequence uses the existing robust
head-channel criterion. This is an exact structured class, not a
quantitative neighborhood or an unrestricted converse. No publication
priority is claimed.

## 1. Statement and actual-head consequence

Let `R=R1 tensor R2`, let Q have dimension at most four, and let
`sigma=P/2` for a rank-two projector P on RQ. Purify sigma by a qubit E,
and set `rho=Tr_Q |Psi><Psi|` and `S=sqrt(rho)`. Then

```math
\operatorname{rank}\rho\le4,\qquad \rho_E=I_E/2.
```

Suppose S has only reference Pauli components `I,X1,Z1,X2,Z2`.
Equivalently, equality holds in the Pauli-conjugation estimate

```math
\sum_{A\in\{X_1,Z_1,X_2,Z_2\}}\operatorname{Tr}(SASA)
\le 2+\frac12\operatorname{Tr}[(\operatorname{Tr}_R S)^2].
\tag{1}
```

Let Phi be the head-to-Q channel determined by the purification, and put
`f_A=||SAS||_1`.

**Theorem.** Under this assumption, `rho=Pi/4` for a rank-four projector
Pi, and

```math
\boxed{\Phi\text{ is entanglement breaking}
\quad\text{or}\quad \sum_A f_A\le2+\sqrt2.}
\tag{2}
```

For an actual earlier Hamiltonian
`H0=X1 B1+Z1 D1+X2 B2+Z2 D2`, let U and m be its two greatest
eigenvalues and take P to be its actual top head. If `m>=k:=2+sqrt(2)`,
(2) proves `||H0+h3||<=4+sqrt(2)` for every third binary-POVM pair.
Indeed trace-norm duality gives `U+m<=2 sum_A f_A`. In the low-support
case, `U>=m>=k` therefore forces U=m=k, and the triangle bound applies.
In the EB case, the
[robust head-channel theorem](ROBUST_HEAD_CHANNEL_CONVERSE.md#2-the-complete-high-second-mode-strip-lies-in-the-rectangle)
applies throughout this high-m strip and gives a strict bound. No
assumption is made about cross commutation or the earlier readout algebra.

## 2. Flatness from the Pauli gap alone

Put `T=Tr_R S` and `Gamma=Y1 Y2`. The assumed Pauli support gives

```math
S+\Gamma S\Gamma=I_R\otimes T/2.
\tag{3}
```

T is positive definite: a kernel direction would support neither S nor
rho, contradicting `rho_E=I/2`. Define

```math
C=(I_R\otimes T^{-1/2})S(I_R\otimes T^{-1/2}).
```

Then `C+Gamma C Gamma=I/2`. Both positive summands have rank at most
four, while their sum has rank eight; both ranks thus equal four.
Moreover `0<=C<=I/2`, and `I/2-C` has rank four. Its four zero
eigenvalues force all four nonzero eigenvalues of C to equal one half.
Thus `F=4C-I` is a reflection. Its reference support is

```math
F=\sum_A A\otimes M_A.
\tag{4}
```

The identity `F^2=I` imposes same-site commutation, cross-site
anticommutation, and `sum_A M_A^2=I_E`. Consequently
`L(X)=sum_A M_A X M_A` is unital and completely positive. Substituting

```math
S=\frac14(I_R\otimes\sqrt T)(I+F)(I_R\otimes\sqrt T)
```

into `Tr_R S^2=I/2` gives exactly

```math
T+L(T)=2T^{-1}.
\tag{5}
```

Let l and u be the minimum and maximum eigenvalues of T. Positivity and
unitality give `lI<=L(T)<=uI`. Evaluating (5) in the corresponding
extremal eigenvectors yields

```math
u(u+l)\le2\le l(u+l).
```

Hence u=l, and the scalar equation implies T=I. Therefore
`S=(I+F)/4=Pi/2` and `rho=Pi/4`. Neither fidelity--affinity equality
nor equal support coordinates were used.

## 3. Three coefficient forms

The following cases exhaust the Hermitian qubit coefficients in (4), up
to a unitary on E and exchange of reference sites.

**Traceless coefficients.** If every nonzero coefficient is traceless,
commutation makes each site's Bloch vectors parallel, while cross
anticommutation makes the two site axes perpendicular. Thus

```math
F=(aX_1+bZ_1)\otimes\boldsymbol n\cdot\boldsymbol\sigma_E
 +(cX_2+dZ_2)\otimes\boldsymbol n'\cdot\boldsymbol\sigma_E,
\quad a^2+b^2+c^2+d^2=1,
\tag{6}
```

with perpendicular unit axes n,n'. Zero sites are allowed. Diagonalize
the two commuting reference factors. In their product eigenvectors
`|rs>`, F has a unit Bloch vector on E, so

```math
\rho=\frac14\sum_{r,s}|rs\rangle\langle rs|_R
 \otimes|\chi_{rs}\rangle\langle\chi_{rs}|_E.
\tag{7}
```

Purifying with orthogonal memory labels gives

```math
\Phi(\omega)=\frac12\sum_{r,s}
 \langle\chi_{rs}^{*}|\omega|\chi_{rs}^{*}\rangle
 |rs\rangle\langle rs|_Q.
\tag{8}
```

The rank-one effects sum to I because `rho_E=I/2`. Equation (8) is
measure and prepare. Every other purification differs by a memory
isometry, preserving the EB property.

**A single reference site.** If only one site occurs, its commuting
coefficients can be diagonalized on E:

```math
F=(a_+X_1+b_+Z_1)\otimes P_+
 +(a_-X_1+b_-Z_1)\otimes P_-,
\quad a_\pm^2+b_\pm^2=1.
\tag{9}
```

Its fidelity profile is

```math
\left(\frac{|a_+|+|a_-|}{2},
\frac{|b_+|+|b_-|}{2},1,1\right).
\tag{10}
```

The sum is at most `2+sqrt(2)`. This channel need not be EB.

**Flagged disjoint axes.** Suppose both sites occur and some coefficient
M is nontraceless. If M were invertible, every anticommuting coefficient
on the other site would vanish. Indeed writing
`M=aI+v.sigma`, `N=bI+w.sigma`, with a nonzero, gives
`aw+bv=0` and `ab+v.w=0`, hence `b(a^2-|v|^2)=0`.
Invertibility would force N=0. Thus M has rank one. In its diagonal
basis, an anticommuting Hermitian partner is supported on its kernel;
a nonzero partner then forces every original-site coefficient onto
the other line. Therefore

```math
F=(aX_1+bZ_1)\otimes P
 +(cX_2+dZ_2)\otimes(I-P),
\quad a^2+b^2=c^2+d^2=1.
\tag{11}
```

The profile is

```math
\frac12(1+|a|,1+|b|,1+|c|,1+|d|),
\tag{12}
```

again with sum at most `2+sqrt(2)`. The formulas (10) and (12) follow
by diagonalizing rho on E: each block has one pure reference qubit and
one maximally mixed reference qubit. Compressing a Pauli to the pure
factor gives its Bloch expectation.

This flagged case is essential: nonzero coefficients at both sites do
not alone force the traceless form. It obeys
`sum_A f_A^2<=3/2+sqrt(2)`, so its squared deficit is at least
`3/2-sqrt(2)`; this is why it was absent from the earlier zero-squared-
deficit classification. Equations (6)--(12) prove (2).

## 4. A fixed EB head need not have equal leading energies

The theorem does not assert U=m in the EB case. In reference bisector
coordinates, the balanced earlier operator is

```math
H_*={2\over\sqrt3}(Z_1Z_A+Z_2Z_B)
 +\sqrt{2/3}(X_1X_A+X_2Z_AX_B).
```

Both `G=X1 XA ZB` and `G'=X2 XB` commute with H_* and anticommute
with each other. G therefore restricts to a traceless reflection on its
top doublet. For `0<tau<=1/1000`, the allowed contraction operator
`H_tau=(1-tau)H_*+tau G` has the same isolated top projector and

```math
U=(1-\tau)2\sqrt3+\tau,
\qquad m=(1-\tau)2\sqrt3-\tau>2+\sqrt2.
\tag{13}
```

The original site-one readouts have norms at most
`(1-tau)+tau/sqrt(2)<=1`; the other pair is simply scaled. The original
spectral gap exceeds two, so this small commuting perturbation preserves
the top projector. For the last strict comparison, use
`sqrt(3)>173/100` and `sqrt(2)<283/200`. Thus the head channel stays
exactly EB while U and m split. Equal energies require additional
readout structure or saturation assumptions.

## 5. Verification and scope

Independent internal review reconstructed the flattening identity,
all three coefficient cases, the support profiles and the EB channel.
The result assumes an exactly vanishing Pauli gap. It does not settle
any complete remaining reflection signature or the unrestricted bound.

Targeted finite diagnostics are included in

```bash
python tools/check_head_structure_converses.py --output results/head_structure_converses.json
```

Those fixed constructions and exact scalar comparisons are consistency
checks, not substitutes for the universal proofs. The result record
stores hashes of the source and proof notes; it does not establish
publication priority.
