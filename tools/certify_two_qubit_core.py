#!/usr/bin/env python3
"""Exact rational interval certificate for the remaining high-score bridge.
All intervals have endpoints integers / 2**BITS. No float arithmetic is used.
The mathematical reduction and domain are proved in
docs/audits/TWO_QUBIT_CORE_STABILITY.md. This certificate verifies that scalar
reduction; it does not prove unrestricted two-qubit or all-n optimality.
"""
from dataclasses import dataclass
from functools import lru_cache
from math import isqrt
import json

BITS = 80
SCALE = 1 << BITS
LOG_TERMS = 72

def ceildiv(a, b):
    if b <= 0:
        raise ValueError('positive denominator required')
    return -((-a)//b)

@dataclass(frozen=True)
class I:
    lo: int
    hi: int
    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError('reversed interval')
    def __add__(self, x):
        x = lift(x)
        return I(self.lo+x.lo, self.hi+x.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi,-self.lo)
    def __sub__(self,x):
        return self+-lift(x)
    def __rsub__(self,x):
        return lift(x)+-self
    def __mul__(self,x):
        x=lift(x)
        v=[self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi]
        return I(min(v)//SCALE,ceildiv(max(v),SCALE))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=lift(x)
        if x.lo <= 0:
            raise ValueError('denominator not strictly positive')
        vals=[(self.lo*SCALE,x.lo),(self.lo*SCALE,x.hi),
              (self.hi*SCALE,x.lo),(self.hi*SCALE,x.hi)]
        return I(min(a//b for a,b in vals),max(ceildiv(a,b) for a,b in vals))
    def __rtruediv__(self,x):
        return lift(x)/self
    def sqrt(self):
        if self.lo < 0:
            raise ValueError('negative radicand')
        l=isqrt(self.lo*SCALE)
        h=isqrt(self.hi*SCALE)
        if h*h < self.hi*SCALE:
            h+=1
        return I(l,h)
    def square(self):
        lo=0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        hi=max(self.lo*self.lo,self.hi*self.hi)
        return I(lo//SCALE,ceildiv(hi,SCALE))

def lift(x):
    if isinstance(x,I):
        return x
    if not isinstance(x,int):
        raise TypeError('only integer constants are permitted')
    return I(x*SCALE,x*SCALE)

def rat(n,d=1):
    return I(n*SCALE//d,ceildiv(n*SCALE,d))

def positive_part(x):
    return I(max(0,x.lo),max(0,x.hi))

def interval_min(x,y):
    return I(min(x.lo,y.lo),min(x.hi,y.hi))

def log_core(x):
    """Enclose ln x for a positive interval lying in [1,2]."""
    if x.lo < SCALE or x.hi > 2*SCALE:
        raise ValueError('log range reduction failed')
    z=(x-1)/(x+1)
    z2=z.square()
    p=z
    acc=lift(0)
    for j in range(LOG_TERMS):
        acc=acc+p/(2*j+1)
        p=p*z2
    # At this point p encloses z**(2*N+1).  All omitted terms are positive,
    # and their sum is <= p/[(2*N+1)(1-z*z)].
    rem=p/((2*LOG_TERMS+1)*(1-z2))
    return I(2*acc.lo,2*acc.hi+2*rem.hi)

LN2=log_core(lift(2))

@lru_cache(maxsize=None)
def log_endpoint(n):
    if n <= 0:
        raise ValueError('log endpoint must be positive')
    k=n.bit_length()-1-BITS
    if k>=0:
        y=I(n//(1<<k),ceildiv(n,1<<k))
    else:
        y=I(n<<(-k),n<<(-k))
    if y.lo < SCALE or y.hi > 2*SCALE:
        raise ValueError('invalid reduced endpoint')
    return log_core(y)+k*LN2

@lru_cache(maxsize=None)
def entropy_endpoint(n):
    if not 0<n<SCALE:
        raise ValueError('entropy endpoint outside (0,1)')
    x=I(n,n)
    return (-x*log_endpoint(n)-(1-x)*log_endpoint(SCALE-n))/LN2

def entropy_increasing(x):
    if not 0<x.lo<=x.hi<=SCALE//2:
        raise ValueError('binary entropy monotonic domain failed')
    return I(entropy_endpoint(x.lo).lo,entropy_endpoint(x.hi).hi)

SQ2=lift(2).sqrt()
C=2-SQ2
SQ5=lift(5).sqrt()
ZERO=lift(0)

# Return (status, exact lower margin numerator, auxiliary values).
def check_box(el,eh,ml,mh):
    e=I(el,eh);m=I(ml,mh)
    r=1-2*m
    g=(4-2*r.square()).sqrt()
    dm=SQ2+g-rat(10,3)
    if dm.hi<=0:
        return 'no_high_score',None,None
    he=entropy_increasing(e)
    hm=entropy_increasing(m)
    a0=4-(1-2*e).square()
    z=(1-e)*r.square()
    rad=a0-z
    if rad.lo<=0:
        return 'split',None,None
    D=2*rad.sqrt()-(2+SQ2)-C*he+C*(1-e)*(1-hm)+e*positive_part(C-1/a0.sqrt())
    if D.hi<0:
        return 'sld_excluded',None,None
    t=((1-m)/m).sqrt()
    bstar=SQ5*t/m
    c1=9/m
    c2=(29+4*SQ5*t)/(rat(7,2)*m)
    denominator=c2-c1
    if denominator.lo<=0:
        return 'split',None,None
    lspec=2-g
    # Known analytic nonnegativity permits these intersections.
    dm=positive_part(dm)
    delta=positive_part(2*SQ2+C*hm-(SQ2+g))
    b=bstar*lspec
    dstar=b/denominator
    ell_end=2*e*interval_min(c1*dm+b,c2*dm)-(1-e)*dm
    loss_hi=max(0,ell_end.hi)
    if dstar.lo<=dm.hi:
        relevant_star=I(max(0,dstar.lo),min(dstar.hi,dm.hi))
        ell_star=(2*e*c2-1+e)*relevant_star
        loss_hi=max(loss_hi,ell_star.hi)
    left=C*he-2*SQ2*e+(1-e)*delta
    margin=left.lo-loss_hi
    if margin>0:
        return 'bridge_certified',margin,None
    return 'split',margin,None

def main():
    # The box encloses the closed rational rectangle.  m>=9/20 is handled
    # by the separate elementary proof, epsilon<=1/100 likewise.
    initial=(rat(1,100).lo,rat(1,29).hi,rat(3,10).lo,rat(9,20).hi,0)
    todo=[initial]
    counts={'no_high_score':0,'sld_excluded':0,'bridge_certified':0}
    split_count=0
    smallest_margin=None
    maximum_depth=0
    while todo:
        el,eh,ml,mh,depth=todo.pop()
        maximum_depth=max(maximum_depth,depth)
        status,margin,_=check_box(el,eh,ml,mh)
        if status!='split':
            counts[status]+=1
            if margin is not None:
                smallest_margin=margin if smallest_margin is None else min(smallest_margin,margin)
            continue
        if depth>=42:
            raise RuntimeError('unresolved interval box '+repr((el,eh,ml,mh,margin)))
        split_count+=1
        # Compare widths after scaling each original coordinate range.
        # Integer-only comparison keeps the traversal deterministic.
        if (eh-el)*(initial[3]-initial[2]) >= (mh-ml)*(initial[1]-initial[0]):
            mid=(el+eh)//2
            if not el<mid<eh: raise RuntimeError('epsilon subdivision exhausted')
            todo.append((mid,eh,ml,mh,depth+1))
            todo.append((el,mid,ml,mh,depth+1))
        else:
            mid=(ml+mh)//2
            if not ml<mid<mh: raise RuntimeError('m subdivision exhausted')
            todo.append((el,eh,mid,mh,depth+1))
            todo.append((el,eh,ml,mid,depth+1))
    result={'certificate':'PASS','arithmetic':'integer endpoints / 2**80, outward rounded',
            'bits':BITS,'log_terms':LOG_TERMS,'leaf_counts':counts,
            'split_count':split_count,'maximum_depth':maximum_depth,
            'minimum_positive_margin_numerator':smallest_margin,
            'margin_denominator':SCALE,
            'domain':{'epsilon':['1/100','1/29'],'m':['3/10','9/20']}}
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
