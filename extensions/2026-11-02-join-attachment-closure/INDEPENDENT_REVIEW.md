# Independent review of rooted join preservation

Date: 2026-11-02. Independent AI mathematical review, not human peer review or proof-assistant certification. No external writes. Historical novelty is not assessed.

## Verdict

**The proposed positive theorem is mathematically valid.** For integers a,b≥1, the rooted join operator C_ab preserves monic polynomials whose zeros are real and nonpositive. Consequently the graph class with real-nonpositive Bell quotients at every actual clique size is closed under graph join. This does not prove arbitrary clique-union closure or BRW Conjecture 6.5.

The proof below was checked independently from the operator definition. The file `review_check.py` supplies a separate exact basis computation: 225 monomial cases a,b=1,2,3 and p,q=0,…,4 agree, including all zero-degree edge cases. Four factorized examples additionally pass exact real-root counts. Finite checks are supplementary, not premises.

## 1. Exact operator and graph transfer

Write B(x^k)=T_k(z), and r_k^(a)(x)=(x+a)…(x+a+k−1). If B^{-1}f=Σ c_k r_k^(a) and B^{-1}g=Σ d_l r_l^(b), define

C_ab(f,g)=B(Σ c_k d_l r_(k+l)^(a+b)).

For a graph containing an a-clique, P_G/R_a expands in r_k^(a) by exactly the signed stable-partition coefficients of G with index a+k. The signed coefficients for a join convolve: stable blocks cannot meet both join factors. Hence

C_ab(B(P_G/R_a),B(P_H/R_b))=B(P_(G∨H)/R_(a+b)).

The signs agree: (−1)^(n−a−k)(−1)^(m−b−l)=(−1)^(n+m−a−b−k−l). Divisibility alone causes no hidden low-index term: an actual a-clique implies the stable-partition coefficients below a vanish.

## 2. Independent generating-function derivation

B^{-1}(exp(zu))=(1+u)^x. Its shifted-rising expansion is

(1+u)^x=(1+u)^(−a) Σ_k r_k^(a)(x) [u/(1+u)]^k/k!.

Applying the operator to the two exponentials gives

Σ_(p,q≥0) C_ab(z^p,z^q) u^p v^q/(p!q!)
 = [(1+u)^b(1+v)^a/(1−uv)^(a+b)] exp[z(u+v+2uv)/(1−uv)].

This uses the Bell transform of exp(xw), namely exp[z(exp(w)−1)]. It is valid as a formal power-series identity.

Make the invertible formal substitution

u=ξ/(1+η),  v=η/(1+ξ).

Then (u+v+2uv)/(1−uv)=ξ+η, the prefactor becomes (1+ξ)^b(1+η)^a, and the Jacobian is

∂(u,v)/∂(ξ,η)=(1+ξ+η)/[(1+ξ)^2(1+η)^2].

Formal coefficient extraction (or the equivalent two-variable residue substitution) therefore gives

C_ab(z^p,z^q)/(p!q!)
 = [ξ^p η^q] (1+ξ+η)e^{z(ξ+η)}(1+ξ)^(q+b−1)(1+η)^(p+a−1).

Since p![ξ^p]e^{zξ}(1+ξ)^r is the row-reversed matching polynomial M_(p,r)(z) of K_(p,r), this proves

C_ab(z^p,z^q)=(1+∂_z)[M_(p,q+b−1)(z) M_(q,p+a−1)(z)].

The derivative has exactly the right combinatorial interpretation: in a baseline matching, the exponent of z is the number of unused rows; adding a single common column allows matching it to any such row. The baseline boards are disjoint. Thus the formula is precisely the reversed matching enumerator of the claimed enlarged board.

## 3. Root-edge lifting and positivity

For f=∏_(i=1)^p(z+α_i) and g=∏_(j=1)^q(z+β_j), all α_i,β_j≥0, use p red rows and q blue rows. There are q+b−1 columns originally accessible only to red rows, p+a−1 columns originally accessible only to blue rows, and a common column adjacent to every row.

Because a,b≥1, there are at least p blue-only columns and q red-only columns. Reserve distinct ones, add an α_i-weighted edge from red row i to its reserved blue-only column, and add β_j-weighted edges in the other direction. These added edges do not duplicate baseline edges and are pairwise vertex-disjoint.

For any selected subset S of α-edges and T of β-edges, delete their endpoints. The remaining baseline board is exactly the same construction with p replaced by p−|S| and q by q−|T|. In particular the two exclusive column counts decrease in the correct opposite directions. The common column is unaffected. Therefore the coefficient of ∏_(i∈S)α_i∏_(j∈T)β_j in the matching enumerator is C_ab(z^(p−|S|),z^(q−|T|)). Bilinearity proves that the entire matching enumerator equals C_ab(f,g).

All weights are nonnegative. The classical weighted matching real-root theorem implies that this reversed enumerator has only real nonpositive zeros. There are p+q rows, so no matching can have more than p+q edges; reversing with exponent p+q cannot create negative powers. For a direct normalization check, its matching polynomial satisfies μ(y)=(−1)^(p+q)y^(a+b−1)M(−y²).

## 4. Boundary cases and downward closure

The board and formulas remain valid for p=0, q=0, or both. In particular C_ab(1,1)=1. Zero root parameters merely give zero-weight edges, which can be omitted. Positive leading constants can be restored by bilinearity. Empty input graphs can be handled separately because their join is the other graph.

It suffices to check the maximal actual clique size. If F=B(h) has real nonpositive zeros and nonnegative coefficients, then

B((x+j)h)=(z+j)F+zF'

has the same properties for every integer j≥0. To see the zero statement, first remove a zero-root factor F=z^m H. For simple negative roots r_i of H, the relevant quotient is

z+j+m+Σ_i z/(z−r_i).

Its derivative away from the poles is 1+Σ_i (−r_i)/(z−r_i)^2>0. Its signs at the poles and at zero yield one real zero in each intervening interval and one in the leftmost interval; the final root is nonpositive. Repeated negative roots follow by approximation, and the zero-root factor remains. Coefficient nonnegativity is immediate from the differential expression.

Take a=ω(G), b=ω(H) for nonempty graphs. Clique number is additive under join. The rooted operator proves the quotient at a+b, and repeated downward steps prove every smaller positive clique-size quotient. The hypotheses on all smaller input cliques are therefore redundant: the maximal quotient alone characterizes this class.

## Attribution and scope

The construction is a parameterized rooted extension of the Lah/star matching mechanism in Kang–Liu–Sun–Zhang, arXiv:2609.07457v1, rather than an invocation of their ordinary-join theorem as though it already treated quotients. Their theorem requires zero factors and their ordinary star product is not C_ab. Heilmann–Lieb supplies the classical matching real-root input. The Bell product used for clique attachment is a different operation again. No assertion of historical novelty or exclusion of overlap with inaccessible literature is justified by this review.

## Addendum: composition corollaries reviewed independently

**The proposed disjoint-union and exact-clique-sum corollaries are correct.** Suppose G_1 and G_2 intersect in precisely a complete graph K_k, with no other vertex identifications and no edges between their remaining vertex sets. Write W=G_1∪_(K_k)G_2, and assume ω_1≥ω_2. Any clique of W lies entirely in one factor, since vertices outside the intersection in opposite factors are nonadjacent. Thus ω(W)=ω_1. The signed chromatic clique-sum identity gives

P_W/R_(ω_1) = (P_(G_1)/R_(ω_1)) (P_(G_2)/R_k).

For k≥1, both factors on the right have Bell transforms with real nonpositive zeros by the complete-quotient hypotheses. For k=0, put R_0=1; the second factor's ordinary Bell transform follows by repeated downward multiplication, including the final j=0 step. The BRW Bell product identity

B(fg)=Σ_(r≥0) z^r [B(f)]^(r)[B(g)]^(r)/r!

and its real-nonpositive-root preservation establish the maximal quotient for W. Downward closure gives all positive clique sizes. For disjoint union k=0, the same proof applies. Empty factors are harmless and may instead be handled separately.

Consequently the class is closed under (i) disjoint union, (ii) exact clique sums with the stated graph-intersection convention, and (iii) graph join by the theorem reviewed above. This is a structural closure theorem for the **stronger complete-quotient class**, not a proof that arbitrary ordinary tau-real graphs have this property or that arbitrary ordinary tau-real clique sums are tau-real.

**Seed qualification is essential.** Only families proved to have the full actual clique-size range may be inserted into this closure construction. A theorem restricted to j≤j_0 does not supply a seed unless j_0≥ω(G) for that particular graph. In particular a co-bipartite result bounded by an original colorclass size must not silently be promoted to the full-clique result when larger actual cliques exist. Padding/budget hypotheses, matching-component restrictions, and any other assumptions in existing full-range seed theorems must be retained.
