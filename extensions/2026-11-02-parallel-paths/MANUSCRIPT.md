---
title: "Real rooted Bell quotients for parallel paths and five cycle substitution"
date: "2 November 2026"
lang: en
---

## Abstract

We establish three results about the ordinary Brenti--Royle--Wagner $\tau$-polynomial. First, a product inequality at the rational radius $R=21/20$ proves real-rootedness of the Bell edge quotient for any number $r\geq2$ of parallel paths. It suffices that every path length be at least $L$, where $R^L\geq1+46r$. Second, the four-path family $\Theta(2,2,2,m)$ has a Bell edge quotient with simple strictly negative roots for every $m\geq2$. This follows from an exact rational induction base and a fixed-source arrowhead invariant, whose full proof is given here. Third, replacing one vertex of a five-cycle by any ordinary $\tau$-real graph produces another ordinary $\tau$-real graph whose edge quotient is real-rooted. This operation can be iterated and permits universal ordinary edge attachment. Its proof realizes a differential operator by a nonnegatively weighted matching graph.

The parallel-path results permit attachment along every complete intersection because their factor graphs are triangle-free. The substitution result permits edge attachment but makes no assertion for larger clique intersections: its outputs can contain arbitrarily large cliques. None of the results proves general clique-overlap closure, and no historical novelty or proof-assistant verification is claimed.

## 1 Ordinary tau reality and the Bell normalization

All graphs are finite and simple. Path lengths count edges. If $G$ has $n$ vertices, let

$$
P_G(x)=(-1)^n\chi_G(-x),
$$

where $\chi_G$ is its chromatic polynomial. For the empty graph, $P_G=1$. Define the linear Bell transform by

$$
B((x)_j)=z^j,\qquad
(x)_j=x(x-1)\cdots(x-j+1),\qquad (x)_0=1.
$$

Equivalently,

$$
B(x^j)=T_j(z)=\sum_{i=0}^j S(j,i)z^i,
\qquad T_0=1,\qquad T_{j+1}=z(T_j+T_j'),
$$

where $S(j,i)$ are Stirling numbers of the second kind.

In the notation of Brenti--Royle--Wagner [1], the transforms $S$ and $T$ send falling and rising factorials, respectively, to monomials:

$$
S((x)_j)=z^j,\qquad
T\bigl(x(x+1)\cdots(x+j-1)\bigr)=z^j.
$$

Thus $B=S$. With reflection $(\varepsilon f)(x)=f(-x)$, one has $B=\varepsilon T\varepsilon$, and [1, Proposition 5.1(d)] gives

$$
B(P_G)(z)=(-1)^n\tau_{\mathrm{BRW}}(G,-z).\tag{1}
$$

Consequently real-rootedness of $B(P_G)$ is precisely ordinary BRW $\tau$-reality, not $\sigma$-reality of $\chi_G$. Deletion--contraction gives $P_G=P_{G-e}+P_{G/e}$, so $P_G$ has nonnegative coefficients. The same is true of $B(P_G)$. When its roots are real, therefore, they are nonpositive.

We use the Bell product

$$
(f*g)(z)=\sum_{j\geq0}\frac{z^j}{j!}f^{(j)}(z)g^{(j)}(z).
$$

By [1, Propositions 4.2 and 4.4],

$$
B(FG)=B(F)*B(G),\tag{2}
$$

and $f*g$ has only real nonpositive roots whenever both $f$ and $g$ do.

### 1.1 The edge attachment interface

For a graph $H$ with an edge, put

$$
Q_H(x)=\frac{P_H(x)}{x(x+1)}.
$$

The denominator divides $P_H$. An ordinary attachment $G\cup H$ retains the common graph, makes no further identifications, and adds no cross edges between the exclusive sides. If $G\cap H=K_2$, complete-cutset factorization [1, Proposition 1.1] gives

$$
P_{G\cup H}=P_GQ_H.\tag{3}
$$

Thus a real-rooted $B(Q_H)$ with nonpositive roots supplies universal edge attachment to every ordinary $\tau$-real $G$, by (1)--(2). It also proves that $H$ itself is $\tau$-real, since

$$
P_H=x(x+1)Q_H,\qquad B(x(x+1))=z(z+2).
$$

The known empty and one-vertex overlap cases [1, Proposition 5.12] then apply. If $H$ is triangle-free, these cases and an edge exhaust its complete intersections. We will use this interface for all three results; only the triangle-free results yield every complete intersection in this way.

For differential calculations, write

$$
D=\frac{d}{dz},\qquad \mathcal S=1+D,\qquad L=z\mathcal S.
$$

Here $\mathcal S$ is a differential operator, distinct from the BRW transform $S=B$. The Bell identities are

$$
B(xF)=L B(F),\qquad
B(F(x+1))=\mathcal S B(F),\qquad
B((x+1)F)=\bigl(zD+z+1\bigr)B(F).\tag{4}
$$

## 2 The quotient for any number of parallel paths

Let $H=\Theta(\ell_1,\ldots,\ell_r)$ consist of $r\geq2$ internally vertex-disjoint paths of lengths $\ell_i\geq2$ with the same two distinct endpoints. Set

$$
N=\sum_{i=1}^r\ell_i,\qquad |V(H)|=N-r+2,\qquad
S_j(t)=1+t+\cdots+t^{j-1},\quad S_0(t)=0,\quad t=x+1.
$$

The geometric sum $S_j(t)$ is unrelated to the transform $S$. With endpoint colors prescribed equal or distinct, the respective internal-coloring counts for a path of length $\ell$ are

$$
E_\ell(q)=\frac{(q-1)^\ell+(q-1)(-1)^\ell}{q},\qquad
D_\ell(q)=\frac{(q-1)^\ell-(-1)^\ell}{q}.
$$

These follow, for example, from the two-state endpoint-color recurrence; the displayed expressions are polynomials after cancellation. Choosing the common endpoint colors gives

$$
\chi_H(q)=q\prod_{i=1}^rE_{\ell_i}(q)
+q(q-1)\prod_{i=1}^rD_{\ell_i}(q).
$$

At $q=1-t$,

$$
E_\ell(1-t)=(-1)^{\ell+1}tS_{\ell-1}(t),\qquad
D_\ell(1-t)=(-1)^{\ell+1}S_\ell(t).
$$

The reflection sign cancels all parity dependence, because
$|V(H)|+\sum_i(\ell_i+1)=2N+2$ is even. After division by $x(x+1)$, this proves

$$
Q_H(t-1)=\prod_{i=1}^rS_{\ell_i}(t)
-t^{r-1}\prod_{i=1}^rS_{\ell_i-1}(t).\tag{5}
$$

This is a polynomial identity, including at $t=1$.

The degree is $d=N-r$. The first product in (5) is monic of degree $d$ and has next coefficient $r$; the subtracted term is monic of degree $d-1$. Hence

$$
\sum_{Q_H(t_j-1)=0}t_j=-(r-1),\tag{6}
$$

with roots counted with multiplicity.

There is also a coefficientwise positivity argument. A monomial choice in the subtracted product is indexed by $0\leq k_i\leq\ell_i-2$, with exponent $r-1+\sum_i k_i$. Add one to its first $r-1$ coordinates and leave its last coordinate unchanged. This injects these choices, preserving the exponent, into the monomial choices of the first product. The image misses the constant monomial. Therefore $Q_H(t-1)$ has nonnegative $t$-coefficients and constant $1$. In particular,

$$
Q_H(t-1)>0\quad(t\geq0),\qquad
Q_H(0)=\prod_i\ell_i-\prod_i(\ell_i-1)>0.\tag{7}
$$

Every real $t$-root is thus strictly negative. The same coloring calculation and (5) also hold for a single path; this special case will be used only as a corollary in Section 5.

## 3 Long parallel paths with unrestricted path count

**Theorem 1.** Let $r\geq2$, let $\ell_i\geq2$, and set $R=21/20$. If

$$
\prod_{i=1}^r\frac{R^{\ell_i}+R}{R^{\ell_i}-1}<R,\tag{8}
$$

then $B(Q_H)$ has only strictly negative real roots. Consequently $H$ can be ordinarily attached to any ordinary $\tau$-real graph along any complete intersection while preserving ordinary $\tau$-reality.

In particular, (8) holds whenever every $\ell_i\geq L$ and

$$
R^L\geq1+46r.
$$

A sufficient minimum length is therefore

$$
L(r)=\min\{L\in\mathbb Z:L\geq2,\ 21^L\geq(1+46r)20^L\}
=\left\lceil\frac{\log(1+46r)}{\log(21/20)}\right\rceil.\tag{9}
$$

This is a sufficient bound, not an asserted optimal threshold. The cases $r=2$ and $r=3$ overlap cycle and three-path results; no all-length conclusion for arbitrary $r\geq4$ is asserted.

### 3.1 The product radius bound

Multiply (5) by $(t-1)^r$. If $t$ is a root with $\rho=|t|>1$, the factors $t^{\ell_i}-1$ do not vanish, and rearrangement gives

$$
t=\prod_{i=1}^r
\frac{1-t^{-(\ell_i-1)}}{1-t^{-\ell_i}}.
$$

It follows that

$$
\rho\leq\prod_{i=1}^r
\frac{1+\rho^{-(\ell_i-1)}}{1-\rho^{-\ell_i}}
=\prod_{i=1}^r\frac{\rho^{\ell_i}+\rho}{\rho^{\ell_i}-1}.\tag{10}
$$

For every integer $\ell\geq2$,

$$
f_\ell(\rho)=\frac{\rho^\ell+\rho}{\rho^\ell-1}
=1+\frac{\rho+1}{\rho^\ell-1}
$$

is strictly decreasing on $\rho>1$: the numerator of the derivative of its second term is

$$
\rho^\ell-1-\ell\rho^{\ell-1}(\rho+1)
=-(\ell-1)\rho^\ell-\ell\rho^{\ell-1}-1<0.
$$

If $\rho\geq R$, (8) makes the right side of (10) less than $R\leq\rho$, a contradiction. Thus

$$
|t_j|<R\quad\text{for every root of }Q_H(t-1).\tag{11}
$$

### 3.2 The precise factor repair input

We use two radius-disk repair lemmas from the public all-theta proof [3, Section 4]. That reference and its complete rational certificates are fixed at commit `cfa1f5fd798116b44ddc95da6f90710e48fac14a`; they are not finite tests of the present $r$-path family. We state the lemmas and explain their exact acceptance conditions.

A nonreal conjugate $t$-pair gives a real monic factor

$$
h(x)=x^2+px+q,\qquad p=2-2\operatorname{Re}t,\qquad q=|t-1|^2>0,
$$

and

$$
B(h)=z^2+(p+1)z+q.
$$

Call it good if $J=(p+1)^2-4q\geq0$, and bad otherwise. A good factor has strictly negative Bell roots because $p+1>3-2R=9/10$. For a bad factor, put $\delta=q-p=|t|^2-1$. Then

$$
J=(p-1)^2-4\delta<0,\qquad
0<\delta<\frac{41}{400}<\frac19,
\qquad |p-1|<\frac23,
\qquad \operatorname{Re}t>\frac16.\tag{12}
$$

The two repair lemmas are as follows.

- If $h_1$ is a bad quadratic from the radius-$R$ disk and $h_2$ is any nonreal conjugate-pair quadratic from the same disk, then $B(h_1h_2)$ has four distinct strictly negative roots.
- If $h=x^2+Ax+(A+e)$, $0\leq e\leq1/9$, $(A-1)^2\leq4e$, and $1\leq\alpha\leq21/10$, then $B(h(x)(x+\alpha))$ has three distinct strictly negative roots.

Here and below $h(x)(x+\alpha)$ denotes multiplication, not substitution into $h$.

For the first lemma, enlarge to parameters $a,b,u,v\in[0,1]$ and put

$$
\begin{aligned}
P&=1+\frac23b(2a-1),&Q&=P+\frac{b^2}{9},\\
p&=2+2R-4Ru,&q&=(1+R-2Ru)^2+4R^2u(1-u)v.
\end{aligned}\tag{13}
$$

These cover the bad-factor region for $x^2+Px+Q$ and the entire radius disk for the second quadratic. Direct expansion gives

$$
\begin{aligned}
f(z)=B\bigl((x^2+Px+Q)(x^2+px+q)\bigr)
={}&z^4+(6+P+p)z^3\\
&+\bigl(7+3(P+p)+Q+q+Pp\bigr)z^2\\
&+\bigl(1+P+p+Q+q+Pp+Pq+pQ\bigr)z+Qq.
\end{aligned}\tag{14}
$$

Its discriminant, after (13), has coordinate degrees $(10,5,6,10)$ in $(u,v,a,b)$. All $5,082$ tensor Bernstein coefficients are strictly positive, with exact minimum

$$
\frac{1319869198532766581}{19683000000000000}>0.\tag{15}
$$

For precision, if a polynomial of coordinate degrees $\mathbf n$ has power coefficients $c_{\mathbf j}$, the Bernstein coefficients used here are

$$
\beta_{\mathbf i}=\sum_{\mathbf j\leq\mathbf i}
c_{\mathbf j}\prod_\ell
\frac{\binom{i_\ell}{j_\ell}}{\binom{n_\ell}{j_\ell}}.
$$

The certificate verifies positivity of every rational $\beta_{\mathbf i}$ and reconstructs the power coefficients by

$$
c_{\mathbf j}=
\left(\prod_\ell\binom{n_\ell}{j_\ell}\right)
\sum_{\mathbf i\leq\mathbf j}(-1)^{|\mathbf j-\mathbf i|}
\beta_{\mathbf i}\prod_\ell\binom{j_\ell}{i_\ell}.\tag{16}
$$

The tensor Bernstein basis is nonnegative and sums to one on the cube, so (15)--(16) prove a strictly positive discriminant throughout that cube. At $b=0$, $u=31/42$, $v=300/341$, both factors equal $x^2+x+1$ and

$$
f(z)=z^4+8z^3+16z^2+8z+1
=\bigl(z^2+(4+\sqrt2)z+1\bigr)
 \bigl(z^2+(4-\sqrt2)z+1\bigr).
$$

This has four distinct negative roots. A continuous monic real-polynomial family cannot change its number of real roots without a repeated root. Connectedness of the cube and the nonvanishing discriminant therefore give four distinct real roots everywhere in the cube. The inequalities $P\geq1/3$, $Q\geq P$, $p\geq-1/10$, $q\geq0$ make the nonconstant coefficients of (14) positive. Thus no root is positive. For the actual nonreal factors, $Qq>0$, excluding zero as well. Boundary points with $q=0$ need not have strictly negative roots; they are not used as nonreal factors.

For the second lemma, direct expansion gives

$$
B(h(x)(x+\alpha))
=z^3+(3+A+\alpha)z^2
+(1+2A+\alpha+\alpha A+e)z+\alpha(A+e).\tag{17}
$$

The parameterization

$$
y=2u-1,\quad A=1+\frac23y,\quad
e=\frac{y^2+(1-y^2)v}{9},\quad
\alpha=1+\frac{11}{10}w,\qquad u,v,w\in[0,1]
$$

covers its hypotheses. The discriminant has coordinate degrees $(6,3,4)$; all $140$ Bernstein coefficients are positive, with exact minimum

$$
\frac{72882116}{6834375}>0.\tag{18}
$$

The same exact conversion and inverse reconstruction are checked. At $(u,v,w)=(1/2,0,0)$, the cubic is $(z+1)(z^2+4z+1)$. Connectedness gives three distinct real roots throughout the cube, and its positive coefficients make them strictly negative. The full coefficient lists and regeneration programs for both lemmas are publicly available in [3]. Their mathematical role is positivity on entire parameter boxes, not extrapolation from sampled parameters.

### 3.3 Assembly for all path counts

Factor $Q_H$ over $\mathbb R$, retaining multiplicities. By (7) and (11), a real $t$-root gives a linear factor $x+\alpha$ with

$$
1<\alpha<1+R=41/20<21/10.
$$

Its Bell transform already has a negative root. Good quadratic factors also already have strictly negative Bell roots.

If the number of bad quadratics is even, group them in pairs and apply the first repair lemma. If it is odd and a real linear factor exists, combine one bad quadratic with that real factor by the second lemma and pair the rest.

If it is odd and no real factors exist, at least one good quadratic must exist. Otherwise every $t$-root would have positive real part by (12), contradicting the negative root sum (6). Reserve one good quadratic, combine it with one bad quadratic by the first lemma, and pair the remaining bad quadratics.

Each factor occurrence is used once, so repeated factors present no difficulty. All resulting groups have Bell transforms with negative real roots. Iterating (2) proves that $B(Q_H)$ has only real nonpositive roots. Equation (7) gives $B(Q_H)(0)=Q_H(0)>0$, so no zero root occurs. The edge-attachment interface of Section 1.1 now applies. Every cycle of $H$ uses two paths and has length at least four, so $H$ is triangle-free and every complete intersection is covered.

### 3.4 The explicit minimum length bound

If $\ell_i\geq L$ and $R^L\geq1+46r$, then

$$
f_{\ell_i}(R)=1+\frac{R+1}{R^{\ell_i}-1}
\leq1+\frac{41}{920r}<1+\frac{1}{22r}.
$$

Since $\binom rk\leq r^k$, the binomial theorem gives

$$
\left(1+\frac{1}{22r}\right)^r
\leq\sum_{k=0}^r\left(\frac1{22}\right)^k
<\sum_{k=0}^\infty\left(\frac1{22}\right)^k
=\frac{22}{21}<\frac{21}{20}=R.
$$

This proves (8) and completes Theorem 1. For example, the sufficient bounds are $L(4)=107$, $L(5)=112$, $L(10)=126$, and $L(100)=173$. These follow from exact integer comparisons in (9); they are not claims about sharp thresholds.

## 4 Every member of the four path family Theta 2 2 2 m

**Theorem 2.** For every integer $m\geq2$, let $H_m=\Theta(2,2,2,m)$. Then $B(Q_{H_m})$ has only simple strictly negative roots. Ordinary attachment of $H_m$ to any ordinary $\tau$-real graph along any complete intersection preserves ordinary $\tau$-reality.

### 4.1 Exact recurrence and the fixed source

Equation (5) gives, for $m\geq1$,

$$
Q_{H_m}(t-1)=(t+1)^3S_m(t)-t^3S_{m-1}(t).
$$

Introduce the algebraic seed $Q_0(t-1)=t^2$. This is not an assertion about a length-zero simple graph. The sequence agrees with the displayed graph quotient for $m\geq1$ and satisfies

$$
Q_{m+1}(t-1)=tQ_m(t-1)+C(t),\qquad
C(t)=(t+1)^3-t^3=3t^2+3t+1.\tag{19}
$$

Indeed the first step gives $Q_1(t-1)=(t+1)^3$, and $S_{m+1}=tS_m+1$ proves every later step. Thus, by (4), the polynomials $F_m=B(Q_m)$ obey

$$
F_0=z^2+3z+1,\qquad
F_{m+1}=zF_m'+(z+1)F_m+h,\qquad
h=3z^2+12z+7.\tag{20}
$$

In particular, $F_m$ is monic of degree $m+2$ and $F_m(0)=1+7m$.

### 4.2 A general fixed source arrowhead invariant

The following lemma permits any fixed real polynomial source of degree below the current polynomial. In particular it is not restricted to a linear source.

**Lemma.** Let $f$ be monic of degree $n\geq2$, with distinct strictly negative roots $r_1,\ldots,r_n$. Let $h$ be real, $\deg h<n$, and $h(0)>0$. Define

$$
R_i=-r_i>0,\qquad a_i=\frac{h(r_i)}{f'(r_i)},\qquad
\kappa_i=\frac{a_i}{R_i},\qquad
w=\frac{h(0)}{f(0)},\qquad
V=\sum_i\frac{\kappa_i^2}{1-\kappa_i}.
$$

If

$$
|\kappa_i|<1\quad\text{for all }i,\qquad
0<w\leq\frac27,\qquad V\leq2w,\tag{21}
$$

then

$$
g=zf'+(z+1)f+h
$$

is monic of degree $n+1$ with distinct strictly negative roots. With the same $h$, its new quantities satisfy

$$
|\kappa'_j|<1,\qquad
w'=\frac{w}{1+w}\leq\frac27,\qquad V'\leq2w'.\tag{22}
$$

**Proof.** Partial fractions and evaluation at zero give

$$
\frac{h(z)}{f(z)}=\sum_i\frac{a_i}{z-r_i},\qquad
\sum_i\kappa_i=w.
$$

Consequently,

$$
\frac{g(z)}{f(z)}
=z+n+1+\sum_i\frac{r_i+a_i}{z-r_i}
=z+n+1-\sum_i\frac{b_i^2}{z-r_i},\qquad
b_i=\sqrt{R_i-a_i}>0.\tag{23}
$$

The last inequality follows from $\kappa_i<1$. Thus $g$ is the characteristic polynomial of the real symmetric arrowhead matrix

$$
M=\begin{pmatrix}
\operatorname{diag}(r_i)&b\\
b^{\mathsf T}&-(n+1)
\end{pmatrix}.
$$

Put $A=-M$ and $\Delta=\operatorname{diag}(R_i)$. The upper-left block $\Delta$ is positive definite; its Schur complement in $A$ is

$$
n+1-b^{\mathsf T}\Delta^{-1}b
=n+1-\sum_i(1-\kappa_i)=1+w>0.
$$

Hence $A$ is positive definite and every eigenvalue of $M$ is negative. On each interval complementary to the poles, the right side of (23) has derivative

$$
1+\sum_i\frac{b_i^2}{(z-r_i)^2}>0.
$$

Its one-sided limits give exactly one zero on each of the $n+1$ complementary intervals. No pole is a zero of $g$, because $g(r_i)=-b_i^2f'(r_i)\ne0$. Therefore the roots of $g$ are distinct and strictly negative.

To control the new residues, put $c_i=a_i/(2b_i)$ and

$$
E=\begin{pmatrix}0&c\\c^{\mathsf T}&0\end{pmatrix}.
$$

Let $s_j$ be a root of $g$ and $v_j$ a normalized real eigenvector of $M$ for $s_j$. Its last coordinate is nonzero, and

$$
(v_j)_i=\frac{b_i(v_j)_{n+1}}{s_j-r_i},\qquad
(v_j)_{n+1}^2=
\frac{1}{1+\sum_i b_i^2/(s_j-r_i)^2}.
$$

Using (23) and $g(s_j)=0$ yields

$$
v_j^{\mathsf T}Ev_j
=\frac{\sum_i a_i/(s_j-r_i)}
 {1+\sum_i b_i^2/(s_j-r_i)^2}
=\frac{h(s_j)}{g'(s_j)}.\tag{24}
$$

Now let $K=A^{-1/2}EA^{-1/2}$. Since $Av_j=(-s_j)v_j$, its diagonal entries in the orthonormal eigenbasis $v_j$ are

$$
v_j^{\mathsf T}Kv_j
=\frac{h(s_j)}{(-s_j)g'(s_j)}=\kappa'_j.\tag{25}
$$

The two nonzero eigenvalues of the rank-two matrix $K$ are the generalized eigenvalues of $Ev=\lambda Av$. For $\lambda\ne0$, the upper-left block of $E-\lambda A$ is $-\lambda\Delta$. Taking its Schur complement, and using

$$
c^{\mathsf T}\Delta^{-1}b=\frac w2,\qquad
c^{\mathsf T}\Delta^{-1}c=\frac V4,
$$

gives

$$
(1+w)\lambda^2-w\lambda-\frac V4=0.\tag{26}
$$

Indeed the Schur complement is $-\lambda(1+w)+w+V/(4\lambda)$. Since $w>0$, at least one $a_i\ne0$, so $V>0$ and $E$ has rank two. Equation (26) has one positive root $\lambda_+$ and one negative root $\lambda_-$. Its values at $1$ and $-1$ are respectively $1-V/4>0$ and $1+2w-V/4>0$, because $V\leq2w\leq4/7<4$. Hence

$$
-1<\lambda_-<0<\lambda_+<1.
$$

The remaining eigenvalues of $K$ are zero. Every diagonal entry in any orthonormal basis is a convex combination of its eigenvalues, so (25) proves $|\kappa'_j|<1$.

Finally,

$$
\phi(u)=\frac{u^2}{1-u}=\frac1{1-u}-1-u
$$

is convex for $u<1$, since $\phi''(u)=2/(1-u)^3>0$. Orthogonally diagonalize $K$ and apply scalar Jensen to each diagonal entry. Summing, and using the row and column squared-norm identities of an orthogonal matrix, gives

$$
V'=\sum_j\phi(\kappa'_j)
\leq\phi(\lambda_+)+\phi(\lambda_-).\tag{27}
$$

The zero eigenvalues contribute $\phi(0)=0$. From (26),

$$
\lambda_++\lambda_-=\frac{w}{1+w},\qquad
\lambda_+\lambda_-=-\frac{V}{4(1+w)}.
$$

Thus the right side of (27) equals

$$
\Phi(V,w)=\frac{2+w}{1-V/4}-2-\frac{w}{1+w}.
$$

It is increasing in $V<4$. Since $V\leq2w$,

$$
V'\leq\Phi(2w,w),\qquad
\frac{2w}{1+w}-\Phi(2w,w)
=\frac{w(2-7w)}{(2-w)(1+w)}\geq0.
$$

Also $g(0)=f(0)+h(0)$, so $w'=w/(1+w)\leq2/7$. This gives $V'\leq2w'$ and proves the lemma. $\square$

### 4.3 A fully specified rational induction base

The ascending coefficient lists of $F_0,\ldots,F_4$, reconstructed from (20), are

$$
\begin{aligned}
F_0 &: [1,3,1],\\
F_1 &: [8,19,9,1],\\
F_2 &: [15,58,49,13,1],\\
F_3 &: [22,143,208,101,18,1],\\
F_4 &: [29,320,770,612,191,24,1].
\end{aligned}\tag{28}
$$

All terminating decimals in the next tables denote exact rational numbers. For $m=0,1,2,3$, the following disjoint negative intervals have the listed endpoint signs of $F_m$. Each row supplies exactly $\deg F_m$ intervals.

| $m$ | Root intervals in increasing order | Endpoint signs in the same order |
|---:|---|---|
| $0$ | $(-2.6181,-2.6180)$; $(-0.3820,-0.3819)$ | $(+,-)$; $(-,+)$ |
| $1$ | $(-6.1005,-6.1004)$; $(-2.3389,-2.3388)$; $(-0.5607,-0.5606)$ | $(-,+)$; $(+,-)$; $(-,+)$ |
| $2$ | $(-7.4015,-7.4014)$; $(-3.7052,-3.7051)$; $(-1.5378,-1.5377)$; $(-0.3557,-0.3556)$ | $(+,-)$; $(-,+)$; $(+,-)$; $(-,+)$ |
| $3$ | $(-9.5287,-9.5286)$; $(-4.9700,-4.9699)$; $(-2.3702,-2.3701)$; $(-0.9178,-0.9177)$; $(-0.2136,-0.2135)$ | $(-,+)$; $(+,-)$; $(-,+)$; $(+,-)$; $(-,+)$ |

For $f=F_4$ and $h=3z^2+12z+7$, the exact root and residue data are:

| Root interval $I_i$ | Signs of $f$ at the endpoints | A rational enclosure for $\kappa_i$ |
|---|---|---|
| $(-11.62810958,-11.62810957)$ | $(+,-)$ | $(-0.000450,-0.000449)$ |
| $(-6.60727567,-6.60727566)$ | $(-,+)$ | $(0.002892,0.002893)$ |
| $(-3.50632808,-3.50632807)$ | $(+,-)$ | $(-0.001066,-0.001065)$ |
| $(-1.58861933,-1.58861932)$ | $(-,+)$ | $(-0.019158,-0.019157)$ |
| $(-0.54542894,-0.54542893)$ | $(+,-)$ | $(-0.028264,-0.028263)$ |
| $(-0.12423842,-0.12423841)$ | $(-,+)$ | $(0.287423,0.287424)$ |

Here is the exact certificate criterion. For a rational interval $I_i$, evaluate $f$ at both endpoints using rational Horner arithmetic and check the displayed strict opposite signs. Evaluate $f'$ and $h$ on $I_i$ by interval Horner arithmetic. Multiply the enclosure of $f'$ by $-I_i$ and check that the resulting denominator interval excludes zero before interval division. Dividing the enclosure of $h$ by that denominator gives a rational enclosure of

$$
\kappa_i=\frac{h(r_i)}{(-r_i)f'(r_i)}
$$

inside the last table column. All operations are additions, multiplications and comparisons of rational numbers. The intermediate value theorem gives a distinct negative root in each interval; degree counting exhausts the roots and proves simplicity. Thus these tables do not depend on numerical root classification.

The full rational enclosures, the coefficients reconstructed from (20), and exact endpoint signs are supplied in [the base certificate](theta222m_exact_base.json); [the base checker](theta222m_exact_base.py) replays the rational inequalities. The displayed residue enclosures are outward rational simplifications of those full enclosures.

In particular, the first five residues have $|\kappa_i|<1/20$ and the last has $|\kappa_6|<1/3$. For $|u|\leq c<1$ one has $u^2/(1-u)\leq c^2/(1-c)$, so

$$
V<5\frac{(1/20)^2}{1-1/20}+\frac{(1/3)^2}{1-1/3}
=\frac{41}{228}<\frac{14}{29}=2w,\qquad
w=\frac7{29}<\frac27.\tag{29}
$$

Every hypothesis of the lemma holds at $F_4$. Apply it repeatedly with this fixed quadratic $h$. The degree condition remains valid, the roots remain simple and negative, and $w$ decreases by $w\mapsto w/(1+w)$. This is an unbounded induction for every $m\geq4$, not an inference from a finite root sweep. The explicitly certified smaller polynomials cover $m=0,1,2,3$.

For graph lengths $m\geq2$, (19)--(20) identify $F_m=B(Q_{H_m})$. The attachment interface applies, and $H_m$ is triangle-free. This completes Theorem 2.

## 5 Five cycle substitution with any ordinary tau real input

**Theorem 3.** Let $F$ be any finite simple ordinary $\tau$-real graph, including the empty graph. Add four new vertices $u,a,b,v$ inducing the path $u-a-b-v$, and join every vertex of $F$ to both $u$ and $v$, adding no other edges. Call the resulting graph $H$.

Then $B(Q_H)$ has only real nonpositive roots, $H$ is ordinary $\tau$-real, and $H$ can be ordinarily attached along any edge to any ordinary $\tau$-real graph while preserving ordinary $\tau$-reality. The operation is iterable: its output again satisfies the ordinary $\tau$-real input hypothesis.

Equivalently, $H$ is obtained by replacing one vertex of a five-cycle by $F$, preserving its internal edges and making its two former neighbors adjacent to every vertex of $F$. For empty $F$ the result is the four-vertex path. No real-rootedness hypothesis on a quotient of $P_F$ is required.

### 5.1 The positive weighted matching operator

We first prove that

$$
\mathcal A=z^2\mathcal S^4
+z\mathcal S^2(3+4D)+\mathcal S(1+3D)\tag{30}
$$

preserves the cone of real polynomials with nonnegative coefficients and only nonpositive roots. This is a cone-preservation statement, not preservation of all real-rooted polynomials without sign restrictions.

For $n\geq0$, start with six core vertices $0,1,2,3,4,5$. Its only core edges are $01$, $12$, $23$, with weights $2$, $1/2$, $1/2$, respectively; vertices $4,5$ have no core edges. Add $n$ ordinary pairs $(r_i,r'_i)$. Each $r_i$ is joined to $2$ with weight $1/2$. Each $r'_i$ is joined to $1,2,4,5$ with weights $1,1/2,1,1$, respectively. There are initially no diagonal edges $r_ir'_i$ and no further edges.

Let $m_j$ be the sum of products of edge weights over all $j$-edge matchings. Define the reverse matching polynomial

$$
R_n(z)=\sum_jm_jz^{n+2-j}.
$$

This is a polynomial: $\{r'_1,\ldots,r'_n,1,2\}$ is a vertex cover of size $n+2$, so every matching has size at most $n+2$.

We now count all matchings for arbitrary $n$. The possible core matchings $M$ are the empty matching, one of the three core edges, or the pair $\{01,23\}$. Their weights are $1,2,1/2,1/2,1$. Only support vertices

$$
U=\{1,2,4,5\}
$$

receive ordinary attachments. Set $a_1=a_4=a_5=0$, $a_2=1/2$, and $b_s=1-a_s$ for $s\in U$. For disjoint subsets $A,B\subseteq U\setminus V(M)$, choose attachments using unprimed ordinary vertices at $A$ and primed ordinary vertices at $B$. There are independently $(n)_{|A|}$ and $(n)_{|B|}$ injective choices of the two endpoint types. Using $r_i$ and $r'_i$ together is allowed, since no diagonal is present. Thus the exact contribution to $m_{|M|+|A|+|B|}$ is

$$
\operatorname{wt}(M)(n)_{|A|}(n)_{|B|}
\prod_{s\in A}a_s\prod_{s\in B}b_s.\tag{31}
$$

For an explicit short expansion, let $u$ count matching edges, and let $a,b$ mark the two attachment types before assigning their ordinary vertices. Conditioning on the five core matchings gives

$$
\begin{aligned}
\mathcal F(u,a,b)={}&(1+bu)^3\left(1+\frac{(a+b)u}{2}\right)\\
&+2u(1+bu)^2\left(1+\frac{(a+b)u}{2}\right)\\
&+\frac u2(1+bu)^2+\frac u2(1+bu)^3
+u^2(1+bu)^2.
\end{aligned}\tag{32}
$$

Replace every $a^ib^j$ by $(n)_i(n)_j$ and read the coefficients of $u$. This is precisely the finite formula (31), and expansion yields

$$
\begin{aligned}
m_0&=1,&m_1&=4n+3,\\
m_2&=6n^2+4n+1,&m_3&=n(4n^2-n+1),\\
m_4&=n(n-1)(n^2-n+1),&m_j&=0\quad(j\geq5).
\end{aligned}\tag{33}
$$

The formal falling-factorial calculation proves these identities for all $n$, not for a sample of degrees. Normal ordering (30) gives coefficients of $D^0,\ldots,D^4$ equal to

$$
z^2+3z+1,\quad
4z^2+10z+4,\quad
6z^2+11z+3,\quad
4z^2+4z,\quad z^2.
$$

Applying this operator to $z^n$ and collecting powers produces exactly (33). Hence

$$
R_n=\mathcal A(z^n)\qquad(n\geq0).\tag{34}
$$

For $n=0,1$, any terms with apparently negative exponents have zero coefficients; the vertex-cover proof already guarantees polynomiality. The exact symbolic expansion is also replayed by [the core identity checker](certify_short_branch_core.py), with [its rational identity record](certify_short_branch_core.json).

### 5.2 Diagonal edge lifting and Heilmann Lieb normalization

Let

$$
f(z)=\prod_{i=1}^n(z+\alpha_i),\qquad \alpha_i\geq0.
$$

Add a diagonal edge $r_ir'_i$ of weight $\alpha_i$ for each $i$. The same vertex cover remains valid. Classify a matching by its exact subset $J$ of used diagonal edges. Remove the endpoints of the selected diagonals. Every unselected diagonal is forbidden within this class, so the remaining allowed non-diagonal graph is exactly the baseline graph with $n-|J|$ ordinary pairs.

Selecting $|J|$ diagonals reduces the reverse exponent by $|J|$. Thus the reverse matching polynomial of the weighted graph is

$$
\begin{aligned}
R_G(z)
&=\sum_{J\subseteq[n]}\left(\prod_{i\in J}\alpha_i\right)R_{n-|J|}(z)\\
&=\mathcal A\left[\sum_{J\subseteq[n]}
\left(\prod_{i\in J}\alpha_i\right)z^{n-|J|}\right]
=\mathcal A f(z).
\end{aligned}\tag{35}
$$

All weights are nonnegative. The weighted Heilmann--Lieb theorem [2] applies to general graphs, not only bipartite graphs: with $m_j$ the nonnegative weighted matching counts,

$$
\mu_G(y)=\sum_j(-1)^jm_jy^{|V(G)|-2j}
$$

has only real roots. The auxiliary graph here need not be bipartite; diagonal edges can create triangles. Since $|V(G)|=2n+6$, the normalization is exactly

$$
\mu_G(y)=(-1)^{n+2}y^2R_G(-y^2).\tag{36}
$$

If a nonzero root $\zeta$ of $R_G$ were not a negative real number, a square root of $-\zeta$ would be a nonreal zero of $\mu_G$, contradicting Heilmann--Lieb. Therefore all roots of $R_G=\mathcal A f$ are real and nonpositive; a zero root is allowed. Repeated $\alpha_i$, zero $\alpha_i$, and $n=0$ present no difficulty. Nonnegative leading scaling and the zero polynomial complete the stated cone-preservation result.

### 5.3 The exact coloring identity for substitution

Condition on the colors of $u$ and $v$. If distinct, there are $q(q-1)$ ordered choices; $F$ must avoid both colors and contributes $\chi_F(q-2)$. The path of length three contributes $D_3(q)$. If equal, there are $q$ choices, and the two factors are $\chi_F(q-1)$ and $E_3(q)$. Hence

$$
\chi_H(q)=q(q-1)D_3(q)\chi_F(q-2)
+qE_3(q)\chi_F(q-1),\tag{37}
$$

where

$$
q(q-1)D_3(q)=(q-1)\bigl((q-1)^3+1\bigr),\qquad
qE_3(q)=(q-1)^3-(q-1).
$$

Since $|V(H)|=|V(F)|+4$, unsigned reflection gives

$$
P_H(x)=x(x+1)\left[
(x^2+3x+3)P_F(x+2)-(x+2)P_F(x+1)\right].\tag{38}
$$

Using (4),

$$
B(Q_H)=\left[(L^2+3L+3)\mathcal S^2-(L+2)\mathcal S\right]B(P_F)
=\mathcal A B(P_F).\tag{39}
$$

The last equality follows by normal ordering, or by the displayed derivative coefficients after (33). Ordinary $\tau$-reality of $F$ places $B(P_F)$ directly in the nonnegative-coefficient, nonpositive-root cone. Section 5.2 therefore proves that $B(Q_H)$ has only nonpositive real roots. No division of $P_F$ by $x$ or by any clique factor occurs. In particular the empty input $P_F=1$ is covered.

By Section 1.1, $H$ is ordinary $\tau$-real and supplies universal ordinary edge attachment. Since $H$ itself is an allowed input, the substitution can be iterated. This proves Theorem 3.

### 5.4 The short parallel path corollary and the clique limit

Take $F$ to be an edgeless graph on $k\geq0$ vertices. Then $P_F=x^k$, $B(P_F)=T_k$, and the output consists of $k$ length-two branches and one length-three branch. Its quotient is

$$
Q_k(x)=(x+2)^k(x^2+3x+3)-(x+1)^k(x+2),\qquad
B(Q_k)=\mathcal A T_k.\tag{40}
$$

For $k=0$ this is the ordinary path of length three, not a generalized theta graph; for $k=1$ it is $C_5$. For $k\geq2$ it is $\Theta(2^k,3)$ with $r=k+1$ parallel paths. This is a corollary of Theorem 3, not a separate hypothesis or a fourth result. Its Bell quotient has strictly negative roots, because

$$
B(Q_k)(0)=Q_k(0)=3\cdot2^k-2>0.
$$

These factor graphs are triangle-free, so their complete intersections are exhausted by the cases in Section 1.1.

For general $F$, however, the output can contain triangles or arbitrarily large cliques: for example, the vertices of a clique in $F$, together with $u$, still form a clique. Theorem 3 asserts universal **edge** attachment, not attachment along cliques of size greater than two. It is not a general graph-substitution closure theorem.

## 6 Research boundary and exact verification

The three results use distinct sufficient mechanisms. Theorem 1 requires a sufficiently large minimum path length, not merely a large maximum. Theorem 2 proves every $m\geq2$ for one four-path family by an invariant. Theorem 3 allows arbitrary ordinary $\tau$-real substitution inputs, but supplies only the edge-quotient attachment interface for its potentially non-triangle-free outputs.

The radius restriction in Theorem 1 is a limitation of that proof method. For $\Theta(2,2,2,m)$ one has

$$
(t-1)Q_m(t-1)=t^m A(t)-C(t),\qquad
A(t)=t^3+2t^2+3t+1,\qquad C(t)=3t^2+3t+1.
$$

The cubic $A$ has one real root $\alpha\in(-1/2,-2/5)$, since $A'(t)=3t^2+4t+3>0$ on $\mathbb R$. Its other roots are a simple conjugate pair $\zeta,\overline\zeta$, with $\alpha|\zeta|^2=-1$, so $|\zeta|>\sqrt2>21/20$. On a sufficiently small circle about $\zeta$, lying in $|t|>\sqrt2$ and excluding $1$, the term $t^mA(t)$ eventually dominates $C(t)$. Rouché's theorem supplies a quotient root there; shrinking the circle shows convergence to $\zeta$. Thus quotient roots persist outside the radius-$21/20$ disk as $m$ grows. This obstructs a maximum-length-only disk argument, not Bell real-rootedness: Theorem 2 already proves that family's Bell conclusion for all $m\geq2$.

A broader unresolved operator family, with the differential notation of Section 1, is

$$
\mathcal A_1=\mathcal S^2,\qquad
\mathcal A_{m+1}=L_1\mathcal A_m+D\mathcal S,\qquad
L_1=z\mathcal S+1.\tag{41}
$$

It gives the Bell quotient $\mathcal A_mT_k$ for $k$ length-two branches and one length-$m$ branch. The operator in Theorem 3 is $\mathcal A_3$. No preservation theorem for every $\mathcal A_m$ is asserted, and no finite diagnostic calculations are premises of the three proofs above. A residue estimate uniform in arbitrary branch count is likewise not supplied by the fixed four-path induction.

The accompanying verification programs reconstruct the exact arithmetic obligations: the rational induction base, the formal matching identity, the coloring/operator identities, and the two Bernstein certificates. Section 3.2 gives the exact coefficient acceptance condition for the latter; Section 4.3 gives the exact sign and interval criterion for the induction base. The infinite ranges are justified by the analytic radius argument, the invariant induction, and the formal all-degree matching construction, not by a finite sweep. Package execution and integrity instructions are provided separately.

AI systems assisted with derivations, exact computations, review passes, and manuscript preparation. AI review is not independent human peer review, and this work is ordinary computer-assisted mathematics, not proof-assistant formalization. The full $\tau$ clause of BRW Conjecture 6.5 for arbitrary pairs of $\tau$-real graphs remains outside the claims.

### 6.1 Unresolved literature overlap

A potentially relevant paper is Lili Mu, Qi Shen and Xinyao Xu, *On the Real-rootedness, invariance, and root bounds of $\tau$-polynomials* [4]. Its full text, exact normalization, hypotheses, graph families and theorem statements have not been inspected. The accessible formula-stripped metadata does not determine whether its results subsume, overlap with, or differ from the present statements. That comparison remains unknown. Inaccessibility is not evidence of non-overlap, and no historical priority or comprehensive literature certification is claimed.

## References

1. Francesco Brenti, Gordon F. Royle, and David G. Wagner. *Location of zeros of chromatic and related polynomials of graphs*. Canadian Journal of Mathematics **46** (1), 55--80 (1994). [doi:10.4153/CJM-1994-002-3](https://doi.org/10.4153/CJM-1994-002-3). Proposition 1.1 gives complete-cutset factorization; Propositions 4.2 and 4.4 give Bell-product identity and preservation; Proposition 5.1(d) gives reflection; Proposition 5.12 covers empty and one-vertex intersections.

2. Ole J. Heilmann and Elliott H. Lieb. *Theory of monomer-dimer systems*. Communications in Mathematical Physics **25**, 190--232 (1972). [doi:10.1007/BF01877590](https://doi.org/10.1007/BF01877590). The nonnegative weighted matching theorem applies to general graphs; (36) records the normalization used here.

3. *Real rooted edge quotients and clique attachment for theta graphs*. Public proof and exact certificates, fixed GitHub commit `cfa1f5fd798116b44ddc95da6f90710e48fac14a`, 2 November 2026. [Manuscript Section 4](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/cfa1f5fd798116b44ddc95da6f90710e48fac14a/extensions/2026-11-02-all-theta/MANUSCRIPT.md#4-exact-factor-repair-in-the-radius-disk); [immutable certificate package](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/cfa1f5fd798116b44ddc95da6f90710e48fac14a/extensions/2026-11-02-all-theta). In particular, the [mixed quartic certificate](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/cfa1f5fd798116b44ddc95da6f90710e48fac14a/extensions/2026-11-02-all-theta/effective_mixed_certificate.json) and [cubic certificate](https://github.com/Aurantium-47/brw-tau-clique-attachments/blob/cfa1f5fd798116b44ddc95da6f90710e48fac14a/extensions/2026-11-02-all-theta/effective_cubic_certificate.json) supply the exact coefficient lists used in Section 3.2.

4. Lili Mu, Qi Shen, and Xinyao Xu. *On the Real-rootedness, invariance, and root bounds of $\tau$-polynomials*. Discrete Mathematics, Algorithms and Applications, article 2550185. [doi:10.1142/S179383092550185X](https://doi.org/10.1142/S179383092550185X). Its precise mathematical overlap is unverified, as explained in Section 6.1.
