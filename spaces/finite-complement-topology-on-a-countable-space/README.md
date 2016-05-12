---
uid: S000015
slug: finite-complement-topology-on-a-countable-space
name: Finite Complement Topology on a Countable Space
---
$U \subset X$ is open if and only if $X \setminus U$ is finite or $U = \emptyset$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 49-50.
* [Cofinite topology](http://en.wikipedia.org/wiki/Finite_complement_topology#Cofinite_topology) on Wikipedia.

[[Proof of Topology]]
When know that $U = \emptyset$ is open by definition. Now let $U = X$. This implies $X/U = X/X = \emptyset$. Now let $A$ be a collection of open sets in $X$. Let $U = \bigcup\limits_{i=1}^{\infty}a_i$ where $a_i \in U$ (show that $X/U$ is finite or $\emptyset$). So, $X/U = X /\bigcup\limits_{i=1}^{\infty}a_i = (X/ a_i) \cap (X/a_{i+1}) \cap \dots$. An arbitrary intersection of finite sets is finite. Now let $A$ be a collection of open sets in $X$. Let $U = \bigcap\limits_i^j a_i$ where $a_i \in A$. So, $X/U = X/\bigcap\limits_i^j a_i = (X/a_i) \cup (X/a_{i+1}) \cup \dots \cup (X/a_j)$. A finite union of finite sets is finite.

