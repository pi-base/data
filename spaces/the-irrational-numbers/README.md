---
uid: S000028
slug: the-irrational-numbers
name: The Irrational Numbers
---
Let $X$ be the complement of the rational numbers in $\mathbb{R}$ with the subspace topology.

Equivalently, $X \cong \omega^\omega$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 59-60.
* [Irrational number](http://en.wikipedia.org/wiki/Irrational_number) on Wikipedia.

[[Proof of Topology]]
In order to confirm the topology on the irrational numbers we simply must verify it is a subspace.  Let $\mathbb{I}$ be the set of irrational numbers.  Let $\tau$ denote the topology on $\mathbb{R}$.  
Observe both $\emptyset$ and $\mathbb{I}$ belong to $\tau_\mathbb{I}$ since
$$\emptyset = \mathbb{I} \cap \emptyset$$  
$$\mathbb{I} = \mathbb{I} \cap \mathbb{R},$$
noting that both $\emptyset$ and $\mathbb{I}$ belong to $\tau$.
Taking the arbitrary union of any elements of $\tau_\mathbb{I}$ we note
$$ \bigcup_{i \in I} (\mathbb{I} \cap U_i) = \mathbb{I} \cap \bigcup_{i \in I} U_i $$
which is in $\tau_\mathbb{I}$ since $\bigcup_{i \in I} U_i \in \tau$.   
Taking the intersection of finitely-many elements of $\tau_\mathbb{I}$, we note 
$$ \bigcap_{i = 1}^n (\mathbb{I} \cap U_i) = \mathbb{I} \cap \bigcap_{i = 1}^n U_i $$
which is in $\tau_\mathbb{I}$ since $\bigcap_{i=1}^n U_i \in \tau$.

