# PDF quality assurance record

Date: 2026-11-02 (UTC).

## Result

The final `manuscript.pdf` has 6 US Letter pages. Every page of the final build was rendered with Poppler at 120 dpi and visually inspected. No clipped text or equations, overlaps, missing glyphs, broken links in the references, or misplaced page numbers were found. The title block, hierarchy, equation spacing, and references are legible and consistent. All fonts are embedded. An independent text-coordinate check found no characters outside the page boundaries.

## Page review

- Page 1: title, abstract, notation, Bell convention, and exact BRW normalization relation checked.
- Page 2: edge realization, boundary case, chromatic expansion, and Bell identity checked.
- Page 3: generating-function continuation, inclusion-exclusion, and matching-root argument checked.
- Page 4: edge attachment and complete bounded-clique theorem and proof checked.
- Page 5: even-cycle-complement corollary, verification counts, and scope discussion checked.
- Page 6: AI-review disclosure and both bibliography entries checked.

## Content and reproducibility checks

- The edge construction is exactly the complete bipartite graph with part sizes n - 2 and n - 1, with the embedded complement edges deleted.
- The larger-clique result is explicitly restricted to 1 <= j <= t for the chosen complement bipartition with side sizes s <= t. The general matching-polynomial identity has sign (-1)^(n - j) and factor y^(j - 1).
- The n = 2 edge case is stated separately. The finite checks are identified as 165 cases (147 atlas and 18 structured) and 663 bounded-j checks; they support, rather than prove, the infinite-family result.
- The manuscript uses the portable command `python verify.py` and contains no private workspace paths or agent identifiers.
- AI-assisted proof and independent AI review are disclosed, without representing either as human peer review or proof-assistant certification. Historical novelty remains unknown and Mu-Shen-Xu overlap remains unassessed.

The editable Markdown was compiled with Pandoc 3.1.11.1 and XeLaTeX using Latin Modern text and math fonts. In a normal Pandoc/XeLaTeX installation, rebuild from the package directory with:

```sh
pandoc manuscript.md --from markdown --pdf-engine=xelatex -o manuscript.pdf
```

Rendered PNGs and build intermediates were removed from the distributable package. This record concerns document presentation and content consistency; it is not additional mathematical certification.

## Final file integrity

- `manuscript.md` SHA-256: `c63d07448a4e5796ac75029452233ec30413698f772f6034e5e8bc2aef151912`
- `manuscript.pdf` SHA-256: `a7f2787699d8c42ff5a3132307a0b18e04d77e47463b1c7b53e9b8252281e033`
