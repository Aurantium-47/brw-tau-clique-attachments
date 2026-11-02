# Self-contained short-range supplement: m=1 and m=2

2026-11-02. This separate supplement leaves the frozen linear-seed core unchanged.

For a>=0,r>=1, use p=z+a+2, q=1, L=z(1+D)+1,
H=Lq+rp, F_1=(L+r)p, F_2=LF_1+H.

## m=1

F_1=z^2+(a+r+4)z+(r+1)(a+2).
Its discriminant is exactly (a-r)^2+4a+8>0. Both roots are therefore real and distinct. Its coefficients are strictly positive, so both roots are strictly negative.

## m=2

Direct expansion gives

F_2=z^3+(a+r+7)z^2+(ar+3a+5r+11)z+(2ar+a+4r+3).

The exact cubic discriminant is supplied in `short_range_certificate.json` and recomputed by `check_short_ranges.py`. Under the two substitutions

- r=a+t+1, with a,t>=0;
- a=b+t and r=b+1, with b,t>=0,

the discriminant has, respectively, 23 and 22 nonzero terms, all with positive integer coefficients; the constant term is 469 in each case. These sectors cover the full parameter domain. Hence the discriminant is strictly positive everywhere, including boundaries.

At a=0,r=1 the cubic is z^3+8z^2+16z+7. Exact Sturm calculations give one root in each of (-6,-5),(-3,-2),(-1,0). Because the parameter domain is connected, the polynomial remains monic of fixed degree, and its discriminant never vanishes, all three roots remain real and distinct throughout. Every coefficient is strictly positive, so no root is nonnegative. This proves the m=2 claim directly, without importing a separate join-preservation theorem.

Together with the independently reviewed F_3 arrowhead-seed result and its credited propagation lemma, this establishes the required negative-root conclusion for every integer m>=1, every a>=0, and every r>=1. Strict consecutive interlacing from the invariant is claimed only starting at m=3; this supplement does not assert additional adjacency statements.

## Exact reproduction

Run `python check_short_ranges.py` or `python -O check_short_ranges.py`. The checker independently constructs both polynomials from L, verifies the quadratic identity, recalculates the cubic discriminant and every certificate coefficient, and checks the basepoint root intervals by Sturm's theorem. Guards are explicit exceptions and remain enabled under optimization. A successful finite algebra check certifies the displayed parameter identities; the continuity and coefficient argument above supplies the all-parameter conclusion.
