"""Exhaust all simple bipartite 5-edge graphs, ignoring isolated vertices.
Each color side has <=5 vertices because every retained vertex meets an edge.
Hence this is complete even when original graph order is unbounded.
"""
if not __debug__:
    raise SystemExit("Run without -O: exact verification requires assertions.")

import itertools,json
from pathlib import Path

def matching(V,E):
    if not E:return (1,)
    v=next(iter(next(iter(E))))
    out=list(matching(V-{v},{e for e in E if v not in e}))
    for e in E:
        if v in e:
            p=matching(V-e,{f for f in E if not f&e})
            while len(out)<len(p)+1:out.append(0)
            for k,c in enumerate(p):out[k+1]+=c
    return tuple(out)

candidates=0;eligible=0;rooted=0;patterns={}
for a in range(1,6):
    for b in range(a,6):
        V=set(range(a+b));possible=[frozenset((i,a+j)) for i in range(a) for j in range(b)]
        for chosen in itertools.combinations(possible,5):
            E=set(chosen)
            if set().union(*E)!=V:continue
            candidates+=1
            degree=[sum(v in e for e in E) for v in V]
            if sum(d*(d-1)//2 for d in degree)!=5:continue
            if matching(V,E)!=(1,5,5):continue
            eligible+=1;key=str((a,b,tuple(sorted(degree))))
            patterns[key]=patterns.get(key,0)+1
            for r in V:
                if degree[r]==2 and matching(V-{r},{e for e in E if r not in e})==(1,3,1):rooted+=1
assert eligible and not rooted
assert all('(2, 4,' in key for key in patterns)
result=dict(nonisolated_five_edge_candidates=candidates,matching_equivalent_labeled_candidates=eligible,rooted_equivalent_candidates=rooted,patterns=patterns)
Path(__file__).with_name('c5_obstruction_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));print('PASS: exhaustive nonisolated five-edge bipartite graph audit')
