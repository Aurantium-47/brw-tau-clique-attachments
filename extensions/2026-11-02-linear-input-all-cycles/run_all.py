#!/usr/bin/env python3
"""Hash-guarded isolated replay; written proofs carry the infinite claims."""
import hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def need(v,m):
 if not v:raise RuntimeError(m)
def verify():
 manifest=json.loads((ROOT/'MANIFEST.json').read_text())
 found={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
 need(found==set(manifest['sha256'])|{'MANIFEST.json'},'Unexpected or missing release file')
 for rel,digest in manifest['sha256'].items():
  need(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()==digest,'Checksum mismatch: '+rel)
 return manifest
verify()
new=['check_linear_seed.py','check_short_ranges.py','check_independent.py','check_graph_scope.py','check_graph_independent.py','check_m4_identities.py','check_m4_formal.py']
old=['dependency/check_invariant_algebra.py','dependency/check_independent.py']
logs=[]
with tempfile.TemporaryDirectory(prefix='brw_linear_all_cycles_') as tmp:
 dst=Path(tmp)/'release';shutil.copytree(ROOT,dst)
 for name in new:
  result=subprocess.run([sys.executable,'-I','-B','-O',str(dst/name)],cwd=tmp,text=True,capture_output=True,timeout=240)
  need(result.returncode==0,name+' failed: '+result.stdout+result.stderr)
  logs.append({'checker':name,'result':result.stdout.strip()})
 for name in old:
  rejected=subprocess.run([sys.executable,'-I','-B','-O',str(dst/name)],cwd=tmp,text=True,capture_output=True,timeout=60)
  need(rejected.returncode!=0 and 'Run without optimization' in rejected.stderr,'Historical optimization guard did not reject: '+name)
  result=subprocess.run([sys.executable,'-I','-B',str(dst/name)],cwd=tmp,text=True,capture_output=True,timeout=60)
  need(result.returncode==0,name+' failed: '+result.stdout+result.stderr)
  logs.append({'checker':name,'result':result.stdout.strip(),'optimization_guard':'PASS'})
verify()
print(json.dumps({'status':'PASS','checks':logs,'scope':'Exact supporting certificates and identities, not finite sampling proof of infinite claims.'},indent=2))
