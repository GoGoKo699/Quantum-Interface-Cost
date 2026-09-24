#!/usr/bin/env python3
"""Exact algebra supporting the finite-tail and Bayes-rank audit notes.

This checks polynomial identities, not concavity by sampled matrices and
not the unresolved uniform entropy inequality. Standard library only.
"""
from fractions import Fraction as F
import json

N = 9
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


def scale(p, factor):
    return clean({k: F(factor)*v for k, v in p.items()})


def mul(p, q):
    out = {}
    for k, v in p.items():
        for h, w in q.items():
            key = tuple(i+j for i, j in zip(k, h))
            out[key] = out.get(key, F(0)) + v*w
    return clean(out)


def square(p):
    return mul(p, p)


def derivative(p, i):
    out = {}
    for k, v in p.items():
        if k[i]:
            key = list(k)
            key[i] -= 1
            out[tuple(key)] = k[i]*v
    return clean(out)


def equal(p, q, label):
    if add(p, scale(q, -1)):
        raise RuntimeError(label)


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def main():
    # Diagonalize the Hermitian core A. C=BB^dagger has entries r,h,h*,t;
    # w denotes |h|^2, retained as an independent real polynomial symbol.
    alpha, beta, r, t, w, lam, s, z, y = [var(i) for i in range(N)]
    a, b = add(alpha, beta), mul(alpha, beta)
    c = add(r, t)
    d = add(mul(beta, r), mul(alpha, t))
    e = add(mul(r, t), scale(w, -1))
    left = add(square(lam), scale(mul(alpha, lam), -1), scale(mul(s, r), -1))
    right = add(square(lam), scale(mul(beta, lam), -1), scale(mul(s, t), -1))
    determinant = add(mul(left, right), scale(mul(square(s), w), -1))
    quartic = add(square(square(lam)), scale(mul(a, mul(square(lam), lam)), -1),
                  mul(add(b, scale(mul(s, c), -1)), square(lam)),
                  mul(mul(s, d), lam), mul(square(s), e))
    equal(determinant, quartic, 'Block characteristic polynomial')

    # Multiply the central square identity by 4z to avoid division.
    lhs = add(square(add(mul(a, z), d)),
              scale(mul(b, add(mul(c, z), square(z), e)), -4))
    rhs = add(square(add(mul(add(alpha, scale(beta, -1)), z),
                         mul(alpha, t), scale(mul(beta, r), -1))),
              scale(mul(b, w), 4))
    equal(lhs, rhs, 'D_z-b C_z square identity')

    # Independent formal variables for the Vieta discriminant.
    a, b, c, d, e, y, w, s, z = [var(i) for i in range(N)]
    discriminant = add(square(mul(mul(a, s), d)),
                       scale(mul(mul(y, square(s)),
                                 add(square(d), mul(e, square(a)), scale(mul(e, y), 4))), 4))
    factored = mul(square(s), mul(add(square(a), scale(y, 4)),
                                 add(square(d), scale(mul(e, y), 4))))
    equal(discriminant, factored, 'Vieta discriminant factorization')

    # q(s) is the radical squared in R_z. This identity proves the sign
    # of R_z'' after the analytical reduction D_z>=b C_z.
    q = add(square(add(b, scale(mul(s, c), -1))), scale(mul(s, d), 4))
    numerator = add(scale(mul(square(c), q), 4), scale(square(derivative(q, 7)), -1))
    expected = scale(mul(d, add(mul(b, c), scale(d, -1))), 16)
    equal(numerator, expected, 'Scalar-root second derivative numerator')

    # Every target label has the same incompatible strict weight tests.
    C = [[F(2-(i^j).bit_count(), 4) for j in range(4)] for i in range(4)]
    require(all(sum(C[i][j] for i in range(4)) == 1 for j in range(4)),
            'Bayes coefficient normalization')
    for target in range(4):
        n1, n2, opp = target^1, target^2, target^3
        # Let w_opp=1-w_n1-w_n2. Each comparison is an affine polynomial.
        x, y = var(0), var(1)
        weights = {n1: x, n2: y, opp: add(const(1), scale(x, -1), scale(y, -1))}
        diff1 = add(*(scale(weights[j], C[j][n1]) for j in weights), const(-C[target][n1]))
        diff2 = add(*(scale(weights[j], C[j][n2]) for j in weights), const(-C[target][n2]))
        equal(diff1, scale(add(x, scale(y, -1)), F(1, 4)), 'First strict exclusion')
        equal(diff2, scale(diff1, -1), 'Opposite strict exclusion')
        selected = [k for k in range(4) if C[target][k] > 0 and C[target][k] >= C[n1][k]]
        require(set(selected) == {target, n2}, 'Rank-two certificate attainer')

    print(json.dumps({
        'status': 'PASS',
        'arithmetic': 'exact rational sparse polynomials',
        'checks': [
            'two-by-two-block characteristic polynomial',
            'D_z-b C_z square identity, including complex off-diagonal modulus',
            'Vieta discriminant factorization',
            'scalar-root second derivative numerator',
            'Bayes coefficient normalization',
            'opposite strict weight inequalities and rank-two attainers for all four decisions'
        ],
        'scope': 'Algebra supporting supplied analytical proofs; no uniform entropy or originality certificate.'
    }, indent=2))


if __name__ == '__main__':
    main()
