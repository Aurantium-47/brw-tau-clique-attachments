# Complete Bell clique quotients are closed under graph join

The proof is in [RESEARCH_NOTE.md](RESEARCH_NOTE.md); fresh independent AI review is in [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md).

For P_G(x)=(-1)^|V(G)| χ_G(-x), R_j(x)=x(x+1)…(x+j−1), and the Touchard Bell transform B, the property that every actual clique-size quotient B(P_G/R_j) has only real nonpositive zeros is closed under graph join. Nonnegative coefficients are included in the theorem's convention. A weighted matching realization proves a parameterized operator theorem for positive integer root parameters. Disjoint union and exact clique-sum corollaries follow from classical BRW Bell-product preservation.

**Scope:** This does not prove BRW 6.5 for arbitrary ordinary tau-real graphs. Partial-range seed theorems are not automatically full-clique seeds. Historical novelty is unassessed; the extension explicitly credits Kang–Liu–Sun–Zhang's matching mechanism and coefficient-substitution lemma and Heilmann–Lieb's weighted root theorem. Inaccessible Mu–Shen–Xu full-text overlap remains unresolved.

## Reproduce

Python 3.10+ and SymPy 1.14.0:

```sh
python -m pip install -r requirements.txt
python run_all.py
```

Tested on Python 3.12.14. Run from any directory using the path to `run_all.py`. It checks the SHA-256 manifest, runs all checkers under `python -O` in a temporary directory, and compares regenerated exact certificates with the committed JSON data. Guards use explicit exceptions, not removable assertions. No network is used by the checkers; installing dependencies may require network access.

- `verify.py`: 160 exact operator/bipartite-board identities, coefficient signs, and multiplicity-aware real-root counts.
- `review_check.py`: independently implemented 225 monomial identities and four factorized examples.
- `graph_check.py`: independent stable-partition enumeration for 44 small graph compositions, every quotient from j=0 through clique number.
- `certificate.json`, `graph_certificate.json`: exact rational coefficient records.
- The three `*.log` files: retained successful individual runs.
- `MANIFEST.json`: SHA-256 checksums for every other release file.

Finite tests corroborate the proof; they are not premises. AI review is not human peer review or proof-assistant verification. The author/research attribution is AI-assisted; this package does not assert endorsements by cited authors.
