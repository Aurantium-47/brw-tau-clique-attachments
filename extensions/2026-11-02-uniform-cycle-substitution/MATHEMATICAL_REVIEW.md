# Mathematical review

The proof was developed and separately reviewed using AI. This is not human peer review or proof-assistant certification.

**Verdict: PASS.** No mathematical gap or transcription error was found in the reviewed version of `RESEARCH_NOTE.md`. The final GitHub-compatible math delimiter conversion was checked by reversing it and recovering the exact prior reviewed source hash after removal of the two added scope sentences; those sentences were also checked for consistency.

Reviewed note SHA256:

`2d170166296e7926d6ea38c4bb022129600cd467806785baac4f9ab46bfa783b`

## Scope of the review

The review independently checked the logical steps and displayed formulas establishing the uniform operator theorem, its higher-shift extension, and the stated graph consequences.

- **Initial residues.** The ordered-root map for `1 + D` has a strictly positive Jacobian. The scaling identity and implicit root derivative are consistent, including degree one. They give the strict estimate `0 < κ_i < 1/2`, the partial-fraction identity for `w`, and the initial potential bound.
- **Arrowhead step.** The characteristic-polynomial quotient, positive-definiteness Schur complement, simplicity argument, eigenvector formula, and identification of new residues as diagonal entries are correct. The generalized determinant has the displayed sign and power of the eigenvalue parameter. The rank-two calculation applies also to the two-dimensional matrix arising from degree one.
- **Invariant.** The eigenvalue endpoint inequalities, scalar Jensen argument, spectral-potential formula, monotonicity in `V`, and exact boundary identity propagate `0 < w ≤ 1` and `V ≤ 2 − w`. Residue positivity is not incorrectly assumed after the initial step.
- **Iteration and boundary cases.** The forcing polynomial stays fixed and below the current degree. Constants are handled without invoking the nonzero rank-two argument. Fixed-degree monic limits justify repeated roots and roots at zero without degree loss. Scaling and the zero input are covered.
- **Consecutive interlacing.** The added strict alternating-root assertion follows from the secular quotient and its complementary-interval roots. Simultaneous fixed-degree limits of consecutive outputs give weak interlacing for nonzero boundary inputs; constants and the vacuous degree-zero pair are handled separately. The boundary statement explicitly defines the input degree and lists roots with multiplicity. The additions were checked against the prior reviewed version by exact source reconstruction.
- **Higher-shift extension.** The `k`-fold root map and factor `t^(n−k)` are valid for every integer `k ≥ 2`, including `n < k`. The resulting residue bound places the seed inside the same invariant.
- **Graph bridge.** Endpoint coloring, vertex-count signs, unsigned chromatic normalization, Bell-shift identities, and the operator recurrence agree. The edge, vertex, and empty-intersection consequences follow from the stated Bell-product theorem.
- **Clique lift.** The join identity and rising-factorial quotients are correct for `0 ≤ j ≤ s + 2`. The triangle-free specialization covers all cliques of the lifted graph. The note does not promote this restricted consequence to unrestricted larger-clique attachment.

Both accompanying exact algebra programs, `check_invariant_algebra.py` and `check_independent.py`, were rerun successfully. Their finite symbolic checks support the algebraic identities; the root-map, matrix, and limiting arguments supply the uniform mathematical proof.

This is a mathematical review, not a proof-assistant certification. It verifies the stated operator and graph results, not historical priority or the full unrestricted BRW clique-attachment conjecture. The separate star-core realization question remains distinct from the now-proved operator preservation theorem.

**Editorial transparency check.** The AI-development and review disclosure and the unresolved related-literature boundary were checked. Removing only the two added note paragraphs exactly recovers the previously reviewed mathematical source. These additions change no mathematical statement or proof and make no human-peer-review, formal-certification, priority, or non-overlap claim.
