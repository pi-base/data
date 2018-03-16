---
uid: I000110
if:
  and:
  - t_4: true
  - pseudocompact: true
then:
  weakly-countably-compact: true
refs:
- doi: 10.1007/978-1-4612-6290-9
  name: Counterexamples in Topology
---
Suppose $X$ is a $T_4$ space which is not weakly countably compact. Then there is some sequence $x_n$ in $X$ with no limit point. Define $f:x_n \mapsto n$. By the Tietze Extension Theorem, $f$ extends to a continuous unbounded $F: X \rightarrow \mathbb{R}$, so $X$ is not pseudocompact.

Shown on page 20 of {{doi:10.1007/978-1-4612-6290-9}}.
