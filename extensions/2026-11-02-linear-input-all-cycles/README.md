# All cycle lengths for linear clique-quotient inputs

2026-11-02. Exact partial result with independent AI mathematical review. This is not human peer review, a Lean/formal proof, or a historical-priority claim.

## 中文概览

本包证明：在输入多项式为一次式的完整参数范围内，循环长度可以任意增长，不再只限于五边形。证明先用精确代数证书建立一个可反复传递的不等式条件，再调用本项目此前已证明的矩阵引理进行无限归纳；不是把很多有限例子计算通过后推断全部成立。

图论实例是“一个最大团外加一个顶点”的替换，包括九顶点的明确例子。这个例子不满足原论文某个直接充分条件，但本结果仍能处理。这里只排除了那个充分条件及少数直接分解方式，并不声称所有旧方法都不能处理，或我们是历史首创。

一般高次输入的六边形及更长循环情形仍未解决。附上的 m=4 推导只准确定位待证明的符号不等式，不能作为已完成的定理。

## The proved statement

For every real a>=0 and r>=1, set h=z+a, p=(1+D)^2h=z+a+2, q=D(1+D)h=1, L=z(1+D)+1 and H=Lq+r p. Define

F1=(L+r)p, and F_(m+1)=L F_m+H.

Every F_m, m>=1, has only simple strictly negative roots. The established arrowhead invariant holds at F3 and propagates thereafter. **Strict consecutive interlacing is asserted only from F3 onward**: F_m interlaces F_(m+1) for m>=3. The shorter-range supplement proves F1 and F2 root properties separately.

For graph inputs with order omega+1, a=d is the integer number of neighbors of the extra vertex in a maximum K_r, so 0<=d<=r-1. Replacing one vertex of any cycle by that graph preserves the full clique-quotient property. For cycle path length m>=2 the Bell transform of the maximal quotient is F_m; the m=1 triangle case is a join and the Bell transform of its maximal quotient is z+d+2 directly. Real a,r outside the graph parameter range are an analytic extension, not additional graph parameters.

## Reading order

1. `LINEAR_SEED_PROOF.md`: exact resultant seed and infinite propagation.
2. `SHORT_RANGE_SUPPLEMENT.md`: elementary m=1,2 cases.
3. `dependency/ARROWHEAD_THEOREM.md`, Lemma2: the complete previously reviewed matrix invariant used by the proof. Its other statements are preserved as dependency context, not claimed as new in this release.
4. `INDEPENDENT_REVIEW.md`: independent verification and scope boundaries.
5. `GRAPH_BRIDGE.md` and `GRAPH_SCOPE.md`: direct coloring translation, nine-vertex graph, and sufficient-criterion separation.
6. `M4_REDUCTION.md`: exact but unresolved arbitrary-degree next-case reduction.

Original paths in preserved source notes are mapped by `PROVENANCE.json`; the complete required dependency is included locally. External source paths are not needed to run the checks.

## Reproduce

Use Python3 with SymPy installed, then run `python run_all.py` from any working directory. The runner verifies the full file inventory/hashes, copies to a temporary directory, and executes exact checks. New checkers use explicit runtime guards and run under optimized Python. The unchanged historical dependency scripts intentionally reject optimized execution; the runner verifies that guard and runs them normally.

Checks validate complete polynomial certificates, rational root/residue bounds, exact trace identities, the nine-vertex chromatic polynomial by two independent4096-subset enumerations, complex root isolation and boundary exclusion, and the displayed m=4 identities, including an independent formal differential-ring verification valid in arbitrary degree. These computations support the written proof; finite graph/root examples are not used as a substitute for the all-iteration argument.

No floating probes are included or executed. General-degree m>=4 remains unresolved.

## Attribution and evidence boundary

The arrowhead lemma is an earlier result within this project and is reproduced with its previous review and exact source hashes. The original graph-polynomial context is Brenti, Royle and Wagner, *Location of zeros of chromatic and related polynomials of graphs* (Canadian Journal of Mathematics46,1994), DOI https://doi.org/10.4153/CJM-1994-002-3. The example separates the direct parabolic hypothesis of Proposition5.13, not the paper's entire theory. Full historical overlap with later literature remains unverified.

This is an extension within the existing research family, not a new problem-family count, new upstream contribution, or a resolution of the general BRW conjecture.
