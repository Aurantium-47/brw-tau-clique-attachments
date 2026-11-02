"""Independent stable-partition graph checks; no NetworkX dependency."""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import sympy as s
x,z=s.symbols('x z')
def need(ok,detail):
 if not ok: raise RuntimeError(str(detail))
def graph(n,edges):return (n,frozenset(tuple(sorted(e)) for e in edges))
def chromatic(G):
 n,edges=G
 independent=[all(not(mask>>u&1 and mask>>v&1) for u,v in edges) for mask in range(1<<n)]
 @lru_cache(None)
 def counts(mask):
  if not mask:return (1,)
  bit=mask&-mask;out=[0]*(mask.bit_count()+1);sub=mask
  while sub:
   if sub&bit and independent[sub]:
    for k,v in enumerate(counts(mask^sub)):out[k+1]+=v
   sub=(sub-1)&mask
  return tuple(out)
 return s.Poly(s.expand(sum((-1)**(n-k)*v*s.rf(x,k) for k,v in enumerate(counts((1<<n)-1)))),x)
def omega(G):
 n,E=G
 return max([0]+[len(S) for k in range(1,n+1) for S in combinations(range(n),k) if all(e in E for e in combinations(S,2))])
def B(poly):return s.Poly(sum(c*s.bell(k,z) for (k,),c in poly.terms()),z)
def check(G):
 P=chromatic(G);w=omega(G);vals=[]
 for j in range(w+1):
  q,r=s.div(P,s.Poly(s.rf(x,j),x));need(r.is_zero,('division',G,j));f=B(q)
  need(all(c>=0 for c in f.all_coeffs()),('sign',G,j))
  need(sum(h.count_roots(-s.oo,0)*m for h,m in f.sqf_list()[1])==f.degree(),('roots',G,j))
  vals.append(list(map(str,f.all_coeffs())))
 return vals
seeds=[graph(1,[]),graph(2,[]),graph(2,[(0,1)]),graph(3,[(0,1),(1,2)]),graph(3,[(0,1),(1,2),(0,2)]),graph(4,[(0,1),(1,2),(2,3)])]
records=[]
for i,A in enumerate(seeds):
 check(A)
 for j,BG in enumerate(seeds[i:],i):
  n,E=A;m,F=BG;shift={(u+n,v+n) for u,v in F}
  for operation in ['union','join']:
   edges=set(E)|shift
   if operation=='join':edges|={(u,v+n) for u in range(n) for v in range(m)}
   G=graph(n+m,edges);vals=check(G)
   records.append(dict(operation=operation,i=i,j=j,n=n+m,omega=omega(G),quotients=vals))
# Two triangles glued along an edge, and two triangles glued at a vertex.
for G in [graph(4,[(0,1),(0,2),(1,2),(0,3),(1,3)]),graph(5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)])]:
 records.append(dict(operation='clique_sum',n=G[0],omega=omega(G),quotients=check(G)))
(Path(__file__).resolve().parent/'graph_certificate.json').write_text(json.dumps(records,indent=2)+'\n')
print('PASS',len(records),'direct graph compositions; every quotient from j=0 to clique number checked exactly')
