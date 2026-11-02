"""Exact small-graph checks of the coloring/quotient bridge, not an all-graph proof."""
import itertools
import sympy as s
from sympy.functions.combinatorial.numbers import stirling
x,z=s.symbols('x z')
def pg(n,edges):
 adj=[0]*n
 for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
 counts=[0]*(n+1)
 def visit(i,blocks):
  if i==n:counts[len(blocks)]+=1;return
  for j,mask in enumerate(blocks):
   if not mask&adj[i]:
    blocks[j]|=1<<i;visit(i+1,blocks);blocks[j]=mask
  blocks.append(1<<i);visit(i+1,blocks);blocks.pop()
 visit(0,[])
 return s.expand(sum((-1)**(n+k)*counts[k]*s.rf(x,k) for k in range(n+1)))
def omega(n,e):
 e={tuple(sorted(a)) for a in e}
 return max(len(v) for k in range(n+1) for v in itertools.combinations(range(n),k) if all((a,b) in e for a,b in itertools.combinations(v,2)))
def bell(p):
 return s.Poly(s.expand(sum(co*sum(stirling(k,j,kind=2)*z**j for j in range(k+1)) for (k,),co in s.Poly(p,x).terms())),z)
cases=[]
for n in range(1,4):
 ee=list(itertools.combinations(range(n),2))
 for mask in range(1<<len(ee)):cases.append((n,[e for i,e in enumerate(ee) if mask>>i&1]))
cases += [(4,[(0,1),(1,2),(2,3),(3,0)]),(5,[(i,(i+1)%5) for i in range(5)]),(4,list(itertools.combinations(range(4),2)))]
checks=0
for n,e in cases:
 r=omega(n,e); P=pg(n,e)
 u,a,b,v=range(n,n+4)
 eh=e+[(u,a),(a,b),(b,v)]+[(i,t) for i in range(n) for t in (u,v)]
 PH=pg(n+4,eh)
 rhs=x*(x+1)*((x*x+3*x+3)*P.subs(x,x+2)-(x+2)*P.subs(x,x+1))
 if s.expand(PH-rhs)!=0 or omega(n+4,eh)!=r+1:raise RuntimeError('bridge')
 for j in range(r+2):
  q,rem=s.div(PH,s.rf(x,j),x)
  if rem!=0:raise RuntimeError('divisibility')
  B=bell(q)
  if sum(mult for _,mult in B.intervals())!=B.degree():raise RuntimeError('nonreal')
  if B.count_roots(0,s.oo)>int(B.eval(0)==0):raise RuntimeError('positive')
  checks+=1
print('PASS:',len(cases),'independent stable-partition graph bridges;',checks,'exact output clique quotients')
