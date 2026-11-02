import sympy as s
z=s.symbols('z'); X,Y,u=s.symbols('X Y u', real=True)
def eq(a,b):
 if s.expand(a-b)!=0:raise RuntimeError(s.expand(a-b))
def L(p):return s.expand(z*(p+s.diff(p,z))+p)
def T(p):return s.expand(L(L(p))+L(p)+p)
def star(f,g):return s.expand(sum(z**k*s.diff(f,z,k)*s.diff(g,z,k)/s.factorial(k) for k in range(min(s.degree(f,z),s.degree(g,z))+1)))
G=u**3-(X-1)*u**2-(X-s.Rational(1,2))*u-s.Rational(1,2)
H=-u**3+(Y+1)*u**2-(Y+s.Rational(1,2))*u-s.Rational(1,2)
eq(G,(u-X)*u*(u+1)+(u-1)/2)
eq(H,(Y-u)*u*(u-1)-(u+1)/2)
eq(s.together(-u*(u+1)/(2*u+1)+(u-1)/2+(3*u+1)/(2*(2*u+1)))*2*(2*u+1),0)
eq(s.together(u*(u-1)/(2*u+1)-(u+1)/2+(5*u+1)/(2*(2*u+1)))*2*(2*u+1),0)
eq(s.together((u*u+1-(u+1/(2*u+1))**2)*(2*u+1)**2),2*u)
P=[s.symbols('p:'+str(6))][0]
p=sum(P[i]*z**i for i in range(6))
eq(T(p),z*z*s.diff(p,z,2)+(2*z*z+4*z)*s.diff(p,z)+(z*z+4*z+3)*p)
eq(T(p),star(z*z+4*z+3,p))
# Product-rule source calculation with independent formal h derivatives.
h=s.Function('h')(z)
eq(T(p*h)-h*T(p),2*z*(z+2)*p*s.diff(h,z)+2*z*z*s.diff(p,z)*s.diff(h,z)+z*z*p*s.diff(h,z,2))
# Verify derivative-root identity algebra modulo root constraint v=X^2-1.
t,uu,v,w=s.symbols('t uu v w')
DD=2*X*(t+uu-v)-2*(v-w)
eq(DD.subs({uu:X-t-2,v:X*X-1}),2*(w-X**3-X+1))
# Independent Touchard transform comparison for an arbitrary degree-five f.
x,rr=s.symbols('x rr')
f=sum(P[i]*x**i for i in range(6))
from sympy.functions.combinatorial.numbers import stirling
def bell(poly):
 poly=s.Poly(s.expand(poly),x)
 return s.expand(sum(co*sum(stirling(k,ell,kind=2)*z**ell for ell in range(k+1)) for (k,),co in poly.terms()))
hh=bell(f); pp=hh+2*s.diff(hh,z)+s.diff(hh,z,2); qq=s.diff(hh,z)+s.diff(hh,z,2)
raw=(x+rr+1)*(1+(x+1)+(x+1)**2)*f.subs(x,x+2)-(x+1)*(1+(x+1))*f.subs(x,x+1)
eq(bell(raw),L(L(L(pp)))+L(L(qq))+L(qq)+rr*T(pp))
print('PASS: exact differential, Bell, cubic-bound, root-reduction and quotient identities')
# Finite sanity checks, not the proof of all-degree theorem.
count=0
for aa in [[],[1],[2],[1,2],[1,2,3],[1,1,2],[0,0,1],[1,3,5,7]]:
 p=s.prod(z+a for a in aa); n=len(aa)
 import itertools
 for kk in range(min(2,n)+1):
  for active in itertools.combinations(range(n),kk):
   q=s.expand(sum(s.Rational(aa[i],2)*s.prod(z+aa[j] for j in range(n) if j!=i) for i in active))
   F=s.expand(L(L(L(p)))+L(L(q))+L(q)); TT=T(p)
   for rr in [-5,0,1,10]:
    poly=s.Poly(F+rr*TT,z)
    if sum(mult for _,mult in poly.intervals())!=poly.degree():raise RuntimeError((aa,active,rr))
    if rr>=0 and poly.count_roots(0,s.oo)>int(poly.eval(0)==0):raise RuntimeError('positive root')
    count+=1
print('PASS:',count,'exact finite pencil checks (diagnostic only)')
