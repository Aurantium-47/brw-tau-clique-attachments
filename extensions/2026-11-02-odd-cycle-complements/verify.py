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
records=[]
for n in range(5,26,2):
 m=n//2
 # Spine 0,...,n-2, with two additional leaves n-1,n at 0.
 edges=[(i,i+1) for i in range(n-2)]+[(0,n-1),(0,n)]
 counts=matching_counts(n+1,edges)
 expected=tuple(n*comb(n-k,k)//(n-k) for k in range(m+1))
 assert counts==expected
 A=[i for i in range(n-1) if i%2==0];B=[i for i in range(n-1) if i%2==1]+[n-1,n]
 assert (len(A),len(B))==(m,m+2)
 ai={v:i for i,v in enumerate(A)};bi={v:i for i,v in enumerate(B)}
 forbidden=[(ai[u],bi[v]) if u in ai else (ai[v],bi[u]) for u,v in edges]
 for j in range(1,m+2):
  co=coefficients(n,j,counts); p=s.Poly.from_list(co[::-1],z)
  assert all(c>=0 for c in co)
  assert p.count_roots(-s.oo,0)==p.degree()
  direct=False
  if n<=9:
   assert board(n-j,n-1,forbidden)==co;direct=True
  records.append(dict(n=n,j=j,degree=p.degree(),coefficients_ascending=co,exact_nonpositive_root_count=p.degree(),direct_allowed_board=direct))
 print('verified n =',n,flush=True)
Path(__file__).with_name('certificate.json').write_text(json.dumps(dict(cases=len(records),records=records),indent=2)+'\n')
print('PASS',len(records))
