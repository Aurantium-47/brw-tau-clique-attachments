# Bell chromatic quotients and clique attachment

A reader/public-review package for the complete-bipartite-minus-one-edge theorem and its structural corollary. Read **manuscript.md** (editable mathematical source) or **manuscript.pdf**.

## Proven scope
For every a,b >= 2, H = K_{a,b} minus one edge has real-rooted Bell chromatic quotient B(P_H/[x(x+1)]), hence can be ordinarily attached along any clique to any tau-real graph. The structural corollary applies to a join with one distinguished edge removed, under stronger first-quotient real-rootedness assumptions on its two inputs. Its attachment conclusion is restricted to cliques of size at most two.

This is not a proof of general BRW Conjecture 6.5. Conjecture 6.6 concerns the different graph-join operation; the separate w-real clause of Conjecture 6.5 is not a theorem newly established by this package. No historical-priority, global-openness, human-peer-review, or formal-verification claim is made. Mathematical development and separate cross-checking were AI-assisted; expert review remains appropriate.

## Reproduction
Use Python 3.10 or newer and SymPy 1.14.0. Assertions must stay enabled: do not use `python -O`, `python -OO`, or set `PYTHONOPTIMIZE`. The runner rejects optimized Python before any checker runs. In an isolated environment:

```sh
python3 -m pip install -r requirements.txt
python3 verify_all.py
```

The runner locates files relative to its own location, so the directory can be relocated. It checks SHA-256 seals on the nine unchanged mathematical checker sources before and after running them. It writes VERIFICATION_RECEIPT.json; some checkers also regenerate their individual JSON outputs in checkers/. The package includes original exact receipts under certificates/ and a fresh combined replay receipt. None of these finite tests substitutes for the all-parameter proof. Check the release SHA256SUMS before running: the runner deliberately refreshes its receipt, whose environment metadata can differ on another system.

### What is checked
- Bivariate kernel: finite core rational identity, direct matching enumeration, and diagonal-edge lifting examples.
- Independently derived symbolic chromatic-to-matching generating function identity.
- Actual graph chromatic polynomials and exact root checks for specified finite instances.
- Supplementary weighted K_{3,b}-minus-edge operator and matching identities (a redundant restricted-family check, not needed for the general theorem).
- Exact chromatic-root rectangle and structural seed-class separation checks.
- Structural corollary: 28 nonzero signed-polynomial test pairs; the universal bridge is proved by bilinear basis extension in the manuscript.

CHECKER_PROVENANCE.json records unchanged source/receipt hashes. SHA256SUMS and MANIFEST.json cover this release. DELTA_REPORT.md explains editorial and privacy changes. PUBLIC_SOURCES.md gives public mathematical references.
