---
uid: S000020
slug: countable-fort-space
name: Countable Fort Space
---
Fix a point $p \in X$ and define $U \subset X$ open if and only if $X \setminus U$ is finite or $p \notin U$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 52-53.
* [Fort space](http://en.wikipedia.org/wiki/Fort_space) on Wikipedia.

[[Proof of Topology]]
Let $\tau$ be the collection of all open sets $U \subset X$. Then $X$ is an element of $\tau$ since $X \setminus X = \emptyset$. Also, the empty set is an element of $\tau$ since $p \notin \emptyset$.

Let $\mathcal{A}$ be a subcollection of elements from $\tau$.
Two cases arise.

The first case is that no $A \in \mathcal{A}$ contains $p$. Thus,
$
\bigcup\limits_{A \in \mathcal{A}} A \in \tau.
$
The second case is that $p$ is in at least one element of $\mathcal{A}$. Without loss of generality, let $p \in A_1$. Now denote $U = \cup_{A \in \mathcal{A}} A$.
Thus, $A_1 \subset U$.
Now we are able to remove $A_1$ and $U$ from $X$ to receive,
$
X \setminus U \subset X \setminus A_1.
$
Since, $p \notin A_1$, but $A_1$ is still open, $A_1$ must be finite. Thus, $X \setminus A_1$ is finite and so is $X \setminus U$. Therefore, $U \in \tau$.

Again, let $\mathcal{A}$ be a subcollection of elements from $\tau$.
Two cases arise.
The first case is that $p \notin A$ for some $A \in \mathcal{A}$. Thus,
$
p \notin \bigcap\limits_{A \in \mathcal{A}} A \in \tau.
$

The second case is that $p$ is in every $A \in \mathcal{A}$.
Notice, $X \setminus A_i$ is finite for all $i$. Thus,
$
\bigcup\limits_{i = 1}^n X \setminus A_i
$
is finite.

Now by DeMorgan's Laws we find
$
\bigcup\limits_{i = 1}^n X \setminus A_i = X \setminus \bigcap\limits_{i = 1}^n A_i \in \tau.
$

