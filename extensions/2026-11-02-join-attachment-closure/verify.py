import sympy as s
from functools import lru_cache
from pathlib import Path
import json
def require(condition, detail):
 if not condition: raise RuntimeError(str(detail))

x,z=s.symbols('x z')
def bell(f):
 p=s.Poly(s.expand(f),x)
 return s.Poly(sum(c*s.bell(k,z) for (k,),c in p.terms()),z)
def invbell(f):
 p=s.Poly(f,z); out=0
 while not p.is_zero:
  k=p.degree(); c=p.LC();out+=c*x**k;p-=s.Poly(c*s.bell(k,z),z)
 return s.expand(out)
def basis(f,a):
 p=s.Poly(f,x);out={}
 while not p.is_zero:
  k=p.degree();c=p.LC();out[k]=c;p-=s.Poly(c*s.rf(x+a,k),x)
 return out
def op(f,g,a,b):
 c=basis(invbell(f),a);d=basis(invbell(g),b)
 return bell(sum(v*w*s.rf(x+a+b,k+l) for k,v in c.items() for l,w in d.items()))
def board(al,be,a,b):
 p,q=len(al),len(be); red=q+b-1;blue=p+a-1;om=red+blue
 rows=[]
 for i,t in enumerate(al):rows.append([(j,1) for j in range(red)]+[(red+i,t),(om,1)])
 for i,t in enumerate(be):rows.append([(red+j,1) for j in range(blue)]+[(i,t),(om,1)])
 @lru_cache(None)
 def rec(i,mask):
  if i==p+q:return (1,)
  base=rec(i+1,mask);res=[0]+list(base)
  for c,w in rows[i]:
   if not(mask>>c&1) and w:
    r=rec(i+1,mask|(1<<c))
    for k,v in enumerate(r):res[k]+=w*v
  return tuple(res)
 return s.Poly.from_list(list(reversed(rec(0,0))),z)
records=[]
for a,b in [(1,1),(1,2),(2,1),(2,3),(4,2)]:
 for p in range(4):
  for q in range(4):
   for mode in range(2):
    al=[0 if mode==0 else s.Rational(i+1,2) for i in range(p)]
    be=[0 if mode==0 else s.Rational(i+2,3) for i in range(q)]
    f=s.prod(z+t for t in al);g=s.prod(z+t for t in be)
    out=op(f,g,a,b);mat=board(al,be,a,b)
    require(out==mat,(a,b,al,be,out,mat))
    require(all(t>=0 for t in out.all_coeffs()),out)
    require(sum(h.count_roots(-s.oo,0)*m for h,m in out.sqf_list()[1])==out.degree(),out)
    records.append(dict(a=a,b=b,alpha=list(map(str,al)),beta=list(map(str,be)),coeffs=list(map(str,out.all_coeffs()))))
json.dump(records,open(Path(__file__).resolve().parent/'certificate.json','w'),indent=2)
print('PASS',len(records),'exact operator/weighted-board/root-count checks')
