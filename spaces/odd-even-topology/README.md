---
uid: S000005
slug: odd-even-topology
name: Odd-Even Topology
---
Define a topology on $\mathbb{N}$ by taking as a basis all sets of the form $\{\{2k-1,2k\}\, |\, k \in \mathbb{N}\}$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 43-44.
* [Partition topology](http://en.wikipedia.org/wiki/Partition_topology) on Wikipedia.

[[Proof of Topology]]
Let $X=\{\{2k-1, 2k\} | k \in \mathbb{N}\}$. Also, let $\tau = \{$Collection of all subsets, $B$, of $X\}$. Finally, let $\mathcal{B} = \{$collection of all $B\}$ Now, for any $k \in \mathbb{N}$, $\{2k-1, 2k\} \in X$. Since $B \subseteq X$, we know that for any $\{2k-1, 2k\}$ chosen, it is in an arbitrary $B$, that it is in at least one $B$. Without loss of generality, let $\{2k-1, 2k\}$ be in $B_1$ and $B_2$. Let $B_1 \cap B_2 = \{2k-1, 2k\}$. Again, without the loss of generality, let there be a $B_3$ such that $\{2k-1, 2k\} \in B_3$. This means that $B_3 \subset B_1 \cap B_2$, which is vacuously true.

