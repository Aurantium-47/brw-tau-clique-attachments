"""Independent P4 blow-up review: symbolic interfaces and actual graph enumeration."""
import sympy as s, json, itertools
from functools import lru_cache
from pathlib import Path
x,z=s.symbols('x z');u=s.symbols('a b c d');a,b,c,d=u
M=s.Matrix([[0,1,1,1],[1,0,1,1],[0,1,0,1],[0,0,1,0]])
U=s.diag(*u);N=1-a*b-b*c-c*d-a*b*c-b*c*d;H=s.prod(1+t for t in u)
assert s.expand((s.eye(4)-U*M).det()-N)==0
assert s.expand((s.eye(4)+U*(s.ones(4)-M)).det()-H)==0
Qminus=1/((1+a)*(1+c))+1/((1+a)*(1+d))+1/((1+b)*(1+d))-1/(1+a)-1/(1+d)
assert s.cancel(Qminus-N/H)==0
# Per-color support polynomial and differentiated fixed B,C labels.
tA,tB,tC,tD=s.symbols('tA tB tC tD')
Q=tA*tC+tA*tD+tB*tD-tA-tD
QB=tB*s.diff(Q,tB);QC=tC*s.diff(Q,tC)
assert s.diff(QB,tC)==0 and s.expand(QB*QC-tA*tB*tC*tD)==0

def bell(p):return s.expand(sum(co*s.bell(m[0],z) for m,co in s.Poly(p,x).terms()))
def chromatic_edge_subsets(sizes):
 starts=[];n=0
 for k in sizes:starts.append(list(range(n,n+k)));n+=k
 edges=[(i,j) for A,B in zip(starts,starts[1:]) for i in A for j in B]
 cs=[0]*(n+1)
 for mask in range(1<<len(edges)):
  par=list(range(n))
  def root(i):
   while i!=par[i]:i=par[i]
   return i
  for k,(i,j) in enumerate(edges):
   if mask>>k&1:par[root(i)]=root(j)
  cs[len({root(i) for i in range(n)})]+=(-1)**mask.bit_count()
 P=sum((-1)**(n+j)*co*x**j for j,co in enumerate(cs))
 quotient,remainder=s.div(P,x*(x+1),x);assert remainder==0
 return bell(quotient)

def matching(counts,alphas=None):
 left=[];right=[];offset=0
 for k in counts:
  left.append(list(range(offset,offset+k)));offset+=k
 n=offset
 for L in left:right.append([i+n for i in L])
 w=2*n;Nverts=w+1;adj=[{} for _ in range(Nverts)]
 def edge(i,j,weight=1):adj[i][j]=s.Rational(weight);adj[j][i]=s.Rational(weight)
 for i in range(4):
  for j in range(4):
   if M[i,j]:
    for v in left[i]:
     for vv in right[j]:edge(v,vv)
 for R in right:
  for v in R:edge(w,v)
 if alphas is not None:
  for i in range(4):
   for l,r,weight in zip(left[i],right[i],alphas[i]):edge(l,r,weight)
 @lru_cache(None)
 def rec(mask):
  if not mask:return (s.Integer(1),)
  bit=mask&-mask;v=bit.bit_length()-1;rest=mask^bit;out=list(rec(rest))+[s.Integer(0)]
  for j,weight in adj[v].items():
   if rest>>j&1:
    for k,co in enumerate(rec(rest^(1<<j))):out[k+1]+=weight*co
  return tuple(out)
 cs=rec((1<<Nverts)-1)
 assert all(co==0 for k,co in enumerate(cs) if k>n)
 return s.expand(sum(co*z**(n-k) for k,co in enumerate(cs) if co))
@lru_cache(None)
def kernel(counts):return matching(counts)
def multilinear(fs):
 out=0
 for terms in itertools.product(*(s.Poly(f,z).terms() for f in fs)):
  counts=tuple(m[0] for m,c in terms);co=s.prod(c for m,c in terms)
  out+=co*kernel(counts)
 return s.expand(out)
profiles=[(0,1,1,0),(1,1,1,1),(2,1,1,1),(1,2,1,2),(2,2,2,2),(2,1,2,2)]
for p,b,c,q in profiles:
 actual=chromatic_edge_subsets((p,b,c,q))
 predicted=multilinear([s.bell(k,z) for k in (p,b-1,c-1,q)])
 assert s.expand(actual-predicted)==0,(p,b,c,q)
weighted_counts=[(0,0,0,0),(1,0,0,1),(1,1,1,1),(2,1,0,1)]
for counts in weighted_counts:
 alphas=[[s.Rational(i+j,3) for j in range(k)] for i,k in enumerate(counts)]
 fs=[s.prod(z+a for a in A) for A in alphas]
 assert s.expand(matching(counts,alphas)-multilinear(fs))==0
result={'status':'PASS','symbolic_interfaces':['Qminus=N/H','det(I-UM)=N','rank-one augmented determinant=H','fixed middle-color derivative'], 'actual_graph_profiles':profiles,'direct_weighted_lifting_profiles':weighted_counts,'note':'Universal proof is the formal EGF/root-lifting argument; finite graphs are supplements.'}
Path(__file__).with_name('p4_check_results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
