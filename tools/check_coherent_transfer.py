"""Check the exact obstruction in docs/audits/COHERENT_TRANSFER_AUDIT.md.

This verifies a physical counterexample and conditional algebra, not the
unproved support-function target, unrestricted optimality, or originality.
"""
from fractions import Fraction as F
from math import factorial
import json

# Q(sqrt(2), sqrt(3), sqrt(7)); a mask identifies a product of roots.
class K:
    def __init__(self, value=0, mask=0):
        self.c = [F(0)] * 8
        self.c[mask] = F(value)
    def __add__(self, other):
        other = other if isinstance(other, K) else K(other)
        out = K()
        out.c = [a+b for a,b in zip(self.c, other.c)]
        return out
    __radd__ = __add__
    def __neg__(self):
        out = K()
        out.c = [-a for a in self.c]
        return out
    def __sub__(self, other):
        return self + (-other if isinstance(other, K) else K(-other))
    def __mul__(self, other):
        other = other if isinstance(other, K) else K(other)
        out = K()
        for i,a in enumerate(self.c):
            for j,b in enumerate(other.c):
                factor = 1
                for bit,radicand in enumerate([2,3,7]):
                    if (i & j) & (1 << bit):
                        factor *= radicand
                out.c[i ^ j] += a*b*factor
        return out
    __rmul__ = __mul__
    def __eq__(self, other):
        other = other if isinstance(other, K) else K(other)
        return self.c == other.c

def require(condition, label):
    if not condition:
        raise RuntimeError(label)

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

r2,r3,r7 = K(1,1),K(1,2),K(1,4)
h = K(F(1,2))
e1 = [r2*h,0,0,r2*h]
e2 = [0,r2*h,-r2*h,0]
e3 = [h,h,h,-h]
v = [h,-h,-h,-h]
frame = [e1,e2,e3,v]
require(all(dot(x,y) == (i==j) for i,x in enumerate(frame)
            for j,y in enumerate(frame)), 'four-vector physical frame')
u = [(e2[i]+e3[i])*r2*h for i in range(4)]
basis = [u,e1,v]
require(all(dot(x,y) == (i==j) for i,x in enumerate(basis)
            for j,y in enumerate(basis)), 'physical orthonormality')
ops = [lambda x:[x[2],x[3],x[0],x[1]],
       lambda x:[x[0],x[1],-x[2],-x[3]],
       lambda x:[x[1],x[0],x[3],x[2]],
       lambda x:[x[0],-x[1],x[2],-x[3]]]
physical = [[[dot(x,op(y)) for y in basis] for x in basis] for op in ops]
expected = [[-r2*h,h,-h],[h,K(),-r2*h],[-h,-r2*h,K()]]
require(physical[0] == expected, 'X_A compression')
signs = [(1,[1,1,1]),(-1,[1,-1,-1]),(-1,[1,-1,1]),(1,[1,1,-1])]
w = [F(1,3), F(2,3), F(-2,3)]
require(dot(w,w) == 1, 'Householder normalization')
raw = [[2*w[i]*w[j]-(i==j) for j in range(3)] for i in range(3)]
decoders = []
for matrix,(sgn,s) in zip(physical,signs):
    require(all(matrix[i][j] == sgn*s[i]*s[j]*expected[i][j]
                for i in range(3) for j in range(3)), 'signed physical conjugation')
    decoder = [[sgn*s[i]*s[j]*raw[i][j] for j in range(3)] for i in range(3)]
    require(all(sum(decoder[i][k]*decoder[k][j] for k in range(3)) == (i==j)
                for i in range(3) for j in range(3)), 'decoder involution')
    decoders.append(decoder)

amp = [r3*h,h]
a = sum(sum(amp[i]*amp[j]*matrix[i][j]*decoder[i][j]
            for i in range(2) for j in range(2))
        for matrix,decoder in zip(physical,decoders))
b = sum(sum(amp[i]*matrix[i][2]*decoder[i][2] for i in range(2))
        for matrix,decoder in zip(physical,decoders))
require(a == F(7,6)*r2+F(4,9)*r3, 'core expectation')
require(b == F(4,9)*r3+F(8,9)*r2, 'cross amplitude')
d = r2+F(1,2)*r2*r7-a
require(d == F(1,2)*r2*r7-F(1,6)*r2-F(4,9)*r3, 'deficit')
residual = b*b-2*r2*d-2*d*d
require(residual == F(1,81)*(-442+112*r2*r3-108*r7+72*r2*r3*r7),
        'radical residual')
require(F(12,5)**2 < 6 and F(8,3)**2 > 7 and F(97,15)**2 < 42,
        'radical comparison premises')
lower = F(1,81)*(-442+112*F(12,5)-108*F(8,3)+72*F(97,15))
require(lower == F(22,405) > 0, 'positive residual certificate')
require(F(173,100)**2 < 3 and F(141,100)**2 < 2 and F(749,200)**2 > 14,
        'b and d comparison premises')
require(F(1,9)*(4*F(173,100)+8*F(141,100)) == F(91,45) > 2,
        'b exceeds two')
require(F(749,400)-F(141,600)-F(173,225) == F(3127,3600) < F(87,100),
        'd less than 87/100')
require(F(7,2)**2 < 14 and F(3,2)**2 > 2 and 2**2 > 3,
        'positive d comparison premises')
require(F(7,4)-F(1,4)-F(8,9) == F(11,18) > 0, 'positive d')
require(F(283,200)**2 > 2 and 3*F(87,100) < 4, 'linear shortcut failure')
require(2*F(283,200)*F(87,100)+2*F(87,100)**2 == F(39759,10000) < 4,
        'both quadratic shortcuts fail')

# The entropy implication is conditional on the unproved support-function bound.
require(F(13,20)**2 < F(3,7), 'gain square-root comparison')
require(6/(1+F(13,20)) == F(40,11), 'conditional gain coefficient')
require(29**7 > 2**34, 'base-two logarithm certificate')
require(sum(F(7,10)**j/factorial(j) for j in range(5)) == F(482921,240000) > 2,
        'natural-logarithm certificate')
require(F(34,7)+F(280,203) == F(1266,203), 'entropy-ratio lower bound')
require(F(99,70)**2 > 2 and 2-F(99,70) == F(41,70), 'entropy coefficient')
require(F(41,70)*F(1266,203) > F(73,20), 'conditional entropy coefficient')
require(F(73,20)-F(40,11) == F(3,220) > 0, 'conditional entropy margin')
print(json.dumps({
    'status': 'pass', 'arithmetic': 'exact multiquadratic and rational',
    'physical_signed_conjugations': 4, 'decoder_involutions': 4,
    'core_parameter_m': '1/4', 'refuted_intermediate_bounds': 3,
    'quadratic_residual_lower_bound': str(lower),
    'conditional_entropy_margin_coefficient': '3/220',
    'scope': 'physical counterexample and conditional algebra; no proof of the support-function target',
}, indent=2))
