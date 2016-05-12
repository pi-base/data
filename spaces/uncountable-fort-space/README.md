---
uid: S000021
slug: uncountable-fort-space
name: Uncountable Fort Space
---
Fix a point $p$ in an uncountable set $X$ and define $U \subset X$ open if and only if $X \setminus U$ is finite or $p \notin U$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 52-53.
* [Fort space](http://en.wikipedia.org/wiki/Fort_space) on Wikipedia.

[[Proof of Topology]]
Let $\tau$ be the collection of all open sets $U \subset X$.

Since $X \setminus X =$ 0, which is finite, $X \in \tau$. Also since we know that $p \notin \emptyset$, thus $\emptyset \in \tau$. Showing that the first axiom of a topological space is met.\\

Now, let $\mathcal{A}$ be a subcollection of $\tau$, two cases arise. In the first case, we have no $A \in \mathcal{A}$ have a $p$. Thus, $p \notin \bigcup\limits_{A \in \mathcal{A}} A \in \tau.$ In the second case we have $p$ is in at least one $A$. Without loss of generality, let $p \in A_1$. So, $U = \bigcup\limits_{A \in \mathcal{A}} A$. Then, $X \setminus U \subset X \setminus A_1$. Since $p \in A_1$ and $A_1$ is infinite, then $X \setminus A_1$ is finite, thus $U \in \tau$. This shows that the second axiom of a topological space is met.\\

Finally, let $\mathcal{A}$ be a subcollection, two cases arise. In the first case some $A \in \mathcal{A}$ does not have $p$ in it. Then, $p \notin \bigcap\limits_{A \in \mathcal{A}} A$. Thus $p \notin U$, $\in \tau$. In the second case $p \in A$ for all $A \in \mathcal{A}$. We know that $X \setminus A$ is finite for all $A \in \mathcal{A}$. So, $p \in (\,\bigcap\limits_{A \in \mathcal{A}} A$)\, Now consider (\,$\bigcap\limits_{A \in \mathcal{A}} A)\,^c = \bigcup\limits_{A \in \mathcal{A}} A^c$, by DeMorgan's. Thus, it is finite, because a union of a finite set is finite. Showing that the third axiom of a topological space is met.

