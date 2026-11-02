import sympy as S
s,v,w,x,u,k=S.symbols('s v w x u k')
def need(c,m):
 if not c:raise RuntimeError(m)
def delta(f):
 need(not f.has(x),'unsupported fifth moment needed')
 return S.expand((s-v)*S.diff(f,s)+2*(v-w)*S.diff(f,v)+3*(w-x)*S.diff(f,w)+u*(1-u)*S.diff(f,u))
def Lc(f):return S.expand(delta(f)+(s+1)*f)
P=[S.S(1)]
for i in range(4):P.append(Lc(P[-1]))
T=S.expand(sum(P[:4]));A=s**3+7*s**2+11*s+4-(3*s+7)*v+2*w
need(S.expand(T-A)==0,'formal T ratio')
B=3*s**2+14*s+11-3*v;C=3*s+7;D=B*(s-v)-2*C*(v-w)+6*(w-x)
need(delta(A)==S.expand(D),'formal derivative')
g=k*(1-u);Q=[g]
for i in range(3):Q.append(Lc(Q[-1]))
F=S.expand(P[4]+sum(Q[1:]));N=D+1-k*(1-u)*(1+B*u-2*C*u**2+6*u**3)
need(S.expand(F-N-(s+g)*A)==0,'formal off-root numerator')
print('PASS formal differential-ring identities for arbitrary moment symbols and one active summand; all summands by linearity')
