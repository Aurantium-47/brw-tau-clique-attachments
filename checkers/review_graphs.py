"""Independent graph enumerations, separate from author symbolic certificate."""
import sympy as s, json
from functools import lru_cache
from pathlib import Path
x,z=s.symbols('x z')
def chromatic_subset(b):
 n=3+b;edges=[(i,3+j) for i in range(3) for j in range(b) if (i,j)!=(0,0)];co=[0]*(n+1)
 for mask in range(1<<len(edges)):
  parents=list(range(n))
  def root(i):
   while parents[i]!=i:i=parents[i]
   return i
  for k,(u,v) in enumerate(edges):
   if mask>>k&1:parents[root(u)]=root(v)
  comp=len({root(i) for i in range(n)})
  co[comp]+=(-1)**mask.bit_count()
 return sum(c*x**i for i,c in enumerate(co))
for b in range(2,6):
 chi=chromatic_subset(b);P=s.expand((-1)**(b+3)*chi.subs(x,-x))
 Q=(x+2)**2*(x+3)**(b-1)-(3*x+5)*(x+2)**(b-1)+(x+1)**(b-1)
 assert s.expand(P-x*(x+1)*Q)==0

def A(f):
 E=lambda h:s.expand(h+s.diff(h,z))
 L=lambda c,h:s.expand(z*E(h)+c*h)
 return s.expand(L(2,L(2,E(E(E(f)))))-3*L(0,E(E(f)))-5*E(E(f))+E(f))
def augmented(n):
 # core0=c,1=l1,2=l2,3=d,4=e,5=f,6=g
 edges=[(0,1,s.Integer(1)),(0,2,s.Integer(1))];alphas=[]
 for i in range(n):
  r,rp=7+2*i,8+2*i;alpha=[s.Integer(0),s.Rational(1,3),s.Integer(2),s.Rational(7,5)][i];alphas.append(alpha)
  edges += [(r,0,s.Rational(2,3)),(r,3,s.Rational(1,2)),(rp,0,s.Rational(1,3)),(rp,3,s.Rational(1,2))]
  edges += [(r,j,s.Integer(1)) for j in [4,5,6]]+[(r,rp,alpha)]
 adj=[[] for _ in range(7+2*n)]
 for u,v,w in edges:
  adj[u].append((v,w));adj[v].append((u,w))
 @lru_cache(None)
 def match(mask):
  if mask==0:return (s.Integer(1),)
  bit=mask&-mask;u=bit.bit_length()-1;rest=mask^bit;out=list(match(rest))+[s.Integer(0)]
  for v,w in adj[u]:
   if rest>>v&1:
    for k,c in enumerate(match(rest^(1<<v))):out[k+1]+=w*c
  return tuple(out)
 co=match((1<<(7+2*n))-1)
 assert all(c==0 for k,c in enumerate(co) if k>n+2)
 M=sum(c*z**(n+2-k) for k,c in enumerate(co) if c)
 assert s.expand(M-A(s.prod(z+a for a in alphas)))==0
for n in range(5):augmented(n)
result={'status':'PASS','independent_chromatic_subset_graphs':4,'independent_augmented_weighted_graphs':5}
Path(__file__).with_name('graph_review.json').write_text(json.dumps(result,indent=2));print(result)
