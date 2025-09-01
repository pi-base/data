---
uid: S000213
name: Pseudocircle
refs:
  - wikipedia: Pseudocircle
    name: Pseudocircle on Wikipedia
---

Let $X$ be the *complete bipartite poset* $K_{2,2}$, with two incomparable elements in the bottom layer, two incomparable elements in the top layer, and every bottom element less than every top element.

Specifically, take $X=\{0,1,2,3\}$ with bottom elements $0,2$ and top elements $1,3$.
(The ordered pairs $(a,b)$ with $a<b$ are $(0,1),(0,3),(2,1),(2,3)$.)

The topology on $X$ is the {P90} topology where the open sets are the upper sets of the poset:
$\varnothing, \{1\}, \{3\}, \{1,3\}, \{0,1,3\}, \{2,1,3\}, X$.

---
This space can also be viewed as the *non-Hausdorff suspension* of $S^0$ ({S1}).
See Definition 3.4.2 in
[Finite Spaces and Larger Contexts (J. P. May & E. Pishevar)](https://math.uchicago.edu/~may/REU2024/FiniteSpaces24.pdf).
