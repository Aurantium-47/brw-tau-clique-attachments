# Weighted-star bound: checked local research package

Read **RESEARCH_NOTE.md** for the standalone theorem and proof.

For a triangle-free graph H with n vertices, e edges and matching number ν, adding
`t >= max(0,e+ν−n)` isolated vertices to H suffices to make its complement
universally attachable along every clique to any ordinary τ-real graph.
The sharper spectral budget is `t >= max(0,1+Σceil(λ_i)−n)`, where
`m_H(u)=∏(1+λ_i u)`. Every initial-factor Bell quotient through `j=N−ν`
is explicitly a reversed nonnegative weighted matching polynomial.

This is a sufficient budget, not an optimality or historical-novelty claim.
General eventual closure is already implied by BRW Proposition 5.13. An exact
12-vertex example shows the displayed budget does not imply that proposition's
direct chromatic-root-region hypothesis; the example itself is an already-known
cograph type. No unrestricted BRW conjecture is resolved.

## Reproduce

Tested with Python 3.12.14. Dependencies are pinned in `requirements.txt`.

```sh
python -m pip install -r requirements.txt
python verify_all.py
```

The suite is read-only and uses paths relative to its own location. It checks:

- 19 exact weighted-board/Bell identities and root counts across six inputs;
  four are actual unweighted graph cases and two are rational-weight diagnostics.
- A separately written exhaustive verifier for all 6,222 labeled triangle-free
  graphs with an edge through six vertices: 46 distinct maximal quotient checks.
- An exact rational-rectangle certificate outside BRW's direct root region.
- Safe optimization behavior: the assertion-based release checker explicitly
  refuses `python -O`; the two independently written checkers retain their
  explicit checks under `-O` and return matching results.
- All hashes listed in `MANIFEST.sha256` when present. The manifest excludes
  itself and is covered by the archive hash supplied separately.

Finite checks are support, not the proof. Reviews are independent AI reviews,
not human peer review or proof-assistant certification.

## Files and historical records

- `RESEARCH_NOTE.md`: standalone proof, examples, source attribution, limits.
- `checkers/`: guarded release weighted-board verifier and certificate.
- `fresh_review/`: independent review, enumeration checker and replay records.
- `region/`: exact outside-region witness and certificate.
- `independent_audit/`: preserved initial audit and original checker. The original
  checker contains bare assertions and must not be run with `-O`; use the release
  checker instead. Its old statement that region comparison was unknown is
  explicitly superseded by `region/` and the final research note.
- `verify_all.py`, `requirements.txt`, `verification.log`, `MANIFEST.sha256`:
  portable replay and integrity records.

No remote publication, repository update, or account change was performed.
