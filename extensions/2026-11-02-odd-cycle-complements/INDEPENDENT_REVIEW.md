# Independent AI mathematical review

Date: 2026-11-02. Reviewer: a fresh child agent assigned specifically to audit
RESEARCH_NOTE.md and verify.py. This is not human peer review or proof-assistant
verification. No external publication or other external write was performed.

## Verdict

No mathematical correction to the main theorem, surrogate identity, odd-cycle
range, or disjoint-component extension was found. The results are proved,
conditional only on the same established matching-root and Bell-product
preservation theorems used in the accepted co-bipartite note.

## Checks performed

1. Triangle-freeness of H is exactly what makes every independent block of
   complement(H) have size at most two. The stable-partition matching expansion
   and its (-1)^k sign therefore apply even when H is nonbipartite.
2. Equal matching numbers suffice for forbidden-edge inclusion-exclusion.
   The original n remains in R_(n-k), a=n-j, and b=n-1. No use is made of a
   false equality between chromatic polynomials on n and n+1 vertices.
3. If the surrogate embeds with first side at most a, all nonzero matching
   terms have k<=a, so division by R_j is legitimate before transformation.
4. For C_n, selecting its closing edge leaves P_(n-2). For the fork, selecting
   its extra leaf edge leaves P_(n-2) plus an isolated vertex. Omitting the
   distinguished edge leaves P_n (and an isolated vertex in the fork).
   Hence every matching count agrees, including the empty matching.
5. The fork has n+1 vertices and, when n=2m+1, parts m and m+2. The bounds
   m<=n-j and m+2<=n-1 hold exactly as claimed for m>=2 and j<=m+1.
6. omega(complement(C_(2m+1)))=m; chi=m+1 follows from packing m disjoint
   cycle edges as color classes and the lower bound on color classes of size
   at most two. Thus j=m+1 is algebraically valid but is not a clique size;
   R_(m+2) cannot divide P_G since chi_G(m+1)>0.
7. For the disjoint extension, the product rule preserves matching counts,
   the surrogate has n+c vertices, S>=2c, and T=n+c-S<=n-c<=n-1.
   The bound S<=(n+c)/2<=n-2 is valid because n>=5c and c>=1, including
   the tight n=5,c=1 case. Thus all 1<=j<=n-S fit.
8. The matching-polynomial conversion has sign (-1)^a and exponent j-1.
   Its degree is 2a+j-1=a+b, so the substitution and nonpositive-root
   conclusion have correct normalization.
9. Nonnegative coefficients come from allowed-board matching counts, not
   merely a signed chromatic expansion. Bell-product preservation then
   gives the stated graph attachments with precisely a common clique and
   no additional identifications or cross edges, as in the accepted note.
10. The rooted-attachment limitation is correctly retained. An unrooted
    matching surrogate does not automatically handle attached trees.

## Computations reproduced and supplemented

- Re-ran `python verify.py`: PASS, 88 exact cases, odd n from 5 through 25,
  every j from 1 through (n+1)/2.
- Read the matching recursion and the allowed-board row dynamic program.
  Both have correct state transitions; the latter is independent of
  forbidden-board inclusion-exclusion and covers all j at n=5,7,9.
- Independently performed 33 further symbolic checks for odd n=5 through 15:
  explicitly expand P from rising factorials, divide by R_j with exact zero
  remainder, apply the Stirling-number definition B(x^d)=T_d, and compare
  against the claimed inclusion-exclusion polynomial. All passed.

## Editorial clarifications (nonblocking)

- Section 1 reuses F for both the surrogate and an attached tau-real graph in
  its last formula. Using X for the attached graph would remove ambiguity.
- The phrase “all triangle-free maximum-degree-two complements” combines the
  c>=1 result with the previously proved bipartite c=0 case. Explicitly saying
  so would make the scope self-contained.
- Graph attachment should retain the precise intersection/no-extra-cross-edges
  conditions from the accepted note whenever this result is restated publicly.

No historical novelty assessment was attempted. The unavailable
Mu--Shen--Xu full text was not accessed or bypassed.

## Component-check addendum

After the initial review, inspected and replayed `check_components.py`:
39 additional exact cases passed for C5+C7, C5+K1,6, C7+K2,3,
C5 plus four isolated vertices, and three disjoint C5 components, throughout
the asserted j bounds. Verified the supplied S values (5,3,5,2,6), the
original graph vertex counts, and T=n+c-S. This supplement computes original
complement matching counts directly rather than assuming the fork identity.

## Standalone-note revision review

Re-read the expanded standalone note. The explicit Touchard/Bell definitions,
Bell-star formula, rising-factorial generating function and coefficient identity,
clique-intersection convention, and separate c=0 bipartite argument are correct.
The max-degree-two scope clarification has been incorporated. The author is
also replacing the reused attachment symbol F by X. For complete expository
closure, recommended explicitly recording chromatic coefficient sign alternation
(to make Theta_X nonnegative), the definition of mu_J, and that K_j is ordinary
tau-real by applying Bell-product preservation to the linear transforms
B(x+i)=z+i of the factors of R_j. These are standard immediate justifications,
not corrections to the theorem or its proof mechanism.
