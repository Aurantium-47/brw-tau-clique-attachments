"""Independent exact review of the full missing-edge matching EGF.
No coefficient-change lemma or finite-r,s extrapolation is used.
"""
import sympy as s,json
from pathlib import Path
u,v,z,xi,eta,t=s.symbols('u v z xi eta t')
W=1+xi+eta;H=(1+xi)*(1+eta)
means_left=[t*(1+eta),t*W,t*W];means_right=[t*W,t*(1+xi)]
weights=[[eta,xi*eta/W],[W,xi],[W,1+xi]]
# Enumerate effective core matchings directly.
def rec(i,used,weight,left_unmatched,right_used):
 if i==3:
  term=weight*s.prod(left_unmatched)*s.prod(means_right[j] for j in range(2) if not (right_used>>j)&1)
  return term
 total=rec(i+1,used,weight,left_unmatched+[means_left[i]],right_used)
 for j in range(2):
  if not used>>j&1:total+=rec(i+1,used|1<<j,weight*weights[i][j],left_unmatched,right_used|1<<j)
 return total
core=s.factor(rec(0,0,s.Integer(1),[],0))
P=z*z*H*W**3+z*W**2*(6*H-2*W-1)+W*(6*H-4*W-1)
assert s.factor(core-t*P.subs(z,t*t))==0
# Derive Bell polynomial part from unsigned coloring EGF after two derivatives.
# A=1+U+V where U=e^-X-1, V=e^-Y-1, J=e^-(X+Y).
A,U,V,J,x=s.symbols('A U V J x')
pre=J*A**(-x-4)*((x+1)*A*(x+2-A)+(x+2)*(x+3)*U*V)
# Independent algebraic verification of that derivative: use a=e^-X,b=e^-Y.
a,b=s.symbols('a b');AA=a+b-1
raw=x*x*AA**(-x-1)+x*(x+1)*(a-1)*(b-1)*AA**(-x-2)
derived=s.diff(s.diff(raw,a),b)*a*b/(x*(x+1))
# Strip the common invertible formal factor AA**(-x-4).
residual=derived-pre.subs({J:a*b,A:AA,U:a-1,V:b-1})
residual=residual.xreplace({AA**(-x-k):AA**(4-k) for k in range(1,6)})
assert s.factor(residual)==0
# Bell of a polynomial times A^-x has x -> z/A and x² -> z²/A²+z/A.
f=s.Poly(s.expand((x+1)*A*(x+2-A)+(x+2)*(x+3)*U*V),x)
bell_factor=J*A**-4*(f.nth(0)+f.nth(1)*z/A+f.nth(2)*(z*z/A**2+z/A))
D=1-u*v;C=(1+u)*(1+v)
chrom=s.factor(bell_factor.subs({J:1/C,A:D/C,U:-u/(1+u),V:-v/(1+v)}))
xx=u*(1+v)/D;ee=v*(1+u)/D
match=s.factor(P.subs({xi:xx,eta:ee})/D)
assert s.factor(chrom-match)==0
result={'status':'PASS exact rational identities','core_matching_vs_P':'zero residual','unsigned_coloring_derivative':'zero residual','chromatic_Bell_EGF_vs_matching_EGF':'zero residual','note':'Stirling composition, not a finite parameter sweep, gives all a,b.'}
Path(__file__).with_name('full_symbolic_review.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
