# Odd-cycle-complement quotient theorem

Main result: for G = complement(C_(2m+1)), m>=2, every Bell quotient
B(P_G/R_j), 1<=j<=m+1, has only real nonpositive zeros. The proof replaces
the odd cycle with a matching-equivalent bipartite fork tree. A bounded
disjoint-component extension is also proved.

Read `RESEARCH_NOTE.md` for the self-contained argument and exact scope;
`INDEPENDENT_REVIEW.md` records an independent AI audit, not human peer
review or formal proof verification. Historical novelty is not asserted.

## Reproduce

Python 3, then:

```
python -m pip install -r requirements.txt
python verify.py
python check_components.py
```

The first script reproduces 88 exact checks; the second replays those and
adds 39 component checks. JSON certificates are regenerated deterministically.
Do not use Python `-O`: both entrypoints explicitly reject disabled assertions.
The proof is infinite-family and does not depend on these finite checks.

`MANIFEST.sha256` records package file hashes (excluding itself).
No solution of unrestricted BRW edge closure or graph counterexample is claimed.
