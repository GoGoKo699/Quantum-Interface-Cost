#!/usr/bin/env python3
"""Exact algebra checks for the parity and mixed-decoder audit notes.

No numerical optimization, continuum spectral certificate, or novelty claim.
The analytical argument supplies the matrix reduction and root-order reasoning.
"""
from fractions import Fraction as F
from itertools import permutations
import json

# Sparse polynomials in (a,b,x,z,lambda,r), with rational coefficients.
N = 6
ZERO = (0,) * N

def clean(p):
    return {k: v for k, v in p.items() if v}

def const(v):
    return {ZERO: F(v)} if v else {}

def var(i):
    k = list(ZERO)
    k[i] = 1
    return {tuple(k): F(1)}

def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return clean(out)

def scale(p, s):
    return clean({k: F(s) * v for k, v in p.items()})

def mul(p, q):
    out = {}
    for k, v in p.items():
        for h, w in q.items():
            t = tuple(i + j for i, j in zip(k, h))
            out[t] = out.get(t, F(0)) + v * w
    return clean(out)

def square(p):
    return mul(p, p)

def reduce_square(p, index, replacement):
    out = {}
    pending = dict(p)
    while pending:
        k, v = pending.popitem()
        if k[index] < 2:
            out = add(out, {k: v})
        else:
            h = list(k)
            h[index] -= 2
            pending = add(pending, mul({tuple(h): v}, replacement))
    return out

def derivative(p, index):
    out = {}
    for k, v in p.items():
        if k[index]:
            h = list(k)
            h[index] -= 1
            out[tuple(h)] = k[index] * v
    return clean(out)

def determinant(matrix):
    out = {}
    for p in permutations(range(4)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        term = const(sign)
        for i in range(4):
            term = mul(term, matrix[i][p[i]])
        out = add(out, term)
    return out

def require_zero(p, message):
    if clean(p):
        raise RuntimeError(message)

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

a, b, x, z, lam, r = [var(i) for i in range(N)]
a2, b2, x2, r2 = map(square, (a, b, x, r))
one, two = const(1), const(2)
ab, ax, bz = mul(a, b), mul(a, x), mul(b, z)

# Independently expand det(lambda I-K4) directly from its four rows.
diag = [add(ab, a, b), add(scale(ab, -1), a, scale(b, -1)),
        add(scale(ab, -1), scale(a, -1), b), add(ab, scale(a, -1), scale(b, -1))]
M = [[{} for _ in range(4)] for _ in range(4)]
for i in range(4):
    M[i][i] = add(lam, scale(diag[i], -1))
for i, j, value in [(0, 1, bz), (2, 3, scale(bz, -1)), (0, 2, ax), (1, 3, ax)]:
    M[i][j] = M[j][i] = scale(value, -1)

h = add(square(lam), scale(mul(a2, add(one, b2)), -1), mul(add(b2, scale(a2, -1)), x2))
D = add(square(h), scale(mul(b2, square(add(lam, a2))), -4),
        scale(mul(mul(b2, add(b2, scale(a2, -1))), add(one, scale(x2, -1))), 4))
require_zero(reduce_square(add(determinant(M), scale(D, -1)), 3, add(one, scale(x2, -1))),
             'Characteristic polynomial identity failed')

# d/dx D(lambda,x^2)=4x(b^2-a^2)(h-2b^2).
require_zero(add(derivative(D, 2), scale(mul(mul(x, add(b2, scale(a2, -1))), add(h, scale(b2, -2))), -4)),
             'Orientation derivative identity failed')

# At lambda0=a+br, r^2=a^2+2a+2, the residual is 2ab(r+b).
lam0 = add(a, mul(b, r))
residual = add(square(lam0), scale(mul(a2, add(one, b2)), -1), scale(b2, -2),
               scale(mul(ab, add(r, b)), -2))
require_zero(reduce_square(residual, 5, add(a2, scale(a, 2), two)),
             'Endpoint residual identity failed')

# Weighted Cauchy and the uniform constant are separate exact identities.
cauchy_gap = add(scale(b2, 3), scale(r2, F(3, 2)), scale(square(add(b, r)), -1),
                  scale(square(add(r, scale(b, -2))), F(-1, 2)))
require_zero(cauchy_gap, 'Weighted Cauchy square decomposition failed')
upper = add(scale(b2, 3), scale(r2, F(3, 2)), const(F(-21, 2)),
            scale(square(add(a, const(-1))), F(3, 2)))
upper = reduce_square(upper, 1, add(two, scale(a2, -1)))
upper = reduce_square(upper, 5, add(a2, scale(a, 2), two))
require_zero(upper, 'Uniform scalar majorant identity failed')
require(F(21, 2) < F(13, 4) ** 2 < F(10, 3) ** 2, 'Threshold ordering failed')
# Equality in the final majorant forces a=b=1; Cauchy equality then
# requires r^2=4, whereas r^2=a^2+2a+2=5.
require(F(4) != F(5), 'Strictness incompatibility failed')

# Binary symmetry witness in its local two-dimensional Pauli algebra.
# Here a,b denote longitudinal/transverse coefficients with a^2+b^2=1;
# this separate check does not use the decoder relation a^2+b^2=2.
def mm(A, B):
    return [[add(*(mul(A[i][k], B[k][j]) for k in range(2)))
             for j in range(2)] for i in range(2)]

U = [[a, b], [b, scale(a, -1)]]
W = [[b, scale(a, -1)], [scale(a, -1), scale(b, -1)]]
W2, UWU = mm(W, W), mm(mm(U, W), U)
for i in range(2):
    for j in range(2):
        require_zero(reduce_square(add(W2[i][j], const(-int(i == j))),
                                   1, add(one, scale(a2, -1))), 'Witness reflection')
        require_zero(reduce_square(add(UWU[i][j], W[i][j]),
                                   1, add(one, scale(a2, -1))), 'Swapped witness outcomes')

require(5**15 > 2**34, 'Binary entropy lower bound')
require(F(7, 5)**2 < 2 < F(3, 2)**2, 'Square-root comparisons')
require(4*F(66, 29) < F(61, 20)**2, 'Parity score upper bound')
margin = F(14, 5)+F(28, 87)-F(61, 20)
require(margin == F(25, 348) > F(1, 16), 'Parity entropy margin')
require(F(64, 7) < F(16, 5)**2 and 82 > 9**2,
        'Parity support-function comparison')

print(json.dumps({
    'status': 'passed',
    'arithmetic': 'exact rational sparse polynomials',
    'checks': [
        'four-by-four characteristic polynomial (24-permutation determinant)',
        'orientation derivative',
        'principal-axis endpoint residual',
        'weighted-Cauchy square decomposition',
        'uniform scalar majorant and strictness',
        '21/2 < (13/4)^2 < (10/3)^2',
        'binary symmetry witness reflection and sign flip',
        'parity entropy and support-function rational comparisons'
    ],
    'parity_residual_strip_margin': str(margin),
    'scope': 'Algebra supporting the supplied restricted proofs; does not certify unrestricted optimality or publication novelty.'
}, indent=2))
