import sympy as s,json
x=s.symbols('x')
f=x**6-11*x**5+55*x**4-154*x**3+250*x**2-220*x+81
real,rects=s.polys.polytools.intervals(f,all=True,eps=s.Rational(1,100))
cert=[]
for (lo,hi),mult in rects:
 rlo,ilo=s.re(lo),s.im(lo);rhi,ihi=s.re(hi),s.im(hi)
 if ilo>0:
  bound=s.factor(1+4*rhi-4*ilo**2)
  if bound<0:cert.append({'re_lower':str(rlo),'re_upper':str(rhi),'im_lower':str(ilo),'im_upper':str(ihi),'multiplicity':mult,'parabola_expression_upper_bound':str(bound)})
assert cert
print(json.dumps({'graph':'independent P4 blowup sizes(2,2,2,2)','chromatic_polynomial':'x*(x-1)*('+str(f)+')','method':'exact rational complex-root isolation, multiplicities certified by SymPy intervals(all=True)','outside_closed_parabola_certificates':cert,'scope':'excludes BRW displayed parabolic sufficient condition, not all prior literature'},indent=2))
