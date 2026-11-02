if not __debug__: raise SystemExit('Assertions must remain enabled')
"""Exact rational base certificates for the fixed-source arrowhead induction.
No numerical roots are calculated or trusted by this checker.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def interval(poly,I):
 out=(F(0),F(0))
 for c in reversed(poly):out=add(mul(out,I),(F(c),F(c)))
 return out
def exact(poly,x):return interval(poly,(x,x))[0]
def derivative(p):return [i*p[i] for i in range(1,len(p))]
def divide(a,b):
 assert b[0]*b[1]>0
 return mul(a,(1/b[1],1/b[0]))
def nxt(p,h):
 q=[0]*(len(p)+1)
 for i,c in enumerate(p):q[i]+=(i+1)*c;q[i+1]+=c
 for i,c in enumerate(h):q[i]+=c
 return q
h=[7,12,3];p=[1,3,1]
# Fixed exact brackets: [n/d,(n+1)/d].
base=[([-26181,-3820],10000),([-61005,-23389,-5607],10000),([-74015,-37052,-15378,-3557],10000),([-95287,-49700,-23702,-9178,-2136],10000),([-1162810958,-660727567,-350632808,-158861933,-54542894,-12423842],100000000)]
records=[]
for m,(nums,d) in enumerate(base):
 assert len(nums)==len(p)-1
 rows=[];prev=None
 for i,n in enumerate(nums):
  I=(F(n,d),F(n+1,d));a,b=[exact(p,t) for t in I]
  assert I[1]<0 and a*b<0 and (prev is None or prev<I[0]);prev=I[1]
  row={'interval':[str(v) for v in I],'endpoint_signs':[1 if v>0 else -1 for v in (a,b)]}
  if m==4:
   den=mul((-I[1],-I[0]),interval(derivative(p),I))
   K=divide(interval(h,I),den);cap=F(1,20) if i<5 else F(1,3)
   assert -cap<K[0]<=K[1]<cap
   row.update(kappa_interval=[str(v) for v in K],absolute_kappa_cap=str(cap))
  rows.append(row)
 records.append({'m':m,'ascending_coefficients':p,'roots':rows})
 if m<4:p=nxt(p,h)
w=F(7,29);Vcap=5*F(1,20)**2/(1-F(1,20))+F(1,3)**2/(1-F(1,3))
assert w<=F(2,7) and Vcap==F(41,228) and Vcap<2*w
result={'status':'PASS','records':records,'base_m':4,'base_w':str(w),'V_upper_bound':str(Vcap),'two_w':str(2*w),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2))
