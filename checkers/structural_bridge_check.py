"""Independent finite diagnostics for a universal bilinear identity proved in the review."""
import sympy as s,json,random
from functools import lru_cache
from pathlib import Path
x,z=s.symbols('x z')
def rise(n):return s.prod(x+i for i in range(n))
def expansion(p):
 p=s.Poly(p,x);c={}
 while not p.is_zero:
  n=p.degree();a=p.LC();c[n]=a;p=s.Poly(p.as_expr()-a*rise(n),x)
 return c
def join(p,q):return s.expand(sum(a*b*rise(i+j) for i,a in expansion(p).items() for j,b in expansion(q).items()))
def bell(p):return s.expand(sum(a*s.bell(k[0],z) for k,a in s.Poly(p,x).terms()))
@lru_cache(None)
def kernel(r,t):
 N=5+2*r+2*t;adj=[0]*N
 def edge(u,v):adj[u]|=1<<v;adj[v]|=1<<u
 for u,v in [(1,2),(2,3),(3,4)]:edge(u,v)
 reds=[(5+2*i,6+2*i) for i in range(r)];blues=[(5+2*r+2*j,6+2*r+2*j) for j in range(t)]
 for a,b in reds:
  for c in [2,4]:edge(a,c)
  for c in [1,3]:edge(b,c)
 for a,b in blues:
  edge(a,2)
  for c in [0,1,3]:edge(b,c)
 for a,aa in reds:
  for b,bb in blues:edge(a,bb);edge(b,aa)
 @lru_cache(None)
 def match(mask):
  if not mask:return (1,)
  bit=mask&-mask;u=bit.bit_length()-1;rest=mask^bit;out=list(match(rest))+[0]
  nb=adj[u]&rest
  while nb:
   vbit=nb&-nb;nb^=vbit
   for k,c in enumerate(match(rest^vbit)):out[k+1]+=c
  return tuple(out)
 return s.expand(sum(c*z**(r+t+2-k) for k,c in enumerate(match((1<<N)-1)) if c))
def C(f,g):return s.expand(sum(a*b*kernel(i[0],j[0]) for i,a in s.Poly(f,z).terms() for j,b in s.Poly(g,z).terms()))
random.seed(20261102)
passed=0
for k in range(30):
 p=sum(random.randint(-3,3)*x**j for j in range(1,random.randint(2,5)))
 q=sum(random.randint(-3,3)*x**j for j in range(1,random.randint(2,5)))
 if p==0 or q==0:continue
 num=join(x*p,x*q)-x*join(p,q).subs(x,x+1)
 quotient,rem=s.div(num,x*(x+1),x);assert rem==0
 assert s.expand(bell(quotient)-C(bell(p/x),bell(q/x)))==0
 passed+=1
result={'status':'PASS','attempts':30,'nonzero_test_pairs_passed':passed,'kind':'arbitrary signed-polynomial bilinear identity, independent direct matching kernel','scope':'finite diagnostics only; universal proof is basis extension'}
Path(__file__).with_name('structural_bridge_results.json').write_text(json.dumps(result,indent=2));print(result)
