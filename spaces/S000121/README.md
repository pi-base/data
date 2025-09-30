---
uid: S000121
name: Bernstein's connected set
counterexamples_id: 124
refs:
  - zb: "0386.54001"
    name: Counterexamples in Topology
---

Let $\{C_\alpha\ : \alpha<\mathfrak c\}$ be a well-ordering of the set of
all closed, {P36} subsets of {S176} that contain at least two points
(so in fact each $C_\alpha$ has cardinality $\mathfrak c$).
Note that there are $\mathfrak c$ such $C_\alpha$.
We shall define sets $A_\alpha$ and $B_\alpha$ such that
$A_\alpha \cap B_\beta = \emptyset$ for all $\alpha, \beta<\mathfrak c$.
First, let $A_0$, $B_0$ be distinct singletons in $\mathbb{R}^2$.
Now, assuming $A_\beta,B_\beta$ are defined for all $\beta<\alpha$
and $|\bigcup_{\beta<\alpha}(A_\beta\cup B_\beta)|<\mathfrak c$,
we may choose $A_\alpha=\{a_\alpha\}\cup\bigcup_{\beta<\alpha}A_\beta$
and $B_\alpha=\{b_\alpha\}\cup\bigcup_{\beta<\alpha}B_\beta$ such that
$a_\alpha,b_\alpha$ are distinct points in
$C_\alpha\setminus\left(\bigcup_{\beta<\alpha}(A_\beta\cup B_\beta)\right)$.

Bernstein's connected set is $A=\bigcup_{\alpha<\mathfrak c}A_\alpha$
with its subspace topology induced from {S176}.

Defined as counterexample #124 ("Bernstein's Connected Sets")
in {{zb:0386.54001}}.
