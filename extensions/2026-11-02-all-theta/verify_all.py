"""Replay exact theta certificates without writing into this package."""
if not __debug__: raise SystemExit('Optimized Python is unsupported: assertions are required')
import argparse,hashlib,json,os,re,shutil,stat,subprocess,sys,tempfile,zipfile
from pathlib import Path
if sys.flags.optimize or os.environ.get('PYTHONOPTIMIZE'):
    raise SystemExit('Optimization flags/environment are unsupported')
BASE=Path(__file__).resolve().parent
# Exact total-length 72 analytic tail threshold, independent of root certificates.
assert 21**68*(21**3-20**3) > (2*21**2+21*20+20**2)*20**69
assert 9*(21**2-20**2) < 20**2

def digest(raw):return hashlib.sha256(raw).hexdigest()

def extract_verified(archive,manifest,destination):
    """No extractall: validate the complete flat allowlist before writing bytes."""
    if manifest['format']!=1 or manifest['count']!=2460:raise ValueError('invalid manifest format/count')
    entries=manifest['entries'];allowed={}
    for item in entries:
        name=item['name']
        if not re.fullmatch(r'[0-9]{2}_[0-9]{2}_[0-9]{2}\.json',name):raise ValueError('unsafe manifest name')
        if name in allowed:raise ValueError('duplicate manifest name')
        if not isinstance(item['size'],int) or item['size']<0:raise ValueError('invalid entry size')
        if not re.fullmatch('[0-9a-f]{64}',item['sha256']):raise ValueError('invalid entry hash')
        allowed[name]=item
    if len(allowed)!=2460:raise ValueError('wrong allowlist count')
    if digest(archive.read_bytes())!=manifest['archive_sha256']:raise ValueError('archive hash mismatch')
    with zipfile.ZipFile(archive) as z:
        infos=z.infolist();names=[i.filename for i in infos]
        if len(names)!=len(set(names)):raise ValueError('duplicate ZIP entry')
        if set(names)!=set(allowed):raise ValueError('unexpected/missing ZIP entries')
        for info in infos:
            mode=info.external_attr>>16
            if info.is_dir() or stat.S_IFMT(mode) not in (0,stat.S_IFREG):raise ValueError('nonregular ZIP entry')
            if info.file_size!=allowed[info.filename]['size']:raise ValueError('entry size mismatch')
        for info in infos:
            raw=z.read(info)
            if digest(raw)!=allowed[info.filename]['sha256']:raise ValueError('entry hash mismatch')
            (destination/info.filename).write_bytes(raw)

def run(script,args=()):
    p=subprocess.run([sys.executable,'-E',str(script),*map(str,args)],capture_output=True,text=True)
    if p.returncode:raise RuntimeError(script.name+' failed: '+p.stderr)
    return p.stdout

def finite():
    with tempfile.TemporaryDirectory(prefix='theta-finite-') as tmp:
        out=Path(tmp);manifest=json.loads((BASE/'certificate_manifest.json').read_text())
        extract_verified(BASE/'finite_certificates.zip',manifest,out)
        one=json.loads(run(BASE/'audit_finite_certificates.py',['--certificates',out]))
        two=json.loads(run(BASE/'check_certificates.py',[out,'--complete']))
        if one['status']!='PASS complete finite cover' or two['status']!='PASS full finite domain':raise ValueError('incomplete replay')
        return {'status':'PASS two complete exact finite replays','first':one,'second':two,'archive_sha256':manifest['archive_sha256']}

def bernstein():
    delta=json.loads((BASE/'source_delta.json').read_text());results=[]
    with tempfile.TemporaryDirectory(prefix='theta-bernstein-') as tmp:
        out=Path(tmp)
        for name in ['effective_cubic_certificate','effective_mixed_certificate']:
            source=BASE/(name+'.py');target=out/source.name;shutil.copyfile(source,target)
            if name=='effective_mixed_certificate' and digest(source.read_bytes())!=delta['packaged_sha256']:raise ValueError('guarded source hash mismatch')
            run(target)
            expected=json.loads((BASE/(name+'.json')).read_text());actual=json.loads(target.with_suffix('.json').read_text())
            if name=='effective_mixed_certificate':
                if expected.pop('script_sha256')!=delta['original_sha256']:raise ValueError('original source identity mismatch')
                if actual.pop('script_sha256')!=delta['packaged_sha256']:raise ValueError('regenerated source identity mismatch')
            if actual!=expected:raise ValueError('Bernstein mathematical data mismatch')
            results.append({'name':name,'status':'PASS exact regeneration and mathematical data equality','coefficient_count':actual['coefficient_count']})
    return {'status':'PASS Bernstein regeneration','certificates':results}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--finite',action='store_true',help='two full standard-library exact replays (default)');p.add_argument('--bernstein',action='store_true',help='regenerate exact cubic/quartic Bernstein certificates; needs SymPy');a=p.parse_args()
    result={}
    if a.finite or not a.bernstein:result['finite']=finite()
    if a.bernstein:result['bernstein']=bernstein()
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
