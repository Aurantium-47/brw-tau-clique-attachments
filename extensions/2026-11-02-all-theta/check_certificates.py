"""Independent integer-only replay: direct binomial/Stirling coefficients and rational signs."""
if not __debug__: raise SystemExit('Assertions required')
import argparse,json,hashlib,math
from pathlib import Path
from fractions import Fraction

def polynomial(t):
    N=sum(t)-1; d=N-2
    q=[math.comb(N,k+2)-sum(math.comb(v,k+2) if k+2<=v else 0 for v in t) for k in range(d+1)]
    assert all(v>0 for v in q)
    S=[1];result=[0]*(d+1)
    for k in range(d+1):
        for j,v in enumerate(S):result[j]+=q[k]*v
        new=[0]*(len(S)+1)
        for j in range(1,len(new)):new[j]=(S[j-1] if j-1<len(S) else 0)+(j*S[j] if j<len(S) else 0)
        S=new
    assert result[-1]==1 and all(v>0 for v in result)
    return result

def rat(v):
    assert len(v)==2
    a,b=map(int,v);assert b>0
    return Fraction(a,b)

def sign_at(p,t):
    n,d=t.numerator,t.denominator
    acc=p[-1];power=1
    for c in reversed(p[:-1]):
        power*=d;acc=acc*n+c*power
    return (acc>0)-(acc<0)

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def check(path):
    r=json.loads(path.read_text());t=r['triple'];assert len(t)==3 and 2<=t[0]<=t[1]<=t[2]<=68
    assert r['status']=='PASS';p=polynomial(t)
    assert hashlib.sha256(json.dumps(list(map(str,p)),separators=(',',':')).encode()).hexdigest()==r['polynomial_sha256']
    product=[1];nroots=0
    for f in r['factors']:
        q=list(map(int,f['coefficients']));m=f['multiplicity'];assert isinstance(m,int) and m>=1 and len(q)>1 and q[-1]==1
        assert len(f['roots'])==len(q)-1
        prev=None
        for box in f['roots']:
            if 'point' in box:
                lo=hi=rat(box['point']);assert sign_at(q,lo)==0
            else:
                lo,hi=rat(box['lo']),rat(box['hi']);assert lo<hi and sign_at(q,lo)*sign_at(q,hi)==-1
            assert hi<0 and (prev is None or prev<lo);prev=hi
        for _ in range(m):product=multiply(product,q)
        nroots+=(len(q)-1)*m
    assert product==p and nroots==len(p)-1==r['degree']
    return tuple(t),nroots

p=argparse.ArgumentParser();p.add_argument('directory',type=Path);p.add_argument('--complete',action='store_true');a=p.parse_args()
seen=set();roots=0
for f in sorted(a.directory.glob('*.json')):
    t,n=check(f);assert t not in seen;seen.add(t);roots+=n
out={'status':'PASS supplied certificates only','triples':len(seen),'root_occurrences':roots,'method':'direct binomial/Stirling coefficients, integer Horner rational signs, exact integer factor multiplication'}
if a.complete:
    expected=set();covered=0;total=0
    for c in range(2,69):
        for b in range(2,c+1):
            for aa in range(2,b+1):
                t=(aa,b,c);N=sum(t)-1;total+=1
                margin=21**N-sum(21**v*20**(N-v) for v in t)-21*20**(N-1)-20**N
                if margin>0:covered+=1
                else:expected.add(t)
    assert seen==expected,(len(seen),len(expected),len(expected-seen),len(seen-expected))
    assert total==52394 and covered==49934 and len(expected)==2460
    out.update(status='PASS full finite domain',total=total,analytic_radius_cases=covered,exact_sign_cases=len(expected))
print(json.dumps(out,indent=2))
