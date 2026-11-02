"""Independent set-partition enumeration of actual K_ab-e vs matching kernel."""
from functools import lru_cache
from math import factorial
import json
from pathlib import Path

def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):c[i+j]+=u*v
 return c

def graph_poly(a,b):
 n=a+b;adj=[0]*n
 for i in range(a):
  for j in range(a,n):
   if i==0 and j==a:continue
   adj[i]|=1<<j;adj[j]|=1<<i
 independent=[True]*(1<<n)
 for m in range(1,1<<n):
  v=m&-m;r=m^v;independent[m]=independent[r] and not(adj[v.bit_length()-1]&r)
 @lru_cache(None)
 def partitions(mask):
  if mask==0:return (1,)
  v=mask&-mask;rest=mask^v;sub=rest;out=[0]*(mask.bit_count()+1)
  while True:
   cls=sub|v
   if independent[cls]:
    for k,c in enumerate(partitions(mask^cls)):out[k+1]+=c
   if sub==0:break
   sub=(sub-1)&rest
  return tuple(out)
 sig=partitions((1<<n)-1);P=[0]*(n+1);rise=[1]
 for k,c in enumerate(sig):
  for j,w in enumerate(rise):P[j]+=(-1)**(n+k)*c*w
  rise=mul(rise,[k,1])
 assert P[0]==0;P=P[1:]
 Q=[0]*(len(P)-1);Q[-1]=P[-1]
 for j in range(len(Q)-2,-1,-1):Q[j]=P[j+1]-Q[j+1]
 assert P[0]==Q[0]
 return Q
T=[[1]]
for n in range(1,15):
 row=[0]*(n+1)
 for j,c in enumerate(T[-1]):row[j]+=j*c;row[j+1]+=c
 T.append(row)
def bell(Q):
 out=[0]*len(Q)
 for i,c in enumerate(Q):
  for j,t in enumerate(T[i]):out[j]+=c*t
 return out
@lru_cache(None)
def kernel(r,s):
 N=5+2*r+2*s;adj=[set() for _ in range(N)]
 def edge(i,j):adj[i].add(j);adj[j].add(i)
 for i,j in [(1,2),(2,3),(3,4)]:edge(i,j)
 for i in range(r):
  R=5+2*i;Rp=R+1
  for v in (2,4):edge(R,v)
  for v in (1,3):edge(Rp,v)
 for j in range(s):
  B=5+2*r+2*j;Bp=B+1;edge(B,2)
  for v in (0,1,3):edge(Bp,v)
  for i in range(r):edge(5+2*i,Bp);edge(6+2*i,B)
 @lru_cache(None)
 def count(mask):
  if not mask:return (1,)
  bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit;out=list(count(rest))+[0]
  for j in adj[i]:
   if rest>>j&1:
    for k,c in enumerate(count(rest^(1<<j))):out[k+1]+=c
  return tuple(out)
 counts=count((1<<N)-1);out=[0]*(r+s+3)
 for k,c in enumerate(counts):
  if c:assert k<=r+s+2;out[r+s+2-k]=c
 return tuple(out)
cases=[]
for a in range(2,6):
 for b in range(2,6):
  actual=bell(graph_poly(a,b));expected=[0]*(a+b-1)
  for r,cr in enumerate(T[a-2]):
   for s,cs in enumerate(T[b-2]):
    for k,c in enumerate(kernel(r,s)):expected[k]+=cr*cs*c
  assert actual==expected,(a,b,actual,expected)
  cases.append({'a':a,'b':b,'quotient_bell_ascending':actual})
result={'status':'PASS','method':'actual independent-set partitions vs direct matching deletion DP','cases':cases,'scope':'finite interface checks; universal proof is symbolic'}
Path(__file__).with_name('actual_graphs_certificate.json').write_text(json.dumps(result,indent=2));print(json.dumps({'status':'PASS','actual_graphs':len(cases)}))
