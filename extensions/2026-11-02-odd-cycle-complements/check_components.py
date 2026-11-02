if not __debug__:
    raise RuntimeError("Run without -O: verification requires active assertions")
# Separate exact checks of the component extension, using routines from verify.py.
# Importing verify also replays the original 88-case certificate.
import json
from pathlib import Path
import sympy as s
from verify import matching_counts,coefficients,z

def cycle(n):return n,[(i,(i+1)%n) for i in range(n)]
def star(leaves):return leaves+1,[(0,i) for i in range(1,leaves+1)]
def complete_bip(a,b):return a+b,[(i,a+j) for i in range(a) for j in range(b)]
def union(parts):
 n=0;es=[]
 for v,e in parts:es += [(x+n,y+n) for x,y in e];n+=v
 return n,es
records=[]
for tag,parts,S,c in [
 ('C5+C7',[cycle(5),cycle(7)],5,2),
 ('C5+K1,6',[cycle(5),star(6)],3,1),
 ('C7+K2,3',[cycle(7),complete_bip(2,3)],5,1),
 ('C5+4isolates',[cycle(5),(4,[])],2,1),
 ('3C5',[cycle(5)]*3,6,3),
]:
 n,es=union(parts);counts=matching_counts(n,es)
 assert S<=n-2 and n+c-S<=n-1
 for j in range(1,n-S+1):
  co=coefficients(n,j,counts);p=s.Poly.from_list(co[::-1],z)
  assert all(x>=0 for x in co)
  assert p.count_roots(-s.oo,0)==p.degree()
  records.append(dict(tag=tag,n=n,S=S,T=n+c-S,j=j,coefficients_ascending=co,exact_nonpositive_root_count=p.degree()))
Path(__file__).with_name('component_certificate.json').write_text(json.dumps(dict(cases=len(records),records=records),indent=2)+'\n')
print('PASS component checks:',len(records))
