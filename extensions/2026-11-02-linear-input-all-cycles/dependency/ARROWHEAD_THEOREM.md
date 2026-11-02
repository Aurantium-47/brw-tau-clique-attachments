# Uniform preservation by cycle substitution operators

The proof was developed and separately reviewed using AI. This is not human peer review or proof-assistant certification.

Related-literature boundary: the exact normalization and overlap with Mu–Shen–Xu, DOI [10.1142/S179383092550185X](https://doi.org/10.1142/S179383092550185X), remain unverified because its full text was not obtained. That paper is not used as a proof dependency here, and no claim of non-overlap is made.

## Scope and main result

Let $D=d/dz$, $S=1+D$, and $L=zD+z+1$. Define linear operators on real polynomials by

$$
 A_1=S^2,\qquad A_{m+1}=LA_m+DS\qquad(m\ge1).
 \tag{1}
$$

This note proves that **every $A_m$ preserves polynomials whose zeros are all real and nonpositive**, in every input degree. The proof uses an initial residue estimate obtained from monotonicity of roots, followed by an invariant for symmetric arrowhead matrices. It includes repeated roots, roots at zero, constants, and the zero polynomial. This is an ordinary mathematical proof; the accompanying exact symbolic checks are optional checks of displayed identities, not premises of the theorem.

The graph consequence is uniform in the cycle length: substitution of any ordinary $\tau$-real graph for one vertex of $C_{m+2}$, for every $m\ge1$, remains ordinary $\tau$-real and has a Bell-real edge quotient. It can consequently be attached along an edge to any ordinary $\tau$-real graph. The exact graph construction and normalization are given in Section 5. The graph theorem concerns one-vertex substitution into a cycle, not arbitrary simultaneous graph substitution or general clique closure.

The operator proof is independent of weighted-matching realizations. Uniform feasibility of a particular earlier star-core realization remains a separate open construction problem; it is not needed for the theorem proved here. A standard universal-clique lift gives the limited larger-clique consequence stated in Section 5.5. No unrestricted larger-clique attachment or historical-priority assertion is made.

## 1 The preservation theorem

Write

$$
 \mathcal C=\{0\}\cup
 \left\{c\prod_{j=1}^{n}(z+\alpha_j):
 n\ge0,\ c>0,\ \alpha_j\ge0\right\}.
 \tag{2}
$$

The empty product includes positive constants. Since the operators are linear, preservation of $\mathcal C$ also proves the root-location statement for inputs with negative leading coefficient.

**Theorem 1.** For every integer $m\ge1$,

$$
 A_m\mathcal C\subseteq\mathcal C.
 \tag{3}
$$

More precisely, if $f$ is monic of degree $n\ge1$ with distinct strictly negative roots, then $A_m f$ is monic of degree $n+m-1$ with distinct strictly negative roots.

The consecutive outputs also interlace. Put $N=n+m-1$, and list the roots of $A_mf$ and $A_{m+1}f$ as $r_1<\cdots<r_N$ and $s_1<\cdots<s_{N+1}$. For such a strict input,

$$
 s_1<r_1<s_2<\cdots<r_N<s_{N+1}<0.
$$

For every nonzero input $f\in\mathcal C$, put $n=\deg f\ge0$ and $N=n+m-1$. List the roots of $A_mf$ and $A_{m+1}f$ in nondecreasing order with multiplicity as $r_i$ and $s_i$, respectively. They satisfy the weak inequalities

$$
 s_1\le r_1\le s_2\le\cdots\le r_N\le s_{N+1}\le0.
$$

For a constant input and $m=1$, the first root list is empty and the interlacing assertion is vacuous. No interlacing assertion is made for the zero polynomial.


The proof has two parts. First, for

$$
 F=S^2f,\qquad h=DSf,
 \tag{4}
$$

the normalized residues of $h/F$ satisfy a uniform bound. Second, an invariant propagates those bounds under $F\mapsto LF+h$, with $h$ held fixed. The latter iteration is exactly (1) applied to $f$.

## 2 Initial residue bounds from root monotonicity

### 2.1 The root map of one plus differentiation

Let $g$ be monic of degree $n\ge1$, with distinct real roots
$a_1<\cdots<a_n$. Away from these roots,

$$
 \frac{Sg(z)}{g(z)}
  =H(z;a):=1+\sum_{j=1}^{n}\frac1{z-a_j},
 \qquad
 H_z=-\sum_{j=1}^{n}\frac1{(z-a_j)^2}<0.
 \tag{5}
$$

There is one zero of $H$ in $(-\infty,a_1)$ and one in each $(a_j,a_{j+1})$. The endpoint limits and strict decrease give existence and uniqueness on these intervals. None of the $a_j$ is a root of $Sg$, because $Sg(a_j)=g'(a_j)\ne0$. Degree counting accounts for all $n$ roots of $Sg$, which are simple. In particular, strictly negative input roots give strictly negative output roots.

Let $s_i(a)$ be the ordered roots of $Sg$. Implicit differentiation of (5) gives

$$
 \frac{\partial s_i}{\partial a_j}
 =\frac{(s_i-a_j)^{-2}}
        {\sum_{k=1}^{n}(s_i-a_k)^{-2}}>0.
 \tag{6}
$$

These functions are smooth throughout the open ordered-root chamber. Their Jacobian is entrywise positive, and every row sums to one. Applying the map twice therefore gives a smooth ordered-root map for $S^2$, again with an entrywise positive Jacobian.

### 2.2 A uniform bound on each initial residue

Now let $f$ be monic of degree $n\ge1$ with distinct strictly negative roots $a_j$. Put

$$
 p=Sf,\qquad F=Sp=S^2f,\qquad h=p'=DSf.
 \tag{7}
$$

Both $p$ and $F$ have distinct strictly negative roots. If $r_i$ is a root of $F$, then $p(r_i)\ne0$, and (5) applied to $p$ gives

$$
 \frac{F'(r_i)}{p(r_i)}
 =-\sum_{j=1}^{n}\frac1{(r_i-\operatorname{root}_j(p))^2}<0.
 \tag{8}
$$

Since $F(r_i)=0$, one also has $h(r_i)=p'(r_i)=-p(r_i)$. Define

$$
 \kappa_i=\frac{h(r_i)}{(-r_i)F'(r_i)}
          =\frac{p(r_i)}{r_iF'(r_i)}>0.
 \tag{9}
$$

To obtain an upper bound, for $t>0$ set

$$
 F_t=(D+t)^2f,
 \qquad q_t(y)=t^n f(y/t).
 \tag{10}
$$

The monic polynomial $q_t$ has ordered roots $ta_j$, and direct differentiation gives

$$
 (1+D_y)^2q_t(y)=t^{n-2}F_t(y/t).
 \tag{11}
$$

Thus $F_t$ has distinct strictly negative roots $r_i(t)$, and
$y_i(t):=t r_i(t)$ is the ordered-root map of $S^2$ evaluated at $(ta_1,\ldots,ta_n)$. Its derivative is strictly negative: the Jacobian of that map is entrywise positive by (6), while every coordinate of $(a_1,\ldots,a_n)$ is strictly negative. At $t=1$, this says

$$
 r_i+r_i'(1)<0.
 \tag{12}
$$

On the other hand, differentiating $F_t(r_i(t))=0$ at $t=1$ yields

$$
 r_i'(1)=-\frac{2p(r_i)}{F'(r_i)},
 \qquad
 \kappa_i=\frac{r_i'(1)}{-2r_i}.
 \tag{13}
$$

Together, (9), (12), and (13) prove the strict bound

$$
 \boxed{0<\kappa_i<\frac12\quad(1\le i\le n).}
 \tag{14}
$$

The argument applies without change when $n=1$. For example, if $f=z+\alpha$, $\alpha>0$, then $F=z+\alpha+2$, $h=1$, and $\kappa_1=1/(\alpha+2)<1/2$.

### 2.3 The initial total and potential

Because $\deg h=n-1<\deg F$, partial fractions evaluated at zero give

$$
 w:=\frac{h(0)}{F(0)}=\sum_{i=1}^{n}\kappa_i.
 \tag{15}
$$

All coefficients of $f$ are positive. In particular,

$$
 h(0)=f'(0)+f''(0)>0,
 \qquad F(0)-h(0)=f(0)+f'(0)>0,
$$

so $0<w<1$. Define the potential

$$
 V:=\sum_{i=1}^{n}\frac{\kappa_i^2}{1-\kappa_i}.
 \tag{16}
$$

For $0<\kappa_i<1/2$, each summand is strictly less than $\kappa_i$. Therefore

$$
 0<V<w<2-w.
 \tag{17}
$$

These inequalities provide the initial point of the invariant below.

## 3 The enlarged arrowhead invariant

**Lemma 2.** Let $F$ be monic of degree $N\ge1$ with distinct strictly negative roots $r_1,\ldots,r_N$. Let $h\in\mathbb R[z]$ satisfy $\deg h<N$ and $h(0)>0$. Define

$$
 \begin{aligned}
 R_i&=-r_i>0,&
 a_i&=\frac{h(r_i)}{F'(r_i)},&
 \kappa_i&=\frac{a_i}{R_i},\\
 w&=\sum_{i=1}^{N}\kappa_i=\frac{h(0)}{F(0)},&
 V&=\sum_{i=1}^{N}\frac{\kappa_i^2}{1-\kappa_i}.
 \end{aligned}
 \tag{18}
$$

Suppose

$$
 |\kappa_i|<1\quad\text{for all }i,
 \qquad 0<w\le1,
 \qquad V\le2-w.
 \tag{19}
$$

Then

$$
 G=LF+h=zF'+(z+1)F+h
 \tag{20}
$$

is monic of degree $N+1$ with distinct strictly negative roots. The quantities $\kappa'_j,w',V'$ defined by (18) using $G$ and the same $h$ satisfy

$$
 |\kappa'_j|<1,
 \qquad w'=\frac{w}{1+w}\in(0,1/2],
 \qquad V'\le2-w'.
 \tag{21}
$$

The individual residues in this lemma may have either sign. Positivity of every residue is needed only for the initial estimate in Section 2, not for the induction.

### 3.1 The arrowhead matrix and its roots

Partial fractions give

$$
 \frac{h(z)}{F(z)}=\sum_{i=1}^{N}\frac{a_i}{z-r_i}.
 \tag{22}
$$

Since $z/(z-r_i)=1+r_i/(z-r_i)$, equation (20) becomes

$$
 \frac{G(z)}{F(z)}
 =z+N+1-\sum_{i=1}^{N}\frac{b_i^2}{z-r_i},
 \qquad b_i:=\sqrt{R_i-a_i}
             =\sqrt{R_i(1-\kappa_i)}>0.
 \tag{23}
$$

Let $b=(b_1,\ldots,b_N)^T$ and $\Delta=\operatorname{diag}(R_i)$. The symmetric arrowhead matrix

$$
 M=\begin{pmatrix}
    \operatorname{diag}(r_i)&b\\
    b^T&-(N+1)
   \end{pmatrix},
 \qquad
 A=-M=\begin{pmatrix}
      \Delta&-b\\
      -b^T&N+1
     \end{pmatrix}
 \tag{24}
$$

has characteristic polynomial $G$, by the Schur complement formula and (23). The Schur complement of $\Delta$ in $A$ is

$$
 N+1-b^T\Delta^{-1}b
 =N+1-\sum_{i=1}^{N}(1-\kappa_i)=1+w>0.
 \tag{25}
$$

Consequently $A$ is positive definite, so every eigenvalue of $M$, hence every root of $G$, is strictly negative.

These roots are simple. Indeed, the quotient in (23) has derivative

$$
 1+\sum_{i=1}^{N}\frac{b_i^2}{(z-r_i)^2}>0
 \tag{26}
$$

on each interval outside its poles. Its endpoint limits yield one zero in each of the $N+1$ complementary intervals. No pole is a root of $G$, because
$G(r_i)=-b_i^2F'(r_i)\ne0$. Thus all $N+1$ roots are distinct.

### 3.2 A rank two representation of the new residues

Put

$$
 c_i=\frac{a_i}{2b_i},\qquad
 E=\begin{pmatrix}0&c\\c^T&0\end{pmatrix},\qquad
 K=A^{-1/2}EA^{-1/2}.
 \tag{27}
$$

Let $s_j$ be a root of $G$, and let $v_j$ be a normalized real eigenvector of $M$ with eigenvalue $s_j$. Its last coordinate is nonzero, and the eigenvector equations and normalization give

$$
 (v_j)_i=\frac{b_i(v_j)_{N+1}}{s_j-r_i},
 \qquad
 (v_j)_{N+1}^2
  =\left(1+\sum_{i=1}^{N}\frac{b_i^2}{(s_j-r_i)^2}\right)^{-1}.
 \tag{28}
$$

Using $2b_ic_i=a_i$, (22), and (26), we obtain

$$
 \begin{aligned}
 v_j^TEv_j
 &=\frac{\sum_i a_i/(s_j-r_i)}
         {1+\sum_i b_i^2/(s_j-r_i)^2}\\
 &=\frac{h(s_j)/F(s_j)}{G'(s_j)/F(s_j)}
  =\frac{h(s_j)}{G'(s_j)}.
 \end{aligned}
 \tag{29}
$$

The same eigenvectors diagonalize $A$, with eigenvalues $-s_j>0$. It follows that the diagonal entries of $K$, when written in this orthonormal eigenbasis of $A$, are exactly the new normalized residues:

$$
 v_j^TKv_j
 =\frac{h(s_j)}{(-s_j)G'(s_j)}=\kappa'_j.
 \tag{30}
$$

### 3.3 The two nonzero eigenvalues

At least one $a_i$ is nonzero, because $\sum_i a_i/R_i=w>0$. Thus $c\ne0$, and $E$ and $K$ have rank two. The identities

$$
 b^T\Delta^{-1}b=N-w,
 \qquad c^T\Delta^{-1}b=\frac w2,
 \qquad c^T\Delta^{-1}c=\frac V4
 \tag{31}
$$

follow directly from (18), (23), and (27).

For $\lambda\ne0$, the Schur complement of $-\lambda\Delta$ in

$$
 E-\lambda A
 =\begin{pmatrix}
   -\lambda\Delta&c+\lambda b\\
   c^T+\lambda b^T&-\lambda(N+1)
  \end{pmatrix}
$$

is

$$
 \begin{aligned}
 -\lambda(N+1)
  +\frac1\lambda(c+\lambda b)^T\Delta^{-1}(c+\lambda b)
 &=-(1+w)\lambda+w+\frac{V}{4\lambda}.
 \end{aligned}
 \tag{32}
$$

Hence, as a polynomial identity,

$$
 \det(E-\lambda A)
 =(-1)^{N+1}\det(\Delta)\lambda^{N-1}
   \left((1+w)\lambda^2-w\lambda-\frac V4\right).
 \tag{33}
$$

Congruence gives
$E-\lambda A=A^{1/2}(K-\lambda I)A^{1/2}$.
The two nonzero eigenvalues $\lambda_-$ and $\lambda_+$ of $K$ are therefore the roots of

$$
 q(\lambda):=(1+w)\lambda^2-w\lambda-\frac V4=0.
 \tag{34}
$$

Here $V>0$. By (19), $V\le2-w<2$, and

$$
 q(0)=-V/4<0,
 \quad q(1)=1-V/4>0,
 \quad q(-1)=1+2w-V/4>0.
 \tag{35}
$$

Thus

$$
 -1<\lambda_-<0<\lambda_+<1.
 \tag{36}
$$

The remaining $N-1$ eigenvalues are zero. Every diagonal entry of a real symmetric matrix in an orthonormal basis is a convex combination of its eigenvalues. Equations (30) and (36) therefore give $|\kappa'_j|<1$.

There is no exception when $N=1$: then $E$ is a $2\times2$ matrix of rank two, the factor $\lambda^{N-1}$ in (33) is one, and the two eigenvalues in (34) are the complete spectrum.

### 3.4 Jensen inequality and closure of the invariant

The scalar function

$$
 \phi(t)=\frac{t^2}{1-t}=\frac1{1-t}-1-t
 \tag{37}
$$

is convex on $( -\infty,1)$, because $\phi''(t)=2/(1-t)^3>0$. In the basis used in (30), write an orthogonal diagonalization
$K=U\operatorname{diag}(\lambda_+,\lambda_-,0,\ldots,0)U^T$.
For each row $j$, the squares $U_{j\ell}^2$ are nonnegative and sum to one. Scalar Jensen inequality gives

$$
 \phi(\kappa'_j)
 \le\sum_\ell U_{j\ell}^2\phi(\lambda_\ell).
$$

Summing over $j$, and using that every column also has squared entries summing to one, proves

$$
 V'\le\phi(\lambda_+)+\phi(\lambda_-).
 \tag{38}
$$

The zero eigenvalues contribute $\phi(0)=0$. From (34),

$$
 \lambda_++\lambda_- =\frac{w}{1+w},
 \qquad
 \lambda_+\lambda_-=-\frac{V}{4(1+w)}.
 \tag{39}
$$

Substitution in (37) yields

$$
 \phi(\lambda_+)+\phi(\lambda_-)
 =\Phi(V,w):=\frac{2+w}{1-V/4}-2-\frac{w}{1+w}.
 \tag{40}
$$

For fixed $w>0$, this is increasing in $V<4$, with derivative

$$
 \frac{\partial\Phi}{\partial V}
 =\frac{2+w}{4(1-V/4)^2}>0.
 \tag{41}
$$

Also $G(0)=F(0)+h(0)$, so partial fractions at zero give

$$
 w'=\frac{h(0)}{G(0)}=\frac{w}{1+w}\in(0,1/2].
 \tag{42}
$$

At the boundary of (19), the potential has the exact identity

$$
 \Phi(2-w,w)
 =\frac{2+w}{1-(2-w)/4}-2-\frac{w}{1+w}
 =2-\frac{w}{1+w}=2-w'.
 \tag{43}
$$

Combining (19), (38), (41), and (43) proves
$V'\le2-w'$. This establishes all of (21) and completes the proof of Lemma 2. $\square$

## 4 Iteration and boundary inputs

For a monic input $f$ of degree $n\ge1$ with distinct strictly negative roots, Section 2 proves the hypotheses of Lemma 2 for

$$
 F_1=S^2f=A_1f,\qquad h=DSf.
$$

Keep $h$ fixed and set $F_{m+1}=LF_m+h$. The recurrence (1) gives $F_m=A_mf$. At every step the degree of $F_m$ increases by one, whereas $\deg h=n-1$ stays fixed. Lemma 2 therefore applies indefinitely. Every $F_m$ is monic of degree $n+m-1$ with distinct strictly negative roots. Equation (23), its endpoint limits, and (26) put one root of $F_{m+1}$ in each complementary interval of the roots of $F_m$. Together with negativity, this proves the strict consecutive-root inequalities in Theorem 1. Thus all strict-input assertions hold.

For the constant input $f=1$, one has $h=0$ and

$$
 A_m1=L^{m-1}1.
 \tag{44}
$$

Here $A_11=1$ and $A_21=z+1$. If a monic $F$ has distinct strictly negative roots, the arrowhead construction (23)–(26) with $a_i=0$ gives a positive definite $-M$, with Schur complement one, and proves that $LF$ has distinct strictly negative roots. Induction establishes the constant-input case. The rank-two argument is not invoked when $h=0$.

Finally, every monic polynomial with repeated or zero nonpositive roots is a coefficientwise limit of monic polynomials of the same degree with distinct strictly negative roots. For each fixed $m$, $A_m$ is a finite differential operator with polynomial coefficients, and hence is continuous in coefficients on each finite-degree polynomial space. Its image of a monic degree-$n$ polynomial is monic of degree $n+m-1$, including $n=0$; thus there is no loss of degree in the limit. The set of monic fixed-degree polynomials whose roots are all real and nonpositive is closed. For example, a coefficient-convergent sequence has uniformly bounded roots, and a convergent subsequence of its ordered real roots factors the limiting polynomial with nonpositive real roots.

For each consecutive pair, the same fixed-degree approximation applies to both outputs simultaneously. Passing to their ordered roots preserves the alternating inequalities weakly, proving the stated weak interlacing for every nonzero boundary input. For constants, the $h=0$ arrowhead argument gives strict interlacing whenever both root lists are nonempty, while the first pair is vacuous. Taking limits proves (3) for every monic input in $\mathcal C$. Positive scalar multiplication, and $A_m0=0$, finish the proof. Arbitrary nonzero real scalar multiplication gives the equivalent statement without a leading-coefficient restriction. $\square$

### 4.1 A separate higher shift extension

The same invariant gives an operator extension with no additional graph assertion.

**Corollary 3.** Fix an integer $k\ge2$ and define

$$
 T_{k,1}=S^k,\qquad
 T_{k,m+1}=LT_{k,m}+DS^{k-1}\qquad(m\ge1).
$$

Then every $T_{k,m}$ preserves $\mathcal C$. The case $k=2$ is Theorem 1.

**Proof.** For a monic $f$ of degree $n\ge1$ with distinct strictly negative roots, set

$$
 p=S^{k-1}f,\qquad F_1=S^kf=p+p',\qquad h=p',
 \qquad F_{m+1}=LF_m+h.
$$

Then $F_m=T_{k,m}f$. All intermediate $S$-iterates have distinct strictly negative roots. At an $F_1$-root $r_i$, the argument of (8)–(9) gives
$\kappa_i=h(r_i)/[(-r_i)F_1'(r_i)]>0$.
For $t>0$, put $F_t=(D+t)^kf$. The scaling identity is now

$$
 (1+D_y)^k[t^nf(y/t)]=t^{n-k}F_t(y/t).
$$

This is valid also when $n<k$, since the scalar $t^{n-k}$ is nonzero. The $k$-fold composition of the root map in (6) has an entrywise positive Jacobian. For the ordered roots $r_i(t)$ of $F_t$, it follows that
$\left.\frac{d}{dt}(tr_i(t))\right|_{t=1}<0$.
Differentiation of $F_t(r_i(t))=0$ gives

$$
 r_i'(1)=-\frac{k p(r_i)}{F_1'(r_i)},
 \qquad
 0<\kappa_i=\frac{r_i'(1)}{-k r_i}<\frac1k\le\frac12.
$$

Also $w=h(0)/F_1(0)=p'(0)/(p(0)+p'(0))\in(0,1)$, and

$$
 V=\sum_i\frac{\kappa_i^2}{1-\kappa_i}
   <\frac{w}{k-1}\le w<2-w.
$$

Lemma 2 applies to $F_1$ with this fixed $h$, and then to every subsequent $F_m$. Constants, repeated roots, zero roots, scalar multiples, and the zero input are handled exactly as in Section 4. This proves the corollary. $\square$

## 5 Cycle substitution and edge attachment

### 5.1 Bell transform and normalization

For a finite simple graph $G$, let $\chi_G(q)$ be its chromatic polynomial, and put

$$
 P_G(x)=(-1)^{|V(G)|}\chi_G(-x).
 \tag{45}
$$

Define the Touchard polynomials by

$$
 T_0(z)=1,\qquad T_{k+1}(z)=z\bigl(T_k(z)+T'_k(z)\bigr),
$$

and define the Bell transform by linear extension of

$$
 \mathcal B(x^k)=T_k(z).
 \tag{46}
$$

We use the unsigned, reflected normalization: $G$ is **ordinary $\tau$-real** when $\mathcal B(P_G)$ has only real nonpositive roots. This is the reflected convention for the ordinary $\tau$-polynomial of Brenti–Royle–Wagner. The unsigned chromatic coefficients and the Touchard coefficients are nonnegative, so $\mathcal B(P_G)\in\mathcal C$ whenever $G$ is ordinary $\tau$-real. No real-rootedness hypothesis on a quotient of $P_G$ is imposed on the input graph.

The graph consequences use the following established Bell-product theorem. If

$$
 f*g:=\sum_{k\ge0}\frac{z^k}{k!}f^{(k)}(z)g^{(k)}(z),
 \tag{47}
$$

then

$$
 \mathcal B(pq)=(\mathcal Bp)*(\mathcal Bq),
 \qquad f,g\in\mathcal C\ \Longrightarrow\ f*g\in\mathcal C.
 \tag{48}
$$

These are Propositions 4.2 and 4.4 of Brenti–Royle–Wagner [1]. They are needed only for the graph-product conclusions below, not for Theorem 1.

### 5.2 The graph and its endpoint coloring identity

For $m\ge1$, construct $H_m(F)$ as follows. Take a path of length $m$, with distinct endpoints $u,v$, disjoint from a finite simple graph $F$. Join every vertex of $F$ to both $u$ and $v$, and add no other edges. When $F$ is nonempty, this is substitution of $F$ for one vertex of $C_{m+2}$. The explicit construction also covers the empty graph $F$.

For prescribed endpoint colors, the numbers of internal colorings of a length-$m$ path are

$$
 \begin{aligned}
 d_m(q)&=\frac{(q-1)^m-(-1)^m}{q}
 &&\text{if the colors are distinct},\\
 e_m(q)&=\frac{(q-1)^m+(q-1)(-1)^m}{q}
 &&\text{if they are equal}.
 \end{aligned}
 \tag{49}
$$

For positive integer $q$, these formulas follow by taking powers of the $q\times q$ matrix with zero diagonal and all off-diagonal entries one: its eigenvalues are $q-1$ on the constant vectors and $-1$ on their orthogonal complement. Choosing the endpoint colors first gives

$$
 \chi_{H_m(F)}(q)
 =q(q-1)d_m(q)\chi_F(q-2)+qe_m(q)\chi_F(q-1).
 \tag{50}
$$

The equality for sufficiently large integers $q$ establishes the polynomial identity.

Let
$\sigma_j(t)=1+t+\cdots+t^{j-1}$ for $j\ge1$, and $\sigma_0(t)=0$. Since $|V(H_m(F))|=|V(F)|+m+1$, unsigned reflection of (50) gives the exact polynomial identity

$$
 \boxed{\begin{aligned}
 Q_m(x)&:=\frac{P_{H_m(F)}(x)}{x(x+1)}\\
 &=\sigma_m(x+1)P_F(x+2)
  -\sigma_{m-1}(x+1)P_F(x+1).
 \end{aligned}}
 \tag{51}
$$

For clarity about the sign, put $t=x+1$. Before division by $x(x+1)=(t-1)t$, the two scalar factors obtained from (50) are $t(t^m-1)$ and $-(t^m-t)$, respectively. Dividing yields precisely the two terms in (51).

### 5.3 The Bell image is the preservation operator

The Bell transform satisfies

$$
 \mathcal B(xp)=z(1+D)\mathcal Bp,
 \qquad
 \mathcal B(p(x+1))=(1+D)\mathcal Bp.
 \tag{52}
$$

The first identity follows from the Touchard recurrence on monomials. For the second, the formal exponential generating function

$$
 \sum_{k\ge0}T_k(z)\frac{u^k}{k!}
 =\exp\bigl(z(e^u-1)\bigr)
$$

shows that applying $1+D$ multiplies the series by $e^u$, which is exactly the binomial shift on the monomial input. Linearity gives (52) for every polynomial.

The geometric sums in (51) satisfy

$$
 Q_1=P_F(x+2),\qquad
 Q_{m+1}=(x+1)Q_m+P_F(x+2)-P_F(x+1).
 \tag{53}
$$

Under $\mathcal B$, multiplication by $x+1$ becomes $z(1+D)+1=L$, and the last difference becomes $(S^2-S)\mathcal B(P_F)=DS\mathcal B(P_F)$. Equations (1), (52), and (53) therefore imply

$$
 \boxed{\mathcal B(Q_m)=A_m\mathcal B(P_F).}
 \tag{54}
$$

**Corollary 4.** For every $m\ge1$ and every ordinary $\tau$-real graph $F$,

$$
 \mathcal B\!\left(\frac{P_{H_m(F)}}{x(x+1)}\right)
 =\mathcal B(Q_m)\in\mathcal C.
 \tag{55}
$$

This is an immediate application of Theorem 1 to (54). In particular, $H_m(F)$ is ordinary $\tau$-real: since
$\mathcal B(x(x+1))=z(z+2)\in\mathcal C$, the Bell-product theorem applied to $P_{H_m(F)}=x(x+1)Q_m$ gives the claim.

### 5.4 Attachment along an edge

Suppose an ordinary $\tau$-real graph $G$ and $H_m(F)$ intersect in exactly a common edge, with no additional vertex identifications or cross edges. The chromatic-polynomial product formula along a complete intersection of size two is

$$
 \chi_{G\cup H_m(F)}(q)
 =\frac{\chi_G(q)\chi_{H_m(F)}(q)}{q(q-1)}.
 \tag{56}
$$

Indeed, fixing the two distinct colors on the common edge leaves independent coloring choices on the two sides. Under the unsigned reflection (45), (56) becomes

$$
 P_{G\cup H_m(F)}=P_GQ_m.
 \tag{57}
$$

Both factors on the right have Bell transforms in $\mathcal C$, by the hypothesis on $G$ and (55). Equation (48) proves that the union is ordinary $\tau$-real.

The same conclusion holds for an empty or single-vertex complete intersection, again with no additional identifications or cross edges. The corresponding unsigned factorizations are

$$
 P_{G\cup H_m(F)}=
 \begin{cases}
 P_G\,x(x+1)Q_m,&\text{empty intersection},\\
 P_G\,(x+1)Q_m,&\text{one common vertex}.
 \end{cases}
 \tag{58}
$$

Here $\mathcal B(x+1)=z+1\in\mathcal C$, so repeated use of (48) applies. These operations are iterable because their output is ordinary $\tau$-real. The edge quotient alone gives no assertion for larger complete intersections in $H_m(F)$ itself. The next construction adds a universal clique and gives a specific larger-clique consequence.

### 5.5 A standard universal clique lift

Write

$$
 R_0(x)=1,\qquad R_j(x)=\prod_{h=0}^{j-1}(x+h)\quad(j\ge1).
 \tag{59}
$$

Suppose a graph $H$ has a polynomial quotient
$Q_H=P_H/R_2$ with $\mathcal B(Q_H)\in\mathcal C$.
For $s\ge0$, let $J=K_s\vee H$ be the join obtained by adding a clique of $s$ new vertices, each adjacent to every vertex of $H$. Choosing the distinct clique colors first, and then reflecting the chromatic identity, gives

$$
 P_J(x)=R_s(x)P_H(x+s)
       =R_{s+2}(x)Q_H(x+s).
 \tag{60}
$$

Repeated application of (52) yields
$\mathcal B(Q_H(x+s))=S^s\mathcal B(Q_H)\in\mathcal C$.
Here preservation by $S$ follows from Section 2.1 and the same fixed-degree limits used in Section 4. For every integer $0\le j\le s+2$,

$$
 \frac{P_J(x)}{R_j(x)}
 =Q_H(x+s)\prod_{h=j}^{s+1}(x+h),
 \qquad
 \mathcal B\!\left(\frac{P_J}{R_j}\right)\in\mathcal C.
 \tag{61}
$$

The product is empty when $j=s+2$. The Bell conclusion follows from (48), because every linear factor has Bell transform $z+h\in\mathcal C$.

If an ordinary $\tau$-real graph $G$ intersects $J$ in exactly a common clique of size $j\le s+2$, with no additional identifications or cross edges, the complete-intersection coloring formula gives

$$
 P_{G\cup J}=P_G\frac{P_J}{R_j}.
 \tag{62}
$$

Equations (48) and (61) prove that the union is ordinary $\tau$-real. Thus $J$ is attachable along every clique of size at most $s+2$ that it contains. If $H$ is triangle-free, every clique of $J$ has size at most $s+2$, so these include all its possible complete intersections.

In particular, take $H=H_m(F)$ with $m\ge2$ and $F$ edgeless, including the empty graph. Such $F$ is ordinary $\tau$-real: its unsigned chromatic polynomial is a power of $x$, whose Bell transform is in $\mathcal C$ by repeated application of (48) to $\mathcal Bx=z$. The graph $H_m(F)$ is triangle-free, since the endpoints of the path are nonadjacent and the substituted vertices have no mutual edges or neighbors among the internal path vertices. Corollary 4 supplies its Bell-real edge quotient. Hence $K_s\vee H_m(F)$ is attachable to an ordinary $\tau$-real graph along any complete intersection, under the same no-extra-identifications and no-cross-edges convention. This is the stated clique-lift consequence, not unrestricted larger-clique attachment for general substituted graphs.

## 6 Exact checks and the separate star core question

The proof above is uniform in both $m$ and the input degree. It does not depend on numerical root tests or on checking a finite range of either parameter.

The accompanying relative checkers are:

* [`check_invariant_algebra.py`](check_invariant_algebra.py), for the exact algebra used by the invariant and its boundary calculation.
* [`check_independent.py`](check_independent.py), for a separate exact verification of the spectral-potential identities, endpoint signs, and degree-one formulas.

The scripts support the displayed algebra; the root-monotonicity, matrix, and limiting arguments establish the arbitrary-degree theorem. The defining recurrence and the graph bridge are polynomial identities, not numerical approximations.

A separate weighted-matching star-core approach provides a sufficient realization criterion for individual operators and, in particular, an exact realization of $A_5$. Its uniform parameter-feasibility problem asks whether every member of that particular ansatz can be realized with the required root and nonnegative-weight conditions. The present arrowhead proof resolves preservation by all $A_m$ without resolving that additional realization problem. Existing obstructions to specific star-core continuation or factorwise tests remain method obstructions, not counterexamples to the preservation theorem.

## Reference

[1] F. Brenti, G. F. Royle, and D. G. Wagner, *Location of Zeros of Chromatic and Related Polynomials of Graphs*, Canadian Journal of Mathematics **46** (1994), 55–80. Bell-product identity and preservation: Propositions 4.2 and 4.4. [DOI 10.4153/CJM-1994-002-3](https://doi.org/10.4153/CJM-1994-002-3).
