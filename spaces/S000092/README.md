---
uid: S000092
name: Thomas corkscrew
counterexamples_id: 94
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
---

For a space $X$, define $Z = X\times \mathbb{N} \cup \{p\}$ where $p$ is a new point to have topology such that $U\subseteq Z$ is open iff $U\cap (X\times \mathbb{N})$ is open in the product topology where $\mathbb{N}$ is {S2}, and if $p\in U$ then $X\times \{n\in \mathbb{N} : n\geq N\}\subseteq U$ for some $N$. If $H, K\subseteq X$ are disjoint closed subsets which can't be separated by open sets, define $\text{J}(X) = Z/\sim$ where $\sim$ is such that $(x, 2n)\sim (x, 2n+1)$ for $x\in H$ and $(x, 2n-1)\sim (x, 2n)$ for $x\in K$ and let $q:Z\to \text{J}(X)$ be the quotient map. Define $\text{DJ}(X) = (\text{J}(X)\times \{0, 1\})/\sim$ where $(x, 0)\sim (x, 1)$ for $x\in q(X\times \{1\})$. If $g:\text{J}(X)\times \{0, 1\}\to \text{DJ}(X)$ is the quotient map denote $p^+ = g(p, 1)$ and $p^- = g(p, 0)$. Thomas corkscrew is defined as $\text{DJ}(X)$ where $X$ is {S91}, $H = L_0$ and $K = \{(0, \frac{1}{n}) : n\in\mathbb{N}\}$.

Defined as counterexample #94 ("Thomas' Corkscrew")
in {{doi:10.1007/978-1-4612-6290-9}}.
