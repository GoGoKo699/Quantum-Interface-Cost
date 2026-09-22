# An entropy bound for spectra of bounded condition number

Date: 2026-09-22. Research base:
`87b6432cdd1f29bc4981f24bd6732bb933741193`.
Status: derived with the proof below and independently reconstructed within
this workspace. This is a sufficient spectral
condition, not a resolution of the unrestricted entropy conjecture or a
claim of publication novelty.

This note excludes a dimension-independent neighborhood of the maximally
mixed Gram matrix from witnessing a collective rate advantage. The
eigenvectors are unrestricted: complex, entangled eigenvectors are allowed.
The result applies for every number of input qubits, including the
two-input, full-rank case left open by the rank-two theorem.

## 1. Statement

For an n-qubit density matrix, write

$$
g(\rho)=\sum_{i=1}^n\sum_{b=X,Z}
\|\sqrt\rho P_{i,b}\sqrt\rho\|_1,
\qquad c=2-\sqrt2.
$$

Suppose that rho is full rank, and define its spectral condition number
and a coefficient by

$$
\kappa=\frac{\lambda_{\max}(\rho)}{\lambda_{\min}(\rho)},
\qquad
\alpha_\kappa=1+\frac{2\sqrt\kappa}{1+\kappa}.
$$

All entropies below are in bits. The logarithm in `ln 2` is natural.

**Theorem.** Every such state satisfies

$$
\boxed{
g(\rho)\le
2n-\frac{\alpha_\kappa\ln2}{2}\bigl(n-S(\rho)\bigr).
}
\tag{1}
$$

Consequently, put

$$
r_* = \frac{2(2-\sqrt2)}{\ln2}-1,
\qquad
\kappa_*=
\left(\frac{1+\sqrt{1-r_*^2}}{r_*}\right)^2
=6.235819648070267\ldots.
\tag{2}
$$

Whenever `kappa <= kappa_*`,

$$
\boxed{
g(\rho)\le\sqrt2 n+(2-\sqrt2)S(\rho).
}
\tag{3}
$$

For a nonmaximally mixed state satisfying the condition, (3) is strict.
The threshold in (2) is sufficient; its optimality is not asserted.

An easier operator-norm condition implying the hypothesis is

$$
\|2^n\rho-I\|_\infty
\le\sqrt{1-r_*^2}=0.7235973120842801\ldots.
\tag{4}
$$

Indeed, if the left side is at most t below one, then
`kappa <= (1+t)/(1-t)`.

## 2. A direct trace-norm bound

For any Hermitian unitary P, define

$$
F_P=\|\sqrt\rho P\sqrt\rho\|_1,
\qquad
I_\rho(P)=\frac12\sum_{a,b}
\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}
|P_{ab}|^2,
\tag{5}
$$

where matrix entries are taken in an eigenbasis of rho. This is one quarter
of the usual symmetric-logarithmic-derivative quantum Fisher information
for the unitary generator P. The proof uses the displayed expression,
without importing a metrological operational model.

Choose a Hermitian contraction B attaining trace-norm duality for
`sqrt(rho) P sqrt(rho)`. Weighted Cauchy-Schwarz gives

$$
\begin{aligned}
F_P^2
&=\left|\sum_{a,b}\sqrt{\lambda_a\lambda_b}
P_{ab}B_{ba}\right|^2\\
&\le
\left(\sum_{a,b}\frac{2\lambda_a\lambda_b}
{\lambda_a+\lambda_b}|P_{ab}|^2\right)
\left(\sum_{a,b}\frac{\lambda_a+\lambda_b}{2}
|B_{ba}|^2\right)\\
&\le 1-I_\rho(P).
\end{aligned}
\tag{6}
$$

For the last line, the second parenthesis is `Tr(rho B^2)<=1`. The first
is `1-I_rho(P)`, because `P^2=I` and

$$
\frac{2\lambda_a\lambda_b}{\lambda_a+\lambda_b}
=\frac{\lambda_a+\lambda_b}{2}
-\frac{(\lambda_a-\lambda_b)^2}{2(\lambda_a+\lambda_b)}.
$$

In particular, `0<=I_rho(P)<=1`, and

$$
F_P\le\sqrt{1-I_\rho(P)}\le1-\frac12 I_\rho(P).
\tag{7}
$$

Equations (5)--(7) also hold for singular states when terms with two zero
eigenvalues are assigned zero. Full rank is needed for the uniform
condition-number comparison in the next step.

## 3. Comparison with affinity and the entropy energy

Let

$$
a_P=\operatorname{Tr}(\sqrt\rho P\sqrt\rho P).
$$

Using `P^2=I` again,

$$
1-a_P=\frac12\sum_{a,b}
(\sqrt{\lambda_a}-\sqrt{\lambda_b})^2|P_{ab}|^2.
\tag{8}
$$

For each pair of positive eigenvalues,

$$
\frac{(\lambda_a-\lambda_b)^2}{\lambda_a+\lambda_b}
=(\sqrt{\lambda_a}-\sqrt{\lambda_b})^2
\left(1+\frac{2\sqrt{\lambda_a\lambda_b}}
{\lambda_a+\lambda_b}\right).
$$

Their ratio lies in `[1/kappa,kappa]`, so the parenthesis is at least
`alpha_kappa`. Equal eigenvalues contribute zero to both sides. Therefore

$$
I_\rho(P)\ge\alpha_\kappa(1-a_P).
\tag{9}
$$

Use the normalized trace and depolarizing Dirichlet form from
[the unrestricted converse](STRONG_ENTROPIC_CONVERSE.md), Sections 2--3:

$$
d=2^n,\quad A=\sqrt{d\rho},\quad
\tau(T)=\operatorname{Tr}(T)/d,\quad
\mathscr D(A)=\tau\left(A\sum_i(\mathrm{id}-\mathcal E_i)(A)\right).
$$

Here `E_i` is normalized partial trace on site i followed by reinsertion
of the identity there. The Pauli expansion gives

$$
\sum_{i,b=X,Z}(1-a_{P_{i,b}})\ge2\mathscr D(A).
\tag{10}
$$

The established qubit logarithmic-Sobolev inequality gives

$$
\mathscr D(A)\ge\frac{\ln2}{2}(n-S(\rho)).
\tag{11}
$$

For exact provenance and normalization, Beigi,
[arXiv:2105.00462v2](https://arxiv.org/pdf/2105.00462v2), Theorem 2,
Eqs. (6)--(7), printed p. 4, supplies the stronger bound

$$
\mathscr D(A)\ge
n\left(\frac12-\sqrt{u(1-u)}\right),
\qquad h_2(u)=S(\rho)/n,\quad 0\le u\le\frac12.
\tag{12}
$$

Equation (11) follows from (12) and the scalar inequality

$$
1-2\sqrt{u(1-u)}\ge(\ln2)(1-h_2(u)).
$$

That scalar inequality is proved explicitly in
[the stabilizer-basis argument](ENTROPY_INEQUALITY_BOUNDARIES.md),
Section 3. Thus neither a tensorization assertion for SLD information nor
a new logarithmic-Sobolev theorem is assumed here.

Summing (9), (10), and (11) yields

$$
\sum_{i,b} I_\rho(P_{i,b})
\ge\alpha_\kappa\ln2\,(n-S(\rho)).
\tag{13}
$$

Summing (7) now proves (1). The function `alpha_kappa` decreases for
`kappa>=1`; solving `alpha_kappa ln2/2 >= 2-sqrt(2)` gives (2), and
therefore (3).

If rho is not maximally mixed, it fails to commute with at least one of
the local X/Z generators, since those generators span the full matrix
algebra under products. For that generator `I_rho(P)>0`, and the second
inequality in (7) is strict. This proves the stated strictness.

## 4. A state-dependent refinement and the remaining gap

Keeping (12), and applying Cauchy-Schwarz to the sum in (6), also gives

$$
\frac{g(\rho)}{2n}
\le\sqrt{1-\alpha_\kappa
\left(\frac12-\sqrt{u(1-u)}\right)},
\qquad h_2(u)=S(\rho)/n.
\tag{14}
$$

Its radicand is nonnegative for any state obeying the hypotheses, as
follows already from (6), (9), and (10). Equation (14) can certify (3)
for some larger condition numbers at a specified entropy. Equation (2)
is the uniform, entropy-independent sufficient threshold reported here.

A tempting stronger route would establish
`sum_{i,b} I_rho(P_{i,b}) >= n-S(rho)` for all states. Together with
(6), that would give the unrestricted memory-rate lower bound
`R(eta)>=max(0,2 eta^2-1)`. No proof of that SLD entropy inequality is
provided or assumed. The established logarithmic-Sobolev theorem controls
the affinity deficits instead; the quantitative comparison (9) is what
makes the present restricted result valid.

The condition on the Gram spectrum is an exclusion criterion for a
possible witness, not a restriction imposed on admissible encoders.
The [entropy-rate characterization](ENTROPY_RATE_CHARACTERIZATION.md)
therefore implies that no Gram matrix satisfying (2) can demonstrate a
rate improvement over the subset line. All original operational
quantifiers remain unchanged: one arbitrary unknown specimen, a single
delayed query, arbitrary collective encoding, unlimited finite classical
records, worst-case quantum dimension, and uniform arbitrary-input error.
Although a full-rank single-block seed itself has quantum dimension
`2^n`, its entropy can be smaller than n; the entropy-rate characterization
is why excluding such Gram matrices is useful. Products of separately
certified states also satisfy (3), by additivity of g and S, even when
their multiplied condition number exceeds (2).
Full-rank matrices with larger condition number and the unrestricted
conjecture remain unresolved.
