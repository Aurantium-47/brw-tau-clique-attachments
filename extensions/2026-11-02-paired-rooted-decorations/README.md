# Connected paired-decoration extension

Read `RESEARCH_NOTE.md` for two exact results:

1. An odd cycle with reflection-paired rooted connected bipartite
   decorations, and an undecorated axis vertex, has a bipartite matching
   surrogate on one extra vertex. Original-order board capacity gives
   real nonpositive Bell quotient zeros for `1 <= j <= (N+1)/2`, and
   universal ordinary-tau-real edge attachment of its complement.
2. No rooted bipartite matching surrogate exists for rooted C5, even
   permitting arbitrary isolated vertices. This obstructs unrestricted
   rooted substitution, not BRW real-rootedness.

Reproduce with Python 3 and SymPy:

    python verify.py

Expected final line:

    PASS ALL 15 97 obstruction candidates 24

`certificate.json` records integer matching counts, quotient coefficients,
exact nonpositive root counts, and every matching-equivalent candidate in
an exhaustive five-edge bipartite search through six vertices. The proof
shows why six nonisolated vertices suffice for that obstruction.

The verifier is self-contained except SymPy and the standard library.
It makes no network calls. The research is AI-assisted, historical novelty
and Mu–Shen–Xu overlap unassessed, and not a resolution of unrestricted BRW.

Independent review and standard-library-only checks are in `audit/`:

    python audit/verify_paired.py
    python audit/verify_c5_obstruction.py

These independently pass 9 constructed examples and 33 direct board/Bell
identities, and enumerate all 1,329 nonisolated five-edge bipartite labeled
candidates (24 matching-equivalent to C5, none rooted-equivalent).
Both independent verifiers reject optimized Python (`-O`) so assertions
cannot be silently skipped. The author verifier has the same guard.

## Attribution revision

This attributed edition preserves all proof arguments and all executable
and certificate bytes from the preceding frozen package. Classical
matching/chromatic and rectangular-board ingredients are credited to
Farrell–Whitehead (1992), and the exact bare cycle/fork identity to Ma–Li
(2016), Lemma 3.2(2). Read `LITERATURE_ATTRIBUTION.md` and
`CITATION_DELTA_REVIEW.md`. A prior exact paired-decoration equivalent was
not located in the scoped audit; this is not a proof of novelty.
