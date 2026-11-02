"""Portable exact certificate replay; no floating-point roots."""
if not __debug__:
 raise SystemExit("Refusing optimized Python: exact replay requires assertions enabled.")
import sys,json,math
from pathlib import Path
from functools import lru_cache
import networkx as nx
import sympy as s
x=s.Symbol('x')
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]+=u*v
 return c
def graphpoly(G):
 n=len(G);adj=[sum(1<<v for v in G[i]) for i in range(n)]
 ind=[True]*(1<<n)
 for m in range(1,1<<n):
  a=m&-m;r=m^a;ind[m]=ind[r] and not(adj[a.bit_length()-1]&r)
 @lru_cache(None)
 def parts(m):
  if not m:return (1,)
  a=m&-m;t=m^a;ans=[0]*(m.bit_count()+1)
  while True:
   cl=t|a
   if ind[cl]:
    for k,v in enumerate(parts(m^cl)):ans[k+1]+=v
   if not t:break
   t=(t-1)&(m^a)
  return tuple(ans)
 coeff=parts((1<<n)-1);out=[0]*(n+1);fac=[1]
 for k,v in enumerate(coeff):
  for j,w in enumerate(fac):out[j]+=(-1)**(n+k)*v*w
  fac=mul(fac,[k,1])
 return out
T=[[1]]
for n in range(1,30):
 r=[0]*(n+1)
 for k,v in enumerate(T[-1]):r[k]+=k*v;r[k+1]+=v
 T.append(r)
def bell(p):
 a=[0]*len(p)
 for i,c in enumerate(p):
  for j,v in enumerate(T[i]):a[j]+=c*v
 return a
def div(p,j):
 q=[0]*(len(p)-1);q[-1]=p[-1]
 for k in range(len(q)-2,-1,-1):q[k]=p[k+1]-j*q[k+1]
 assert p[0]==j*q[0]
 return q
def rr(p):
 f=s.Poly.from_list(p[::-1],x)
 return sum(m for r,m in f.intervals())==f.degree()

OUT=Path(__file__).parent

def board_counts(rows,b):
 dp={0:1}
 for adj in rows:
  nd=dp.copy()
  for used,v in dp.items():
   for j in adj:
    if not used>>j&1:nd[used|1<<j]=nd.get(used|1<<j,0)+v
  dp=nd
 out=[0]*(len(rows)+1)
 for used,v in dp.items():out[used.bit_count()]+=v
 return out

def check(G,tag):
 n=len(G);H=nx.complement(G)
 if n==2:
  assert G.number_of_edges()==1
  return {'tag':tag,'n':2,'quotient_bell':[1]}
 colors=nx.bipartite.color(H)
 A=[v for v in H if colors[v]==0];B=[v for v in H if colors[v]==1]
 if not H.number_of_edges():A=[0];B=list(range(1,n))
 if len(A)>len(B):A,B=B,A
 assert len(A)<=n-2 and len(B)<=n-1
 bi={v:j for j,v in enumerate(B)}
 forbidden=[{bi[v] for v in H[u]} for u in A]+[set() for _ in range(n-2-len(A))]
 Jrows=[set(range(n-1))-r for r in forbidden]
 counts=board_counts(Jrows,n-1)
 matched=counts[::-1]
 p=graphpoly(G);q=div(div(p,0),1);actual=bell(q)
 assert actual==matched,(tag,actual,matched)
 assert rr(actual)
 # independent inclusion-exclusion from forbidden-board rook counts
 mk=board_counts(forbidden,n-1);inc=[0]*(n-1)
 for k,m in enumerate(mk):
  for j in range(n-1-k):
   inc[n-2-k-j]+=(-1)**k*m*math.comb(n-2-k,j)*math.comb(n-1-k,j)*math.factorial(j)
 assert inc==actual
 clique_checks=[]
 for j in range(1,len(B)+1):
  fq=p
  for c in range(j):fq=div(fq,c)
  rows=[set(range(n-1))-{bi[v] for v in H[u]} for u in A]+[set(range(n-1)) for _ in range(n-j-len(A))]
  bj=bell(fq);mj=board_counts(rows,n-1)[::-1]
  assert bj==mj and rr(bj),(tag,j)
  clique_checks.append({'j':j,'quotient_bell':bj,'exact_real':True})
 return {'clique_checks':clique_checks,'tag':tag,'n':n,'edges':list(G.edges()),'complement_parts':[A,B], 'forbidden_rows':[sorted(r) for r in forbidden], 'P':p,'quotient':q,'quotient_bell':actual,'matching_counts':counts,'exact_real':True}
records=[]
for i,G in enumerate(nx.graph_atlas_g()):
 if len(G)>=2 and G.number_of_edges() and nx.is_bipartite(nx.complement(G)):
  records.append(check(G,'atlas_'+str(i)))
# Deterministic structured larger examples, not a random search.
for n in range(8,13):
 for typ in ['path','cycle_even','double_star','complete_bipartite']:
  if typ=='path':H=nx.path_graph(n)
  elif typ=='cycle_even':
   if n%2:continue
   H=nx.cycle_graph(n)
  elif typ=='double_star':H=nx.Graph();H.add_nodes_from(range(n));H.add_edge(0,1);H.add_edges_from((0,v) if v%2 else (1,v) for v in range(2,n))
  else:H=nx.complete_bipartite_graph(n//2,n-n//2)
  records.append(check(nx.complement(H),f'{typ}_{n}'))
computed=json.loads(json.dumps({'count':len(records),'records':records}))
expected=json.loads((OUT/'certificate.json').read_text())
assert computed==expected, 'Certificate mismatch'
assert sum(len(r.get('clique_checks',[])) for r in records)==663
print('PASS',len(records),'exact identities and exact RR checks')
