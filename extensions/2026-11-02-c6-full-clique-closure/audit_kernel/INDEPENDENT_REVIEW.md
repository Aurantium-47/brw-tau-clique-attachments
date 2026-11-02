# Independent review: m=4 stability mass splitting

2026-11-02.

## Verdict

ACCEPT the abstract rootedness proof. The author has included the explicit W real-rootedness supplement; its three quadratic discriminants and four sign-changing base intervals were independently verified. The originally requested sparse-vertex statement has been strengthened correctly to every nonnegative kappa vector with total at most one. The argument does not prove interlacing with T_4, and does not prove any m>=5 statement or historical novelty.

For p(z)=prod(z+a_i), a_i>=0, q=sum_i a_i kappa_i prod_{j!=i}(z+a_j), kappa_i>=0, sum kappa_i<=1, and r>=0, the output

(U_4+rR_4) star p +(R_4-1) star q

has only nonpositive real roots.

## Independent checks

1. Recomputed U_4,R_4, A=S(U_4+rR_4), C=U_4+rR_4+R_4-1, their resultant and discriminants.
2. Verified exact alternating root intervals for A,C at r=0. Both remain simple and real for r>=0 and their resultant never vanishes, so the orientation of interlacing persists.
3. Verified W=U_4+rR_4 independently rather than importing a prior constant-input theorem. Its discriminant is

r^4(229r^2-660r+1000)+r^2(7798r^2-10122r+10000)+(82229r^2-47278r+227081).

All three quadratics have positive leading coefficients and negative discriminants. Thus Disc(W)>0 for every real r. A Sturm count gives four negative roots at r=0, so W stays simple real-rooted for all real r. For r>=0 its coefficients are positive, hence its roots are negative. Consequently W/SW is a rational Pick function with the same orientation as C/SW.
4. Checked the logarithmic-derivative proof that a fresh-variable operator 1+y(1+D_w) preserves complex stability. Its proof is valid with other variables specialized anywhere in the upper half-plane, and includes constants in w.
5. Independently verified the partial-symmetrization source: Borcea, Branden and Liggett, *Negative dependence and the geometry of polynomials*, JAMS22(2009), Theorem4.20 and proof on printed p550. The proof works for complex stable polynomials in two swapped variables after fixing every other upper-half-plane coordinate. Therefore w need not be multiaffine here. Primary source:
https://www.ams.org/journals/jams/2009-22-02/S0894-0347-08-00618-8/S0894-0347-08-00618-8.pdf
6. Checked the mass-splitting algorithm. At each step a coordinate transposition acts on the omitted-factor terms exactly as a swap of the kappa coefficients. Starting with all mass in coordinate1, successive partial symmetrizations realize every nonnegative target vector with the same total. This is a special stability-preserving sequence, not an invalid arbitrary convex-combination argument.
7. Recomputed a fully symbolic three-coordinate mass split, the positive diagonal identity, and the equality with L^4p+(L+L^2+L^3)q+r(I+L+L^2+L^3)p.
8. Boundary handling is sound: a_i>0 gives positive diagonal scaling; a_i=0 follows by coefficient limits with fixed monic leading degree. The zero-degree case is W. Nonnegative coefficients and nonzero leading coefficient exclude positive roots and the zero polynomial.

## Reproducibility

`python -I -O check_independent.py` passed. It independently checks the scalar certificates, base root order, original diagnostic kernel factorization, symbolic mass splitting, Bell diagonal, and actual operator equality. These finite algebra checks support the universal analytic proof; they are not substituted for it.

## Scope limits

The old concern that real-rooted vertices need not have real-rooted convex mixtures is resolved by the verified partial-symmetrization construction. No unrestricted convexity is asserted. The proof uses a classical multivariate stability theorem, which must be credited, and no global priority claim is justified. Actual-cycle seed residue hypotheses and the graph coloring translation, if used in a subsequent corollary, must be stated and checked separately.
