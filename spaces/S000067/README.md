---
uid: S000067
name: Irrational slope topology
counterexamples_id: 75
refs:
  - doi: 10.1007/978-1-4612-6290-9 
    name: Counterexamples in Topology
  - zb: 0051.13902
    name: A connected countable Hausdorff space (R.H. Bing)
---

Let $X = \{(x,y) : x,y \in \mathbb{Q}, y \geq 0\}$. For a fixed irrational $\theta>0$, the irrational slope topology on $X$ is obtained by taking as a local base of open neighborhoods of each point $(x,y)\in X$ the collection of sets $N_\epsilon(x,y)$ with $\epsilon>0$,
defined by $N_\epsilon(x,y) = \{(x,y)\} \cup B(x - y/\theta, \epsilon) \cup B(x + y/\theta, \epsilon)$ where $B(a, \epsilon):=((a-\epsilon,a+\epsilon)\cap\mathbb Q)\times\{0\}$.  That is, $N_\epsilon(x,y)$ consists of the point $(x,y)$ together with the rational numbers in an $\epsilon$-neighborhood around the two points where the lines passing through $(x,y)$ with slopes $\theta$ and $-\theta$ cross the real $x$-axis.

Defined as counterexample #75 ("Irrational Slope Topology")
in {{doi:10.1007/978-1-4612-6290-9}}. Originally introduced in {{zb:0051.13902}} with $\theta=\sqrt 3$.
