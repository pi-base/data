---
uid: S000016
slug: finite-complement-topology-on-an-uncountable-space
name: Finite Complement Topology on the Real Numbers
aliases:
  - Finite Complement Topology on an Uncountable Space
counterexamples_id: 19
refs:
- doi: 10.1007\/978-1-4612-6290-9_6
  name: Counterexamples in Topology
- wikipedia: Finite_complement_topology
  name: Finite complement topology on Wikipedia
---
The finite complement topology on a space $X$ is defined by taking
$U \subset X$ to be open if and only if $X \setminus U$ is finite or
$U = \emptyset$. In this case we let \(X=\mathbb R\) so it has cardinality
\(\mathfrak c\).

Defined as counterexample #19 ("Finite Complement Topology on an Uncountable Space")
in {{doi:10.1007\/978-1-4612-6290-9_6}}.

<!-- [[Proof of Topology]]
1) $U = \emptyset$ is open by definition. Now let $U = X$. This implies $X/U = X/X = \emptyset$.

2) Let $A$ be a collection of open sets in $X$. Let $U = \bigcup\limits_{i=1}^{\infty}a_i$ where $a_i \in U$. We want to show that $X/U$ is finite or $\emptyset$. So, $X/U = X /\bigcup\limits_{i=1}^{\infty}a_i = (X/ a_i) \cap (X/a_{i+1}) \cap \dots$. An arbitrary intersection of finite sets is finite.

3) Let $A$ be a collection of open sets in $X$. Let $U = \bigcap\limits_i^j a_i$ where $a_i \in A$. So, $X/U = X/\bigcap\limits_i^j a_i = (X/a_i) \cup (X/a_{i+1}) \cup \dots \cup (X/a_j)$. A finite union of finite sets is finite. -->
