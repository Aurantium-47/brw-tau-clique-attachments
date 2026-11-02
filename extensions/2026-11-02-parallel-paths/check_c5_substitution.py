if not __debug__: raise SystemExit('Assertions must remain enabled')
import sympy as s,json
from pathlib import Path
x,z=s.symbols('x z')
def unsigned(n,edges):
 co=[0]*(n+1)
 for mask in range(1<<len(edges)):
  par=list(range(n));c=n
  def root(v):
   while par[v]!=v:v=par[v]
   return v
  for j,(a,b) in enumerate(edges):
   if mask>>j&1:
    a,b=root(a),root(b)
    if a!=b:par[a]=b;c-=1
  co[c]+=(-1)**(n+mask.bit_count()+c)
 return s.Poly.from_list(list(reversed(co)),x).as_expr()
def bell(p):
 p=s.Poly(p,x);T=s.Integer(1);out=0
 for i in range(p.degree()+1):out+=p.nth(i)*T;T=s.expand(z*(T+s.diff(T,z)))
 return s.expand(out)
def E(f):return f+s.diff(f,z)
def A(f):return s.expand(z*z*E(E(E(E(f))))+z*E(E(3*f+4*s.diff(f,z)))+E(f+3*s.diff(f,z)))
rows=[]
for name,n,ed in [('empty',0,[]),('K1',1,[]),('E2',2,[]),('K2',2,[(0,1)]),('P3',3,[(0,1),(1,2)]),('K3',3,[(0,1),(1,2),(0,2)]),('C4',4,[(0,1),(1,2),(2,3),(3,0)])]:
 F=unsigned(n,ed);u,a,b,v=range(n,n+4);he=ed+[(u,a),(a,b),(b,v)]+[(i,j) for i in range(n) for j in [u,v]]
 H=unsigned(n+4,he);Q=(x*x+3*x+3)*F.subs(x,x+2)-(x+2)*F.subs(x,x+1)
 assert s.expand(H-x*(x+1)*Q)==0
 assert s.expand(bell(Q)-A(bell(F)))==0
 rows.append({'input':name,'vertices':n+4,'edges':len(he),'graphic_and_Bell_identity':'PASS','edge_quotient':str(s.expand(Q))})
Path(__file__).with_name('c5_substitution_check_results.json').write_text(json.dumps({'status':'PASS independent actual-graph edge-subset checks','cases':rows},indent=2)+'\n')
print(json.dumps(rows,indent=2))
