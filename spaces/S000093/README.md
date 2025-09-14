---
uid: S000093
name: Double arrow space
aliases:
  - Split interval
  - Weak parallel line topology
counterexamples_id: 95
refs:
  - zb: "0386.54001"
    name: Counterexamples in Topology
  - zb: "0684.54001"
    name: General Topology (Engelking, 1989)
  - wikipedia: Split_interval
    name: Split interval on Wikipedia
---

The set $X=([0,1]\times\{0,1\})\setminus
\{\langle 0,0\rangle,\langle 1,1\rangle \}$ with the order topology given by the lexicographic order.
$$\langle x,t\rangle < \langle x',t'\rangle
\iff x<x' \text{ or } (x=x' \text{ and } t<t')$$

Defined as counterexample #95 ("Weak Parallel Line Topology")
in {{zb:0386.54001}}. Base open sets $W$ and $U$ mentioned therein are the open intervals
$(\langle a,0\rangle, \langle b,1\rangle)$ and
$(\langle a,1\rangle, \langle b,0\rangle)$ respectively
(with $0\leq a<b\leq 1$).

Referenced in Exercise 3.10.C of {{zb:0684.54001}}.
