---
uid: S000020
slug: countable-fort-space
name: Fort Space on a Countably Infinite Set
aliases:
  - Countable Fort Space
counterexamples_id: 23
refs:
  - doi: 10.1007\/978-1-4612-6290-9_6
    name: Counterexamples in Topology
  - wikipedia: Fort_space
    name: Fort space
---
Let \(X=\omega\cup\{\infty\}=\{0,1,2\dots\}\cup\{\infty\}\).
Define $U \subset X$ to open if its complement is finite or includes \(\infty\).

Defined as counterexample #23 ("Countable Fort Space")
in {{doi:10.1007\/978-1-4612-6290-9_6}}.

<!-- [[Proof of Topology]]
Let $\tau$ be the collection of all open sets $U \subset X$.

Then $X$ is an element of $\tau$ since $X \setminus X = \emptyset$. Also, the empty set is an element of $\tau$ since $p \notin \emptyset$.

Now, let $\mathcal{A}$ be a subcollection of elements from $\tau$, two cases arise. The first case is that no $A \in \mathcal{A}$ contains $p$. Thus, $\bigcup\limits_{A \in \mathcal{A}} A \in \tau.$ The second case is that $p$ is in at least one element of $\mathcal{A}$. Without loss of generality, let $p \in A_1$. Denote $U = \cup_{A \in \mathcal{A}} A$. Now, $X \setminus U \subset X \setminus A_1.$ Since, $p \in A_1$ but $A_1$ is still open, it must be that $X \setminus A_1$ is finite. Therefore, $X \setminus U$ is finite, so $U \in \tau$.

Finally, let $\mathcal{A}$ be a subcollection, two cases arise. In the first case some $A \in \mathcal{A}$ does not have $p$ in it. Then, $p \notin \bigcap\limits_{A \in \mathcal{A}} A$. Thus $p \notin U$, $\in \tau$. In the second case $p \in A$ for all $A \in \mathcal{A}$. We know that $X \setminus A$ is finite for all $A \in \mathcal{A}$. So, $p \in (\,\bigcap\limits_{A \in \mathcal{A}} A$)\, Now consider (\,$\bigcap\limits_{A \in \mathcal{A}} A)\,^c = \bigcup\limits_{A \in \mathcal{A}} A^c$, by DeMorgan's. Thus, it is countable, because a union of a countable set is countable. Showing that the third axiom of a topological space is met. -->
