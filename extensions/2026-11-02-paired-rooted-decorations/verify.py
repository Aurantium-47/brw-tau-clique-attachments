if not __debug__:
    raise RuntimeError("Run without -O: verification requires active assertions")
"""Exact reproducible checks; no floating point and no external dependencies beyond SymPy."""
import json
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import sympy as s
z=s.symbols('z')
def matching_counts(n, edges):
 adj=[0]*n
 for u,v in edges: adj[u]|=1<<v;adj[v]|=1<<u
 @lru_cache(None)
 def rec(mask):
  if not mask:return (1,)
  bit=mask&-mask;v=bit.bit_length()-1;rest=mask^bit
  out=list(rec(rest)); nei=adj[v]&rest
  while nei:
   ub=nei&-nei;nei-=ub
   q=rec(rest^ub)
   if len(out)<len(q)+1:out += [0]*(len(q)+1-len(out))
   for k,c in enumerate(q):out[k+1]+=c
  while len(out)>1 and out[-1]==0:out.pop()
  return tuple(out)
 return rec((1<<n)-1)
def board(a,b,forbidden):
 blocked=[set() for _ in range(a)]
 for u,v in forbidden:blocked[u].add(v)
 states={0:1}
 for row in range(a):
  nxt=dict(states)
  for mask,c in states.items():
   for col in range(b):
    if col not in blocked[row] and not (mask>>col)&1:
     key=mask|1<<col;nxt[key]=nxt.get(key,0)+c
  states=nxt
 co=[0]*(a+1)
 for mask,c in states.items():co[a-mask.bit_count()]+=c
 return co
def coefficients(n,j,counts):
 a=n-j;b=n-1;co=[0]*(a+1)
 for k,m in enumerate(counts):
  for l in range(a-k+1):co[a-k-l]+=(-1)**k*m*comb(a-k,l)*comb(b-k,l)*factorial(l)
 return co

from itertools import combinations

def delete(n, edges, vertices):
 return matching_counts(n,[(u,v) for u,v in edges if u not in vertices and v not in vertices])

def color(n, edges):
 adj=[[] for _ in range(n)]
 for u,v in edges: adj[u].append(v);adj[v].append(u)
 c={}
 for root in range(n):
  if root in c: continue
  c[root]=0;stack=[root]
  while stack:
   u=stack.pop()
   for v in adj[u]:
    if v in c: assert c[v]!=c[u]
    else:c[v]=1-c[u];stack.append(v)
 return [[v for v in range(n) if c[v]==i] for i in (0,1)]

# Each template has distinguished root 0.
templates={
 'trivial':(1,[]),
 'leaf':(2,[(0,1)]),
 'path3_end':(3,[(0,1),(1,2)]),
 'path3_middle':(3,[(0,1),(0,2)]),
 'star4_center':(4,[(0,1),(0,2),(0,3)]),
 'star4_leaf':(4,[(0,1),(1,2),(1,3)]),
 'cycle4':(4,[(0,1),(1,2),(2,3),(3,0)]),
 'cycle6':(6,[(i,(i+1)%6) for i in range(6)]),
}
def construct(L, names):
 # Python labels are one less than mathematical labels.
 assert len(names)==(L-1)//2
 n=L;edges=[(i,i+1) for i in range(L-1)]
 for i,name in enumerate(names,start=1):
  q,te=templates[name]
  for root in (i,L-i):
   mp={0:root};mp.update({v:n+v-1 for v in range(1,q)})
   n+=q-1
   edges.extend((mp[u],mp[v]) for u,v in te)
 return n,edges,edges+[(0,L-1)],edges+[(n,1)]

cases=[(5,['trivial','trivial']),(5,['leaf','trivial']),
 (5,['trivial','leaf']),(5,['leaf','leaf']),
 (5,['path3_end','trivial']),(5,['path3_middle','trivial']),
 (5,['star4_center','leaf']),(5,['star4_leaf','leaf']),
 (5,['cycle4','trivial']),(5,['trivial','cycle4']),
 (5,['cycle6','leaf']),
 (7,['leaf','path3_middle','trivial']),
 (7,['cycle4','path3_end','leaf']),
 (9,['trivial','leaf','trivial','star4_leaf']),
 (11,['leaf','trivial','path3_middle','trivial','leaf'])]
records=[]
for L,names in cases:
 n,B,H,F=construct(L,names);s0=(n-1)//2
 hc=matching_counts(n,H);fc=matching_counts(n+1,F)
 assert hc==fc
 assert delete(n,B,{0,L-1})==delete(n,B,{1})
 A,C=sorted(color(n+1,F),key=len)
 assert (len(A),len(C))==(s0,s0+2)
 ai={v:i for i,v in enumerate(A)};ci={v:i for i,v in enumerate(C)}
 forbidden=[(ai[u],ci[v]) if u in ai else (ai[v],ci[u]) for u,v in F]
 checks=[]
 for j in range(1,s0+2):
  assert len(A)<=n-j and len(C)<=n-1
  co=coefficients(n,j,hc);p=s.Poly.from_list(co[::-1],z)
  assert all(c>=0 for c in co)
  assert p.count_roots(-s.oo,0)==p.degree()
  # Independently construct the rising quotient and apply Bell's transform.
  x=s.symbols('x')
  quotient=s.expand(sum((-1)**k*c*s.prod(x+i for i in range(j,n-k)) for k,c in enumerate(hc)))
  from sympy.functions.combinatorial.numbers import stirling
  bell=s.Poly(sum(c*sum(stirling(d,ell,kind=2)*z**ell for ell in range(d+1)) for (d,),c in s.Poly(quotient,x).terms()),z)
  assert bell==p
  direct=n<=9
  if direct:assert board(n-j,n-1,forbidden)==co
  checks.append(dict(j=j,coefficients_ascending=co,exact_nonpositive_roots=p.degree(),direct_board=direct))
 records.append(dict(cycle=L,decorations=names,original_n=n,surrogate_n=n+1,parts=[len(A),len(C)],matching_counts=hc,checks=checks))
 print('PASS paired',L,n,names,flush=True)

# Exhaust every labeled bipartite graph with <=6 vertices and exactly 5 edges.
# The proof establishes that every hypothetical C5 surrogate, after deleting
# isolates, has <=6 vertices, so this finite search certifies that classification.
obstruction=[];examined=0
for n in range(2,7):
 for a in range(1,n//2+1):
  all_edges=[(u,v) for u in range(a) for v in range(a,n)]
  for edges in combinations(all_edges,5):
   examined+=1
   if matching_counts(n,edges)!=(1,5,5):continue
   root_counts=[delete(n,edges,{v}) for v in range(n)]
   assert all(q!=(1,3,1) for q in root_counts)
   obstruction.append(dict(n=n,a=a,edges=edges,root_deleted_counts=root_counts))
assert obstruction
out=dict(paired_cases=len(records),quotient_cases=sum(len(r['checks']) for r in records),records=records,
 rooted_C5_obstruction=dict(examined_labeled_graphs=examined,matching_equivalent_graphs=obstruction))
Path(__file__).with_name('certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS ALL',out['paired_cases'],out['quotient_cases'],'obstruction candidates',len(obstruction))
