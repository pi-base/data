---
uid: S000088
name: Tychonoff corkscrew
counterexamples_id: 90
refs:
  - zb: "0386.54001"
    name: Counterexamples in Topology
  - zb: "0652.54016"
    name: Extensions and absolutes of Hausdorff spaces (Porter & Woods)
  - mo: 331563
    name: Answer to "Regular spaces that are not completely regular"
---

The space $X=\text{DJ}(Y, H, K)$, i.e., the result of applying the "Jones machine" to the space $Y=$ {S79} and its two closed subspaces $H = \omega_1\times \{\omega\}$ and $K = \{\omega_1\}\times \omega.$

As described in Problem 1Y of {{zb:0652.54016}}, the "Jones machine" is a general method of constructing
{P5} spaces that are not {P9} (and hence also not {P6}),
starting with a {P5} space $Y$ that is not {P7},
and two disjoint closed subsets $H$ and $K$ that cannot be separated by open sets.
The space $X=\text{DJ}(Y, H, K)$ is obtained by taking countably many copies of $Y$, plus two extra points, and alternately gluing adjacent copies of $Y$ along either $H$ or $K$.

In detail, let $Z = (Y\times \mathbb{Z}) \cup \{p^-, p^+\}$ where $p^\pm$ are two new points to have topology such that $U\subseteq Z$ is open iff $U\cap (Y\times \mathbb{Z})$ is open in the product topology where $\mathbb{Z}$ is discrete, and if $p^\pm\in U$ then $Y\times \{n\in \mathbb{Z} : (-1)^{\pm 1}n\geq N\}\subseteq U$ for some $N\in\mathbb{N}$.
Define $\text{DJ}(Y, H, K)$ as the quotient space $Z/{\sim}$ where the equivalence relation $\sim$ is given by $(x, 2n)\sim (x, 2n+1)$ for $x\in H$ and $(x, 2n-1)\sim (x, 2n)$ for $x\in K$, and no other relations between distinct points.

("DJ" seems to stand for "double-sided Jones" in {{zb:0652.54016}}.
See also {{mo:331563}} for background.)

The space $X$ is defined in a more informal way as counterexample #90 ("Tychonoff Corkscrew")
in {{zb:0386.54001}}.
