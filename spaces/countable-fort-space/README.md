---
uid: S000020
slug: countable-fort-space
name: Countable Fort Space
---
Fix a point $p$ in a set $X$ and define $U \subset X$ to open provided $X \setminus U$ is finite or $p \notin U$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 52-53.
* [Fort space](http://en.wikipedia.org/wiki/Fort_space) on Wikipedia.

[[Proof of Topology]]
Let $\tau$ be the collection of all open sets $U \subset X$. Then $X$ is an element of $\tau$ since $X \setminus X = \emptyset$. Also, the empty set is an element of $\tau$ since $p \notin \emptyset$.

Let $\mathcal{A}$ be a subcollection of elements from $\tau$. Two cases arise.

The first case is that no $A \in \mathcal{A}$ contains $p$. Thus, $\bigcup\limits_{A \in \mathcal{A}} A \in \tau.$

The second case is that $p$ is in at least one element of $\mathcal{A}$. Without loss of generality, let $p \in A_1$. Denote $U = \cup_{A \in \mathcal{A}} A$.
Now, $X \setminus U \subset X \setminus A_1.$
Since, $p \in A_1$ but $A_1$ is still open, it must be that $X \setminus A_1$ is finite. Therefore, $X \setminus U$ is finite, so $U \in \tau$.

