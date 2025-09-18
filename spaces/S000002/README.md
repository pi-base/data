---
uid: S000002
name: Discrete topology on $\omega$
aliases:
  - Discrete topology on a countably infinite set
  - Countable discrete topology
  - Sierpinski's metric space
  - Natural numbers $\mathbb N$
  - Integers $\mathbb Z$
counterexamples_id: 2
refs:
  - zb: "0386.54001"
    name: Counterexamples in Topology
  - wikipedia: Discrete_space
    name: Discrete space on Wikipedia
---

Let $X=\omega=\{0,1,2,\dots\}$, a set with a countably infinite
number of points, and let all subsets of $X$ be open.

Defined as counterexample #2 ("Countable Discrete Topology")
in {{zb:0386.54001}}.

This space is metrizable, with the standard metric for a discrete space given by $d(x,y)=1$ for $x\ne y$.  A different metric that generates the same topology for $X$ is the Sierpiński metric ($d(x,y)=1+1/(x+y+2)$ for $x\ne y$ in $\omega$) given in counterexample #135 in {{zb:0386.54001}}.  Since pi-base is meant to model topological properties and not properties of metrics, it only keeps track of topological spaces up to homeomorphism, and thus does not keep a separate entry for the Sierpiński metric.
