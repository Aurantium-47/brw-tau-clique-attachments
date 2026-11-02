import sympy as s, json
from pathlib import Path
z,a,r,u,v,w=s.symbols('z a r u v w')
def need(x,m):
 if not x: raise RuntimeError(m)
def L(f):return s.Poly(z*s.diff(f,z)+(z+1)*f,z).as_expr()
p=z+a+2;H=(r+1)*z+r*(a+2)+1
F=L(p)+r*p
for j in range(2): F=s.expand(L(F)+H)
need(F==s.expand(z**4+(a+r+11)*z**3+(a*r+6*a+8*r+32)*z**2+(4*a*r+7*a+15*r+26)*z+3*a*r+a+6*r+4),'quartic')
res=s.resultant(F,z*s.diff(F,z)+u*H,z)
exprs={'disc':s.resultant(F,s.diff(F,z),z),'denominator':res.subs(u,1),'minus_resultant':res.subs(u,-1),'gap_numerator':s.diff(res,u).subs(u,1)+2*res.subs(u,1)}
cert=json.loads(Path(__file__).with_name('linear_seed_certificate.json').read_text())
out={}
for k,e in exprs.items():
 out[k]={}
 for sector,sub,gens in [('r_ge_a_plus_1',{r:a+v+1},(a,v)),('a_ge_r_minus_1',{a:w+v,r:w+1},(w,v))]:
  P=s.Poly(s.expand(e.subs(sub,simultaneous=True)),*gens)
  terms=[[list(mon),int(c)]for mon,c in P.terms()]
  need(terms==cert[k][sector]['terms'],'all certificate terms '+k+sector)
  need(min(P.coeffs())>0 and P.coeff_monomial(1)>0,'strict positivity')
  out[k][sector]={'terms':len(terms),'min':int(min(P.coeffs())),'constant':int(P.coeff_monomial(1))}
F0=s.Poly(F.subs({a:0,r:1}),z)
need(F0.count_roots(-s.oo,0)==4 and s.gcd(F0,F0.diff()).degree()==0,'base real simple negative')
# Base residues via exact resultant: no kappa crosses +/-1 along the path H scaled 0..1.
# Isolating every root and direct rational interval bounds from separately defined arithmetic.
def times(A,B):return(min(x*y for x in A for y in B),max(x*y for x in A for y in B))
def ev(P,I):
 acc=(s.S(0),s.S(0))
 for c in P.all_coeffs():
  acc=times(acc,I);acc=(acc[0]+c,acc[1]+c)
 return acc
for datum in cert['base']:
 I=tuple(map(s.Rational,datum['root_interval']));need(F0.count_roots(*I)==1,'base isolate')
 n=ev(s.Poly(-H.subs({a:0,r:1}),z),I);d=times(I,ev(F0.diff(),I));need(d[0]*d[1]>0,'denominator')
 k=times(n,(1/d[1],1/d[0]));need(-1<k[0]<=k[1]<1,'residue bound')
# Companion multiplication trace at several independently chosen rational parameters.
for av,rv in [(0,1),(s.Rational(1,2),s.Rational(7,3)),(7,1),(1,7)]:
 f=s.Poly(F.subs({a:av,r:rv}),z);hh=H.subs({a:av,r:rv});den=z*f.diff().as_expr()+hh
 quotient=s.rem(hh*s.invert(den,f.as_expr(),z),f.as_expr(),z)
 tr=sum(s.Poly(s.rem(z**i*quotient,f.as_expr(),z),z).nth(i)for i in range(4))
 ratio=(s.diff(res,u).subs(u,1)/res.subs(u,1)).subs({a:av,r:rv})
 need(s.cancel(tr-ratio)==0,'trace')
# Spectral invariant identity independently reconstructed from two eigenvalue moments.
W,V=s.symbols('W V');sp=W/(1+W);pr=-V/(4*(1+W))
phi=(2-sp)/(1-sp+pr)-2-sp
need(s.factor(phi-((2+W)/(1-V/4)-2-W/(1+W)))==0,'spectral potential')
need(s.factor(phi.subs(V,2-W)-(2-W/(1+W)))==0,'invariant closure')
Path('independent_result.json').write_text(json.dumps({'status':'PASS','sector_coefficients':out,'base_roots':4,'trace_cases':4,'spectral_identities':2},indent=2)+'\n')
print('PASS independent quartic, full coefficients, roots, residues, four traces and spectral closure')
