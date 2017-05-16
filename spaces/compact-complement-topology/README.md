---
uid: S000019
slug: compact-complement-topology
name: Compact Complement Topology for the Euclidean Real Numbers
aliases:
  - Compact Complement Topology
counterexamples_id: 22
refs:
  - doi: 10.1007\/978-1-4612-6290-9_6
    name: Counterexamples in Topology
  - wikipedia: Compact_complement_topology
    name: Compact complement topology
---
Define a topology $\tau$ on $\mathbb{R}$ by letting $U \subset \mathbb{R}$ be open if and only if $\mathbb{R} \setminus U$ is compact in the usual Euclidean topology.

Note that this topology is coarser than the Euclidean topology on $\mathbb{R}$.

Considered as #22 ("Compact Complement Topology")
in {{doi:10.1007\/978-1-4612-6290-9_6}}.

<!-- [[Proof of Topology]]
1) $U = \emptyset$ is open by definition. Now, allow $U = \mathbb{R}$. This implies $\mathbb{R} / \mathbb{R} = \emptyset$.

2) Let $A= \bigcup\limits^\infty_{i=1} U_i$ where $U_i \in \tau$. Note, $\mathbb{R} / A$ is bounded and closed. $\mathbb{R} / (\bigcup\limits^\infty_{i=1} U_i) = \bigcap\limits^\infty_{i=1} \mathbb{R}/U_i$. Since the compact sets are precisely the closed sets in this space, an arbitrary intersection of compact sets is compact, so each of these is compact by definition.

3) Let $A=\bigcap\limits_{i=1}^nU_i$ where $U_i \in \tau$. Note, $\mathbb{R} / A$ is bounded and closed. $\mathbb{R} / (\bigcap\limits^n_{i=1} U_i) = \bigcup\limits^\infty_{i=1} \mathbb{R}/U_i$. Each of these sets already has their limit points within them (closed). A finite union of compact sets is compact. -->
