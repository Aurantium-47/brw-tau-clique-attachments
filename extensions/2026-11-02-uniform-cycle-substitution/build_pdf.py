"""Optional readable PDF build. Requires pandoc and xelatex on PATH."""
from pathlib import Path
import os,subprocess,tempfile
ROOT=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='uniform_operator_pdf_') as tmp:
    env=os.environ.copy()
    env['XDG_CACHE_HOME']=tmp
    env['TEXMFVAR']=tmp
    subprocess.run(['pandoc',str(ROOT/'RESEARCH_NOTE.md'),
        '--from=markdown+tex_math_single_backslash','--pdf-engine=xelatex',
        '-V','geometry:margin=24mm','-V','fontsize=11pt',
        '-V','colorlinks=true','-V','linkcolor=blue','-V','urlcolor=blue',
        '-o',str(ROOT/'RESEARCH_NOTE.pdf')],cwd=tmp,env=env,check=True)
print('Built RESEARCH_NOTE.pdf. Rebuilding may change PDF metadata and its manifest hash.')
