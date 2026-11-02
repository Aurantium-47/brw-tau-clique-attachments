# Independent audit: weighted-star all-clique bound

2026-11-02. Separate AI mathematical review, not human peer review or formal verification. No external writes. Verdict: **the proposed sufficient bound is valid**, subject to the classical weighted Heilmann–Lieb theorem and BRW Bell-product preservation already used in the source notes. It does not prove the unweighted minimum-row realization and makes no novelty claim.

## Precise statement

Let H be a finite simple triangle-free graph with n vertices, e>=1 edges, and matching number ν. Add t>=0 isolated vertices, put N=n+t, and let G be the complement of this enlarged graph. If N>=e+ν, then, for every integer 1<=j<=N−ν,

    Q_j(z)=B(P_G(x)/R_j(x))

has nonnegative coefficients and only real nonpositive roots. Here P_G(x)=(-1)^N χ_G(-x), R_j=x(x+1)...(x+j−1), and B(x^d)=T_d(z) is the unscaled Bell transform. Consequently G is universally attachable to any ordinary τ-real graph along every clique of G, in the precise clique-sum sense in the source notes.

Thus t>=max(0,e+ν−n) suffices. For a forest with c components, including isolated vertices in c, this is t>=max(0,ν−c). For a connected tree with an edge it becomes t>=ν−1. This is a sufficient budget, not a necessary or claimed optimal one.

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

   Since k<=ν and j<=N−ν, each R_(N−k) is divisible by R_j. The rising-factorial Bell identity from the source notes, with c=j and r=N−j−k, gives

       B(R_(N−k)/R_j)=M_(K_(a−k,b−k)).

   Combining the identities proves Q_j=M_J. The order appearing in the rising factors is always N, never |V(F)|.

7. Weighted Heilmann–Lieb applies to J because its weights are nonnegative; zero-weight edges are removed if the theorem is stated with strictly positive weights. Since a+b=2a+j−1,

       μ_J(y)=(-1)^a y^(j−1) M_J(−y²).

   Every nonzero zero z of M_J would otherwise produce a nonreal zero of μ_J by y²=−z. Hence all zeros of M_J are nonpositive real. Its coefficients are nonnegative by their weighted-matching definition. Isolated rows and resulting zero roots cause no problem.

8. A maximum matching of H has ν disjoint edges, and an independent set can contain at most one endpoint from each, so α(H plus isolates)<=N−ν. Therefore every actual clique size of G lies in the established range. Also χ(G)=N−ν exactly: a coloring has classes of size at most two, whose two-vertex classes form a matching; a maximum matching supplies a coloring with N−ν classes. This proves both the initial divisor range and its maximality, but does not assert a clique of size χ(G).

9. For a clique union Y=G union_(K_j) X, the exact chromatic identity gives P_Y=(P_G/R_j)P_X. Bell-product preservation applies to Q_j and B(P_X), proving ordinary τ-realness whenever X is ordinary τ-real. In particular the j=1 case and X=K_1 also establish τ-realness of G. This uses the established BRW preservation result, not an additional combinatorial assumption.

If e=0, G=K_N. For 1<=j<=N, the quotient is ∏_(i=j)^(N−1)(x+i), and repeated Bell-product preservation directly proves the same assertion. N=0 has no positive clique size and is vacuous.

## Exact independent checks

`verify.py` directly enumerates weighted matchings row by row, independently constructs Bell transforms using Stirling numbers, and compares the coefficients exactly. It checks every j in the stated range for six inputs, then uses exact rational root isolation (not numerical root tolerances). The resulting certificate has 19 quotient checks.

Actual unweighted graph cases are P4 plus one isolate, C5 plus two isolates, K1,3, and three disjoint edges. The first two use the exact algebraic star masses (3±sqrt(5))/2 and (5±sqrt(5))/2, respectively. They exercise fractional forbidden weights and exact cancellation to integer matching counts. Two additional rational-mass cases (3/2,1/2) and (4/3,5/3) test weighted inclusion–exclusion but are **not claimed to arise from unweighted graphs**.

This distinction is unavoidable: λ_i are roots of the monic integer polynomial x^ν−e x^(ν−1)+m_2 x^(ν−2)−..., so any rational λ_i is integral. Nonintegral masses for unweighted H are algebraic irrational. Weighted Heilmann–Lieb accepts these real weights without difficulty.

## Scope and historical qualification

The theorem is an explicit combinatorial sufficient bound and weighted matching realization. BRW Proposition 5.13 already yields eventual universal clique attachment after sufficiently many joins with universal vertices, even beyond triangle-free-complement graphs, by shifting the nonreal chromatic roots into its sufficient region. This note must not claim first eventual closure or a wholly new qualitative phenomenon. Whether the explicit numerical budget here follows directly from that prior region using existing root bounds is not established by this audit. Existing special surrogate constructions can substantially improve the bound (for example, C5 requires no added isolates in the earlier odd-cycle note).
