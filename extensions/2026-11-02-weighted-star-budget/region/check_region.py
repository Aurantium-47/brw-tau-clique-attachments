"""Exact outside-region witness; checks stay enabled under Python -O."""
import json
import sympy as s
x,u=s.symbols('x u'); y=s.symbols('y',real=True)
def require(value):
    if not value: raise RuntimeError('Exact certificate check failed')
def main():
    N,nu,e=12,3,9
    require(N==e+nu)
    m=s.Poly((1+3*u)**3,u)
    f=s.Poly(sum(m.nth(k)*s.prod(x-i for i in range(N-nu,N-k)) for k in range(nu+1)),x)
    require(f.as_expr()==x**3-21*x**2+155*x-396)
    require(s.gcd(f,f.diff()).degree()==0)
    a,b,c,d=map(s.Rational,['7.18','7.19','2.84','2.85'])
    for val in [a,b]:
        re,im=s.expand_complex(f.as_expr().subs(x,val+s.I*y)).as_real_imag()
        require(s.gcd(s.Poly(re,y),s.Poly(im,y)).degree()==0)
    for val in [c,d]:
        re,im=s.expand_complex(f.as_expr().subs(x,y+s.I*val)).as_real_imag()
        require(s.gcd(s.Poly(re,y),s.Poly(im,y)).degree()==0)
    require(f.count_roots(a+s.I*c,b+s.I*d)==1)
    require(f.count_roots(a-s.I*d,b-s.I*c)==1)
    margin=c*c-b-s.Rational(1,4)
    require(margin==s.Rational(391,625)>0)
    print(json.dumps(dict(H='3 disjoint K1,3',N=N,e=e,nu=nu,t=0,matching_counts=[int(m.nth(k)) for k in range(4)],chromatic_residual=str(f.as_expr()),real_interval=[str(a),str(b)],imag_interval=[str(c),str(d)],upper_count=1,conjugate_count=1,boundary_root_free=True,outside_margin=str(margin),qualification='Direct BRW 5.13 hypothesis fails; complement is a cograph, so no new graphscope or novelty claim'),indent=2))
if __name__=='__main__': main()
