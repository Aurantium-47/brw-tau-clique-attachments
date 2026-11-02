# Next-cycle propagation: exact reduction and bounded outcome

2026-11-02. No all-degree m=4 theorem or novelty claim.

## Outcome

The new m=3 theorem does not by itself establish the old arrowhead invariant for its output/source pair. No degree-free propagation proof was obtained in this pass. A separate exact resultant calculation does establish that invariant for every **linear actual seed** h=z+a, a>=0, and real r>=1. Together with the previously proved invariant propagation lemma, that gives all subsequent cycle lengths for this subfamily. See `../brw_m4_invariant_probe_20261102/LINEAR_SEED_PROOF.md` and its complete exact certificate. That lemma is submitted for independent review rather than assumed accepted here.

The following m=4 sign reduction is exact and can support a future degree-free proof. It is a reduction, not a proof that the required sign holds.

## Setup
Let L=z(1+D)+1, p=prod_i(z+a_i), a_i>0, and
q/p=sum_i a_i*kappa_i/(z+a_i), with 0<=kappa_i<=1/2 and sum kappa_i<=1.
For actual cycle inputs, p=(1+D)^2 h and q=D(1+D)h.
Put
T_4=(I+L+L^2+L^3)p,
F_4=L^4p+(L+L^2+L^3)q.
The desired output is F_4+r T_4.
The classical Bell product gives T_4=R_4 star p, where
R_4=z^3+7z^2+11z+4.
R_4 has three simple negative roots (discriminant229 and a direct Sturm count); therefore the classical Bell-product theorem gives nonpositive real roots for T_4. This alone says nothing about its compatibility with F_4.

## Root moments
At a negative zero t of T_4 which is not a zero of p, write
u_i=t/(t+a_i), s=t+sum_i u_i,
v=sum_i u_i^2, w=sum_i u_i^3, x=sum_i u_i^4.
Then the exact root equation is
A=s^3+7s^2+11s+4-(3s+7)v+2w=0.
Every u_i lies outside [0,1], and s<sum_i u_i<=v. These are extra admissibility constraints, not optional numerical assumptions.

Set
B=3s^2+14s+11-3v, C=3s+7.
Indeed z p'/p=sum u_i, z^2 p''/p=(sum u_i)^2-v, and z^3 p'''/p=(sum u_i)^3-3(sum u_i)v+2w. Substitution into R_4 star p proves the displayed equation identically. Also z d/dz(s)=s-v, z d/dz(v)=2(v-w), and z d/dz(w)=3(w-x).

The exact derivative identity at a root is
D0=t T_4'(t)/p(t)
 =B(s-v)-2C(v-w)+6(w-x)
 =3s^3-3s^2v+14s^2-23sv+6sw+11s+3v^2-25v+20w-6x.
Unlike m=3, the root equation is cubic in s and does not yield a simple bound of the form v=X^2-1. It has three branches even for constant p, so assigning D0 one fixed sign is invalid.

The exact numerator at the same root is
N=F_4(t)/p(t)
 =D0+1-sum_i kappa_i (1-u_i)[1+B u_i-2C u_i^2+6u_i^3].
This follows from F_4=(L-1)T_4+p+(I+L+L^2+L^3)q-q and the product rule. More explicitly, writing eta=q/p, the commutator at a root has normalized value B z eta'+C z^2 eta''+z^3 eta'''. For each term kappa_i(1-u_i), its three scaled derivatives are -kappa_i u_i(1-u_i), 2kappa_i u_i^2(1-u_i), and -6kappa_i u_i^3(1-u_i). These identities give N for arbitrary input degree, not only the finite checker fixtures.
If T_4 has simple roots and p is nonzero at them, strict compatibility is equivalent to
F_4(t)/T_4'(t)=t N/D0<0,
that is, N and D0 have the same sign at every root.

N is affine in the kappa vector. Hence it suffices to prove this inequality for zero, one or two active coordinates equal to1/2, exactly as in the m=3 polytope reduction. No such degree-free inequality is established here.

## Recurrence route and its exact missing hypothesis
For fixed actual seed h and fixed r, H=Lq+r p and F_(m+1)=L F_m+H. The accepted m=3 theorem proves F_3 is real-rooted, but applying the older arrowhead propagation lemma additionally requires
|H(t_i)/((-t_i)F_3'(t_i))|<1,
0<H(0)/F_3(0)<=1,
and sum_i kappa_i^2/(1-kappa_i)<=2-H(0)/F_3(0).
Rootedness alone is not that hypothesis. The new linear-seed certificate proves it for degree1; a degree-independent proof or exact counterexample remains missing.

## Supporting computation boundaries
`check_m4_identities.py` checks the displayed moment identities independently against differential-operator expansion on exact rational seeds, and the cubic R_4 root count. It does not prove the unresolved sign inequality.
`probe.py` made15000 floating-point abstract m=4 attempts with no detected failure. Numerically nonreal T roots were skipped. This is exploratory only, not an exhaustive check or a theorem premise; it is not part of an exact certificate.
