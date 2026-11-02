"""Exact algebra/sign certificates; not a numerical proof of eventuality."""
if not __debug__:
    raise SystemExit('Assertions must remain enabled.')
import json
from pathlib import Path
import sympy as s
t,u,v,w,x,z=s.symbols('t u v w x z')
# u=t^a, v=t^b, w=t^m. This rational identity proves the algebra for all lengths.
q_path=(t*(u-1)*(v-1)*(w-1)-(u-t)*(v-t)*(w-t))/(t*(t-1)**3)
q_compact=((u*v/t-1)*w-u-v+t+1)/(t-1)**2
assert s.cancel(q_path-q_compact)==0
# Product form S_(a+b-1) S_m + t S_(a-1) S_(b-1).
q_positive=(u*v/t-1)*(w-1)/(t-1)**2+t*(u/t-1)*(v/t-1)/(t-1)**2
assert s.cancel(q_compact-q_positive)==0
h=(x*x+x+1)**2
bell=s.expand(sum(c*s.bell(k[0],z) for k,c in s.Poly(h,x).terms()))
quartic=z**4+8*z**3+16*z**2+8*z+1
assert bell==quartic
intervals=[(-6,-5),(-3,-2),(s.Rational(-1,2),s.Rational(-2,5)),(s.Rational(-1,5),s.Rational(-1,10))]
values=[]
for lo,hi in intervals:
 a,b=quartic.subs(z,lo),quartic.subs(z,hi)
 assert a*b<0
 values.append({'interval':[str(lo),str(hi)],'endpoint_values':[str(a),str(b)]})
r,y=s.symbols('r y',real=True)
J=5-4*r-4*y*y
assert s.expand(J-(4*(1-r*r-y*y)+4*(r-s.Rational(1,2))**2))==0
result={'status':'PASS','checks':['all-length rational path/coloring quotient identity','all-length positive geometric-sum identity','exact Bell quartic identity','four disjoint negative sign intervals','parabola radial identity'],'quartic':str(quartic),'intervals':values,'limitation':'The existential eventual threshold is established by the analytic proof, not these finite/algebraic checks.'}
Path(__file__).with_name('general_theta_identity_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
