---
uid: S000019
slug: compact-complement-topology
name: Compact Complement Topology
---
Define a topology $\tau$ on $\mathbb{R}$ by letting $U \subset \mathbb{R}$ be open if and only if $\mathbb{R} \setminus U$ is compact in the usual Euclidean topology.

Note that this topology is coarser than the standard topology on $\mathbb{R}$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 51-52.
* [Compact complement topology](http://en.wikipedia.org/wiki/Compact_complement_topology) on Wikipedia.

[[Proof of Topology]]
1) $U = \emptyset$ is open by definition. Now, allow $U = \mathbb{R}$. This implies $\mathbb{R} / \mathbb{R} = \emptyset$. 

2) Let $A= \bigcup\limits^\infty_{i=1} U_i$ where $U_i \in \tau$. Note, $\mathbb{R} / A$ is bounded and closed. $\mathbb{R} / (\bigcup\limits^\infty_{i=1} U_i) = \bigcap\limits^\infty_{i=1} \mathbb{R}/U_i$. Since the compact sets are precisely the closed sets in this space, an arbitrary intersection of compact sets is compact, so each of these is compact by definition.

3) Let $A=\bigcap\limits_{i=1}^nU_i$ where $U_i \in \tau$. Note, $\mathbb{R} / A$ is bounded and closed. $\mathbb{R} / (\bigcap\limits^n_{i=1} U_i) = \bigcup\limits^\infty_{i=1} \mathbb{R}/U_i$. Each of these sets already has their limit points within them (closed). A finite union of compact sets is compact.

