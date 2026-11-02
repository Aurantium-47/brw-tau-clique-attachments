# Reader-package delta and privacy policy

This is a separate reader edition. The two sealed source artifacts are unchanged. Their immutable SHA-256 digests are recorded in CHECKER_PROVENANCE.json, without account identifiers or machine locations.

## Preserved mathematics and code
- The manuscript combines the complete missing-edge theorem, its detailed matching-kernel derivation, and the structural corollary. It is an editorial transcription, not an asserted mathematical strengthening.
- Nine mathematical checker programs are copied byte-for-byte. Only their directory location changes. CHECKER_PROVENANCE.json maps every retained checker to its original digest.
- Nine original exact JSON receipts are retained byte-for-byte under certificates/. Fresh replay outputs are separate; regenerated individual receipts agree byte-for-byte with their original counterparts.
- The replacement verify_all.py is an orchestration-only runner: it validates checker digests, runs each script from a relocatable directory, and records outputs. It does not alter the mathematical computations.

## Excluded from this edition
- Private source-account identifiers, transfer metadata, absolute machine paths, helper scripts and transfer logs.
- Raw internal mathematical-review narratives and coordination records. Their checker code and exact receipts remain available.
- Superseded exploratory assessments, abandoned matching templates, unrelated theta experiments and numerical searches.
- The separate weighted-subfamily proof exposition, which is redundant to the accepted all-parameter result. Its exact operator/matching checks are retained as supplementary diagnostics.
- Old source-bundle manifests and seals that reference excluded private or internal files. This reader edition has its own exact allowlist and hashes.

## New editorial material
README.md is a short verification guide; PUBLIC_SOURCES.md lists public mathematical sources and a bounded literature caveat. The manuscript uses “main proof” rather than internal coordination terminology, and mathematical references point to the reader package rather than omitted review narratives. Mathematical content is subject to a separate transcription audit. AI-assisted checking is disclosed without implying human peer review or proof-assistant certification.

## Scope retained
The full ordinary tau clique-overlap conjecture is not claimed. The complete-bipartite-minus-edge family has all possible clique attachments; the general structural corollary assumes first-quotient real-rootedness and establishes attachment only through cliques of size at most two. No global novelty or historical-priority claim is made.

## Portable replay outcome
All nine stages passed in the reader directory and in a separately relocated copy invoked from outside that directory. The two combined receipts were byte-identical (Python 3.12.14, SymPy 1.14.0). Original source ZIP hashes were checked again and were unchanged.

## Manuscript transcription map
- Main theorem source sections 1, 2, 4, 5 map to manuscript sections 1, 2, 4, 5 respectively. Section 3 combines the main generating-function proof with the detailed finite-core moment derivation, making it self-contained without a companion file. The structural corollary becomes section 6; scope observations become section 7.
- ASCII formulas are typeset in LaTeX. The operators B, C and J are styled as calligraphic symbols; the kernel polynomial is styled as calligraphic P; the baseline formal moment is named B_0. The differential operator is written with d/dz, distinct from the formal denominator D=1-uv. Formula content and parameter ranges are preserved.
- Definitions of falling factorial, R_0, empty clique intersection, graph join, and Stirling numbers are made explicit. Evaluation of J(P,Q) at x+1 is clarified.
- The detailed optional Jacobian/coefficient-change argument is omitted because the retained chromatic-to-matching generating-function proof establishes the required identity without it. The alternative Touchard matching illustration is omitted; its original recurrence/interlacing justification remains.
- The explicit cograph/cycle/Theta(2,2,3) seed-class comparison is retained as a structural observation, without references to private work history. The minimum-part-size-two boundary remains included in the theorem even though its earlier-project classification discussion is omitted.
- Public proposition citations, an abstract, an AI-assistance disclosure, and explicit limitations are added. These edits do not assert mathematical strengthening or correction.

## Assertion-mode hardening
This derivative adds an explicit fail-fast `if not __debug__` guard to the runner and documents the requirement to keep Python assertions enabled. No mathematical checker source, manuscript byte, or original receipt is changed. The preceding reader ZIP is preserved unchanged. Normal replay passed all nine stages and produced a byte-identical receipt. Both `python -O verify_all.py` and `PYTHONOPTIMIZE=1 python verify_all.py` exited with status 1 before any checker ran, with the explicit assertions-enabled diagnostic.
