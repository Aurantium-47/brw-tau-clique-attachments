"""Exact rational Bernstein certificate for the cubic repair box."""
if not __debug__: raise SystemExit('Assertions must remain enabled')
import sympy as s,itertools,math,json
from pathlib import Path
A,e,alpha,z=s.symbols('A e alpha z');u,v,w=s.symbols('u v w')
f=z**3+(3+A+alpha)*z**2+(1+2*A+alpha+alpha*A+e)*z+alpha*(A+e)
D=s.discriminant(f,z);y=2*u-1
p=s.Poly(s.expand(D.subs({A:1+s.Rational(2,3)*y,e:(y*y+(1-y*y)*v)/9,alpha:1+s.Rational(11,10)*w})),u,v,w)
deg=p.degree_list();power=dict(p.terms());indices=list(itertools.product(*(range(n+1) for n in deg)))
b={}
for i in indices:
 b[i]=sum(c*s.prod(s.Rational(math.comb(ii,jj),math.comb(nn,jj)) for ii,jj,nn in zip(i,j,deg)) for j,c in power.items() if all(jj<=ii for ii,jj in zip(i,j)))
assert all(c>0 for c in b.values())
for j in indices:
 restored=s.prod(math.comb(n,jj) for n,jj in zip(deg,j))*sum(c*(-1)**sum(jj-ii for ii,jj in zip(i,j))*s.prod(math.comb(jj,ii) for ii,jj in zip(i,j)) for i,c in b.items() if all(ii<=jj for ii,jj in zip(i,j)))
 assert restored==power.get(j,0)
assert s.factor(f.subs({A:1,e:0,alpha:1})-(z+1)*(z*z+4*z+1))==0
out={'status':'PASS','degrees':list(deg),'coefficient_count':len(b),'minimum':str(min(b.values())),'exact_inverse_roundtrip':True,'substitution':{'A':'1+2(2u-1)/3','e':'((2u-1)^2+(1-(2u-1)^2)v)/9','alpha':'1+11w/10'},'domain':'u,v,w in [0,1]','bernstein_coefficients':{','.join(map(str,i)):str(c) for i,c in b.items()}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='bernstein_coefficients'})
