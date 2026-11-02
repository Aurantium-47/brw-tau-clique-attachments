"""Independent exact finite checks for the all-parameter symbolic theorem."""
import functools,itertools,json,sympy as s
from sympy.functions.combinatorial.numbers import stirling
x,z=s.symbols('x z')
M=((0,1,1,1),(1,0,1,1),(0,1,0,1),(0,0,1,0))
def chromatic_by_partitions(sizes):
 types=[i for i,n in enumerate(sizes) for _ in range(n)];N=len(types)
 adj=[sum(1<<j for j,t in enumerate(types) if abs(t-types[i])==1) for i in range(N)]
 independent=[True]*(1<<N)
 for mask in range(1,1<<N):
  bit=mask&-mask;v=bit.bit_length()-1;independent[mask]=independent[mask^bit] and not(adj[v]&(mask^bit))
 @functools.lru_cache(None)
 def parts(mask):
  if not mask:return (1,)
  bit=mask&-mask;rest=mask^bit;sub=rest;out=[0]*(mask.bit_count()+1)
  while True:
   block=sub|bit
   if independent[block]:
    for k,c in enumerate(parts(mask^block)):out[k+1]+=c
   if not sub:break
   sub=(sub-1)&rest
  return tuple(out)
 return s.expand(sum(c*s.prod(x-j for j in range(k)) for k,c in enumerate(parts((1<<N)-1))))
def bell(f):return s.expand(sum(c*s.bell(k[0],z) for k,c in s.Poly(f,x).terms()))
@functools.lru_cache(None)
def matching(ns):
 types=[i for i,n in enumerate(ns) for _ in range(n)];n=len(types)
 # Left vertices0..n-1 plus universaln; right0..n-1 bitmask.
 adj=[[j for j,t in enumerate(types) if M[types[i]][t]] for i in range(n)]+[list(range(n))]
 d={0:1}
 for nbrs in adj:
  nd=dict(d)
  for mask,c in d.items():
   for j in nbrs:
    if not mask>>j&1:nd[mask|1<<j]=nd.get(mask|1<<j,0)+c
  d=nd
 return s.expand(sum(c*z**(n-mask.bit_count()) for mask,c in d.items()))
def kernel_touchard(ns):
 result=0
 for ks in itertools.product(*(range(n+1) for n in ns)):
  c=s.prod(stirling(n,k,kind=2) for n,k in zip(ns,ks))
  if c:result+=c*matching(tuple(ks))
 return s.expand(result)
results=[]
for sizes in itertools.product([1,2],repeat=4):
 n=sum(sizes);chi=chromatic_by_partitions(sizes);P=s.expand((-1)**n*chi.subs(x,-x));Q=s.cancel(P/(x*(x+1)))
 target=bell(Q);ns=(sizes[0],sizes[1]-1,sizes[2]-1,sizes[3])
 got=kernel_touchard(ns);assert got==target,(sizes,got,target)
 assert sum(m for bracket,m in s.polys.polytools.intervals(target,eps=s.Rational(1,100)))==s.degree(target,z)
 results.append({'sizes':sizes,'q_coefficients':s.Poly(target,z).all_coeffs()})
v=s.symbols('a b c d');U=s.diag(*v);Mat=s.Matrix(M);a,b,c,d=v;N=1-a*b-b*c-c*d-a*b*c-b*c*d;H=s.prod(1+t for t in v)
assert s.expand((s.eye(4)-U*Mat).det()-N)==0
one=s.ones(4,1);assert s.cancel(1+(one.T*(s.eye(4)-U*Mat).inv()*U*one)[0]-H/N)==0
print(json.dumps({'status':'passed','symbolic_matrix_identities':2,'actual_graph_vs_kernel_cases':len(results),'results':results,'scope':'finite checks supplement all-parameter proof'},default=lambda x:int(x),indent=2))
