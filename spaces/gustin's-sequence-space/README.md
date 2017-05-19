---
uid: S000122
slug: gustin's-sequence-space
name: Gustin's Sequence Space
---
Let $\mathbb{Z}^+$ denote the set of positive integers, $Y = (\mathbb{Z}^+)^{<\omega}$ be the set of all finite sequences of positive integers, $W = \{A \subset Y\ |\ |A| = 2\}$. Gustin's Sequence Space is the set $X = Y \cup (\mathbb{Z}^+ \times W)$ with topology defined as follows:

For any $\alpha, \beta \in Y$, let $\alpha \cap \beta$ be the sequence formed by adjoining $\beta$ to the end of $\alpha$. Let $\alpha \geq i \in \mathbb{Z}$ abbreviate $a \geq i$ for every $a \in \alpha$. Let $\beta \supset_i \alpha$ abbreviate $\exists \gamma \geq i$ with $\beta = \alpha\gamma$ and $U_i(\alpha) = \{\beta \in Y\ |\ \beta \supset_i \alpha\}$.

Fix a bijection $p$ from $W$ to the set of all positive primes. Define $q: \mathbb{Z}^+ \times W \rightarrow \mathbb{Z}^+$ by $q(n,w) = [p(w)]^n$.

Define a topology on $X$ by letting neighborhoods of points $\alpha \in Y$ be sets of the form $U_i(\alpha)$, and neighborhoods of points $(n,w) = (n, \{\alpha, \beta\})$ be sets of the form $V_i(n,w) = \{(n,w)\} \cup U_i\big(\alpha q(n,w)\big) \cup U_i\big(\beta q(n,w)\big) $

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 142-143.

