"""Verify exact identities in docs/audits/SHARP_SUBSPACE_AND_FLAT_CORE.md.

This checks algebraic proof ingredients, not unrestricted optimality or novelty.
"""
from fractions import Fraction as F
from math import comb, factorial
import json

def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a

def add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])

def scale(a, c):
    return trim([c*x for x in a])

def mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)

def power(a, n):
    ans = [F(1)]
    for _ in range(n):
        ans = mul(ans, a)
    return ans

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def bernstein(weights, denominator):
    degree = len(weights)-1
    ans = [F(0)]
    for k, w in enumerate(weights):
        basis = mul([F(0)]*k+[F(comb(degree,k))], power([F(1),F(-1)], degree-k))
        ans = add(ans, scale(basis, F(w, denominator)))
    return ans

c, r, D, E = F(7,20), F(7,8), F(299,80), F(45,16)
phi, psi = [c*r*r, 1-2*c*r, c], [D, F(0), -E]
q0 = add(mul(phi,phi), [F(0),F(0),F(-1)])
q1 = add(scale(mul(phi,psi),2), [F(-4),F(0),F(2)])
q2 = add(mul(psi,psi), [F(0),F(0),F(-1)])
b1 = add(q0, scale(q1,F(1,28)))
b2 = add(add(q0,scale(q1,F(1,14))),scale(q2,F(1,196)))
q0_factored = mul(scale(power([-r,F(1)],2), c), add([F(0),F(2)],scale(power([-r,F(1)],2),c)))
require(q0 == q0_factored, 'Q0 square identity')
p = [16797,2692965,2208145,225921,205461]
q = [105747,33423588,55698550,61633548]
require(all(v>0 for v in p+q), 'positive Bernstein integers')
require(b1 == bernstein(p,34406400), 'B1 identity')
require(b2 == add(mul([F(1),F(-1)],bernstein(q,240844800)),[F(0)]*4+[F(2743,11468800)]), 'B2 identity')
require(D-E>0 and 1-2*c*r>0, 'majorant and score coefficient signs')
require(14*c-F(3,2)*E == F(109,160), 'second-moment coefficient')
U = 4*c*r*r+F(10,3)*(1-2*c*r)+3*c
V = 4*D-3*E-U
require(U==F(3277,960) and V==F(595,192), 'summed affine bound')
require(140**2 < 2*99**2 and U < 2+F(140,99), 'zero entropy endpoint')
require(29**7 > 2**34, 'base-two logarithm bound')
require(sum(F(7,10)**j/factorial(j) for j in range(5)) == F(482921,240000)>2, 'natural logarithm bound')
x = F(1,29)
h_low = F(34,7)*x+F(10,7)*(1-x)*(x+x*x/2)
K = 1-x+h_low
margin = 2*K+(2-K)*F(140,99)-(U+V*x)
require(2-K>0 and margin==F(151,23312520)>0, 'positive entropy endpoint')
print(json.dumps({
    'status': 'pass', 'arithmetic': 'exact rational',
    'positive_bernstein_coefficients': len(p)+len(q),
    'interval_partitions': 0, 'affine_intercept': str(U),
    'affine_slope': str(V), 'entropy_endpoint_margin': str(margin),
    'scope': 'scalar identities and endpoints; analytical reductions required',
}, indent=2))
