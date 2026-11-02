import sympy as s,json,itertools
from pathlib import Path
x=s.symbols('x');n=9
# Path 0--1--2--3--4--5; substituted graph on6,7,8, edge6--7.
edges=[(i,i+1)for i in range(5)]+[(6,7)]+[(v,w)for v in [0,5]for w in [6,7,8]]
c=[0]*(n+1)
for mask in range(1<<len(edges)):
 p=list(range(n))
 def find(v):
  while p[v]!=v:
   p[v]=p[p[v]];v=p[v]
  return v
 for j,(a,b)in enumerate(edges):
  if (mask>>j)&1:p[find(a)]=find(b)
 k=len({find(i)for i in range(n)});c[k]+=(-1)**mask.bit_count()
chi=sum(v*x**j for j,v in enumerate(c));quot=s.cancel(chi/(x*(x-1)*(x-2)))
expected=x**6-9*x**5+35*x**4-75*x**3+95*x**2-71*x+26
if s.expand(quot-expected)!=0:raise RuntimeError('polynomial mismatch')
E={frozenset(e)for e in edges};cliques=[set(v)for k in range(n+1)for v in itertools.combinations(range(n),k)if all(frozenset(e)in E for e in itertools.combinations(v,2))]
omega=max(map(len,cliques))
if omega!=3:raise RuntimeError('clique number')
lo=s.Rational(634,1000)+s.I*s.Rational(988,1000);hi=s.Rational(636,1000)+s.I*s.Rational(990,1000)
Q=s.Poly(quot,x)
count=Q.count_roots(lo,hi)
if count!=1:raise RuntimeError('root rectangle count')
margin=s.Rational(988,1000)**2-s.Rational(636,1000)-s.Rational(1,4)
if margin!=s.Rational(2817,31250):raise RuntimeError('margin')
# Check nonzero boundary edges: gcd real and imaginary restricted edge polynomial.
t=s.symbols('t',real=True)
for z in [s.Rational(634,1000)+s.I*t,s.Rational(636,1000)+s.I*t,t+s.I*s.Rational(988,1000),t+s.I*s.Rational(990,1000)]:
 e=s.expand_complex(quot.subs(x,z));re,im=s.expand(e).as_real_imag()
 if s.Poly(s.gcd(re,im),t).degree()!=0:raise RuntimeError('possible boundary root')
# Finite direct structural diagnostics, not an exhaustive closure classification.
def components(verts):
 p={i:i for i in verts}
 def f(i):
  if p[i]!=i:p[i]=f(p[i])
  return p[i]
 for a,b in edges:
  if a in p and b in p:p[f(a)]=f(b)
 return len({f(i)for i in p})
separators=[sorted(K)for K in cliques if len(K)<n and components(set(range(n))-K)>1]
comp_edges=[(a,b)for a,b in itertools.combinations(range(n),2)if frozenset((a,b))not in E]
p=list(range(n))
def f(i):
 if p[i]!=i:p[i]=f(p[i])
 return p[i]
for a,b in comp_edges:p[f(a)]=f(b)
complement_connected=len({f(i)for i in range(n)})==1
indep=max(len(v)for k in range(n+1)for v in itertools.combinations(range(n),k)if all(frozenset(e)not in E for e in itertools.combinations(v,2)))
# A last C5 single-vertex substitution would require a five-vertex module.
modules=[]
for tup in itertools.combinations(range(n),5):
 M=set(tup);O=set(range(n))-M
 if not all(len({frozenset((v,w))in E for v in M})==1 for w in O):continue
 ce=[(a,b)for a,b in itertools.combinations(O,2)if frozenset((a,b))in E]+[(9,w)for w in O if frozenset((tup[0],w))in E]
 deg={v:0 for v in O|{9}}
 for a,b in ce:deg[a]+=1;deg[b]+=1
 if len(ce)==5 and all(v==2 for v in deg.values()):modules.append(sorted(M))
universal=[v for v in range(n)if all(frozenset((v,w))in E for w in set(range(n))-{v})]
result={'status':'PASS','vertices':n,'edges':edges,'chi':str(s.expand(chi)),'maximal_chromatic_quotient':str(quot),'clique_number':omega,'root_rectangle_count':int(count),'parabolic_margin':str(margin),'clique_separators':separators,'complement_connected':complement_connected,'independence_number':indep,'possible_last_C5_substitution_modules':modules,'universal_vertices':universal}
Path('graph_independent_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
