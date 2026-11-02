# Structural and eventual theta extensions

Read [the manuscript](manuscript.md) or [its PDF](manuscript.pdf).

## Results and exact limits
1. **Anchored incomparability graphs.** Suppose a finite graph is an incomparability graph, has a partition into k nonempty independent classes, and has one chosen vertex in each class adjacent to every vertex outside that class. Every Bell chromatic quotient B(P/R_j), 0 <= j <= k, has only nonpositive real zeros. Thus ordinary attachment along any clique to any tau-real graph preserves tau-reality. A merely dominating clique is not the hypothesis.
2. **Eventual theta attachment.** For each fixed a,b >= 2, there exists M(a,b) such that Theta(a,b,m) has a real-rooted edge Bell quotient for every m >= M(a,b). Its ordinary edge attachment to any tau-real graph therefore preserves tau-reality. No effective threshold, uniform threshold in a,b, or all-length theorem is claimed.

The anchored theorem includes connected Ferrers/chain graphs with an edge, independent P4 blow-ups (complete bipartite graphs minus a rectangular block), and K_{a,b} minus two disjoint edges for a,b >= 3. These are sufficient classes, not a solution of the general BRW Conjecture 6.5. Empty/vertex intersection closure was already proved in BRW Proposition 5.12. Conjecture 6.6 is the different graph-join assertion.

The proofs and separate checks were AI-assisted. No human-peer-review, proof-assistant verification, historical-priority, or comprehensive literature-review claim is made. A deeper expert literature comparison remains appropriate.

## Exact reproduction
Use Python 3.10 or newer and SymPy 1.14.0:

```sh
python3 -m pip install -r requirements.txt
python3 verify_all.py
```

Assertions must remain enabled: do not use `-O`, `-OO`, or `PYTHONOPTIMIZE`. The runner fails immediately under optimized Python. Checker subprocesses are launched with `-E` and no optimization flags, so inherited Python environment options cannot disable their assertions. It validates checker digests before and after running eight unchanged mathematical checker sources, and writes a fresh VERIFICATION_RECEIPT.json. File locations are relative to the runner, so the directory can be relocated. Absolute execution paths printed by a checker are normalized to package-relative paths in the public combined receipt; mathematical outputs are unchanged.

Checks include the poset principal-minor identity, actual graph chromatic polynomials versus explicit matching polynomials, odd-k signs, P4 weighted diagonal examples, exact parabolic-region separation, symbolic all-length theta identities and four exact negative sign intervals. The theta eventuality proof is analytic (compactness, local root persistence, and a finite-residue implicit-function argument). Finite computations neither prove that eventuality nor yield its threshold.

The original exact individual receipts are in certificates/. Regenerated receipts may also appear in checkers/. CHECKER_PROVENANCE.json gives exact source hashes. Check SHA256SUMS before running; replay deliberately refreshes the combined receipt and its environment metadata can differ on another system.

## Release separation
This extension is self-contained and has its own manifest. The original root manuscript, checkers and 37-file release are not modified. The full conjecture remains unresolved by these results. PUBLIC_SOURCES.md and DELTA_REPORT.md state references, scope and editorial changes; PUBLIC_AUDIT.md records the separate transcription/privacy audit.
