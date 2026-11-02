import sympy as s
z,w,r,y=s.symbols('z w r y')
def need(v,msg):
 if not v: raise RuntimeError(msg)
L=lambda f:s.expand(z*(f+s.diff(f,z))+f)
S=lambda f:s.expand(f+s.diff(f,z))
U0=s.Integer(1);us=[U0]
for _ in range(4):us.append(L(us[-1]))
R=s.expand(sum(us[:4]));U=us[4];V=R-1;W=U+r*R;A=S(W);C=W+V
res=687*r**5+1145*r**4+15987*r**3+29875*r**2+95694*r+101164
need(s.resultant(C,A,z)==res,'resultant')
need(all(v>0 for v in s.Poly(res,r).all_coeffs()),'resultant positive')
da=r**4*(1425*r*r-3160*r+2000)+r*r*(71778*r*r-24142*r+1202393)+438818*r+5525009
dc=229*r**6+916*r**5+9696*r**4+30428*r**3+136908*r**2+217360*r+422496
dw=r**4*(229*r*r-660*r+1000)+r*r*(7798*r*r-10122*r+10000)+(82229*r*r-47278*r+227081)
for f,d in [(A,da),(C,dc),(W,dw)]:need(s.expand(s.discriminant(f,z)-d)==0,'discriminant certificate')
for q in [1425*r*r-3160*r+2000,71778*r*r-24142*r+1202393,229*r*r-660*r+1000,7798*r*r-10122*r+10000,82229*r*r-47278*r+227081]:
 need(s.LC(s.Poly(q,r))>0 and s.discriminant(q,r)<0,'positive quadratic')
AI=[(-s.Rational(149,18),-s.Rational(91,11)),(-s.Rational(39,10),-s.Rational(74,19)),(-s.Rational(3,2),-s.Rational(106,71)),(-s.Rational(1,3),-s.Rational(18,55))]
CI=[(-s.Rational(193,28),-s.Rational(62,9)),(-s.Rational(32,11),-s.Rational(29,10)),(-s.Rational(101,100),-s.Rational(99,100)),(-s.Rational(1,5),-s.Rational(18,91))]
WI=[(-s.Rational(319,49),-s.Rational(332,51)),(-s.Rational(61,23),-s.Rational(53,20)),(-s.Rational(13,17),-s.Rational(16,21)),(-s.Rational(1,13),-s.Rational(1,14))]
for f,ints in [(A,AI),(C,CI),(W,WI)]:
 for lo,hi in ints:need(f.subs({r:0,z:lo})*f.subs({r:0,z:hi})<0,'base sign bracket')
for i in range(4):
 need(AI[i][1]<CI[i][0],'A before C')
 if i<3:need(CI[i][1]<AI[i+1][0],'C before next A')
# Classical half-vertex kernel factorization, retained as diagnostic.
B=S(W+V/2);K=y*y*S(S(W))+2*y*B+C
need(s.expand(K-(C+y*A+y*(C+s.diff(C,z)+y*(A+s.diff(A,z)))))==0,'kernel factorization')
def bell(f,g):
 return s.expand(sum(z**j*s.diff(f,z,j)*s.diff(g,z,j)/s.factorial(j) for j in range(min(s.degree(f,z),s.degree(g,z))+1)))
def Mop(f,yy):return s.expand(f+yy*(f+s.diff(f,w)))
# Symbolically check mass splitting and diagonal for rational weights, variable active roots.
for weights in [(s.Rational(1,3),s.Rational(1,6),s.Rational(1,4)),(s.Rational(3,4),s.Rational(1,8)),(0,s.Rational(1,2),0,s.Rational(1,2))]:
 n=len(weights);ys=s.symbols('y0:'+str(n));aa=s.symbols('a0:'+str(n));total=sum(weights)
 f=W.subs(z,w)+total*V.subs(z,w)+ys[0]*A.subs(z,w)
 for yy in ys[1:]:f=Mop(f,yy)
 b=[total]+[s.Integer(0)]*(n-1)
 for j in range(1,n):
  if b[0]==0:continue
  theta=1-weights[j]/b[0]
  need(0<=theta<=1,'valid splitting parameter')
  f=s.expand(theta*f+(1-theta)*f.xreplace({ys[0]:ys[j],ys[j]:ys[0]}))
  b[j]=(1-theta)*b[0];b[0]=theta*b[0]
 need(b==list(weights),'target mass vector')
 base=W.subs(z,w)
 for yy in ys:base=Mop(base,yy)
 for i,k in enumerate(weights):
  term=V.subs(z,w)
  for j,yy in enumerate(ys):
   if j!=i:term=Mop(term,yy)
  base+=k*term
 need(s.expand(f-base)==0,'mass splitting identity')
 p=s.prod(z+a for a in aa);q=sum(aa[i]*weights[i]*s.prod(z+aa[j] for j in range(n) if j!=i) for i in range(n))
 diag=s.expand(s.prod(aa)*f.subs({w:z,**{ys[i]:z/aa[i] for i in range(n)}}))
 need(s.expand(diag-bell(W,p)-bell(V,q))==0,'Bell diagonal identity')
# Independent finite root checks are diagnostics, not substitutes for proof.
cases=0
for av,kv in [([1],[s.Rational(3,4)]),([1,2],[s.Rational(3,4),s.Rational(1,4)]),([0,1,3],[s.Rational(1,4)]*3),([1,1,2,4],[s.Rational(1,8)]*4),([s.Rational(1,2),2,7],[0,0,1])]:
 p=s.prod(z+a for a in av);q=sum(av[i]*kv[i]*s.prod(z+av[j] for j in range(len(av)) if j!=i) for i in range(len(av)))
 for rv in [0,s.Rational(1,2),1,3]:
  f=s.Poly(bell(W.subs(r,rv),p)+bell(V,q),z)
  need(all(c>=0 for c in f.all_coeffs()),'positive output coefficients')
  need(sum(mult for _,mult in s.polys.polytools.intervals(f))==f.degree(),'finite exact real-root count')
  cases+=1
print('PASS exact scalar certificates; base interlacing; symbolic mass splitting and diagonal; '+str(cases)+' exact finite output checks')
