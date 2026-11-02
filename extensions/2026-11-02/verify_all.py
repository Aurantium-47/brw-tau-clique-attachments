"""Portable exact checks. Analytic eventuality rests on the manuscript, not test counts."""
if not __debug__:
    raise SystemExit('Verification requires assertions enabled; do not use -O, -OO, or PYTHONOPTIMIZE.')
from pathlib import Path
import sys,json,hashlib,subprocess
root=Path(__file__).resolve().parent
records=json.loads((root/'CHECKER_PROVENANCE.json').read_text())['checkers']
def seals():
    for item in records:
        if hashlib.sha256((root/item['file']).read_bytes()).hexdigest()!=item['sha256']:
            raise SystemExit('Checker digest mismatch: '+item['file'])
seals();results=[]
for item in records:
    print('RUN',item['file'],flush=True)
    r=subprocess.run([sys.executable,'-E',str(root/item['file'])],cwd=root/'checkers',capture_output=True,text=True)
    public_stdout=r.stdout.replace(str(root)+'/', '')
    print(public_stdout,end='',flush=True)
    if r.returncode:
        print(r.stderr,file=sys.stderr);raise SystemExit(r.returncode)
    results.append({'checker':item['file'],'status':'PASS','stdout':public_stdout})
seals()
receipt={'status':'PASS','python':sys.version.split()[0],'sympy':__import__('sympy').__version__,'checker_count':len(results),'checks':results,'limitation':'These exact identities and finite graph checks support ordinary proofs; they neither verify analytic eventuality algorithmically nor supply an effective theta threshold.'}
(root/'VERIFICATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('PASS all exact checks and unchanged-checker digests')
