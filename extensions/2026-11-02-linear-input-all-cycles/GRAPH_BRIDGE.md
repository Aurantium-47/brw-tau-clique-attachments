# From the operator theorem to the graph subfamily

Let F consist of a maximum clique K_r and one extra vertex with d neighbors in it, where r>=1 and 0<=d<=r-1 are integers. Direct coloring gives
chi_F(k)=(k)_r(k-d), hence P_F(x)=(-1)^(r+1)chi_F(-x)=R_r(x)(x+d).
Thus its maximal Bell quotient is h=z+d. Lower quotients follow by the standard operators L_j=z(1+D)+j, which preserve the nonpositive-root cone by derivative interlacing. In particular F has the full clique-quotient property.

Replace one vertex of C_(m+2) by F. Denote its two neighboring vertices by u,v and the path between them outside F by a path of length m. Every vertex of F is adjacent to u and v, and there are no other edges to the path. For m>=2 the output clique number is r+1.

For fixed endpoint colors on a length-m path, let A_m count proper path colorings when those colors are equal, and B_m when distinct. The elementary transition matrix of the complete graph without loops has eigenvalues k-1 and -1, so
A_m=((k-1)^m+(k-1)(-1)^m)/k,
B_m=((k-1)^m-(-1)^m)/k.
These formulas can also be verified by the two-state recurrence A_(m+1)=(k-1)B_m, B_(m+1)=A_m+(k-2)B_m, with A_1=0,B_1=1.
Accordingly
chi_H(k)=k A_m chi_F(k-1)+k(k-1)B_m chi_F(k-2).

Put sigma_m(t)=1+t+...+t^(m-1). Substitution k=-x and the unsigned normalization yield the exact polynomial identity
P_H/[x(x+1)]=sigma_m(x+1)P_F(x+2)-sigma_(m-1)(x+1)P_F(x+1).
Here sigma_0=0. Cancellation of rising factorials then gives, for m>=2,
Q_m=P_H/R_(r+1)
=(x+r+1)sigma_m(x+1)(x+d+2)
 -(x+1)sigma_(m-1)(x+1)(x+d+1).
This cancellation uses R_r(x+2)x(x+1)/R_(r+1)(x)=x+r+1 and R_r(x+1)x(x+1)/R_(r+1)(x)=x+1.

The same algebra defines Q_1=(x+r+1)(x+d+2), and geometric-series recurrence gives
Q_(m+1)=(x+1)Q_m+(x+r+1)(x+d+2)-(x+1)(x+d+1).
The Bell rules B[(x+c)g]=[z(1+D)+c]B[g] and B[g(x+1)]=(1+D)B[g] turn this exactly into F1=(L+r)p and F_(m+1)=L F_m+H from the proved linear-input theorem, with h=z+d,p=z+d+2,q=1 and H=Lq+r p.
Thus BQ_m has nonpositive real roots for every m>=2, and the lower clique quotients follow again by applying L_j. This proves the graph assertion for every cycle of length at least4.

For m=1 the graph is K2 joined to F; its maximal clique size is r+2 rather than r+1. Directly P_H=R_(r+2)(x)(x+d+2), so the Bell transform of its maximal quotient is z+d+2 (the raw quotient is x+d+2), and lower quotients follow as above. This handles the triangle separately without misidentifying Q_1 as the maximal quotient.

This argument proves the subfamily and its normalization; it does not establish historical novelty or the arbitrary-input-degree cycle claim.
