---
uid: S000017
name: Cocountable topology on $\mathbb R$
aliases:
  - Cocountable topology on the real numbers
  - Countable complement space
counterexamples_id: 20
refs:
  - doi: 10.1007/978-1-4612-6290-9 
    name: Counterexamples in Topology
  - wikipedia: Cocountable_topology
    name: Cocountable topology on Wikipedia
---

Let $X=\mathbb R$ be the set of real numbers.  Define topology on $X$ by letting a subset $U \subset X$ be open iff its complement is countable or $U = \emptyset$. 

Defined as counterexample #20 ("Countable Complement Topology")
in {{doi:10.1007/978-1-4612-6290-9}}.

<!-- [[Proof of Topology]]
Let $\tau = \{$Any countable set$\}$. And let $X$ be an uncountable space.
Frist we know that $X^c = \emptyset$, which is countable. Also $\emptyset ^c = X$, which is explicitly allowed, showing that both $X$ and $\emptyset$ are in $\tau$.
Now let $\{ U_i | i \in \textbf{I}\}$ be a sub collection of $X$. (Show $\bigcup\limits_{i \in \textbf{I}} U_i \in X$) We know ($\bigcup\limits_{i \in \textbf{I}} U_i \in X$)$^c$ is countable. So ($\bigcup\limits_{i \in \textbf{I}} U_i$)$^c$ $=\bigcap\limits_{i \in \textbf{I}} U_i ^c$, by the DeMorgan's Law. We know that $\bigcap\limits_{i \in \textbf{I}} U_i ^c$ $\subseteq U_j^c$ for any $j \in \textbf{I}$, which is countable. Now let $\mathcal{A} = \{U_i | i \in [n]\}$ be a sub collection of open sets in $X$. Let $\bigcap\limits_{i=1}^n U_i$, where $U_i \in \mathcal{A}$. We know that ($\bigcap\limits_{i=1}^n U_i$)$^c$$=\bigcup\limits_{i=1}^n U_i^c$ by DeMorgan's Law. Since a countable union of countable sets is countable, it is countable. -->
