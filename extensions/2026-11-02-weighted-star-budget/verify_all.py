"""Replay release certificates, check optimization policy, and verify manifest."""
import hashlib,json,subprocess,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent

def require(condition,message):
    if not condition: raise RuntimeError(message)

def run(script,certificate,optimized=False):
    args=[sys.executable]+(['-O'] if optimized else [])+[str(BASE/script)]
    result=subprocess.run(args,capture_output=True,text=True,check=True)
    actual=json.loads(result.stdout)
    expected=json.loads((BASE/certificate).read_text())
    require(actual==expected,'Certificate mismatch: '+script)
    print('PASS:',script,('(optimized)' if optimized else ''))

def main():
    import sympy,mpmath
    require(sympy.__version__=='1.14.0','Expected SymPy 1.14.0')
    require(mpmath.__version__=='1.3.0','Expected mpmath 1.3.0')
    run('checkers/verify.py','checkers/certificate.json')
    run('region/check_region.py','region/certificate.json')
    run('region/check_region.py','region/certificate.json',True)
    run('fresh_review/check_fresh.py','fresh_review/certificate.json')
    run('fresh_review/check_fresh.py','fresh_review/certificate.json',True)
    r=subprocess.run([sys.executable,'-O',str(BASE/'checkers/verify.py')],capture_output=True,text=True)
    require(r.returncode!=0 and 'Run without -O' in r.stderr,'Release checker must reject -O')
    print('PASS: release checker rejects disabled assertions')
    manifest=BASE/'MANIFEST.sha256'
    if manifest.exists():
        for line in manifest.read_text().splitlines():
            digest,rel=line.split('  ',1)
            require(hashlib.sha256((BASE/rel).read_bytes()).hexdigest()==digest,'Hash mismatch: '+rel)
        print('PASS: all manifest hashes')
    print('PASS: 19 weighted-board checks; 6222 labeled graph checks / 46 distinct maximal quotients; exact outside-region witness')
if __name__=='__main__': main()
