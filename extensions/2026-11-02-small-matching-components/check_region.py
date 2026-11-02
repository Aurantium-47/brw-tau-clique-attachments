"""Exact BRW 5.13 region inclusion for the two-double-star example."""
if not __debug__:raise RuntimeError('Assertions required')
import sympy as s
import json
from pathlib import Path
x=s.symbols('x');f=s.Poly(x**4-28*x**3+302*x**2-1483*x+2792,x)
assert s.gcd(f,f.diff()).degree()==0
records=[]
for a,b,c,d in [(691,693,90,92),(707,709,267,269)]:
 a,b,c,d=[s.Rational(v,100) for v in (a,b,c,d)]
 assert f.count_roots(a+s.I*c,b+s.I*d)==1
 assert f.count_roots(a-s.I*d,b-s.I*c)==1
 margin=a+s.Rational(1,4)-d*d
 assert margin>0
 records.append(dict(real_interval=[str(a),str(b)],positive_imag_interval=[str(c),str(d)],upper_root_count=1,conjugate_root_count=1,region_margin=str(margin)))
assert f.degree()==4
Path(__file__).with_name('region_certificate.json').write_text(json.dumps(dict(polynomial=str(f.as_expr()),criterion='Im(q)^2 < Re(q)+1/4',all_nonreal_roots_strictly_inside=True,records=records),indent=2)+'\n')
print('PASS: all four nonreal chromatic zeros lie strictly inside BRW R_T(0)')
# A different, already quotient-verified component example escapes the criterion.
t=s.symbols('t');m=s.Poly((1+5*t+4*t*t)*(1+3*t+t*t)*(1+4*t+2*t*t),t)
P=s.Poly(sum((-1)**k*m.nth(k)*s.rf(x,15-k) for k in range(7)),x)
Q,rem=s.div(P,s.Poly(s.rf(x,9),x));assert rem.is_zero
f=s.Poly(Q.as_expr().subs(x,-x),x)
assert s.gcd(f,f.diff()).degree()==0
assert f.as_expr()==x**6-57*x**5+1369*x**4-17710*x**3+129992*x**2-512731*x+848168
a,b,c,d=map(s.Rational,['10.15','10.16','3.63','3.64'])
# Exclude roots on all four rational boundary lines via exact real/imag gcd.
y=s.symbols('y',real=True)
for value in [a,b]:
 re,im=s.expand_complex(f.as_expr().subs(x,value+s.I*y)).as_real_imag()
 assert s.gcd(s.Poly(re,y),s.Poly(im,y)).degree()==0
for value in [c,d]:
 re,im=s.expand_complex(f.as_expr().subs(x,y+s.I*value)).as_real_imag()
 assert s.gcd(s.Poly(re,y),s.Poly(im,y)).degree()==0
assert f.count_roots(a+s.I*c,b+s.I*d)==1
margin=c*c-b-s.Rational(1,4)
assert margin==s.Rational(27669,10000)>0
Path(__file__).with_name('outside_region_certificate.json').write_text(json.dumps(dict(complement_components=['D(2,2)','D(1,1)','D(1,2)'],n=15,nu=6,clique_number=9,matching_counts=[int(m.nth(k)) for k in range(7)],chromatic_residual=str(f.as_expr()),rectangle=dict(real=[str(a),str(b)],imag=[str(c),str(d)]),exact_complex_root_count=1,squarefree=True,boundary_root_free=True,outside_margin=str(margin),claim='Outside closed BRW R_T(0); no claim about other criteria or novelty'),indent=2)+'\n')
print('PASS: n15 example has certified zero outside closed BRW R_T(0)')
