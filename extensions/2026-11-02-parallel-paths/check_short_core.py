if not __debug__: raise SystemExit('Assertions must remain enabled')
import sympy as s
import json
from pathlib import Path
u,a,b,n,z=s.symbols('u a b n z')
# Independent core-state polynomial: empty; each of three single edges;
# disjoint edge pair01,23. a,b mark distinct ordinary/primed leaf choices.
F=(1+b*u)**3*(1+(a+b)*u/2)+2*u*(1+b*u)**2*(1+(a+b)*u/2)+u*(1+b*u)**2/2+u*(1+b*u)**3/2+u*u*(1+b*u)**2
F=s.Poly(s.expand(F),u,a,b)
counts=[0]*5
for (k,i,j),c in F.terms():counts[k]+=c*s.ff(n,i)*s.ff(n,j)
counts=list(map(s.expand,counts))
# Independent expansion of the normal operator by E^d binomial coefficients.
terms=[]
for j in range(5):terms.append((2,j,s.binomial(4,j)))
for j in range(3):terms.append((1,j,3*s.binomial(2,j)));terms.append((1,j+1,4*s.binomial(2,j)))
terms +=[(0,0,1),(0,1,4),(0,2,3)]
want=[0]*5
for power,j,c in terms:want[2+j-power]+=c*s.ff(n,j)
assert all(s.expand(x-y)==0 for x,y in zip(counts,want))
# Exact genuine-graph quotient formula and Bell/operator identity, including k0.
def bell(p):
 P=s.Poly(s.expand(p),z);T=s.Integer(1);out=0
 for j in range(P.degree()+1):out+=P.nth(j)*T;T=s.expand(z*(T+s.diff(T,z)))
 return s.expand(out)
def A(f):return s.expand(sum(c*z**power*s.diff(f,z,j) for power,j,c in terms))
for k in range(9):
 Q=(z*z+3*z+3)*(z+2)**k-(z+1)**k*(z+2)
 assert s.expand(bell(Q)-A(bell(z**k)))==0
out={'status':'PASS independent core-state identity for all n','matching_coefficients':[str(s.factor(c)) for c in counts],'finite_Bell_interface_checks':list(range(9)),'method':'symbolic bivariate core-state polynomial, independent binomial operator expansion'}
Path(__file__).with_name('short_core_check_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
