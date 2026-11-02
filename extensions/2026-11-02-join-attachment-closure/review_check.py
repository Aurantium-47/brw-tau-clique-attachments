import sympy as s
from math import factorial,comb
def require(condition, detail):
 if not condition: raise RuntimeError(str(detail))

x,z=s.symbols('x z')
def bell(f):
 p=s.Poly(f,x); return s.Poly(sum(c*s.bell(k,z) for (k,),c in p.terms()),z)
def invbell(f):
 f=s.Poly(f,z); rem=f.as_expr(); out=0
 for k in range(f.degree(),-1,-1):
  c=s.expand(rem).coeff(z,k);out+=c*x**k;rem-=c*s.bell(k,z)
 require(s.expand(rem)==0,rem)
 return s.expand(out)
def shifted(f,a):
 rem=s.expand(f);out=[]
 for k in range(s.degree(f,x),-1,-1):
  c=rem.coeff(x,k);out.append((k,c));rem=s.expand(rem-c*s.rf(x+a,k))
 require(rem==0,rem)
 return out
def C(f,g,a,b):
 return bell(s.expand(sum(c*d*s.rf(x+a+b,k+l) for k,c in shifted(invbell(f),a) for l,d in shifted(invbell(g),b))))
def M(p,q):return sum(comb(p,k)*comb(q,k)*factorial(k)*z**(p-k) for k in range(min(p,q)+1))
count=0
for a in range(1,4):
 for b in range(1,4):
  for p in range(5):
   for q in range(5):
    t=M(p,q+b-1)*M(q,p+a-1)
    require(C(z**p,z**q,a,b)==s.Poly(t+s.diff(t,z),z),(a,b,p,q))
    count+=1
print('Independent direct basis check passed:',count)
for a,b,p,q in [(1,1,2,2),(3,1,3,2),(1,4,0,3),(2,2,3,0)]:
 f=s.prod(z+i for i in range(p));g=s.prod(z+2*i for i in range(q));c=C(f,g,a,b)
 require(all(v>=0 for v in c.all_coeffs()),c)
 require(sum(h.count_roots(-s.oo,0)*m for h,m in c.sqf_list()[1])==c.degree(),c)
 print(a,b,p,q,c.as_expr())
