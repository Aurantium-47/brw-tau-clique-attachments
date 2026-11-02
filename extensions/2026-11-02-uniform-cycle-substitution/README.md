# Uniform cycle substitution operator theorem

The proof was developed and separately reviewed using AI. This is not human peer review or proof-assistant certification.

Related-literature boundary: the exact normalization and overlap with Mu–Shen–Xu, DOI [10.1142/S179383092550185X](https://doi.org/10.1142/S179383092550185X), remain unverified because its full text was not obtained. That paper is not used as a proof dependency here, and no claim of non-overlap is made.

`RESEARCH_NOTE.md` contains a self-contained proof that every operator

A1 = (1 + D)^2,   A_(m+1) = (zD + z + 1) A_m + D(1 + D)

preserves polynomials whose zeros are all real and nonpositive. It derives the corresponding substitution into every cycle C_(m+2), with any ordinary tau-real graph as input, and the resulting universal edge-attachment property.

Consecutive outputs strictly interlace for simple strictly negative inputs and weakly interlace for nonzero boundary inputs.

The proof uses root-map monotonicity and an invariant for symmetric arrowhead matrices. Separate sections give the independently checked higher-shift seed extension and the standard, explicitly bounded universal-clique lift. It is not a finite-input test or a claim about arbitrary larger-clique attachment, the full BRW conjecture, or historical priority.

## Verification

Tested with Python 3.12.14 and SymPy 1.14.0:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python verify.py
```

On Windows use `.venv\Scripts\python.exe`. With dependencies already installed, `python verify.py` works from any directory and needs no network. Do not enable `-O`, `-OO`, or `PYTHONOPTIMIZE`.

The verifier checks package hashes, reruns both exact symbolic checkers in a temporary directory, and verifies their optimization guards. The checkers establish the displayed rational identities and the one-root matrix case. **They are supporting checks, not substitutes for the universal written proof.** The separate mathematical transcription review is summarized in `MATHEMATICAL_REVIEW.md`.

## Files and reproducibility

- `RESEARCH_NOTE.md`: editable mathematical source.
- `RESEARCH_NOTE.pdf`: readable rendering of that source.
- `check_invariant_algebra.py` and `check_independent.py`: exact supporting checks.
- `verify.py`: portable guarded replay and integrity verification.
- `build_pdf.py`: optional PDF rebuild using Pandoc and XeLaTeX; neither is needed to verify the algebra.
- `PROVENANCE.json`: hashes of preserved pre-packaging sources.
- `MANIFEST.json`: SHA256 hashes of packaged source, review, and output files.

Hashes detect changes but are not digital signatures. Rebuilding the PDF can change metadata and therefore its hash. The delivered PDF was rendered and checked for readability. The verifier leaves the package unchanged.

## Earlier alternative method

The earlier unpublished star-core work is preserved separately as an alternative-method record. Its former statement that all-m operator preservation was unresolved is superseded by this arrowhead proof. Uniform feasibility of that particular star-core matching ansatz remains a different, unresolved question. No public artifact is changed or published by this package.
