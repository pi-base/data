---
uid: S000128
slug: miller's-biconnected-set
name: Miller's biconnected set
counterexamples_id: 131
refs:
- doi: 10.1007/978-1-4612-6290-9
  name: Counterexamples in Topology
ambiguous_construction: true
---
Let $C \subset [0,1]$ be the Cantor set. Let $W = C \times [0,1] \subset \mathbb{R}^2$. Let $K$ be an indecomposable continuum such that $K \cap [0,1]^2 = W$. Let $\Delta$ be a countable dense subset of $K$ (which exists, as $K$ is compact and metrizable). Let $\mathcal{C}$ be the set of composants of $K$, $\mathcal{B}$ the set of continua which separate  $K$ and $\mathcal{D}$ the set of subsets of $\Delta$ which are dense in some square $S \subset [0,1]^2$ which meets $W$ and has edges parallel to the $x$- and $y$- axes. Choose well orderings $\{C_\alpha\}$, $\{B_\alpha\}$ and $\{D_\alpha\}$ of $\mathcal{C}$, $\mathcal{B}$ and  $\mathcal{D}$ respectively for $\alpha < \kappa$ where $\kappa$ is the least ordinal with $|\kappa| = \mathfrak{c}$.

Inductively define for each $\alpha$ an $M_\alpha \subset K$ and simple closed curve $J_\alpha$ such that:

1. $M_\alpha = p_\alpha \in B_\alpha \cap K$ if $B_\alpha \cap \Delta = \emptyset$
2. $M_\alpha = \emptyset$ if $B_\alpha \cap \Delta \neq \emptyset$
3. For ordinals $\mu \neq \lambda$ with $M_\mu, M_\lambda \neq \emptyset$, $M_\mu$ and $M_\lambda$ are in different composants of $K$
4. $J_\alpha$ separates $K$
5. $J_\alpha \cap \Delta \setminus D_\alpha = J_\alpha \cap M = \emptyset$ where $M = \bigcup_{\alpha < \kappa} M_\alpha$

Let $X = \Delta \cup M \subset \mathbb{R}^2$ with the subspace topology.   

Defined as counterexample #131 ("Miller's Biconnected Set")
in {{doi:10.1007/978-1-4612-6290-9}}.
