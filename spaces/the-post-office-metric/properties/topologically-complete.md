---
uid: T001033
space: the-post-office-metric
property: topologically-complete
value: true
refs:
  - doi: 10.1007/978-1-4612-6290-9_6
    name: Counterexamples in Topology
---
Suppose that $\langle x_n \rangle$ is a Cauchy sequence that does not converge to $(0,0)$.  Then there is $\varepsilon>0$ and a subsequence $x_{n_i}$ such that $d(x_{n_i},(0,0))\ge \varepsilon$.  Let $N$ be an index such that $d(x_n,x_m)<\varepsilon$ for all $n,m\ge N$.  Let $n_i$ be the first element of the subsequence with $n_i\ge N$ and let $n\ge N$ be arbitrary. We have $d(x_n,(0,0))+d(x_{n_i},(0,0))\ge \varepsilon$, and therefore we must conclude that $x_{n}=x_{n_i}$, hence $\langle x_n \rangle$ is eventually constant and therefore convergent.

Asserted in the General Reference Chart for space #139 in
{{doi:10.1007/978-1-4612-6290-9_6}}.
