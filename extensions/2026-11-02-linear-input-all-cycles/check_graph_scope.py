#!/usr/bin/env python3
import sympy as S
from itertools import combinations
z=S.symbols('z');n=9
edges=[(i,i+1) for i in range(5)]+[(6,7)]+[(u,v) for u in (0,5) for v in (6,7,8)]
def require(v,msg):
 if not v:raise RuntimeError(msg)
# Whitney subset expansion, independent of cycle quotient formula.
chi=0
for mask in range(1<<len(edges)):
 parent=list(range(n))
 def root(i):
  while parent[i]!=i:i=parent[i]
  return i
 for j,(u,v) in enumerate(edges):
  if mask>>j&1:parent[root(u)]=root(v)
 chi+=(-1)**mask.bit_count()*z**len({root(i) for i in range(n)})
chi=S.expand(chi)
Q=z**6-9*z**5+35*z**4-75*z**3+95*z**2-71*z+26
require(S.expand(chi-z*(z-1)*(z-2)*Q)==0,'independent graph chromatic polynomial')
lo=S.Rational(317,500)+S.I*S.Rational(247,250);hi=S.Rational(159,250)+S.I*S.Rational(99,100)
require(S.Poly(Q,z).count_roots(lo,hi)==1,'one root in exact complex rectangle')
margin=S.Rational(247,250)**2-S.Rational(159,250)-S.Rational(1,4)
require(margin==S.Rational(2817,31250) and margin>0,'whole rectangle outside closed parabola')
adj={i:set() for i in range(n)}
for u,v in edges:adj[u].add(v);adj[v].add(u)
def connected(vertices,AA):
 if len(vertices)<=1:return True
 seen={next(iter(vertices))};front=list(seen)
 while front:
  for w in AA[front.pop()]&vertices:
   if w not in seen:seen.add(w);front.append(w)
 return seen==vertices
cliques=[]
for k in range(1,n+1):
 for c in combinations(range(n),k):
  if all(v in adj[u] for u,v in combinations(c,2)):cliques.append(c)
require(max(map(len,cliques))==3,'clique number3')
require(all(len(adj[i])<n-1 for i in adj),'no universal vertex')
require(all(connected(set(range(n))-set(c),adj) for c in cliques),'no clique separator')
comp={i:set(range(n))-{i}-adj[i] for i in range(n)}
require(connected(set(range(n)),comp),'connected complement')
require(any(all(v in comp[u] for u,v in combinations(c,2)) for c in combinations(range(n),3)),'complement has triangles')
# Direct Bell transforms of all actual clique quotients, supporting check only.
P=S.expand((-1)**n*chi.subs(z,-z))
for j in range(1,4):
 quo,rem=S.div(P,S.prod(z+i for i in range(j)),z);require(rem==0,'clique divisibility')
 B=sum(c*sum(S.functions.combinatorial.numbers.stirling(k,l,kind=2)*z**l for l in range(k+1)) for (k,),c in S.Poly(quo,z).terms())
 require(S.Poly(B,z).count_roots(-S.oo,0)==S.degree(B,z),'Bell quotient nonpositive rooted')
print({'status':'PASS','vertices':n,'edges':len(edges),'subset_terms':2**len(edges),'clique_quotients':3,'rectangle_count':1,'margin':str(margin),'scope':'direct criterion separation, not novelty or exhaustive prior-class exclusion'})
