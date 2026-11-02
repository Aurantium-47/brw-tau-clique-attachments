"""Independent exhaustive labeled-graph checks; runtime checks survive python -O."""
import itertools,json
from functools import lru_cache
import sympy as s
from sympy.functions.combinatorial.numbers import stirling

def require(condition, explanation):
    if not condition: raise RuntimeError(explanation)

def match_vector(n,edges):
    adj=[0]*n
    for u,v in edges: adj[u]|=1<<v; adj[v]|=1<<u
    @lru_cache(None)
    def rec(mask):
        if not mask:return (1,)
        u=(mask&-mask).bit_length()-1
        rest=mask^(1<<u)
        result=list(rec(rest))
        nbrs=adj[u]&rest
        while nbrs:
            bit=nbrs&-nbrs;nbrs^=bit
            term=rec(rest^bit)
            while len(result)<len(term)+1:result.append(0)
            for k,value in enumerate(term):result[k+1]+=value
        while len(result)>1 and not result[-1]:result.pop()
        return tuple(result)
    return rec((1<<n)-1)

def main():
    x,z=s.symbols('x z')
    records={}; counts={}
    for n in range(1,7):
        pairs=list(itertools.combinations(range(n),2))
        triangles=[sum(1<<pairs.index(edge) for edge in itertools.combinations(triple,2)) for triple in itertools.combinations(range(n),3)]
        count=0
        for mask in range(1,1<<len(pairs)):
            if any(mask&tri==tri for tri in triangles):continue
            edges=[edge for k,edge in enumerate(pairs) if mask>>k&1]
            m=match_vector(n,edges);nu=len(m)-1;e=len(edges)
            require(m[1]==e,'incorrect edge coefficient')
            N=max(n,e+nu);j=N-nu
            key=(N,m)
            count+=1
            if key in records:continue
            q=s.Poly(sum((-1)**k*mk*s.prod(x+i for i in range(j,N-k)) for k,mk in enumerate(m)),x)
            Q=s.Poly(sum(coef*sum(stirling(d,l,kind=2)*z**l for l in range(d+1)) for (d,),coef in q.terms()),z)
            require(Q.degree()==nu,'degree mismatch')
            require(all(v>=0 for v in Q.all_coeffs()),'negative coefficient')
            roots=Q.intervals(eps=s.Rational(1,10**8))
            require(sum(mult for _,mult in roots)==nu,'nonreal root')
            require(all(upper<=0 for (lower,upper),mult in roots),'positive root')
            records[key]={'N':N,'matching_vector':list(m),'j':j,'Q':str(Q.as_expr())}
        counts[n]=count
    print(json.dumps({'triangle_free_graphs_with_edges_by_order':counts,'graph_checks':sum(counts.values()),'distinct_exact_quotient_checks':len(records),'checks':list(records.values())},indent=2))
if __name__=='__main__':main()
