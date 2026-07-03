---
uid: S000171
name: Brian's stack of Bernstein sets
refs:
  - mo: 416752
    name: Answer to "Example of an uncountable scattered space with some properties"
  - wikipedia: Bernstein_set
    name: Bernstein set on Wikipedia
---

Let $X = \mathbb{R}$ and let $(X_i)_{i\in \omega}$ be a countably infinite partition of $X$ into
[Bernstein sets](https://en.wikipedia.org/wiki/Bernstein_set) (for the Euclidean topology).
Given $x \in X$, let $n \in \omega$ be such that $x \in X_n$.
Then basic open neighbourhoods of $x$ are given by the sets $\{x\} \cup (U \cap \bigcup_{i<n}X_i)$,
with $U$ (basic) open neighbourhood of $x$ in the Euclidean topology.

This topology is finer than {S25}.

This space was constructed in {{mo:416752}} by Will Brian, providing an example in ZFC for an uncountable, Hausdorff,
first-countable, scattered, Lindelöf space.
