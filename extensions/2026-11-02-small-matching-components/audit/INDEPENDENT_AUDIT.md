# Independent audit: full-clique double-star quotients

Date: 2026-11-02. Separate AI reasoning audit, not human peer review or formal proof verification. No historical novelty finding.

## Verdict

The proposed theorem and its disjoint-component extension are correct. The new graph-specific step is an elementary two-row matching surrogate; the Bell/board composition is the matching-surrogate principle restated in `RESEARCH_NOTE.md`. This audit checked that principle's signs, normalization, and embedding hypotheses as used here.

## Double-star calculation

Let D(p,q) consist of an edge uv, p leaves adjacent to u, and q leaves adjacent to v, with 1 <= p <= q. Its order is n=p+q+2. Every matching has size at most 2. There are p+q+1 single edges. A two-edge matching must select one pendant edge at each center, giving exactly pq choices. Thus its ordinary matching enumerator is 1+(p+q+1)t+pq t^2.

Take a bipartite graph F whose two row-neighborhoods have sizes p and q+1, with the first contained in the second. Such neighborhoods exist because p <= q+1. Its edge count is p+q+1. Ordered choices of one edge in each row total p(q+1), of which exactly p share a column. Hence m_2(F)=pq, and there are no higher matchings. The matching vectors agree exactly; equality of usual matching polynomials without a vertex-power correction is neither needed nor generally true.

The sides of F have sizes 2 and q+1. For every 1 <= j <= n-2, these satisfy 2 <= n-j and q+1 <= n-1. The board construction therefore gives the precise identity

    B(P_complement(D(p,q))/R_j) = M_(K_(n-j,n-1) minus E(F)).

The identity gives nonnegative coefficients and nonpositive real zeros by Heilmann--Lieb. The double star has maximum independent set consisting of all p+q leaves, and no independent set is larger: choosing either center excludes its leaves and the other center, leaving at most max(p+1,q+1) <= p+q. Thus alpha(D)=p+q=n-2, and the range covers every actual clique size in its complement. If p,q>=2, alpha exceeds the larger original bipartition side q+1 by p-1; this is genuinely beyond that particular board embedding. With p=1 no enlargement of that bound occurs, but the statement remains valid.

## Disjoint components and degeneracies

A nontrivial star K_(1,r) has a one-row surrogate with r columns, and matching number 1. An isolate contributes no edge or positive-degree matching coefficient, so it may be omitted from the surrogate while being retained in original n. For a disjoint union of these stars and double stars, take the disjoint union of the described surrogates. Products of matching generating polynomials prove equality of every matching count. Its row count is nu(H). Its column count is at most n-nu(H): the double-star column count q+1 <= p+q is the only nontrivial inequality; stars attain equality; omitted isolates only increase the available bound.

For H with an edge, nu(H)>=1 implies n-nu(H)<=n-1. For every j<=n-nu(H), the row count is at most n-j. By Konig's theorem, alpha(H)=n-nu(H) for bipartite H. Thus the entire clique range is covered. For H edgeless, G=K_n and the quotient is a rising-factorial tail; the existing Bell identity directly gives the complete board K_(n-j,n-1), including constant 1 when j=n. The original order n, not surrogate order, must be used throughout. n=1 and n=2 introduce no contradiction when handled this way. The empty graph has no positive clique size and needs no claim.

## Stronger optional extension

The same conclusion holds when every connected component of bipartite H has matching number at most 2; this includes non-tree components such as K_(2,r), not just stars and double stars.

Proof: apply Konig's theorem to a nontrivial component and choose a minimum vertex cover C of size nu<=2. If C is independent, its complement is independent by the vertex-cover property, so C versus V\C gives an actual bipartition with nu rows and |V|-nu columns. If C is not independent, nu=2 and its two vertices are adjacent. Every edge is incident to them. No vertex can be adjacent to both because H is triangle-free. Consequently the nontrivial component is exactly a double star. For nu=2 both pendant counts are positive; otherwise it would be a star with matching number 1. Replace that component by the Ferrers surrogate above. Disjoint union then finishes exactly as before.

## Attachment and scope

The standard chromatic clique-sum formula gives P_(G union_(K_j) X)=(P_G/R_j)P_X. Applying the stated Bell product preservation to the nonnegative real-rooted board enumerator and Theta_X proves universal ordinary tau-real attachment, provided the intersection and absence of extra cross edges have the usual stipulated meaning. This does not establish full-clique quotients for arbitrary co-bipartite graphs, arbitrary trees, or the general BRW clique-union conjecture. No conclusion about novelty or comparison with all older sufficient criteria follows.

## Important strength caveat: simpler factorization

For a single double star, setting s=p+q gives the exact factorization

    P_G = R_s[(x+s)(x+s+1) -(s+1)(x+s) +pq]
        = R_s(x+p)(x+q).

Therefore every P_G/R_j in the claimed range is itself a product of linear factors with nonnegative constants. Its Bell-realness follows alternatively from repeated Bell product preservation, without a surrogate. The complement is chordal: the p+q original pendant leaves form a clique, while each original center is simplicial, and the two centers are nonadjacent. Thus this particular family does not show any advance beyond real-chromatic-root/chordal sufficient criteria, even though it closes the stated limitation of the literal complement-board embedding. At j=s the Bell quotient is exactly z^2+(s+1)z+pq.

## Independently verified non-real-chromatic example

Let H be the disjoint union of two D(2,2), and G its complement. Here n=12, nu(H)=4, and alpha(H)=8. Each connected component has its unique bipartition sizes 3,3, so every bipartition of H has sizes 6,6. Thus the full quotient range through j=8 strictly exceeds every original-complement bipartition bound, not just one poorly chosen orientation.

Using the exact matching enumerator (1+5t+4t^2)^2 in the signed rising-factorial expansion independently gives

    Q(x)=P_G/R_8=x^4+28x^3+302x^2+1483x+2792,
    B(Q)(z)=z^4+34z^3+393z^2+1814z+2792.

Independent SymPy exact rational root counting returned 0 real roots for Q and 4 negative roots for B(Q). There are also short elementary certificates, eliminating dependence on root-counting software:

* With y=x+7, Q(x)=y^4+8y^2-y+6=y^4+8(y-1/16)^2+191/32>0 for every real x. Thus the quartic Q has no real root.
* The Bell quartic takes values 648,-118,-48,74,8,-78,-96,50 at -16,-15,-10,-9,-6,-5,-4,-3 respectively. The four disjoint intervals (-16,-15), (-10,-9), (-6,-5), and (-4,-3) each contain a root by the intermediate value theorem. A quartic has at most four roots, so these are all roots and all are strictly negative.

The two centers from each double-star component induce two disjoint edges in H. In G, the same four vertices induce K_(2,2), an induced C4; hence G is not chordal. Since P_G=R_8 Q and Q has no real zeros, G is not a graph with all-real chromatic zeros. This shows that the disjoint-component theorem is not restricted to the simple chordal/all-real-chromatic situation of a single double star. It does not establish that this example lies outside BRW Proposition 5.13's chromatic-root region or any other older sufficient theorem.

## Precise nonimplication of the direct BRW Proposition 5.13 hypothesis

For H=D(2,2) disjoint union D(1,1) disjoint union D(1,2), n=15, nu(H)=6, alpha(H)=9. The matching generating polynomial is

    (1+5t+4t^2)(1+3t+t^2)(1+4t+2t^2).

I independently expanded the chromatic stable-partition sum, retaining original n=15 and dividing each falling-factorial term by (x)_9. It gives exactly

    f(x)=chi_complement(H)(x)/(x)_9
        =x^6-57x^5+1369x^4-17710x^3+129992x^2-512731x+848168.

Independent exact SymPy calculation `Poly(f,x).count_roots(Rational(1015,100)+I*Rational(363,100), Rational(1016,100)+I*Rational(364,100))` returned 1. Thus a nonreal chromatic zero lies in that rational rectangle. For every point s+it of its closed rectangle,

    t^2-s-1/4 >= (363/100)^2-1016/100-1/4
               =27669/10000 >0.

I independently opened the original primary BRW paper and checked pp.70--71: the region R_T(m) is defined by 4t^2 < 1+4m+4s, and Proposition 5.13 requires the attached factor's nonreal chromatic zeros to lie in R_T(0). The certified zero violates even the weak/closed version of that region. The strict-versus-weak boundary convention is therefore immaterial to this example.

Primary source: Brenti--Royle--Wagner (1994), DOI https://doi.org/10.4153/CJM-1994-002-3, original PDF https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8B66867EF89BFB7C22DDD36E718D8157/S0008414X00045016a.pdf/location-of-zeros-of-chromatic-and-related-polynomials-of-graphs.pdf .

Consequently the full-clique surrogate theorem covers a graph failing the direct nonreal-root hypothesis of Proposition 5.13. This is a precisely scoped separation of hypotheses, not proof that every attachment involving this graph is unavailable by Proposition 5.13 (the two factors can sometimes be interchanged), nor exclusion of indirect applications, other published criteria, or historical overlap. The earlier 12-vertex example remains only a nonchordal/non-real-chromatic example; its previously stated caveat is retained.


## Portable independent audit replay

Run `python audit/check_independent.py` from the package root. The script independently reconstructs both examples from unsigned matching products and falling-factorial chromatic expansions, verifies the 12-vertex sum-of-squares and Bell sign brackets, checks that all four nonreal chromatic roots of the 12-vertex example are strictly **inside** R_T(0), and verifies the 15-vertex squarefree residual, exact complex rectangle root count, and rational exclusion margin. It imports only SymPy, never reads sibling files, uses explicit runtime checks that remain enabled under `python -O`, and has a standard main guard. The successful exact run is recorded in `audit/independent_run.log`.

The 12-vertex example therefore is not a separation from Proposition 5.13; only the 15-vertex example provides the precisely limited direct-hypothesis separation discussed above.
