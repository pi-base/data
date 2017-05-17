---
uid: S000022
slug: fortissimo-space
name: Fortissimo Space on the Real Numbers
aliases:
  - Fortissimo Space
counterexamples_id: 25
refs:
  - doi: 10.1007/978-1-4612-6290-9 
    name: Counterexamples in Topology
  - wikipedia: Fort_space
    name: Fort space
---

Let \(X=\mathbb{R}\cup\{\infty\}\).
Define $U \subset X$ to open if its complement is countable
or includes \(\infty\).

Defined as counterexample #25 ("Fortissimo Space")
in {{doi:10.1007/978-1-4612-6290-9}}.

<!-- [[Proof of Topology]]
Let $\tau$ be the collection of all open sets $U \subset X$.

Since $X \setminus X =$ 0, which is countable, $X \in \tau$. Also since we know that $p \notin \emptyset$, thus $\emptyset \in \tau$. Showing that the first axiom of a topological space is met.\\

Now, let $\mathcal{A}$ be a subcollection of $\tau$, two cases arise. In the first case, we have no $A \in \mathcal{A}$ have a $p$. Thus, $p \notin \bigcup\limits_{A \in \mathcal{A}} A \in \tau.$ In the second case we have $p$ is in at least one $A$. Without loss of generality, let $p \in A_1$. So, $U = \bigcup\limits_{A \in \mathcal{A}} A$. Then, $X \setminus U \subset X \setminus A_1$. Since $p \in A_1$ and $A_1$ is uncountable, then $X \setminus A_1$ is countable, thus $U \in \tau$. This shows that the second axiom of a topological space is met.\\

Finally, let $\mathcal{A}$ be a subcollection, two cases arise. In the first case some $A \in \mathcal{A}$ does not have $p$ in it. Then, $p \notin \bigcap\limits_{A \in \mathcal{A}} A$. Thus $p \notin U$, $\in \tau$. In the second case $p \in A$ for all $A \in \mathcal{A}$. We know that $X \setminus A$ is finite for all $A \in \mathcal{A}$. So, $p \in (\,\bigcap\limits_{A \in \mathcal{A}} A$)\, Now consider (\,$\bigcap\limits_{A \in \mathcal{A}} A)\,^c = \bigcup\limits_{A \in \mathcal{A}} A^c$, by DeMorgan's. Thus, it is countable, because a union of a countable set is countable. Showing that the third axiom of a topological space is met. -->
