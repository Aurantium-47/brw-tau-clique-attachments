# Independent audit: all-degree m=4 stability bridge

2026-11-02. Verdict: ACCEPT the displayed theorem and C6 full-clique-quotient consequence. No historical novelty assessment; no m>=5 or stronger pencil-interlacing claim.

Reviewed `brw_m4_vertex_kernel_20261102/PROOF.md`, including the self-contained W discriminant and actual-seed/graph sections. This audit was independent of the earlier sparse-kernel review.

## Primary-source dependency

Read Borcea, Brändén and Liggett, *Negative dependence and the geometry of polynomials*, arXiv:0707.2340v2, Theorem 4.20 and its proof, PDF pages 29–30 (printed pages 29–30 in that preprint): https://arxiv.org/pdf/0707.2340 . The theorem explicitly permits **complex** multiaffine stable generating polynomials. Its proof fixes the other upper-half-plane variables before reducing to the two swapped variables. Thus applying it after fixing w is valid even though the original polynomial need not be multiaffine in w. No homogenization, positivity of specialized complex coefficients, or limiting mass-redistribution theorem is required. The AMS PDF endpoint returned 403 to this audit; the primary arXiv version was accessible.

## Main mathematical checks

1. Independently reconstructed R,U,W,A,C from L and S. Recomputed the resultant Res(C,A), both displayed quartic discriminants, and W's discriminant decomposition exactly. All positivity claims follow from the stated negative quadratic discriminants and nonnegative coefficients.
2. Independently isolated r=0 roots by rational intervals. A,C alternate in the specified orientation. Fixed monic degree, nonzero discriminants, and nonzero resultant preserve the ordering for every r>=0. Consequently residues C(alpha)/A'(alpha) are negative, so C/A maps the upper half-plane into itself. W/A has the same sign by the elementary S-root interlacing argument. Their convex mixture is Pick, which proves C_K(w)+yA(w) stable for 0<=K<=1.
3. The fresh-variable operator 1+y(1+D_w) is stable-preserving by the logarithmic derivative argument even when other variables are specialized to complex upper-half-plane values. The strict negative imaginary part of 1/y prevents cancellation; constants are harmless.
4. Each partial swap really mixes the corresponding two residue masses. Starting with (K,0,...,0), at most n-1 swaps with theta=1-kappa_j/M allocate the desired masses. M=0 is handled separately. This is a finite argument and does not assert arbitrary convex combinations of stable polynomials preserve stability.
5. Diagonal substitutions w=z and y_i=z/a_i preserve upper-half-plane nonvanishing for a_i>0. Expansion of the commuting differential factors gives exactly W star p+V star q. Independent symbolic checks with arbitrary a_i,kappa_i,r confirmed this for n=1,2,3,4. The general expansion is an elementary identity, not inferred from those checks.
6. The diagonal polynomial has real nonnegative coefficients. Stability and conjugation force all roots real; coefficient nonnegativity excludes positive roots. Its monic leading degree stays fixed, so limits as a_i tend to zero cover zero/repeated-root boundaries. Empty input reduces to W.
7. The actual seed p=S^2h,q=DSh has positive residues and total mass q(0)/p(0)<1 for simple strictly negative h. This uses p-q=Sh and the logarithmic derivative at roots of p. No half-residue bound is required. Constant and boundary inputs follow separately/by limits.
8. Reconstructed the C6 endpoint-color counts independently using the length-four complete-graph walk recurrence. The resulting unsigned R2 quotient and maximal quotient agree with the proof. Independently verified the Bell/operator bridge symbolically in r on x^n for n=0,...,6, in addition to checking its general recurrence identity. Clique number increases from r to r+1, and lower quotients follow by the usual L_j preservation.

## Reproducible evidence

`check.py` uses explicit runtime guards, not removable assertions. `python -I -O check.py` passed. It checks the resultant, three discriminants and their positive decompositions, base root intervals/order, four symbolic diagonal identities, and seven symbolic-parameter Bell graph/operator identities.

The proof is accepted as mathematics, not on the basis of numerical probing. No floating-point root evidence is used. The initial checker-development issues (zero polynomial degree and removable assert statements) were corrected before the final guarded run; neither affected the mathematical argument.

Additional independent graph validation: `python -I -O check_graphs.py` passed for seeds K1, K2, I2, P3 and C4. Each output chromatic polynomial was reconstructed from all Whitney edge subsets, not the proposed endpoint formula; it agrees with that formula, has maximum clique omega(G)+1, and its maximal Bell quotient has exactly its degree many real roots and nonnegative coefficients. This is a modest cross-check, not the proof of the arbitrary-graph corollary.
