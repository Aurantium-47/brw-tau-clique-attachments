# Independent review: all-cycle linear-input propagation

Date: 2026-11-02. Verdict: **ACCEPT** the stated F3 invariant and its all-iteration consequence for a ≥ 0 and real r ≥ 1. This is an independent AI mathematical review, not human peer review or proof-assistant certification. No historical novelty or new graph-family claim is assessed.

## Material reviewed

- `brw_m4_invariant_probe_20261102/LINEAR_SEED_PROOF.md`
- Its exact checker and full coefficient certificate.
- The complete proof of Lemma 2 in `brw_uniform_operator_deliverable_20261102/RESEARCH_NOTE.md`, including the arrowhead construction, rank-two residue representation, eigenvalue bounds, and Jensen potential estimate.

## Mathematical findings

1. For h=z+a, p=S²h=z+a+2 and q=DSh=1, the actual fixed source is H=Lq+r p=(r+1)z+r(a+2)+1. Starting F1=(L+r)p, direct iteration gives exactly the displayed quartic F3. Thus the theorem uses the correct recurrence, not the ordinary edge-quotient recurrence with a different source.
2. The two sectors r−1 ≥ a and a ≥ r−1 cover the entire closed quadrant. Every supplied coefficient of all four sector polynomials was independently recomputed and matched. Strictly positive constant terms exclude boundary exceptions.
3. Positive quartic discriminant plus four real simple negative roots at the base point establishes four simple real roots throughout the connected parameter domain. Fixed monic degree precludes roots escaping to infinity along a compact path, and positive coefficients exclude nonnegative roots. Positive discriminant alone would not suffice, but the connectedness/base-point argument supplies the missing information correctly.
4. The ordered roots and residues are continuous. The two nonzero resultants exclude κ=1 and κ=−1. Independent rational interval bounds at the base point establish |κ|<1, so this persists everywhere.
5. Since deg H=1<4, partial fractions give sum κ=H(0)/F3(0)=w. Direct positive arithmetic gives 0<w<1. Differentiating the resultant product gives R'(1)/R(1)=−(w+V), and consequently G/D=2−w−V>0. The resultant sign and denominator are controlled by the exact certificates.
6. All hypotheses of the older arrowhead lemma are therefore met. Its proof is valid for residues of either sign. At each iteration H remains fixed of degree1 while the monic output degree increases, and H(0)>0 throughout. The lemma's Schur complement is 1+w>0, its rank-two eigenvalues lie strictly between −1 and1, and the convex potential closes exactly at V=2−w. Hence every Fm, m≥3, has simple strictly negative roots, with strict consecutive interlacing from F3 onward.

No repair to the submitted argument was needed. Its reference to earlier m=1,2 results should be retained, or replaced with the elementary supplement below if a completely self-contained shorter-range proof is desired.

## Independent exact validation

Run `python -I -O brw_linear_propagation_audit_20261102/check_independent.py` from the workspace root. This independently reconstructs the recurrence and checks:

- the full quartic formula;
- every coefficient in eight sector expansions (four polynomials, two sectors);
- all four base-point root intervals and their rational residue bounds;
- four quotient-ring multiplication traces at independently chosen rational parameters;
- the rank-two spectral-potential formula and its invariant boundary identity.

All checks passed. Results are in `RESULT.json`. These finite algebraic checks validate identities used in the proof; they are not finite sampling evidence substituted for the infinite induction.

## Optional shorter-range supplement

F1 has discriminant (a−r)²+4a+8>0 and positive coefficients. For F2, put b=r−1. Its cubic discriminant has strictly positive coefficients in both sectors b=a+t and a=b+t: respectively23 and22 terms, constant469 and minimum coefficient1. At a=b=0, its roots lie in(-6,-5),(-3,-2),(-1,0). The same continuity argument gives simple negative roots for F2. These statements were independently checked but do not alter the submitted certificate.

## Scope

The result is uniform in cycle length for linear cone inputs, not uniform in input degree. It does not solve the all-degree m≥4 problem, the full BRW clique-amalgamation conjecture, or establish historical priority. The strict interlacing proven by this seed-and-propagation argument begins at F3; no earlier consecutive-pair claim is inferred without a separate argument.

## Independently verified graph-scope example

The graph H5(K2 disjoint K1) has path edges 01,12,23,34,45, seed edge67, and six edges from each of0,5 to each of6,7,8. Direct Whitney expansion over all4096 edge subsets gives

chi(x)=x^9−12x^8+64x^7−198x^6+390x^5−506x^4+429x^3−220x^2+52x.

Direct clique enumeration gives omega=3. Division by x(x−1)(x−2) gives exactly

Q(x)=x^6−9x^5+35x^4−75x^3+95x^2−71x+26.

An exact complex root count gives one root in the rectangle (317/500,159/250)+i(247/250,99/100). Real/imaginary polynomial gcd checks on each boundary line exclude boundary roots. For every point in the closed rectangle,

(Im z)^2−Re z−1/4 ≥ (247/250)^2−159/250−1/4 =2817/31250>0.

Thus a genuine chromatic root violates even the closed direct parabolic condition. The unsigned normalization is P(x)=−chi(−x) because the graph has odd order9; the maximal unsigned quotient is Q(−x), with even quotient degree6. No sign change was silently applied to the chromatic-root rectangle.

Independent finite structural checks additionally find independence number4, connected complement, no clique separator, no universal vertex, and no five-vertex module whose contraction is C5. These exclude co-bipartite membership, nontrivial join, nontrivial clique-amalgamation decomposition, nontrivial universal-clique lift, and direct final single-vertex C5 substitution respectively. They do not exclude every earlier theorem, construction, or possible equivalent formulation.

**Accepted scope:** direct BRW Proposition5.13 hypothesis separation. No historical novelty or comprehensive exclusion of older closure results is established. Checks and exact results are in `check_graph_example.py` and `GRAPH_EXAMPLE_RESULT.json`.

## Final release supplements reviewed

The final `SHORT_RANGE_SUPPLEMENT.md` and complete certificate were accepted. Independent reconstruction using the cubic derivative resultant with its negative discriminant sign matches every sector coefficient (23/22 terms, constant469), as well as the quadratic discriminant and three base intervals. The m=1,2 claims are now directly supported without importing the join-preservation theorem. The corrected displayed F2 coefficients match the defining recurrence.

`GRAPH_BRIDGE.md` was checked in full. Endpoint path-coloring formulas, reflected normalization, rising-factorial cancellations, Bell recurrence, and maximum clique sizes agree. The m=1 triangle case is correctly handled separately with clique size r+2 and linear maximal quotient; for m≥2 the clique size is r+1. The graph family follows, with no historical-priority assertion.

The m=4 reduction was independently verified as a formal polynomial identity in arbitrary moment variables, not only sampled fixtures. With δs=s−v, δv=2(v−w), δw=3(w−x), δu=u(1−u), conjugating L by p gives δ+s+1. This reconstructs the displayed A, the corrected derivative D0 with −2C(v−w), and the off-root identity F/p−N=(s+g)A for an arbitrary weighted single active coordinate g=κ(1−u); linearity supplies every sum. Script: `check_m4_formal.py`. This establishes the reduction only. The required general sign inequality and all-degree m≥4 closure remain unresolved.
