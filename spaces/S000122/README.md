---
uid: S000122
name: Gustin's sequence space
counterexamples_id: 125
refs:
- doi: 10.1007/978-1-4612-6290-9
  name: Counterexamples in Topology
---
Let $\mathbb{Z}^+$ denote the set of positive integers, $Y$ be the set of all finite sequences of positive integers of even length, and $W = \{A \subseteq Y\ |\ |A| = 2\}$. Gustin's Sequence Space is the set $X = Y \cup (\mathbb{Z}^+ \times W)$ with topology defined as follows:

For any finite sequences $\alpha, \beta$ of arbitrary length, let $\alpha\beta$ be the sequence formed by adjoining $\beta$ to the end of $\alpha$. Let $\alpha \geq i \in \mathbb{Z}$ abbreviate $a \geq i$ for every $a \in \alpha$. Let $\beta \supseteq_i \alpha$ abbreviate that there exists a sequence of finite length $\gamma\geq i$ with $\beta = \alpha\gamma$ and $U_i(\alpha) = \{\beta \in Y\ |\ \beta \supseteq_i \alpha\}$.

Let $q: \mathbb{Z}^+ \times W\rightarrow \mathbb{Z}^+$ be a function increasing on its first coordinate. (For example, fix a bijection $p$ from $W$ to the set of all positive primes, and define $q: \mathbb{Z}^+ \times W \rightarrow \mathbb{Z}^+$ by $q(n,w) = [p(w)]^n$.)

Define a topology on $X$ by letting neighborhoods of points $\alpha \in Y$ be sets of the form $U_i(\alpha)$, and neighborhoods of points $(n,w) = (n, \{\alpha, \beta\})$ be sets of the form $V_i(n,w) = \{(n,w)\} \cup U_i\big(\alpha q(n,w)\big) \cup U_i\big(\beta q(n,w)\big) $.

Defined as counterexample #125 ("Gustin's Sequence Space")
in {{doi:10.1007/978-1-4612-6290-9}}.
