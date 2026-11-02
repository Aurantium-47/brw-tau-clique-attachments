import sympy as s,json
u,v,n=s.symbols('u v n')
core=(1+(u+v)/2)*(1+u)**3
empty=(1+s.Rational(2,3)*u+s.Rational(1,3)*v)*core
normal={0:{2:1,1:2},1:{2:5,1:11,0:3},2:{2:10,1:21,0:7},3:{2:10,1:17,0:4},4:{2:5,1:5},5:{2:1}}
fall=lambda n,k:s.prod(n-i for i in range(k))
result=[]
for k in range(0,8):
 m=0
 for f,shift in [(empty,0),(2*core,1)]:
  for (a,b),c in s.Poly(s.expand(f),u,v).terms():
   if a+b+shift==k:m+=c*fall(n,a)*fall(n,b)
 target=sum(c*fall(n,j) for j,d in normal.items() for p,c in d.items() if j+2-p==k)
 difference=s.factor(m-target)
 assert difference==0,(k,difference)
 result.append({'matching_size':k,'coefficient':str(s.factor(m)),'difference':str(difference)})
print(json.dumps({'status':'exact all-n polynomial identity','coefficients':result},indent=2))
