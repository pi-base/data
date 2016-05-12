---
uid: S000017
slug: countable-complement-topology
name: Countable Complement Topology
---
Let $X$ be an uncountable space.  Define the open sets on $X$ by a letting a set $U \subset X$ be open iff its complement is is countable.  Taking the collection of all such sets, $U$, together with both the $\emptyset$ and $X$ yields a topology on $X$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 50-51.
* [Cocountable topology](http://en.wikipedia.org/wiki/Countable_complement_topology) on Wikipedia.

[[Proof of Topology]]
Let $\tau = \{$Any countable set$\}$. And let $X$ be an uncountable space.\\
Frist we know that $X^c = \emptyset$, which is countable. Also $\emptyset ^c = X$, which is explicitly allowed, showing that both $X$ and $\emptyset$ are in $\tau$.
Now let $\{ U_i | i \in \textbf{I}\}$ be a sub collection of $X$. (Show $\bigcup\limits_{i \in \textbf{I}} U_i \in X$) We know ($\bigcup\limits_{i \in \textbf{I}} U_i \in X$)$^c$ is countable. So ($\bigcup\limits_{i \in \textbf{I}} U_i$)$^c$ $=\bigcap\limits_{i \in \textbf{I}} U_i ^c$, by the DeMorgan's Law. We know that $\bigcap\limits_{i \in \textbf{I}} U_i ^c$ $\subseteq U_j^c$ for any $j \in \textbf{I}$, which is countable. Now let $\mathcal{A} = \{U_i | i \in [n]\}$ be a sub collection of open sets in $X$. Let $\bigcap\limits_{i=1}^n U_i$, where $U_i \in \mathcal{A}$. We know that ($\bigcap\limits_{i=1}^n U_i$)$^c$$=\bigcup\limits_{i=1}^n U_i^c$ by DeMorgan's Law. Since a countable union of countable sets is countable, it is countable.

