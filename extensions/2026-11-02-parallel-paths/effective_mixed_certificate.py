"""Exact rational certificate; no floating-point computation is used."""
if not __debug__: raise SystemExit('Assertions must remain enabled')
import sympy as sp
import itertools,json,hashlib
from math import comb
from pathlib import Path
OUT=Path(__file__).resolve().parent
z,P,Q,p,q=sp.symbols('z P Q p q')
u,v,a,b=sp.symbols('u v a b')
R=sp.Rational(21,20); S=sp.Rational(1,3)
f=z**4+(6+P+p)*z**3+(7+3*(P+p)+Q+q+P*p)*z**2+(1+P+p+Q+q+P*p+P*q+p*Q)*z+Q*q
D=sp.discriminant(f,z)
subs={P:1+2*S*b*(2*a-1),Q:1+2*S*b*(2*a-1)+S*S*b*b,p:2+2*R-4*R*u,q:(1+R-2*R*u)**2+4*R*R*u*(1-u)*v}
E=sp.Poly(D.subs(subs),u,v,a,b)
ns=E.degree_list();co=dict(E.terms())
for axis,n in enumerate(ns):
 out={}
 for idx,c in co.items():
  j=idx[axis]
  for k in range(j,n+1):
   dst=list(idx);dst[axis]=k;dst=tuple(dst)
   out[dst]=out.get(dst,0)+c*sp.Rational(comb(k,j),comb(n,j))
 co=out
full=list(itertools.product(*(range(n+1) for n in ns)))
assert set(co)==set(full)
assert all(c>0 for c in co.values())
# Independently expand each Bernstein basis B_(i,n) into powers, and check
# exact coefficient equality with the original discriminant polynomial.
back=co
for axis,n in enumerate(ns):
 expanded={}
 for idx,c in back.items():
  i=idx[axis]
  for j in range(i,n+1):
   dst=list(idx);dst[axis]=j;dst=tuple(dst)
   expanded[dst]=expanded.get(dst,0)+c*comb(n,i)*comb(n-i,j-i)*(-1)**(j-i)
 back=expanded
assert {k:v for k,v in back.items() if v} == dict(E.terms())
assert R**2-1<S**2
assert R**67*(R**3-1)>4
assert R**66*(R**3-1)<4
# All nonconstant coefficients of f stay strictly positive over this box:
# P>=1/3, p>=-1/10, Q>=P, q>=0. The z coefficient
# =1+P+p+Q+q+P*p+P*q+p*Q >= .9+.9P+.9Q>0.
certificate={
 'radius':str(R),'s_bound':str(S),'degree':list(ns),'coefficient_count':len(co),
 'minimum':str(min(co.values())),'threshold':69,
 'exact_bernstein_to_power_roundtrip':True,
 'radius_inequality_at_69':str(R**67*(R**3-1)),
 'bernstein_coefficients':[{'index':list(k),'coefficient':str(co[k])} for k in full],
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(OUT/'effective_mixed_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print({k:v for k,v in certificate.items() if k!='bernstein_coefficients'})
