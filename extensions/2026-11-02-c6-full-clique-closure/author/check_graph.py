import sympy as s
from itertools import combinations
x,z,k=s.symbols('x z k')
def need(c,msg):
 if not c:raise RuntimeError(msg)
def chrom(n,edges):
 coeff=[0]*(n+1)
 for mask in range(1<<len(edges)):
  parent=list(range(n));parts=n
  def root(a):
   while parent[a]!=a:
    a=parent[a]
   return a
  for j,(a,b) in enumerate(edges):
   if mask>>j&1:
    ra,rb=root(a),root(b)
    if ra!=rb:parent[ra]=rb;parts-=1
  coeff[parts]+=(-1)**mask.bit_count()
 return s.Poly(sum(c*x**i for i,c in enumerate(coeff)),x).as_expr()
def omega(n,edges):
 es={tuple(sorted(e)) for e in edges}
 return max(len(vs) for j in range(n+1) for vs in combinations(range(n),j) if all(tuple(sorted(e)) in es for e in combinations(vs,2)))
def bell(f):
 f=s.Poly(f,x);return s.Poly(sum(c*s.bell(int(mon[0]),z) for mon,c in f.terms()),z)
def rising(j):return s.prod(x+i for i in range(j))
A=s.Integer(1);D=s.Integer(0)
for _ in range(4):A,D=s.expand((k-1)*D),s.expand(A+(k-2)*D)
need(s.expand(A-(k-1)*(k*k-3*k+3))==0,'same endpoint walk count')
need(s.expand(D-(k-2)*(k*k-2*k+2))==0,'distinct endpoint walk count')
cases=0;quotients=0
for n,edges in [(1,[]),(2,[]),(2,[(0,1)]),(3,[(0,1)]),(3,[(0,1),(1,2)])]:
 r=omega(n,edges);cg=chrom(n,edges);pg=s.expand((-1)**n*cg.subs(x,-x))
 # u,a,b,c,v are new path vertices, four edges along the remaining path.
 new=list(range(n,n+5));he=list(edges)+list(zip(new,new[1:]))+[(j,new[0]) for j in range(n)]+[(j,new[-1]) for j in range(n)]
 N=n+5;ch=chrom(N,he);ph=s.expand((-1)**N*ch.subs(x,-x))
 need(omega(N,he)==r+1,'C6 maximum clique')
 form=x*(x+1)*((x+2)*(x*x+2*x+2)*pg.subs(x,x+2)-(x*x+3*x+3)*pg.subs(x,x+1))
 need(s.expand(ph-form)==0,'independent Whitney graph identity')
 f=s.div(pg,rising(r),x);need(f[1]==0,'seed clique quotient division')
 q=(x+r+1)*(x+2)*(x*x+2*x+2)*f[0].subs(x,x+2)-(x+1)*(x*x+3*x+3)*f[0].subs(x,x+1)
 need(s.expand(ph-rising(r+1)*q)==0,'maximal quotient normalization')
 for j in range(1,r+2):
  g,rem=s.div(ph,rising(j),x);need(rem==0,'actual clique quotient division');bg=bell(g)
  need(all(c>=0 for c in bg.all_coeffs()),'Bell coefficient positivity')
  need(sum(mult for _,mult in s.polys.polytools.intervals(bg))==bg.degree(),'exact clique quotient real-rootedness')
  quotients+=1
 cases+=1
print('PASS endpoint walk recurrence and '+str(cases)+' independent Whitney C6 graphs / '+str(quotients)+' exact Bell quotient checks')
