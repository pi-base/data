---
uid: S000171
name: Brian's Example
refs:
  - mo: 416331
    name: Example of an uncountable scattered space with some properties
  - wikipedia: Bernstein_set
    name: Bernstein set on Wikipedia
---

Let $X = \mathbb{R}$ and let $(X_i)_{i\in \omega}$ be a partition of $X$ into [Bernstein sets](https://en.wikipedia.org/wiki/Bernstein_set) (for the Euclidean topology).
Given some $x \in X$, there is a unique $n \in \omega$ such that $x \in X_n$. Then $\{x\} \cup (U \cap \bigcup_{i<n}X_i)$, with $U \subseteq X$ with $U$ open in the usual topology, form a neighbourhood basis for $x$.

This topology in finer than {S25}.

This space was constructed in {{mo:416331}} by Will Brian, providing an example in ZFC for an uncountable, Hausdorff,
first-countable, scattered, Lindelöf space.
