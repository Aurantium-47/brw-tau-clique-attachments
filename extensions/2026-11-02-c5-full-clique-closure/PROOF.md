# Degree-free m=3 compatibility from an elementary cubic estimate

2026-11-02. Theorem with independent mathematical review. No historical novelty claim.

## Statement
Let L=z(1+D)+1, p(z)=prod_i(z+a_i), a_i>=0, and
q(z)=sum_i a_i*kappa_i*prod_{j!=i}(z+a_j), where 0<=kappa_i<=1/2 and sum kappa_i<=1.
Put T=(L^2+L+I)p and F=L^3 p+(L^2+L)q.
Then T and F have only nonpositive real roots and T weakly interlaces F. Consequently F+rT has only nonpositive real roots for every real r>=0.
For generic distinct positive a_i (specified below), interlacing is strict and all roots are strictly negative.
A positive scalar multiple is harmless; the empty product is allowed.

## Classical input
The Bell product f star g=sum_k z^k f^(k)g^(k)/k! preserves polynomials with nonnegative coefficients and only nonpositive real roots (Brenti–Royle–Wagner 1994, Propositions 4.2 and 4.4). Since
T=(z^2+4z+3) star p=(z+1)(z+3) star p,
T has only nonpositive real roots. We do not re-prove this classical theorem here.

## Generic reduction
Initially assume all a_i>0 distinct, and T and p have no common zero. This is a dense condition: at a root -a_i of p,
T(-a_i)/p'(-a_i)=2a_i^2 sum_{j!=i}1/(a_j-a_i)+2a_i^2-4a_i.
For n>=2 each expression is a nonconstant rational function of any one other a_j, so its zero set has empty interior. For n=1 it vanishes only at a_1=2; n=0 is vacuous. A finite union of these algebraic zero sets has empty interior in the positive distinct-root locus.
All coefficients of T are positive, so its real roots t are strictly negative.

## Root identities
Fix a root t of T, set
u_i=t/(t+a_i), u=sum_i u_i, v=sum_i u_i^2, w=sum_i u_i^3, X=t+u+2.
Direct division gives
T/p=(z+z p'/p+2)^2 - sum_i (z/(z+a_i))^2 -1.
Thus at t,
v=X^2-1, so |X|>=1 and |u_i|<=sqrt(X^2-1)<|X|.
The derivative identity is
D0 := t T'(t)/p(t)=2(w-X^3-X+1).
Since |w|<=v^(3/2), D0<0 for X>=1, whereas D0>0 for X<=-1. In particular T'(t)!=0; all roots of T are simple.

Write h=q/p=sum_i kappa_i(1-u_i). Using T(ph)=hT(p)+2z(z+z p'/p+2)p h'+z^2 p h'', we obtain
N := F(t)/p(t)
 = D0+1 - sum_i kappa_i (1-u_i)(1+2X u_i-2u_i^2).
The desired inequality is F(t)/T'(t)=t*N/D0<0. It is enough to show N and D0 have the same sign.

## Polytope reduction
At fixed p and t the quantity N is affine in kappa. The polytope 0<=kappa_i<=1/2, sum kappa_i<=1 has exactly the vertices with zero, one or two active coordinates, each equal to1/2. This follows by scaling x_i=2kappa_i: any two fractional coordinates can be perturbed against one another, and a single fractional coordinate either has slack or contradicts integral sum2 on a tight constraint. Thus it suffices to check those vertices.
Let k in{0,1,2} be the number of active coordinates. At a vertex,
N=3-2X^3-2X + sum_inactive 2u_i^3
 + sum_active [u_i^3+(X+1)u_i^2-(X-1/2)u_i-1/2].

## Upper bound when X>=1
For every real s with |s|<=sqrt(X^2-1), define
G_X(s)=s^3-(X-1)s^2-(X-1/2)s-1/2
      =(s-X)s(s+1)+(s-1)/2.
We claim G_X(s)<=(X-1)/4.
- If s<=-1, both summands in the factored expression are nonpositive.
- If -1<=s<=0, (X-s)(-s(s+1))<=(X+1)/4 and (s-1)/2<=-1/2, giving the bound.
- If 0<=s<=1, both factored summands are nonpositive.
- If s>=1, X>=sqrt(s^2+1)>=s+1/(2s+1). Hence
  G_X(s)<=-s(s+1)/(2s+1)+(s-1)/2=-(3s+1)/(2(2s+1))<0.
The elementary square-root bound follows by squaring: (s+1/(2s+1))^2<=s^2+1 for s>=0.
An active summand is therefore <=2X s^2+(X-1)/4. An inactive summand satisfies 2s^3<=2X s^2, since s<X. Summing and using v=X^2-1 gives
N<=3-2X^3-2X+2X(X^2-1)+k(X-1)/4
 <=3-4X+(X-1)/2=(5-7X)/2<0.

## Lower bound when X<=-1
Write Y=-X>=1 and s_i=-u_i. Now sum s_i^2=Y^2-1 and
N=3+2Y^3+2Y + sum_inactive (-2s_i^3)
 + sum_active [-s_i^3+(1-Y)s_i^2-(Y+1/2)s_i-1/2].
For |s|<=sqrt(Y^2-1), define
H_Y(s)=-s^3+(Y+1)s^2-(Y+1/2)s-1/2
      =(Y-s)s(s-1)-(s+1)/2.
We claim H_Y(s)>=-Y/4-1.
- If s<=0, the first factored summand is nonnegative and the second is >=-1/2.
- If 0<=s<=1, (Y-s)s(s-1)>=-Y/4 and -(s+1)/2>=-1.
- If s>=1, Y-s>=1/(2s+1), so
  H_Y(s)>=s(s-1)/(2s+1)-(s+1)/2=-(5s+1)/(2(2s+1))>-5/4>=-Y/4-1.
Thus each active summand is >=-2Y s_i^2-Y/4-1, and each inactive summand is >=-2Y s_i^2. Therefore
N>=3+2Y^3+2Y-2Y(Y^2-1)-k(Y/4+1)
 >=1+(7/2)Y>0.
This agrees with the sign of D0 in both cases, proving strict interlacing.

## Boundary and pencil conclusion
For generic p, T is monic degree n+2 and F is monic degree n+3. The negative ratios F(t)/T'(t) give one zero of F in each gap and both exterior intervals, by alternating signs and leading terms. Thus strict interlacing holds. The same sign argument applies to F+rT for every real r; when r>=0 all its coefficients are nonnegative and its constant term is positive, so all roots are negative.
Approximate arbitrary labeled a_i>=0 by distinct positive generic a_i, holding the admissible kappa vector fixed. All coefficients, including q expressed as products omitting one factor, vary continuously; degrees and leading coefficients of T and F+rT are fixed. Limits of real-rooted polynomials remain real-rooted, and interlacing persists weakly. Nonnegative coefficients rule out positive roots. This proves the statement, including repeated and zero roots.

## Translation to the actual cycle operator
For admissible h, put p=S^2h, q=DSh, S=1+D. The previously established seed-residue lemma gives q/p=sum a_i*kappa_i/(z+a_i) with 0<kappa_i<1/2 and sum kappa_i<1 for strict generic h. The exact recurrence gives the m=3 quotient operator F_3^(r)=F+rT, with the F,T above. Therefore the seed lemma and limiting argument imply the all-degree m=3 quotient result for every real r>=0. The seed lemma is reproduced and proved below. No claim is made for m>=4 or historical novelty/new graph-family coverage.

## Seed lemma, included for completeness
Let h be monic with distinct strictly negative roots. For any such polynomial g, the roots b_i of Sg are the unique zeros, one to the left of the first root and one in each consecutive gap, of
1+sum_j 1/(z-alpha_j).
The derivative in z is negative, and implicit differentiation gives
partial b_i/partial alpha_j=(b_i-alpha_j)^(-2)/sum_k(b_i-alpha_k)^(-2)>0.
Thus S and S^2 have smooth ordered-root maps with entrywise positive Jacobians.
Put g=Sh, p=Sg and q=g'. At a root -a_i of p, q=-g, while p'/g<0; therefore kappa_i=q(-a_i)/(a_i p'(-a_i))>0. Consider p_t=(D+t)^2h and its root rho_i(t). Under the scaling H_t(y)=t^n h(y/t), the ordered roots of S^2H_t are y_i(t)=t rho_i(t). Since every original root of h is negative and the S^2 root-map Jacobian is entrywise positive, y_i'(1)=rho_i(1)+rho_i'(1)<0. On the other hand, implicit differentiation gives rho_i'(1)=-2g(rho_i)/p'(rho_i) and kappa_i=rho_i'(1)/(-2rho_i). Thus kappa_i<1/2. Finally partial fractions at zero give sum kappa_i=q(0)/p(0)<1, because p-q=h+h' has positive value at zero. Constants have q=0. Approximation covers the entire nonnegative-coefficient/nonpositive-root cone.
Consequently the abstract theorem applies unconditionally to p=S^2h,q=DSh, including limits. The explicit maximal-quotient operator at m=3 is
B[(x+r+1)(1+(x+1)+(x+1)^2) f(x+2) -(x+1)(1+(x+1))f(x+1)], h=Bf.
Its recurrence expands exactly to F+rT. This proves preservation for every input degree and real r>=0.

## Graph corollary and scope
For a nonempty graph G define P_G(x)=(-1)^|V(G)| chi_G(-x), R_j=x(x+1)...(x+j-1), and the full clique-quotient property by B(P_G/R_j) belonging to the nonpositive-root cone for all actual clique sizes j. In particular take r=omega(G) and f=P_G/R_r. Replace one vertex of C5 by G, joining every vertex of G to the two former neighbors of the replaced vertex, and leave all other edges unchanged. Its clique number is r+1. The established coloring identity gives exactly the displayed m=3 maximal quotient. It is therefore in the cone. Each smaller quotient follows from multiplying the polynomial quotient by x+j, whose Bell action is L_j=z(1+D)+j; this operator preserves the cone by the ordinary derivative/interlacing argument. Thus the full clique-quotient property is preserved by this C5 substitution.
This strengthens the previously retained ordinary-tau-input/edge-output cycle statement within this project. It does not establish full cycle substitution for m>=4, general clique-sum closure from ordinary tau inputs, or historical novelty. The original Bell-product theorem is classical; the seed proof above reproduces the project's previously reviewed lemma, not a new claim of invention.

For completeness, the C5 coloring identity can be checked without a general cycle formula. Denote its two neighbors of the substituted vertex by u,v, and its remaining path by u-a-b-v. With k colors, if u,v have the same color there are k choices for that color, (k-1)(k-2) colorings of a,b, and chi_G(k-1) colorings of G. If u,v have different colors there are k(k-1) ordered choices, k^2-3k+3 colorings of a,b, and chi_G(k-2) colorings of G. Hence
chi_H(k)=k(k-1)(k-2)chi_G(k-1)+k(k-1)(k^2-3k+3)chi_G(k-2).
The unsigned normalization gives
P_H/[x(x+1)]=(x^2+3x+3)P_G(x+2)-(x+2)P_G(x+1),
and dividing by R_(r+1) yields the displayed quotient exactly. The equal-color internal count follows by choosing a first and then b distinct from that color and the endpoint color. For different endpoint colors, choosing a equal to the color of v gives k-1 choices for b; the other k-2 choices of a each give k-2 choices for b, totaling k^2-3k+3.
