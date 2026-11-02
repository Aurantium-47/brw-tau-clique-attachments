"""Exact reproduction checks for three parallel-path/vertex-substitution theorems."""
if not __debug__:raise SystemExit('Optimized Python is unsupported: assertions are required')
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
if sys.flags.optimize or os.environ.get('PYTHONOPTIMIZE'):raise SystemExit('Optimization flags/environment are unsupported')
BASE=Path(__file__).resolve().parent

def sha(raw):return hashlib.sha256(raw).hexdigest()
def run(source,temporary):
    target=temporary/source.name;shutil.copyfile(source,target)
    p=subprocess.run([sys.executable,'-E',str(target)],capture_output=True,text=True)
    if p.returncode:raise RuntimeError(source.name+' failed: '+p.stderr)
    return p.stdout

def replay(bernstein=False):
    deltas={d['file']:d for d in json.loads((BASE/'source_deltas.json').read_text())['files']}
    tasks=[('certify_short_branch_core','certify_short_branch_core.json',None),('check_short_core','short_core_check_results.json',None),('check_c5_substitution','c5_substitution_check_results.json',None),('theta222m_exact_base','theta222m_exact_base.json','checker_sha256'),('check_parallel','parallel_check_results.json',None)]
    if bernstein:tasks=[('effective_cubic_certificate','effective_cubic_certificate.json',None),('effective_mixed_certificate','effective_mixed_certificate.json','script_sha256')]
    rows=[]
    with tempfile.TemporaryDirectory(prefix='parallel-path-replay-') as tmp:
        temporary=Path(tmp)
        for stem,data_name,hash_key in tasks:
            source=BASE/(stem+'.py');delta=deltas[source.name]
            if sha(source.read_bytes())!=delta['packaged_sha256']:raise ValueError('source hash mismatch: '+source.name)
            stdout=run(source,temporary)
            actual=json.loads(stdout) if stem=='theta222m_exact_base' else json.loads((temporary/data_name).read_text())
            expected=json.loads((BASE/data_name).read_text())
            if hash_key:
                if expected.pop(hash_key)!=delta['original_sha256']:raise ValueError('original source identity mismatch')
                if actual.pop(hash_key)!=delta['packaged_sha256']:raise ValueError('packaged source identity mismatch')
            if actual!=expected:raise ValueError('exact regenerated mathematical data mismatch: '+data_name)
            rows.append({'checker':source.name,'status':'PASS exact regeneration and data equality','source_sha256':delta['packaged_sha256']})
    return {'status':'PASS Bernstein certificates' if bernstein else 'PASS exact core, graph interfaces, threshold examples, and arrowhead base','checks':rows}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--bernstein',action='store_true',help='regenerate the larger analytic Bernstein certificates instead of the default checks');p.add_argument('--all',action='store_true',help='run both default and Bernstein checks');a=p.parse_args();out={}
    if not a.bernstein or a.all:out['default']=replay()
    if a.bernstein or a.all:out['bernstein']=replay(True)
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
