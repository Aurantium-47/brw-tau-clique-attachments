"""Exact finite formula checks only; not a proof of eventual real-rootedness."""
import json
from pathlib import Path
import sympy as s
x,t,z,q=s.symbols('x t z q')
def S(n): return sum(t**i for i in range(n))
def theta(a,b,m):
    edges=[]; nxt=2
    for length in (a,b,m):
        path=[0]+list(range(nxt,nxt+length-1))+[1]; nxt+=length-1
        edges += list(zip(path,path[1:]))
    return nxt,edges
def chromatic_subset(n,edges):
    coeff=[0]*(n+1)
    for mask in range(1<<len(edges)):
        p=list(range(n)); components=n
        def root(v):
            while p[v]!=v: v=p[v]
            return v
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:
                u,v=root(u),root(v)
                if u!=v:p[u]=v;components-=1
        coeff[components]+=(-1)**mask.bit_count()
    return sum(c*q**k for k,c in enumerate(coeff))
out={'scope':'Exact finite identity checks; not an eventual-root proof','cases':[]}
for a,b,m in [(2,2,2),(2,2,3),(2,3,4),(3,3,3),(2,4,5),(4,3,4)]:
    n,e=theta(a,b,m); chi=chromatic_subset(n,e)
    Q=s.expand((S(a+b-1)*S(m)+t*S(a-1)*S(b-1)).subs(t,x+1))
    P=s.expand((-1)**n*chi.subs(q,-x))
    ok=s.expand(P-x*(x+1)*Q)==0
    quotient_ok=s.expand((S(a+b-1)*t**m-(S(a)+S(b)-1))-(t-1)*(S(a+b-1)*S(m)+t*S(a-1)*S(b-1)))==0
    assert ok and quotient_ok
    out['cases'].append({'paths':[a,b,m],'vertices':n,'edges':len(e),'independent_subset_expansion_match':ok,'quotient_identity':quotient_ok})
h=x*x+x+1
quartic=s.expand(sum(c*s.bell(j,z) for (j,),c in s.Poly(h*h,x).terms()))
assert quartic==z**4+8*z**3+16*z*z+8*z+1
brackets=[(-6,-5),(-3,-2),(s.Rational(-1,2),s.Rational(-2,5)),(s.Rational(-1,5),s.Rational(-1,10))]
out['quartic']={'coefficients':[int(c) for c in s.Poly(quartic,z).all_coeffs()], 'brackets':[]}
for l,r in brackets:
    fl,fr=quartic.subs(z,l),quartic.subs(z,r);assert fl*fr<0
    out['quartic']['brackets'].append({'left':str(l),'right':str(r),'left_value':str(fl),'right_value':str(fr)})
u,v=s.symbols('u v',real=True)
assert s.expand((5-4*u-4*v*v)-(4*(1-u*u-v*v)+4*(u-s.Rational(1,2))**2))==0
out['unit_disk_margin_identity']=True
path=Path(__file__).with_name('EXACT_IDENTITY_CHECKS.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(path)
