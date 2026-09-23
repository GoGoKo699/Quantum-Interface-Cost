# Two exact obstructions to proposed entropy proof methods

Date: 2026-09-23. Reviewed main:
`d74f329605c9cf82707c09a3c0e925919e8512c0` (PR #16 merge).
Status: exact counterexamples to specified relaxations, independently
checked internally. Neither is an admissible Quantum Interface Cost
counterexample. No all-state proof or violating admissible seed was found.

## 1. Targets and what a relaxation must preserve

For a normalized seed Gram state rho on n qubits, write

$$
g_n(\rho)=\sum_{i,b}\|\sqrt\rho P_{i,b}\sqrt\rho\|_1,
\qquad f_n(\rho)=g_n(\rho)/(2n),\qquad t=1/\sqrt2.
$$

The conjectured sharp local-query entropy inequality is

$$
f_n(\rho)\le t+(1-t)S(\rho)/n.
\tag{1}
$$

The joint score j_n, defined in the
[joint-score audit](ROOF_PROVENANCE_AND_JOINT_SCORE.md), averages the
optimal Bayesian Hamming score for decoding all bits of a chosen product
X/Z basis from its filtered ensemble. It satisfies j_n<=f_n, with an
explicit persistent strict gap. The same right side in (1), with j_n on
the left, is a weaker unresolved target. This comparison does not replace
the original one-delayed-query contract by a joint-query task.

Section 2 shows that exact basis priors and a total Holevo budget are
insufficient even for the joint target. Section 3 shows that the complete
rank-two spectral bound, a norm constraint and vanishing partial traces
are insufficient for the local entropy-energy target. Both constructions
identify constraints discarded by the proposed relaxation; neither
changes the allowed encoder, specimen, error or memory model.

## 2. Exact priors plus a total Holevo budget allow too much decoding

### 2.1 The genuine ensemble and subset equality states

For a fixed product X/Z basis b, the filtered pure-state ensemble is

$$
v_x=\sqrt\rho\,|x_b\rangle,\qquad
p_x=\|v_x\|^2,\qquad
\sum_x|v_x\rangle\langle v_x|=\rho.
$$

Every measurement output Y satisfies the established Holevo bound
`I(X:Y)<=S(rho)` in bits. The proposed relaxation retains the exact prior
p_x and permits any classical channel obeying this scalar budget, then
optimizes its Hamming loss. The following explicit construction defeats
the sharp constant at every nontrivial subset equality state.

For primary statements of the Holevo inequality, see Ruskai,
[quant-ph/0205064v2](https://arxiv.org/abs/quant-ph/0205064v2), Section 7.1,
Eqs. (47)–(50), printed pp. 17–18, and Holevo,
[quant-ph/9611023v1](https://arxiv.org/abs/quant-ph/9611023v1), Section 2,
p. 2. The audit's source review read both primary versions. No capacity
achievability theorem is substituted for a single-specimen measurement;
the classical construction below needs no asymptotic rate-distortion
theorem.

Put `p=(1-t)/2`, and let beta be the positive eigenstate of `(X+Z)/sqrt(2)`.
For every pair of integers `1<=q<n`, take

$$
\rho_{n,q}=\left(\frac I2\right)^{\otimes q}
\otimes|\beta\rangle\langle\beta|^{\otimes(n-q)}.
\tag{2}
$$

Its entropy is q. In every basis tuple the label consists of q independent
uniform bits and n-q independent Bernoulli(p) bits, with bit one denoting
the less likely eigenvalue. The normalized filtered signal states
distinguish the q uniform bits perfectly and contain no information about
the remaining labels: changing one of those labels only multiplies the
unnormalized vector by a scalar.

The exact minimum total Hamming risk is therefore `(n-q)p`, attained by
decoding the uniform bits and outputting zero on all other bits. Thus

$$
j_n(\rho_{n,q})=f_n(\rho_{n,q})
=1-\frac{2(n-q)p}{n}=t+(1-t)\frac qn.
\tag{3}
$$

### 2.2 A classical channel with less information and lower risk

Choose one uniform bit and one Bernoulli(p) bit. Set `e=1/1024` and
`D=p-2e`. Define their joint distribution with outputs Y_1,Y_2 by reverse
binary channels:

- Y_1 is uniform, N_1 is independent Bernoulli(e), and X_1=Y_1 xor N_1.
- Y_2 is Bernoulli(r), N_2 is independent Bernoulli(D), and
  X_2=Y_2 xor N_2, where

$$
r=\frac{p-D}{1-2D}=\frac{2e}{t+4e}.
$$

The pairs are independent, X_1 is uniform and X_2 is exactly Bernoulli(p).
All parameters are in (0,1), and this is a valid forward classical
channel by Bayes' rule. Its two Hamming distortions are e and D, while

$$
I(X_1X_2:Y_1Y_2)=1-h_2(e)+h_2(p)-h_2(p-2e).
$$

Output the other q-1 uniform bits exactly and zero on the other n-q-1
biased bits. Independence gives

$$
I(X:Y)=q-h_2(e)+h_2(p)-h_2(p-2e).
\tag{4}
$$

This is strictly below q by elementary exact bounds. Since t<3/4, p>1/8,
and hence p-2e>1/9. On the interval [p-2e,p],

$$
h_2'(u)=\log_2\frac{1-u}{u}<3.
$$

Consequently `h_2(p)-h_2(p-2e)<6e`, while `h_2(e)>=10e`, so

$$
I(X:Y)<q-4e<q=S(\rho_{n,q}).
\tag{5}
$$

Nevertheless its total Hamming risk is

$$
e+(p-2e)+(n-q-1)p=(n-q)p-e,
$$

and its normalized score is

$$
1-\frac{2\mathbb E d_H(X,Y)}n
=t+(1-t)\frac qn+\frac{2e}{n}.
\tag{6}
$$

This strictly exceeds the conjectured line. The same classical channel
works for every basis tuple, since all the priors are identical with the
specified bit labeling. For n=2, q=1, the relaxation allows score
`(1+t)/2+1/1024` at mutual information strictly below one bit.

### 2.3 Scope of the obstruction

The displayed Y is not a quantum measurement of the filtered ensemble.
It learns a little about a label on which the actual normalized signal
state does not depend, paying for that by slightly worsening a perfectly
encoded uniform bit. A total-information budget loses this constraint on
where information can reside. Keeping all exact priors and the exact
entropy budget still fails; this is not merely a loose application of
Fano's inequality or an approximate entropy inverse.

Conditional Holevo quantities, signal overlaps or additional simultaneous
constraints may avoid the obstruction. Such an argument must use
information discarded here. No extra physical specimen, admissible
interface or advantage over subset encoding has been constructed.

## 3. The rank-two spectral bound does not extend by itself

### 3.1 A Hamiltonian satisfying the relaxed conditions

The genuine two-input Hamiltonians have the form

$$
H_{\rm QIC}=\sum_{i=1}^2\sum_{b=X,Z} A_{i,b}\otimes P_{i,b},
\qquad -I\le A_{i,b}\le I,
\tag{7}
$$

with the trusted operators restricted to X_1,Z_1,X_2,Z_2. They have norm
at most four. Their expectation on a pure vector of Schmidt probabilities
p,q is at most

$$
\sqrt2+\sqrt2\sqrt{1+4pq},\qquad p+q=1,
\tag{8}
$$

by the established rank-two seed theorem. The following H meets the norm
and every rank-two bound (8), and even has both partial traces zero, but
fails the desired all-rank entropy inequality. Its forbidden Pauli terms
are identified explicitly below.

On C^4 tensor C^4 let `Pi=sum_i |ii><ii|` and
`|Omega>=sum_i |ii>` be unnormalized. Set

$$
H=\frac{67}{21}\Pi+\frac37|\Omega\rangle\langle\Omega|
-\frac{19}{21}I_{16}.
\tag{9}
$$

Both partial traces vanish. Its eigenvalues are four on Omega/2, 16/7
on the other three maximally correlated directions, and -19/21 on the
twelve off-diagonal product directions. Thus `||H||_infinity=4`.

For a normalized bipartite vector with coefficient matrix C,

$$
\langle H\rangle=\frac{67}{21}\sum_i|C_{ii}|^2
+\frac37|\operatorname{Tr}C|^2-\frac{19}{21}.
$$

Since `sum_i |C_ii|^2<=||C||_F^2=1` and
`|Tr C|<=||C||_1=sqrt(p)+sqrt(q)` for Schmidt rank at most two,

$$
\langle H\rangle\le\frac{19}7+\frac67\sqrt{pq}.
\tag{10}
$$

Put r=2sqrt(pq), a=19/7 and b=3/7. The inequality
`a<=sqrt(2)+sqrt(2-b^2)` reduces to `185<=133 sqrt(2)`, true by squaring.
Cauchy–Schwarz then gives

$$
a+br\le\sqrt2+\sqrt2\sqrt{1+r^2}.
$$

Hence H satisfies the established rank-two spectral upper bound for all
rank-two vectors, including arbitrary complex Schmidt bases and rank-one
limits. It need not saturate that bound.

### 3.2 An exact all-rank entropy violation in this larger class

Choose `C=diag(sqrt(lambda_1),...,sqrt(lambda_4))` with Schmidt
probabilities `lambda=(9/10,1/30,1/30,1/30)`. Direct substitution gives

$$
\langle H\rangle=\frac{98+9\sqrt3}{35}.
\tag{11}
$$

Its entropy obeys

$$
S=\frac9{10}\log_2\frac{10}9+\frac1{10}\log_2 30
<\frac{13}{20},
$$

using `(10/9)^6<2` and `30<32`. The proposed affine entropy-energy bound
would therefore be strictly less than

$$
2\sqrt2+(2-\sqrt2)\frac{13}{20}
=\frac{26+27\sqrt2}{20}.
\tag{12}
$$

But (11) exceeds (12): cross multiplication reduces this to
`70+12 sqrt(3)>63 sqrt(2)`, which follows from
`sqrt(3)>5/3` and `sqrt(2)<10/7`. This is an exact positive gap,
without a numerical logarithm or optimization certificate.

### 3.3 Why this is not an interface counterexample

H is outside (7). In its trusted Pauli expansion the coefficient of
Z_1 Z_2 is

$$
\frac14\operatorname{Tr}_{B}
[(I\otimes Z_1Z_2)H]=\frac{19}{21}Z_1Z_2\ne0.
\tag{13}
$$

It is identically zero for every genuine Hamiltonian (7). The norm,
zero partial traces and complete rank-two bound cannot imply the desired
all-rank extension without using the fixed trusted-Pauli structure.
Vanishing both partial traces is an additional property of this example,
not a necessary condition asserted for every admissible Hamiltonian.

## 4. Consequence for the next proof attempt

The missing all-state theorem has not been reduced to a scalar information
budget or to interpolation of rank-two bounds. A valid argument along
these routes must retain the filtered ensemble's information distribution
or the precise trusted local-operator structure, respectively. These are
proof-method obstructions, not new physical memory bounds and not evidence
that (1) is false.

The broader bounded search inspected entropy/decision bounds and parallel
CHSH/formation routes without identifying a theorem supplying (1). This
is a search outcome, not an absence-of-prior-work claim. Both constructions
and all strict inequalities above received independent internal review.
No matrix search, numerical solver or large simulation was used; unchanged
diagnostics were not rerun. Publication novelty and unrestricted
equal-accuracy optimality remain open.
