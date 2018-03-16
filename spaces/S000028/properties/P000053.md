---
uid: T000658
space: the-irrational-numbers
property: metrizable
value: true
refs:
  - doi: 10.1007/978-1-4612-6290-9_6
    name: Counterexamples in Topology
---
We verify the metric axioms:

$\textbf{M1}:$ $d(x,x)= |x-x|=0$

$\textbf{M2}:$ $d(x,y)+d(y,z) = |x - y| + |y - z| \geq |x - y + y - z| = |x - z| = d(x,z)$.

$\textbf{M3}:$ $d(x,y) = |x - y| = |y - x| = d(y,x)$

$\textbf{M4}:$ Since absolute values can only be positive or zero and $d(x,y)$ could only be zero if $x=y$, we know that when $x \ne y$, then $d(x,y) = |x - y| > 0$.  

We use the metric $d$ to create $\epsilon$-balls around any $x\in \mathbb{I}$ such that $B(x,\epsilon) =\{ y \in \mathbb{I} | d(x,y)<\epsilon \}$ which creates the basis collection $\mathcal{B} = \{ B(x,\epsilon) | \epsilon \in \mathbb{I}\}$.  This basis generates the topology on the irrational numbers, thus $\mathbb{I}$ is metrizable.

Asserted in the General Reference Chart for space #31 in
{{doi:10.1007/978-1-4612-6290-9_6}}.
