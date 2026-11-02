import sympy as s
z,x,r=s.symbols('z x r')
L=lambda p:s.expand(z*(p+s.diff(p,z))+p)
S=lambda p:s.expand(p+s.diff(p,z))
for n in range(7):
 h=z**n; f=0;rem=h
 for k in range(n,-1,-1):
  c=s.expand(rem).coeff(z,k);f+=c*x**k;rem=s.expand(rem-c*s.bell(k,z))
 p=S(S(h));q=s.diff(S(h),z)
 out=L(L(L(p)))+L(L(q))+L(q)+r*(L(L(p))+L(p)+p)
 Q=s.expand((x+r+1)*(1+(x+1)+(x+1)**2)*f.subs(x,x+2)-(x+1)*(2+x)*f.subs(x,x+1))
 B=s.Add(*[c*s.bell(k[0],z) for k,c in s.Poly(Q,x).terms()])
 if s.expand(B-out)!=0: raise AssertionError(n)
print('7 symbolic-r monomial Bell translations PASS')
