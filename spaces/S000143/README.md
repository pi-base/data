---
uid: S000143
name: Butterfly space
aliases:
- Bow-tie space
refs:
  - zb: "0148.16701"
    name: $\aleph_0$-spaces (E. Michael)
  - zb: "0684.54001"
    name: General Topology (Engelking, 1989)
---

The space $X=\mathbb R\times [0,\infty)$ is the closed upper half-plane topologized as follows.  Points above the $x$-axis have their usual Euclidean neighborhoods.  A local base for a point $p$ on the $x$-axis is formed by the "butterfly neighborhoods" $N_\varepsilon(p)$ for $\varepsilon>0$, where $N_\varepsilon(p)$ consists of $p$ together with all points $q=\langle q_x,q_y\rangle$ at distance less than $\varepsilon$ from $p$ and lying underneath the union of the two rays in $X$ that emanate from $p$ and have slopes $\varepsilon$ and $-\varepsilon$.  In formula, $$N_\varepsilon(p)=\{p\} \cup \{q\in X:\|q-p\|<\varepsilon\text{ and }q_y<\varepsilon|q_x-p_x|\}.$$

Defined as Example 12.1 in {{zb:0148.16701}} (<https://www.jstor.org/stable/24901448>).

Exercise 3.1.I in {{zb:0684.54001}} defines a very similar space of the same name, with a slightly different topology but essentially the same properties.
