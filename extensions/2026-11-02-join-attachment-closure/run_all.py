"""Guarded replay in a temporary directory; does not modify release artifacts."""
import hashlib,json,subprocess,sys,tempfile,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def require(ok,reason):
 if not ok: raise RuntimeError(reason)
manifest=json.loads((ROOT/'MANIFEST.json').read_text())
for name,digest in manifest['sha256'].items():
 require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'Manifest mismatch: '+name)
with tempfile.TemporaryDirectory(prefix='brw-rooted-join-') as directory:
 target=Path(directory)
 for name in ['verify.py','review_check.py','graph_check.py']:
  shutil.copy2(ROOT/name,target/name)
  result=subprocess.run([sys.executable,'-O',str(target/name)],cwd=target,text=True,capture_output=True)
  require(result.returncode==0,name+' failed:\n'+result.stdout+result.stderr)
  print(result.stdout,end='')
 for name in ['certificate.json','graph_certificate.json']:
  require(json.loads((target/name).read_text())==json.loads((ROOT/name).read_text()),'Certificate mismatch: '+name)
print('PASS manifest, optimized-Python guarded checks, and exact certificate replay')
