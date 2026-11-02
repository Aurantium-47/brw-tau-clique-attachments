# Full-clique quotients for complements with small matching components

Date: 2026-11-02. AI-assisted mathematical research; historical novelty not asserted.

## Result

**Theorem.** Let H be a finite simple bipartite graph on n vertices such that every connected component has matching number at most two, and let G be its complement. For every integer 1 ≤ j ≤ ω(G), the Bell transform B(P_G/R_j) has only real nonpositive zeros and nonnegative coefficients. Consequently attaching G along any of its cliques to an ordinary tau-real graph preserves ordinary tau-realness.

This includes arbitrary disjoint unions of stars, double stars, and bipartite graphs supported on two independent cover vertices, together with any number of isolates. In particular it settles every double-star complement, including clique sizes larger than both colorclasses of the original connected complement. It does not settle arbitrary tree complements, all co-bipartite graphs, or general BRW clique union.

Here P_G(x)=(-1)^n χ_G(-x), R_j(x)=x(x+1)…(x+j−1), and B(x^d)=T_d(z), the Touchard polynomial. Ordinary tau-real means B(P_G) is real-rooted. These are the unscaled Bell conventions of the preceding notes.

## 1. The small-row surrogate

**Lemma.** If H is bipartite and every connected component has matching number at most two, and H has an edge, there is a simple bipartite F with the same matching numbers as H and a specified bipartition of sizes

    S = ν(H),       T ≤ n−ν(H) ≤ n−1.

Isolates of H may be omitted from F; n always remains the original order of H.

**Proof.** Work componentwise. An isolated vertex contributes no edge and may be omitted. By König's theorem a nontrivial bipartite component has a vertex cover C of size its matching number r, where r is one or two. If C is independent, its complement is independent by the vertex-cover property. Thus C and V\C form a bipartition with r rows and n_component−r columns. Keep this component unchanged.

Otherwise r=2 and C={u,v} is an edge. Every remaining vertex lies outside the cover, so no two remaining vertices are adjacent. Each is adjacent only to u or v; none can meet both because H is triangle-free. Connectedness forces each to meet one of them. Thus this component is a double star D(p,q): adjacent centers with p and q pendant leaves. Because its matching number is two, p,q≥1. Swap the centers if needed so p≤q.

Its matching generating polynomial is

    m_H(t)=1+(p+q+1)t+pq t².

The only two-edge matchings choose one leaf edge from each center; a matching containing the central edge has no other edge. Now take F_component with two row vertices and q+1 columns, with nested row neighborhoods of sizes p and q+1. Its edge number is p+q+1, and its two-edge matching count is

    p(q+1)−p = pq.

It has no larger matching. Hence it is matching-equivalent, and its column count q+1≤p+q=n_component−2. This is an elementary Ferrers-board rook count, not a newly asserted counting principle.

Disjoint union multiplies matching generating polynomials. Taking the component surrogates gives row total S=Σr=ν(H), column total T≤Σ(n_component−r)≤n−ν(H). As H has an edge, ν(H)≥1, giving T≤n−1. ∎

## 2. Exact quotient realization through the entire clique range

For a bipartite H, König's theorem gives

    ω(G)=α(H)=n−ν(H).

Fix 1≤j≤n−ν(H), put a=n−j, b=n−1, and embed the lemma's F into K_(a,b). The bounds S=ν(H)≤a and T≤b prove that the embedding exists. Let J be the complete board with the embedded edges of F deleted, retaining all board vertices. Then

    B(P_G/R_j)(z) = Σ_(l=0)^a m_l(J) z^(a−l).             (1)

For clarity, this identity follows from the classical matching-surrogate mechanism, recalled here rather than assumed. Trianglefreeness of H makes every independent block of G a singleton or an edge of H. Hence

    P_G = Σ_k (−1)^k m_k(H) R_(n−k).

Since k≤ν(H)≤n−j, every summand is divisible by R_j. The Bell identity

    B(∏_(i=0)^(r−1)(x+c+i))
       = Σ_l binom(r,l) binom(r+c−1,l) l! z^(r−l)

comes by extracting coefficients from (1−u)^(−c) exp(zu/(1−u)). Setting c=j and r=a−k expresses B(R_(n−k)/R_j) as the reversed matching enumerator of K_(a−k,b−k). Forbidden-edge inclusion–exclusion on K_(a,b) therefore gives (1), since m_k(F)=m_k(H). The exponents are a−k−l; no extra z^k factor is inserted.

The matching polynomial of J satisfies

    μ_J(y) = (−1)^a y^(j−1) M_J(−y²),
    M_J(z) = Σ_l m_l(J) z^(a−l).

The Heilmann–Lieb real-root theorem implies every nonzero zero of M_J is negative; zero roots are allowed. Coefficients count matchings and are nonnegative. If H is edgeless, G=K_n and the same identity holds with empty forbidden graph for every 1≤j≤n, including a=0,j=n and constant polynomial 1. For n=0 there is no positive clique size to consider.

For a clique attachment X∪_(K_j)G, with intersection exactly K_j and no additional cross edges, the chromatic identity gives P_union=P_X P_G/R_j. The Bell product identity B(fg)=B(f)⋆B(g), with

    (f⋆g)(z)=Σ_k z^k f^(k)(z)g^(k)(z)/k!,

and BRW's real-nonpositive-root preservation prove the attachment assertion.

## 3. A strict extension of the original colorclass bound

For connected D(p,q), 1≤p≤q, the original two colorclasses have sizes p+1 and q+1. The previous direct-board theorem guaranteed only j≤q+1. The result above reaches every actual clique size

    j≤α(D(p,q))=p+q=n−2.

For p≥2 this is a strict improvement by p−1 values. At the maximal value, J is K_(2,p+q+1) minus the two-row Ferrers surrogate, so the entire maximal-clique quotient is explicitly quadratic:

    B(P_G/R_(n−2))
      = z²+(p+q+1)z+pq.

Indeed the allowed row degrees are q+1 and p, with overlap p, giving m₂=pq. The discriminant is (p−q)²+2(p+q)+1>0. This explicit formula is an additional direct check, not needed for the general proof.

**Important overlap caveat.** The double-star complement already satisfies

    P_G(x)=R_(p+q)(x)(x+p)(x+q).

This follows by factoring R_(p+q) from its three-term matching expansion. In particular all chromatic zeros are real integers. It is also chordal: the original leaves form a clique, and the two original centers are nonadjacent simplicial vertices. Thus this connected family already follows from real-chromatic-root sufficient criteria (and directly from Bell product preservation of the displayed real-linear factors). The new calculation closes the particular board-size gap, not a demonstrated gap in the known BRW attachment scope. The broader component theorem is an exact valid combined statement. Section 6 supplies a precise failure of the hypothesis of BRW Proposition 5.13 for one instance, without a novelty claim.

## 4. Scope and attribution

The classical components are König's theorem; elementary Ferrers-board matching counts; the complement matching/chromatic correspondence and rectangular forbidden-board inclusion–exclusion of Farrell–Whitehead (1992); Heilmann–Lieb (1972); and BRW (1994) Bell product preservation and clique chromatic identity. The preceding literature audit already identifies different-order matching surrogates in Farrell–Whitehead. No historical novelty is claimed for these ingredients or for the combined family theorem. Full-text overlap with Mu–Shen–Xu remains unassessed; no access restriction was retried or bypassed.

References and exact source positions appear below; the earlier [published attribution audit](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/fde6a285e7241b04f84fdde1806106d0cc433cce/MATCHING_LITERATURE_STATUS.md) records the primary-text provenance. This pass performs no external writes. Independent AI audit is recorded separately; it is not human peer review or proof-assistant verification.

The bounded research question is decided positively for this infinite subclass. The unresolved next boundary is a connected bipartite complement of matching number at least three with no independent minimum cover; no universal small-row surrogate theorem or counterexample is asserted here.

## 5. Exact finite verification and comparison example

Run `python verify.py` with NetworkX and SymPy installed. The run checked 122 graphs and all 585 positive clique-size quotients: qualifying bipartite atlas graphs through seven vertices, 21 double stars 1≤p≤q≤6, and three disjoint-component examples. Independent vertex-deletion matching recursion verifies surrogate equivalence; exact polynomial division and the monomial Bell transform agree with board inclusion–exclusion. Exact real-root counts certify all n−j roots are nonpositive. For 452 quotients with n≤8, an independent allowed-board matching DP agrees as well. `certificate.json` records every polynomial and the direct-check flag; `run.log` records the completed run. The proof does not depend on these finite checks.

Consider H=D(2,2)⊔D(2,2). Every bipartition has sides 6,6, while α(H)=8. Thus j=7,8 exceed the old direct-embedding bound. Its complement contains an induced C4 on the two pairs of centers, so is not chordal. At j=8,

    Q(x)=P_G/R_8=x⁴+28x³+302x²+1483x+2792,
    B(Q)=z⁴+34z³+393z²+1814z+2792.

Writing y=x+7 gives Q=y⁴+8(y−1/16)²+191/32>0, so Q has no real roots. An independent audit certifies four negative roots of B(Q) by sign changes on (−16,−15), (−10,−9), (−6,−5), (−4,−3).

**Nevertheless this example is already covered by BRW Proposition 5.13.** The primary BRW paper, p.70, defines R_T(m) by 4(Im q)²<1+4m+4 Re q; p.71 states the attachment criterion for R_T(0). The nonreal chromatic factor is f(q)=Q(−q). Exact complex root counts give one upper-half-plane root in each rectangle

    6.91<Re q<6.93, 0.90<Im q<0.92;
    7.07<Re q<7.09, 2.67<Im q<2.69,

and one in each conjugate rectangle. On these rectangles, Re q+1/4−(Im q)² is bounded below by 3946/625 and 839/10000 respectively, both positive. These four roots exhaust the quartic. `check_region.py` and `region_certificate.json` certify strict inclusion. Therefore neither this nonchordal example nor the connected double stars establish an attachment class outside that older sufficient criterion. The combined component theorem remains valid. The next section supplies a different example outside that particular sufficient condition; this n=12 example does not.

Primary source inspected for this comparison: Brenti–Royle–Wagner, *Location of Zeros of Chromatic and Related Polynomials of Graphs*, Canadian Journal of Mathematics 46 (1994), 55–80, DOI https://doi.org/10.4153/CJM-1994-002-3 ; [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8B66867EF89BFB7C22DDD36E718D8157/S0008414X00045016a.pdf/location-of-zeros-of-chromatic-and-related-polynomials-of-graphs.pdf).

## 6. A proved example outside the BRW 5.13 region

A bounded scan of the three already verified component examples identifies a different outcome for

    H=D(2,2)⊔D(1,1)⊔D(1,2),       n=15, ν(H)=6, α(H)=9.

Its matching generating polynomial is

    (1+5t+4t²)(1+3t+t²)(1+4t+2t²).

The component theorem proves the matching realization and real nonpositive Bell roots for every 1≤j≤9. This includes j=9 beyond the largest possible original complement colorclass (8). Independent exact division gives

    χ_G(x)/(x)_9
     = x⁶−57x⁵+1369x⁴−17710x³+129992x²−512731x+848168.

An exact complex root count finds one root in the rational rectangle

    1015/100 < Re x < 1016/100,
     363/100 < Im x <  364/100.

Throughout this rectangle,

    (Im x)²−Re x−1/4 ≥ (363/100)²−1016/100−1/4
                       = 27669/10000 > 0.

Thus this graph has a nonreal chromatic zero outside even the **closed** region underlying BRW Proposition 5.13. The checker reconstructs the chromatic residual from the matching product, verifies squarefreeness and absence of boundary-line roots by polynomial gcd, and certifies the root count and inequality using exact rational arithmetic; see `check_region.py` and `outside_region_certificate.json`.

**Precise comparison:** the full-clique component theorem has at least one instance for which the hypothesis of BRW Proposition 5.13 fails. This is not a proof of historical novelty, exclusion from other known criteria or their closures, or a solution of general BRW clique union. It does not exclude swapped-factor or indirect applications of Proposition 5.13; it certifies failure of its direct chromatic-region hypothesis for this graph. It does not contradict the earlier n=12 example's inclusion in the region. The finite search stopped upon obtaining this single exact comparison witness, as intended.

## References and source positions

- F. Brenti, G. F. Royle, D. G. Wagner, *Location of Zeros of Chromatic and Related Polynomials of Graphs*, Canadian Journal of Mathematics **46** (1994), 55–80. DOI: https://doi.org/10.4153/CJM-1994-002-3. Proposition 1.1 (p.56): clique chromatic formula; Propositions 5.2 and 5.4 (pp.69–70): product identity/preservation; region definition and Theorem 5.5 (p.70); Proposition 5.13 (p.71): sufficient chromatic-region attachment criterion. The Bell convention here is the sign-reflected normalization, not the paper's raw signed tau notation.
- E. J. Farrell and E. G. Whitehead Jr., *Connections between the matching and chromatic polynomials*, International Journal of Mathematics and Mathematical Sciences **15** (1992), 757–766. DOI: https://doi.org/10.1155/S016117129200098X. Theorem 1 / Corollary 1.1 (p.759): triangle-free complement matching expansion; Theorem 3 (p.760) and Corollary 3.2 (p.761): forbidden-board inclusion–exclusion; Theorem 7 (pp.761–762): matching-equivalent different-order surrogates. These source positions come from the prior local primary-text audit, not a novelty search in this pass. [Primary journal archive PDF](https://www.maths.tcd.ie/EMIS/journals/HOA/IJMMS/Volume15_4/213850.pdf).
- O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics **25** (1972), 190–232. DOI: https://doi.org/10.1007/BF01877590. Real-rootedness of the matching polynomial is the root-location input.

König's matching/vertex-cover theorem and two-row Ferrers rook counting are classical; their usage and all needed elementary counting details are explicit above. The independent reviewer suggested the minimum-cover formulation that enlarges the initial double-star/star statement to every component of matching number at most two.
