# Co-bipartite matching-quotient extension

This package is an extension within the ordinary Brenti–Royle–Wagner graph-polynomial project, not a resolution of unrestricted clique or edge amalgamation.

## Result

For every edge-containing co-bipartite graph G, the Bell transform of P_G/[x(x+1)] has only real nonpositive roots. It is exactly the reversed matching polynomial of an explicit bipartite graph. Thus G is a universal ordinary τ-real edge attachment. The manuscript also proves a carefully bounded larger-clique variant.

The proof and review were AI-assisted. They are not human peer review or proof-assistant certification. Historical novelty is not claimed; overlap with Mu–Shen–Xu remains unassessed.

## Files

- `manuscript.md`, `manuscript.pdf`: editable and rendered theorem/proof.
- `verify.py`: standalone exact replay, with no local-project imports.
- `certificate.json`: 165 edge-quotient cases and 663 bounded-j checks.
- `requirements.txt`: pinned Python dependencies.
- `MATHEMATICAL_REVIEW.md`: independent mathematical review scope.
- `PDF_QA.md`: rendered-document QA record.

## Replay

Use Python 3.12 or a compatible modern Python environment:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python verify.py
```

Expected output: `PASS 165 exact identities and exact RR checks`. The program also asserts exact agreement with all 663 bounded-j records. All root tests use rational isolation rather than floating approximations. The checks support the identities; the general theorem is proved analytically, not inferred from the finite sample.

The checker does not modify the retained certificate. Any failed assertion is a replay failure and must be investigated.
