import sympy as s
z,w,r=s.symbols('z w r');L=lambda f:s.expand(w*(f+s.diff(f,w))+f);S=lambda f:s.expand(f+s.diff(f,w))
def need(c,m):
 if not c:raise RuntimeError(m)
u=[s.Integer(1)]
for j in range(4):u.append(L(u[-1]))
R=s.expand(sum(u[:4]));V=R-1;W=s.expand(u[4]+r*R);A=S(W);C=s.expand(W+V)
DW=s.discriminant(W,w)
DWcert=r**4*(229*r*r-660*r+1000)+r*r*(7798*r*r-10122*r+10000)+(82229*r*r-47278*r+227081)
need(s.expand(DW-DWcert)==0,'W discriminant certificate')
for aa,bb,cc in [(229,-660,1000),(7798,-10122,10000),(82229,-47278,227081)]:
 need(aa>0 and bb*bb-4*aa*cc<0,'positive quadratic')
DC=s.Poly(s.discriminant(C,w),r)
need(all(c>0 for c in DC.all_coeffs()),'C discriminant positive coefficients')
res=s.resultant(C,A,w)
need(s.expand(res-(687*r**5+1145*r**4+15987*r**3+29875*r*r+95694*r+101164))==0,'C/A resultant')
need(s.Poly(W.subs(r,0),w).count_roots(-s.oo,0)==4,'W base roots')
AI=[(-9,-8),(-4,s.Rational(-38,10)),(s.Rational(-15,10),s.Rational(-14,10)),(s.Rational(-4,10),s.Rational(-3,10))]
CI=[(s.Rational(-69,10),s.Rational(-68,10)),(-3,s.Rational(-29,10)),(-1,-1),(s.Rational(-2,10),s.Rational(-1,10))]
for lo,hi in AI:need(s.Poly(A.subs(r,0),w).count_roots(lo,hi)==1,'A base interval')
for lo,hi in CI:need(s.Poly(C.subs(r,0),w).count_roots(lo,hi)==1,'C base interval')
for i in range(4):
 need(AI[i][1]<CI[i][0],'A before C')
 if i<3:need(CI[i][1]<AI[i+1][0],'C before next A')
# Original quadratic-kernel factorization.
y=s.symbols('y');K=y*y*S(S(W))+2*y*S(W+V/2)+C
need(s.expand(K-(C+y*A+y*S(C+y*A)))==0,'kernel factorization')
# Three-coordinate full symmetrization identity with symbolic masses.
yy=s.symbols('y0:3');k=s.symbols('k0:3');total=sum(k)
def M(f,j):return s.expand(f+yy[j]*(f+s.diff(f,w)))
def family(weights):
 f=W
 for j in range(3):f=M(f,j)
 for i in range(3):
  g=V
  for j in range(3):
   if j!=i:g=M(g,j)
  f+=weights[i]*g
 return s.expand(f)
P=family([total,0,0])
# First split target k2 into slot2; then k1 into slot1.
for j,mass,remain in [(2,k[2],total),(1,k[1],k[0]+k[1])]:
 swapped=P.xreplace({yy[0]:yy[j],yy[j]:yy[0]})
 P=s.cancel(((remain-mass)*P+mass*swapped)/remain)
need(s.expand(P-family(k))==0,'exact mass splitting')
# Bell recovery with nontrivial exact root parameters and symbolic masses/r.
aa=[s.Rational(1,3),2,5];p=s.prod(z+a for a in aa);q=sum(k[i]*aa[i]*s.prod(z+aa[j] for j in range(3) if j!=i) for i in range(3))
def star(f,g):
 return s.expand(sum(z**j*s.diff(f,z,j)*s.diff(g,z,j)/s.factorial(j) for j in range(min(s.degree(f,z),s.degree(g,z))+1)))
diag=s.prod(aa)*family(k).subs(dict(zip(yy,[z/a for a in aa]))).subs(w,z)
need(s.expand(diag-star(W.subs(w,z),p)-star(V.subs(w,z),q))==0,'Bell diagonal')
# Differential L operators equal Bell multiplication by their constant seeds.
Lz=lambda f:s.expand(z*(f+s.diff(f,z))+f)
pp=[p];qq=[q]
for j in range(4):pp.append(Lz(pp[-1]));qq.append(Lz(qq[-1]))
actual=pp[4]+sum(qq[1:4])+r*sum(pp[:4])
need(s.expand(diag-actual)==0,'actual abstract m4 operator')
print('PASS independent discriminants, resultant, exact root order, kernel factorization, symbolic mass splitting, Bell diagonal and abstract operator identity.')
