# Publication audit

## Result

PASS for mathematical transcription, stated scope, checker provenance and publication privacy of the files identified below. This is a separate AI-assisted audit, not human peer review, a formal proof certificate, or a novelty determination.

## Scope and proof interfaces

The manuscript faithfully retains three results: a sufficient long-minimum condition for parallel paths; the all-length family Θ(2,2,2,m), m ≥ 2; and five-cycle vertex substitution with arbitrary ordinary τ-real input, including the empty input. The full fixed-source arrowhead invariant, its exact finite base, and the weighted matching argument are retained. The matching theorem is used for general graphs, without a bipartiteness assumption.

The parallel-path families are triangle-free, so the stated attachment conclusion covers every possible complete intersection. Five-cycle substitution can create larger cliques: its attachment conclusion is restricted to intersections of size at most two. No general larger-cycle substitution theorem, general BRW resolution, or priority claim is asserted. The exact scope of the cited Mu–Shen–Xu work is not assumed. The unresolved operator recurrence is explicitly separated from the proved results.

## Computational provenance and safety

All seven certificate/result JSON files were compared with their source versions and are byte-identical. Of seven mathematical checker files, two are byte-identical and five differ only by an explicit assertion-enabling guard, as recorded in `source_deltas.json`; no mathematical code change was found. The runner checks source hashes, uses temporary working directories and launches children with `-E`. It rejects optimized execution. Recorded default, Bernstein and relocation replays passed; recorded integrity tests reject modified source hashes or mathematical result data. These computations support the stated exact identities, finite base and Bernstein inequalities; they are not finite-sample substitutes for the analytic proofs.

## Reader files and privacy

The Markdown was compared with the reviewed proof sources. The final PDF has 15 pages. Its text, metadata, link actions and attachment structure were independently inspected: no private filesystem locations, internal review narratives, personal author metadata, embedded attachments or executable actions were found. Links target public references or accompanying files. The TeX is self-contained and has a blank author field. Separate rendering QA records all-page visual inspection, 526 preserved mathematical expressions, 41 equation tags and embedded fonts; this audit does not claim a second all-page visual inspection.

## Frozen content hashes

| File | SHA-256 |
|---|---|
| `MANUSCRIPT.md` | `20c74bf7d627c4b102a24a1a0fa7534a50ca40b7c5eb8e7f9cece0a6c3fd1101` |
| `MANUSCRIPT.tex` | `afcb5c56dfab3e0d7512488d344ba61769b48a100fafec74672662404e9ca833` |
| `manuscript.pdf` | `134a7511aa7fa8e7080689caef03a17bda01850fc661678d6a00b0a93254a924` |
| `verify_all.py` | `a00b0ca8a2523b91c6688258d9452ad9462f547b68f09a99e4d92937f373d226` |
| `source_deltas.json` | `d97d57ced2a9f7f161a745938a2fdb226e651e457b07ae74d4dee99abfd6a605` |
