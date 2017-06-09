---
uid: T000023
space: right-half-open-interval-topology
property: completely-normal
value: true
refs:
  - doi: 10.1007/978-1-4612-6290-9_6
    name: Counterexamples in Topology
---
Let $A,B \subset X$ with $cl(A) \cap B = A \cap cl(B) = \emptyset$. Since $A \subset X \setminus cl(B)$ chose for each $a \in A$ an interval $[a, x_a) \subset X \setminus cl(B)$. Then $O_A = \cup_{a \in A} [a, x_a)$ is an open set containing $A$. Define $O_B$ similarly. If $O_A \cap O_B \neq \emptyset$, then there are $a \in A$ and $b \in B$ so that $[a, x_a) \cap [b, x_b) \neq \emptyset$. Thus either $b \in [a, x_a)$ or $a \in [b, x_b)$, a contradiction. Thus $O_A$ and $O_B$ are disjoint, as required.

Asserted in the General Reference Chart for space #51 in
{{doi:10.1007/978-1-4612-6290-9_6}}.
