# Uniform eventual real rootedness for theta graph edge quotients

This note proves that one threshold works for all simple theta graphs whose three path lengths are at least two. Once the longest path exceeds that threshold, the Bell transform of the edge quotient is real-rooted. Consequently, attaching such a theta graph to any ordinary $\tau$-real graph along a complete subgraph preserves $\tau$-reality. The threshold is existential; no numerical value or assertion for all theta graphs is given.

## 1 The result and the polynomial normalization

All graphs are finite and simple. Write $\chi_G(q)$ for the chromatic polynomial of $G$, and set

$$
P_G(x)=(-1)^{|V(G)|}\chi_G(-x).
$$

Let $B:\mathbb R[x]\to\mathbb R[z]$ be the Bell transform, defined by

$$
B(x^j)=T_j(z)=\sum_{k=0}^j
\left\{\begin{matrix}j\\k\end{matrix}\right\}z^k,
$$

where the braces denote Stirling numbers of the second kind and $T_0(z)=1$. Thus $T_j$ is the $j$th Touchard polynomial. Equivalently, if

$$
x^{\underline j}=x(x-1)\cdots(x-j+1),
\qquad
x^{\overline j}=x(x+1)\cdots(x+j-1),
$$

with both empty products equal to $1$, then $B(x^{\underline j})=z^j$.

In the notation of Brenti, Royle, and Wagner [BRW], the transforms $S$ and $T$ send falling and rising factorials, respectively, to monomials. If $\epsilon$ denotes reflection, $(\epsilon f)(x)=f(-x)$, then

$$
B=S=\epsilon T\epsilon.
$$

Indeed, $\epsilon(x^{\underline j})=(-1)^j x^{\overline j}$, and reflecting the output cancels the factor $(-1)^j$. Since the ordinary BRW polynomial is $\tau_{\mathrm{BRW}}(G;z)=T\chi_G(z)$, this gives

$$
B(P_G)(z)=(-1)^{|V(G)|}\tau_{\mathrm{BRW}}(G;-z).
\tag{1}
$$

Thus $G$ is ordinary $\tau$-real if and only if $B(P_G)$ has only real zeros. These zeros are then nonpositive. To see the last assertion directly, deletion and contraction give $P_G=P_{G-e}+P_{G/e}$, with parallel edges after contraction suppressed. Induction from edgeless graphs shows that $P_G$ has nonnegative coefficients. The same is true of $B(P_G)$, so it cannot vanish at a positive real number.

We use the following established Bell-product fact. For real polynomials $f,g$, define

$$
(f*g)(z)=\sum_{k\geq0}\frac{z^k}{k!}f^{(k)}(z)g^{(k)}(z).
$$

Then

$$
B(FG)=B(F)*B(G).
\tag{2}
$$

Moreover, if $f$ and $g$ have only real nonpositive zeros, so does $f*g$. These are [BRW, Propositions 4.2 and 4.4](https://doi.org/10.4153/CJM-1994-002-3). In particular, products of polynomial factors whose Bell transforms have only real nonpositive zeros again have that property after applying $B$.

For integers $a,b,c\geq2$, let $\Theta(a,b,c)$ consist of three internally vertex-disjoint paths of lengths $a,b,c$ with common distinct endpoints. The lengths count edges.

**Theorem.** There exists an integer $M\geq2$ such that, for every $a,b,c\geq2$ with $\max\{a,b,c\}\geq M$, the polynomial

$$
B\!\left(\frac{P_{\Theta(a,b,c)}(x)}{x(x+1)}\right)
$$

has only real nonpositive zeros. For every such theta graph $H$ and every ordinary $\tau$-real graph $G$, if $G\cap H$ is a complete graph, including an empty or single-vertex intersection, then $G\cup H$ is ordinary $\tau$-real.

The proof below establishes a single $M$ independent of all three path lengths. By permuting the paths, it is enough to work with

$$
2\leq a\leq b\leq m,
\qquad H=\Theta(a,b,m),
\qquad Q(x)=\frac{P_H(x)}{x(x+1)}.
$$

## 2 The exact path coloring identity

For a path of length $\ell$, let $E_\ell(q)$ and $D_\ell(q)$ count proper internal colorings when its endpoint colors are fixed and equal or fixed and distinct, respectively. For positive integral $q\geq2$, the color-transition matrix gives the recurrences

$$
E_{\ell+1}=(q-1)D_\ell,
\qquad
D_{\ell+1}=E_\ell+(q-2)D_\ell,
\qquad E_0=1,\quad D_0=0.
$$

Consequently,

$$
E_\ell-D_\ell=(-1)^\ell,
\qquad
E_\ell+(q-1)D_\ell=(q-1)^\ell,
$$

and solving gives

$$
E_\ell(q)=\frac{(q-1)^\ell+(q-1)(-1)^\ell}{q},
\qquad
D_\ell(q)=\frac{(q-1)^\ell-(-1)^\ell}{q}.
\tag{3}
$$

The quotients are polynomials after cancellation, and the identities therefore hold as polynomial identities. Choosing the two common endpoint colors yields

$$
\chi_H(q)=qE_a(q)E_b(q)E_m(q)
+q(q-1)D_a(q)D_b(q)D_m(q).
\tag{4}
$$

We record the parity calculation explicitly. Put $L=a+b+m$ and $t=x+1$, so $q=-x=1-t$ and $q-1=-t$. Equation (3) becomes

$$
E_\ell(-x)=(-1)^{\ell+1}\frac{t^\ell-t}{t-1},
\qquad
D_\ell(-x)=(-1)^{\ell+1}\frac{t^\ell-1}{t-1}.
$$

The equal-endpoint term in (4) is therefore

$$
\frac{(-1)^L(t^a-t)(t^b-t)(t^m-t)}{(t-1)^2},
$$

and the distinct-endpoint term is

$$
\frac{(-1)^{L+1}t(t^a-1)(t^b-1)(t^m-1)}{(t-1)^2}.
$$

Since $|V(H)|=L-1$, multiplication by $(-1)^{L-1}$ gives

$$
P_H(x)=
\frac{t(t^a-1)(t^b-1)(t^m-1)
-(t^a-t)(t^b-t)(t^m-t)}{(t-1)^2}.
\tag{5}
$$

Expanding the numerator in (5) gives

$$
t(t-1)\bigl[(t^{a+b-1}-1)t^m-(t^a+t^b-t-1)\bigr].
$$

Define $S_\ell(t)=1+t+\cdots+t^{\ell-1}$ for $\ell\geq1$, and put

$$
A(t)=S_{a+b-1}(t),\qquad
C(t)=S_a(t)+S_b(t)-1,\qquad
N(t)=A(t)t^m-C(t).
$$

Dividing (5) by $x(x+1)=(t-1)t$ now gives the exact identity

$$
Q(t-1)=\frac{N(t)}{t-1}.
\tag{6}
$$

There is no singularity at $t=1$, because $A(1)=C(1)=a+b-1$. More usefully,

$$
A(t)-C(t)=(t-1)tS_{a-1}(t)S_{b-1}(t),
$$

so

$$
\boxed{
Q(t-1)=S_{a+b-1}(t)S_m(t)
+tS_{a-1}(t)S_{b-1}(t).
}
\tag{7}
$$

The right side has nonnegative coefficients in $t$ and is monic of degree $L-3$. After $t=x+1$, its leading monomial alone contributes positively to every coefficient of $Q(x)$. Hence **every coefficient of $Q$ is strictly positive**, and every real zero of $Q$ is strictly negative. Also (7) shows $Q(0)>0$, so the factor $t-1$ in $N$ has multiplicity exactly one.

## 3 The quadratic condition and its exceptional point

For an upper-half-plane zero $t$ of $Q(t-1)$, write

$$
t-1=-u+iv,\qquad u=1-\operatorname{Re}t,\quad v=\operatorname{Im}t>0.
$$

The corresponding monic real quadratic factor of $Q$ is

$$
h_t(x)=(x-(t-1))(x-(\overline t-1))
=x^2+2ux+u^2+v^2.
$$

Since $B(1)=1$, $B(x)=z$, and $B(x^2)=z^2+z$,

$$
B(h_t)(z)=z^2+(2u+1)z+u^2+v^2.
$$

Its discriminant is

$$
\begin{aligned}
J(t)&=1+4u-4v^2\\
&=5-4\operatorname{Re}t-4(\operatorname{Im}t)^2\\
&=4(1-|t|^2)+4\left(\operatorname{Re}t-\frac12\right)^2.
\end{aligned}
\tag{8}
$$

Call $h_t$ **good** if $J(t)\geq0$ and **bad** if $J(t)<0$. For a good quadratic, $u\geq v^2-1/4\geq-1/4$, so $2u+1>0$, while $u^2+v^2>0$. Its Bell transform has real roots with negative sum and positive product; both roots are strictly negative. This includes the boundary case of a double root.

Equation (8) shows that $J$ is positive inside the unit disk. On the unit circle, its only upper-half-plane zero is

$$
\zeta=e^{i\pi/3}=\frac12+i\frac{\sqrt3}{2}.
$$

## 4 Repairing two nearby quadratic factors

At $t=\zeta$,

$$
h_\zeta(x)=x^2+x+1.
$$

Using

$$
T_3(z)=z^3+3z^2+z,
\qquad
T_4(z)=z^4+6z^3+7z^2+z,
$$

we obtain

$$
\begin{aligned}
B(h_\zeta^2)(z)
&=B(x^4+2x^3+3x^2+2x+1)\\
&=z^4+8z^3+16z^2+8z+1\\
&=\bigl(z^2+(4+\sqrt2)z+1\bigr)
  \bigl(z^2+(4-\sqrt2)z+1\bigr).
\end{aligned}
\tag{9}
$$

Each of $4+\sqrt2$ and $4-\sqrt2$ is greater than $2$. Each quadratic in the last line therefore has two distinct strictly negative roots. The two quadratics have no common root: subtracting them would force a common root to be $0$, contrary to their constant terms. Thus (9) has four simple strictly negative roots.

Choose four pairwise disjoint closed intervals in $(-\infty,0)$, one around each root, with opposite nonzero signs of (9) at the two endpoints of each interval. The coefficients of $B(h_t h_s)$ depend continuously on the real and imaginary parts of $t$ and $s$. Hence there exists $\delta>0$ such that

$$
|t-\zeta|<\delta,\qquad |s-\zeta|<\delta
\tag{10}
$$

preserve all eight endpoint signs. The intermediate value theorem then supplies a root of $B(h_t h_s)$ in each of the four intervals. Since this polynomial is monic of degree four, these are all its roots and are simple and strictly negative. We reduce $\delta$ if necessary so that its disk about $\zeta$ lies in the upper half-plane. This repair applies whether either individual quadratic is good or bad.

## 5 A uniform outer radius for the numerator roots

The polynomial

$$
N(t)=S_{a+b-1}(t)t^m-(S_a(t)+S_b(t)-1)
$$

is monic of degree

$$
D=a+b+m-2\geq m+2,
$$

has constant coefficient $-1$, and has every nonleading coefficient of absolute value at most $2$. Indeed, the first summand has coefficients $0$ or $1$, the subtracted polynomial has coefficients $0$, $1$, or $2$, and overlapping positions cannot increase the absolute value beyond $2$. The leading term cannot cancel, since $D>b-1$. In particular, no root is zero.

If $t$ is a root and $r=|t|>1$, multiplying $N(t)=0$ by $t-1$ gives

$$
(t^{a+b-1}-1)t^m=t^a+t^b-t-1.
$$

The triangle and reverse-triangle inequalities imply

$$
(r^{a+b-1}-1)r^m
\leq r^a+r^b+r+1
\leq2r^b+2r.
$$

Dividing by $r^b$ yields

$$
(r^{a+b-1}-1)r^{m-b}
\leq2+2r^{1-b}\leq4.
$$

On the other hand, because $a,b\geq2$,

$$
\begin{aligned}
(r^{a+b-1}-1)r^{m-b}
&\geq(r^{b+1}-1)r^{m-b}\\
&=r^{m+1}-r^{m-b}\\
&\geq r^{m+1}-r^{m-2}
=r^{m-2}(r^3-1).
\end{aligned}
$$

Thus every such root satisfies

$$
r^{m-2}(r^3-1)\leq4.
\tag{11}
$$

Let $R_m>1$ be the unique solution of

$$
R_m^{m-2}(R_m^3-1)=4.
$$

Existence and uniqueness follow because the left side, as a function of $R_m>1$, is continuous, strictly increasing from $0$ to infinity, also when $m=2$. All roots of $N$ lie in $|t|\leq R_m$. Moreover, for every fixed $\varepsilon>0$,

$$
(1+\varepsilon)^{m-2}\bigl((1+\varepsilon)^3-1\bigr)>4
$$

for all sufficiently large $m$. It follows that

$$
R_m\longrightarrow1.
\tag{12}
$$

The bound and its convergence are independent of $a$ and $b$.

## 6 Uniform radial concentration

List the $D$ roots of $N$, with multiplicity, as

$$
t_j=r_j e^{i\theta_j},\qquad r_j>0,\qquad 1\leq j\leq D.
$$

Vieta's formula and the constant coefficient $-1$ give

$$
\prod_{j=1}^D r_j=1,
\qquad
\sum_{j=1}^D\log r_j=0.
$$

For $0<\varepsilon<1$, let $\alpha_\varepsilon$ be the fraction of roots with $r_j\leq1-\varepsilon$. Since every other radius is at most $R_m$,

$$
0\leq D\bigl[
\alpha_\varepsilon\log(1-\varepsilon)
+(1-\alpha_\varepsilon)\log R_m
\bigr].
$$

Consequently,

$$
\alpha_\varepsilon
\leq\frac{\log R_m}
{\log R_m-\log(1-\varepsilon)}
\longrightarrow0.
\tag{13}
$$

For each fixed $\varepsilon$, this convergence is uniform over $2\leq a\leq b\leq m$. Together with (12), it says that the fraction of roots outside any fixed annulus about the unit circle tends to zero uniformly. It does not assert that every individual root approaches that circle.

## 7 Uniform angular distribution

Write

$$
N(t)=t^D+d_1t^{D-1}+\cdots+d_D,
\qquad |d_j|\leq2,
$$

and let $p_k=\sum_{j=1}^D t_j^k$. Newton's identities give, for $1\leq k\leq D$,

$$
p_k+d_1p_{k-1}+\cdots+d_{k-1}p_1+kd_k=0.
$$

Induction yields

$$
|p_k|\leq3^k-1.
\tag{14}
$$

For $k=1$ this is $|p_1|\leq2$. If the assertion holds at smaller indices, the next bound is

$$
|p_k|
\leq2\sum_{i=1}^{k-1}(3^i-1)+2k
=3^k-1.
$$

For every fixed positive integer $k$, therefore, $p_k/D\to0$ uniformly as $m\to\infty$, because $D\geq m+2$.

We must pass from these power sums to the angles. Since

$$
|e^{ik\theta_j}-t_j^k|=|1-r_j^k|,
$$

the roots with $r_j\leq1-\varepsilon$ contribute at most $\alpha_\varepsilon$ to the normalized sum of these differences. On the remaining roots the difference is bounded by

$$
\max\bigl\{1-(1-\varepsilon)^k,\ R_m^k-1\bigr\}.
$$

Hence

$$
\frac1D\sum_{j=1}^D|e^{ik\theta_j}-t_j^k|
\leq\alpha_\varepsilon+
\max\bigl\{1-(1-\varepsilon)^k,\ R_m^k-1\bigr\}.
$$

First let $m\to\infty$ and then $\varepsilon\downarrow0$. Equations (12)--(14) imply

$$
\frac1D\sum_{j=1}^D e^{ik\theta_j}\longrightarrow0
\qquad(k\neq0),
\tag{15}
$$

uniformly over the ordered triples. Negative $k$ follow by complex conjugation; the zeroth moment is $1$.

It follows that, for every fixed continuous $2\pi$-periodic function $\varphi$,

$$
\frac1D\sum_{j=1}^D\varphi(\theta_j)
\longrightarrow
\frac1{2\pi}\int_0^{2\pi}\varphi(\theta)\,d\theta,
\tag{16}
$$

again uniformly in $a,b$. Indeed, approximate $\varphi$ uniformly by a fixed finite trigonometric polynomial. Each of its nonconstant terms has vanishing normalized average by (15), and the approximation error bounds both the empirical and circle averages independently of the roots and their number.

For completeness, the needed approximation can be obtained without any theorem about complex zeros. The nonnegative trigonometric polynomial

$$
K_n(u)=\frac1{n+1}\left|\sum_{j=0}^n e^{iju}\right|^2
$$

has circle average $1$. Away from any fixed neighborhood of $0$ modulo $2\pi$, the geometric-sum formula bounds $K_n(u)$ by a constant times $(n+1)^{-1}$. The convolution

$$
\varphi_n(\theta)=\frac1{2\pi}\int_0^{2\pi}
K_n(u)\varphi(\theta-u)\,du
$$

is a finite trigonometric polynomial. Uniform continuity of $\varphi$ controls the integral near $u=0$, and the stated bound controls its complement. Thus $\varphi_n\to\varphi$ uniformly, proving precisely the approximation used in (16).

## 8 A spare good quadratic for every sufficiently large triple

Fix the repair radius $\delta$ from Section 4. Choose a point $\rho$ on the upper unit semicircle, different from $\zeta$ but sufficiently close to it that $|\rho-\zeta|<\delta$. Equation (8) gives

$$
J(\rho)=4\left(\operatorname{Re}\rho-\frac12\right)^2>0.
$$

By continuity, there exist $0<\varepsilon<1$ and an open angular interval $I\subset(0,\pi)$ such that the closure of the annular sector

$$
V=\{r e^{i\theta}:1-\varepsilon<r<1+\varepsilon,\ \theta\in I\}
\tag{17}
$$

lies inside $|t-\zeta|<\delta$, inside $J(t)>0$, and away from $t=1$ and the real axis. These choices are fixed once and do not depend on $a,b,m$.

Choose a continuous $2\pi$-periodic function $\varphi$ with $0\leq\varphi\leq1$, not identically zero, whose support is contained in $I$. Its circle average

$$
c_\varphi=\frac1{2\pi}\int_0^{2\pi}\varphi(\theta)\,d\theta
$$

is positive. By (16), for every sufficiently large $m$ and every $2\leq a\leq b\leq m$,

$$
\frac1D\sum_{j=1}^D\varphi(\theta_j)\geq\frac{c_\varphi}{2}.
$$

By (12) and (13), enlarging this uniform threshold if needed, the fraction of roots outside $1-\varepsilon<r_j<1+\varepsilon$ is less than $c_\varphi/4$. Since $\varphi\leq1$, removing these roots leaves

$$
\frac1D\sum_{\substack{j:\ 1-\varepsilon<r_j<1+\varepsilon}}
\varphi(\theta_j)>
\frac{c_\varphi}{4}>0.
$$

Thus at least one actual root $s$ of $N$ belongs to $V$, for **every** sufficiently large ordered triple. This root is nonreal, lies in the upper half-plane, and is not $1$, so it survives division by $t-1$ in (6). Its conjugate supplies a good quadratic factor $h_s$ of $Q$, with $J(s)>0$ and $|s-\zeta|<\delta$. We reserve one occurrence of this factor for a possible parity adjustment.

## 9 Uniform localization of all bad quadratics

For any upper-half-plane root $t$ belonging to a bad factor, (8) gives

$$
1<|t|\leq R_m,
\qquad
\left|\operatorname{Re}t-\frac12\right|
<\sqrt{R_m^2-1}.
\tag{18}
$$

As $m\to\infty$, the real parts therefore approach $1/2$ uniformly, and the moduli approach $1$ uniformly. Since the imaginary part is positive and

$$
(\operatorname{Im}t)^2=|t|^2-(\operatorname{Re}t)^2,
$$

the imaginary parts approach $\sqrt3/2$ uniformly. Thus every bad upper root approaches $\zeta$ uniformly over all $a,b$ and over all roots, counted with multiplicity. In particular, beyond a single threshold every bad quadratic has its upper root in the repair disk $|t-\zeta|<\delta$.

## 10 Factor assembly and clique attachment

Take one integer $M\geq2$ large enough for both the spare-factor conclusion of Section 8 and the localization conclusion of Section 9. Their uniformity means this single $M$ works for every $2\leq a\leq b\leq m$ with $m\geq M$.

Factor the monic polynomial $Q$ over $\mathbb R$, keeping all multiplicities. By (7), each real linear factor is $x+\lambda$ with $\lambda>0$; its Bell transform is $z+\lambda$. Every good quadratic has a Bell transform with strictly negative real roots, by Section 3.

If the number of bad quadratic factors is even, pair them arbitrarily. If it is odd, remove one occurrence of the spare good quadratic from the good collection and add it to the bad collection, then pair the resulting even collection. Every pair has both upper roots in the repair disk, so Section 4 proves that its product has a Bell transform with four simple strictly negative roots. This construction also covers repeated roots and repeated factors: only one occurrence of the spare is removed, and every factor occurrence is used exactly once.

We have expressed $Q$ as a product of linear, good quadratic, and repaired quartic blocks, each with a Bell transform having only real nonpositive zeros. Iterating (2) and Bell-product preservation proves the asserted real-rootedness of $B(Q)$.

Now suppose $G\cap H=K_2$. The chromatic complete-cutset identity, [BRW, Proposition 1.1](https://doi.org/10.4153/CJM-1994-002-3), gives

$$
\chi_{G\cup H}(q)=\frac{\chi_G(q)\chi_H(q)}{q(q-1)}.
$$

Since $|V(G\cup H)|=|V(G)|+|V(H)|-2$, substituting $q=-x$ yields, with no residual sign,

$$
P_{G\cup H}(x)=\frac{P_G(x)P_H(x)}{x(x+1)}=P_G(x)Q(x).
$$

For a $\tau$-real graph $G$, equation (1) and coefficient nonnegativity show that $B(P_G)$ has only real nonpositive zeros. One more use of (2) therefore proves that $G\cup H$ is $\tau$-real.

The theta graph itself is also $\tau$-real. Indeed,

$$
P_H=x(x+1)Q,
\qquad
B(x(x+1))=z(z+2),
$$

so the same product theorem applies. Thus [BRW, Proposition 5.12](https://doi.org/10.4153/CJM-1994-002-3) supplies the conclusion when $G\cap H$ is empty or a single vertex. Finally, $H$ is triangle-free: each of its cycles uses two of the three paths and has length at least four. Its complete subgraphs therefore have at most two vertices. The three cases just proved exhaust every possible complete overlap and finish the theorem.

## 11 Scope

The quantifiers are

$$
\exists M\geq2\ \ \forall a,b,c\geq2:
\quad \max\{a,b,c\}\geq M
\ \Longrightarrow\
B\!\left(P_{\Theta(a,b,c)}/(x(x+1))\right)
\text{ has only real nonpositive zeros}.
$$

Thus only finitely many triples lie outside the assertion. The proof supplies no numerical value of $M$ and does not settle those remaining triples. It is not an all-theta theorem or a proof of general clique closure for arbitrary $\tau$-real graphs. No historical novelty or priority claim is made.

The theta-specific argument above uses exact identities, elementary real-root continuity, Vieta's formula, Newton's identities, and trigonometric approximation. Its graph-preservation inputs are precisely the cited BRW results; no finite root sweep or numerical extrapolation is used.

## Reference

**[BRW]** F. Brenti, G. F. Royle, and D. G. Wagner, *Location of Zeros of Chromatic and Related Polynomials of Graphs*, Canadian Journal of Mathematics **46** (1) (1994), 55–80. [DOI 10.4153/CJM-1994-002-3](https://doi.org/10.4153/CJM-1994-002-3). Proposition 1.1 gives chromatic complete-cutset factorization; Propositions 4.2 and 4.4 give the Bell or $S$ product and its real-root preservation; Proposition 5.12 covers intersections of at most one vertex.
