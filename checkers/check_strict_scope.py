import sympy as s,json,itertools
q=s.symbols('q');p=s.Poly(q**4-7*q**3+21*q**2-30*q+17,q)
a=s.Rational(189,100)+s.Rational(31,20)*s.I;b=s.Rational(19,10)+s.Rational(39,25)*s.I
count=p.count_roots(a,b);margin=4*s.Rational(31,20)**2-1-4*s.Rational(19,10)
assert count==1 and margin>0
V=set(range(6)); E={frozenset((i,j)) for i in range(3) for j in range(3,6)}-{frozenset((0,3))}
def connected(W, edges):
 if not W:return False
 seen={next(iter(W))}
 while True:
  new=seen|{v for v in W for u in seen if frozenset((u,v)) in edges}
  if new==seen:return seen==W
  seen=new
assert connected(V,E)
comp={frozenset(p) for p in itertools.combinations(V,2)}-E
assert connected(V,comp)
cliques=[()] + [(v,) for v in V] + [tuple(e) for e in E]
assert all(connected(V-set(C),E) for C in cliques)
path=[0,4,1,3]
assert {e for e in E if e<=set(path)}=={frozenset(p) for p in zip(path,path[1:])}
assert len(E)==8
out={'graph':'K_3,3 minus edge 0--3','vertices':sorted(V),'edges':sorted(sorted(e) for e in E),'quartic':str(p.as_expr()),'rectangle':[str(a),str(b)],'exact_complex_root_count':int(count),'outside_closed_parabola_margin_lower_bound':str(margin),'connected':True,'complement_connected':True,'no_clique_separator':True,'induced_P4':[0,4,1,3],'not_H3_edge_count':8,'scope':'Not a novelty certificate; certifies outside BRW parabolic sufficient condition and outside nontrivial join/clique-amalgamation generation from cographs, cycles, H3 by structural final-operation obstruction.'}
print(json.dumps(out,indent=2))
