---
uid: S000125
name: Knaster-Kuratowski fan
aliases:
  - Cantor's leaky tent
counterexamples_id: 128
refs:
- zb: "0386.54001"
  name: Counterexamples in Topology
- wikipedia: Knaster-Kuratowski_fan
  name: Knaster-Kuratowski fan
---

$X$ is a subspace of {S176} defined as follows.
For any $a \in [0,1]$, let $L(a)$ be the closed line segment from $(a,0)$ to $p = (\frac{1}{2}, \frac{1}{2})$.
Let $C$ be the middle-thirds Cantor set in the unit interval, $E$ the set of endpoints of the removed intervals and $F = C\setminus E$.
Define $A = \{(x,y) \in L(c):c \in E, y \in \mathbb Q\}$ and $B = \{(x,y) \in L(c):c \in F, y \not\in \mathbb Q\}$.
Then take $X = A \cup B\subseteq\mathbb R^2$ with the subspace topology.

The subspace $X\setminus\{p\}$ obtained by removing the apex point is {S126}.

Defined as counterexample #128 ("Cantor's Leaky Tent")
in {{zb:0386.54001}}.
