"""Integrity checks and replay of supporting exact algebra, not a proof assistant."""
import sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Run without optimization: certificate assertions must remain active')
from pathlib import Path
import hashlib,json,shutil,subprocess,tempfile
ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'MANIFEST.json').read_text())
for name,expected in manifest['files_sha256'].items():
    if Path(name).name!=name or not (ROOT/name).is_file():
        raise RuntimeError('Missing or invalid manifest entry: '+name)
    if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=expected:
        raise RuntimeError('SHA256 mismatch: '+name)
note_hash=hashlib.sha256((ROOT/'RESEARCH_NOTE.md').read_bytes()).hexdigest()
if note_hash not in (ROOT/'MATHEMATICAL_REVIEW.md').read_text():
    raise RuntimeError('Mathematical review is not bound to this note')
checks=['check_invariant_algebra.py','check_independent.py']
with tempfile.TemporaryDirectory(prefix='uniform_operator_verify_') as tmp:
    work=Path(tmp)
    for name in checks:
        shutil.copyfile(ROOT/name,work/name)
        proc=subprocess.run([sys.executable,'-I',str(work/name)],cwd=work,capture_output=True,text=True)
        if proc.returncode:
            raise RuntimeError(name+' failed:\n'+proc.stdout+proc.stderr)
        guarded=subprocess.run([sys.executable,'-I','-O',str(work/name)],cwd=work,capture_output=True,text=True)
        if guarded.returncode==0 or 'certificate assertions must remain active' not in guarded.stderr:
            raise RuntimeError('Optimization guard failed: '+name)
        print(name+': PASS')
print('All packaged hashes and supporting exact algebra replays: PASS')
print('The universal argument is the written proof, not these finite symbolic checks.')
