# Bell chromatic quotients and clique attachment

Exact mathematical proofs and reproducible computations toward ordinary **τ-real clique-overlap closure**. The results below establish specific graph families and operations, **not the full τ clause of BRW Conjecture 6.5**. Here $P_G(x)=(-1)^{|V(G)|}\chi_G(-x)$, and the Bell transform sends $x^j$ to the Touchard polynomial $T_j$.

## Current results

- **Composition theorem for complete clique quotients.** The class with nonnegative-coefficient, real-nonpositive-rooted Bell quotients for **every actual clique size** is closed under graph join, disjoint union and ordinary clique amalgamation (exact common clique, no extra identifications or cross edges). A proved parameterized operator $C_{a,b}$ for integers $a,b\ge1$ supplies the join mechanism, extending the matching construction and coefficient substitution of [Kang–Liu–Sun–Zhang (2026)](https://arxiv.org/html/2609.07457v1); the other two closures follow from classical BRW Bell-product preservation. [Proof, scope and exact replay](extensions/2026-11-02-join-attachment-closure/README.md). This requires the stronger complete-quotient property, not ordinary τ-reality alone, and does not solve general BRW 6.5: bounded-$j$ seeds qualify only when their proved range covers the clique number. Historical novelty remains unassessed.

- **Full clique-quotient closure under five-cycle substitution.** Replacing one vertex of $C_5$ by any nonempty graph with the complete clique-quotient property preserves that same property, with no input-degree or graph-order bound. An elementary residue/polytope argument proves the stronger all-degree $m=3$ operator theorem; see the [proof, independent AI review and exact replay](extensions/2026-11-02-c5-full-clique-closure/README.md). This strengthens the edge-output conclusion below under stronger input hypotheses and subsumes this project's earlier low-degree $m=3$ certificates. It does not establish full-clique substitution for every cycle length or the full BRW conjecture; historical novelty remains unassessed.

- **Uniform cycle substitution.** For every $m\ge1$, replacing **one vertex** of $C_{m+2}$ by any ordinary τ-real graph $F$ preserves ordinary τ-reality and gives a Bell-real edge quotient. Thus the output is universally edge-attachable; the operation is iterable. With $D=d/dz$, $S=1+D$, $L_1=zD+z+1$, the operators $A_1=S^2$, $A_{m+1}=L_1A_m+DS$ preserve the entire nonpositive-root cone in every input degree. Root monotonicity and an enlarged arrowhead invariant give an ordinary mathematical proof, not finite-case extrapolation: simple strictly negative inputs give simple negative outputs with strict consecutive interlacing; nonzero boundary inputs give weak interlacing. [Proof at the published version](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/dc6d35ba53c6a41064bc9982cb524b05b74dc2ff/extensions/2026-11-02-uniform-cycle-substitution).

  Adding a universal $K_s$ to a seed $H$ with Bell-real edge quotient gives real-rooted clique quotients for orders $0\le j\le s+2$ and attachment along those clique sizes. This covers every clique only when $H$ is triangle-free; it does not give arbitrary larger-clique closure for general substituted graphs.

- **Every three-path theta graph.** For all $a,b,c\ge2$, the edge quotient $B(P_{\Theta(a,b,c)}/[x(x+1)])$ has strictly negative real roots. These graphs can be attached along any complete intersection to an arbitrary ordinary τ-real graph. [Proof and exact certificates at the published version](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/cfa1f5fd798116b44ddc95da6f90710e48fac14a/extensions/2026-11-02-all-theta) · [PDF](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/cfa1f5fd798116b44ddc95da6f90710e48fac14a/extensions/2026-11-02-all-theta/manuscript.pdf).

- **Parallel paths under a uniform length condition.** The [consolidated extension](extensions/2026-11-02-parallel-paths/README.md) proves the result for arbitrary path counts under an explicit product-radius criterion, with a sufficient logarithmic minimum-length bound. This remains independent current scope. Its five-cycle substitution and $\Theta(2,2,2,m)$ conclusions are now special cases of uniform cycle substitution. More generally, taking $F$ edgeless recovers $\Theta(2^k,m)$ (here $2^k$ means $k$ paths of length two), for $k\ge1$ and $m\ge2$. The earlier $C_5/C_7$ and short-branch special cases are subsumed, not additional scope; the all-three-path theorem above and the arbitrary-path-count length condition are not superseded. [Historical manuscript](extensions/2026-11-02-parallel-paths/MANUSCRIPT.md) · [PDF](extensions/2026-11-02-parallel-paths/manuscript.pdf) · [sealed manifest](extensions/2026-11-02-parallel-paths/MANIFEST.json).

- **Co-bipartite matching quotients.** Every edge-containing co-bipartite graph (its vertices can be partitioned into two cliques) has a Bell-real edge quotient, realized exactly as a reversed matching enumerator of an explicit bipartite graph. It is therefore universally attachable along an edge to any ordinary τ-real graph. For $n\ge3$, a chosen complement bipartition with part sizes $1\le s\le t$ also gives real-rooted clique quotients and attachment for $1\le j\le t$; this bound does **not** cover arbitrary larger cliques. The matching proof establishes the general result; 165 edge-quotient cases and 663 bounded-$j$ checks support its identities, not finite-sample extrapolation. [Proof and exact replay](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/3b1cf60a6bda10d2796ecf54438b0c5b895af81d/extensions/2026-11-02-cobipartite-matching) · [PDF](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/3b1cf60a6bda10d2796ecf54438b0c5b895af81d/extensions/2026-11-02-cobipartite-matching/manuscript.pdf). Independent AI review is not human peer review or proof-assistant certification; no historical-novelty claim is made.

  **Odd-cycle complements and matching surrogates.** For $G=\overline{C_{2m+1}}$, every $m\ge2$ and $1\le j\le m+1$, the Bell quotient $B(P_G/R_j)$ has only real nonpositive roots, where $R_j=x(x+1)\cdots(x+j-1)$. A matching-equivalent bipartite fork tree proves the result, giving attachment along every actual clique of $G$: those cliques have size at most $m$, so the additional algebraic quotient at $j=m+1$ does **not** assert an $(m+1)$-clique. Disjoint unions of bipartite components and odd cycles of length at least five also admit a bounded quotient range (see the precise component bound in the note), not arbitrary clique closure or trees attached directly to cycle vertices. [Proof, independent AI review and exact replay](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/9f1780659a475700dcfe9bfe913deb4ca1a19d55/extensions/2026-11-02-odd-cycle-complements). The 88 odd-cycle and 39 component checks support the infinite-family proof; they do not replace it. No general BRW closure or historical-novelty claim is made.

  **Paired rooted decorations.** For the complement of an odd cycle of length at least five with reflection-paired rooted connected bipartite decorations and an undecorated axis vertex, original order $N=2s+1$ guarantees real-rooted Bell quotients and attachment along its cliques of sizes $1\le j\le s+1$, not all larger cliques; see the [precise construction and proof](extensions/2026-11-02-paired-rooted-decorations/README.md). The exact obstruction to a rooted bipartite matching surrogate for rooted $C_5$ limits this method, not BRW real-rootedness.

  The matching/chromatic encoding and rectangular-board inclusion–exclusion are classical (Farrell–Whitehead, 1992), as is the cycle/fork identity (explicitly in Ma–Li, 2016); see the [matching-literature attribution and unresolved-overlap note](MATCHING_LITERATURE_STATUS.md).

  **Full-clique subclass with small matching components.** If the complement is bipartite and each connected component has matching number at most two, every actual clique quotient is Bell-real and attachment along every clique preserves ordinary τ-reality; see the [theorem and exact replay](extensions/2026-11-02-small-matching-components/README.md). An exact root rectangle for the 15-vertex example with complement $D(2,2)\sqcup D(1,1)\sqcup D(1,2)$ excludes the direct parabolic-region hypothesis of BRW Proposition 5.13, not all older criteria or historical overlap; single double-star complements already satisfy older chordal/real-chromatic-root criteria.

  **Explicit weighted-star attachment budget.** For a triangle-free complement $H$ with $n$ vertices, $e\ge1$ edges and matching number $\nu$, adding $t\ge\max(0,e+\nu-n)$ isolates gives $N=n+t$ and nonnegative weighted-board realizations of every Bell quotient $1\le j\le N-\nu$, hence universal attachment along every actual clique of its complement; the [proof gives a sharper spectral budget](extensions/2026-11-02-weighted-star-budget/README.md). Eventual closure after joining $K_t$ already follows from BRW Proposition 5.13, the sufficient budget is not claimed optimal or historically new, and the exact star-forest witness separates only the direct root-region hypothesis while already belonging to the cograph class.

- **Anchored incomparability graphs.** A proper partition into $k$ nonempty independent classes, with one selected vertex in each class adjacent to every vertex outside its class, gives real-rooted clique quotients of orders $0$ through $k$, provided the graph is an incomparability graph. These hypotheses require more than a dominating clique. [Precise theorem and verification package at the published version](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/1ecaf2df19a751422a4672a4ccb30aefe8f73f51/extensions/2026-11-02).

- **Complete bipartite graphs minus one edge.** For every $a,b\ge2$, $K_{a,b}-e$ has a real-rooted Bell edge quotient and universal complete-intersection attachment. The initial structural corollary concerns a join with one distinguished edge removed and requires stronger first-quotient hypotheses on its inputs; its attachment conclusion is also limited to clique sizes at most two. [Initial mathematical manuscript](manuscript.md) · [PDF](manuscript.pdf) · [immutable initial release](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/07ff23038f18c4a444555de037e135fc4aead7e0).

The earlier [fixed-two-path eventual theorem](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/1ecaf2df19a751422a4672a4ccb30aefe8f73f51/extensions/2026-11-02) and [uniform cofinite theta addendum](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/1ecaf2df19a751422a4672a4ccb30aefe8f73f51/extensions/2026-11-02-uniform-theta) remain unchanged as historical stages. Their theta conclusions are superseded by the all-length three-path theorem, not counted as additional current scope.

## Verify the result you are reading

Each package has its own README, manifest and checksums. **The root verifier checks only the initial missing-edge package; it does not verify every extension.** Use Python 3.10 or newer, with assertions enabled. Do not use `-O`, `-OO`, or `PYTHONOPTIMIZE`.

```sh
python3 -m pip install -r requirements.txt

# Uniform cycle theorem: supporting identity checks, not a replacement for the proof
python3 extensions/2026-11-02-uniform-cycle-substitution/verify.py

# Co-bipartite matching quotients: supporting checks; use Python 3.12 or compatible
python3 -m pip install -r extensions/2026-11-02-cobipartite-matching/requirements.txt
python3 extensions/2026-11-02-cobipartite-matching/verify.py

# Odd-cycle complements: supporting checks; the second also replays the first
python3 extensions/2026-11-02-odd-cycle-complements/verify.py
python3 extensions/2026-11-02-odd-cycle-complements/check_components.py

# Paired rooted decorations: supporting exact checks and rooted-surrogate obstruction
python3 extensions/2026-11-02-paired-rooted-decorations/verify.py

# Small matching components: supporting quotient and BRW-region checks
python3 extensions/2026-11-02-small-matching-components/verify.py
python3 extensions/2026-11-02-small-matching-components/check_region.py

# Weighted-star budget: aggregate supporting exact replay
python3 extensions/2026-11-02-weighted-star-budget/verify_all.py

# Complete clique-quotient composition: aggregate supporting exact replay
python3 extensions/2026-11-02-join-attachment-closure/run_all.py

# All-degree C5 full clique-quotient closure: guarded supporting exact replay
python3 extensions/2026-11-02-c5-full-clique-closure/run_all.py

# Initial missing-edge theorem and its original structural corollary
python3 verify_all.py

# All-length three-path theorem: full finite replay and Bernstein regeneration
python3 extensions/2026-11-02-all-theta/verify_all.py --finite --bernstein

# Consolidated parallel-path and five-cycle-substitution extension
python3 extensions/2026-11-02-parallel-paths/verify_all.py --all
```

For the uniform cycle theorem, read the ordinary mathematical proof at the version linked above; its exact symbolic scripts check identities only and are not proof premises. For the anchored and historical cofinite packages, follow their separate README commands. Finite graph checks are interface tests, not proofs of infinite parameter ranges; the manuscripts identify the exact computation-assisted proof obligations and the analytic or algebraic arguments completing them.

**Integrity scopes.** Check `SHA256SUMS` from the relevant package directory before replay. The root `ALLOWLIST.txt`, `MANIFEST.json` and `SHA256SUMS` cover the initial root package, not all extension directories. Older verifiers, including the root verifier, refresh their receipts, so environment-dependent output can change after a successful replay. The all-theta and consolidated parallel-path runners instead work in temporary directories without modifying their packages.

This landing index updates only the root README and its necessary manifest/checksum entries. All mathematical manuscripts, checker sources and mathematical data remain unchanged; the initial commit and original downloadable archives remain historical snapshots. The root audit and delta report describe that initial package, not a new mathematical review of this navigation update.

## Scope and review limits

BRW Conjecture 6.6 concerns graph joins, a different operation. The separate w-real clause is not newly proved by these packages. No arbitrary simultaneous graph-substitution theorem or all-length generalized-theta theorem for arbitrary path lengths and counts is claimed.

Derivation, exact computation and separate cross-checking were AI-assisted. This is not human peer review or proof-assistant formalization. No historical-priority or comprehensive-literature claim is made. In particular, the exact overlap with the Mu–Shen–Xu article remains unknown; see the [literature-status note](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/cfa1f5fd798116b44ddc95da6f90710e48fac14a/LITERATURE_STATUS.md).
