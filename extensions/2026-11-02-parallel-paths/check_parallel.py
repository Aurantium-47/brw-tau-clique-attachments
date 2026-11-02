if not __debug__: raise SystemExit('Assertions must remain enabled')
from itertools import product
from fractions import Fraction
import sympy as s
import json
from pathlib import Path
x,t=s.symbols('x t')
def S(n): return sum(t**j for j in range(n))
def quotient(ls): return s.Poly(s.prod(S(l) for l in ls)-t**(len(ls)-1)*s.prod(S(l-1) for l in ls),t)
def chromatic(ls):
 edges=[];n=2
 for l in ls:
  path=[0]+list(range(n,n+l-1))+[1];n+=l-1
  edges+=list(zip(path,path[1:]))
 co=[0]*(n+1)
 for mask in range(1<<len(edges)):
  par=list(range(n));k=n
  def root(a):
   while par[a]!=a:a=par[a]
   return a
  for j,(a,b) in enumerate(edges):
   if mask>>j&1:
    a,b=root(a),root(b)
    if a!=b:par[a]=b;k-=1
  co[k]+=(-1)**mask.bit_count()
 chi=sum(v*x**i for i,v in enumerate(co))
 return n, s.expand((-1)**n*chi.subs(x,-x))
rows=[]
for ls in [(2,2),(2,3),(2,2,3),(2,3,3),(2,2,2,2),(2,2,2,3),(2,2,2,2,2)]:
 n,P=chromatic(ls);Q=quotient(ls)
 assert s.expand(P-x*(x+1)*Q.as_expr().subs(t,x+1))==0
 assert Q.degree()==sum(ls)-len(ls)
 assert Q.all_coeffs()[1]==len(ls)-1
 rows.append({'lengths':ls,'vertices':n,'degree':Q.degree(),'actual_graph_formula':'PASS','trace':-(len(ls)-1)})
R=Fraction(21,20);bounds=[]
for r in [2,3,4,5,10,100,1000]:
 L=2
 while R**L<1+46*r:L+=1
 ratio=(R**L+R)/(R**L-1)
 assert ratio<=1+Fraction(1,22*r)
 assert ratio**r<Fraction(22,21)<R
 bounds.append({'paths':r,'sufficient_min_length':L})
out={'status':'PASS exact independent checks','graph_checks':rows,'threshold_examples':bounds,'threshold_constant_comparison':str(Fraction(41,920)-Fraction(1,22))}
Path(__file__).with_name('parallel_check_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
