---
title: "Real rooted edge quotients and clique attachment for theta graphs"
date: "2 November 2026"
lang: en
---

## Abstract

For every simple theta graph whose three path lengths are at least two, we prove that the Bell transform of its unsigned chromatic edge quotient has only strictly negative real zeros. Consequently, ordinary attachment of any such theta graph to an arbitrary $\tau$-real graph along a complete intersection preserves $\tau$-reality. The proof is exact and computer-assisted. A rational radius criterion, together with two Bernstein-certified factor-repair lemmas, covers every total path length at least $72$ and many smaller triples. An exhaustive finite verification covers the remainder: among $52,394$ sorted triples with maximum path length at most $68$, $49,934$ satisfy the radius criterion and $2,460$ have exact negative-root certificates. The finite verification checks $83,842$ factor-root boxes using integer arithmetic and rational sign changes, not numerical root classification.

This is a theta-family result, not a proof of general clique-overlap closure for arbitrary $\tau$-real graphs. No historical novelty, human peer review, or proof-assistant verification is asserted.

## 1 Statement and normalization

All graphs are finite and simple. For $a,b,c\geq2$, let $\Theta(a,b,c)$ consist of three internally vertex-disjoint paths of lengths $a,b,c$ with common distinct endpoints. Path lengths count edges. For a graph $G$ on $n$ vertices, set

$$
P_G(x)=(-1)^n\chi_G(-x),
$$

where $\chi_G$ is the chromatic polynomial. Define the linear Bell transform by

$$
B((x)_j)=z^j,\qquad
(x)_j=x(x-1)\cdots(x-j+1),\qquad (x)_0=1.
$$

Equivalently,

$$
B(x^j)=T_j(z)=\sum_{i=0}^j S(j,i)z^i,
$$

where $S(j,i)$ are Stirling numbers of the second kind and $T_j$ are the Touchard polynomials.

**Theorem.** For all integers $a,b,c\geq2$, with $H=\Theta(a,b,c)$, the polynomial

$$
B(Q_H),\qquad Q_H(x)=\frac{P_H(x)}{x(x+1)},
$$

has only strictly negative real zeros. If $G$ is any ordinary $\tau$-real graph and $G\cap H$ is complete, then the ordinary union $G\cup H$ is $\tau$-real.

Ordinary attachment retains the common clique, makes no additional identifications, and adds no cross edges between the exclusive sides. Since $H$ is triangle-free, the possible complete intersections are empty, one vertex, or one edge.

### 1.1 The BRW transforms

In Brenti--Royle--Wagner [1], the transforms $S$ and $T$ send falling and rising factorials, respectively, to monomials:

$$
S((x)_j)=z^j,\qquad
T\bigl(x(x+1)\cdots(x+j-1)\bigr)=z^j.
$$

Thus $B=S$. If $\varepsilon$ denotes reflection, $(\varepsilon f)(x)=f(-x)$, then $B=\varepsilon T\varepsilon$, and

$$
B(P_G)(z)=(-1)^n\tau_{\mathrm{BRW}}(G,-z).\tag{1}
$$

This is the reflection relation of [1, Proposition 5.1(d)]. Therefore real-rootedness of $B(P_G)$ is exactly ordinary BRW $\tau$-reality, not $\sigma$-reality of the original chromatic polynomial. When these roots are real, they are nonpositive: deletion--contraction gives $P_G=P_{G-e}+P_{G/e}$, so induction shows that $P_G$, and hence $B(P_G)$, has nonnegative coefficients.

We use the Bell product

$$
(f*g)(z)=\sum_{j\geq0}\frac{z^j}{j!}f^{(j)}(z)g^{(j)}(z).
$$

By [1, Propositions 4.2 and 4.4],

$$
B(FG)=B(F)*B(G),\tag{2}
$$

and $f*g$ has only real nonpositive zeros whenever $f$ and $g$ do. These are the root-preservation inputs used throughout the proof.

## 2 The exact theta quotient and its root trace

Write

$$
S_\ell(t)=1+t+\cdots+t^{\ell-1}\quad(\ell\geq1),
\qquad S_0(t)=0,\qquad t=x+1.
$$

For a path of length $\ell$, the numbers of proper internal colorings with prescribed equal or prescribed distinct endpoint colors are

$$
E_\ell(q)=\frac{(q-1)^\ell+(q-1)(-1)^\ell}{q},\qquad
D_\ell(q)=\frac{(q-1)^\ell-(-1)^\ell}{q}.
$$

For example, these follow from

$$
E_{\ell+1}=(q-1)D_\ell,\qquad
D_{\ell+1}=E_\ell+(q-2)D_\ell,
\qquad E_0=1,\quad D_0=0.
$$

The displayed quotients are polynomials after cancellation. Choosing the two common endpoint colors gives

$$
\chi_H(q)=qE_a(q)E_b(q)E_c(q)
+q(q-1)D_a(q)D_b(q)D_c(q).
$$

Put $s=a+b+c$, so $|V(H)|=s-1$. Substituting $q=1-t=-x$ and applying the sign $(-1)^{s-1}$ gives

$$
P_H(x)=\frac{t(t^a-1)(t^b-1)(t^c-1)
-(t^a-t)(t^b-t)(t^c-t)}{(t-1)^2}.
$$

After division by $x(x+1)=(t-1)t$, the exact quotient identities are

$$
Q_H(t-1)=S_{a+b-1}(t)S_c(t)
+tS_{a-1}(t)S_{b-1}(t),\tag{3}
$$

and, equivalently,

$$
(t-1)^2Q_H(t-1)
=t^{s-1}-t^a-t^b-t^c+t+1.\tag{4}
$$

These are polynomial identities, including at $t=1$. Formula (3) is positive for every real $t\geq0$, including $t=0$, where its value is $1$. Thus every real $t$-root is negative. After $t=x+1$, all coefficients of $Q_H(x)$ are strictly positive: the leading monomial in (3) alone contributes positively to every coefficient.

The degree of $Q_H(t-1)$ is

$$
d=s-3.
$$

It is monic and its next coefficient is $2$. To see this, write

$$
N(t)=S_{a+b-1}(t)t^c-\bigl(S_a(t)+S_b(t)-1\bigr).
$$

Then $Q_H(t-1)=N(t)/(t-1)$. The leading two coefficients of $N$ are $1,1$, since $a,b,c\geq2$ place the subtracted polynomial below those terms. Division by $t-1$ gives the asserted next coefficient. Hence Vieta's formula gives

$$
\sum_{Q_H(t-1)=0}t=-2,\tag{5}
$$

with all roots counted with multiplicity.

## 3 An effective radius criterion

Set

$$
R=\frac{21}{20}.
$$

We first prove the analytic part of the theorem under the strict rational condition

$$
R^{s-1}>R^a+R^b+R^c+R+1.\tag{6}
$$

If a root $t$ of $Q_H(t-1)$ had $r=|t|\geq R$, equation (4) and the triangle inequality would imply

$$
1\leq r^{a-s+1}+r^{b-s+1}+r^{c-s+1}
+r^{2-s}+r^{1-s}.
$$

Every exponent on the right is negative. Its value is therefore at most its value at $R$, which (6) makes strictly less than one. This contradiction proves

$$
|t|<R\quad\text{for every root of }Q_H(t-1).\tag{7}
$$

### 3.1 Every total path length at least 72 satisfies the criterion

For $r>1$ and $a,b\geq2$,

$$
r^a+r^b\leq r^{a+b-2}+r^2,
$$

because the difference is $r^2(r^{a-2}-1)(r^{b-2}-1)\geq0$. Applying this again gives

$$
r^a+r^b+r^c\leq r^{s-4}+2r^2.
$$

The exact integer inequality

$$
21^{68}(21^3-20^3)
>(2\cdot21^2+21\cdot20+20^2)20^{69}\tag{8}
$$

is equivalent to $R^{68}(R^3-1)>2R^2+R+1$. Therefore, for $s\geq72$,

$$
R^{s-1}>R^{s-4}+2R^2+R+1
\geq R^a+R^b+R^c+R+1.
$$

Thus every total path length at least $72$ satisfies (6). This is a concrete exact bound, not an asymptotic or existential threshold.

## 4 Exact factor repair in the radius disk

Assume (7), and factor $Q_H$ over $\mathbb R$, keeping multiplicities. A real $t$-root is negative by (3), so the corresponding factor in $x=t-1$ is $x+\alpha$, with

$$
1<\alpha<1+R=\frac{41}{20}.
$$

A nonreal conjugate $t$-pair gives a monic factor

$$
h(x)=x^2+px+q,\qquad
p=2-2\operatorname{Re}t,\qquad q=|t-1|^2>0.
$$

Its Bell transform is $B(h)=z^2+(p+1)z+q$. Call the pair *good* if

$$
J=(p+1)^2-4q\geq0,
$$

and *bad* otherwise. For a good pair, $p+1=3-2\operatorname{Re}t>3-2R=9/10>0$, so $B(h)$ has real strictly negative roots.

For a bad pair, set

$$
\delta=q-p=|t|^2-1.
$$

Then

$$
J=(p-1)^2-4\delta<0,
\qquad
0<\delta<R^2-1=\frac{41}{400}<\frac19.
$$

Consequently $|p-1|<2\sqrt\delta<2/3$ and

$$
\operatorname{Re}t=1-p/2>1/6.\tag{9}
$$

The next two lemmas repair products containing bad factors. Their discriminant claims are certified by finite exact rational arithmetic over entire parameter boxes.

### 4.1 The tensor Bernstein certificate principle

For a variable $y\in[0,1]$, the degree-$n$ Bernstein polynomials are

$$
b_{i,n}(y)=\binom ni y^i(1-y)^{n-i}\qquad(0\leq i\leq n).
$$

They are nonnegative and sum to one. For a multivariate polynomial of coordinate degrees $\mathbf n=(n_1,\ldots,n_r)$,

$$
D(\mathbf y)=\sum_{\mathbf j}c_{\mathbf j}\mathbf y^{\mathbf j}
=\sum_{\mathbf i}\beta_{\mathbf i}
\prod_{\ell=1}^r b_{i_\ell,n_\ell}(y_\ell),
$$

the exact conversion is

$$
\beta_{\mathbf i}
=\sum_{\mathbf j\leq\mathbf i}c_{\mathbf j}
\prod_{\ell=1}^r
\frac{\binom{i_\ell}{j_\ell}}{\binom{n_\ell}{j_\ell}}.\tag{10}
$$

It follows by applying, in each coordinate,

$$
y^j=\sum_{i=j}^n
\frac{\binom ij}{\binom nj}\binom ni y^i(1-y)^{n-i}.
$$

The coefficients can be checked by the inverse identity

$$
c_{\mathbf j}
=\left(\prod_{\ell=1}^r\binom{n_\ell}{j_\ell}\right)
\sum_{\mathbf i\leq\mathbf j}
(-1)^{|\mathbf j-\mathbf i|}\beta_{\mathbf i}
\prod_{\ell=1}^r\binom{j_\ell}{i_\ell},\tag{11}
$$

which is obtained by expanding the Bernstein basis back into powers. All inequalities between multi-indices are coordinatewise.

If every $\beta_{\mathbf i}>0$, then $D$ is strictly positive throughout $[0,1]^r$. For the two discriminants below, the supplied certificates give every rational Bernstein coefficient, verify its positivity, and verify the exact inverse conversion. Positivity of a quartic discriminant alone does not imply four real roots. We also use a real-rooted basepoint and connectedness: in a continuous monic real-polynomial family with no repeated roots, the number of real roots cannot change. The parameter boxes are connected and the discriminants do not vanish.

### 4.2 A bad quadratic times any conjugate quadratic

Let $h_1=x^2+Px+Q$ be a bad factor arising from the radius-$R$ disk, and let $h_2=x^2+px+q$ be any conjugate-pair factor from that disk. Then $B(h_1h_2)$ has four distinct strictly negative roots.

To certify this, enlarge the parameter domain to $a_0,b_0,u,v\in[0,1]$ and set

$$
\begin{aligned}
P&=1+\frac23b_0(2a_0-1),&
Q&=P+\frac{b_0^2}{9},\\
p&=2+2R-4Ru,&
q&=(1+R-2Ru)^2+4R^2u(1-u)v.
\end{aligned}\tag{12}
$$

For the desired bad factor, take $b_0=3\sqrt\delta$ and $2a_0-1=(P-1)/(2\sqrt\delta)$. The inequalities preceding (9) put these parameters in the box. For the second root, use

$$
\operatorname{Re}t=-R+2Ru,\qquad
(\operatorname{Im}t)^2=4R^2u(1-u)v.
$$

This represents the entire disk. The added boundary cases only enlarge the domain.

Direct Bell expansion gives

$$
\begin{aligned}
f(z)=B(h_1h_2)
={}&z^4+(6+P+p)z^3\\
&+(7+3(P+p)+Q+q+Pp)z^2\\
&+(1+P+p+Q+q+Pp+Pq+pQ)z+Qq.
\end{aligned}\tag{13}
$$

After substitution (12), $\operatorname{Disc}_z(f)$ has coordinate degrees

$$
(10,5,6,10)\quad\text{in }(u,v,a_0,b_0).
$$

All $11\cdot6\cdot7\cdot11=5,082$ tensor Bernstein coefficients are strictly positive. Their exact minimum is

$$
\frac{1319869198532766581}{19683000000000000}>0.\tag{14}
$$

The complete rational list is supplied in `effective_mixed_certificate.json`; `effective_mixed_certificate.py` constructs the discriminant, performs (10), and checks the exact inverse expansion (11).

At $b_0=0$, $u=31/42$, and $v=300/341$, independently of $a_0$, both factors are $x^2+x+1$, and

$$
\begin{aligned}
f(z)&=z^4+8z^3+16z^2+8z+1\\
&=\bigl(z^2+(4+\sqrt2)z+1\bigr)
\bigl(z^2+(4-\sqrt2)z+1\bigr).
\end{aligned}\tag{15}
$$

This has four distinct strictly negative roots. Nonvanishing discriminant and connectedness therefore give four distinct real roots throughout the parameter box.

Moreover, $P\geq1/3$, $Q\geq P$, $p\geq-1/10$, and $q\geq0$. These inequalities make every nonconstant coefficient in (13) strictly positive and the constant nonnegative. For example, the coefficient of $z$ is

$$
1+p+P(1+p)+Q(1+p)+Pq+q
\geq\frac9{10}+\frac9{10}P+\frac9{10}Q>0.
$$

Thus no root is positive. In the actual nonreal-pair application, $q,Q>0$, so no root is zero either. This proves the lemma. On the enlarged box boundary $q=0$, a simple zero is allowed; strict negativity is asserted for the actual factors used in the proof.

### 4.3 A bad quadratic times a real linear factor

Let

$$
h(x)=x^2+Ax+(A+e),\qquad
0\leq e\leq\frac19,\qquad (A-1)^2\leq4e,
$$

and let $1\leq\alpha\leq21/10$. Then $B(h(x)(x+\alpha))$ has three distinct strictly negative roots.

The transformed cubic is

$$
f(z)=z^3+(3+A+\alpha)z^2
+(1+2A+\alpha+\alpha A+e)z+\alpha(A+e).\tag{16}
$$

Parameterize the region by $u,v,w\in[0,1]$:

$$
y=2u-1,\qquad
A=1+\frac23y,\qquad
e=\frac{y^2+(1-y^2)v}{9},\qquad
\alpha=1+\frac{11}{10}w.\tag{17}
$$

This covers the stated curved $(A,e)$ region; when $|y|=1$, necessarily $e=1/9$, and $v$ can be chosen arbitrarily. The exact discriminant in $(u,v,w)$ has coordinate degrees $(6,3,4)$. Its $7\cdot4\cdot5=140$ Bernstein coefficients are all positive, with exact minimum

$$
\frac{72882116}{6834375}>0.\tag{18}
$$

The full list and the exact inverse conversion are supplied in `effective_cubic_certificate.json` and checked by `effective_cubic_certificate.py`. At $(u,v,w)=(1/2,0,0)$, one has $A=1$, $e=0$, $\alpha=1$, and

$$
f(z)=(z+1)(z^2+4z+1),
$$

with three distinct negative roots. Connectedness and the nonvanishing discriminant give three distinct real roots everywhere in the cube. All coefficients are strictly positive because $A\geq1/3$, $e\geq0$, and $\alpha\geq1$, so all roots are strictly negative.

Every actual bad quadratic from (7) satisfies these conditions with $A=p$ and $e=\delta$. Every actual real linear factor also fits because $1<\alpha<41/20<21/10$.

## 5 Assembly for every radius certified triple

If the number of bad quadratic factors is even, pair them arbitrarily and use Section 4.2 on each pair. If it is odd and a real linear factor exists, combine one bad quadratic with that real factor using Section 4.3, then pair the remaining bad quadratics.

Suppose instead that the number is odd and there are no real factors. There must be at least one good quadratic: otherwise all $t$-roots would have positive real part by (9), contradicting their total sum $-2$ in (5). Reserve one good quadratic and combine it with one bad quadratic using Section 4.2, then pair the remaining bad quadratics.

Unused good quadratics and real linears already have strictly negative Bell roots. Repeated factors are counted with multiplicity throughout; each factor occurrence is used once. Iterating (2) proves that $B(Q_H)$ has only real nonpositive zeros. Its constant coefficient is $Q_H(0)>0$, by (3) at $t=1$, so zero is not a root. This proves the theorem for every triple satisfying (6), including every total path length at least $72$.

## 6 Exhaustive exact verification of the finite remainder

### 6.1 The finite domain and its exact partition

By symmetry, sort the path lengths as $2\leq a\leq b\leq c$. If $c\geq69$, then $a+b+c\geq73$, so Section 3.1 applies. It therefore suffices to enumerate

$$
2\leq a\leq b\leq c\leq68.
$$

There are $\binom{69}{3}=52,394$ such triples. For each triple, put $n=a+b+c-1$. Clearing positive denominators in (6) gives the integer margin

$$
\begin{aligned}
\Delta(a,b,c)={}&21^n
-21^a20^{n-a}-21^b20^{n-b}-21^c20^{n-c}\\
&-21\cdot20^{n-1}-20^n.
\end{aligned}\tag{19}
$$

A positive margin selects the analytic branch. Every other triple must have a complete exact root certificate. The exhaustive loop uses $c=2,\ldots,68$, $b=2,\ldots,c$, and $a=2,\ldots,b$, so no ordering or symmetry case is omitted.

### 6.2 Independent integer constructions of the intended polynomial

Write

$$
Q_H(x)=\sum_{j=0}^d c_jx^j,\qquad
B(Q_H)(z)=\sum_{i=0}^d b_iz^i,
\qquad d=a+b+c-3.
$$

One direct coefficient formula follows from (4), after $t=x+1$ and division by $x^2$:

$$
c_j=\binom{a+b+c-1}{j+2}
-\binom a{j+2}-\binom b{j+2}-\binom c{j+2}.\tag{20}
$$

Binomial coefficients outside their usual range are zero. The linear and constant terms $t+1$ in (4) contribute nothing to these coefficients.

A separate construction starts with the two geometric-sum products in (3). If their convolution gives

$$
Q_H(t-1)=\sum_{k=0}^d q_kt^k,
$$

then the shift and Bell transform are

$$
c_j=\sum_{k=j}^d q_k\binom kj,\qquad
b_i=\sum_{j=i}^d c_jS(j,i).\tag{21}
$$

All these operations use integers. The Stirling numbers can be generated from $S(0,0)=1$ and

$$
S(j+1,i)=iS(j,i)+S(j,i-1).
$$

The independent finite auditor reconstructs the intended polynomial by the geometric-convolution route, checks its degree $d$, monicity and positive coefficients, and compares it with the certificate's polynomial identity. This is not a verification that merely accepts polynomial coefficients supplied by a root-finding program.

### 6.3 The exact negative root certificate criterion

For each remaining triple, the certificate lists monic integer polynomials $f_\nu(z)$ and positive integer multiplicities $m_\nu$. The checker verifies the exact coefficient identity

$$
B(Q_H)(z)=\prod_\nu f_\nu(z)^{m_\nu}.\tag{22}
$$

For each listed factor of degree $e$, it requires exactly $e$ pairwise strictly disjoint rational boxes, ordered along the negative real axis. A box is either:

- a rational singleton $r<0$ with $f_\nu(r)=0$ exactly; or
- an interval $[\ell,u]$ with $\ell<u<0$ and $f_\nu(\ell)f_\nu(u)<0$ exactly.

Strict disjointness is required within each factor. The intermediate value theorem supplies a distinct negative root in each box. Since there are degree-many boxes, these exhaust all roots of that factor and make them simple. Boxes belonging to different factors need not be disjoint: the exact product identity (22) and the recorded multiplicities handle repeated roots of the full polynomial.

Endpoint signs use homogeneous integer evaluation. For $f(z)=\sum_{j=0}^e f_jz^j$ and a rational endpoint $n/d$ with $d>0$,

$$
\mathcal E_f(n,d)=\sum_{j=0}^e f_jn^jd^{e-j}
=d^ef(n/d).\tag{23}
$$

Thus the integer $\mathcal E_f(n,d)$ has exactly the sign of $f(n/d)$. The checker uses this identity, exact integer polynomial multiplication, and degree counting. It does not trust a factorization oracle, a numerical real/nonreal classification, or an approximate root-isolator conclusion. Numerical or interval software may propose candidate boxes during certificate generation; a successful verification depends only on the exact tests just stated.

### 6.4 The completed finite verification

The supplied finite certificates and coverage record pass the complete check with the following results:

| Quantity | Exact count |
|---|---:|
| Sorted triples in the finite domain | 52,394 |
| Triples satisfying the strict radius test | 49,934 |
| Triples with complete exact root certificates | 2,460 |
| Missing triples | 0 |
| Factor-root boxes checked | 83,842 |

The $83,842$ count is the sum of the degrees of the listed factors, without multiplying by their recorded exponents; it is not a count of globally distinct numerical roots across different triples. Every exceptional quotient has degree at most $68$, and the largest exceptional path length is $67$.

The complete records are supplied in `finite_certificates.zip`, with file identities in `certificate_manifest.json` and one coverage entry per finite-domain triple in `finite_coverage.jsonl.gz`. The replay recomputes (19) for every triple. It rejects missing certificates, certificates assigned to the wrong triple, failed factor or root-box identities, and unexpected certificate files. The counts are consistency checks, not substitutes for exhaustive coverage.

It follows from (22)--(23) that every one of the $2,460$ remaining Bell quotients has only strictly negative real zeros. Together with the $49,934$ analytic branches and the unbounded analytic tail of Section 3.1, this exhausts all $a,b,c\geq2$ and proves the quotient assertion of the theorem.

## 7 Clique attachment

If $G\cap H=K_2$, chromatic complete-cutset factorization [1, Proposition 1.1] gives

$$
P_{G\cup H}=P_G\frac{P_H}{x(x+1)}=P_GQ_H.
$$

For an ordinary $\tau$-real $G$, formula (1) makes $B(P_G)$ real-rooted with nonpositive zeros. The proved quotient theorem and (2) then show that $G\cup H$ is $\tau$-real.

The theta graph itself is also $\tau$-real, since

$$
P_H=x(x+1)Q_H,\qquad B(x(x+1))=z(z+2),
$$

and the Bell-product theorem applies once more. BRW Proposition 5.12 therefore gives the empty and single-vertex overlap cases. Every cycle of $H$ uses two of its paths and has length at least four, so $H$ is triangle-free. These cases exhaust its possible complete overlaps and finish the theorem.

## 8 Reproducibility and limitations

This is an exact computer-assisted proof. The two repair lemmas use complete rational Bernstein certificates for explicit discriminants over compact parameter boxes. The finite part uses exact rational sign changes and integer factor identities. Both computational components are proof obligations, not merely illustrative numerical checks.

The accompanying `verify_all.py`, `check_certificates.py`, and `audit_finite_certificates.py` provide the package verification route. The two effective-certificate scripts reconstruct the Bernstein calculations; `finite_theta_verify.py` supplies the finite certificate generator. The mathematical acceptance conditions are stated explicitly in Sections 4.1 and 6.3, so the claims are not based on the generator's success message alone. Detailed execution and integrity information is given in the accompanying package documentation.

AI systems assisted with derivation, review passes, exact computations and manuscript preparation. AI review is not independent human peer review, and this work is not proof-assistant formalization. The theorem concerns the stated theta family; it does not establish the full $\tau$ clause of BRW Conjecture 6.5 for arbitrary pairs of $\tau$-real graphs.

### 8.1 An unresolved literature comparison

A potentially relevant paper is Lili Mu, Qi Shen and Xinyao Xu, *On the Real-rootedness, invariance, and root bounds of $\tau$-polynomials*, Discrete Mathematics, Algorithms and Applications, article 2550185 [2]. Its publisher-deposited Crossref record lists an online-publication date of 9 January 2026; some secondary listings show a 2025 date.

The full text, exact normalization, graph families, hypotheses and theorem statements of that paper have not been inspected. The accessible deposited abstract has mathematical expressions replaced by formula placeholders, and the publisher text was not accessible in the bounded literature check. Whether it subsumes, overlaps with, or differs from the present quotient and attachment theorem therefore remains unknown. Inaccessible formulas are not evidence of non-overlap. No historical priority or comprehensive-literature certificate is claimed.

## References

1. Francesco Brenti, Gordon F. Royle, and David G. Wagner. *Location of zeros of chromatic and related polynomials of graphs*. Canadian Journal of Mathematics **46** (1), 55--80 (1994). [doi:10.4153/CJM-1994-002-3](https://doi.org/10.4153/CJM-1994-002-3). Proposition 1.1 gives complete-cutset chromatic factorization; Propositions 4.2 and 4.4 give the Bell product and its root preservation; Proposition 5.1(d) gives reflection; Proposition 5.12 covers intersections of at most one vertex.

2. Lili Mu, Qi Shen, and Xinyao Xu. *On the Real-rootedness, invariance, and root bounds of $\tau$-polynomials*. Discrete Mathematics, Algorithms and Applications, article 2550185. [doi:10.1142/S179383092550185X](https://doi.org/10.1142/S179383092550185X). Bibliographic metadata: [publisher-deposited Crossref record](https://api.crossref.org/works/10.1142/S179383092550185X). The precise mathematical scope remains unverified, as explained in Section 8.1.
