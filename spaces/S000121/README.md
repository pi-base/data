---
uid: S000121
name: Bernstein's connected set
counterexamples_id: 124
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
---
Let \(\{C_\alpha\ : \alpha<\mathfrak c\}\) be a well-ordering of the set of
all closed, {P36} subsets of {S176}.
We shall define \(A_\alpha\) and \(B_\alpha\) such that
\(A_\alpha \cap B_\beta = \emptyset\) for all \(\alpha, \beta<\mathfrak c\).
First, let \(A_0,B_0\) be distinct singletons in \(\mathbb{R}^2\).
Now, assuming \(A_\beta,B_\beta\) are defined for all \(\beta<\alpha\)
and \(|\bigcup_{\beta<\alpha}A_\beta\cup B_\beta|<\mathfrak c\),
we may choose \(A_\alpha=\{a_\alpha\}\cup\bigcup_{\beta<\alpha}A_\beta\)
and \(B_\alpha=\{b_\alpha\}\cup\bigcup_{\beta<\alpha}B_\beta\) such that
\(a_\alpha,b_\alpha\) are distinct points in
\(C_\alpha\setminus\left(\bigcup_{\beta<\alpha}A_\beta\cup B_\beta\right)\).

Bertstein's connected set is \(A=\bigcup_{\alpha<\mathfrak c}A_\alpha\)
with its subspace topology.

Defined as counterexample #124 ("Bernstein's Connected Sets")
in {{doi:10.1007/978-1-4612-6290-9}}.