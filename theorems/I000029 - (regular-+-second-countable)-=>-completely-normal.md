---
uid: I000029
if:
  and:
  - regular: true
  - second-countable: true
then:
  completely-normal: true
---
If $X$ is second countable and regular and $A,B \subset X$ with $cl(A) \cap B = A \cap cl(B) = \emptyset$, every point of $a$ has a neighborhood disjoint from $B$ and thus, by regularity, a neighborhood $C$ with closure disjoint from $B$. For each $x$ and $C$, choose a basic open set $U$ with $x \in B \subset V$. Then the collection of all such basis elements is a countable cover of $A$ and may be written as $\{U_n\}$ for $n \in \omega$. Let $\{V_n\}$ be a collection defined similarly for $B$. Let $U'_n = U_n \setminus \cup_{i \leq n} cl(V_i)$ and $V'_n = V_n \setminus \cup_{i \leq n} cl(U_i)$. Then if $U' = \cup U'_n$ and $V' = \cup V'_n$ then $U', V'$ are disjoint open sets containing $A$ and $B$ respectively.

