import sympy as s
from itertools import combinations
z,X,Y,t=s.symbols('z X Y t')
L=lambda p:s.expand(z*(p+s.diff(p,z))+p)
G=t**3-(X-1)*t**2-(X-s.Rational(1,2))*t-s.Rational(1,2)
H=-t**3+(Y+1)*t**2-(Y+s.Rational(1,2))*t-s.Rational(1,2)
if not (s.expand(G-((t-X)*t*(t+1)+(t-1)/2))==0): raise AssertionError('s.expand(G-((t-X)*t*(t+1)+(t-1)/2))==0')
if not (s.expand(H-((Y-t)*t*(t-1)-(t+1)/2))==0): raise AssertionError('s.expand(H-((Y-t)*t*(t-1)-(t+1)/2))==0')
if not (s.cancel(t*(t-1)/(2*t+1)-(t+1)/2+(5*t+1)/(2*(2*t+1)))==0): raise AssertionError('s.cancel(t*(t-1)/(2*t+1)-(t+1)/2+(5*t+1)/(2*(2*t+1)))==0')
if not (s.cancel(-(5*t+1)/(2*(2*t+1))+s.Rational(5,4)-s.Rational(3,4)/(2*t+1))==0): raise AssertionError('s.cancel(-(5*t+1)/(2*(2*t+1))+s.Rational(5,4)-s.Rational(3,4)/(2*t+1))==0')
fixtures=[[],[1],[2],[0],[1,2],[1,1],[0,0],[1,3,5],[s.Rational(1,2),2,6],[0,1,1,4],[1,2,3,4,5],[s.Rational(i,3) for i in range(1,7)]]
checks=0;identities=0
for aa in fixtures[:8]:
 p=s.prod(z+a for a in aa); T=L(L(p))+L(p)+p
 u=[z/(z+a) for a in aa]; xx=z+sum(u)+2
 if not (s.cancel(T/p-(xx**2-1-sum(v*v for v in u)))==0): raise AssertionError('s.cancel(T/p-(xx**2-1-sum(v*v for v in u)))==0')
 D0=2*(sum(v**3 for v in u)-xx**3-xx+1)
 num=s.fraction(s.cancel(z*s.diff(T,z)/p-D0))[0]
 if not (s.rem(num,s.div(T,s.gcd(T,p),z)[0],z)==0): raise AssertionError('s.rem(num,s.div(T,s.gcd(T,p),z)[0],z)==0')
 identities+=2
 for k in range(min(2,len(aa))+1):
  for inds in combinations(range(len(aa)),k):
   q=s.Add(*[aa[i]*s.prod(z+aa[j] for j in range(len(aa)) if j!=i)/2 for i in inds])
   F=L(L(L(p)))+L(L(q))+L(q)
   N=D0+1-s.Add(*[(1-u[i])*(1+2*xx*u[i]-2*u[i]**2)/2 for i in inds])
   num=s.fraction(s.cancel(F/p-N))[0]
   if not (s.rem(num,s.div(T,s.gcd(T,p),z)[0],z)==0): raise AssertionError('s.rem(num,s.div(T,s.gcd(T,p),z)[0],z)==0')
   identities+=1
   for r in [0,1,s.Rational(7,2)]:
    P=s.Poly(F+r*T,z)
    if not (all(c>=0 for c in P.all_coeffs())): raise AssertionError('all(c>=0 for c in P.all_coeffs())')
    for fac,mult in s.sqf_list(P)[1]:
     if not (fac.count_roots(-s.oo,0)==fac.degree()): raise AssertionError('fac.count_roots(-s.oo,0)==fac.degree()')
    checks+=1
print({'exact_pencil_cases':checks,'exact_identity_checks':identities,'fixtures':len(fixtures[:8]),'status':'PASS'})
