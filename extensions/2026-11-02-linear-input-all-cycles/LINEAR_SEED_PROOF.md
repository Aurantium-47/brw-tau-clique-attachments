# An all-iteration arrowhead seed for linear Bell inputs

2026-11-02. Proposed exact lemma for independent review. Not an all-degree theorem or historical-novelty claim.

## Result
For every a>=0 and r>=1, let h=z+a, S=1+D, L=z(1+D)+1,
p=S^2 h=z+a+2, q=DSh=1, and H=Lq+r p=(r+1)z+r(a+2)+1.
Define F_1=(L+r)p and F_(m+1)=L F_m+H. Then the previously proved arrowhead invariant holds at F_3. Consequently every F_m for m>=3 has simple strictly negative roots; successive outputs strictly interlace. The earlier m=1,2 results cover the shorter ranges. This removes the cycle-length bound for this linear-input subfamily, but says nothing uniform about higher input degree.

This statement uses the existing rigorously reviewed arrowhead lemma in `brw_uniform_operator_deliverable_20261102/RESEARCH_NOTE.md`, Lemma 2. That lemma says: for monic simple strictly-negative-root F and fixed lower-degree H with H(0)>0, define kappa_i=H(t_i)/((-t_i)F'(t_i)), w=H(0)/F(0), V=sum kappa_i^2/(1-kappa_i). If |kappa_i|<1, 0<w<=1, V<=2-w, then L F+H has the same invariant and strict negative roots/interlacing.

## Explicit seed
Direct recurrence expansion gives

F_3 = z^4+(a+r+11)z^3+(ar+6a+8r+32)z^2
      +(4ar+7a+15r+26)z+(3ar+a+6r+4).

In particular F_3(0)-H(0)=2ar+a+4r+3>0, so 0<w<1.

## Exact positive-coefficient certificates
Put R(u)=Res_z(F_3,z F_3'+u H), D=R(1), M=R(-1), G=R'(1)+2R(1), and Delta=disc_z(F_3).
The complete integer-coefficient expansions are in `linear_seed_certificate.json`; `check_linear_seed.py` independently recomputes them from the displayed operators by exact resultant/discriminant arithmetic. There are two sectors covering the entire parameter domain:

1. r=a+t+1, with a,t>=0 (r-1>=a);
2. a=b+t and r=b+1, with b,t>=0 (a>=r-1).

In each sector every coefficient and the constant coefficient of each of Delta,D,M,G is strictly positive. The term counts are 54 for Delta and 74 each for D,M,G. Thus all four are strictly positive everywhere in the closed parameter domain. This is an exact finite polynomial identity certificate valid for all parameter values, not numerical sampling.

## Root continuity and residue bounds
The positive discriminant excludes collisions. At (a,r)=(0,1),
F_3=z^4+12z^3+40z^2+41z+10,
and exact Sturm calculations give one root in each of the four intervals
(-7.220,-7.219), (-3.202,-3.201), (-1.226,-1.225), (-0.353,-0.352).
They exhaust the degree. Connectedness, fixed monic degree, and nonzero discriminant therefore imply four simple real roots throughout the parameter domain. All coefficients are positive, excluding nonnegative roots.

The ordered roots and the kappa_i vary continuously. At the base point, rational interval evaluation of -H(t)/(tF_3'(t)) in those isolating intervals proves -1<kappa_i<1; exact interval endpoints/bounds are in the certificate. D and M never vanish. Since
zF_3'+H at a root = zF_3'(1-kappa_i),
zF_3'-H at a root = zF_3'(1+kappa_i),
no kappa_i can cross either endpoint +/-1. Therefore |kappa_i|<1 throughout.

## Trace identity and the V bound
As F_3 is monic,
R'(1)/R(1)=sum_i H(t_i)/(t_iF_3'(t_i)+H(t_i))
           =-sum_i kappa_i/(1-kappa_i)=-(w+V).
Here sum kappa_i=w follows by partial fractions of H/F_3 at zero. Thus
2-w-V = (R'(1)+2R(1))/R(1)=G/D>0.
The denominator and numerator positivity were certified above. This proves every hypothesis of the arrowhead lemma at F_3; induction gives the claimed all-iteration conclusion.

## Scope and checks
The exact checker uses explicit RuntimeError guards, works under python -O, recomputes all sector polynomials and every certificate coefficient, checks the four base intervals by Sturm, and checks the trace identity independently using a quotient-ring multiplication trace at a rational point. The written product-of-roots identity supplies its general proof.

Two 100,000-attempt floating-point searches found no invariant failure at F_3, once for actual inputs of degrees 0..8 and once for abstract extreme-residue seeds. A separate abstract F_2 search also found none. These exploratory observations are not premises, not exact all-case checks, and do not establish the higher-degree invariant. Numerically unstable/non-real-root results were skipped. The precise remaining gap is a degree-independent proof (or exact counterexample) for the invariant at F_2 or F_3.
