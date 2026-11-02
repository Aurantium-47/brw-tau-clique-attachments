# Completed bounded research pass

Read `RESEARCH_NOTE.md` for the precise theorem and important older-criterion caveats. Independent proof review: `audit/INDEPENDENT_AUDIT.md`.

Verified: 122 graphs / 585 exact quotient checks; 452 independent direct-board checks. Run `python verify.py` and `python check_region.py` after installing `requirements.txt`.

Result: full-clique matching realizations when each bipartite complement component has matching number at most two. Double-star complements close the literal board-size gap but already have real chromatic roots; the worked disjoint example is also covered by BRW 5.13. No historical novelty, general co-bipartite theorem, or general BRW solution is claimed. No external state changed.

Final scope comparison: the n=15 example with complement D(2,2)⊔D(1,1)⊔D(1,2) has a certified nonreal chromatic zero outside the closed BRW Proposition 5.13 region. See §6 and `outside_region_certificate.json`. This establishes nonimplication of that particular sufficient hypothesis, not exclusion of all older results or historical novelty.

Reproduce all checks:

```sh
python -m pip install -r requirements.txt
python verify.py
python check_region.py
python audit/check_independent.py
sha256sum -c SHA256SUMS
```

The first two checkers deliberately reject `python -O`. The independent checker uses explicit, non-disableable `require` checks and passes identically under `python -O`. Logs record both behaviors. Manifest covers every included file except itself. Source attribution is self-contained and links to immutable published provenance; no sibling workspace files are required.
