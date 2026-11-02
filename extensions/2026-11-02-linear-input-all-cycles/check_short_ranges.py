#!/usr/bin/env python3
"""Exact supplementary F1/F2 checks for all a>=0,r>=1."""
import json
from pathlib import Path
import sympy as s
z,a,r,t,b=s.symbols('z a r t b')
def require(v,msg):
 if not v:raise RuntimeError(msg)
def L(f):return s.expand(z*(f+s.diff(f,z))+f)
p=z+a+2;q=s.Integer(1);H=s.expand(L(q)+r*p)
F1=s.expand(L(p)+r*p);F2=s.expand(L(F1)+H)
require(s.expand(s.discriminant(F1,z)-((a-r)**2+4*a+8))==0,'F1 discriminant identity')
require(s.expand(F1-(z**2+(a+r+4)*z+(r+1)*(a+2)))==0,'F1 coefficient identity')
require(s.expand(F2-(z**3+(a+r+7)*z**2+(a*r+3*a+5*r+11)*z+(2*a*r+a+4*r+3)))==0,'F2 displayed coefficient identity')
D=s.discriminant(F2,z)
cert={'F1':str(F1),'F2':str(F2),'F2_discriminant':str(s.expand(D)),'sectors':{}}
for name,sub,vs in [('r_minus_1_ge_a',{r:a+t+1},(a,t)),('a_ge_r_minus_1',{a:b+t,r:b+1},(b,t))]:
 P=s.Poly(D.subs(sub,simultaneous=True).expand(),*vs)
 require(all(v>0 for v in P.coeffs()),'all discriminant sector coefficients positive')
 require(P.coeff_monomial(1)>0,'positive sector constant')
 cert['sectors'][name]={'terms':[[list(k),int(v)] for k,v in P.terms()],'constant':int(P.coeff_monomial(1))}
base=s.Poly(F2.subs({a:0,r:1}),z)
intervals=[(-6,-5),(-3,-2),(-1,0)]
for lo,hi in intervals:require(base.count_roots(lo,hi)==1,'F2 base Sturm interval')
cert['base_F2']=str(base.as_expr());cert['base_intervals']=intervals
# All coefficients are positive directly in a>=0,r>=1 (indeed r>=0).
for F in [F1,F2]:
 for coeff in s.Poly(F,z).all_coeffs():
  P=s.Poly(coeff,a,r)
  require(all(v>=0 for v in P.coeffs()),'nonnegative coefficient polynomial')
  require(coeff.subs({a:0,r:1})>0,'positive throughout domain')
path=Path(__file__).with_name('short_range_certificate.json')
# JSON tuples round-trip as lists.
cert=json.loads(json.dumps(cert))
if path.exists():require(json.loads(path.read_text())==cert,'frozen exact certificate')
else:path.write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps({'status':'PASS','F1_discriminant':'positive exact identity','F2_sector_terms':[len(v['terms']) for v in cert['sectors'].values()],'F2_base_intervals':3}))
