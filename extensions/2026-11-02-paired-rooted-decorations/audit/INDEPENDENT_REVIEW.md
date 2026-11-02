# Independent audit: paired rooted decorations

Date: 2026-11-02. Computational/mathematical assistant audit, not human peer review. Historical novelty not evaluated. Reviewed `../RESEARCH_NOTE.md` against the accepted matching-surrogate principle in the antecedent note, *Odd-cycle complements via matching-equivalent forbidden trees*.

## Verdict

The main theorem and the rooted C5 obstruction are correct as stated. No mathematical repair is required. This audit does not extend the theorem to arbitrary unpaired decorations or all actual clique sizes.

## Indexed matching proof

Write each attachment vertex as `(i,u)`, where `u=0` is its root and the rooted isomorphisms identify local vertex labels in paired copies. The left residual has vertex set `V(B) - {(1,0),(L,0)}`. The right residual, after removing the specifically isolated vertex `(1,0)`, has vertex set `V(B) - {(1,0),(2,0)}`. The map `(i,u) -> (L+2-i,u)` is defined on every left-residual vertex, is a bijection onto the right-residual set, and preserves edges:

* surviving spine indices `2,...,L-1` map to `L,...,3`, reversing their path;
* interior whole attachments map to their rooted-isomorphic counterparts;
* root-deleted attachment at L maps to root-deleted attachment at 2.

Any isolated vertices inside a root-deleted attachment are preserved too. Removing the isolated vertex v1 changes no matching number. Thus the two edge-deletion recurrences give identical ordinary matching generating polynomials. H has N vertices and F has N+1; equality of matching numbers does not imply equal usual matching polynomials without their vertex-count factor (indeed mu_F = y mu_H).

## Structural and capacity checks

Distinct copies must have disjoint nonroot vertices and meet the spine only at their designated roots. Under this stated construction H is connected because each attachment is connected. It is triangle-free: attachments are bipartite and a triangle using more than one block cannot exist across a single-vertex junction; the spine cycle has L>=5. It is nonbipartite because its spine is an odd cycle. B and F are bipartite, and F is connected.

For each paired root, `i+(L+2-i)=L+2` is odd, so roots occupy opposite spine colors. If a rooted graph's color classes have sizes a (root color) and b, its nonroot contributions are `(a-1,b)` at one root and `(b,a-1)` at its partner. Combined contribution is `a+b-1=|T|-1` to each side. Hence N=2s+1 and the F sides are exactly s,s+2. Since s>=2, both board capacities hold throughout 1<=j<=s+1. This uses original N, not N+1. Matching number <=s ensures the quotients are genuine polynomials.

Connectedness of each attachment is sufficient and natural for the advertised connected family. It is not necessary for the algebraic identity: paired disconnected rooted bipartite graphs also work if copies of all detached components are colored oppositely in pairs. Arbitrary bipartite-color routines may orient detached components inconsistently, so connectedness cleanly avoids that implementation ambiguity.

Boundary L=5 with trivial attachments passes and has s=2. L=3 is not covered, because H contains a triangle and the triangle-free complement expansion fails. Trivial and root-deleted-disconnected decorations pose no problem.

## Bounded clique scope is essential

Take L=5, put a rooted 3-leaf star at each of v2 and v5, and leave the other spine vertices undecorated. Then N=11, s=5. H has an independent set consisting of all six pendant leaves and v1,v3, and exact enumeration gives alpha(H)=8. Therefore its complement has an 8-clique, while this theorem guarantees only j<=6. The author correctly avoids claiming universal attachment along all actual cliques. This example is NOT a counterexample to larger-j real-rootedness; it only shows those j are outside the proved range.

## Rooted C5 obstruction

The five-edge classification is complete. A bipartite cycle must be a C4; adding a pendant/disjoint edge produces respectively 4/6 two-matchings, not 5. Therefore F is a forest. Since sum binom(deg(v),2)=5, max degree <=3 and the only feasible nonisolated degree multiset is (3,2,2,1,1,1). It has six vertices and five edges, hence is connected. The two possible claw subdivisions have arm lengths (3,1,1) and (2,2,1); the latter has a three-matching. The former is D6. The two degree-2 root choices have deletion enumerators 1+3t+2t^2 and 1+3t, not P4's 1+3t+t^2. Isolates cannot fix a mismatch. The wedge identity in the note is also correct.

## Independent reproducible computations

No author verifier was imported. Standard-library Python only:

```
python audit/verify_paired.py
python audit/verify_c5_obstruction.py
```

`verify_paired.py` reconstructs nine families/examples (N=5 through 13), including rooted edges, endpoint paths, rooted stars, rooted squares, mixtures, and one disconnected-attachment stress test. All nine pass explicit residual vertex/edge isomorphism, exact matching enumerator equality, and direct triangle enumeration. Every connected example passes exact bipartition-size checks. Thirty-three quotient checks independently expand rising-factorial quotients into ordinary powers, apply Stirling-number Bell transforms, and compare with direct row-by-row allowed-board matching counts. No floating-point root approximation is used or needed for these identities. This audit relies on the accepted Heilmann--Lieb argument rather than claiming an additional independent root-count test.

`verify_c5_obstruction.py` enumerates every nonisolated simple bipartite five-edge graph with part sizes at most 5 (each nonisolated vertex touches at least one of five edges). Thus its enumeration covers any finite graph order after removing isolates, not merely graphs with at most six vertices. It examines 1,329 labeled candidates, finds 24 with matching polynomial 1+5t+5t^2, all with parts (2,4) and D6's degree sequence, and finds zero valid roots. Certificates are `paired_certificate.json` and `c5_obstruction_certificate.json`.

Only local audit files were written. No external state was changed.
