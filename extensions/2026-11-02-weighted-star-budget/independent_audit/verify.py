import sympy as s
from sympy.functions.combinatorial.numbers import stirling
import json
x,z=s.symbols('x z')

def simplify(v): return s.simplify(s.expand(v))
def matching(board):
    d={0:s.Integer(1)}
    for row in board:
        nd=dict(d)
        for mask,v in d.items():
            for c,w in enumerate(row):
                if not (mask>>c)&1 and w:
                    new=mask|(1<<c)
                    nd[new]=nd.get(new,0)+v*w
        d={m:simplify(v) for m,v in nd.items()}
    result=[s.Integer(0)]*(len(board)+1)
    for mask,v in d.items(): result[mask.bit_count()]+=v
    return list(map(simplify,result))

def bell(p):
    return s.expand(sum(c*sum(stirling(k,ell,kind=2)*z**ell for ell in range(k+1)) for (k,),c in s.Poly(p,x).terms()))

cases=[('P4 plus isolate',5,[ (3+s.sqrt(5))/2,(3-s.sqrt(5))/2 ],[1,3,1]),
       ('C5 plus two isolates',7,[(5+s.sqrt(5))/2,(5-s.sqrt(5))/2],[1,5,5]),
       ('K1,3',4,[s.Integer(3)],[1,3]),
       ('three disjoint edges',6,[s.Integer(1)]*3,[1,3,3,1]),
       ('rational weighted diagnostic A',4,[s.Rational(3,2),s.Rational(1,2)],[1,2,s.Rational(3,4)]),
       ('rational weighted diagnostic B',5,[s.Rational(4,3),s.Rational(5,3)],[1,3,s.Rational(20,9)])]
report=[]
for name,N,lambdas,ms in cases:
    nu=len(lambdas)
    C=sum(int(s.ceiling(v)) for v in lambdas)
    assert C<=N-1
    weights=[]
    for val in lambdas:
        f=int(s.floor(val)); row=[s.Integer(1)]*f
        rem=simplify(val-f)
        if rem: row.append(rem)
        weights.append(row)
    for j in range(1,N-nu+1):
        a,b=N-j,N-1
        F=[[s.Integer(0)]*b for _ in range(a)]
        col=0
        for r,ws in enumerate(weights):
            for w in ws: F[r][col]=w; col+=1
        fm=matching(F)
        assert all(simplify(fm[k]-(ms[k] if k<len(ms) else 0))==0 for k in range(a+1))
        J=[[simplify(1-w) for w in row] for row in F]
        jm=matching(J)
        M=s.Poly(sum(v*z**(a-k) for k,v in enumerate(jm)),z)
        q=sum((-1)**k*mk*s.prod(x+i for i in range(j,N-k)) for k,mk in enumerate(ms))
        Q=s.Poly(bell(q),z)
        assert s.expand(M.as_expr()-Q.as_expr())==0
        assert all(c>=0 for c in Q.all_coeffs())
        # SymPy exact real-root isolation, multiplicities included.
        intervals=Q.intervals(eps=s.Rational(1,10**10))
        assert sum(mult for _,mult in intervals)==a
        assert all(upper<=0 for (lower,upper),mult in intervals)
        report.append({'case':name,'N':N,'j':j,'columns':C,'Q':str(Q.as_expr()),'exact_roots':a})
print(json.dumps({'checks':len(report),'results':report},indent=2))
