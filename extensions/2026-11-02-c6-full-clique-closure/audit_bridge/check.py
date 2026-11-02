import sympy as s
z, r = s.symbols('z r')
L = lambda f: s.expand(z * (f + s.diff(f, z)) + f)
S = lambda f: s.expand(f + s.diff(f, z))
seq = [s.Integer(1)]
for _ in range(4):
    seq.append(L(seq[-1]))
R = sum(seq[:4])
U = seq[4]
V = R - 1
W = U + r * R
A = S(W)
C = W + V
res = s.resultant(C, A, z)
if not s.expand(res - (687 * r ** 5 + 1145 * r ** 4 + 15987 * r ** 3 + 29875 * r ** 2 + 95694 * r + 101164)) == 0:
    raise RuntimeError('exact check failed')
if not s.expand(s.discriminant(C, z) - (229 * r ** 6 + 916 * r ** 5 + 9696 * r ** 4 + 30428 * r ** 3 + 136908 * r ** 2 + 217360 * r + 422496)) == 0:
    raise RuntimeError('exact check failed')
if not s.expand(s.discriminant(A, z) - (r ** 4 * (1425 * r * r - 3160 * r + 2000) + r * r * (71778 * r * r - 24142 * r + 1202393) + 438818 * r + 5525009)) == 0:
    raise RuntimeError('exact check failed')
for aa, bb, cc in [(1425, -3160, 2000), (71778, -24142, 1202393)]:
    if not bb * bb - 4 * aa * cc < 0:
        raise RuntimeError('exact check failed')
roots = []
for name, f in [('A', A), ('C', C), ('W', W)]:
    ints = s.Poly(f.subs(r, 0), z).intervals(eps=s.Rational(1, 100000))
    if not len(ints) == 4:
        raise RuntimeError('exact check failed')
    if not all((m == 1 and b < 0 for (a, b), m in ints)):
        raise RuntimeError('exact check failed')
    roots.extend(((a, b, name) for (a, b), m in ints))
    print(name, ints)
ac = sorted((x for x in roots if x[2] != 'W'))
if not [x[2] for x in ac] == ['A', 'C'] * 4:
    raise RuntimeError('exact check failed')
for x, y in zip(ac, ac[1:]):
    if not x[1] < y[0]:
        raise RuntimeError('exact check failed')
x, w = s.symbols('x w')

def bell(f):
    p = s.Poly(s.expand(f), x)
    return s.expand(sum((c * sum((s.functions.combinatorial.numbers.stirling(k, j, kind=2) * z ** j for j in range(k + 1))) for (k,), c in p.terms())))

def star(f, g):
    if f == 0 or g == 0:
        return s.Integer(0)
    return s.expand(sum((z ** j * s.diff(f, z, j) * s.diff(g, z, j) / s.factorial(j) for j in range(min(s.degree(f, z), s.degree(g, z)) + 1))))
for n in range(1, 5):
    av = s.symbols('a:' + str(n))
    kv = s.symbols('k:' + str(n))
    p = s.prod((z + a for a in av))
    q = sum((av[i] * kv[i] * s.prod((z + av[j] for j in range(n) if j != i)) for i in range(n)))

    def apply(f, inds):
        for i in inds:
            f = s.expand((av[i] + z) * f + z * s.diff(f, w))
        return f.subs(w, z)
    out = apply(W.subs(z, w), range(n)) + sum((av[i] * kv[i] * apply(V.subs(z, w), [j for j in range(n) if j != i]) for i in range(n)))
    if not s.expand(out - star(W, p) - star(V, q)) == 0:
        raise RuntimeError('exact check failed')
print('PASS resultant,discriminants,baseorder,diagonal n1..4')
if not s.expand(s.discriminant(W, z) - (r ** 4 * (229 * r * r - 660 * r + 1000) + r * r * (7798 * r * r - 10122 * r + 10000) + (82229 * r * r - 47278 * r + 227081))) == 0:
    raise RuntimeError('exact check failed')
for aa, bb, cc, dd in [(229, -660, 1000, -480400), (7798, -10122, 10000, -209465116), (82229, -47278, 227081, -72455364912)]:
    if not bb * bb - 4 * aa * cc == dd < 0:
        raise RuntimeError('exact check failed')
for n in range(7):
    f = x ** n
    h = bell(f)
    p = S(S(h))
    q = s.diff(S(h), z)
    graph = (x + r + 1) * sum(((x + 1) ** j for j in range(4))) * f.subs(x, x + 2) - (x + 1) * sum(((x + 1) ** j for j in range(3))) * f.subs(x, x + 1)
    if not s.expand(bell(graph) - star(W, p) - star(V, q)) == 0:
        raise RuntimeError('exact check failed')
print('PASS W certificate and symbolic-r graph/operator basis n0..6')
