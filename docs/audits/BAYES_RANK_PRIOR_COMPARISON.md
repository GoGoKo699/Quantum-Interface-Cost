# The 2012 Bayes-rank theorem: a completed scoped comparison

Date: 2026-09-24. Reviewed main:
`3964f9b97766463a2aff65233560c9dcdf60c297` (PR #26).
Reviewed tree: `0bdb23c6045674fc4d0c2b18d5119e095d531196`.

**Finding:** the previously unread Nakahira–Usuda theorem is now read.
Under the natural reduction of our two-bit Hamming score, its complete
weighted rank-certificate family gives exactly rank at most two. It does
not directly imply our rank-one projectivity theorem. This closes one
specified source gap, not the exhaustive originality question. The
Tomassoli full-text comparison remains open and is a useful human-access
request.

**Subsequent full-text follow-up, 24 September 2026:** the user supplied
the requested PDF. The [completed thesis comparison](TOMASSOLI_FULL_TEXT_COMPARISON.md)
closes that request and credits the overlapping calibrated boundary and
axis family. The access status below is historical to this report's base.

## 1. Primary theorem and assumptions

Kenji Nakahira and Tsuyoshi Sasaki Usuda, *Minimum-Bayes-cost
discrimination for symmetric quantum states*, Physical Review A **86**,
062305 (2012), published 6 December 2012,
[DOI](https://doi.org/10.1103/PhysRevA.86.062305).
The eight-page primary PDF was retrieved from the official public
[APS endpoint](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevA.86.062305/fulltext)
and its rank theorem and proof were read. The paper is not redistributed.

Theorem 2, Eqs. (8)–(9), printed p. 062305-2, considers prior-weighted
positive hypotheses `rho_t`, nonnegative coefficients `C_st`, and the
minimum-error ensemble `sigma_s=sum_t C_st rho_t` obtained from a Bayes
problem. For each decision s it bounds an optimal effect E_s by the rank
of a selected sum of original hypotheses. The explicitly weighted
extension, Eq. (14), printed p. 062305-3, allows every probability vector
`w_j` on competing decisions `j!=s`:

$$
T_s(w)=\{t:C_{st}>0,\ C_{st}\ge\sum_{j\ne s}w_jC_{jt}\},\qquad
\operatorname{rank}E_s\le
\operatorname{rank}\sum_{t\in T_s(w)}C_{st}\rho_t.
\tag{1}
$$

The proof transfers a small positive rank-one contribution between POVM
effects and uses a kernel-dimension contradiction. This rank theorem
does **not** require ensemble symmetry. Corollary 3 adds strict cyclic
coefficient conditions; Section IV's closed-form measurements separately
require geometrically uniform or cyclic ensembles.

## 2. Apply the full weighted family, not just one choice

Fix one joint two-input context and `rho>0`. In its four-vector product
basis use the prior-weighted hypotheses

$$
\rho_t=\sqrt\rho\,|t\rangle\langle t|\sqrt\rho,
\quad t\in\{00,01,10,11\}.
$$

All have positive trace, their traces sum to one, and their four defining
vectors are linearly independent. The reward in the
[joint-decoder theorem](RESOURCE_OPTIMA_AND_JOINT_DECODERS.md), Section 4,
is `1-d_H(s,t)`. Minimizing Hamming distance is equivalent. Remark 1,
Eqs. (4)–(6), printed p. 062305-2, therefore gives

$$
C_{st}=\frac{2-d_H(s,t)}4,
\qquad
4C=\begin{pmatrix}
2&1&1&0\\1&2&0&1\\1&0&2&1\\0&1&1&2
\end{pmatrix}.
\tag{2}
$$

Each unnormalized coefficient column sums to four, so the source's
normalization is precisely `1/4`. Equivalently
`sigma_s=[rho+sqrt(rho)(Pi_s-Pi_-s)sqrt(rho)]/4`.

For `s=00`, the hypothesis `00` always belongs to `T_00(w)`, and `11`
never belongs because its coefficient is zero. Excluding `01` requires

$$
1<2w_{01}+w_{11}=1+w_{01}-w_{10},
$$

whereas excluding `10` requires

$$
1<2w_{10}+w_{11}=1+w_{10}-w_{01}.
$$

These are incompatible strict inequalities. At least one neighbor stays
in the selected set. Taking `w_01=1` gives exactly `T_00={00,10}`.
Every positive selected sum has rank equal to its number of terms,
because the four hypotheses are linearly independent. By symmetry the
best bound from (1), for every effect, is **rank at most two**.

Our supplied theorem instead proves that every optimum is rank one and
projective for full-rank rho. Thus (1), including its entire weighted
extension, does not directly subsume that conclusion under this reduction.
This does not rule out a different ensemble decomposition or a further
deduction from the source's proof machinery.

Common column offsets cannot help this particular family: they cancel
from the comparison with the weighted average. Nonnegativity forces each
offset to be nonnegative because each original column has a zero entry;
the target and neighbor coefficients therefore remain positive.

In cyclic Gray order `00,01,11,10`, the coefficient sequence is
`(2,1,0,1)/4`. Corollary 3's strict convexity condition fails by equality
`1=(2+0)/2` at both neighbors, and the strict decreasing condition also
fails. A general full-rank correlated seed need not be a symmetric
ensemble, so Section IV cannot be assumed applicable.

## 3. The remaining human-access request

**Resolved by the user's upload:** see the full-text follow-up above.
The following records the request that led to that source becoming
available, rather than a current request to upload it again.

Giacomo Tomassoli, *Certificatori di Entanglement per due qubit con due
correlatori*, Università degli Studi di Padova, bachelor's thesis,
academic year 2024/25, supervisor Pietro Silvi:
[institutional record](https://hdl.handle.net/20.500.12608/84769).
The catalogue's English title is *Quantitative Entanglement Witness for
two qubit with two correlators*. The previously retrieved deposit metadata
dates it to 14 April 2025 and advertises an open-access PDF of about 3 MB.

The advertised [PDF](https://thesis.unipd.it/bitstream/20.500.12608/84769/1/Tomassoli_Giacomo.pdf.pdf)
returned HTTP 403 in earlier ordinary retrieval attempts. Its mathematical
contents remain unread. A bounded search found no usable alternate primary
full text; no author was contacted and no access restriction was bypassed.

**Useful human help:** upload that PDF if it opens in the user's browser.
We need its precise entanglement measure, correlator calibration, dimension
assumptions, optimization/convexification and equality constructions.
The relevant page numbers are unknown because the source is unread.

Its two-qubit metadata neither establishes nor excludes overlap with the
full two-parameter formation evaluation. It is not an identified solution
of the all-n interface conjecture. Reading it would resolve a specific
comparison, not prove exhaustive originality by itself.

## 4. Scope and verification

The normalization, complete weight-simplex obstruction, endpoint attainer
for the rank-two certificate, and strict-condition failure were independently
reconstructed within this workspace. No numerical search is used in the
argument. The exact algebra checker accompanying the
[finite-tail note](FINITE_TAIL_STRUCTURE.md) also verifies the coefficient
identities and the four symmetric target cases.

The original task retains one unknown specimen, a single delayed local
query, unrestricted collective encoders, unlimited finite classical
records, worst-case quantum dimension and uniform input/query error.
The joint context here is an auxiliary weaker problem; it is not substituted
for the operational local-query task. No new entropy converse or publication
originality claim follows from this source comparison.
