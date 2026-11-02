# Uniform eventual theta clique attachment

Read [the standalone addendum](addendum.md) or [its PDF](addendum.pdf).

**Theorem.** There exists one integer M such that every theta graph Theta(a,b,c), with a,b,c >= 2 and max(a,b,c) >= M, has a Bell edge quotient with only nonpositive real zeros. It therefore preserves tau-reality when ordinarily attached along an edge to any tau-real graph. The already-known empty/vertex intersection cases give all possible clique overlaps.

This strengthens the fixed-two-paths quantifier in the separate [structural/theta extension](../2026-11-02/README.md). The addendum is self-contained; the earlier manuscript is unchanged. The threshold is existential, not numerically specified. Finitely many triples remain outside the theorem; this is not an all-theta or general clique-overlap solution.

The proof uses uniform root-radius control, Vieta's formula, bounded Newton sums, angular distribution, and the local two-quadratic Bell-root repair. It is an ordinary AI-assisted proof, not human peer review or proof-assistant verification. No historical-priority claim is made.

## Reproduction and limits

```sh
python3 -m pip install -r requirements.txt
python3 verify_all.py
```

Use Python 3.10 or newer and SymPy 1.14.0. Assertions must remain enabled; do not use -O, -OO, or PYTHONOPTIMIZE. The runner rejects optimized Python and launches its unchanged algebraic checker with -E and no optimization flags. The checker verifies exact path identities, the repair quartic, four rational negative sign intervals and the parabola identity. These support the proof but do not compute M or verify its analytic limiting argument algorithmically.

CHECKER_PROVENANCE.json records unchanged source/receipt hashes; PUBLIC_AUDIT.md records the separate transcription/privacy audit. Verify SHA256SUMS before replay, which deliberately refreshes environment information in VERIFICATION_RECEIPT.json. This directory has its own manifest and does not modify the original release or the separate two-theorem extension.
