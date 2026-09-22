# Literature comparison and audit queue

Updated: 2026-09-22. This is a starting ledger, not a completed novelty audit.
The baseline's references and locator claims are inherited from v0.1. During
bootstrap the primary abstract/metadata records below were rechecked; this
does not independently verify every equation locator or theorem application.
The audit workspace must open the full primary sources and record versions.

## Direct framework precedents

**Marie Ioannou et al., Simulability of high-dimensional quantum measurements**,
PRL 129, 190401 (2022), [arXiv:2202.12980](https://arxiv.org/abs/2202.12980).
The arbitrary-state, instrument-compression, later-measurement framework is
already here. Classical simulation is joint measurability. Audit the exact
scenario and simulation constructions, including its MUB examples, before
claiming a gap. The current workload is 2n local binary observables, not two
full 2^n-outcome measurements.

**Benjamin D. M. Jones et al., Equivalence between simulability of
high-dimensional measurements and high-dimensional steering**, PRA 107,
052425 (2023), [arXiv:2207.04080](https://arxiv.org/abs/2207.04080).
This is a direct precedent for dimensional steering/simulability connections.
Check Theorems 1–2 and dimension-witness sections against the seed reduction.
A Choi-state or steering reformulation alone is not the intended contribution.

**Andreas Bluhm, Lukas Rauber, Michael M. Wolf, Quantum compression relative
to a set of measurements**, [arXiv:1708.04898](https://arxiv.org/abs/1708.04898).
Compare its reconstruction requirements with our separately chosen binary
decoders. Do not assume either equivalence or non-equivalence from titles.

## Ingredients, not novelty claims

**Berta et al., The Uncertainty Principle in the Presence of Quantum Memory**,
Nature Physics 6, 659–662 (2010),
[arXiv:0909.0950](https://arxiv.org/abs/0909.0950).
Note Section 5 uses the quantum conditional-entropy relation and Fano's
inequality. Recheck bases, logarithms, error quantifiers, and cq conditioning.

**Brandao, Christandl, Yard, Faithful Squashed Entanglement**,
[arXiv:1010.1750v5](https://arxiv.org/abs/1010.1750v5), with the
[published erratum](https://doi.org/10.1007/s00220-012-1584-y).
The corrected theorem uses one-way LOCC, not the originally claimed full-LOCC
norm. Recheck Corollary 1, norm normalization, direction, and the coefficient
1/(16 ln 2). Note Section 6 also needs monogamy and a dimension bound with a
free classical flag.

**Christandl and Winter, Squashed Entanglement — An Additive Entanglement
Measure**, [quant-ph/0308088](https://arxiv.org/abs/quant-ph/0308088).
Use for definitions and properties, not as certification of our application.

## High-priority possible subsumption

**Devetak and Berger, Quantum Rate-Distortion Theory for I.I.D. Sources**,
[quant-ph/0011085v3](https://arxiv.org/abs/quant-ph/0011085v3).
Its abstract reports an exact rate for isotropic qubit sources with unrestricted
classical side information and entanglement-fidelity distortion. This is a
serious potential comparison, not a citation to wave away. Determine whether
source averaging, reconstruction, and distortion can be translated to our
uniform arbitrary-state readout task. Present a reduction or an explicit
obstruction. Full theorem-level translation remains pending.

Also search bounded/noisy quantum storage, BB84/postmeasurement information,
quantum random-access encodings, dimension-bounded steering, tensorization,
and measurement-compression rate problems. Treat an existing theorem that
settles the question as a useful research finding, not a reason to conceal it.

## Controls and neighboring tasks

Huang, Kueng, Preskill, [arXiv:2002.08953](https://arxiv.org/abs/2002.08953),
and Chen, Gong, Ye, [arXiv:2404.19105](https://arxiv.org/abs/2404.19105),
concern repeated measurement data and Pauli estimation. Our Section 9 derives
its special estimator directly. Do not import many-copy sample lower bounds
into a one-specimen interface claim, or the converse.

## Required format for completed comparisons

For each closest source record: exact version; theorem/equation/page; source
assumptions; our assumptions; resource accounting; quantifiers and error
metric; a reduction, corollary, obstruction, or unresolved step; and the
resulting novelty implication. Abstract-level resemblance is not a proof of
subsumption. Failure to find a result is not proof of absence.
