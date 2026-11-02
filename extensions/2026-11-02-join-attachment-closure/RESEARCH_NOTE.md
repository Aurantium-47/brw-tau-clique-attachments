# Rooted Bell join preservation and full-clique quotient closure

2026-11-02. AI-assisted research, historical novelty unassessed. The ordinary graph-join theorem of Kang–Liu–Sun–Zhang is not claimed as new. The theorem below is a parameterized extension of its matching mechanism.

## Result

For a finite graph G of order n put P_G(x)=(-1)^n χ_G(-x), R_j(x)=x(x+1)…(x+j−1), and let B(x^k)=T_k(z), the Touchard polynomial. Say G has the **complete clique-quotient property** if B(P_G/R_j) has nonnegative coefficients and only real nonpositive roots for every 1≤j≤ω(G). Constants qualify.

**Theorem.** This class is closed under graph join. More precisely, for any positive clique sizes a of G and b of H, if B(P_G/R_a) and B(P_H/R_b) are real-nonpositive-rooted with nonnegative coefficients, then so is B(P_(G∨H)/R_(a+b)).

This is not a proof of BRW Conjecture 6.5 for arbitrary ordinary tau-real factors. It proves a structural closure rule for the stronger quotient property. No new historical-priority claim is made; overlap with unavailable Mu–Shen–Xu full text remains unassessed.

## 1. The parameterized operator

For integers a,b≥1 define C_(a,b) as follows. Expand

    B^(-1)f = Σ_k c_k (x+a)^{overline k},
    B^(-1)g = Σ_l d_l (x+b)^{overline l}.

Set

    C_(a,b)(f,g) = B[Σ_(k,l) c_k d_l (x+a+b)^{overline(k+l)}].       (1)

**Operator theorem.** C_(a,b) preserves the cone of nonzero polynomials having nonnegative coefficients and only real nonpositive zeros.

Let D=1−uv and Φ=(u+v+2uv)/D. Its exponential kernel is

    Σ_(p,q≥0) C_(a,b)(z^p,z^q) u^p v^q/(p!q!)
        = ((1+u)^b (1+v)^a / D^(a+b)) exp(zΦ).                    (2)

Indeed B^(-1)(exp(zu))=(1+u)^x. Its shifted-rising expansion is

    (1+u)^x=(1+u)^(-a) Σ_k (x+a)^{overline k}
                                       [u/(1+u)]^k/k!.

Insert both expansions into (1), sum the rising-factorial generating function, and apply B(t^x)=exp(z(t−1)). All series here are formal; no analytic interchange is required.

## 2. A matching realization of the monomial kernel

For a bipartite graph with r specified row vertices define

    M_J(z)=Σ_(matchings S of J) w(S) z^(r−|S|).

For p,q≥0 form Γ_(p,q)^(a,b) with p red rows, q blue rows, q+b−1 columns adjacent to all red rows, p+a−1 disjoint columns adjacent to all blue rows, and one additional column adjacent to every row. All edges initially have weight one. Then

    C_(a,b)(z^p,z^q) = M_(Γ_(p,q)^(a,b))(z).                     (3)

To prove this, the reversed matching enumerator without the additional common column is

    A_(p,q)(z)=M_(K_(p,q+b−1))(z) M_(K_(q,p+a−1))(z).

Adding the common column gives (1+∂_z)A_(p,q), since a matching with k matched rows has p+q−k choices for its extra edge.

Here is the exact coefficient calculation establishing (3). Set

    ξ=u(1+v)/(1−uv),   η=v(1+u)/(1−uv),   S=1+ξ+η.

The Jacobian is J=(1+u)(1+v)/(1−uv)^3. The formal coefficient substitution identity is

    [u^p v^q] J F(ξ,η)
       = [ξ^p η^q](1+ξ)^(q+1)(1+η)^(p+1)F(ξ,η).               (4)

For completeness, apply the one-variable identity

    [t^r] (d/dt)(ct/(1−dt)) H(ct/(1−dt))
       = [w^r](c+dw)^(r+1)H(w)

first with t=u,c=1+v,d=v and H(w)=(1+w)F(w,v(1+w)); then extract v^q by η=v(1+ξ). The one-variable identity itself follows by testing H(w)=w^k and the binomial expansion. This proves (4).

Under this substitution Φ=ξ+η, and the prefactor in (2), divided by J, equals

    S (1+ξ)^(b−2)(1+η)^(a−2).

Consequently (2) and (4) give

    C_(a,b)(z^p,z^q)
      = p!q![ξ^p η^q] S exp(z(ξ+η))
                    (1+ξ)^(q+b−1)(1+η)^(p+a−1)
      = (1+∂_z)A_(p,q)(z).

The last equality follows directly from

    M_(K_(r,s))(z)=r![t^r] exp(zt)(1+t)^s.

The temporary negative exponents when a=1 or b=1 are valid formal series with constant term one; the final exponents q+b−1,p+a−1 are nonnegative. Cases p=0 or q=0 are included, as is p=q=0.

## 3. Arbitrary real-rooted inputs

By positive scaling assume f and g monic, and write

    f(z)=∏_(i=1)^p(z+α_i),   g(z)=∏_(j=1)^q(z+β_j),
    α_i,β_j≥0.

In Γ_(p,q)^(a,b), distinguish p of the p+a−1 blue-only columns and q of the q+b−1 red-only columns. Add the p edges from red row i to its distinct distinguished blue-only column with weight α_i; add the q edges from blue row j to its distinct distinguished red-only column with weight β_j. These are absent from the original graph, so there are no parallel edges. Call the resulting weighted board W.

Expand its matching enumerator by the chosen added edges. They have pairwise disjoint endpoints, including between the two types. If a subset of s α-edges and t β-edges is chosen, delete their endpoints. Among original edges the remaining board is exactly

    Γ_(p−s,q−t)^(a,b):
    red rows p−s; red-only columns q+b−1−t;
    blue rows q−t; blue-only columns p+a−1−s;
    common column unchanged.

No extra power of z occurs: z^(p+q−s−t−k) is the residual reversed exponent. Thus the coefficient of every squarefree product of α's and β's is precisely C_(a,b)(z^(p−s),z^(q−t)) by (3). Bilinearity and expansion of f,g prove

    C_(a,b)(f,g)=M_W.                                           (5)

All weights are nonnegative. The classical weighted Heilmann–Lieb theorem implies that the matching generating polynomial Z_W(t)=Σ_S w(S)t^|S| has only negative real zeros. Its reversal z^(p+q)Z_W(1/z) therefore has only real nonpositive zeros, with nonnegative coefficients. This proves the operator theorem. Zero weights and constant inputs cause no difficulty.

## 4. Passage to graphs and downward closure

Write the chromatic polynomial in its stable-partition falling-factorial expansion. Under graph join the corresponding coefficient sequences convolve: each independent block lies entirely in one factor, and unordered partitions in the two factors correspond bijectively to their union. After the sign reflection this says that the bilinear operation R_k ◇ R_l=R_(k+l) satisfies

    P_(G∨H)=P_G ◇ P_H.

If P_G=R_a Σ c_k(x+a)^{overline k}, its rising expansion is Σ c_k R_(a+k); likewise for H. Dividing the displayed join identity by R_(a+b) proves exactly

    B(P_(G∨H)/R_(a+b))
        =C_(a,b)(B(P_G/R_a),B(P_H/R_b)).                         (6)

It remains to explain why proving just the maximal clique quotient suffices. If Q=B(P_G/R_(j+1)), then

    B(P_G/R_j)=(z+j)Q+zQ'.                                      (7)

This operator preserves nonnegative coefficients and real nonpositive zeros for j≥0. One elementary proof, after separating Q=z^m H with H(0)≠0, is to use

    ((z+j)Q+zQ')/Q = z+j+m+Σ_i z/(z+λ_i),   λ_i>0,

when the negative roots are distinct: its derivative off its poles is 1+Σ_i λ_i/(z+λ_i)^2>0, giving one root on each intervening interval and the remaining roots on the negative end intervals (a root at zero is allowed if j+m=0). Repeated roots follow by perturbation/continuity; a constant H is immediate. Thus downward iteration from j=ω(G) proves all smaller positive clique sizes. It also proves ordinary tau-realness by the j=0 step.

For nonempty G,H, choose a=ω(G)≥1 and b=ω(H)≥1. Since ω(G∨H)=a+b, (6), the operator theorem, and (7) establish the complete clique-quotient property for their join. An empty factor leaves the other graph unchanged.

## 5. What this extends, and what it does not

Kang–Liu–Sun–Zhang, *Real-rootedness of the τ-polynomial under graph joins*, arXiv:2609.07457v1, Theorem 1.2 proves preservation for its unparameterized Lah-star product when both inputs vanish at zero. Theorems 3.2 and 4.1 realize that product by a bipartite matching board with a common column and weighted diagonal edges. Their Lemma 3.6 is the coefficient substitution (4). Primary full text inspected: https://arxiv.org/html/2609.07457v1 . Their Remark 2.1 distinguishes their product from BRW's Bell product.

Our parameters a,b≥1 supply additional columns, permitting weighted diagonal edges for **all** roots without requiring a zero root. The shifted operator (1), kernel (2), and rooted graph quotient identity (6) are essential; applying the ordinary join theorem directly to clique quotients would not justify the conclusion. At a=b=0, our full arbitrary-input matching construction fails precisely because there are too few private columns. No claim of preservation for arbitrary inputs at those parameters is made.

The weighted root-location input is Heilmann–Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190–232, DOI 10.1007/BF01877590. BRW conventions and the clique quotient motivation follow *Location of Zeros of Chromatic and Related Polynomials of Graphs*, Canadian Journal of Mathematics 46 (1994), 55–80, DOI 10.4153/CJM-1994-002-3.

## 6. Verification

`verify.py` independently computes (1) by triangular changes of polynomial basis and directly enumerates weighted board matchings by row/mask dynamic programming. It checks 160 cases with a,b in {(1,1),(1,2),(2,1),(2,3),(4,2)}, p,q from 0 through 3, and zero or rational nonnegative root magnitudes. Exact squarefree-factor real-root counts, with multiplicities, confirm every output. `certificate.json` and `run.log` record the results. These finite checks are not premises of the proof. A fresh independent AI review in `INDEPENDENT_REVIEW.md` found the theorem valid and independently checked 225 monomial identities and four factorized examples; its checker and log are retained. This is not human peer review or proof-assistant verification.


## 7. Classical composition corollaries

The complete clique-quotient class is also closed under disjoint union and exact clique sums. These are direct consequences of the classical BRW Bell-product preservation theorem, not additional new operator machinery.

Suppose G1 and G2 intersect in exactly a complete graph K_k, with no other identifications and no added cross edges. For k=0 this means disjoint union. Write ω1≥ω2. Every clique of the union lies in one of the factors, so ω(union)=ω1. The chromatic clique-sum formula gives

    P_union/R_ω1 = (P_G1/R_ω1)(P_G2/R_k),      R_0=1.

For k≥1 both displayed quotient Bell transforms have real nonpositive roots by hypothesis and downward closure. For k=0 the second factor is ordinary B(P_G2), supplied by downward closure through j=0. The BRW identity

    B(fg)=Σ_(r≥0) z^r B(f)^(r) B(g)^(r)/r!

and its preservation theorem give the maximal quotient property for the union, hence all smaller quotients. Empty factors are immediate. The operation must be an exact clique sum as specified; arbitrary cross edges are outside this argument.

Thus any already verified full-clique seed class may be closed under joins, disjoint unions, and exact clique sums. In particular the previously proved full-clique small-matching-component complement class and sufficiently padded triangle-free-complement class may be used as seeds. This is a composition statement, not an assertion that every previously studied attachment family is a full-clique seed. A theorem proved only for j≤r qualifies only when r≥ω(G). General uniform-cycle substitutions, paired-rooted bounded-j families, and partial co-bipartite ranges cannot silently be promoted to full-clique results. An edge-quotient theorem is sufficient for a triangle-free seed of clique number two, but not for graphs with larger cliques.


Release reproducibility: the guarded `run_all.py` checks file hashes, runs all checkers under optimized Python in a temporary directory, and compares regenerated exact certificates. `graph_check.py` additionally checks 44 small direct graph compositions through independent stable-partition enumeration; all clique-size quotients including j=0 pass exact sign and root counts. These finite checks are supporting evidence, not proof premises.
