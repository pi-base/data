---
uid: I000025
if:
  and:
  - t_2: true
  - paracompact: true
then:
  t_4: true
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
---
If $X$ is $T_2$ paracompact, let $a \in X$ and $B \subset X$ disjoint from $a$. Then by $T_2$, for each $b \in B$ there is an open $U_b \subset X$ with $a \notin cl(U_b)$. Cover $X$ by all the sets $U_b$ along with $X \setminus B$ and take a locally finite open refinment that covers $B$. Then if $\mathcal{V}$ is the subcollection of all elements which intersect $B$. Then $\cup \mathcal{V}$ is an open set containing $B$ and $a \notin cl(\cup \mathcal{V})$ since $\mathcal{V}$ is locally finite and locally finite collections are closure preserving. Thus $X$ is $T_3$.

Similarly, for each $b \in B$ there is an open $U_b \subset X$ with $A \cap cl(U_b) = \emptyset$. Cover $X$ by all the sets $U_b$ along with $X \setminus B$ and take a locally finite open refinment that covers $B$. Then if $\mathcal{V}$ is the subcollection of all elements which intersect $B$. Then $\cup \mathcal{V}$ is an open set containing $B$ and $A \cap cl(\cup \mathcal{V}) = \emptyset$ since $\mathcal{V}$ is locally finite and locally finite collections are closure preserving. Thus $X$ is $T_4$.

Asserted in Figure 7 of {{doi:10.1007/978-1-4612-6290-9}}.
