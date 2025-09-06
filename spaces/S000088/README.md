---
uid: S000088
name: Tychonoff corkscrew
counterexamples_id: 90
refs:
  - zb: "0386.54001"
    name: Counterexamples in Topology
  - doi: 10.1007/BFb0064021
    name: Hereditarily separable, non-completely regular spaces
  - zb: "0652.54016"
    name: Extensions and absolutes of Hausdorff spaces
---

Let $Y$ be {S79}, $H = \omega_1\times \{\omega\}$ and $K = \{\omega_1\}\times \omega$ be subspaces of $Y$. Define $Z = (Y\times \mathbb{Z}) \cup \{p^-, p^+\}$ where $p^\pm$ are two new points to have topology such that $U\subseteq Z$ is open iff $U\cap (Y\times \mathbb{Z})$ is open in the product topology where $\mathbb{Z}$ is discrete, and if $p^\pm\in U$ then $Y\times \{n\in \mathbb{Z} : (-1)^{\pm 1}n\geq N\}\subseteq U$ for some $N\in\mathbb{N}$.
Define $X$ as the quotient space $Z/{\sim}$ where the equivalence relation $\sim$ is given by $(x, 2n)\sim (x, 2n+1)$ for $x\in H$ and $(x, 2n-1)\sim (x, 2n)$ for $x\in K$, and no other relations between distinct points.

This is a double-sided variation of the "Jones machine" construction, described in the comment after corollary in  {{doi:10.1007/BFb0064021}}. Also see the space $\text{DJ}(Y)$ of exercise 1Y.6 in {{zb:0652.54016}}.

The space $X$ is defined in a more informal way as counterexample #90 ("Tychonoff Corkscrew")
in {{zb:0386.54001}}.
