"""Exact algebraic support only; uniform eventuality is an ordinary analytic proof."""
if not __debug__:
    raise SystemExit('Verification requires assertions enabled; do not use -O, -OO, or PYTHONOPTIMIZE.')
from pathlib import Path
import sys,json,hashlib,subprocess
root=Path(__file__).resolve().parent
records=json.loads((root/'CHECKER_PROVENANCE.json').read_text())['files']
def seal():
    for item in records:
        if hashlib.sha256((root/item['file']).read_bytes()).hexdigest()!=item['sha256']:
            raise SystemExit('Digest mismatch: '+item['file'])
seal()
script='checkers/check_general_theta_identities.py'
r=subprocess.run([sys.executable,'-E',str(root/script)],cwd=root/'checkers',capture_output=True,text=True)
print(r.stdout,end='')
if r.returncode:
    print(r.stderr,file=sys.stderr);raise SystemExit(r.returncode)
seal()
receipt={'status':'PASS','python':sys.version.split()[0],'sympy':__import__('sympy').__version__,'checker':script,'stdout':r.stdout,'limitation':'Exact algebraic identities and sign certificates only; no effective threshold or computational verification of analytic eventuality is claimed.'}
(root/'VERIFICATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('PASS exact algebraic support and unchanged source digests')
