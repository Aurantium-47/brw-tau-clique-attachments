"""Replay exact checks; finite diagnostics do not replace the manuscript's proofs."""
if not __debug__:
    raise SystemExit("Verification requires assertions enabled; do not use python -O, -OO, or PYTHONOPTIMIZE.")

from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parent
records=json.loads((root/'CHECKER_PROVENANCE.json').read_text())['files']
def seal():
    for record in records:
        assert hashlib.sha256((root/record['file']).read_bytes()).hexdigest()==record['sha256'],record['file']
seal()
results=[]
for record in records:
    filename=record['file']
    print('RUN',filename,flush=True)
    completed=subprocess.run([sys.executable,str(root/filename)],cwd=root/'checkers',capture_output=True,text=True)
    print(completed.stdout,end='',flush=True)
    if completed.returncode:
        print(completed.stderr,file=sys.stderr)
        raise SystemExit(completed.returncode)
    results.append({'checker':filename,'status':'PASS','stdout':completed.stdout})
seal()
receipt={'status':'PASS','python':sys.version.split()[0], 'sympy':__import__('sympy').__version__,'checker_count':len(records),'checks':results,'limitations':'Symbolic identities and finite diagnostics support the ordinary proof; no machine-checked universal theorem or human peer review is claimed.'}
(root/'VERIFICATION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('PASS all exact checks and unchanged-checker seals')
