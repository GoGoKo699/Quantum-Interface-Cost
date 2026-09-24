#!/usr/bin/env python3
"""Exact scalar certificate for the curved high-score core transfer gate.

Conditional on the analytical reductions in
docs/audits/CURVED_CORE_TRANSFER.md, certify the entire closed four-variable
domain recorded in the output. Every numerical endpoint and subdivision
comparison uses integer arithmetic. This is not a sampled-state test or a
proof of unrestricted two-qubit or all-size optimality. The imported interval
implementation rounds outward at integer endpoints divided by 2**80.
"""
import json

from certify_two_qubit_core import (
    C, I, SCALE, SQ2, entropy_increasing, interval_min, positive_part, rat,
)


def interval_max(a, b):
    return I(max(a.lo, b.lo), max(a.hi, b.hi))


def exact_endpoint(n):
    return I(n, n)


def check_box(box):
    e, m, u, loss = [I(lo, hi) for lo, hi in box]
    q = 1-e
    r = 1-2*m
    ga = (4-2*r.square()).sqrt()
    dmax = SQ2+ga-rat(13, 4)
    if dmax.hi < 0 or loss.lo > dmax.hi:
        return 'empty', None
    fa = ga-loss
    if fa.lo <= 0:
        return 'split', None
    hm = entropy_increasing(m)
    he = entropy_increasing(e)

    # Phi(S,a) increases with S and decreases with a. Its upper bound
    # can therefore use the upper endpoint of S0 and lower endpoint of a.
    s0 = 4-(1-2*e).square()-q*r.square()
    a = q*fa
    shi = exact_endpoint(s0.hi)
    root_shi = shi.sqrt()
    if a.lo > root_shi.hi:
        alo = exact_endpoint(a.lo)
        radicand = 2*shi-alo.square()
        if radicand.hi < 0:
            return 'empty', None  # Impossible active score: a^2 > 2*S0.
        phi = alo+positive_part(radicand).sqrt()
    else:
        phi = 2*root_shi
    sld_gap = (phi-2*SQ2-C*(he+q*hm+e)
               +e*positive_part(C-1/s0.sqrt()))
    if sld_gap.hi < 0:
        return 'sld', -sld_gap.hi

    kappa = (1-m)/m
    bm = 2*SQ2+2*SQ2*kappa/(2*SQ2*kappa+1)
    dmin = interval_max(m*bm*u, 2*SQ2*m*u+loss)
    if dmin.lo > dmax.hi:
        return 'empty', None
    angle_denominator = (1-4*u).sqrt()
    ka = interval_min(
        2*kappa.sqrt()/(m*angle_denominator)*(2-ga+loss),
        8*kappa.sqrt()*u/angle_denominator,
    )
    # The exact expression is nonnegative; intersect its enclosure with
    # that known range before taking any square root.
    ka = positive_part(ka)

    # Rationalized forms avoid subtracting nearly equal positive roots.
    gain_a = 4*e*fa*ka/((fa.square()+4*e/q*fa*ka).sqrt()+fa)
    b = 4*q*e
    d_angle = 1-8*u+8*u.square()
    inner = ((1-b).square()*d_angle.square()+4*b).sqrt()
    outer = (1+b+inner).sqrt()
    gain_b = (b*(1+(4-(2-b)*d_angle.square())/(inner+d_angle))
              /(outer+SQ2*(1-2*u)))
    delta = positive_part(2*SQ2+C*hm-(SQ2+ga))
    transfer_gap = gain_a+gain_b-q*(delta+dmin)-C*he
    if transfer_gap.hi < 0:
        return 'transfer', -transfer_gap.hi
    return 'split', min(transfer_gap.hi, sld_gap.hi)


def main():
    # The last coordinate harmlessly enlarges L <= sqrt(2)-5/4 < 1/6.
    initial = [
        (rat(1, 99).lo, rat(1, 29).hi),
        (rat(7, 32).lo, rat(1, 2).hi),
        (0, rat(1, 10).hi),
        (0, rat(1, 6).hi),
    ]
    todo = [(initial, 0)]
    counts = {'transfer': 0, 'sld': 0, 'empty': 0}
    margins = {}
    visited = 0
    maximum_depth = 0
    while todo:
        if visited >= 100000:
            raise RuntimeError('interval budget exhausted with unresolved boxes')
        box, depth = todo.pop()
        visited += 1
        maximum_depth = max(depth, maximum_depth)
        status, margin = check_box(box)
        if status in counts:
            counts[status] += 1
            if margin is not None:
                margins[status] = min(margins.get(status, margin), margin)
            continue
        if status != 'split':
            raise RuntimeError('unknown interval classification: '+repr(status))
        if depth >= 32:
            raise RuntimeError('unresolved interval box: '+repr((box, margin)))
        # Split the greatest normalized coordinate width, using integer
        # cross multiplication. Ties are resolved by coordinate order.
        coordinate = 0
        for j in range(1, 4):
            if ((box[j][1]-box[j][0])
                    *(initial[coordinate][1]-initial[coordinate][0])
                    > (box[coordinate][1]-box[coordinate][0])
                    *(initial[j][1]-initial[j][0])):
                coordinate = j
        lo, hi = box[coordinate]
        mid = (lo+hi)//2
        if not lo < mid < hi:
            raise RuntimeError('integer subdivision exhausted')
        low, high = list(box), list(box)
        low[coordinate], high[coordinate] = (lo, mid), (mid, hi)
        todo.extend([(high, depth+1), (low, depth+1)])
    print(json.dumps({
        'certificate': 'PASS',
        'scope': 'scalar transfer/SLD reduction for normalized top-two spectral cores',
        'arithmetic': 'integer endpoints / 2**80, outward rounded',
        'closed_domain': {
            'epsilon': ['1/99', '1/29'],
            'm': ['7/32', '1/2'],
            'u': ['0', '1/10'],
            'L': ['0', '1/6'],
        },
        'necessary_constraints': [
            'd0=max(m*B(m)*u,2*sqrt(2)*m*u+L)<=G(m)-13/4',
            'a_min^2<=2*S0',
        ],
        'visited_boxes': visited,
        'terminal_leaves': sum(counts.values()),
        'leaf_counts': counts,
        'maximum_depth': maximum_depth,
        'minimum_positive_margin_numerators': margins,
        'margin_denominator': SCALE,
    }, indent=2))


if __name__ == '__main__':
    main()
