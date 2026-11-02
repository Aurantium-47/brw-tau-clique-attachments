import sympy as s,json
from pathlib import Path
from check_p4 import chromatic_edge_subsets,bell,x
q=s.symbols('q');f=s.Poly(q**6-11*q**5+55*q**4-154*q**3+250*q**2-220*q+81,q)
assert s.expand(chromatic_edge_subsets((2,2,2,2))-bell(f.as_expr().subs(q,-x)))==0
lo=s.Rational(219,100)+s.I*s.Rational(199,100);hi=s.Rational(220,100)+s.I*s.Rational(200,100)
count=f.count_roots(lo,hi);bound=1+4*s.Rational(220,100)-4*s.Rational(199,100)**2
assert count==1 and bound<0
r={'polynomial':str(f.as_expr()),'lower':str(lo),'upper':str(hi),'root_count':int(count),'parabola_upper_bound':str(bound),'actual_graph_factor_verified':True}
Path(__file__).with_name('p4_seed_region.json').write_text(json.dumps(r,indent=2));print(r)
