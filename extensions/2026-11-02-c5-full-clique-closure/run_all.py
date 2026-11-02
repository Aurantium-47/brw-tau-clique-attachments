from pathlib import Path
import hashlib,json,subprocess,sys,tempfile
root=Path(__file__).resolve().parent
m=json.loads((root/'MANIFEST.json').read_text())
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
expected=set(m['files'])|{'MANIFEST.json'}
if actual!=expected:raise RuntimeError('File inventory mismatch: '+repr(actual^expected))
for name,sha in m['files'].items():
 if hashlib.sha256((root/name).read_bytes()).hexdigest()!=sha:raise RuntimeError('Hash mismatch: '+name)
with tempfile.TemporaryDirectory() as td:
 for script in ['check_identities.py','check_graph_bridge.py']:
  subprocess.run([sys.executable,'-I','-O',str(root/script)],cwd=td,check=True)
with tempfile.TemporaryDirectory() as td:
 for script in ['check_small_exact.py','check_translation.py']:
  subprocess.run([sys.executable,'-I','-O',str(root/script)],cwd=td,check=True)
print('PASS: exact inventory, hashes and isolated optimized checker')
