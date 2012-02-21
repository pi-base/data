---
uid: I000030
if:
  and:
  - regular: true
  - lindelof: true
then:
  normal: true
---
If $X$ is Lindelof and regular and $A,B \subset X$ are closed and disjoint, every point of $a$ has a neighborhood disjoint from $B$ and thus, by regularity, a neighborhood with closure disjoint from $B$. The collection of all such neighborhoods covers $A$, which is Lindelof, and so has a countable subcover which may be written as $\{U_n\}$ for $n \in \omega$. Let $\{V_n\}$ be the corresponding cover of $B$. Let $U'_n = U_n \setminus \cup_{i \leq n} \cl(V_i)$ and $V'_n = V_n \setminus \cup_{i \leq n} \cl(U_i)$. Then if $U' = \cup U'_n$ and $V' = \cup V'_n$ then $U', V'$ are disjoint open sets containing $A$ and $B$ respectively.

