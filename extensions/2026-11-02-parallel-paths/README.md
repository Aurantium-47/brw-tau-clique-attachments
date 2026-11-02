# Three ordinary τ-realness extensions

This package contains a manuscript and exact reproducibility checks for three results. Write P_G(x)=(-1)^|V(G)|χ_G(-x) and B(x^j)=T_j(z), the ordinary Touchard/Bell transform. “Edge quotient” means B(P_G/[x(x+1)]).

1. **Many sufficiently long parallel paths.** For r≥2 internally disjoint paths of lengths l_i≥2 between common endpoints, the edge quotient is strictly negative-rooted if, with R=21/20,
   ∏_i (R^l_i+R)/(R^l_i−1)<R.
   A sufficient bound is every l_i≥L(r), where L(r) is the least L≥2 with 21^L≥(1+46r)20^L; for example L(4)=107.
2. **The entire four-path family Θ(2,2,2,m), m≥2.** Its edge quotient has simple strictly negative roots, proved by an exact arrowhead invariant and a certified finite base.
3. **One-vertex C5 substitution.** Replace one vertex of C5 by any ordinary τ-real graph F, joining every F vertex to the two former neighbors. The result has a real nonpositive-rooted edge quotient. The proof gives a weighted-matching differential operator preserving the whole nonpositive-root cone. Edgeless F on k vertices recovers Θ(2^k,3): k=0 is the ordinary length-three path, k=1 is C5, and k≥2 gives k+1 parallel paths.

Each edge-quotient conclusion permits attachment along any edge to any ordinary τ-real graph. The parallel-path graphs are triangle-free, so this covers their nontrivial complete intersections. C5 substitution with nonempty edges in F can create larger cliques: **no larger-clique attachment theorem is asserted** there.

These are not a solution of general BRW clique-overlap closure, nor of all generalized-theta lengths for arbitrary r. No historical novelty claim is made. No general larger-cycle substitution theorem is asserted.

## Exact replay

Use Python 3.10 or later, with assertions enabled:

```
python -m pip install -r requirements.txt
python verify_all.py
python verify_all.py --bernstein
python verify_all.py --all
```

Default replay runs five exact checks: the symbolic all-n weighted matching identity, an independently implemented core-state identity, actual small-graph C5 substitution identities, rational arrowhead base bounds, and independently reconstructed parallel-path identities/threshold examples. The larger `--bernstein` mode regenerates the cubic and mixed-quartic repair certificates (140 and 5,082 exact rational Bernstein coefficients). `--all` runs both groups.

The runner copies checker sources into a temporary directory, uses `-E` subprocesses, regenerates results, and compares exact mathematical data. It never edits the release. SymPy 1.14.0 is the sole nonstandard dependency; no FLINT, numerical roots, network access, private files, or earlier certificate archives are needed.

These checks support, but do not replace, the manuscript's proofs: sampled graph identities are interface checks, the finite arrowhead base needs its induction lemma, and threshold examples do not by themselves prove the all-r inequality. The matching core check is an identity in a formal indeterminate n, not finite extrapolation.

## Integrity and executable guards

`source_deltas.json` records every checker source identity. Missing assertion-enabled guards were added without changing mathematical content. Hash-bearing outputs account explicitly for these guard-only source differences. All mathematical data must match exactly; no coefficient fields are ignored. `receipts/` contains clean successful replay outputs, not independent evidence in place of rerunning the programs.

The following must exit nonzero before running checks (POSIX shell syntax for the last command):

```
python -O verify_all.py
python -OO verify_all.py
PYTHONOPTIMIZE=1 python verify_all.py
```

The parent runner rejects optimization flags and a nonempty optimization environment variable; every packaged checker explicitly rejects disabled assertions.

## References and review status

- F. Brenti, G. F. Royle, D. G. Wagner, *Location of Zeros of Chromatic and Related Polynomials of Graphs*, Canadian Journal of Mathematics 46 (1994), 55–80: https://doi.org/10.4153/CJM-1994-002-3 . Ordinary τ normalization, Bell-product preservation, and complete-cutset identities.
- O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190–232: https://doi.org/10.1007/BF01877590 . Nonnegative weighted matching real-rootedness for general graphs, not just bipartite graphs.
- Lili Mu, Qi Shen, Xinyao Xu, *On the Real-rootedness, invariance, and root bounds of τ-polynomials*, article 2550185: https://doi.org/10.1142/S179383092550185X . Publisher metadata reports online publication 9 January 2026. Its full text was not obtained in this bounded search, so its exact invariant and overlap remain unverified.

The work and independent implementation checks were developed with AI assistance. They are not external peer review or a personal attestation by a named human mathematician. Mathematical correctness should be assessed from the explicit proofs and reproducible exact computations.

## Manuscript and release checksums

Read [the manuscript](MANUSCRIPT.md) or [the PDF](manuscript.pdf). Once the release checksum file is present, verify all listed files from this directory:

```
sha256sum -c SHA256SUMS
```

Checksums establish integrity relative to the supplied checksum list, not external authorship or peer review.
