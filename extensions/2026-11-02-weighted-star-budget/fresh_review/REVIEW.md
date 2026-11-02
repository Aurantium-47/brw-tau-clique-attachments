# Fresh independent mathematical and computational review

2026-11-02. Separate AI review; not human peer review or proof-assistant verification. No external writes.

## Verdict

The theorem and proof in `independent_audit/AUDIT.md` are mathematically sound, conditional only on the stated classical weighted Heilmann–Lieb real-rootedness theorem and Bell-product preservation theorem. In particular:

- Factoring the matching generating polynomial gives strictly positive masses λ_i, with sum e. Their multiplicities cause no difficulty.
- The ceiling-budget proof correctly uses the **integer** total e; its nonintegral fractional-part sum is a positive integer. It yields C<=e+ν−1, including ν=1 and the all-integral case.
- Splitting each mass across a disjoint star produces weights in (0,1] and exactly preserves all matching coefficients.
- N>=n>=2ν is automatic and need not be an additional padding hypothesis. N>=C+1 is the sharper spectral hypothesis, and N>=e+ν implies it.
- Weighted inclusion–exclusion has the correct reversed-polynomial exponent: selecting k forbidden edges leaves a−k available rows and produces degree a−k, with no extra factor of z.
- The Bell identity has matching board dimensions a−k=N−j−k and b−k=N−1−k. The original order N, not the weighted surrogate order, is used consistently.
- The matching polynomial conversion μ_J(y)=(-1)^a y^(j−1)M_J(-y²) has the correct sign and power, including j=1 and zero roots.
- Triangle-freeness gives χ(G)=N−ν, while the elementary matching bound gives ω(G)<=N−ν. Thus all actual cliques are covered; equality of clique and chromatic numbers is not assumed.
- The e=0 complete-graph exception is correctly separated.

The rational diagnostic inputs are accurately distinguished from actual unweighted graphs. The rational-root theorem indeed forces every rational λ_i of an unweighted graph to be an integer.

## Independent computations

1. Replayed the original 19-check weighted-board verifier and obtained byte-identical JSON (`original_replay.json`). The original script uses bare assertions; it should be regarded as an ordinary-mode historical verifier, not optimization-safe. A guarded release checker or explicit rejection of optimized execution is needed in the final package.
2. Wrote `check_fresh.py` independently, without importing or reading the original verifier's computed data. It enumerates every labeled triangle-free graph with at least one edge on 1 through 6 vertices, computes matching counts by a cached vertex-deletion recurrence, pads to N=max(n,e+ν), and constructs the maximal initial-factor quotient at j=N−ν directly from matching counts and Stirling numbers. There are **6,222 graph checks**, reducing to **46 distinct exact quotient checks**. Every quotient has nonnegative coefficients and the expected number of real nonpositive roots, checked by exact rational root isolation.
3. Repeated that independent checker under `python -O`; outputs were byte-identical. It uses explicit runtime checks, not assertions. It needs only SymPy plus the Python standard library; NetworkX is not used or required.

This sweep checks only the maximal j for its graph inputs. It is not an exhaustive weighted-board verification or a replacement for the general proof. The 19 original checks independently cover all claimed j for their six inputs.

## Exact BRW-region witness

Reviewed and replayed `region/check_region.py` under `python -O`, obtaining byte-identical `region_replay.json`. For H=3 disjoint K1,3, its matching counts are (1,9,27,27), N=12=e+ν, and its complement chromatic polynomial after removing (x)_9 has residual

    f(x)=x³−21x²+155x−396.

The code reconstructs this from the matching product rather than taking f as unexplained input. Exact complex root counting gives one upper-half-plane root in

    359/50 < Re(x) < 719/100,
    71/25 < Im(x) < 57/20,

and its conjugate in the reflected rectangle. Boundary root exclusion is verified using exact polynomial gcds. Throughout the upper rectangle,

    (Im x)²−Re x−1/4 > (71/25)²−719/100−1/4 = 391/625 > 0.

Thus these roots are strictly outside even the closed parabola (Im x)²<=Re x+1/4 used for comparison with the direct BRW 5.13 region hypothesis. This certifies that the new budget does **not automatically imply that direct hypothesis**. It does not exclude all prior methods: complements of star forests are cographs and already belong to the previous cograph closure family. No novelty or new graph-scope inference follows from this witness.

The initial audit's statement that comparison with BRW's direct root condition remained unknown is now superseded by this certificate. Historical earliest-priority and broader prior-theorem overlap remain unassessed.

## Final standalone-note check

Inspected the final root-level `RESEARCH_NOTE.md` and `verify_all.py` before freeze. The standalone note correctly promotes the spectral hypothesis into the theorem, proves the Bell rising-factorial identity by formal exponential generating functions with the correct factorial factors, states the precise clique-sum convention, and records the exact region separation without overstating graph scope or novelty. No mathematical correction is needed. The aggregate runner compares regenerated certificates, checks pinned SymPy/mpmath versions, tests optimized execution of the explicit-runtime-check scripts, and requires the guarded release verifier to reject `-O`. Its manifest check verifies listed hashes when a manifest is present; the frozen package must therefore include the generated manifest. Subject to the parent's final aggregate replay and manifest generation, these inspected files are freeze-ready.
