# Extension provenance and editorial changes

This is a separate extension, not a replacement or modification of the earlier 37-file release.

## Mathematical sources
The combined manuscript faithfully transcribes two separately reviewed ordinary proofs:
- Anchored incomparability all-clique theorem: source SHA-256 `bce2880386ad1b16695e0f467cffc3dd98551c9509339af40d23a27a62a41218`.
- General fixed-two-paths eventual theta theorem: source SHA-256 `8630ec42403361331f699b5ad5455262da8e53465974d9ff375c543943f6d8a4`.

The P4 blow-up theorem is a specialization of the anchored theorem and is not presented as a separate duplicate proof. The earlier Theta(2,2,m) argument is subsumed by the general fixed-a,b result and is not duplicated. The stronger all-length theta claim is not made.

## Editorial transformation
Shared notation defines falling and rising factorials, unsigned chromatic polynomials and the original BRW S/T reflection bridge once. The two proofs retain their exact hypotheses and quantifiers. ASCII mathematical formulas are typeset for readability; public references and proof-assistance limitations replace internal review narratives. Structural examples compare explicitly stated graph classes, not historical priority. A public literature note records only the sources actually inspected and the limits of that inspection.

## Exact computational evidence
Eight mathematical checker sources are retained byte-for-byte, with hashes in CHECKER_PROVENANCE.json. Eight original individual receipts are likewise preserved. The new runner is orchestration only: it checks source digests, requires assertions to be enabled, launches checker subprocesses with `-E` and no optimization flags to prevent inherited Python environment options from disabling their assertions, runs the checkers and writes an aggregate receipt. One unchanged checker prints its output path; the runner converts only the local package prefix to relative text before storing/printing the public receipt. No mathematical output is changed by this privacy normalization.

The general theta certificate verifies algebraic identities and negative sign intervals. It does not algorithmically verify the compactness/implicit-function theorem or provide an effective threshold. Exact finite graph comparisons similarly supplement rather than replace the anchored theorem's all-parameter proof.

## Exclusions and release boundaries
Private source-account identifiers, absolute execution paths, transfer/helper logs, raw internal review narratives, and coordination records are excluded. Superseded exploratory notes and unreviewed claims are not included. The optional root README patch is not part of this extension's allowlist and is not an executed repository change. No original release file or historical checksum manifest is edited.

The extension has its own allowlist, manifest, checksums and independent transcription/privacy audit. AI-assisted separate review is not human peer review or proof-assistant verification. No external writes were performed while preparing this package.

## Replay outcomes
All eight stages passed in the extension directory and in a separately relocated copy invoked from outside that directory; their combined receipts were byte-identical. The five regenerated individual receipt files matched the preserved originals byte-for-byte. Parent invocation under `-O`, `-OO`, or ordinary `PYTHONOPTIMIZE=1` was rejected before any checker ran. A full run with parent `-E` and inherited `PYTHONOPTIMIZE=1` also passed safely with checker subprocesses explicitly using `-E`; a separate assertion-probe audit confirmed child optimization remained zero. These are runner-hardening checks, not additional mathematical theorems.
