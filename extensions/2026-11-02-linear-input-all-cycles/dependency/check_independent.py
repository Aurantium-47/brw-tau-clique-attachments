import sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Run without optimization: certificate assertions must remain active')
import sympy as s
w,V=s.symbols('w V',positive=True)
l=s.symbols('l')
wp=w/(1+w)
Phi=(2+w)/(1-V/4)-2-wp
assert s.factor(Phi.subs(V,2-w)-(2-wp))==0
assert s.factor(s.diff(Phi,V)-(2+w)/(4*(1-V/4)**2))==0
q=(1+w)*l*l-w*l-V/4
assert s.expand(q.subs(l,1)-(1-V/4))==0
assert s.expand(q.subs(l,-1)-(1+2*w-V/4))==0
# Sum phi(lambda_+) + phi(lambda_-) using sum/product of eigenvalues.
ss=w/(1+w);pp=-V/(4*(1+w))
sumphi=(2-ss)/(1-ss+pp)-2-ss
assert s.factor(sumphi-Phi)==0
# n=1 direct generalized eigenvalue determinant.
R,a=s.symbols('R a',positive=True)
b=s.symbols('b',positive=True)
A=s.Matrix([[R,-b],[-b,2]])
E=s.Matrix([[0,a/(2*b)],[a/(2*b),0]])
actual=s.expand((E-l*A).det()).subs(b*b,R-a)
expected=R*((1+a/R)*l*l-(a/R)*l-(a/R)**2/(4*(1-a/R)))
assert s.factor(actual-expected)==0
# n=1 base f=z+c gives kappa=w=1/(c+2).
c=s.symbols('c',positive=True)
k=1/(c+2)
assert s.factor(s.Rational(1,2)-k-c/(2*(c+2)))==0
print('Exact enlarged invariant, spectral potential, and n=1 checks: PASS')
