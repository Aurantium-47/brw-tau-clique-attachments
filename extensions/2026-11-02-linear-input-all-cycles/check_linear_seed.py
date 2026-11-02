#!/usr/bin/env python3
"""Exact seed invariant checks. Finite polynomials certify all a>=0,r>=1."""
import json
from pathlib import Path
import sympy as s
z,a,r,t,b,u=s.symbols('z a r t b u')
def require(v,msg):
 if not v:raise RuntimeError(msg)
def L(f):return s.expand(z*(f+s.diff(f,z))+f)
p=z+a+2;q=s.Integer(1);H=s.expand(L(q)+r*p)
F=s.expand(L(L(L(p)))+L(L(q))+L(q)+r*(p+L(p)+L(L(p))))
R=s.resultant(F,z*s.diff(F,z)+u*H,z)
D=s.factor(R.subs(u,1));M=s.factor(R.subs(u,-1));G=s.factor(s.diff(R,u).subs(u,1)+2*D)
Disc=s.discriminant(F,z)
sectors={'r_ge_a_plus_1':({r:a+t+1},(a,t)), 'a_ge_r_minus_1':({a:b+t,r:b+1},(b,t))}
cert={}
for name,expr in [('disc',Disc),('denominator',D),('minus_resultant',M),('gap_numerator',G)]:
 cert[name]={}
 for sector,(sub,vars_) in sectors.items():
  P=s.Poly(expr.subs(sub,simultaneous=True).expand(),*vars_)
  require(all(c>0 for c in P.coeffs()),f'positive coefficients: {name}/{sector}')
  require(P.coeff_monomial(1)>0,f'positive constant: {name}/{sector}')
  cert[name][sector]={'terms':[[list(mon),int(c)] for mon,c in P.terms()], 'constant':int(P.coeff_monomial(1))}
# Base-point negative simple roots and rational interval bounds |kappa|<1.
F0=s.Poly(F.subs({a:0,r:1}),z);H0=s.Poly(H.subs({a:0,r:1}),z)
intervals=[(s.Rational(-7220,1000),s.Rational(-7219,1000)),(s.Rational(-3202,1000),s.Rational(-3201,1000)),(s.Rational(-1226,1000),s.Rational(-1225,1000)),(s.Rational(-353,1000),s.Rational(-352,1000))]
def mul(I,J):
 v=[x*y for x in I for y in J];return min(v),max(v)
def val(P,I):
 out=(s.Rational(0),s.Rational(0))
 for c in P.all_coeffs():
  v=mul(out,I);out=(v[0]+c,v[1]+c)
 return out
def divide(I,J):
 require(J[0]*J[1]>0,'nonzero denominator interval')
 return mul(I,(1/J[1],1/J[0]))
base=[]
for lo,hi in intervals:
 require(F0.count_roots(lo,hi)==1,'exact isolated root')
 II=(lo,hi);HH=val(H0,II);den=mul(II,val(F0.diff(),II))
 K=divide((-HH[1],-HH[0]),den)
 require(K[0]>-1 and K[1]<1,'base |kappa|<1')
 base.append({'root_interval':[str(lo),str(hi)],'kappa_interval':[str(v) for v in K]})
require(s.expand(F.subs(z,0)-H.subs(z,0))==2*a*r+a+4*r+3,'0<w<1')
# Check resultant trace identity independently at a rational seed via quotient-ring trace.
FF=s.Poly(F.subs({a:2,r:3}),z);HH=s.Poly(H.subs({a:2,r:3}),z)
inv=s.invert(z*FF.diff().as_expr()+HH.as_expr(),FF.as_expr(),z)
rem=s.Poly(s.rem(HH.as_expr()*inv,FF.as_expr(),z),z)
# Trace multiplication matrix in Q[z]/F.
trace=0
for j in range(4):trace+=s.Poly(s.rem(rem.as_expr()*z**j,FF.as_expr(),z),z).coeff_monomial(z**j)
require(s.cancel(trace-(s.diff(R,u)/R).subs({a:2,r:3,u:1}))==0,'resultant/quotient trace agreement')
cert['base']=base
path=Path(__file__).with_name('linear_seed_certificate.json')
if path.exists():require(json.loads(path.read_text())==cert,'frozen certificate exact match')
else:path.write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps({'status':'PASS','sectors':2,'polynomials':4,'term_counts':{name:[len(cert[name][key]['terms']) for key in sectors] for name in ['disc','denominator','minus_resultant','gap_numerator']},'base_intervals':4,'trace_identity':'PASS'}))
