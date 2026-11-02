# Odd-cycle complements via matching-equivalent forbidden trees

Date: 2026-11-02. AI-assisted research note; historical novelty unassessed.

## Result

For every integer m>=2, put n=2m+1 and G=complement(C_n). For each
1<=j<=m+1, the Bell transform B(P_G/R_j) has only real nonpositive roots.
In particular, G is universally attachable along an edge to an ordinary
tau-real graph, and along every clique of G. This settles the specified
odd-cycle-complement family, not unrestricted ordinary edge closure.

Definitions: P_G(x)=(-1)^n chi_G(-x), R_j(x)=x(x+1)...(x+j-1),
and B(x^d)=T_d(z), where T_d(z)=sum_q S(d,q)z^q is the Touchard
polynomial and S(d,q) is a Stirling number of the second kind.
Ordinary tau-realness means that Theta_G=B(P_G) has only real zeros.
This is the Bell normalization without factorial rescaling; it satisfies
Theta_G(z)=(-1)^n tau_BRW(G;-z). We use the Bell product identity
B(pq)=B(p) star B(q), where

    (f star g)(z)=sum_k z^k f^(k)(z) g^(k)(z)/k!.

Brenti--Royle--Wagner Proposition 5.4 supplies the preservation theorem:
if f and g have nonnegative coefficients and only nonpositive real
zeros, so does f star g. Nonzero constants are regarded as real-rooted.
Chromatic coefficient sign alternation makes P_X, hence Theta_X,
nonnegative-coefficient for every graph X; thus ordinary tau-realness
means all its roots are nonpositive. Each K_j is ordinary tau-real by
repeated Bell-product preservation applied to B(x+i)=z+i for the
factors of R_j (i=0,...,j-1).
The **original** n=|V(G)| is retained throughout; a matching surrogate is
permitted to have more vertices.

## 1. Matching-surrogate principle

Let H=complement(G) be triangle-free, with n original vertices. Thus its
matchings encode all independent-set partitions of G, giving

    P_G = sum_k (-1)^k m_k(H) R_(n-k).

Suppose a bipartite graph F has precisely the same matching numbers as H,
and admits a bipartition with sides of sizes at most a=n-j and b=n-1,
where j>=1. Since its matching number is at most a, all terms in this
expansion are divisible by R_j. Embed F in K_(a,b), adding isolated
vertices to complete the two board sides. Then

    B(P_G/R_j)(z) = M_J(z),  J=K_(a,b) minus E(F),
    M_J(z) = sum_l m_l(J) z^(a-l).

**Proof.** For c>=1 and r>=0, the Bell rising-factorial identity is

    B(product_(i=0)^(r-1)(x+c+i))
      = sum_l binom(r,l) binom(r+c-1,l) l! z^(r-l).

Its exponential generating function in r is
(1-u)^(-c) exp(zu/(1-u)); coefficient extraction proves the formula.
Since m_l(K_(a,b))=binom(a,l)binom(b,l)l!, setting c=j and r=a-k gives

    B(R_(n-k)/R_j) = M_(K_(a-k,b-k)).

Forbidden-edge inclusion-exclusion therefore gives

    M_J = sum_k (-1)^k m_k(F) M_(K_(a-k,b-k))
        = B(P_G/R_j).

Only equality of the matching numbers is needed; F need not equal H. No assertion
about equality of chromatic polynomials on different vertex counts is
being made. The usual matching polynomial is
mu_J(y)=sum_l (-1)^l m_l(J)y^(|V(J)|-2l). Heilmann--Lieb states
that all its roots are real and gives the desired roots via

    mu_J(y) = (-1)^a y^(j-1) M_J(-y^2).

The coefficients are nonnegative because M_J counts matchings. Bell
product preservation and P_(G union_(K_j) X)=P_G P_X/R_j give universal
ordinary tau-real attachment whenever G contains the stated clique.
Here attachment means intersection exactly a common K_j, no other
vertex identifications and no extra cross edges. The chromatic clique-sum
identity then gives the stated product/quotient formula. Taking the other
graph to be K_j also proves ordinary tau-realness of G.

## 2. A cycle and a fork have identical matching counts

Let n>=3. Label P_n by v_1,...,v_n. Let D_(n+1) be obtained by adjoining
one extra leaf w adjacent to v_2. (For n>=4 this is the familiar fork tree.)
For every k, deletion of the closing edge v_1v_n in C_n gives

    m_k(C_n) = m_k(P_n) + m_(k-1)(P_(n-2)).

Deleting the additional leaf edge wv_2 in D_(n+1) gives exactly the same
expression: if it is absent, the isolated w makes no difference; if it is
present, removal of w and v_2 leaves isolated v_1 and P_(n-2). Hence

    m_k(D_(n+1)) = m_k(C_n) for all k.

Here m_(-1)=0 and P_0 has one empty matching. The extra isolated vertex
in the second deletion is important for vertex bookkeeping but irrelevant
to matching numbers. Equivalently mu_D(y)=y mu_C(y).

## 3. Odd cycles: the whole feasible quotient range

Let n=2m+1, m>=2. The two parts of D_(n+1) have sizes m and m+2:
the even-indexed spine vertices v_2,v_4,...,v_(2m) form the smaller
part, while the other spine vertices and w form the larger part.
For 1<=j<=m+1,

    m <= n-j,    m+2 <= n-1 = 2m.

The surrogate principle proves the precise identity

    B(P_(complement C_(2m+1))/R_j)
       = M_(K_(2m+1-j,2m) minus E(D_(2m+2))).

Thus all these quotients have only real nonpositive zeros. Since
omega(complement C_(2m+1))=alpha(C_(2m+1))=m, this includes every
actual clique-attachment size. The extra algebraic value j=m+1 is
legitimate because every stable-partition term has n-k>=m+1. It does
not assert that G has an (m+1)-clique. In fact chi(G)=m+1, so R_(m+2)
does not divide P_G: the displayed range reaches the maximal possible
initial rising-factorial divisor.

The case n=5 agrees with the earlier uniform-cycle result, since C_5 is
self-complementary. The family n>=7 is the intended nonbipartite-complement
extension of the earlier board argument.

## 4. Disjoint-component extension

Suppose triangle-free H is a disjoint union of bipartite components and
c>=1 odd cycles of lengths at least five. Replace each odd cycle by its
fork and leave each bipartite component unchanged. Products of matching
generating polynomials show that the resulting bipartite F has the same
matching numbers as H. Its vertex count is n+c.

Choose the smaller side of each component as the first side (isolates
contribute zero to it), and let S be their total. The sides of F are
S and T=n+c-S. Each cycle contributes at least two to S, so S>=2c and
T<=n-c<=n-1. Also S<=(n+c)/2<=n-2: for c>=2 use n>=5c>=c+4;
for c=1 use n>=5=c+4. Thus the edge board always fits.
More generally, 1<=j<=n-S implies S<=n-j, so the quotient theorem
holds throughout this bounded range. Together with the bipartite case below, this includes all triangle-free
maximum-degree-two complements and arbitrary disjoint bipartite components.
If c=0, H itself is bipartite: for n>=3 choose nonempty parts s<=t
(if H is edgeless, take s=1,t=n-1). Then s<=n-2 and t<=n-1, so the
surrogate principle with F=H proves the edge result directly; for
1<=j<=t it proves the bounded quotient result. The edge-containing
case n=2 is G=K_2 with quotient 1. These observations handle c=0
without using the c>=1 inequalities.

This statement is **not** about attaching trees directly to a cycle
vertex. Matching equivalence alone need not preserve the vertex-deleted
matching counts required for such rooted attachments. Those connected
odd-cycle attachments remain outside the present proof.

## 5. Exact verification and limits

Run `python verify.py` (Python 3 with SymPy). The certificate contains 88
exact quotient/root checks for all odd n=5,7,...,25 and every
j=1,...,(n+1)/2. For every n, integer matching dynamic programming on
the fork agrees with m_k(C_n)=n/(n-k)*binomial(n-k,k). Exact rational
root counts verify all n-j roots are nonpositive. For n<=9, an independent
allowed-board row dynamic program verifies the inclusion-exclusion
coefficients directly for every recorded j. No numerical root tolerance
is used. These checks support, but are not premises of, the proof.

A separate `python check_components.py` run records 39 exact quotient/root
checks in `component_certificate.json` for C5+C7, C5+K1,6, C7+K2,3,
C5 plus four isolates, and three disjoint C5 components. It also replays
the original verifier.

No failure of the graph quotient criterion was found or asserted. The
ordinary BRW conjecture and general edge closure remain unresolved here.
Novelty and possible overlap with Mu--Shen--Xu are not assessed; their
previously inaccessible full text was not accessed or bypassed in this
pass. No external state was changed.

Primary foundational references:
Heilmann--Lieb, *Theory of monomer-dimer systems*, CMP 25 (1972),
doi:10.1007/BF01877590; Brenti--Royle--Wagner, *Location of Zeros of
Chromatic and Related Polynomials of Graphs*, CJM 46 (1994),
doi:10.4153/CJM-1994-002-3. The surrogate proof above is self-contained
apart from Heilmann--Lieb and the stated Bell-product preservation theorem.
