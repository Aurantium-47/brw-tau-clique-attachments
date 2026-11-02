"""Independent exact actual-graph and matching checks; not a substitute for the proof."""
import functools,itertools,json,sympy as s
x,z=s.symbols('x z')
def poset(chains,cross):
 n=sum(map(len,chains));rel=[[False]*n for _ in range(n)]
 for chain in chains:
  for i,a in enumerate(chain):
   for b in chain[i+1:]:rel[a][b]=True
 for a,b in cross:rel[a][b]=True
 before=[r[:] for r in rel]
 for k in range(n):
  for i in range(n):
   for j in range(n):rel[i][j]|=rel[i][k] and rel[k][j]
 assert not any(rel[i][i] for i in range(n))
 assert rel==before,'unexpected new cross comparabilities'
 return rel

def chromatic(adj):
 n=len(adj);ind=[True]*(1<<n)
 for mask in range(1,1<<n):
  bit=mask&-mask;i=bit.bit_length()-1;ind[mask]=ind[mask^bit] and not(adj[i]&(mask^bit))
 @functools.lru_cache(None)
 def partitions(mask):
  if not mask:return (1,)
  first=mask&-mask;rest=mask^first;sub=rest;out=[0]*(mask.bit_count()+1)
  while True:
   block=first|sub
   if ind[block]:
    for k,c in enumerate(partitions(mask^block)):out[k+1]+=c
   if not sub:break
   sub=(sub-1)&rest
  return tuple(out)
 return s.expand(sum(c*s.prod(x-j for j in range(k)) for k,c in enumerate(partitions((1<<n)-1))))
def bell(f):return s.expand(sum(c*s.bell(k[0],z) for k,c in s.Poly(f,x).terms()))
def direct_matching(rel,anchors):
 remain=[v for v in range(len(rel)) if v not in anchors];R=len(remain)
 adj=[[j for j,w in enumerate(remain) if v!=w and not rel[w][v]] for v in remain]
 adj += [list(range(R)) for _ in range(len(anchors)-1)]
 counts={0:1}
 for nb in adj:
  nxt=dict(counts)
  for mask,c in counts.items():
   for j in nb:
    if not mask>>j&1:nxt[mask|1<<j]=nxt.get(mask|1<<j,0)+c
  counts=nxt
 return s.expand(sum(c*z**(R-mask.bit_count()) for mask,c in counts.items()))
def verify(name,chains,cross,anchors):
 rel=poset(chains,cross);n=len(rel);k=len(anchors)
 adj=[sum(1<<j for j in range(n) if i!=j and not rel[i][j] and not rel[j][i]) for i in range(n)]
 for chain,a in zip(chains,anchors):
  assert a in chain
  assert all(adj[a]>>v&1 for v in range(n) if v not in chain)
 chi=chromatic(adj);P=s.expand((-1)**n*chi.subs(x,-x));quot=s.cancel(P/s.prod(x+j for j in range(k)))
 F=bell(quot);match=direct_matching(rel,anchors);assert F==match
 assert sum(m for bracket,m in s.polys.polytools.intervals(F,eps=s.Rational(1,100)))==s.degree(F,z)
 # Every smaller-clique quotient is checked independently too.
 for j in range(k+1):
  G=bell(s.cancel(P/s.prod(x+h for h in range(j))))
  assert sum(m for bracket,m in s.polys.polytools.intervals(G,eps=s.Rational(1,100)))==s.degree(G,z)
 return {'name':name,'vertices':n,'k':k,'anchors':anchors,'edges':sum(m.bit_count() for m in adj)//2,'chromatic_polynomial':str(s.factor(chi)),'max_clique_quotient_Bell':str(F),'direct_matching_right_vertices':n-k,'direct_matching_left_vertices':n-1,'all_smaller_quotients_checked':k+1}
results=[]
results.append(verify('edgeless4, k1',[[0,1,2,3]],[],[1]))
# Ferrers d=(1,2,3,4), two chains of four.
chains=[list(range(4)),list(range(4,8))];cross=[(i,4+j) for i,d in enumerate([1,2,3,4]) for j in range(4) if j+1>d]
results.append(verify('connected Ferrers d=(1,2,3,4)',chains,cross,[3,4]))
# K44 minus disjoint edges a1b1,a2b2; order each chain as in proof.
results.append(verify('K44 minus two disjoint edges',[[0,2,3,1],[5,6,7,4]],[(0,4),(5,1)],[2,6]))
# Three length-three chains, with cyclic minimum-to-other-maximum relations.
results.append(verify('K333 minus cyclic three cross edges, k3',[[0,1,2],[3,4,5],[6,7,8]],[(0,5),(3,8),(6,2)],[1,4,7]))
print(json.dumps({'status':'passed','method':'stable-set-partition chromatic enumeration vs independent bitmask matching enumeration','actual_graph_cases':len(results),'results':results,'scope':'finite checks supplement all-k proof'},indent=2))
