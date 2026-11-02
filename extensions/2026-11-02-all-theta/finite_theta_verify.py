"""Generate exact negative-root certificates for the finite theta remainder.
FLINT supplies candidate intervals; PASS depends on exact rational endpoint signs.
"""
if not __debug__: raise SystemExit('Assertions must remain enabled')
import argparse,hashlib,json,os,time
from pathlib import Path
from fractions import Fraction
from flint import fmpz_poly,fmpq,ctx
import flint
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
def triples():
    return [(a,b,c) for c in range(2,69) for b in range(2,c+1) for a in range(2,b+1)]
def margin(t):
    a,b,c=t;n=a+b+c-1
    return 21**n-sum(21**k*20**(n-k) for k in t)-21*20**(n-1)-20**n
def coefficient_digest(coeff):
    return hashlib.sha256(json.dumps([str(c) for c in coeff],separators=(',',':')).encode()).hexdigest()
def W_table(n):
    z=fmpz_poly([0,1]);A=fmpz_poly([1]);U=A;W=[fmpz_poly([])]
    for k in range(1,n+1):
        W.append(W[-1]+U)
        A=z*A.derivative()+(z+1)*A;U+=A
    return W
def poly_for(t,W):
    return W[sum(t)-2]-sum((W[k-1] for k in t),fmpz_poly([]))
def pair(q):return [str(q.numerator),str(q.denominator)]
def rational(v):
    if len(v)!=2:raise ValueError('bad rational encoding')
    n,d=map(int,v)
    if d<=0:raise ValueError('nonpositive denominator')
    return fmpq(n,d)
def check_factor_record(record):
    q=fmpz_poly([int(c) for c in record['coefficients']]);degree=q.degree()
    if degree<1 or q[degree]!=1 or record['multiplicity']<1:raise ValueError('bad factor')
    boxes=record['roots']
    if len(boxes)!=degree:raise ValueError('wrong interval count')
    previous=None
    for box in boxes:
        if 'point' in box:
            lo=hi=rational(box['point'])
            if q(lo)!=0:raise ValueError('point is not an exact zero')
        else:
            lo,hi=rational(box['lo']),rational(box['hi'])
            if not lo<hi or not q(lo)*q(hi)<0:raise ValueError('no exact sign change')
        if hi>=0 or previous is not None and not previous<lo:raise ValueError('nonnegative or overlapping root boxes')
        previous=hi
    return q

def validate(record,p,t,require_source=True):
    if record['triple']!=list(t) or record['status']!='PASS':raise ValueError('identity/status mismatch')
    if require_source and record['generator_sha256']!=SELF_SHA:raise ValueError('source digest mismatch')
    if record['polynomial_sha256']!=coefficient_digest(p.coeffs()):raise ValueError('polynomial digest mismatch')
    if p.degree()!=sum(t)-3 or any(c<=0 for c in p.coeffs()):raise ValueError('theta degree/positivity mismatch')
    product=fmpz_poly([1]);total=0
    for f in record['factors']:
        q=check_factor_record(f);m=f['multiplicity'];product*=q**m;total+=q.degree()*m
    if product!=p or total!=p.degree():raise ValueError('factorization identity mismatch')

def certify(p,t):
    content,factors=p.factor_squarefree()
    if content!=1:raise ValueError('not monic')
    records=[]
    for q,m in factors:
        roots=None
        for precision in [64,128,256,512,1024]:
            with ctx.workprec(precision):
                proposed=q.complex_roots();boxes=[]
                for r,multiplicity in proposed:
                    if multiplicity!=1:raise ValueError('squarefree factor proposal repeated')
                    # Numerical real/nonreal classification is NOT used to certify a pass.
                    lo,hi=r.real.lower().fmpq(),r.real.upper().fmpq()
                    if q(lo)==0:box={'point':pair(lo)}
                    elif q(hi)==0:box={'point':pair(hi)}
                    else:box={'lo':pair(lo),'hi':pair(hi)}
                    boxes.append(box)
                boxes.sort(key=lambda b:Fraction(*map(int,b.get('point',b.get('lo')))))
                candidate={'coefficients':[str(c) for c in q.coeffs()],'multiplicity':int(m),'roots':boxes}
                try:check_factor_record(candidate)
                except ValueError:continue
                roots=candidate;break
        if roots is None:raise ValueError('could not certify degree-many negative roots; no PASS inferred')
        records.append(roots)
    record={'status':'PASS','triple':list(t),'degree':p.degree(),'generator_sha256':SELF_SHA,'polynomial_sha256':coefficient_digest(p.coeffs()),'arithmetic':'integer polynomials and exact rational endpoint signs','python_flint':flint.__version__,'factors':records}
    validate(record,p,t);return record

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True);parser.add_argument('--shard',default='0/1');parser.add_argument('--limit',type=int);args=parser.parse_args()
    i,n=map(int,args.shard.split('/'))
    if not 0<=i<n:raise SystemExit('invalid shard')
    all_t=triples();exceptions=[t for t in all_t if margin(t)<=0]
    if len(all_t)!=52394 or len(exceptions)!=2460:raise SystemExit('coverage count mismatch')
    jobs=[t for j,t in enumerate(exceptions) if j%n==i]
    if args.limit is not None:jobs=jobs[:args.limit]
    W=W_table(max(sum(t)-2 for t in exceptions));args.out.mkdir(parents=True,exist_ok=True)
    start=time.time();done=0
    for t in jobs:
        p=poly_for(t,W);path=args.out/('%02d_%02d_%02d.json'%t)
        if path.exists():
            record=json.loads(path.read_text());validate(record,p,t)
        else:
            record=certify(p,t);tmp=path.with_suffix('.tmp.%d'%os.getpid());tmp.write_text(json.dumps(record,separators=(',',':'))+'\n');os.replace(tmp,path)
        done+=1
        if done%100==0:print(json.dumps({'shard':args.shard,'verified':done,'jobs':len(jobs),'seconds':round(time.time()-start,3)}),flush=True)
    print(json.dumps({'status':'PASS selected jobs only','shard':args.shard,'verified':done,'jobs':len(jobs),'seconds':round(time.time()-start,3),'generator_sha256':SELF_SHA}),flush=True)
if __name__=='__main__':main()
