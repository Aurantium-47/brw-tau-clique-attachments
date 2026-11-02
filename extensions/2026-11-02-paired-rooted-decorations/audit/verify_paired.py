"""Independent standard-library-only exact audit; no author code imported."""
if not __debug__:
    raise SystemExit("Run without -O: exact verification requires assertions.")

import functools,itertools,json,math
from pathlib import Path

def graph(L, types):
    # A rooted graph is (order, edges), with root 0.
    vertices={(i,k) for i in range(1,L+1) for k in range(types[i][0])}
    edges={frozenset(((i,a),(i,b))) for i in range(1,L+1) for a,b in types[i][1]}
    edges|={frozenset(((i,0),(i+1,0))) for i in range(1,L)}
    return vertices,edges

def match(V,E):
    V=list(V); pos={v:i for i,v in enumerate(V)}; adj=[0]*len(V)
    for a,b in map(tuple,E):
        if a in pos and b in pos:
            adj[pos[a]]|=1<<pos[b];adj[pos[b]]|=1<<pos[a]
    @functools.lru_cache(None)
    def rec(S):
        if not S:return (1,)
        bit=S&-S;v=bit.bit_length()-1;rest=S^bit
        out=list(rec(rest)); neigh=adj[v]&rest
        while neigh:
            b=neigh&-neigh;neigh^=b;p=rec(rest^b)
            while len(out)<len(p)+1:out.append(0)
            for k,c in enumerate(p):out[k+1]+=c
        return tuple(out)
    return rec((1<<len(V))-1)

def alpha(V,E):
    V=list(V);pos={v:i for i,v in enumerate(V)};adj=[0]*len(V)
    for a,b in map(tuple,E):adj[pos[a]]|=1<<pos[b];adj[pos[b]]|=1<<pos[a]
    @functools.lru_cache(None)
    def rec(S):
        if not S:return 0
        bit=S&-S;i=bit.bit_length()-1
        return max(rec(S^bit),1+rec((S^bit)&~adj[i]))
    return rec((1<<len(V))-1)

def parts(V,E):
    adj={v:set() for v in V}
    for a,b in map(tuple,E):adj[a].add(b);adj[b].add(a)
    col={}
    for root in V:
        if root in col:continue
        col[root]=0;todo=[root]
        while todo:
            v=todo.pop()
            for w in adj[v]:
                if w not in col:col[w]=1-col[v];todo.append(w)
                assert col[w]!=col[v]
    return [set(v for v in V if col[v]==c) for c in (0,1)]

def bellquot(n,j,m):
    # Direct expansion into ordinary x powers, followed by Stirling transform.
    p=[0]*(n-j+1)
    for k,c in enumerate(m):
        term=[1]
        for r in range(j,n-k):
            q=[0]*(len(term)+1)
            for d,a in enumerate(term):q[d]+=r*a;q[d+1]+=a
            term=q
        for d,a in enumerate(term):p[d]+=(-1)**k*c*a
    S=[[1]]
    for d in range(1,len(p)):
        S.append([0]+[(S[d-1][l-1] if l-1<len(S[d-1]) else 0)+l*(S[d-1][l] if l<len(S[d-1]) else 0) for l in range(1,d+1)])
    return [sum(p[d]*S[d][l] for d in range(l,len(p))) for l in range(len(p))]

def board(n,j,V,E):
    A,B=parts(V,E)
    if len(A)>len(B):A,B=B,A
    a,b=n-j,n-1
    assert len(A)<=a and len(B)<=b
    A=list(A)+[('padA',k) for k in range(a-len(A))]
    B=list(B)+[('padB',k) for k in range(b-len(B))]
    dp={0:1}
    for v in A:
        nd=dp.copy()
        for mask,c in dp.items():
            for k,w in enumerate(B):
                if not(mask>>k&1) and frozenset((v,w)) not in E:
                    nm=mask|(1<<k);nd[nm]=nd.get(nm,0)+c
        dp=nd
    out=[0]*(a+1)
    for mask,c in dp.items():out[a-mask.bit_count()]+=c
    return out

K1=(1,[]); EDGE=(2,[(0,1)]); P3=(3,[(0,1),(1,2)]); STAR3=(4,[(0,1),(0,2),(0,3)]); C4=(4,[(0,1),(1,2),(2,3),(3,0)]); DIS=(3,[(1,2)])
rows=[]
for L,A,B in [(5,K1,K1),(7,K1,K1),(5,EDGE,K1),(5,P3,K1),(5,C4,K1),(5,STAR3,K1),(5,EDGE,EDGE),(7,P3,EDGE),(5,DIS,K1)]:
    ts={i:K1 for i in range(1,L+1)}
    ts[2]=ts[L]=A;ts[3]=ts[L-1]=B
    V,E=graph(L,ts);n=len(V);s=(n-1)//2
    HE=E|{frozenset(((1,0),(L,0)))}; FV=V|{('w',0)};FE=E|{frozenset((('w',0),(2,0)))}
    mh,mf=match(V,HE),match(FV,FE);assert mh==mf
    left=V-{(1,0),(L,0)};right=V-{(1,0),(2,0)}
    phi=lambda v:(L+2-v[0],v[1])
    assert {phi(v) for v in left}==right
    assert {frozenset(phi(v) for v in e) for e in E if e<=left}=={e for e in E if e<=right}
    # Triangle-free by direct enumeration.
    assert all(not all(frozenset(pair) in HE for pair in itertools.combinations(t,2)) for t in itertools.combinations(V,3))
    checked=[]
    if A!=DIS:assert sorted(map(len,parts(FV,FE)))==[s,s+2]
    if n<=11 and A!=DIS:
        for j in range(1,s+2):assert bellquot(n,j,mh)==board(n,j,FV,FE);checked.append(j)
    rows.append(dict(L=L,N=n,attachment_A=A,attachment_B=B,matching=list(mh),alpha_H=alpha(V,HE),bounded_j=s+1,independent_board_checks=checked))
out=Path(__file__).with_name('paired_certificate.json');out.write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2));print('PASS: all exact residual-isomorphism, matching, triangle-free, and board checks')
