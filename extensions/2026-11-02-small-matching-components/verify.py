"""Exact checks using NetworkX/SymPy; run without python -O."""
if not __debug__: raise RuntimeError('Assertions required')
from functools import lru_cache
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import json
import networkx as nx
import sympy as s
x,z=s.symbols('x z')

def mc(G):
 G=nx.convert_node_labels_to_integers(G);adj=[sum(1<<v for v in G[u]) for u in G]
 @lru_cache(None)
 def rec(mask):
  if not mask:return (1,)
  bit=mask&-mask;v=bit.bit_length()-1;rest=mask^bit;out=list(rec(rest));nei=adj[v]&rest
  while nei:
   ub=nei&-nei;nei-=ub;q=rec(rest^ub)
   out += [0]*max(0,len(q)+1-len(out))
   for k,c in enumerate(q):out[k+1]+=c
  while len(out)>1 and not out[-1]:out.pop()
  return tuple(out)
 return rec((1<<len(G))-1)

def surrogate(H):
 rows=cols=0;E=[]
 for nodes in nx.connected_components(H):
  C=H.subgraph(nodes);r=len(mc(C))-1
  if not r:continue
  cover=next(set(c) for c in combinations(C,r) if all(u in c or v in c for u,v in C.edges))
  if C.subgraph(cover).number_of_edges()==0:
   A=sorted(cover);B=sorted(set(C)-cover)
   E.extend((rows+A.index(u),cols+B.index(v)) if u in cover else (rows+A.index(v),cols+B.index(u)) for u,v in C.edges)
   rows+=len(A);cols+=len(B)
  else:
   assert r==2
   u,v=cover;p,q=sorted([C.degree(u)-1,C.degree(v)-1]);assert p>=1
   E.extend((rows,col+cols) for col in range(p))
   E.extend((rows+1,col+cols) for col in range(q+1))
   rows+=2;cols+=q+1
 F=nx.Graph();F.add_nodes_from(range(rows+cols));F.add_edges_from((u,rows+v) for u,v in E)
 return rows,cols,E,F

def bell(p):
 coeff=[0]*(s.degree(p,x)+1)
 for (d,),v in s.Poly(p,x).terms():
  for k in range(d+1):coeff[k]+=int(v)*int(s.functions.combinatorial.numbers.stirling(d,k,kind=2))
 return coeff

def board(a,b,E):
 blocked=[set() for _ in range(a)]
 for u,v in E:blocked[u].add(v)
 states={0:1}
 for row in range(a):
  nxt=dict(states)
  for mask,c in states.items():
   for col in range(b):
    if col not in blocked[row] and not (mask>>col)&1:
     key=mask|1<<col;nxt[key]=nxt.get(key,0)+c
  states=nxt
 out=[0]*(a+1)
 for mask,c in states.items():out[a-mask.bit_count()]+=c
 return out

def ds(p,q):
 G=nx.Graph();G.add_edges_from([(0,1)]+[(0,i+2) for i in range(p)]+[(1,i+p+2) for i in range(q)]);return G

cases=[]
for i,H in enumerate(nx.graph_atlas_g()):
 if len(H) and nx.is_bipartite(H) and all(len(mc(H.subgraph(c)))<=3 for c in nx.connected_components(H)):
  cases.append(('atlas_'+str(i),H))
for p in range(1,7):
 for q in range(p,7):cases.append((f'D_{p}_{q}',ds(p,q)))
for spec in [[(2,2),(2,2)],[(2,3),(1,4)],[(2,2),(1,1),(1,2)]]:
 H=nx.Graph()
 for p,q in spec:H=nx.disjoint_union(H,ds(p,q))
 cases.append(('union_'+str(spec),H))
records=[];examples=[]
for name,H in cases:
 n=len(H);counts=mc(H);nu=len(counts)-1;rows,cols,E,F=surrogate(H)
 assert mc(F)==counts and rows==nu and cols<=n-nu
 if nu:assert cols<=n-1
 P=s.Poly(sum((-1)**k*m*s.rf(x,n-k) for k,m in enumerate(counts)),x)
 for j in range(1,n-nu+1):
  a=n-j;b=n-1;Q,rem=s.div(P,s.Poly(s.rf(x,j),x));assert rem.is_zero
  co=bell(Q.as_expr());expected=[0]*(a+1)
  for k,m in enumerate(counts):
   for l in range(a-k+1):expected[a-k-l]+=(-1)**k*m*comb(a-k,l)*comb(b-k,l)*factorial(l)
  assert co==expected and all(v>=0 for v in co)
  poly=s.Poly.from_list(co[::-1],z);assert poly.count_roots(-s.oo,0)==a
  direct=n<=8
  if direct:assert board(a,b,E)==co
  records.append(dict(name=name,n=n,j=j,nu=nu,coefficients_ascending=co,direct_board=direct,exact_nonpositive_roots=a))
 if name.startswith('union'):
  residual=s.div(P,s.Poly(s.rf(x,n-nu),x))[0]
  examples.append(dict(name=name,P_residual=str(residual.as_expr()),residual_degree=residual.degree(),real_root_count=int(residual.count_roots(-s.oo,s.oo))))
 print(name,'PASS',flush=True)
Path(__file__).with_name('certificate.json').write_text(json.dumps(dict(graphs=len(cases),quotients=len(records),records=records,union_chromatic_examples=examples),indent=2)+'\n')
print('PASS',len(cases),'graphs',len(records),'quotients');print(examples)
