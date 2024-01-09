---
uid: S000133
name: Space of Singletons and Standardly Open Sets Containing the Origin in $\mathbb{R}^n$
counterexamples_id: 139
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
---

Fix any $n$ and take $\mathbb{R}^n$ as our set of points. Take as the basic
open sets all singletons except for $\{0\}$ and all standard neighborhoods of
$0$.

For example, $\mathbb{Q} \setminus \{0\}$ is open, and so is $(-1, 1)$, but $\{0\}$ is not
open.

This construction is equivalent to the post office metric space defined below. For proof, see
[this post on the Math Stack Exchange](https://math.stackexchange.com/a/4834226).

If $d$ is the usual metric on $\mathbb{R}^2$, the post office metric $p$ is defined by:

$r(x,y) = \begin{cases}
    0 & x=y \\
    d(x,(0,0)) + d(y,(0,0)) & \text{otherwise}
\end{cases}$

Defined as counterexample #139 ("The Post Office Metric")
in {{doi:10.1007/978-1-4612-6290-9}}.
