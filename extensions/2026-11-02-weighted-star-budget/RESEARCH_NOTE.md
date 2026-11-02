# Weighted stars and an explicit all-clique attachment budget

2026-11-02. AI-assisted research note; historical novelty unassessed. The proof uses classical weighted Heilmann–Lieb real-rootedness and BRW Bell-product preservation. It does not assert an unweighted minimum-row realization.

## Precise statement

Let H be a finite simple triangle-free graph with n vertices, e>=1 edges, and matching number ν. Add t>=0 isolated vertices, put N=n+t, and let G be the complement of this enlarged graph. Write m_H(u)=∏_(i=1)^ν(1+λ_i u) and C=Σ_i ceil(λ_i). The λ_i are positive by Heilmann–Lieb. If N>=C+1 (in particular if N>=e+ν), then, for every integer 1<=j<=N−ν,

    Q_j(z)=B(P_G(x)/R_j(x))

has nonnegative coefficients and only real nonpositive roots. Here P_G(x)=(-1)^N χ_G(-x), R_j=x(x+1)...(x+j−1), and B(x^d)=T_d(z) is the unscaled Bell transform. Consequently G is universally attachable to any ordinary τ-real graph along every clique of G, where the intersection is exactly a common complete graph K_j, with no other vertex identifications and no added cross edges. Nonzero constants count as real-rooted.

Thus the spectral budget t>=max(0,1+C−n) suffices, as does the purely combinatorial budget t>=max(0,e+ν−n). No additional N>=2ν hypothesis is required: n>=2ν for every graph H, and N=n+t>=n. For a forest with c components, including isolated vertices in c, this is t>=max(0,ν−c). For a connected tree with an edge it becomes t>=ν−1. This is a sufficient budget, not a necessary or claimed optimal one.

## Proof with all bookkeeping explicit

1. The weighted matching polynomial theorem, applied first to unweighted H, yields

       m_H(u)=sum_k m_k(H)u^k=∏_(i=1)^ν(1+λ_i u), λ_i>0.

   Indeed μ_H(y)=y^(n−2ν)∏_i(y²−λ_i), with its nonzero roots real and paired in opposite signs. Comparing the coefficient of u gives Σλ_i=e. No simple-root assertion is needed.

2. For each λ_i make one star centered at row i, with floor(λ_i) unit-weight edges and one edge of weight λ_i−floor(λ_i), omitting the latter when zero. Use disjoint column sets for distinct stars. This gives a finite simple **weighted** bipartite graph F with ν rows, C=Σceil(λ_i) columns, every edge weight in (0,1], and m_F(u)=m_H(u). There is no identification of the vertex counts of F and H.

3. Write r for the number of nonintegral λ_i. If r=0 then C=e<=e+ν−1. If r>0 then s=Σ fractional_part(λ_i) is a positive integer (since e and all floors are integers), so C=e+r−s<=e+ν−1. Thus N>=e+ν implies C<=N−1. In fact the sharper sufficient hypothesis is N>=C+1; original N>=n>=2ν already holds.

4. Fix 1<=j<=N−ν and set a=N−j, b=N−1. Then a>=ν and b>=C, so F embeds in K_(a,b). Put w=0 on cells outside F and define an allowed board J with weights 1−w, all nonnegative. Edges of weight zero can simply be deleted. Weighted matchings multiply their edge weights; let M_J(z)=Σ_l m_l(J)z^(a−l).

5. Weighted inclusion–exclusion is exact, including for irrational weights. For each matching S of K_(a,b), expand ∏_(f in S)(1−w_f)=Σ_(T subset S)(−1)^|T|∏_(f in T)w_f. A nonzero T is a matching of F. The number of unweighted completions after removing its k rows and columns is governed by K_(a−k,b−k), independently of T. Therefore

       M_J(z)=Σ_k (−1)^k m_k(F) M_(K_(a−k,b−k))(z).

   No weighted deletion theorem or integrality of the weights is needed for this identity.

6. Triangle-freeness is used precisely to identify all stable color classes of G with singletons and edges of H. Thus

       P_G=Σ_k(−1)^k m_k(H) R_(N−k).

   Since k<=ν and j<=N−ν, each R_(N−k) is divisible by R_j. The rising-factorial Bell identity proved below, with c=j and r=N−j−k, gives

       B(R_(N−k)/R_j)=M_(K_(a−k,b−k)).

   Combining the identities proves Q_j=M_J. The order appearing in the rising factors is always N, never |V(F)|.

7. Weighted Heilmann–Lieb applies to J because its weights are nonnegative; zero-weight edges are removed if the theorem is stated with strictly positive weights. Since a+b=2a+j−1,

       μ_J(y)=(-1)^a y^(j−1) M_J(−y²).

   Every nonzero zero z of M_J would otherwise produce a nonreal zero of μ_J by y²=−z. Hence all zeros of M_J are nonpositive real. Its coefficients are nonnegative by their weighted-matching definition. Isolated rows and resulting zero roots cause no problem.

8. A maximum matching of H has ν disjoint edges, and an independent set can contain at most one endpoint from each, so α(H plus isolates)<=N−ν. Therefore every actual clique size of G lies in the established range. Also χ(G)=N−ν exactly: a coloring has classes of size at most two, whose two-vertex classes form a matching; a maximum matching supplies a coloring with N−ν classes. This proves both the initial divisor range and its maximality, but does not assert a clique of size χ(G).

9. In this normalization B(pq)=B(p) star B(q), where (f star g)(z)=Σ_k z^k f^(k)(z)g^(k)(z)/k!. BRW Propositions 5.2/5.4, after sign reflection, give that this product preserves nonnegative-coefficient polynomials with only nonpositive real zeros. Ordinary τ-realness means precisely that B(P_X) has only real zeros; its coefficients are nonnegative by chromatic coefficient sign alternation.

   For a clique union Y=G union_(K_j) X, the exact chromatic identity gives P_Y=(P_G/R_j)P_X. Bell-product preservation applies to Q_j and B(P_X), proving ordinary τ-realness whenever X is ordinary τ-real. In particular the j=1 case and X=K_1 also establish τ-realness of G. This uses the established BRW preservation result, not an additional combinatorial assumption.

If e=0, G=K_N. For 1<=j<=N, the quotient is ∏_(i=j)^(N−1)(x+i), and repeated Bell-product preservation directly proves the same assertion. N=0 has no positive clique size and is vacuous.

## Bell rising-factorial identity

For integers c>=1 and r>=0, define A_r(x)=∏_(i=0)^(r−1)(x+c+i). Then

    B(A_r)(z)=Σ_l binom(r,l) binom(r+c−1,l) l! z^(r−l).

Indeed Σ_r A_r(x)u^r/r!=(1−u)^(−x−c). The Touchard generating identity B(exp(xv))=exp(z(exp(v)−1)) makes its Bell transform

    (1−u)^(−c) exp(zu/(1−u)).

Expanding in z first gives the coefficient z^h as u^h(1−u)^(−c−h)/h!. Its u^r coefficient times r! is r!/h! binom(c+r−1,r−h); put l=r−h to obtain the stated formula. Setting c=j, r=a−k yields the reversed matching polynomial of K_(a−k,b−k), since b−k=r+c−1.

## Direct comparison with the old chromatic-root region

BRW Proposition 5.13 gives universal attachment when all nonreal chromatic zeros lie in R_T(0)={q : (Im q)²<Re q+1/4}. It already implies eventual attachment after joining any fixed graph with a sufficiently large complete graph, because joining K_t shifts the nonreal chromatic roots to the right by t. Thus eventual closure itself is not a new qualitative conclusion here.

Our numerical hypothesis does **not** force that direct region hypothesis. Take H to be three disjoint stars K1,3, so n=N=12, e=9, ν=3, and N=e+ν with no padding. Its matching polynomial is (1+3u)^3. For G=complement(H),

    χ_G(x)/(x)_9=x³−21x²+155x−396.

Exactly one zero of this cubic lies in the rational rectangle

    7.18 < Re x < 7.19,    2.84 < Im x < 2.85.

Every point in the rectangle satisfies (Im x)²−Re x−1/4>=(2.84)²−7.19−1/4=391/625>0. The checker `region/check_region.py` reconstructs the polynomial and verifies squarefreeness, boundary-line root absence, and exact complex root counts. It certifies failure even of the closed region condition. This graph is nevertheless a cograph and belongs to earlier structural closure families. The example separates direct hypotheses only: it does not establish new graph scope, exclude other results or indirect uses of BRW, or prove historical novelty.

## Verification and limitations

The release checker `checkers/verify.py` compares weighted matching enumeration with direct Bell transforms and exactly isolates roots in 19 cases. Four underlying unweighted graphs are P4 plus one isolate, C5 plus two isolates, K1,3, and three disjoint edges; all feasible j are checked. Two rational-mass diagnostic inputs exercise the weighted identity but are not asserted to be unweighted graphs. The P4 and C5 cases use algebraic radicals exactly. Any rational λ_i of an unweighted graph must be integral by the rational-root theorem applied to x^ν−e x^(ν−1)+m_2x^(ν−2)−.... Thus rational fractional masses are diagnostics, not misleading graph examples.

Historical audit files are preserved unchanged in `independent_audit/`; their last paragraph predates the exact region witness above. The guarded release checker is authoritative for reproducible execution. Fresh independent AI review and its additional finite checks are included in `fresh_review/`. These are not human peer review or proof-assistant verification. Finite checks support, but are not premises of, the general proof. No optimal budget, unrestricted BRW conjecture, or historical novelty is claimed. Potential overlap with inaccessible Mu–Shen–Xu full text remains unresolved; no access control was bypassed.

## Classical sources and attribution

- O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190–232. [DOI](https://doi.org/10.1007/BF01877590). Weighted matching-polynomial real-rootedness is the root-location input.
- F. Brenti, G. F. Royle and D. G. Wagner, *Location of Zeros of Chromatic and Related Polynomials of Graphs*, Canadian Journal of Mathematics 46 (1994), 55–80. [DOI](https://doi.org/10.4153/CJM-1994-002-3). Proposition 1.1 gives the clique chromatic identity; Propositions 5.2/5.4 give product/preservation; p.70 defines R_T(m); Proposition 5.13 supplies the direct root-region attachment criterion. The last region and proposition were rechecked in the original paper in this pass.
- E. J. Farrell and E. G. Whitehead Jr., *Connections between the matching and chromatic polynomials*, International Journal of Mathematics and Mathematical Sciences 15 (1992), 757–766. [DOI](https://doi.org/10.1155/S016117129200098X). Theorem 1/Corollary 1.1 give triangle-free complement matching expansion; Theorem 3/Corollary 3.2 give forbidden-board inclusion–exclusion; Theorem 7 permits different-order matching surrogates. Source positions follow the preceding local primary-text audit. The weighted form needed here is proved explicitly above.
