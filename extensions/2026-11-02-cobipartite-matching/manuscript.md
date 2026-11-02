---
title: Matching Realizations of Edge Quotients for Co-bipartite Graphs
subtitle: Research note
date: 2026-11-02
documentclass: article
fontsize: 11pt
papersize: letter
geometry:
  - margin=0.9in
mainfont: Latin Modern Roman
mathfont: Latin Modern Math
colorlinks: true
linkcolor: black
urlcolor: blue
header-includes:
  - |
    \makeatletter
    \renewcommand{\maketitle}{%
      \begin{center}
        {\LARGE\@title\par}
        \vspace{0.6em}
        {\normalsize\@date\par}
      \end{center}
      \vspace{0.6em}
    }
    \makeatother
---

## Abstract

For a finite simple co-bipartite graph $G$ on $n$ vertices, write
$P_G(x)=(-1)^n\chi_G(-x)$, where $\chi_G$ is its chromatic polynomial.
When $n\geq3$, the Bell transform of $P_G(x)/[x(x+1)]$ is exactly a
reversed matching enumerator of $K_{n-2,n-1}$ with an embedded copy of the
complement edges deleted. The Heilmann--Lieb theorem therefore gives only
real nonpositive zeros for this transformed quotient. Bell product
preservation then implies that attaching $G$ along an edge to any ordinary
$\tau$-real graph preserves ordinary $\tau$-realness. A bounded extension
holds for clique sizes at most the larger side of a chosen bipartition of
the complement. This note proves these statements, records exact finite
checks, and does not assert historical novelty or unrestricted edge closure.

## 1 Notation and conventions

All graphs are finite and simple. A graph is **co-bipartite** if its vertex
set is the union of two cliques, equivalently if its complement is bipartite.
For a graph $G$ of order $n$, put
$$
P_G(x)=(-1)^n\chi_G(-x),\qquad
R_j(x)=\prod_{i=0}^{j-1}(x+i),\qquad R_0(x)=1.
$$
The falling factorial is $(x)_j=x(x-1)\cdots(x-j+1)$, with $(x)_0=1$.

The **Bell transform** is the linear map $\mathcal B:\mathbb R[x]\to
\mathbb R[z]$ determined by
$$
\mathcal B(x^d)=T_d(z),\qquad
T_d(z)=\sum_{q=0}^d
\left\{\begin{matrix}d\\q\end{matrix}\right\}z^q,
\qquad T_0(z)=1,
$$
where the braces denote Stirling numbers of the second kind. Thus the
$T_d$ are the Touchard polynomials and
$$
\sum_{d\geq0}T_d(z)\frac{u^d}{d!}
=\exp\bigl(z(e^u-1)\bigr).
$$
Throughout this note, **ordinary $\tau$-realness** means that
$\Theta_G(z):=\mathcal B(P_G)(z)$ has only real zeros. This is the Bell
normalization; there is no factorial rescaling of its monomial
coefficients. In terms of the signed convention of Brenti--Royle--Wagner
[1], the exact relation is
$$
\Theta_G(z)=(-1)^n\tau_{\mathrm{BRW}}(G;-z).
$$
Thus real-rootedness is the same property in the two conventions.
The coefficients of $P_G$ are nonnegative, by the usual
alternating-sign property of chromatic coefficients. Consequently
$\Theta_G$ has nonnegative coefficients, so its real zeros, if all its
zeros are real, are nonpositive. Constant nonzero polynomials are regarded
as real-rooted.

For a bipartite graph $J$ with specified part sizes $a\leq b$, let
$m_\ell(J)$ be its number of matchings of size $\ell$, including
$m_0(J)=1$. Define the reversed matching enumerator by
$$
M_J(z)=\sum_{\ell=0}^a m_\ell(J)z^{a-\ell}.
$$
Its exponent normalization uses the size $a$ of the specified first part,
not the matching number. Isolated vertices remain part of the graph.

## 2 Exact edge quotient realization

**Theorem 1.** Let $G$ be a co-bipartite graph on $n\geq3$ vertices, and
write $H=\overline G$. Choose a bipartition $A\sqcup B$ of $H$ with
$1\leq |A|\leq |B|$. If $H$ is edgeless, choose $|A|=1$ and $|B|=n-1$.
Embed $H$ in $K_{n-2,n-1}$ with $A$ in the first part and $B$ in the
second, adding unused vertices to fill the parts, and set
$$
J=K_{n-2,n-1}\setminus E(H).
$$
Here only the embedded edges of $H$ are deleted. Then
$$
\boxed{\mathcal B\!\left(\frac{P_G}{R_2}\right)(z)=M_J(z).}
$$
In particular, this transformed quotient has only real nonpositive zeros.
For the remaining edge-containing case $n=2$, necessarily $G=K_2$, and
the quotient is the constant $1$.

The embedding is possible because
$$
|A|\leq\lfloor n/2\rfloor\leq n-2,
\qquad |B|\leq n-1.
$$
When $H$ has edges, both parts are nonempty; isolated complement vertices
may be assigned subject to the stated part-size conditions. The assertion
does not require $G$ to be connected or to have no isolated vertices.

### 2.1 Chromatic expansion by complement matchings

Every independent set in $G$ has at most two vertices. A partition of
$V(G)$ into independent blocks is therefore uniquely specified by a
matching of $H$: its edges give the two-element blocks, and its unmatched
vertices give singleton blocks. A matching of size $k$ gives $n-k$ blocks.
Assigning distinct colors to these blocks yields
$$
\chi_G(x)=\sum_{k\geq0}m_k(H)(x)_{n-k},
\qquad
P_G(x)=\sum_{k\geq0}(-1)^k m_k(H)R_{n-k}(x).
$$
The sign follows from $(-x)_{n-k}=(-1)^{n-k}R_{n-k}(x)$.
Since $k\leq\lfloor n/2\rfloor\leq n-2$, every summand in the last
expression is divisible by $R_2$.

### 2.2 A Bell transform identity

For integers $c\geq1$ and $r\geq0$, with the empty product interpreted as
$1$, one has
$$
\mathcal B\!\left(\prod_{i=0}^{r-1}(x+c+i)\right)(z)
=\sum_{\ell=0}^r
\binom r\ell\binom{r+c-1}\ell\ell!\,z^{r-\ell}.
$$
To prove this identity, take the exponential generating function in $r$.
All operations below are formal power-series operations, so no analytic
convergence assumption is needed. The rising-factorial generating
function and the Touchard identity give
$$
\begin{aligned}
\sum_{r\geq0}\mathcal B\!\left(\prod_{i=0}^{r-1}(x+c+i)\right)
\frac{u^r}{r!}
&=\mathcal B\bigl((1-u)^{-x-c}\bigr)\\
&=(1-u)^{-c}\exp\!\left(\frac{zu}{1-u}\right).
\end{aligned}
$$
The coefficient of $z^d u^r$ on the right is
$\binom{c+r-1}{r-d}/d!$ for $0\leq d\leq r$. Multiplying by $r!$ and
setting $\ell=r-d$ proves the formula.

The complete bipartite graph has matching counts
$$
m_\ell(K_{a,b})=\binom a\ell\binom b\ell\ell!.
$$
Hence, with $a=n-2$, $b=n-1$, $c=2$, and $r=a-k$, the formula implies
$$
\mathcal B\!\left(\frac{P_G}{R_2}\right)
=\sum_{k\geq0}(-1)^k m_k(H)M_{K_{a-k,b-k}}.
$$
Each enumerator on the right is normalized to first-part size $a-k$.

### 2.3 Forbidden edge inclusion and exclusion

Count the $\ell$-edge matchings of $K_{a,b}$ that avoid the embedded edges
of $H$. In inclusion--exclusion, a specified set of forbidden edges can
occur in such a matching only if it is itself a matching. A forbidden
matching of size $k$ leaves a complete bipartite graph $K_{a-k,b-k}$ on
the unused vertices. Therefore
$$
m_\ell(J)=\sum_{k=0}^{\ell}(-1)^k m_k(H)
m_{\ell-k}(K_{a-k,b-k}).
$$
Multiplying by $z^{a-\ell}$ and summing over $\ell$ gives
$$
M_J(z)=\sum_{k\geq0}(-1)^k m_k(H)M_{K_{a-k,b-k}}(z).
$$
Indeed, writing $q=\ell-k$ changes the exponent to $a-k-q$, exactly the
exponent in the smaller-board enumerator. There is no additional power
of $z$. Comparison with the preceding Bell transform proves the claimed
polynomial identity.

## 3 Real zeros and universal edge attachment

The usual matching polynomial of a graph $J$ of order $N$ is
$$
\mu_J(y)=\sum_{\ell\geq0}(-1)^\ell m_\ell(J)y^{N-2\ell}.
$$
The Heilmann--Lieb theorem states that this polynomial has only real zeros
[2]. In the edge construction, $N=2a+1$, and direct substitution gives
$$
\mu_J(y)=(-1)^a yM_J(-y^2).
$$
If $z_0\ne0$ is a zero of $M_J$, choose a complex number $y_0$ with
$y_0^2=-z_0$. Then $y_0\ne0$ and $\mu_J(y_0)=0$, so $y_0$ is real and
$z_0=-y_0^2<0$. Zero roots of $M_J$ are allowed. This finishes the
root assertion of Theorem 1. For $G=K_2$, one has $P_G=R_2$ directly.

For polynomials $f$ and $g$, define
$$
(f\star g)(z)=\sum_{k\geq0}\frac{z^k}{k!}f^{(k)}(z)g^{(k)}(z),
$$
a finite sum. The Bell product identity is
$$
\mathcal B(pq)=\mathcal B(p)\star\mathcal B(q).
$$
It follows, for example, by applying the Touchard generating function to
$p=e^{ux}$ and $q=e^{vx}$ formally and comparing coefficients of $u$ and
$v$. We use the accompanying preservation theorem: if $f$ and $g$ have
nonnegative coefficients and only real nonpositive zeros, then so does
$f\star g$. This is the Bell-normalized form of Brenti--Royle--Wagner
Proposition 5.4 [1].

**Corollary 2.** Let $G$ be an edge-containing co-bipartite graph, and let
$F$ be any ordinary $\tau$-real graph. Suppose their intersection consists
of exactly the two vertices and the edge of a common $K_2$. Form their
union with no other vertex identifications and no additional edges between
their remaining vertices. Then $G\cup F$ is ordinary $\tau$-real.

**Proof.** The chromatic clique-sum identity [1] gives
$$
\chi_{G\cup F}(x)=\frac{\chi_G(x)\chi_F(x)}{(x)_2},
\qquad
P_{G\cup F}(x)=\frac{P_G(x)P_F(x)}{R_2(x)}.
$$
Consequently
$$
\Theta_{G\cup F}
=\mathcal B(P_G/R_2)\star\Theta_F.
$$
Both factors have nonnegative coefficients and only real nonpositive
zeros, by Theorem 1 and the definition of ordinary $\tau$-realness.
Product preservation proves the claim. Taking $F=K_2$, for which
$\Theta_F(z)=z^2+2z$, also shows that $G$ itself is ordinary
$\tau$-real. $\square$

## 4 A bounded extension to larger cliques

**Theorem 3.** Retain $n\geq3$ and a chosen complement bipartition
$A\sqcup B$ as in Theorem 1, and write $s=|A|\leq t=|B|$. For every
integer $j$ with $1\leq j\leq t$, set
$$
a=n-j,\qquad b=n-1,\qquad
J_j=K_{a,b}\setminus E(H),
$$
embedding $A$ in the first part and $B$ in the second. Then
$$
\mathcal B\!\left(\frac{P_G}{R_j}\right)(z)=M_{J_j}(z),
\qquad
\mu_{J_j}(y)=(-1)^{n-j}y^{j-1}M_{J_j}(-y^2).
$$
In particular, the transformed quotient has only real nonpositive zeros,
and attachment of $G$ along a $j$-clique to any ordinary $\tau$-real graph
preserves ordinary $\tau$-realness, with the same restrictions on the
intersection and union as in Corollary 2.

**Proof.** The bound $j\leq t$ implies $s\leq n-j=a$, while
$t\leq n-1=b$. Thus the required embedding exists. Every complement
matching has size $k\leq s\leq a$, so $n-k\geq j$ and every term
$R_{n-k}$ in the chromatic expansion is divisible by $R_j$. Apply the
Bell identity of Section 2.2 with $c=j$ and $r=n-j-k=a-k$; then
$r+c-1=b-k$. The same inclusion--exclusion proof yields $M_{J_j}$.
Since $J_j$ has $a+b=2a+j-1$ vertices, its matching polynomial has the
displayed sign and factor $y^{j-1}$. The Heilmann--Lieb argument again
gives the zeros. Finally, for a common $j$-clique the chromatic identity
gives $P_{G\cup F}=P_GP_F/R_j$, and Bell product preservation applies.
$\square$

The bound refers to the larger side of the **chosen complement
bipartition**, not to an arbitrary clique size of $G$. A clique containing
vertices from both sides may have more than $t$ vertices. No attachment
claim for those larger intersections follows from this embedding proof.
The $n=2$ edge boundary is handled separately in Theorem 1, not by this
bounded extension.

## 5 An infinite family without join or clique separation

A **nontrivial join decomposition** is a partition into two nonempty
vertex sets with every possible edge between them. A **clique separator**
is a clique whose deletion leaves a disconnected graph.

**Corollary 4.** For every $m\geq4$, the graph
$G=\overline{C_{2m}}$ satisfies Theorem 1 and has neither a nontrivial join
decomposition nor a clique separator.

**Proof.** The even cycle $C_{2m}$ is bipartite, so $G$ is co-bipartite.
Its complement is connected, excluding a nontrivial join decomposition.
Suppose that a clique $K$ of $G$ disconnects $G$ when deleted. The set $K$
is independent in $C_{2m}$, so $|K|\leq m$ and at least $m\geq4$ vertices
remain. Distinct components of $G-K$ have all possible cross edges in
$C_{2m}$. Three or more components would therefore give a triangle in
the cycle, which is impossible. If there are exactly two components with
vertex sets $X,Y$, the cycle's maximum degree $2$ forces
$|X|,|Y|\leq2$. At least four vertices remain, so both sets have size $2$,
and their cross edges give a $C_4$ subgraph of $C_{2m}$. A cycle of length
at least $8$ contains no such subgraph. This contradiction proves the
claim. $\square$

This corollary excludes these two decomposition mechanisms for the stated
family; it does not assert exclusion from every earlier closure family.

## 6 Exact verification

The accompanying verifier performs exact integer polynomial and matching
computations, together with rational real-root isolation. From the
directory containing the supplied verification files, run

```text
python verify.py
```

The certificate records **165 exact cases**: all 147 edge-containing
co-bipartite graphs in the graph atlas through seven vertices, and 18
deterministic examples on 8--12 vertices obtained as complements of paths,
even cycles, double stars, and complete bipartite graphs. For $n\geq3$,
three constructions agree: stable-partition chromatic computation followed
by the Bell transform, direct matching dynamic programming on the allowed
board, and forbidden-board matching inclusion--exclusion. The $n=2$
case is a separate direct check of $G=K_2$ and quotient $1$.

Across the $n\geq3$ records, a further **663 bounded-$j$ quotient
identities and exact root checks** pass for the recorded complement
bipartitions. These computations support the identities and help detect
normalization or implementation errors; they are not premises of the
infinite-family proofs.

## 7 Scope and provenance

The graph-specific mechanism has two parts: complement matchings encode
all independent-set partitions, and the bipartite complement embeds in a
rectangular matching board. Independent sets of size at least three
destroy the matching encoding. A triangle-free but nonbipartite complement
still gives the encoding, but not the required board embedding. The
argument therefore does not establish unrestricted ordinary edge closure.

Brenti--Royle--Wagner Proposition 5.12 concerns intersections of at most one
vertex; Proposition 5.13 gives a different chromatic-root sufficient
criterion for clique attachment [1]. This note makes no claim that its
examples fail that criterion, that this class strictly extends every
earlier closure class, or that the matching realization is absent from
the literature. Historical novelty remains unknown, and overlap with
Mu--Shen--Xu remains unassessed.

This research note is dated 2026-11-02, and its proof was developed with
AI assistance. A separate, independent AI review checked the matching
correspondence, signs, Bell identity,
inclusion--exclusion exponents, embedding bounds, matching-polynomial
conversion, and bounded clique extension, without finding a mathematical
correction to the main identity. That review is not human peer review or
proof-assistant verification.

## References

[1] Francesco Brenti, Gordon F. Royle, and David G. Wagner.
*Location of Zeros of Chromatic and Related Polynomials of Graphs*.
Canadian Journal of Mathematics **46**(1), 55--80 (1994).
[doi:10.4153/CJM-1994-002-3](https://doi.org/10.4153/CJM-1994-002-3).

[2] Ole J. Heilmann and Elliott H. Lieb.
*Theory of monomer-dimer systems*.
Communications in Mathematical Physics **25**, 190--232 (1972).
[doi:10.1007/BF01877590](https://doi.org/10.1007/BF01877590).
