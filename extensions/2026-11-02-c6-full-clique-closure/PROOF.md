# m=4 rootedness by a stability-preserving mass-splitting argument

Proof, 2026-11-02. Independently reviewed and accepted; see audit_kernel/INDEPENDENT_REVIEW.md and audit_bridge/INDEPENDENT_REVIEW.md. No novelty claim.

## Statement
Let p(z)=prod_i(z+a_i), a_i>=0, and q(z)=sum_i a_i kappa_i prod_{j!=i}(z+a_j), where kappa_i>=0 and sum kappa_i<=1. Let L=z(1+D)+1, R=sum_{j=0}^3 L^j1, U=L^4 1, and V=R-1. Then for every r>=0,

    (U+rR) star p + V star q

has only nonpositive real roots. Here f star g=sum_j z^j f^(j)g^(j)/j! is the Bell product. This proves rootedness, not the stronger interlacing of R star p with the output. The restrictions kappa_i<=1/2 are unnecessary for this rootedness statement.

## Scalar interlacing certificate
Write W=U+rR, A=SW, C=W+V, where S=1+D. Explicitly,

R=z^3+7z^2+11z+4,
U=z^4+10z^3+25z^2+15z+1,
A=z^4+(r+14)z^3+(10r+55)z^2+(25r+65)z+15r+16,
C=z^4+(r+11)z^3+(7r+32)z^2+(11r+26)z+4r+4.

The resultant is

Res_z(C,A)=687r^5+1145r^4+15987r^3+29875r^2+95694r+101164>0.

Both A and C have simple negative roots for all r>=0. This follows either from the established constant-input interlacing and L,S preservation, or the following independent discriminant certificates:

Disc(C)=229r^6+916r^5+9696r^4+30428r^3+136908r^2+217360r+422496;
Disc(A)=r^4(1425r^2-3160r+2000)+r^2(71778r^2-24142r+1202393)+438818r+5525009.

The two displayed quadratics have positive leading coefficients and negative discriminants. Thus both quartic discriminants are positive for r>=0. At r=0 exact root isolation shows four simple negative roots and alternating order

    alpha_1 < gamma_1 < alpha_2 < gamma_2 < alpha_3 < gamma_3 < alpha_4 < gamma_4,

where alpha are roots of A and gamma roots of C. Continuity, fixed monic degree and positive discriminants preserve real-rootedness; nonzero resultant preserves this order. Positive coefficients exclude nonnegative roots.

Consequently C/A is a rational Pick function: its constant part is1 and each simple pole alpha_i has negative residue C(alpha_i)/A'(alpha_i). For completeness, W itself has four simple negative roots for every r>=0. Its discriminant is

Disc(W)=r^4(229r^2-660r+1000)+r^2(7798r^2-10122r+10000)+(82229r^2-47278r+227081).

The three quadratics have negative discriminants -480400, -209465116 and -72455364912, respectively, and positive leading coefficients. At r=0 four sign-changing negative rational intervals are (-319/49,-332/51), (-61/23,-53/20), (-13/17,-16/21), and (-1/13,-1/14). Continuity and positive coefficients give the assertion for all r>=0. Thus W/A is Pick: A=SW has roots to the left of and alternating with roots of W (standard derivative/logarithmic-derivative argument). Therefore for every K in[0,1],

    C_K/A=((1-K)W+K C)/A=(W+KV)/A

is Pick. It follows that C_K(w)+y A(w) is stable in the two upper-half-plane variables w,y, since its zero would require y=-C_K(w)/A(w), which cannot have positive imaginary part.

## Elementary operator stability
If f(w,other variables) is stable and y is a new variable, then

    (1+y(1+D_w))f

is stable. For upper-half-plane arguments, f is nonzero and the logarithmic derivative f_w/f has nonpositive imaginary part: all roots of the univariate specialization in w lie outside the upper half-plane. Meanwhile 1+1/y has strictly negative imaginary part. The expression equals

    y f [1+1/y+f_w/f],

so is nonzero. This argument also handles f constant in w.

## Multiaffine mass splitting
First assume a_i>0 and n>=1. Set K=sum kappa_i. Begin with the stable polynomial

    W(w)+K V(w)+y_1 SW(w).

For j=2,...,n apply the preceding stability-preserving operator 1+y_j S_w, using a fresh variable each time. The result is stable and multiaffine in all y variables, and equals

    P_(K,0,...,0)=prod_j(1+y_j S_w) W(w)
      + K prod_{j!=1}(1+y_j S_w) V(w).

For any nonnegative vector b define

    P_b=prod_j(1+y_j S_w) W(w)
      + sum_i b_i prod_{j!=i}(1+y_j S_w) V(w).

Swapping y_i,y_j swaps b_i,b_j. A partial symmetrization theta P_b+(1-theta)P_b(y_i<->y_j), 0<=theta<=1, therefore replaces b by the corresponding convex mixture of b and its coordinate swap. The partial symmetrization theorem for multiaffine stable polynomials guarantees that this operation preserves stability. This is NOT a claim that arbitrary convex sums of stable polynomials are stable.

Starting from b=(K,0,...,0), successively split mass from coordinate1 into coordinates2,...,n. If the current remaining mass is M and target coordinate j is kappa_j, choose theta=1-kappa_j/M, so the new coordinate j is kappa_j and the remaining coordinate1 is M-kappa_j. Previously assigned coordinates are untouched. Cases M=0 require no operation. Thus P_kappa is stable. K=0 is immediate.

The theorem applies with w treated as a fixed upper-half-plane parameter, so no assumption of multiaffinity in w is needed. Each partially symmetrized polynomial remains nonzero and stable for every such w.

## Diagonalization and identification
Set y_i=z/a_i and w=z, all upper-half-plane when z is. Multiplication by prod_i a_i gives a stable univariate polynomial. The identity

    [prod_i(a_i+z(1+D_w)) W(w)]_(w=z)=W star prod_i(z+a_i)

follows by expanding the commuting differential factors: choosing j derivatives gives exactly z^j W^(j) p^(j)/j!. Omitting factor i and multiplying by a_i gives the corresponding term of V star q. Hence the diagonal polynomial is exactly W star p+V star q.

Its coefficients are nonnegative and it is not zero, so all its real roots are nonpositive. Taking limits a_i down to0 proves the boundary cases; coefficients and monic leading degree stay fixed. Empty p=1,q=0 reduces to W.

## Dependencies and evidence boundary
The only non-elementary stability input is partial symmetrization:
J. Borcea, P. Branden and T. M. Liggett, *Negative dependence and the geometry of polynomials*, JAMS22(2009), Theorem4.20, states stability preservation for complex multiaffine generating polynomials under theta identity+(1-theta)transposition.
Primary source: https://www.ams.org/journals/jams/2009-22-02/S0894-0347-08-00618-8/S0894-0347-08-00618-8.pdf
Preprint: https://arxiv.org/abs/0707.2340

No arbitrary-convex-combination claim is used. No interlacing of F with T, m>=5 assertion, or historical novelty claim is made in this note. The older sparse two-active kernel factorization is a diagnostic antecedent, but is not needed for this more general proof.


## Actual-seed consequence
Let h be a nonzero polynomial with nonnegative coefficients and only nonpositive real roots. Divide by its positive leading coefficient to make it monic; linearity restores that factor at the end. Put g=Sh, p=Sg and q=Dg. Initially suppose h has simple strictly negative roots. Then g and p do as well, by the logarithmic derivative equation for S. At each root -a_i of p, q=-g and p'/g=(1+g'/g)'<0. Therefore the residues

    kappa_i=q(-a_i)/(a_i p'(-a_i))

are positive. The proper partial fraction expansion q/p gives sum kappa_i=q(0)/p(0)<1, because p-q=g and g(0)>0. No half-residue bound is needed. Constants give q=0. Approximation extends the conclusion to repeated or zero roots.

The mixed recurrence gives the actual m=4 operator as

    F_4^(r)=W star S^2h+V star DSh.

Hence this operator preserves the nonpositive-root cone for every input degree and every real r>=0.

## C6 substitution corollary
Let G be a nonempty graph having the full clique-quotient property: for r=omega(G), h=B(P_G/R_r) belongs to the nonnegative-coefficient/nonpositive-root cone, where P_G=(-1)^n chi_G(-x), R_j=x(x+1)...(x+j-1), and B maps x^j to the j-th Touchard polynomial. Smaller quotients follow from the maximal one by L_j=z(1+D)+j. Replace one vertex of C6 by G, joining all vertices of G to the two former neighbors u,v. The remaining u-v path has length4. The new clique number is r+1.

For k colors, when u,v have the same color the internal path admits (k-1)(k^2-3k+3) choices; when their colors differ it admits (k-2)(k^2-2k+2). For a direct check let A_m,D_m count length-m proper color walks with specified same or distinct endpoint colors. Then A_0=1,D_0=0 and A_(m+1)=(k-1)D_m, D_(m+1)=A_m+(k-2)D_m. Four applications yield the stated A_4,D_4 counts. Multiplying by k or k(k-1), respectively, and by chi_G(k-1) or chi_G(k-2) gives the chromatic polynomial. Its unsigned normalization yields

    P_H/R_2=(x+2)(x^2+2x+2) P_G(x+2) -(x^2+3x+3)P_G(x+1).

Writing f=P_G/R_r and sigma_j(y)=1+y+...+y^(j-1), the maximal quotient is

    P_H/R_(r+1)=(x+r+1)sigma_4(x+1)f(x+2)
                   -(x+1)sigma_3(x+1)f(x+1).

For the exact Bell identification, B[f(x+1)]=Sh and B[(x+1)f(x)]=L Bf. Put p=S^2h, q=DSh=p-Sh and T=I+L+L^2+L^3. The Bell transform of the displayed quotient is

    (L+r)T p -(L+L^2+L^3)(p-q)
      =L^4p+rT p+(L+L^2+L^3)q
      =(U+rR) star p+V star q.

Thus it equals the actual operator F_4^(r) above. Therefore it belongs to the cone. Every smaller actual clique quotient follows by the cone-preserving operators L_j. This proves preservation of the full clique-quotient class under C6 substitution. It does not prove all cycle lengths, ordinary-tau-only input closure, or historical novelty.
