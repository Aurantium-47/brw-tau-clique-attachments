---
title: "Clique attachment for anchored incomparability graphs and long theta graphs"
date: "2 November 2026"
lang: en
---

## Abstract

We establish two sufficient classes for ordinary clique attachment to an arbitrary $\tau$-real graph. First, an incomparability graph with a partition into $k$ nonempty independent classes and one anchor in each class adjacent to every vertex outside that class has real-rooted Bell chromatic quotients for every clique size from zero to $k$. The maximal quotient has an explicit unweighted bipartite matching representation, and the construction extends to independent blow-ups. Second, for each fixed pair of path lengths $a,b\geq2$, the edge quotient of $\Theta(a,b,m)$ has real-rooted Bell transform for all sufficiently large $m$. The second proof uses localization of the obstructing conjugate quadratic factors and a local quartic repair. Its threshold is existential and may depend on $a,b$.

The arguments below are ordinary mathematical proofs prepared with AI assistance. No historical priority, human peer review, proof-assistant verification, or resolution of the general $\tau$ clause of Brenti--Royle--Wagner Conjecture 6.5 is asserted.

## 1 Conventions and the Bell product

All graphs are finite and simple. Write $\chi_G(x)$ for the chromatic polynomial of a graph $G$ on $n$ vertices, and put

$$
P_G(x)=(-1)^n\chi_G(-x).
$$

The falling and rising factorials are, respectively,

$$
(x)_j=x(x-1)\cdots(x-j+1),\qquad
R_j(x)=x(x+1)\cdots(x+j-1),
$$

with $(x)_0=R_0=1$. Let $\mathcal B$ be the linear Bell transform

$$
\mathcal B((x)_j)=z^j.
$$

Equivalently, $\mathcal B(x^j)=T_j(z)$, where $T_j$ is the Touchard polynomial. In particular, $T_0=1$ and

$$
T_{j+1}=z(T_j+T'_j).
$$

The usual Rolle/interlacing argument gives only real nonpositive zeros for every $T_j$.

### 1.1 The BRW normalization and reflection

Brenti--Royle--Wagner [1] define transforms $\mathsf S$ on falling factorials and $\mathsf T$ on rising factorials by

$$
\mathsf S((x)_j)=z^j,\qquad \mathsf T(R_j)=z^j.
$$

Thus $\mathcal B=\mathsf S$, not $\mathsf T$. Let $\varepsilon$ denote reflection, $(\varepsilon f)(x)=f(-x)$. Reflection changes a rising factorial to $(-1)^j$ times its falling counterpart, so

$$
\mathsf T=\varepsilon\mathsf S\varepsilon,
\qquad \mathcal B=\varepsilon\mathsf T\varepsilon.
$$

This is also [1, Proposition 5.1(d)]. For graph polynomials it gives

$$
\begin{aligned}
\mathcal B(P_G)
&=(-1)^n\mathsf S\varepsilon\chi_G\\
&=(-1)^n\varepsilon\mathsf T\chi_G
=(-1)^n\tau_{\mathrm{BRW}}(G,-z).
\end{aligned}\tag{N}
$$

Thus real-rootedness of $\mathcal B(P_G)$ is exactly ordinary BRW $\tau$-reality, not $\sigma$-reality of the original chromatic polynomial. If $G$ is $\tau$-real, the roots of $\mathcal B(P_G)$ are nonpositive because its coefficients are nonnegative.

For real polynomials $p,q$, the two BRW products are

$$
\begin{aligned}
(p\ast q)(z)&=\sum_{j\geq0}\frac{z^j}{j!}p^{(j)}(z)q^{(j)}(z),\\
(p\star q)(z)&=\sum_{j\geq0}\frac{(-z)^j}{j!}p^{(j)}(z)q^{(j)}(z).
\end{aligned}
$$

The direct Bell-product identity is

$$
\mathcal B(FG)=\mathcal B(F)\ast\mathcal B(G).
$$

By [1, Propositions 4.2 and 4.4], if $\mathcal B(F)$ and $\mathcal B(G)$ have only real nonpositive zeros, then so does $\mathcal B(FG)$. The reflected route through [1, Propositions 5.2 and 5.4] gives the same statement, since

$$
\varepsilon\bigl[(\varepsilon p)\star(\varepsilon q)\bigr]=p\ast q.
$$

Reflection sends the nonpositive-root cone to the nonnegative-root cone required for that route, then sends the result back.

Multiplication by $x+h$ corresponds under $\mathcal B$ to

$$
L_h=z\frac{d}{dz}+z+h.
$$

For $h\geq0$ this preserves the nonpositive real-rooted cone, either by the usual Rolle/interlacing argument or by the Bell-product theorem with $\mathcal B(x+h)=z+h$.

### 1.2 Matching polynomials and ordinary attachment

For a graph with nonnegative edge weights, the Heilmann--Lieb theorem [2] gives real-rootedness of

$$
\mu(t)=\sum_M(-1)^{|M|}\operatorname{weight}(M)t^{|V|-2|M|},
$$

where the sum is over matchings. If

$$
Z(y)=\sum_M\operatorname{weight}(M)y^{|M|},
$$

then $\mu(t)=t^{|V|}Z(-1/t^2)$ implies that $Z$ has only negative real zeros. Consequently $z^RZ(1/z)$ has only nonpositive real zeros whenever $R\geq\deg Z$. For a bipartite graph with $R$ right vertices, this degree bound is automatic. Constants and zero edge weights are allowed.

If $G\cap F=K_j$, ordinary chromatic clique factorization [1, Proposition 1.1] gives

$$
P_{G\cup F}=P_G(P_F/R_j).\tag{A}
$$

Here ordinary attachment retains the common clique and makes no additional identifications or exclusive-side cross edges. The empty intersection $K_0$ is allowed. By the Bell-product theorem, real-rootedness of $\mathcal B(P_F/R_j)$ with nonpositive zeros implies $\tau$-reality of $G\cup F$ for every $\tau$-real $G$ with this overlap. BRW Proposition 5.12 already proves closure for empty or single-vertex intersections of $\tau$-real graphs; the attachment conclusions of interest here are edge or larger-clique intersections.

## 2 The two theorems

**Theorem 1.** Let $F$ be the incomparability graph of a finite poset $\mathcal P$, so distinct vertices are adjacent exactly when neither is below the other in $\mathcal P$. Suppose $V(F)$ has a partition into $k\geq1$ nonempty independent classes $I_1,\ldots,I_k$, with an anchor $s_i\in I_i$ adjacent to every vertex outside $I_i$. Then, for every $0\leq j\leq k$,

$$
\mathcal B(P_F/R_j)\text{ has only real nonpositive zeros}.\tag{T1}
$$

Consequently $F$ may be attached to any $\tau$-real graph along any complete intersection. Its maximal quotient $\mathcal B(P_F/R_k)$ is the reversed matching polynomial of the explicit unweighted bipartite graph in Section 3.6, which has exactly $|V(F)|-k$ right vertices. Independent blow-ups also satisfy the theorem when all anchor parts remain nonempty.

The anchors form a $K_k$, and the partition is a proper $k$-coloring, so $\chi(F)=\omega(F)=k$. Each anchor's nonneighbors are exactly the other vertices of its own independent class. A merely dominating clique without these partition and adjacency conditions is not the hypothesis of this theorem.

**Theorem 2.** For every fixed pair of integers $a,b\geq2$, there is an integer $M(a,b)\geq2$ such that, for every $m\geq M(a,b)$, the following holds. Let $H=\Theta(a,b,m)$ be the graph formed by three internally vertex-disjoint paths of lengths $a,b,m$ with common distinct endpoints. Then

$$
\mathcal B\bigl(P_H/[x(x+1)]\bigr)
\text{ has only real nonpositive zeros}.\tag{T2}
$$

Consequently ordinary edge attachment of $H$ to an arbitrary $\tau$-real graph preserves $\tau$-reality. Since $H$ is triangle-free, this covers all possible complete overlaps together with the already-known empty and single-vertex cases.

The threshold in Theorem 2 is existential and may depend on $a,b$. No uniform threshold over $a,b$, effective value of $M(a,b)$, or all-$m$ conclusion is asserted.

## 3 Proof for anchored incomparability graphs

### 3.1 A poset determinant lemma

Choose a linear extension of $\mathcal P$ and number its vertices $1,\ldots,n$. Define an $n$-by-$n$ zero-one matrix $M$ by

$$
\begin{aligned}
M_{ii}&=0,\\
M_{ij}&=1\quad\text{for }i<j,\\
M_{ij}&=1\quad\text{for }i>j\text{ exactly when }i,j\text{ are incomparable}.
\end{aligned}
$$

Put $L=M+I$. Equivalently, $L_{ij}=0$ exactly when $i>_{\mathcal P}j$, and otherwise $L_{ij}=1$.

**Lemma.** For every vertex subset $A$, $\det L[A]=1$ if $A$ is a chain of $\mathcal P$, and $\det L[A]=0$ otherwise. The empty determinant is one.

**Proof.** Work in the induced poset on $A$. If there are at least two minimal elements, their rows of $L[A]$ are identical all-one rows, so the determinant is zero. If there is one minimal element $v$, it is below every other element: each element has a descending chain ending at a minimal element. Simultaneously move $v$'s row and column first. Its column is then $(1,0,\ldots,0)^{\mathsf T}$, so expansion reduces the determinant to that of $A\setminus\{v\}$. Repeat. The determinant is one exactly when a unique minimum remains at every step, which is equivalent to $A$ being a chain. Otherwise it is zero.

Let $u_v$ be formal variables, and put

$$
U=\operatorname{diag}(u_v),\qquad
\mathcal H=\prod_v(1+u_v),\qquad
Z=\operatorname{diag}\left(\frac{u_v}{1+u_v}\right).
$$

The one-color exponential generating function for independent blow-ups is

$$
Q(\mathbf A)=\sum_{J\text{ independent in }F}\prod_{v\in J}(e^{A_v}-1).
$$

Independent sets of $F$ are exactly chains of $\mathcal P$. Put $u_v=e^{A_v}-1$ and $Q_-=Q(-\mathbf A)$. The principal-minor expansion and the lemma give

$$
\det(I-ZL)
=\sum_{J\text{ chain}}(-1)^{|J|}\prod_{v\in J}\frac{u_v}{1+u_v}
=Q_-.
$$

Since $I-UM=(I+U)(I-ZL)$,

$$
N:=\det(I-UM)=\mathcal H Q_-.\tag{I1}
$$

Also $\mathbf1\mathbf1^{\mathsf T}-M$ is lower triangular with diagonal entries one. By the matrix determinant lemma,

$$
\begin{aligned}
1+\Phi
&:=1+\mathbf1^{\mathsf T}(I-UM)^{-1}U\mathbf1\\
&=\frac{\det(I-UM+U\mathbf1\mathbf1^{\mathsf T})}{\det(I-UM)}
=\frac{\mathcal H}{N}.
\end{aligned}\tag{I2}
$$

All inverses are formal around $U=0$.

### 3.2 Anchors and the reflected quotient

The exponential generating function for proper colorings of all independent blow-ups of $F$ with $t$ colors is $Q(\mathbf A)^t$. This follows by giving each color an independent support, and extends coefficientwise polynomially in $t$.

Different anchors are adjacent. Hence no independent support contains two anchors, so every mixed derivative of $Q$ involving two distinct anchor variables is zero. The hypotheses also give

$$
\partial_{A_{s_i}}Q=\exp\left(\sum_{v\in I_i}A_v\right).
$$

Therefore

$$
\left(\prod_{i=1}^k\partial_{A_{s_i}}\right)Q^t
=(t)_kQ^{t-k}\exp\left(\sum_vA_v\right).\tag{I3}
$$

Differentiation fixes one labeled vertex in each anchor part; the exponential generating function indices thereafter count only the remaining vertices.

For residual total degree $m$, the unsigned chromatic polynomial has sign $(-1)^{m+k}$. Substitute $t=-x$ and $A_v\mapsto-A_v$ in (I3), and multiply by $(-1)^k$. The sign from $(-x)_k=(-1)^kR_k$ cancels. Dividing by $R_k$ gives the unsigned quotient exponential generating function

$$
\exp\left(-\sum_vA_v\right)Q_-^{-x-k}.
$$

The formal, coefficientwise identity

$$
\mathcal B(e^{sx})=\exp\bigl(z(e^s-1)\bigr)
$$

now yields

$$
\exp\left(-\sum_vA_v\right)Q_-^{-k}
\exp\bigl(z(Q_-^{-1}-1)\bigr).\tag{I4}
$$

Using (I1)--(I2), this becomes

$$
\frac{\mathcal H^{k-1}}{N^k}\exp(z\Phi)
=N^{-1}(1+\Phi)^{k-1}\exp(z\Phi).\tag{I5}
$$

This normalization includes odd $k$; no sign is suppressed.

### 3.3 The matching path and cycle generating function

For a vector $\mathbf r=(r_v)$ of nonnegative integers, use $r_v$ ordinary pairs $(\ell_{v,h},r_{v,h})$ of each vertex type $v$. Whenever $M_{vw}=1$, join every left vertex of type $v$ to every right vertex of type $w$. All edges have weight one.

Let $R=\sum_vr_v$. The reversed matching polynomial is $\sum_Mz^{R-|M|}$. Its multitype exponential generating function is

$$
N^{-1}\exp(z\Phi).\tag{I6}
$$

For a purely formal proof, identify each ordinary left/right pair as one label. A matching becomes a directed graph on these labels with indegree and outdegree at most one. Its components are directed paths and directed cycles. The cycles contribute

$$
\exp\left(\sum_{j\geq1}\frac{\operatorname{tr}((UM)^j)}j\right)
=\det(I-UM)^{-1},
$$

and the paths, including singleton labels, contribute the exponential of

$$
z\mathbf1^{\mathsf T}(I-UM)^{-1}U\mathbf1.
$$

The exponential formula proves (I6). This identity assumes no finite bound on $\mathbf r$ and uses no analytic convergence argument.

Now add $k-1$ distinct new left vertices, each adjacent to every ordinary right vertex. Before adding one such vertex, $R-|M|$ is the number of available right vertices. Leaving the new vertex unmatched gives the same term; matching it gives $R-|M|$ choices and lowers the exponent by one. Thus each universal left vertex applies $1+D_z$, where $D_z=d/dz$, even after earlier universal vertices have been added. Adding all $k-1$ vertices changes (I6) into

$$
\begin{aligned}
(1+D_z)^{k-1}\bigl[N^{-1}\exp(z\Phi)\bigr]
&=N^{-1}(1+\Phi)^{k-1}\exp(z\Phi),
\end{aligned}\tag{I7}
$$

exactly the quotient kernel (I5). The matching degree is at most $R$ because there are only $R$ right vertices.

### 3.4 Stirling composition

Let $C_{\mathbf r}(z)$ be the reversed matching polynomial just constructed, and define the multilinear map

$$
\mathcal C(z^{r_1},\ldots,z^{r_n})=C_{\mathbf r}(z).
$$

Substitution $u_v=e^{A_v}-1$ in its exponential generating function gives the Stirling composition rule. For blow-up part sizes $m_v$, with $m_{s_i}\geq1$ for anchors and other sizes nonnegative, put $r_v=m_v-1$ at anchor vertices and $r_v=m_v$ elsewhere. Then

$$
\mathcal B(P_{\mathrm{blowup}}/R_k)
=\mathcal C(T_{r_1},\ldots,T_{r_n}).\tag{I8}
$$

Here the exponential substitution uses

$$
\frac{(e^A-1)^i}{i!}=\sum_{r\geq i}S(r,i)\frac{A^r}{r!},
$$

with $S(r,i)$ the Stirling numbers of the second kind.

### 3.5 Weighted diagonal edges and blow-ups

For each type $v$ and ordinary pair $h$, add the previously absent diagonal edge $\ell_{v,h}r_{v,h}$ with a nonnegative weight $\alpha_{v,h}$. It is absent initially because $M_{vv}=0$. Conditioning on which diagonal edges are chosen and deleting their endpoint pairs leaves the same base graph with smaller type counts and the same $k-1$ universal left vertices. The reversed exponent agrees. Consequently the augmented weighted reversed matching polynomial is

$$
\mathcal C\left(
\prod_h(z+\alpha_{1,h}),\ldots,\prod_h(z+\alpha_{n,h})
\right).
$$

The weighted matching theorem therefore proves that $\mathcal C$ preserves real nonpositive zeros in all inputs. Constants, repeated roots and zero weights are permitted. Nonzero scalar factors only scale the output. Since Touchard polynomials have only real nonpositive zeros, (I8) proves the blow-up assertion.

Replacing a poset vertex by a chain gives precisely independent graph twins. This also shows directly that the independent blow-ups preserve the incomparability, independent-class and anchor hypotheses when the anchor parts remain nonempty.

### 3.6 The direct unweighted graph for the original graph

For $F$ itself, every part size $m_v$ equals one. In (I8), the anchor inputs are $T_0=1$ and every other input is $T_1=z$. Hence no Stirling sum or weighted diagonal is needed.

Let $S=\{s_1,\ldots,s_k\}$. The explicit bipartite graph has:

- one ordinary left/right pair for each vertex $v\notin S$;
- an edge $\ell_vr_w$ exactly when $M_{vw}=1$, using the matrix restricted to $V(F)\setminus S$;
- $k-1$ additional left vertices, each adjacent to every ordinary right vertex.

It has exactly $n-k$ right vertices and $n-1$ left vertices. Its reversed matching polynomial

$$
\sum_Mz^{n-k-|M|}
$$

is exactly $\mathcal B(P_F/R_k)$. The matching theorem proves real-rootedness. If $n=k$, the polynomial is one and the graph has no right vertices; the statement still holds.

### 3.7 Smaller cliques and attachment

For $j\leq k$,

$$
P_F/R_j=(P_F/R_k)\prod_{h=j}^{k-1}(x+h).
$$

Applying the operators $L_h$ from Section 1 proves (T1) for every $j$. If $G\cap F=K_j$, formula (A) and Bell-product preservation give $\tau$-reality of the union. The input $G$ is otherwise arbitrary: it need not be an incomparability graph or satisfy the anchor condition. This completes the proof of Theorem 1.

## 4 Explicit subclasses of the anchored theorem

### 4.1 Independent path blow-ups and rectangular deletion

On the path vertices $A-B-C-D$, use the poset relations $A<C$, $A<D$, $B<D$ and no other strict relations. Its incomparability graph is $P_4$. Its independent classes are $\{A,C\}$ and $\{B,D\}$; choose anchors $C$ and $B$.

Replacing each poset element by a chain realizes every independent $P_4$ blow-up. The middle parts must remain nonempty. More explicitly, for $p,q\geq0$ and $b,c\geq1$, this includes $K_{p+c,b+q}$ with a $p$-by-$q$ rectangle of cross edges deleted. The middle two parts have sizes $b,c$ and the outer two have sizes $p,q$. The case $p=q=1$ is complete bipartite minus one edge. The quotient depends only on the chromatic polynomial, so attachment may use any edge, not just the chosen anchor edge.

### 4.2 Connected Ferrers graphs

Let the bipartition be $A=\{a_1,\ldots,a_m\}$ and $B=\{b_1,\ldots,b_n\}$, with

$$
N(a_i)=\{b_1,\ldots,b_{d_i}\},\qquad
1\leq d_1\leq\cdots\leq d_m=n.
$$

Define chains $a_1<\cdots<a_m$ and $b_1<\cdots<b_n$, and cross relations $a_i<b_j$ exactly when $j>d_i$; put no cross relation in the opposite direction. These relations are transitive: increasing the $A$ index can only increase $d_i$, and increasing the $B$ index preserves $j>d_i$. The incomparability graph is exactly the specified Ferrers graph. Anchors $a_m,b_1$ are adjacent to all opposite-part vertices. Hence every such connected Ferrers, or chain, graph has real-rooted Bell quotients for $j=0,1,2$. Disconnected or isolated additions require a separate closure argument and are not included silently.

### 4.3 Two disjoint deleted edges

For $K_{a,b}\setminus\{a_1b_1,a_2b_2\}$, with $a,b\geq3$, order the two parts as chains

$$
a_1<a_3<\cdots<a_a<a_2,\qquad
b_2<b_3<\cdots<b_b<b_1.
$$

Add only the cross relations $a_1<b_1$ and $b_2<a_2$. Each goes from a chain minimum to the other chain maximum, so transitivity creates no further cross relations. Its incomparability graph is exactly the specified graph. Anchors $a_3,b_3$ are universal to the opposite parts. The theorem and its independent blow-up extension apply. This is not a claim for deletion of an arbitrary larger matching.

### 4.4 A three-class example

Use three chains

$$
a_-<a_0<a_+,\qquad b_-<b_0<b_+,\qquad c_-<c_0<c_+,
$$

and add only $a_-<b_+$, $b_-<c_+$, $c_-<a_+$. These minimum-to-maximum cross relations create no additional cross comparabilities. The three middle vertices are anchors. The incomparability graph is $K_{3,3,3}$ minus those three specified cross edges, and its $K_3$ quotient has real-rooted Bell transform.

### 4.5 Separation from a specified structural closure

Take the independent $P_4$ blow-up with part sizes $(2,2,2,2)$, equivalently $K_{4,4}$ minus a $2$-by-$2$ rectangle. It is connected. Its complement consists of two cliques linked by a nonempty rectangular block, so is connected as well. Its clique number is two. Removing any vertex or any adjacent pair leaves a connected graph: both middle parts retain at least one vertex, and every remaining outer vertex is joined to a remaining middle vertex. Thus it has no clique separator.

It contains an induced $P_4$, so it is not a cograph. It is not a cycle, and its eight vertices and twelve edges distinguish it from $\Theta(2,2,3)$. Its connected bipartition is uniquely $4+4$ up to exchange; a complete bipartite graph with one edge deleted on that bipartition has fifteen edges, not twelve.

Consequently this graph cannot be a nontrivial last join, since its complement is connected, or an ordinary clique amalgamation of smaller graphs, since it has no clique separator. It is not one of the listed seeds. Nor can it be the output of the operation

$$
\bigl((G_1+u)\vee(G_2+v)\bigr)-uv,
$$

where $G_1,G_2$ are nonempty, $u,v$ are newly added isolated vertices in their respective inputs, and $\vee$ is graph join. If either input has an edge, that edge and any vertex of the opposite nonempty input make a triangle. Triangle-free output therefore forces both inputs to be edgeless, giving exactly a complete bipartite graph with one edge deleted.

This final-operation obstruction applies to the finite iterative closure generated from cographs, cycles, $\Theta(2,2,3)$, and complete bipartite graphs with one edge deleted, using nontrivial joins, ordinary clique amalgamations, and the displayed operation. It compares these explicit structural scopes only, not all earlier mathematical results or their polynomial consequences.

## 5 Proof for fixed two paths and a sufficiently long third path

Fix $a,b\geq2$, and write $H=\Theta(a,b,m)$ and

$$
Q_H(x)=P_H(x)/[x(x+1)].
$$

### 5.1 The exact path coloring formula

For a path of length $\ell$, the numbers of proper internal colorings when its endpoint colors are fixed and equal or distinct are respectively

$$
E_\ell(q)=\frac{(q-1)^\ell+(q-1)(-1)^\ell}{q},\qquad
D_\ell(q)=\frac{(q-1)^\ell-(-1)^\ell}{q}.
$$

These identities follow from the eigenvalues $q-1$ and $-1$ of the complete-color transition matrix, or its two-state recurrence, and are polynomial identities after the displayed cancellation. Choosing endpoint colors gives

$$
\chi_H(q)=qE_a(q)E_b(q)E_m(q)
+q(q-1)D_a(q)D_b(q)D_m(q).
$$

There are $a+b+m-1$ vertices. Set $t=x+1$ and substitute $q=-x$. Direct cancellation of the parity signs yields

$$
\begin{aligned}
P_H(x)
&=\frac{t(t^a-1)(t^b-1)(t^m-1)
-(t^a-t)(t^b-t)(t^m-t)}{(t-1)^2}\\
&=\frac{t\bigl[(t^{a+b-1}-1)t^m-(t^a+t^b-t-1)\bigr]}{t-1}.
\end{aligned}
$$

Write $S_\ell(t)=1+t+\cdots+t^{\ell-1}$ and define fixed polynomials

$$
A(t)=S_{a+b-1}(t),\qquad C(t)=S_a(t)+S_b(t)-1.
$$

Then the edge quotient is exactly

$$
\begin{aligned}
Q_H(t-1)
&=\frac{A(t)t^m-C(t)}{t-1}\\
&=A(t)S_m(t)+tS_{a-1}(t)S_{b-1}(t).
\end{aligned}\tag{H1}
$$

For the last equality, use

$$
A-C=(t-1)tS_{a-1}S_{b-1}.
$$

In particular, $Q_H(x)$ has strictly positive coefficients. The right side of (H1) has nonnegative coefficients in $t$, and its leading power of $t$ alone contributes positively to every $x$-coefficient after $t=x+1$. Thus all real roots of $Q_H$ are strictly negative.

The zeros of $A$ are roots of unity other than $1$, so all have modulus one. The fixed polynomial $C$ is nonzero, because $C(1)=a+b-1>0$.

### 5.2 Localization of every obstructing quadratic factor

Set $N_m(t)=A(t)t^m-C(t)$. It is monic. All its nonleading coefficients have modulus at most two, including positions where the terms overlap, so its roots satisfy the uniform Cauchy bound $|t|\leq3$.

For fixed $a,b$, every limit of roots $t_j$ of $N_{m_j}$, with $m_j\to\infty$, lies in the closed unit disk. Indeed, after passing to a convergent subsequence, a hypothetical limit $|t_*|>1$ would give

$$
A(t_j)=\frac{C(t_j)}{t_j^{m_j}}\longrightarrow0,
$$

and hence $A(t_*)=0$, contradicting the location of $A$'s zeros. No claim about the number or reality of roots inside the disk is needed.

For an upper-half-plane root $t$ of $Q_H(t-1)$, write its $x$-root as $t-1=-u+iv$, with $v>0$. Its monic real quadratic factor is

$$
h_t(x)=x^2+2ux+u^2+v^2.
$$

Its Bell transform is

$$
\mathcal B(h_t)(z)=z^2+(2u+1)z+u^2+v^2,
$$

with discriminant

$$
\begin{aligned}
J(t)&=1+4u-4v^2\\
&=5-4\operatorname{Re}(t)-4(\operatorname{Im}t)^2\\
&=4(1-|t|^2)+4\bigl(\operatorname{Re}(t)-\tfrac12\bigr)^2.
\end{aligned}\tag{H2}
$$

If $J(t)\geq0$, then $\mathcal B(h_t)$ has real strictly negative zeros: $J\geq0$ implies $u\geq-1/4$, its linear coefficient is positive, and its constant coefficient is positive. Call a quadratic *bad* if $J(t)<0$, and *good* otherwise.

By (H2), $J$ is strictly positive inside the unit disk. On its boundary it vanishes only at $\zeta=e^{i\pi/3}$ and $\overline\zeta$. Therefore, for every $\delta>0$, all upper-half-plane roots of bad quadratic factors eventually lie within $\delta$ of $\zeta$. Otherwise a sequence of bad roots outside that neighborhood would have a convergent subsequence in the closed unit disk, with $J\leq0$, and its upper-half-plane limit would have to be $\zeta$, a contradiction. This proves uniform localization of all bad factors, counted with multiplicity.

### 5.3 Local quartic repair

At $\zeta$, $h_\zeta(x)=x^2+x+1$. Direct calculation gives

$$
\begin{aligned}
\mathcal B(h_\zeta^2)(z)
&=z^4+8z^3+16z^2+8z+1\\
&=\bigl(z^2+(4+\sqrt2)z+1\bigr)
\bigl(z^2+(4-\sqrt2)z+1\bigr).
\end{aligned}\tag{H3}
$$

Its four zeros are simple and strictly negative. By continuity of coefficients and persistence of four disjoint negative sign-change intervals, there exists $\delta>0$ such that

$$
|t-\zeta|<\delta,\qquad |s-\zeta|<\delta
$$

imply that $\mathcal B(h_th_s)$ has four simple negative zeros. This applies whether either quadratic separately is good or bad. At the central quartic one may use the disjoint intervals

$$
(-6,-5),\quad(-3,-2),\quad
\left(-\tfrac12,-\tfrac25\right),\quad
\left(-\tfrac15,-\tfrac1{10}\right).
$$

Reduce $\delta$ so its disk is in the upper half-plane.

### 5.4 A spare good pair for every sufficiently large length

Choose a root of unity $\rho$ in this disk, with $\rho\ne\zeta$ and $A(\rho)C(\rho)\ne0$. This is possible because roots of unity are dense on the unit circle, while only finitely many choices are excluded. Let $\ell$ be the order of $\rho$. Then $J(\rho)>0$.

For each residue $r=0,\ldots,\ell-1$, choose a complex logarithm $w_{r,0}$ satisfying

$$
\exp(w_{r,0})=\rho^{-r}\frac{C(\rho)}{A(\rho)}.
$$

The analytic function

$$
H_r(\epsilon,w)=\exp(w)A\bigl(\rho\exp(\epsilon w)\bigr)
-\rho^{-r}C\bigl(\rho\exp(\epsilon w)\bigr)
$$

vanishes at $(0,w_{r,0})$, and its $w$ derivative there is $\exp(w_{r,0})A(\rho)\ne0$. The analytic implicit-function theorem supplies $w_r(\epsilon)$ near zero with $H_r(\epsilon,w_r(\epsilon))=0$.

For all sufficiently large $m$ congruent to $r$ modulo $\ell$,

$$
s_m=\rho\exp\bigl(w_r(1/m)/m\bigr)
$$

satisfies $N_m(s_m)=0$. Since $s_m\to\rho$, it eventually lies in the upper half-plane within $\delta$ of $\zeta$, differs from $t=1$, and satisfies $J(s_m)>0$. It therefore gives a good conjugate quadratic factor of $Q_H$. The number of residues is finite, so this spare good factor is available for every sufficiently large $m$, not merely a subsequence.

### 5.5 Assemble the real factorization and attach

Take a common threshold for Sections 5.2--5.4, and factor $Q_H$ over $\mathbb R$ with multiplicity.

- Each real linear factor has a negative root, by (H1).
- Each good conjugate quadratic has real-rooted Bell transform, by (H2).
- All bad quadratics have upper roots in the local-repair disk.

If the number of bad quadratics is even, pair them arbitrarily. If it is odd, include the spare good quadratic from Section 5.4 and pair the resulting even collection, removing that spare from the separately treated good factors. Every resulting quartic has real-rooted Bell transform by Section 5.3. This argument permits repeated roots and repeated factors.

Iterating Bell-product preservation over these factor blocks proves that $\mathcal B(Q_H)$ has only real nonpositive zeros. For an edge overlap $G\cap H=K_2$, formula (A) reads

$$
P_{G\cup H}=P_GQ_H.
$$

If $G$ is $\tau$-real, one final Bell-product application proves the attachment assertion. Also $\mathcal B(x(x+1))=z(z+2)$ is real-rooted, so multiplying $Q_H$ by $x(x+1)$ through the same Bell product proves that $H$ itself is $\tau$-real. This supplies the premise for BRW Proposition 5.12 at empty or single-vertex overlaps. The normalization equivalence is (N), completing the proof of Theorem 2.

## 6 Boundaries and evidence

### 6.1 The anchor hypothesis cannot be weakened silently

A triangle $\{a,b,c\}$ together with a leaf $v$ adjacent only to $a$ has a dominating triangle, but $v$ is a nonneighbor of both $b$ and $c$. It therefore contributes to both anchor derivatives $Q_b=\partial_{A_b}Q$ and $Q_c=\partial_{A_c}Q$, so the product of anchor derivatives is not $\exp(\sum_vA_v)$. This obstructs dropping the precise anchor-partition hypothesis from the exponential generating function proof. It is not a counterexample to real-rootedness; this graph is chordal.

Theorem 1 does not replace its anchor and incomparability assumptions by ordinary $\tau$-reality. Theorem 2 does not supply $M(a,b)$ and does not justify extending finite checks to every $m$. In particular, the all-length $\Theta(2,2,m)$ edge-quotient problem and arbitrary $\tau$-real clique overlap are not settled here.

### 6.2 Prior results and attribution

BRW Conjecture 6.5 concerns ordinary clique intersection, with separate $\tau$ and $w$ clauses. Conjecture 6.6 concerns graph join. Kang--Liu--Sun--Zhang [3] address Conjecture 6.6 and provide an acknowledged weighted matching and diagonal-edge root-lifting precedent. The weighted matching real-rootedness theorem is due to Heilmann--Lieb [2]. Neither method is claimed as historically new here.

The inspected incomparability results in Brenti [4] and BRW concern $\sigma$-polynomial real-rootedness; these must not be relabeled as Bell chromatic-clique-quotient or arbitrary $\tau$-factor attachment results. Ferrers graph enumeration [5] is relevant background, not a substitute assumed for the quotient proof. A bounded literature search does not determine historical priority or exclude a subsuming result elsewhere. No priority is claimed for the determinant identity, matching representation, or local-repair argument.

### 6.3 Exact checks and AI assistance

Companion programs independently compare selected actual chromatic quotients with the anchored matching representation, including a nontrivial three-class example, and check the exact polynomial identities in the theta argument. Such computations support the displayed proofs; they do not prove all-parameter matching identities by finite extrapolation. In particular, exact theta algebra checks neither verify analytic eventuality nor supply an effective threshold.

AI systems assisted with derivation, separate review passes, computational checks, and manuscript preparation. Separate AI review is not independent human peer review. The arguments have not been verified in a proof assistant. Human mathematical review and a deeper literature audit are appropriate before publication or a priority claim.

## References

1. Francesco Brenti, Gordon F. Royle, and David G. Wagner. *Location of zeros of chromatic and related polynomials of graphs*. Canadian Journal of Mathematics **46** (1), 55--80 (1994). [doi:10.4153/CJM-1994-002-3](https://doi.org/10.4153/CJM-1994-002-3).

2. Ole J. Heilmann and Elliott H. Lieb. *Theory of monomer-dimer systems*. Communications in Mathematical Physics **25**, 190--232 (1972). [doi:10.1007/BF01877590](https://doi.org/10.1007/BF01877590).

3. Mingyang Kang, Zhixin Liu, Sophie C. C. Sun, and Philip B. Zhang. *Real-rootedness of the $\tau$-polynomial under graph joins*. arXiv:2609.07457v1 (7 September 2026). [Versioned preprint](https://arxiv.org/html/2609.07457v1).

4. Francesco Brenti. *Expansions of chromatic polynomials and log-concavity*. Transactions of the American Mathematical Society **332** (2), 729--756 (1992). [doi:10.1090/S0002-9947-1992-1069745-7](https://doi.org/10.1090/S0002-9947-1992-1069745-7).

5. Richard Ehrenborg and Stephanie van Willigenburg. *Enumerative properties of Ferrers graphs*. [arXiv:0706.2918](https://arxiv.org/abs/0706.2918).
