import sympy as s
from itertools import combinations
x,z=s.symbols('x z')
def require(b):
 if not b: raise RuntimeError('exact graph check failed')
def chi(n,edges):
 co=[0]*(n+1)
 for mask in range(1<<len(edges)):
  parent=list(range(n))
  def find(a):
   while parent[a]!=a:a=parent[a]
   return a
  for j,(a,b) in enumerate(edges):
   if (mask>>j)&1:parent[find(a)]=find(b)
  co[len({find(a) for a in range(n)})]+=(-1)**mask.bit_count()
 return sum(v*x**i for i,v in enumerate(co))
def omega(n,edges):
 es={frozenset(e) for e in edges}
 return max(len(v) for k in range(1,n+1) for v in combinations(range(n),k) if all(frozenset(e) in es for e in combinations(v,2)))
def bell(f):
 return s.expand(sum(c*sum(s.functions.combinatorial.numbers.stirling(k,j,kind=2)*z**j for j in range(k+1)) for (k,),c in s.Poly(f,x).terms()))
fixtures=[(1,[]),(2,[(0,1)]),(2,[]),(3,[(0,1),(1,2)]),(4,[(0,1),(1,2),(2,3),(3,0)])]
for n,es in fixtures:
 # Five retained C6 vertices form length-four endpoint path.
 new=es+[(n+i,n+i+1) for i in range(4)]+[(i,j) for i in range(n) for j in [n,n+4]]
 cg=chi(n,es);ch=chi(n+5,new);r=omega(n,es)
 direct=((x-1)**4+(x-1))*cg.subs(x,x-1)+(x-1)*((x-1)**4-1)*cg.subs(x,x-2)
 require(s.expand(ch-direct)==0);require(omega(n+5,new)==r+1)
 P=s.expand((-1)**(n+5)*ch.subs(x,-x));Q,rem=s.div(P,s.prod(x+i for i in range(r+1)),x);require(rem==0)
 b=bell(Q);bp=s.Poly(b,z);require(bp.count_roots(-s.oo,s.oo)==bp.degree());require(all(c>=0 for c in bp.all_coeffs()))
 print(n,'vertices seed; output',n+5,'clique',r+1,'PASS')
print('PASS five independent Whitney graphs and maximal Bell quotients')
