"""Exact checks accompanying symbolic proof; finite cases are not the proof."""
import functools,itertools,json,sympy as s
x,y,z=s.symbols('x y z');W=1+x+y;H=(1+x)*(1+y)
Lm=[1+y,W,W];Rm=[W,1+x];E=[[y,x*y/W],[W,x],[W,1+x]]
one=sum(E[i][j]*s.prod(Lm[k] for k in range(3) if k!=i)*Rm[1-j] for i in range(3) for j in range(2))
two=sum(E[i][0]*E[j][1]*Lm[3-i-j] for i in range(3) for j in range(3) if i!=j)
assert s.cancel(one-W**2*(6*H-2*W-1))==0
assert s.cancel(two-W*(6*H-4*W-1))==0
P=W*(z*z*W*W*H+z*W*(6*H-2*W-1)+6*H-4*W-1)
def coefficient(r,t):
 p=s.Poly(s.expand((1+x)**t*(1+y)**r*P),x,y)
 return s.expand(s.factorial(r)*s.factorial(t)*sum(c*z**(r+t-a-b)/(s.factorial(r-a)*s.factorial(t-b)) for (a,b),c in p.terms() if a<=r and b<=t))
def match(r,t,alpha=None,beta=None):
 N=5+2*r+2*t;adj=[{} for _ in range(N)]
 def edge(a,b,w=1):adj[a][b]=w;adj[b][a]=w
 for a,b in [(1,2),(2,3),(3,4)]:edge(a,b)
 for i in range(r):
  for c in [2,4]:edge(5+2*i,c)
  for c in [1,3]:edge(6+2*i,c)
 for j in range(t):
  edge(5+2*r+2*j,2)
  for c in [0,1,3]:edge(6+2*r+2*j,c)
 for i in range(r):
  for j in range(t):edge(5+2*i,6+2*r+2*j);edge(6+2*i,5+2*r+2*j)
 if alpha is not None:
  for i,w in enumerate(alpha):edge(5+2*i,6+2*i,w)
 if beta is not None:
  for j,w in enumerate(beta):edge(5+2*r+2*j,6+2*r+2*j,w)
 @functools.lru_cache(None)
 def f(mask):
  if not mask:return (s.Integer(1),)
  a=(mask&-mask).bit_length()-1;mask^=1<<a;v=list(f(mask))
  for b,w in adj[a].items():
   if mask>>b&1:
    q=f(mask^(1<<b));v += [0]*max(0,len(q)+1-len(v))
    for k,c in enumerate(q):v[k+1]+=w*c
  return tuple(v)
 return s.expand(sum(c*z**(r+t+2-k) for k,c in enumerate(f((1<<N)-1))))
C={}
for r in range(4):
 for t in range(4):
  C[r,t]=coefficient(r,t)
  assert C[r,t]==match(r,t),(r,t)
weighted=0
for r in range(4):
 for t in range(4):
  a=[s.Rational(i+1,2) for i in range(r)];b=[s.Rational(j+2,3) for j in range(t)]
  f=s.Poly(s.prod(z+c for c in a),z);g=s.Poly(s.prod(z+c for c in b),z)
  target=s.expand(sum(c*d*C[i[0],j[0]] for i,c in f.terms() for j,d in g.terms()))
  assert target==match(r,t,a,b),(r,t,'root_lift')
  weighted+=1
print(json.dumps({'status':'passed','symbolic_core_identities':2,'direct_graph_kernel_checks':16,'weighted_root_lift_checks':weighted,'scope':'checks supplement all-parameter proof'}))
