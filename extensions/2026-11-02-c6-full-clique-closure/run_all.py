from pathlib import Path
import hashlib,json,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parent
CHECKERS=['author/check_exact.py','author/check_graph.py','audit_kernel/check_independent.py','audit_bridge/check.py','audit_bridge/check_graphs.py']
def verify():
 data=json.loads((ROOT/'MANIFEST.json').read_text())
 expected=data['sha256']
 if any(p.is_symlink() for p in ROOT.rglob('*')):raise RuntimeError('symlink not permitted in release')
 actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
 if actual!=set(expected)|{'MANIFEST.json'}:raise RuntimeError('release file allowlist mismatch')
 for name,digest in expected.items():
  p=ROOT/name
  if p.resolve().parent!=ROOT and ROOT not in p.resolve().parents:raise RuntimeError('unsafe manifest path')
  if hashlib.sha256(p.read_bytes()).hexdigest()!=digest:raise RuntimeError('release digest mismatch: '+name)
verify()
with tempfile.TemporaryDirectory(prefix='brw_c6_exact_') as wd:
 for checker in CHECKERS:
  print('Running '+checker,flush=True)
  subprocess.run([sys.executable,'-I','-O',str(ROOT/checker)],cwd=wd,check=True,timeout=300)
verify()
print('PASS all five exact checkers and release integrity')
