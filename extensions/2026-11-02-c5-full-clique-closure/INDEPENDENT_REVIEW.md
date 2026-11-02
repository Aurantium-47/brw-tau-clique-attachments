# Independent mathematical review

2026-11-02. Verdict: **ACCEPT after the arithmetic repair recorded below.** This is an independent AI mathematical review, not human peer review or proof-assistant verification.

## Accepted scope

For p(z)=prod(z+a_i), a_i>=0, and q=sum a_i*kappa_i prod_{j!=i}(z+a_j), where 0<=kappa_i<=1/2 and sum kappa_i<=1, put L=z(1+D)+1, T=(L^2+L+I)p and F=L^3p+(L^2+L)q. T weakly interlaces F, and F+rT has only nonpositive real roots for every real r>=0.

The included seed argument applies this to p=(1+D)^2h, q=D(1+D)h for every nonzero nonnegative-coefficient polynomial h with nonpositive roots, without a degree bound. Consequently the m=3 maximal cycle quotient operator preserves that cone. The direct coloring computation proves that replacing a vertex of C5 by a graph in the full clique-quotient class preserves that class.

This does not settle arbitrary cycle lengths or the original unrestricted clique-sum conjecture. No historical priority or graph-family novelty was assessed.

## Proof checks

1. Independently expanded T/p and differentiated at a root of T. With X=t+sum u_i+2 and u_i=t/(t+a_i), the identities sum u_i^2=X^2-1 and tT'/p=2(sum u_i^3-X^3-X+1) are correct. The l3/l2 bound gives the required strict signs for both X branches, including |X|=1.
2. Independently derived the F/p identity using the second-order product rule. The affine residue reduction uses exactly the vertices with at most two active entries equal to 1/2; T stays fixed throughout this convexity argument.
3. Checked each of the four intervals in the G bound and each of the three intervals in the H bound. The initial manuscript had an arithmetic error for H at s>=1: the numerator is 5s+1, not 4s+1. Its asserted bound greater than -1 was therefore false. The repaired value is greater than -5/4, which is at least -Y/4-1 for Y>=1. Thus the global lower bound and final strict sign are unchanged. The corrected proof includes this repair.
4. The generic common-root exclusion is dense, as shown by the displayed rational expressions at the roots of p. Classical Bell-product preservation supplies real-rootedness of T; the nonzero derivative computation supplies simplicity. Negative F(t)/T'(t) gives the full degree-d versus degree-(d+1) interlacing, including both exterior roots.
5. Positive coefficients exclude nonnegative roots in the strictly positive generic case. Fixed monic degree, coefficient continuity and closure of real-rootedness justify repeated-root, zero-root and common-root boundaries. The same argument applies to the pencil F+rT for all fixed r>=0.
6. Rechecked the seed lemma independently: the ordered-root map of 1+D has strictly positive Jacobian entries; composing twice and scaling (D+t)^2 proves kappa_i<1/2. Partial fractions at zero yield sum kappa_i=q(0)/p(0)<1. Constant inputs have q=0. Approximation handles general admissible inputs.
7. Rechecked the exact operator recurrence and the direct C5 coloring count. Equal endpoint colors give (k-1)(k-2) internal colorings, and distinct endpoint colors give k^2-3k+3. Unsigned normalization and division by the maximal rising factorial yield the displayed quotient. Downward closure uses the standard L_j preservation argument.

The only classical preservation input retained is the cited BRW Bell-product theorem; the new proof does not replace that dependency.

## Independent computational checks

These finite checks corroborate identities and boundary handling; they are not the all-degree proof.

- `check_small_exact.py`: 78 exact polynomial-pencil cases, 42 rational-identity checks, 8 fixtures including repeated roots, zero roots and p/T common roots; squarefree Sturm counts verify every root is real and nonpositive. PASS.
- `check_translation.py`: inverse Bell transform followed by direct C5 quotient construction agrees with the differential operator for monomial inputs of degrees 0 through 6 with symbolic r. Seven checks PASS.
- The review's per-coordinate algebra also independently exposed and verified the H-bound repair.

No GPU, floating-point root approximation, or unproved numerical search is used as a proof premise. An optional larger diagnostic script is not included in the stated completed validation counts.
