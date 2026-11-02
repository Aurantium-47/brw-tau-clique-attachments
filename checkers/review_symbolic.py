"""Independent review: derive A(z^n) by operator composition, no normal-form input."""
import sympy as s,json
from pathlib import Path
n,u,v=s.symbols('n u v')
def add(*fs):
 out={}
 for f in fs:
  for j,c in f.items():out[j]=s.expand(out.get(j,0)+c)
 return {j:c for j,c in out.items() if c!=0}
def scale(c,f):return {j:s.expand(c*a) for j,a in f.items()}
def D(f):return {j-1:s.expand((n+j)*a) for j,a in f.items()}
def Z(f):return {j+1:a for j,a in f.items()}
def E(f):return add(f,D(f))
def L(c,f):return add(Z(E(f)),scale(c,f))
def power(op,k,f):
 for _ in range(k):f=op(f)
 return f
f={0:s.Integer(1)}
A=add(L(2,L(2,power(E,3,f))),scale(-3,L(0,power(E,2,f))),scale(-5,power(E,2,f)),E(f))
# Independently enumerate the choices at each core vertex as products.
# The two possible core edges contribute identically; absent such an edge c may be free or used by either leaf class.
core_free=s.prod([1+s.Rational(2,3)*u+s.Rational(1,3)*v,1+s.Rational(1,2)*u+s.Rational(1,2)*v,1+u,1+u,1+u])
core_used=2*s.prod([1+s.Rational(1,2)*u+s.Rational(1,2)*v,1+u,1+u,1+u])
M={}
for expr,core_count in [(core_free,0),(core_used,1)]:
 for (red,blue),w in s.Poly(s.expand(expr),u,v).terms():
  k=red+blue+core_count
  M[2-k]=M.get(2-k,0)+w*s.ff(n,red)*s.ff(n,blue)
keys=set(A)|set(M)
assert all(s.expand(A.get(j,0)-M.get(j,0))==0 for j in keys)
result={'status':'PASS symbolic all-n identity, independently composed operator','coefficient_by_matching_size':{str(2-j):str(s.factor(M[j])) for j in sorted(M,reverse=True)},'residuals':{str(j):str(s.expand(A.get(j,0)-M.get(j,0))) for j in sorted(keys)}}
Path(__file__).with_name('symbolic_review.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
