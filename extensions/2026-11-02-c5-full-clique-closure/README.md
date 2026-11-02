# Full clique quotients under C5 vertex substitution

## English theorem
Let G be a nonempty graph whose every actual clique-size quotient B(P_G/R_j) has nonnegative coefficients and only real nonpositive zeros. Replace one vertex of a five-cycle by G, with every vertex of G joined to the two former neighbors. The resulting graph has the same full clique-quotient property.

A stronger arbitrary-degree polynomial statement is proved: for L=z(1+D)+1, p=product(z+a_i), q=sum a_i*kappa_i*product_{j!=i}(z+a_j), with a_i>=0, 0<=kappa_i<=1/2 and sum kappa_i<=1, T=(L^2+L+I)p interlaces F=L^3p+(L^2+L)q. Thus F+rT is real-nonpositive-rooted for every real r>=0. Root estimates and a polytope-vertex reduction prove this without input-degree bounds or large discriminant computations.

## 中文范围说明
这是原先循环替换问题中“五边形替换”这一整类情形的完整证明：输入图可以任意大，不再限于前一个证书包中的低次数情况。前提是输入图的所有实际团大小对应的商都满足实根条件，结论保留同样强的条件。因此它强于此前“普通 τ 实根输入推出边对应商实根”的结果。

这并没有解决所有长度的循环替换，也没有解决完整 BRW 猜想。尚未排除与全部既有文献重叠，不能宣称历史首创。这里的独立复核是另一次数学审查，不是人类同行评审或 Lean 形式化验证。旧的低次数证书仍然正确，只是现在被更一般的本项目定理覆盖。

## Proof and verification
- PROOF.md contains the elementary all-degree argument, seed-residue lemma, direct coloring count and graph corollary.
- INDEPENDENT_REVIEW.md records independent checking and the repaired arithmetic typo. The corrected bound preserves the theorem.
- check_identities.py checks exact algebra and 164 finite pencil examples. These examples are diagnostics, not the all-degree proof.
- check_graph_bridge.py independently enumerates stable partitions on 14 input graphs and their substituted outputs, checking 56 exact clique quotients. This verifies the bridge on finite examples only.
- run_all.py first verifies the exact file inventory and hashes, then executes the author checkers with isolated optimized Python from an unrelated temporary directory. The independent reviewer scripts also run in isolated optimized Python; explicit raising guards ensure their checks are not disabled by optimization. Python 3 and SymPy are required; no network access is used.

Run: python3 run_all.py

## Attribution and unresolved scope
The Bell-product identity and real-root preservation are classical: Francesco Brenti, Gordon F. Royle and David G. Wagner, “Location of Zeros of Chromatic and Related Polynomials of Graphs,” Canadian Journal of Mathematics 46 (1994), 55–80, Propositions 4.2 and 4.4; DOI https://doi.org/10.4153/CJM-1994-002-3 . This is the only external preservation theorem used here. The seed lemma is reproduced from this project's prior reviewed uniform-cycle proof with an explicit proof. The graph coloring computation is included directly.

General m>=4 cycle substitution remains unresolved by this package. No additional graph-family count, upstream PR count, novelty priority, full BRW resolution, or formal certification is claimed.
