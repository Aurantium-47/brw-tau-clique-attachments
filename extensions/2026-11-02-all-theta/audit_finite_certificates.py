"""Independent pure-integer checker of theta negative-root certificates and coverage.
No FLINT, floating point, numerical root classification, or generator imports.
"""
if not __debug__: raise SystemExit('Assertions must remain enabled')
import argparse,hashlib,json,math,gzip
from pathlib import Path
from fractions import Fraction

def coeffs(t):
    a,b,c=t;degree=a+b+c-3;qt=[0]*(degree+1)
    for i in range(a+b-1):
        for j in range(c):qt[i+j]+=1
    for i in range(a-1):
        for j in range(b-1):qt[1+i+j]+=1
    # First shift t=x+1; then ordinary power-to-Bell Stirling transform.
    shifted=[sum(qt[k]*math.comb(k,j) for k in range(j,degree+1)) for j in range(degree+1)]
    result=[0]*(degree+1);row=[1]
    for k in range(degree+1):
        for j,v in enumerate(row):result[j]+=shifted[k]*v
        nxt=[0]*(len(row)+1)
        for j,v in enumerate(row):nxt[j]+=j*v;nxt[j+1]+=v
        row=nxt
    return result

def digest(p):return hashlib.sha256(json.dumps([str(c) for c in p],separators=(',',':')).encode()).hexdigest()
def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def rat(v):
    if len(v)!=2:raise ValueError('bad rational')
    n,d=map(int,v)
    if d<=0:raise ValueError('nonpositive denominator')
    return Fraction(n,d)
def eval_numerator(p,r):
    n,d=r.numerator,r.denominator;h=p[-1];dp=d
    for c in p[-2::-1]:h=h*n+c*dp;dp*=d
    return h

def verify_record(record,t,expected_source):
    if record['triple']!=list(t) or record['status']!='PASS' or record['generator_sha256']!=expected_source:raise ValueError('receipt identity mismatch')
    p=coeffs(t)
    if len(p)-1!=sum(t)-3 or p[-1]!=1 or any(c<=0 for c in p):raise ValueError('invalid theta polynomial')
    if record['degree']!=len(p)-1 or record['polynomial_sha256']!=digest(p):raise ValueError('independent polynomial mismatch')
    product=[1];roots_with_multiplicity=0;distinct_boxes=0
    for factor in record['factors']:
        q=list(map(int,factor['coefficients']));m=factor['multiplicity'];degree=len(q)-1
        if degree<1 or q[-1]!=1 or not isinstance(m,int) or m<1:raise ValueError('invalid factor')
        boxes=factor['roots']
        if len(boxes)!=degree:raise ValueError('wrong root count')
        previous=None
        for box in boxes:
            if 'point' in box:
                lo=hi=rat(box['point'])
                if eval_numerator(q,lo)!=0:raise ValueError('false exact root')
            else:
                lo,hi=rat(box['lo']),rat(box['hi'])
                if not lo<hi or eval_numerator(q,lo)*eval_numerator(q,hi)>=0:raise ValueError('no strict rational sign change')
            if hi>=0 or previous is not None and previous>=lo:raise ValueError('nonnegative/overlapping boxes')
            previous=hi
        for _ in range(m):product=multiply(product,q)
        roots_with_multiplicity+=degree*m;distinct_boxes+=degree
    if product!=p or roots_with_multiplicity!=len(p)-1:raise ValueError('factorization/degree mismatch')
    return roots_with_multiplicity,distinct_boxes

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--certificates',type=Path,required=True);ap.add_argument('--allow-partial',action='store_true');ap.add_argument('--coverage-out',type=Path);args=ap.parse_args()
    source=Path(__file__).with_name('finite_theta_verify.py');expected=hashlib.sha256(source.read_bytes()).hexdigest()
    powers21=[21**i for i in range(205)];powers20=[20**i for i in range(205)]
    analytic=finite=missing=0;rows=[];intervals=0;seen=set()
    for c in range(2,69):
        for b in range(2,c+1):
            for a in range(2,b+1):
                t=(a,b,c);N=sum(t)-1
                margin=powers21[N]-sum(powers21[k]*powers20[N-k] for k in t)-21*powers20[N-1]-powers20[N]
                if margin>0:
                    analytic+=1;rows.append({'triple':list(t),'branch':'strict rational radius','positive_margin_numerator':str(margin)});continue
                filename='%02d_%02d_%02d.json'%t;path=args.certificates/filename;seen.add(filename)
                if not path.is_file():
                    missing+=1
                    if not args.allow_partial:raise ValueError('missing exact certificate: '+filename)
                    continue
                raw=path.read_bytes();record=json.loads(raw);degree,boxes=verify_record(record,t,expected);finite+=1;intervals+=boxes
                rows.append({'triple':list(t),'branch':'exact negative root certificates','certificate':filename,'certificate_sha256':hashlib.sha256(raw).hexdigest(),'degree':degree,'distinct_factor_root_boxes':boxes})
    unexpected={p.name for p in args.certificates.glob('*.json')}-seen
    if unexpected:raise ValueError('unexpected certificate files: '+str(sorted(unexpected)))
    if analytic!=49934 or finite+missing!=2460 or analytic+finite+missing!=52394:raise ValueError('nonexhaustive coverage')
    if args.coverage_out:
        if missing:raise ValueError('refusing full coverage receipt for partial run')
        with args.coverage_out.open('wb') as raw:
            with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0) as f:
                for row in rows:f.write((json.dumps(row,separators=(',',':'))+'\n').encode())
    result={'status':'PASS complete finite cover' if not missing else 'PASS partial certificates only','sorted_triples':52394,'analytic_radius':analytic,'exact_certificate_triples':finite,'missing':missing,'distinct_factor_root_boxes_checked':intervals,'generator_sha256':expected,'auditor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'method':'independent geometric sum/binomial/Stirling coefficients, integer homogeneous rational evaluation, exact factor products; no floating arithmetic'}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
