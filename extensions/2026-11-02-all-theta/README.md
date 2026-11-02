# All-length theta edge-quotient certificates

For Θ(a,b,c), a,b,c≥2, this package supports the proof that the ordinary Bell transform of the unsigned chromatic edge quotient PΘ/[x(x+1)] has only negative real roots. Read the [self-contained manuscript](MANUSCRIPT.md) or its [typeset PDF](manuscript.pdf) for the analytic tail and the original normalization. This is a theta-family theorem, not general BRW clique-overlap closure. No historical novelty claim is made.

## Replay

Check the release file hashes first with `sha256sum -c SHA256SUMS` (or an equivalent SHA256 utility).

Use Python 3.10 or later, with assertions enabled:

```
python verify_all.py
python verify_all.py --finite
python -m pip install -r requirements.txt
python verify_all.py --bernstein
```

Default/`--finite` runs **two independent integer-only auditors** over all 2,460 residual certificates. They reconstruct target polynomials by different formulas and verify exact negative rational sign brackets or exact root points, factor products, and exhaustive coverage. No FLINT or numerical roots are needed. The full sorted finite domain contains 52,394 triples: 49,934 satisfy the analytic radius test and 2,460 require certificates.

`--bernstein` regenerates both exact rational Bernstein certificates in a temporary directory and compares all mathematical data. It requires SymPy 1.14.0. Both modes can be selected together. The package is never edited by the runner; output is JSON on standard output. All subprocesses use `-E`. Optimized execution (`-O`, `-OO`, or a nonempty `PYTHONOPTIMIZE`) is rejected by the parent runner; each Python program also explicitly rejects disabled assertions.

## Files and integrity

- `finite_certificates.zip`: deterministic flat archive of 2,460 JSON certificates.
- `certificate_manifest.json`: explicit allowed names, sizes, SHA256 hashes, and archive hash. Extraction rejects unexpected, duplicate, absolute/traversal, directory, and symlink entries before writing; hashes are checked.
- `audit_finite_certificates.py`: geometric-sum/binomial/Stirling coefficient reconstruction.
- `check_certificates.py`: independent direct binomial/Stirling reconstruction.
- `finite_theta_verify.py`: preserved generator source, required to bind existing certificate source hashes. Regenerating roots additionally requires python-flint 0.9.0; it is **not** invoked by replay.
- `effective_*_certificate.py`, `effective_*_certificate.json`: exact analytic repair certificates.
- `source_delta.json`: the mixed/quartic source differs from its original only by an explicit assertion-enabled guard; the original and packaged hashes are recorded. Regeneration accounts for this hash-only output difference.
- `receipts/`: clean replay outputs, not substitutes for running the checks.

The archive/manifest establish integrity relative to this package, not external authorship or a cryptographic signature. The mathematical validity comes from the exact replays plus the manuscript's analytic argument. An inaccessible recent Mu–Shen–Xu article remains a literature-scope uncertainty; no claim about its normalization or overlap is made.

## Reproduce optimization rejection

The following must exit nonzero before starting a replay (the environment syntax shown is for POSIX shells):

```
python -O verify_all.py
python -OO verify_all.py
PYTHONOPTIMIZE=1 python verify_all.py
```

## Primary references and bounded literature note

- F. Brenti, G. F. Royle, D. G. Wagner, *Location of Zeros of Chromatic and Related Polynomials of Graphs*, Canadian Journal of Mathematics **46** (1994), 55–80: https://doi.org/10.4153/CJM-1994-002-3 . This supplies the ordinary τ normalization and Bell-product preservation used in the manuscript.
- Lili Mu, Qi Shen, Xinyao Xu, *On the Real-rootedness, invariance, and root bounds of τ-polynomials*, Discrete Mathematics, Algorithms and Applications, article 2550185: https://doi.org/10.1142/S179383092550185X . Publisher-deposited metadata reports online publication 9 January 2026. Full text was not obtained during this bounded check; formula-stripped metadata does not establish its exact invariant, hypotheses, or overlap with this result.

## Optional independent root-certificate regeneration

This is not needed for replay. Use a new output directory outside this package:

```
python -m pip install python-flint==0.9.0
python finite_theta_verify.py --out /path/to/new-directory
python audit_finite_certificates.py --certificates /path/to/new-directory
python check_certificates.py /path/to/new-directory --complete
```

Replace the illustrative path with a writable new directory. FLINT proposes intervals, but acceptance uses exact rational signs, exact zeros, factor identities, and degree counts. Newly generated interval bytes can differ across software versions or runs; mathematical validity is established by the two exact auditors, not by matching the supplied archive bytes. Keep the generator source unchanged so its identity remains consistent with its output receipts. The optional generator defaults to all 2,460 residual cases; its `--limit` option is only for partial experiments and cannot establish full coverage.
