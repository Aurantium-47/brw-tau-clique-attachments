# Paired rooted decorations: a connected matching-surrogate extension

Date: 2026-11-02. AI-assisted research; historical novelty unassessed.
Attribution revision: classical ingredients explicitly identified below;
mathematical statements, proofs, and computational certificates unchanged.

## Attribution of classical ingredients

The matching/chromatic encoding, forbidden-board inclusion–exclusion,
and permission to use a matching-equivalent graph of different order are
classical ingredients, not new results of this note. Farrell–Whitehead
(1992), Theorem 1 and Corollary 1.1, identify the triangle-free-complement
matching/chromatic coefficient correspondence; Theorem 3 and Corollary
3.2 give the general and rectangular forbidden-edge formulas; Theorem 7
handles a matching-equivalent surrogate of different vertex order.
[Primary paper, pp. 759–762](https://www.maths.tcd.ie/EMIS/journals/HOA/IJMMS/Volume15_4/213850.pdf),
[DOI 10.1155/S016117129200098X](https://doi.org/10.1155/S016117129200098X).

Likewise, the bare cycle/fork identity is explicitly known: Ma–Li (2016),
Lemma 3.2(2), p. 923, gives
`mu(T_(1,1,n),x)=mu(P_1,x) mu(C_(n+2),x)`.
With n=L-2 this is exactly `mu(D_(L+1),x)=x mu(C_L,x)`.
[Ma–Li, DOI 10.4236/am.2016.79082](https://doi.org/10.4236/am.2016.79082).

A scoped primary-source literature audit did not locate an exact prior
equivalent of the paired-decoration construction below or its combined
Bell-quotient/universal-attachment conclusion. This negative search is
not proof of novelty. Rooted matching methods and deletion recurrences
are classical; no novelty claim is made for those techniques. See
`LITERATURE_ATTRIBUTION.md` for references and search limitations.

## Main result

Fix an odd integer L=2m+1>=5. Start with the labeled cycle
v1,...,vL,v1. Leave v1 undecorated. For each i=2,...,m+1 choose
an arbitrary finite rooted connected bipartite graph (T_i,r_i), and
attach two disjoint copies by identifying their roots with vi and
v_(L+2-i). Different copies meet only their respective cycle vertex.
Trivial one-vertex decorations are allowed. Denote this connected,
triangle-free graph by H, put N=|V(H)|=2s+1, and G=complement(H).

**Theorem.** There is a bipartite graph F with N+1 vertices, bipartition
sizes s and s+2, and exactly the same matching numbers as H.
Consequently, for every 1<=j<=s+1,

    B(P_G/R_j)(z) = sum_k m_k(J_j) z^(N-j-k),
    J_j = K_(N-j,N-1) minus E(F).

Here F is embedded in the indicated board, P_G(x)=(-1)^N chi_G(-x),
R_j(x)=x(x+1)...(x+j-1), and B(x^d) is the Touchard polynomial T_d(z).
All zeros of the displayed polynomial are real and nonpositive.
Thus G is universally ordinary-tau-real attachable along each of its
j-cliques for j<=s+1, in particular along every edge. The statement does
not assert that every clique of G has size at most s+1. For example, C5
with three pendant leaves at each of v2 and v5 has N=11 and alpha(H)=8,
so omega(G)=8 exceeds s+1=6: the six pendant leaves, v1, and v3 form
an independent set in H. An independent set using v2 or v5 loses all
three leaves at that root, and the remaining cycle vertices v1,v3,v4
have independence number two, proving the upper bound eight.

This includes arbitrary paired tree attachments (a connected unicyclic
family), and paired rooted bipartite graphs with their own even cycles
(a connected multicyclic family). It is not restricted to a disjoint
union of cycles and bipartite components.

## Proof of matching equivalence

Write Q_X(t)=sum_k m_k(X)t^k, unaffected by isolated vertices. Let B be H
with edge v1vL deleted; thus B is a decorated path. Construct F from B
by adding one new vertex w and edge wv2. It is bipartite because its
spine is a path and every decoration is bipartite. Edge deletion gives

    Q_H = Q_B + t Q_(B-{v1,vL}),
    Q_F = Q_B + t Q_(B-v2).

The first summand in the second equality omits the harmless isolated w.
We claim B-v2 is isomorphic to (B-{v1,vL}) disjoint union K1.
In B-v2 the vertex v1 is isolated because it has no decoration.
The nonisolated comparison consists of:

* the decorated path v2,...,v_(L-1) versus v3,...,vL;
* the root-deleted remnant of the decoration at vL versus that at v2.

The reflection vi -> v_(L+2-i), on the labels 2,...,L, identifies the
first two decorated paths and identifies the two root-deleted remnants.
Rooted isomorphism of each paired decoration is exactly what is needed;
the remnant can be disconnected or empty. This proves the claim and
Q_H=Q_F.

## Original-order board capacity

Let d=sum_(i=2)^(m+1)(|V(T_i)|-1). Then N=L+2d=2(m+d)+1,
so s=m+d>=2. In the undecorated path, the even-indexed vertices occupy
one side of size m, and the odd-indexed vertices the other of size m+1.
Reflection pairs indices of opposite parity because L+2 is odd.
Therefore two copies of any rooted bipartite graph, attached at opposite
parities, add |V(T_i)|-1 vertices to each side: swapping the root color
swaps the two color-class contributions. This remains true for unbalanced
decorations. Finally w joins the odd-indexed side. Hence the parts of F
are exactly s and s+2, while the ORIGINAL graph order is N=2s+1.
For 1<=j<=s+1,

    s <= N-j,    s+2 <= N-1=2s.

The matching-surrogate principle in the accepted odd-cycle note now
applies without changing N to N+1. Its forbidden-edge inclusion-exclusion
identity is the stated formula. Heilmann--Lieb gives the real nonpositive
zeros, and Bell-product preservation gives the clique attachment claim.
No new analytic preservation theorem is assumed.

## Matching-surrogate principle and normalization (standalone)

For completeness, let H be any triangle-free graph of original order N,
G its complement, and F any bipartite graph matching-equivalent to H
whose sides fit a=N-j and b=N-1, where j>=1. Independent blocks of G
have size at most two, so stable partitions correspond to matchings of H:

    P_G = sum_k (-1)^k m_k(H) R_(N-k).

Since the matching number of F is at most a, each nonzero summand is
divisible by R_j. The elementary Bell rising-factorial identity is

    B(product_(i=0)^(r-1)(x+c+i))
      = sum_l binom(r,l) binom(r+c-1,l) l! z^(r-l),  c>=1.

Its exponential generating function in r is
(1-u)^(-c) exp(zu/(1-u)), which proves it by coefficient extraction.
Since m_l(K_(a,b))=binom(a,l)binom(b,l)l!, taking c=j and r=a-k
gives B(R_(N-k)/R_j)=M_(K_(a-k,b-k)), where M uses the smaller-board
first-side exponent a-k. Forbidden-edge inclusion-exclusion then yields

    B(P_G/R_j) = sum_k (-1)^k m_k(F) M_(K_(a-k,b-k))
               = M_(K_(a,b) minus E(F)).

The latter coefficient at z^(a-l) counts l-matchings avoiding F.
For J=K_(a,b) minus E(F), the ordinary matching polynomial obeys

    mu_J(y)=sum_l (-1)^l m_l(J)y^(a+b-2l)
           =(-1)^a y^(j-1) M_J(-y^2).

Heilmann--Lieb real-rootedness of mu_J therefore implies that every root
of M_J is nonpositive real. These enumerators also have nonnegative
coefficients. Finally, the Bell product identity is

    B(pq)=B(p) star B(q),
    (f star g)(z)=sum_k z^k f^(k)(z) g^(k)(z)/k!.

Brenti--Royle--Wagner Proposition 5.4 supplies preservation of
nonnegative-coefficient polynomials with only nonpositive real zeros.
If G and an ordinary-tau-real X meet in exactly a common K_j, with no
other identifications or extra cross edges, the chromatic clique-sum
identity gives P_(G union X)=(P_G/R_j)P_X. Apply that preservation theorem.
Ordinary tau-realness here means real-rootedness of Theta_X=B(P_X), with
no factorial coefficient rescaling; Theta_X(z)=(-1)^|V(X)| tau_BRW(X;-z).
Chromatic coefficient sign alternation gives nonnegative coefficients.
Thus a tau-real Theta_X has only nonpositive zeros. This verifies all
normalizations and the asserted attachment conclusion.

## Why arbitrary rooted replacement is not available even for C5

A rooted matching equivalence means both Q_F=Q_H and
Q_(F-r)=Q_(H-v). This is the sufficient pair of identities for freely
identifying the root with any other rooted graph. Indeed, if A and D
meet only at their roots, then

    Q_(A wedge D) = Q_A Q_(D-r) + Q_(A-r) Q_D
                     - Q_(A-r) Q_(D-r).

The three terms count matchings using a root edge on at most one side.

**Obstruction.** No finite simple rooted bipartite graph (F,r) is rooted
matching-equivalent to a rooted C5, even allowing arbitrarily many
extra isolated vertices.

Proof: Q_C5=1+5t+5t^2, so F has five edges, exactly five two-matchings,
and no three-matching. Ignore isolated vertices. If F has a cycle,
bipartiteness and the five-edge count force a C4 plus one edge. That
edge is either pendant, yielding four two-matchings, or disjoint,
yielding six two-matchings. (A chord is impossible in a simple
bipartite C4.) Thus F is a forest. The identity

    m_2(F) = binom(5,2) - sum_v binom(deg(v),2)

forces the latter sum to be 5. Maximum degree is at most 3, and the
only possible finite forest degree pattern is one degree-3 vertex,
two degree-2 vertices, and three leaves: otherwise five degree-2
vertices would already consume the entire degree sum 10 with no
leaves. The degree pattern has six nonisolated vertices, hence the
forest is connected. It is a three-arm subdivided claw with arm
lengths either (3,1,1) or (2,2,1). The latter has a perfect matching,
contradicting m_3=0. Thus F is the fork D6, possibly plus isolates.

Root deletion must remove two edges, since Q_(C5-v)=Q_P4=1+3t+t^2.
Only the two degree-2 vertices of D6 are eligible. Deleting these gives,
respectively,

    (1+2t)(1+t)=1+3t+2t^2,    or    1+3t.

Neither is Q_P4. Extra isolates do not change the conclusion.

This is an exact obstruction to arbitrary rooted replacement of a bare
C5, NOT a BRW counterexample, NOT a failure for its independently decorated
versions, and NOT an obstruction to other matching-equivalent bipartite
surrogates for decorated graphs. The paired construction bypasses the
obstruction by preserving two deletion residuals globally, not by making
one rooted cycle replacement.

## Verification, provenance, and limitations

Run `python verify.py`. The exact certificate checks paired leaves,
paths, stars rooted at different positions, even cycles, and mixed
choices; it independently compares integer matching enumerators for
H and F, the deletion residuals, original-order part capacities, and
Bell quotient coefficients with exact nonpositive real-root counts.
For small boards it also counts matchings on the allowed board directly.
The completed certificate contains 15 paired-decoration examples and 97
exact quotient/root checks. A finite exhaustive bipartite graph check
through six vertices finds 24 labeled matching-equivalent candidates and
independently verifies the C5 rooted obstruction classification.
The proof, not finite checks, establishes the infinite family.

The antecedent matching-surrogate note is the accepted
[odd-cycle note](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/9f1780659a475700dcfe9bfe913deb4ca1a19d55/extensions/2026-11-02-odd-cycle-complements/RESEARCH_NOTE.md).
Foundational inputs are Heilmann--Lieb, *Theory of monomer-dimer systems*
(1972), doi:10.1007/BF01877590, and Brenti--Royle--Wagner, *Location of
Zeros of Chromatic and Related Polynomials of Graphs* (1994),
doi:10.4153/CJM-1994-002-3, as used in that accepted note.
A subsequent scoped primary-source literature audit identified the known
ingredients explicitly credited above. It did not establish novelty of
the paired construction. Possible Mu--Shen--Xu full-text overlap remains
unresolved; no unavailable publisher text was accessed or bypassed. Unrestricted ordinary BRW
real-rootedness and unrestricted graph edge closure remain unresolved.
No external state was changed.
