"""Independent diagnostics for the anchored-color-class incomparability theorem."""
import sympy as s,json,random,itertools
from functools import lru_cache
from pathlib import Path
x,z=s.symbols('x z')
def closure(n,relations):
 R=[[False]*n for _ in range(n)]
 for i,j in relations:assert i<j;R[i][j]=True
 for k in range(n):
  for i in range(n):
   for j in range(n):R[i][j]=R[i][j] or (R[i][k] and R[k][j])
 return R

def principal_checks(R):
 n=len(R);L=s.Matrix([[int(not R[j][i]) for j in range(n)] for i in range(n)])
 for mask in range(1<<n):
  S=[i for i in range(n) if mask>>i&1]
  chain=all(R[i][j] or R[j][i] for i,j in itertools.combinations(S,2))
  assert L.extract(S,S).det()==int(chain)
 return 1<<n

def unsigned_chromatic(R):
 n=len(R);adj=[0]*n
 for i,j in itertools.combinations(range(n),2):
  if not R[i][j] and not R[j][i]:adj[i]|=1<<j;adj[j]|=1<<i
 independent=[True]*(1<<n)
 for mask in range(1,1<<n):
  bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit
  independent[mask]=independent[rest] and not(adj[i]&rest)
 @lru_cache(None)
 def parts(mask):
  if not mask:return (1,)
  bit=mask&-mask;rest=mask^bit;sub=rest;out=[0]*(mask.bit_count()+1)
  while True:
   block=bit|sub
   if independent[block]:
    for k,c in enumerate(parts(mask^block)):out[k+1]+=c
   if sub==0:break
   sub=(sub-1)&rest
  return tuple(out)
 return s.expand(sum((-1)**(n+k)*c*s.prod(x+j for j in range(k)) for k,c in enumerate(parts((1<<n)-1))))
def bell(p):return s.expand(sum(c*s.bell(m[0],z) for m,c in s.Poly(p,x).terms()))
def matching(R,anchors,k):
 keep=[i for i in range(len(R)) if i not in anchors];N=len(keep);nv=2*N+k-1;adj=[0]*nv
 def edge(i,j):adj[i]|=1<<j;adj[j]|=1<<i
 for i,I in enumerate(keep):
  for j,J in enumerate(keep):
   if i<j or (i>j and not R[J][I]):edge(i,N+j)
 for w in range(2*N,nv):
  for j in range(N):edge(w,N+j)
 @lru_cache(None)
 def rec(mask):
  if not mask:return (1,)
  bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit;out=list(rec(rest))+[0];nb=adj[i]&rest
  while nb:
   v=nb&-nb;nb^=v
   for j,c in enumerate(rec(rest^v)):out[j+1]+=c
  return tuple(out)
 return s.expand(sum(c*z**(N-j) for j,c in enumerate(rec((1<<nv)-1)) if c))
def actual_check(n,relations,classes,anchors):
 R=closure(n,relations);k=len(classes)
 assert sorted(sum(classes,[]))==list(range(n)) and len(anchors)==k
 for C,a in zip(classes,anchors):
  assert a in C
  assert all(R[i][j] or R[j][i] for i,j in itertools.combinations(C,2))
  for v in set(range(n))-set(C):assert not R[a][v] and not R[v][a]
 P=unsigned_chromatic(R);quotient,remainder=s.div(P,s.prod(x+j for j in range(k)),x)
 assert remainder==0
 B=bell(quotient);M=matching(R,set(anchors),k)
 assert s.expand(B-M)==0
 return {'n':n,'k':k,'classes':classes,'anchors':anchors,'quotient_Bell':str(B)}
random.seed(114703)
checks=0
for n in range(1,7):
 for t in range(8):
  R=closure(n,[(i,j) for i in range(n) for j in range(i+1,n) if random.random()<.3])
  checks+=principal_checks(R)
cases=[]
cases.append(actual_check(4,[(0,1),(1,2),(2,3)],[[0,1,2,3]],[1]))
# P4 poset, anchor middle path vertices 1 and2, chain classes {0,2},{1,3}.
cases.append(actual_check(4,[(0,2),(0,3),(1,3)],[[0,2],[1,3]],[2,1]))
# Three chains with anchored middle elements and cross low-to-high relations.
relations=[(i,3+i) for i in range(3)]+[(3+i,6+i) for i in range(3)]+[(0,7),(1,8),(2,6)]
cases.append(actual_check(9,relations,[[0,3,6],[1,4,7],[2,5,8]],[3,4,5]))
# Width four, odd/even sign and zero-extra boundary are separately exercised.
cases.append(actual_check(8,[(i,4+i) for i in range(4)],[[i,4+i] for i in range(4)],[4,5,6,7]))
# Strict bipartite seed K3,4 minus two independent edges.
seed_rel=[(0,2),(2,5),(1,3),(3,4),(4,6),(0,6),(1,5)]
cases.append(actual_check(7,seed_rel,[[0,2,5],[1,3,4,6]],[2,3]))
RR=closure(7,seed_rel)
edges=[(i,j) for i,j in itertools.combinations(range(7),2) if not RR[i][j] and not RR[j][i]]
def connected(vertices,edge_list):
 vertices=set(vertices)
 if not vertices:return True
 seen={min(vertices)}
 while True:
  more={v for a,b in edge_list for u,v in [(a,b),(b,a)] if u in seen and v in vertices}
  if more<=seen:return seen==vertices
  seen|=more
assert len(edges)==10 and connected(range(7),edges)
comp=[e for e in itertools.combinations(range(7),2) if e not in edges]
assert connected(range(7),comp)
for cut in [(i,) for i in range(7)]+edges:assert connected(set(range(7))-set(cut),edges)
assert {e for e in edges if set(e)<={0,1,5,6}}=={(0,1),(5,6)}
result={'status':'PASS','principal_minor_instances':checks,'actual_anchored_graph_cases':cases,'strict_seed_checks':{'n':7,'edges':10,'connected_and_coconnected':True,'no_vertex_or_edge_clique_separator':True,'induced_2K2_vertices':[0,1,5,6]},'scope':'finite independent diagnostics; universal proof uses the exact principal-minor and EGF arguments'}
Path(__file__).with_name('anchor_check_results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
