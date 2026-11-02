---
title: "Clique attachment for complete bipartite graphs with one edge removed"
date: "2 November 2026"
lang: en
---

## Abstract

For every $a,b\geq 2$, let $H_{a,b}=K_{a,b}-e$, where exactly one cross-edge is removed. We prove that the Bell transform of the unsigned chromatic quotient $P_{H_{a,b}}/[x(x+1)]$ has only real nonpositive zeros. It follows that ordinary attachment of $H_{a,b}$ along any complete intersection to any $\tau$-real graph preserves $\tau$-reality. The proof identifies the quotient with a bilinear weighted-matching operator and derives the matching and chromatic generating functions independently. A structural corollary extends the construction to joins with one distinguished cross-edge deleted, under first-quotient real-rootedness hypotheses, with attachment restricted to cliques of size at most two.

This is an ordinary mathematical proof manuscript prepared with AI assistance. It does not assert historical priority, human peer review, proof-assistant verification, or a resolution of the general $\tau$ clause of Brenti--Royle--Wagner Conjecture 6.5.

## 1 Statement and conventions

All graphs are finite and simple. For a graph $J$ on $n$ vertices, write

$$
P_J(x)=(-1)^n\chi_J(-x),\qquad
R_k(x)=x(x+1)\cdots(x+k-1),\qquad R_0(x)=1.
$$

Let $\mathcal B$ be the linear Bell transform defined by

$$
\mathcal B((x)_j)=z^j,
\qquad (x)_j=x(x-1)\cdots(x-j+1),\qquad (x)_0=1.
$$

Equivalently, $\mathcal B(x^n)=T_n(z)$, where $T_n$ is the Touchard polynomial. Put $T_J(z)=\mathcal B(P_J)(z)$. In the original Brenti--Royle--Wagner normalization,

$$
T_J(z)=(-1)^n\tau_{\mathrm{BRW}}(J,-z),
$$

so real-rootedness agrees with original BRW $\tau$-reality [1]. A graph is called $\tau$-real when this polynomial has only real zeros.

**Theorem 1.** For every $a,b\geq2$, let $H=H_{a,b}=K_{a,b}-e$, with exactly one cross-edge removed. Then $\mathcal B(P_H/R_2)$ has only real nonpositive zeros. Consequently $\mathcal B(P_H/R_k)$ has only real nonpositive zeros for $k=0,1,2$. If $G$ is any $\tau$-real graph and $G\cap H$ is complete, their ordinary union is $\tau$-real.

In particular, edge attachment retains the shared edge and adds no edges between the exclusive sides. Since $H$ is bipartite and has an edge, its complete intersections have size at most two. The empty intersection, denoted $K_0$, is allowed.

The two substantive ingredients are an exact chromatic quotient identity and an all-degree weighted matching preserver. Both are proved below; neither relies on finite graph searches. The external root-preservation inputs are the weighted matching theorem of Heilmann--Lieb [2] and the Bell-product theorem of BRW [1, Propositions 5.2 and 5.4], used in its reflected, nonpositive-root form.

## 2 The bilinear matching operator

For $r,s\geq0$, define a bipartite graph $\Gamma_{r,s}$. Its left side consists of red vertices $R_i$, blue vertices $B_j$, and core vertices $0,1,3$; its right side consists of red vertices $R'_i$, blue vertices $B'_j$, and core vertices $2,4$. Here $1\leq i\leq r$ and $1\leq j\leq s$. The edges are

- $R_iB'_j$ and $B_jR'_i$ for every $i,j$;
- $R_i2$, $R_i4$, $R'_i1$, $R'_i3$ for every $i$;
- $B_j2$, $B'_j0$, $B'_j1$, $B'_j3$ for every $j$;
- the core path edges $12$, $23$, $34$.

All baseline edges have weight one. Define

$$
M_{r,s}(z)=\sum_{M\text{ matching in }\Gamma_{r,s}}
z^{r+s+2-|M|},
\qquad \mathcal C(z^r,z^s)=M_{r,s}(z),
$$

and extend $\mathcal C$ bilinearly. The right side of $\Gamma_{r,s}$ has $r+s+2$ vertices, so the exponent is always nonnegative.

For

$$
f(z)=\prod_{i=1}^r(z+\alpha_i),\qquad
g(z)=\prod_{j=1}^s(z+\beta_j),\qquad \alpha_i,\beta_j\geq0,
$$

add diagonal edges $R_iR'_i$ of weights $\alpha_i$ and $B_jB'_j$ of weights $\beta_j$. These edges are pairwise vertex-disjoint and absent from the baseline graph.

Condition on exactly which diagonals a matching uses. Deleting their endpoints leaves precisely $\Gamma_{r-|I|,s-|J|}$, with unchanged remaining baseline weights and no vertex remnants. Its exponent is

$$
\begin{aligned}
r+s+2-|I|-|J|-|M_{\mathrm{remaining}}|
&=(r-|I|)+(s-|J|)+2\\
&\qquad{}-|M_{\mathrm{remaining}}|.
\end{aligned}
$$

Expanding $f$ and $g$ into monomials therefore proves the polynomial identity

$$
\mathcal C(f,g)=\sum_{M\text{ matching in augmented }\Gamma_{r,s}}
\operatorname{weight}(M)z^{r+s+2-|M|}.
$$

For a graph with nonnegative edge weights, the Heilmann--Lieb theorem [2] gives real-rootedness of the signed matching polynomial

$$
\mu(t)=\sum_M(-1)^{|M|}\operatorname{weight}(M)t^{|V|-2|M|}.
$$

Consequently its matching-size polynomial

$$
Z(y)=\sum_M\operatorname{weight}(M)y^{|M|}
$$

has only negative real zeros, and $z^N Z(1/z)$ has only nonpositive real zeros whenever $N\geq\deg Z$. This implication follows from $\mu(t)=t^{|V|}Z(-1/t^2)$, paired real roots of $\mu$, and reciprocation. In our case $\deg Z\leq N=r+s+2$, since the right side has exactly $r+s+2$ vertices even after diagonal edges are added.

Thus $\mathcal C$ preserves nonpositive real-rootedness in both inputs. Scaling handles arbitrary nonzero leading coefficients; constants, repeated roots and zero roots are included. The diagonal-edge root-lifting method has precedent in the graph-join work of Kang--Liu--Sun--Zhang [3]; the graph and kernel used here are different.

## 3 The matching generating function

Put

$$
\begin{gathered}
D=1-uv,\qquad C_0=(1+u)(1+v),\\
\xi=\frac{u(1+v)}D,\qquad \eta=\frac{v(1+u)}D,\\
W=1+\xi+\eta=\frac{C_0}D,\qquad
H=(1+\xi)(1+\eta)=\frac{C_0}{D^2},\qquad \Phi=\xi+\eta.
\end{gathered}
$$

In this section $H$ is the displayed auxiliary formal series, not a graph. We will prove

$$
\sum_{r,s\geq0}M_{r,s}(z)\frac{u^r}{r!}\frac{v^s}{s!}
=D^{-1}\exp(z\Phi)\,\mathcal P(\xi,\eta,z),\tag{M}
$$

where

$$
\mathcal P=z^2HW^3+zW^2(6H-2W-1)+W(6H-4W-1).
$$

### 3.1 A formal moment identity

Let ordinary endpoint variables be $a,b$ for $R,B$ and $a',b'$ for $R',B'$. Define the purely formal linear functional $\mathbb E_{u,v}$ by

$$
\mathbb E_{u,v}[a^i(a')^jb^k(b')^\ell]
=\delta_{ij}\delta_{k\ell}\,i!k!u^iv^k.
$$

It satisfies the formal power-series identity

$$
\begin{aligned}
&\mathbb E_{u,v}\exp(ab'+ba'+pa+qb+p'a'+q'b')\\
&\qquad=D^{-1}\exp\left(
\frac{upp'+vqq'+uv(pq'+qp')}{D}\right).
\end{aligned}\tag{F}
$$

For a direct purely formal verification, first contract $a,a'$: the result is

$$
\exp(upp')\exp\bigl(ubb'+(q+up)b+(q'+up')b'\bigr).
$$

The one-pair identity

$$
\mathbb E_v\exp(hbb'+Pb+Qb')
=(1-hv)^{-1}\exp\left(\frac{vPQ}{1-hv}\right)
$$

follows by expanding and summing

$$
\sum_{k\geq0}\binom{k+\ell}{k}(hv)^k=(1-hv)^{-\ell-1}
$$

for each leftover degree $\ell$. Applying it with $h=u$ gives exactly (F). There are no analytic integrations or convergence assumptions.

At $p=q=p'=q'=t$, the right side of (F) is

$$
B_0=D^{-1}\exp(t^2\Phi).
$$

Differentiating (F) in its four source variables shows that, after division by $B_0$, the endpoint moments have means

$$
a,a':\ t\xi;\qquad b,b':\ t\eta,
$$

zero same-side centered covariances, and cross-side centered covariance matrix

$$
[a,b]\text{ against }[a',b']:\qquad
D^{-1}\begin{pmatrix}u&uv\\uv&v\end{pmatrix}.
$$

Higher centered moments are sums over pairings using these covariances. This follows directly by differentiating the exponential of the displayed quadratic form, and is the finite polynomial Wick rule; no probabilistic assumption is used.

### 3.2 Integrating the five vertex core

Temporarily use monomer variable $t$ at every vertex. The ordinary-vertex matching exponential generating function is

$$
\exp\bigl(t(a+a'+b+b')+ab'+ba'\bigr).
$$

A core vertex's monomer polynomial is $t$ plus the sum of its ordinary neighbors' variables. The core left monomer polynomials are

$$
m_0=t+b',\qquad m_1=m_3=t+a'+b',
$$

and the core right monomer polynomials are

$$
m_2=t+a+b,\qquad m_4=t+a.
$$

The core matching polynomial, including its three internal edges, is

$$
m_0\bigl[m_1m_2m_3m_4+m_3m_4+m_1m_4+m_1m_2+1\bigr].\tag{K}
$$

Indeed, the three middle terms correspond to the three choices of one core edge, and the last term to the matching $\{12,34\}$. Applying $\mathbb E_{u,v}$ to the product of the ordinary exponential generating function and (K) gives the exponential generating function of the full monomer matching polynomials, with coefficients $u^r/r!$ and $v^s/s!$.

The source identity replaces the core left monomers by means

$$
t(1+\eta),\quad tW,\quad tW,
$$

and the right monomers by

$$
tW,\quad t(1+\xi).
$$

For every core left-right pair, its effective edge weight is its original core edge weight, zero or one, plus the covariance of its monomer linear forms. The resulting $3$-by-$2$ matrix is

$$
\begin{pmatrix}
\eta&\xi\eta/W\\
W&\xi\\
W&1+\xi
\end{pmatrix}.\tag{E}
$$

For example, $uv/D=\xi\eta/W$. Same-side covariances vanish, so the finite Wick rule is exactly the matching expansion for this effective core graph.

The empty core matching contributes $t^5HW^3$. The sum of one-edge contributions is

$$
t^3W^2(6H-2W-1),
$$

and the sum of two-edge contributions is

$$
tW(6H-4W-1).
$$

These are expansions of the six entries in (E). The original graph has $2r+2s+5$ vertices, so its monomer matching polynomial is $tM_{r,s}(t^2)$. Dividing the full exponential generating function by $t$ and putting $z=t^2$ proves (M).

Although (E) uses a denominator $W$, it cancels from $\mathcal P$; all operations are formal at $\xi=\eta=0$. No limiting root argument or unproved family recurrence enters (M).

## 4 The independent chromatic generating function

Distinguish the two endpoints of the missing edge. Remove them temporarily, leaving $K_{a-1,b-1}$. If the remaining left and right vertices use $i$ and $j$ distinct colors respectively, these color sets are disjoint. The missing-edge endpoints may choose their colors independently in $(q-j)(q-i)$ ways.

For the auxiliary exponential generating function only, extend $H_{a,b}=K_{a,b}-e$ to $a,b\geq1$; these graphs need not contain an edge until after the two differentiations below. Use exponential variables $U,V$ for the two remaining vertex classes. Put

$$
X=e^U-1,\qquad Y=e^V-1,\qquad A=1+X+Y.
$$

The ordinary $K_{a-1,b-1}$ coloring exponential generating function is $A^q$. Marking the numbers $i,j$ by $X\,\partial/\partial X$ and $Y\,\partial/\partial Y$ gives

$$
\sum_{r,s\geq0}\chi_{H_{r+1,s+1}}(q)\frac{U^r}{r!}\frac{V^s}{s!}
=q^2A^{q-1}+q(q-1)XYA^{q-2}.\tag{C1}
$$

One can verify directly: applying $(q-X\,\partial/\partial X)(q-Y\,\partial/\partial Y)$ to $A^q$ simplifies to the displayed expression.

Reflect $q=-x$ and $U,V$ to $-U,-V$. Two distinguished endpoints contribute an even sign, so with

$$
X=e^{-U}-1,\qquad Y=e^{-V}-1,\qquad A=e^{-U}+e^{-V}-1,
$$

the unsigned exponential generating function is

$$
x^2A^{-x-1}+x(x+1)XYA^{-x-2}.
$$

Differentiate once in each of $U,V$. This now indexes $a=r+2,b=s+2$, for which an edge always exists. Divide by $R_2=x(x+1)$; the exact quotient exponential generating function is

$$
e^{-U-V}A^{-x-4}
\bigl[(x+1)A(x+2-A)+(x+2)(x+3)XY\bigr].\tag{C2}
$$

All coefficients are polynomials in $x$. Division is legitimate because every indexed graph has an edge. Identity (C2) can also be verified by direct formal differentiation.

Apply $\mathcal B$ coefficientwise. For formal $R=A^{-1}$, the identities

$$
\begin{aligned}
\mathcal B(R^x)&=\exp(z(R-1)),\\
\mathcal B(xR^x)&=zR\exp(z(R-1)),\\
\mathcal B(x^2R^x)&=(z^2R^2+zR)\exp(z(R-1))
\end{aligned}
$$

follow by expanding the exponential and the defining Bell transform. Thus (C2) becomes

$$
\begin{aligned}
&e^{-U-V}A^{-4}\exp\bigl(z(A^{-1}-1)\bigr)\\
&\quad\times\bigl[A(z^2A^{-2}+4zA^{-1}+2)
-A^2(zA^{-1}+1)\\
&\hspace{4.9em}{}+XY(z^2A^{-2}+6zA^{-1}+6)\bigr].
\end{aligned}\tag{C3}
$$

Now put $u=e^U-1$, $v=e^V-1$. Then

$$
e^{-U-V}=\frac1{C_0},\qquad
X=-\frac{u}{1+u},\qquad Y=-\frac{v}{1+v},\qquad A=\frac D{C_0}.
$$

Substitution into (C3) yields

$$
\begin{aligned}
\exp(z\Phi)\biggl[
&\frac{z^2C_0^4}{D^6}
+\frac{zC_0^2\bigl((4+2uv)C_0-D^2\bigr)}{D^5}\\
&{}+\frac{C_0\bigl((2+4uv)C_0-D^2\bigr)}{D^4}
\biggr].
\end{aligned}
$$

Using $W=C_0/D$ and $H=C_0/D^2$, this expression is exactly $D^{-1}\exp(z\Phi)\mathcal P(\xi,\eta,z)$, the matching exponential generating function (M).

Composition $u=e^U-1$ and $v=e^V-1$ has Stirling coefficients:

$$
\frac{(e^U-1)^i}{i!}=\sum_{r\geq i}S(r,i)\frac{U^r}{r!},
$$

where $S(r,i)$ are Stirling numbers of the second kind. It follows coefficient by coefficient that

$$
\begin{aligned}
\mathcal B(P_{H_{a,b}}/R_2)
&=\sum_{i,j}S(a-2,i)S(b-2,j)M_{i,j}\\
&=\mathcal C(T_{a-2},T_{b-2}).
\end{aligned}\tag{Q}
$$

This is the exact graphic identity needed for Theorem 1.

## 5 Real roots and clique attachment

Touchard polynomials $T_n$ have only real nonpositive zeros, including $T_0=1$. This follows inductively from

$$
T_{n+1}=z(T_n+T'_n)
$$

and the standard Rolle/interlacing argument. Apply the preservation result in Section 2 to (Q). It proves the edge quotient assertion for every $a,b\geq2$.

We use the reflected Bell-product theorem [1, Propositions 5.2 and 5.4] in the following form: if $\mathcal B(F)$ and $\mathcal B(G)$ have only real nonpositive zeros, then so does $\mathcal B(FG)$.

Multiplication of an $x$-polynomial by $x+c$ corresponds under $\mathcal B$ to

$$
L_c=z\frac{d}{dz}+z+c.
$$

For $c\geq0$, $L_c$ preserves nonpositive real-rootedness; equivalently, use the Bell-product theorem with $\mathcal B(x+c)=z+c$. Multiplying back $x+1$, then $x$, proves the quotient statements $k=1,0$.

Every $H_{a,b}$ is bipartite and has an edge, so its clique number is two. If $G\cap H=K_k$, with $k\leq2$, the ordinary chromatic clique formula [1, Proposition 1.1] gives

$$
P_{G\cup H}=P_G(P_H/R_k).
$$

The Bell-product theorem applies to $\mathcal B(P_G)$ and $\mathcal B(P_H/R_k)$, proving $\tau$-reality of the union. Real-rooted $\mathcal B(P_G)$ has nonpositive roots because its coefficients are nonnegative. This completes the proof of Theorem 1.

## 6 A structural corollary for a join with one edge deleted

The join of two vertex-disjoint graphs is obtained by adding every edge between their vertex sets.

**Corollary 2.** Let $G_1,G_2$ be nonempty vertex-disjoint graphs. Add one new isolated vertex $u$ to $G_1$ and one new isolated vertex $v$ to $G_2$. Join the two enlarged graphs, then delete only $uv$, and call the resulting graph $H$. Write

$$
P_i(x)=(-1)^{|V(G_i)|}\chi_{G_i}(-x),\qquad
\rho_i=\mathcal B(P_i/x).
$$

If both $\rho_i$ have only real nonpositive zeros, then

$$
q_H=\mathcal B\bigl(P_H/[x(x+1)]\bigr)
$$

has only real nonpositive zeros. Consequently $H$ may be attached along an edge, or a clique of size zero or one, to any $\tau$-real graph while preserving $\tau$-reality. Moreover,

$$
\rho_H=\mathcal B(P_H/x)=L_1q_H
$$

again has only real nonpositive zeros, so the construction may be iterated on graphs satisfying this stronger first-quotient hypothesis.

The graph $H$ may have clique number greater than two. This corollary does not prove arbitrary larger-clique attachment for $H$, and it does not replace first-quotient real-rootedness of $G_1,G_2$ by ordinary $\tau$-reality.

### 6.1 The exact bilinear bridge

Define $\mathcal J$ bilinearly by

$$
\mathcal J(R_i,R_j)=R_{i+j}.
$$

For actual unsigned chromatic polynomials,

$$
\mathcal J(P_G,P_K)=P_{G\vee K}.
$$

This follows from multiplication of $\sigma$-polynomials under join and the signed rising-factorial expansion [3, Proposition 2.2 and its proof].

The full joined graph before deletion has polynomial $\mathcal J(xP_1,xP_2)$. Contracting its distinguished edge $uv$ gives the cone over $G_1\vee G_2$, whose unsigned polynomial is $x\,\mathcal J(P_1,P_2)(x+1)$. Here $\mathcal J(P_1,P_2)(x+1)$ means evaluation of the resulting polynomial at $x+1$. Unsigned deletion--contraction therefore gives

$$
P_H=\mathcal J(xP_1,xP_2)-x\,\mathcal J(P_1,P_2)(x+1).\tag{S1}
$$

The negative sign is essential: the contracted graph has one fewer vertex.

For arbitrary $P,Q$ divisible by $x$, the right side of (S1) is bilinear in $P,Q$. Its quotient by $R_2$ is a polynomial: on the basis $P=x^p,Q=x^q$, $p,q\geq1$, it is the actual quotient for $K_{p+1,q+1}$ minus one edge; divisibility extends by bilinearity.

For these basis inputs, the already proved graphic kernel identity (Q) reads

$$
\begin{aligned}
&\mathcal B\left(
\frac{\mathcal J(x^{p+1},x^{q+1})-x\,\mathcal J(x^p,x^q)(x+1)}{R_2}
\right)\\
&\qquad=\mathcal C(T_{p-1},T_{q-1}).
\end{aligned}
$$

Since $x^p$ for $p\geq1$ is a basis of $x\mathbb R[x]$, bilinearity now proves, for all $P,Q\in x\mathbb R[x]$,

$$
\begin{aligned}
&\mathcal B\left(
\frac{\mathcal J(xP,xQ)-x\,\mathcal J(P,Q)(x+1)}{R_2}
\right)\\
&\qquad=\mathcal C\bigl(\mathcal B(P/x),\mathcal B(Q/x)\bigr).
\end{aligned}\tag{S2}
$$

Apply (S2) to the two actual graph polynomials and use the bilinear matching preserver of Section 2. This proves $q_H$ real-rooted. Multiplication back by $x+1$ gives $\rho_H$ via $L_1$, and the Bell-product theorem gives attachment along $K_k$ for $k\leq2$, as in Section 5.

The complete-bipartite-minus-edge family is recovered by choosing edgeless $G_1$ and $G_2$. The structural statement is stronger than that particular specialization, with explicitly stronger input hypotheses than ordinary $\tau$-reality.

## 7 Scope and evidence

### 7.1 Intrinsic structural observations

For $a,b\geq3$, $H_{a,b}$ contains an induced $P_4$, so it is not a cograph; it is not a cycle. It is connected and has no clique separator: cliques have size at most two, and deleting a vertex or adjacent pair leaves a connected complete bipartite graph with at least two vertices on each side, minus at most one edge. Its complement is connected, consisting of two cliques joined by the missing cross-edge. Hence it has no nontrivial final join decomposition or clique-amalgamation decomposition.

These facts place $H_{a,b}$, for $a,b\geq3$, outside the explicit structural class generated from cographs, cycles, and $\Theta(2,2,3)$ by joins and ordinary clique amalgamations. Here $\Theta(2,2,3)$ consists of three internally vertex-disjoint paths of lengths $2,2,3$ with common endpoints. It has seven edges, whereas $H_{a,b}$ has $ab-1\geq8$, so $H_{a,b}$ is not that remaining seed either. The absence of a nontrivial final decomposition excludes construction by the stated operations. This is a structural comparison with that specified class, not an assertion of historical novelty.

For $H=K_{3,3}-e$, the nontrivial chromatic factor is

$$
q^4-7q^3+21q^2-30q+17.
$$

An exact rational complex root count gives one zero in

$$
\frac{189}{100}<\operatorname{Re}(q)<\frac{19}{10},\qquad
\frac{31}{20}<\operatorname{Im}(q)<\frac{39}{25}.
$$

Throughout this rectangle,

$$
4\operatorname{Im}(q)^2-1-4\operatorname{Re}(q)\geq\frac{101}{100}>0.
$$

Thus the graph lies outside even the closed parabolic region associated with the sufficient condition of BRW Proposition 5.13 [1]. The exact certificate and checker are supplied as `checkers/region_certificate.json` and `checkers/region_certificate.py`. This comparison does not assert historical novelty or exclude other sufficient theorems.

### 7.2 Limits of the conclusions

The theorem establishes all clique quotients needed for $H_{a,b}$ because its clique number is two. The structural corollary establishes only the quotients $k=0,1,2$. Neither result shows that every $\tau$-real graph has real-rooted clique quotients. The general $\tau$ clause of BRW Conjecture 6.5 is not resolved by this work.

The weighted matching theorem is due to Heilmann--Lieb [2]. Kang--Liu--Sun--Zhang [3] use weighted diagonal-edge root lifting for their graph-join theorem, which addresses BRW Conjecture 6.6, a different operation. Their method is credited, not claimed new here. Known $\sigma$-polynomial results must not be relabeled as the Bell chromatic-quotient statement proved here. No comprehensive literature or priority determination is claimed.

### 7.3 Computational checks and AI assistance

The accompanying checkers test symbolic identities and independently enumerate selected graphs and matchings. In particular, `checkers/review_full_symbolic.py` checks the effective-core enumeration, the unsigned chromatic differentiation, and the chromatic-to-matching generating-function interface. The structural bridge is checked by `checkers/structural_bridge_check.py`. These checks support, rather than replace, the all-parameter proofs above.

AI systems assisted with the mathematical derivations, separate review passes, computational checks, and editorial preparation. Separate AI review is not independent human peer review. The argument has not been verified in a proof assistant, and successful symbolic or finite checks do not constitute such verification. Human mathematical review and a deeper literature audit are appropriate before publication or any priority claim.

## References

1. Francesco Brenti, Gordon F. Royle, and David G. Wagner. *Location of zeros of chromatic and related polynomials of graphs*. Canadian Journal of Mathematics **46** (1), 55--80 (1994). [doi:10.4153/CJM-1994-002-3](https://doi.org/10.4153/CJM-1994-002-3).

2. Ole J. Heilmann and Elliott H. Lieb. *Theory of monomer-dimer systems*. Communications in Mathematical Physics **25**, 190--232 (1972). [doi:10.1007/BF01877590](https://doi.org/10.1007/BF01877590).

3. Mingyang Kang, Zhixin Liu, Sophie C. C. Sun, and Philip B. Zhang. *Real-rootedness of the $\tau$-polynomial under graph joins*. arXiv:2609.07457v1 (7 September 2026). [Versioned preprint](https://arxiv.org/html/2609.07457v1). The weighted-matching implication used here is restated in Theorem 4.2 and Corollary 4.3.
