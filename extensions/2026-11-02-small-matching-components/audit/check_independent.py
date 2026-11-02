"""Portable independent exact audit; no imports from the main verifier.

Run: python audit/check_independent.py
Requires SymPy. Uses exact rational arithmetic throughout.
"""
import sympy as s
from sympy.functions.combinatorial.numbers import stirling


def require(condition, description):
    if not condition:
        raise AssertionError(description)


def chromatic_residual(pairs, x, t):
    """Use unsigned complement matching counts and falling factorials."""
    n = sum(p + q + 2 for p, q in pairs)
    nu = 2 * len(pairs)
    j = n - nu
    matching = s.Poly(s.prod(1 + (p + q + 1)*t + p*q*t*t
                            for p, q in pairs), t)
    residual = s.Poly(sum(matching.nth(k) * s.prod(x - i for i in range(j, n-k))
                         for k in range(nu + 1)), x)
    return residual


def main():
    x, y, z, t = s.symbols('x y z t')
    f12 = chromatic_residual([(2, 2), (2, 2)], x, t)
    q12 = s.Poly(f12.as_expr().subs(x, -x), x)
    require(q12.as_expr() == x**4+28*x**3+302*x**2+1483*x+2792,
            'n12 quartic from falling-factorial expansion')
    sos = y**4 + 8*(y-s.Rational(1, 16))**2 + s.Rational(191, 32)
    require(s.expand(q12.as_expr().subs(x, y-7) - sos) == 0,
            'positive sum-of-squares identity')
    require(s.Rational(191, 32) > 0, 'strict positivity of constant')
    bell = s.Poly(sum(q12.nth(d)*sum(stirling(d, i, kind=2)*z**i
                                    for i in range(d+1))
                      for d in range(q12.degree()+1)), z)
    require(bell.as_expr() == z**4+34*z**3+393*z**2+1814*z+2792,
            'n12 Bell transform')
    points = [-16, -15, -10, -9, -6, -5, -4, -3]
    values = [int(bell.eval(v)) for v in points]
    require(values == [648, -118, -48, 74, 8, -78, -96, 50],
            'Bell endpoint values')
    require(all(values[i]*values[i+1] < 0 for i in range(0, 8, 2)),
            'four disjoint negative sign-change brackets')
    print('PASS: n12 residual, positive sum of squares, Bell transform and four sign brackets')

    # Also verify the earlier example is inside, rather than outside, BRW R_T(0).
    for ai, bi, ci, di in [(691, 693, 90, 92), (707, 709, 267, 269)]:
        a, b, c, d = [s.Rational(v, 100) for v in (ai, bi, ci, di)]
        require(f12.count_roots(a+s.I*c, b+s.I*d) == 1, 'n12 upper box')
        require(f12.count_roots(a-s.I*d, b-s.I*c) == 1, 'n12 conjugate box')
        require(a+s.Rational(1, 4)-d*d > 0, 'n12 region inclusion bound')
    require(f12.degree() == 4, 'n12 boxes account for all roots')
    print('PASS: all n12 nonreal chromatic zeros strictly inside BRW R_T(0)')

    f15 = chromatic_residual([(2, 2), (1, 1), (1, 2)], x, t)
    require(f15.as_expr() == x**6-57*x**5+1369*x**4-17710*x**3
            +129992*x**2-512731*x+848168, 'n15 residual')
    require(s.gcd(f15, f15.diff()).degree() == 0, 'n15 squarefree')
    a, b, c, d = [s.Rational(v, 100) for v in (1015, 1016, 363, 364)]
    require(f15.count_roots(a+s.I*c, b+s.I*d) == 1, 'n15 rectangle root count')
    margin = c*c-b-s.Rational(1, 4)
    require(margin == s.Rational(27669, 10000) and margin > 0,
            'n15 entire rectangle outside closed region')
    print('PASS: n15 falling-factorial residual, squarefree check, exact complex root count = 1')
    print('PASS: n15 rational exclusion margin = 27669/10000 > 0')
    print('PASS: independent audit complete; all checks exact, no sibling-file dependencies')


if __name__ == '__main__':
    main()
