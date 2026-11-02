import sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Run without optimization: certificate assertions must remain active')
import sympy as s
w,V,q=s.symbols('w V q')
Phi=(2+w)/(1-V/4)-2-w/(1+w)
assert s.factor(Phi.subs(V,2-w)-(2-w/(1+w)))==0
poly=(1+w)*q*q-w*q-V/4
assert s.expand(poly.subs(q,1)-(1-V/4))==0
assert s.expand(poly.subs(q,-1)-(1+2*w-V/4))==0
S=w/(1+w);P=-V/(4*(1+w))
phi_sum=(2-S)/(1-S+P)-2-S
assert s.factor(phi_sum-Phi)==0
assert s.factor(s.diff(Phi,V)-(2+w)/(4*(1-V/4)**2))==0
# For 0<k<=1/2, phi(k)<=k is equivalent to k(1-2k)>=0.
k=s.symbols('k')
assert s.factor((k-k*k/(1-k))*(1-k)-k*(1-2*k))==0
print('Invariant algebra and base scalar bound: PASS')
