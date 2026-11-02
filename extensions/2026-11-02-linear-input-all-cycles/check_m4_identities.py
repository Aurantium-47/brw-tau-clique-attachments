#!/usr/bin/env python3
import sympy as S
z=S.symbols('z'); ss,v,w,x=S.symbols('s v w x')
def require(x,msg):
 if not x: raise RuntimeError(msg)
def L(f): return S.expand(z*(f+S.diff(f,z))+f)
A=ss**3+7*ss**2+11*ss+4-(3*ss+7)*v+2*w
B=3*ss**2+14*ss+11-3*v; C=3*ss+7
D0=B*(ss-v)-2*C*(v-w)+6*(w-x)
require(S.expand(D0-(S.diff(A,ss)*(ss-v)+S.diff(A,v)*2*(v-w)+S.diff(A,w)*3*(w-x)))==0,'moment derivative')
R=z**3+7*z**2+11*z+4
require(S.discriminant(R,z)==229,'R discriminant')
require(S.Poly(R,z).count_roots(-S.oo,0)==3,'R negative roots')
fixtures=[[],[S.Rational(1,2)],[1,3],[S.Rational(1,3),2,5]]
cases=0
for aa in fixtures:
 p=S.prod(z+a for a in aa); uu=[z/(z+a) for a in aa]
 mom={ss:S.cancel(z+sum(uu)),v:S.cancel(sum(u**2 for u in uu)),w:S.cancel(sum(u**3 for u in uu)),x:S.cancel(sum(u**4 for u in uu))}
 pp=[p]
 for k in range(4): pp.append(L(pp[-1]))
 T=S.expand(sum(pp[:4])); Ar=S.cancel(A.subs(mom)); Dr=S.cancel(D0.subs(mom)); Br=S.cancel(B.subs(mom)); Cr=S.cancel(C.subs(mom))
 require(S.cancel(T/p-Ar)==0,'T moment identity')
 require(S.cancel(z*S.diff(Ar,z)-Dr)==0,'derivative identity')
 active_sets=[[]]+([[0]] if aa else [])+([[0,len(aa)-1]] if len(aa)>1 else [])
 for active in active_sets:
  h=S.cancel(sum(S.Rational(1,2)*(1-uu[i]) for i in active))
  q=S.cancel(p*h); qq=[q]
  for k in range(3):qq.append(L(qq[-1]))
  F=S.expand(pp[4]+sum(qq[1:4]))
  N=Dr+1-sum(S.Rational(1,2)*(1-uu[i])*(1+Br*uu[i]-2*Cr*uu[i]**2+6*uu[i]**3) for i in active)
  # Off-root identity contains the exact multiple (s+h)A.
  require(S.cancel(F/p-N-(mom[ss]+h)*Ar)==0,'off-root numerator identity')
  cases+=1
print({'status':'PASS','fixtures':len(fixtures),'vertex_cases':cases,'scope':'identities only, not m4 compatibility'})
