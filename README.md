# Bell chromatic quotients and clique attachment

Exact mathematical proofs and reproducible computations toward ordinary **τ-real clique-overlap closure**. The results below establish specific graph families and operations, **not the full τ clause of BRW Conjecture 6.5**. Here $P_G(x)=(-1)^{|V(G)|}\chi_G(-x)$, and the Bell transform sends $x^j$ to the Touchard polynomial $T_j$.

## Current results

- **Every three-path theta graph.** For all $a,b,c\ge2$, the edge quotient $B(P_{\Theta(a,b,c)}/[x(x+1)])$ has strictly negative real roots. These graphs can be attached along any complete intersection to an arbitrary ordinary τ-real graph. [Proof and exact certificates at the published version](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/cfa1f5fd798116b44ddc95da6f90710e48fac14a/extensions/2026-11-02-all-theta) · [PDF](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/cfa1f5fd798116b44ddc95da6f90710e48fac14a/extensions/2026-11-02-all-theta/manuscript.pdf).

- **Parallel paths and five-cycle substitution.** The [consolidated extension](extensions/2026-11-02-parallel-paths/README.md) proves three complementary statements: arbitrary path counts under an explicit product-radius criterion (with a sufficient logarithmic minimum-length bound); every $\Theta(2,2,2,m)$, $m\ge2$; and substitution of **any ordinary τ-real graph** for one vertex of a five-cycle. The substitution is iterable and its output is universally **edge-attachable**; because larger cliques may occur, no attachment theorem for clique sizes above two is asserted. [Manuscript](extensions/2026-11-02-parallel-paths/MANUSCRIPT.md) · [PDF](extensions/2026-11-02-parallel-paths/manuscript.pdf) · [sealed manifest](extensions/2026-11-02-parallel-paths/MANIFEST.json).

- **Anchored incomparability graphs.** A proper partition into $k$ nonempty independent classes, with one selected vertex in each class adjacent to every vertex outside its class, gives real-rooted clique quotients of orders $0$ through $k$, provided the graph is an incomparability graph. These hypotheses require more than a dominating clique. [Precise theorem and verification package at the published version](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/1ecaf2df19a751422a4672a4ccb30aefe8f73f51/extensions/2026-11-02).

- **Complete bipartite graphs minus one edge.** For every $a,b\ge2$, $K_{a,b}-e$ has a real-rooted Bell edge quotient and universal complete-intersection attachment. The initial structural corollary concerns a join with one distinguished edge removed and requires stronger first-quotient hypotheses on its inputs; its attachment conclusion is also limited to clique sizes at most two. [Initial mathematical manuscript](manuscript.md) · [PDF](manuscript.pdf) · [immutable initial release](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/07ff23038f18c4a444555de037e135fc4aead7e0).

The earlier [fixed-two-path eventual theorem](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/1ecaf2df19a751422a4672a4ccb30aefe8f73f51/extensions/2026-11-02) and [uniform cofinite theta addendum](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/1ecaf2df19a751422a4672a4ccb30aefe8f73f51/extensions/2026-11-02-uniform-theta) remain unchanged as historical stages. Their theta conclusions are superseded by the all-length three-path theorem, not counted as additional current scope.

## Verify the result you are reading

Each package has its own README, manifest and checksums. **The root verifier checks only the initial missing-edge package; it does not verify every extension.** Use Python 3.10 or newer, with assertions enabled. Do not use `-O`, `-OO`, or `PYTHONOPTIMIZE`.

```sh
python3 -m pip install -r requirements.txt

# Initial missing-edge theorem and its original structural corollary
python3 verify_all.py

# All-length three-path theorem: full finite replay and Bernstein regeneration
python3 extensions/2026-11-02-all-theta/verify_all.py --finite --bernstein

# Consolidated parallel-path and five-cycle-substitution extension
python3 extensions/2026-11-02-parallel-paths/verify_all.py --all
```

For the anchored and historical cofinite packages, follow their separate README commands. Finite graph checks are interface tests, not proofs of infinite parameter ranges; the manuscripts identify the exact computation-assisted proof obligations and the analytic or algebraic arguments completing them.

**Integrity scopes.** Check `SHA256SUMS` from the relevant package directory before replay. The root `ALLOWLIST.txt`, `MANIFEST.json` and `SHA256SUMS` cover the initial root package, not all extension directories. Older verifiers, including the root verifier, refresh their receipts, so environment-dependent output can change after a successful replay. The all-theta and consolidated parallel-path runners instead work in temporary directories without modifying their packages.

This landing index updates only the root README and its necessary manifest/checksum entries. All mathematical manuscripts, checker sources and mathematical data remain unchanged; the initial commit and original downloadable archives remain historical snapshots. The root audit and delta report describe that initial package, not a new mathematical review of this navigation update.

## Scope and review limits

BRW Conjecture 6.6 concerns graph joins, a different operation. The separate w-real clause is not newly proved by these packages. No general graph-substitution theorem or all-length generalized-theta theorem for arbitrary path counts is claimed.

Derivation, exact computation and separate cross-checking were AI-assisted. This is not human peer review or proof-assistant formalization. No historical-priority or comprehensive-literature claim is made. In particular, the exact overlap with the Mu–Shen–Xu article remains unknown; see the [literature-status note](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/cfa1f5fd798116b44ddc95da6f90710e48fac14a/LITERATURE_STATUS.md).
