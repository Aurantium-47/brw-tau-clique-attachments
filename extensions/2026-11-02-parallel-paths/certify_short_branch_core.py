"""Exact all-n matching identity for A; not finite numerical extrapolation."""
if not __debug__:raise SystemExit('Assertions required')
import itertools,json,sympy as s
from pathlib import Path
n=s.symbols('n');support=[1,2,4,5];av={1:0,2:s.Rational(1,2),4:0,5:0}
core=[([],s.S.One),([(0,1)],s.Integer(2)),([(1,2)],s.Rational(1,2)),([(2,3)],s.Rational(1,2)),([(0,1),(2,3)],s.S.One)]
counts={}
for edges,weight in core:
 blocked={v for e in edges for v in e};avail=[v for v in support if v not in blocked]
 for assignment in itertools.product(range(3),repeat=len(avail)):
  ac=assignment.count(1);bc=assignment.count(2);w=weight*s.ff(n,ac)*s.ff(n,bc)
  for v,k in zip(avail,assignment):
   if k==1:w*=av[v]
   elif k==2:w*=1-av[v]
  size=len(edges)+ac+bc;counts[size]=counts.get(size,0)+w
want=[1,4*n+3,6*n*n+4*n+1,4*s.ff(n,3)+11*s.ff(n,2)+4*n,s.ff(n,4)+4*s.ff(n,3)+3*s.ff(n,2)]
for k in range(5):assert s.expand(counts.get(k,0)-want[k])==0
assert all(s.expand(v)==0 for k,v in counts.items() if k>4)
# Independently derive normal differential operator from Bell identities.
z=s.symbols('z');f=s.Function('f')(z);E=lambda h:h+s.diff(h,z);L=lambda h:z*E(h)
A=L(L(E(E(f))))+3*L(E(E(f)))+3*E(E(f))-L(E(f))-2*E(f)
normal=z*z*E(E(E(E(f))))+z*E(E(3*f+4*s.diff(f,z)))+E(f+3*s.diff(f,z))
assert s.expand(A-normal)==0
coeff=[s.expand(normal).coeff(s.diff(f,z,j)) for j in range(5)]
# Formal monomial coefficient calculation, using derivative falling factorials.
for k,expected in enumerate(want):
 actual=0
 for j,c in enumerate(coeff):
  for (power,),value in s.Poly(c,z).terms():
   if 2+j-power==k:actual+=value*s.ff(n,j)
 assert s.expand(actual-expected)==0
out={'status':'PASS exact symbolic all-n identity','core_edges':[[0,1,'2'],[1,2,'1/2'],[2,3,'1/2']],'isolated_core_vertices':[4,5],'r_attachments':[[2,'1/2']],'r_prime_attachments':[[1,'1'],[2,'1/2'],[4,'1'],[5,'1']],'matching_counts':[str(s.factor(q)) for q in want],'symbolic_domain':'all integer n>=0; identities established as polynomials in n','normal_operator':'z^2(1+D)^4 + z(1+D)^2(3+4D) + (1+D)(1+3D)'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
