# Graph scope of the all-cycle linear-input result

For an actual graph with n=omega+1, choose a maximum clique K_r. The remaining vertex has d neighbors in it, 0<=d<=r-1, and the unsigned chromatic polynomial is R_r(x)(x+d). Thus linear Bell inputs of actual graphs are precisely h=z+d in this family. The analytic theorem permits all real a>=0,r>=1, but graph parameters satisfy these integer restrictions.

The already-proved full C5 substitution closure covers m=3, join closure covers m=2, and the ordinary edge-quotient theorem covers the full clique case r=1. The new linear invariant gives every m>=4 for these non-complete clique-plus-one-vertex seeds. This is a stronger **internal certified subfamily**, not a claim of historical novelty. Whether every resulting graph is already covered by some other theorem remains unverified.

## Concrete criterion separation

Take r=2,d=0,m=5: substitute K2 disjoint K1 into one vertex of C7. Label the length-five path 0-1-2-3-4-5, and the seed vertices6,7,8. Add edge6-7 and connect each seed vertex to both0 and5. The graph has9vertices and12edges, clique number3.

Its chromatic polynomial is
chi_G(x)=x(x-1)(x-2) Q(x),
Q=x^6-9x^5+35x^4-75x^3+95x^2-71x+26.
There is exactly one zero of Q in the open rectangle
(317/500,159/250)+i(247/250,99/100).
Every point in that rectangle has
(Im x)^2-Re x-1/4 > (247/250)^2-159/250-1/4=2817/31250>0.
Hence this graph fails even the closed direct parabolic root-region sufficient condition of BRW Proposition5.13. The rectangle count is exact, not a floating-point root estimate. This does not rule out other classical theorems, matching representations or historical proofs.

The graph has no universal vertex and no clique separator. Its complement is connected and contains triangles, so the previously used triangle-free-complement matching recipe does not directly apply. Its displayed quotient by the seed module is C7, not C5. These are bounded structural distinctions, not an exhaustive classification of all possible existing closure derivations or chromatically equivalent graphs.
