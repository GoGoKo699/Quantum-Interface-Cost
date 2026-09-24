#!/usr/bin/env python3
"""Exact scalar certificate for EXTENDED_CORE_TRANSFER.md, Section 6.

No state sampling or floating-point acceptance. The analytical reduction,
including monotonicity, is supplied in the report, not proved by this script.
Run from any directory with Python 3.10+. Standard library only.
"""
import json

from certify_two_qubit_core import I, SCALE, rat, SQ2, positive_part


def check(ml, mh):
    m = I(ml, mh)
    r = 1 - 2*m
    excess = SQ2 + (4 - 2*r.square()).sqrt() - rat(13, 4)
    if excess.hi <= 0:
        return 'empty', None, None
    # No high-score core exists where excess<0. Its positive part safely
    # extends the upper-bound calculation to the full interval.
    excess = positive_part(excess)
    kappa = (1-m)/m
    b = 2*SQ2 + 2*SQ2*kappa/(2*SQ2*kappa+1)
    u = excess/(m*b)
    if u.hi >= rat(1, 10).lo:
        return 'split', None, None
    # J is increasing on [0,1/10]; the inverse square root also increases.
    v = I(u.hi, u.hi)
    slope = SQ2*(14-32*v+16*v.square())/(1-8*v+8*v.square())
    active = 8*kappa.sqrt()/(1-4*v).sqrt()
    constant = (slope+active)/(m*b)
    if constant.hi >= 49*SCALE:
        return 'split', None, None
    return 'pass', rat(1, 10).lo-u.hi, 49*SCALE-constant.hi


def main():
    todo = [(rat(7, 32).lo, rat(1, 2).hi, 0)]
    counts = {'pass': 0, 'empty': 0}
    maxdepth = 0
    min_angle = None
    min_constant = None
    while todo:
        ml, mh, depth = todo.pop()
        status, angle, constant = check(ml, mh)
        maxdepth = max(maxdepth, depth)
        if status != 'split':
            if status not in counts:
                raise RuntimeError('Unknown interval status')
            counts[status] += 1
            if angle is not None:
                min_angle = angle if min_angle is None else min(angle, min_angle)
                min_constant = constant if min_constant is None else min(constant, min_constant)
            continue
        if depth >= 24:
            raise RuntimeError(('Unresolved interval', ml, mh, depth))
        mid = (ml+mh)//2
        if not ml < mid < mh:
            raise RuntimeError('Subdivision exhausted')
        # Closed children cover the whole parent, including the midpoint.
        todo.extend([(mid, mh, depth+1), (ml, mid, depth+1)])
    if not counts['pass'] or min_angle <= 0 or min_constant <= 0:
        raise RuntimeError('No strictly positive certificate')
    print(json.dumps({
        'certificate': 'PASS',
        'arithmetic': 'integer endpoints / 2**80, outward rounded',
        'domain': {'m': ['7/32', '1/2']},
        'claims': ['U(m)<1/10', 'C(m)<49'],
        'leaf_counts': counts,
        'maximum_depth': maxdepth,
        'minimum_angle_margin_numerator': min_angle,
        'minimum_constant_margin_numerator': min_constant,
        'margin_denominator': SCALE,
        'scope': 'Scalar inequalities conditional on the supplied analytical reduction; not unrestricted optimality or novelty.'
    }, indent=2))


if __name__ == '__main__':
    main()
