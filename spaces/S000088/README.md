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

The space $X=\mathrm{DJ}(Y,H,K)$ is the result of applying the double-sided variation of the "Jones machine" to the space $Y=$ {S79} and its two closed subsets $H=\omega_1\times\{\omega\}$ and $K=\{\omega_1\}\times\omega$ (which have the property that they cannot be separated by open sets in $Y$). It is obtained by taking a two-sided sequence of copies of $Y$, plus two extra limit points, and alternately gluing adjacent copies of $Y$ along either $H$ or $K$.

Formally, define $Z = (Y\times \mathbb{Z}) \cup \{p^-, p^+\}$ where $p^\pm$ are two new points to have topology such that $U\subseteq Z$ is open iff $U\cap (Y\times \mathbb{Z})$ is open in the product topology where $\mathbb{Z}$ is discrete, and if $p^\pm\in U$ then $Y\times \{n\in \mathbb{Z} : (-1)^{\pm 1}n\geq N\}\subseteq U$ for some $N\in\mathbb{N}$. Define $X$ as the quotient space $Z/{\sim}$ where the equivalence relation $\sim$ is given by $(x, 2n)\sim (x, 2n+1)$ for $x\in H$ and $(x, 2n-1)\sim (x, 2n)$ for $x\in K$, and no other relations between distinct points.

The construction above is described in Problem 1Y in {{zb:0652.54016}}, based on the original idea in {{doi:10.1007/BFb0064021}}.

The space $X$ is defined in a more informal way as counterexample #90 ("Tychonoff Corkscrew") in {{zb:0386.54001}}.
