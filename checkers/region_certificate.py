import sympy as s,json
from pathlib import Path
q=s.Symbol('q')
p=s.Poly(q**4-7*q**3+21*q**2-30*q+17,q)
relo,rehi=s.Rational(189,100),s.Rational(190,100)
imlo,imhi=s.Rational(155,100),s.Rational(156,100)
number=p.count_roots(relo+s.I*imlo,rehi+s.I*imhi)
upper=1+4*rehi-4*imlo**2
assert number==1 and upper<0
result={'status':'PASS exact complex rectangle count','chromatic_quotient':str(p.as_expr()),'real_bounds':[str(relo),str(rehi)],'imaginary_bounds':[str(imlo),str(imhi)],'root_count':int(number),'parabola_expression_upper_bound':str(upper),'claim':'K3,3 minus one edge is outside closed BRW R_T(0); not novelty certificate'}
Path(__file__).with_name('region_certificate.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
