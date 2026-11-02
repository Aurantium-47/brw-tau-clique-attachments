# All-degree C6 full-clique-quotient closure

2026-11-02. AI-assisted mathematics, independently reviewed. No historical novelty claim.

## Proven scope
For every p(z)=product(z+a_i), a_i>=0, q(z)=sum_i a_i kappa_i product_(j!=i)(z+a_j), kappa_i>=0 and sum kappa_i<=1, the m=4 output (U_4+rR_4) star p+(R_4-1) star q has only nonpositive real roots for every real r>=0. This statement has no input-degree bound and does not need individual half-residue bounds.

The actual cycle seed p=(1+D)^2h,q=D(1+D)h satisfies these hypotheses. Consequently replacing one vertex of C6 by an arbitrary full-clique-quotient graph preserves that class. This is stronger than an ordinary-tau-input to edge-quotient-output assertion. It does not establish the original general BRW clique-sum conjecture.

The proof uses a scalar interlacing certificate and a multiaffine mass-splitting argument. Crucially, mass splitting uses the established partial-symmetrization theorem, not arbitrary convexity of the real-rooted cone.

## 中文范围说明
本结果把六边形顶点替换这一情形推进到任意输入次数。输入图仍须满足完整的团商实根条件；结论不是整个原猜想，也不宣称历史首创。对更长环的一般输入，尚未在此证明。这里证明的是实根保持，没有声称额外的相邻交错性质。

## Reproduce
Python 3 with SymPy 1.14.0 is the tested environment. Install the dependency from its official package registry if needed. Run `python run_all.py` from any working directory. The runner first verifies its exact file allowlist and SHA-256 manifest, then executes five guarded exact checkers using isolated optimized Python, and verifies integrity again.

The checks cover scalar resultants/discriminants, exact base root ordering, symbolic mass-splitting/diagonal identities, symbolic Bell translations, and independent Whitney-subset graph reconstructions. Finite examples support the proof but do not replace it. No floating root probes are included.

## Contents
- PROOF.md: full proof, actual-seed argument and C6 graph bridge.
- SOURCE.md: precise classical theorem citation and its use.
- author/: algebra and independent graph replay.
- audit_kernel/: first independent mathematical audit/checker.
- audit_bridge/: second independent full proof/graph audit and checkers.
- requirements.txt, run_all.py, MANIFEST.json: reproducibility and integrity.

## Remaining limitations
No m>=5 general theorem, no F/T pencil-interlacing theorem, no ordinary-tau-only input generalization, and no exhaustive literature/priority finding is asserted.
