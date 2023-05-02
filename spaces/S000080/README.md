---
uid: S000080
name: B. Scott's modified Arens square
refs:
  - mathse: 1716095
    name: Answer to "Is Arens Square a Urysohn space?"
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
---

The authors of {{doi:10.1007/978-1-4612-6290-9}} intended the {S72} space (counterexample #80) to be an example of a space that is {P4} and {P10}, but not {P5} and not {P9}.  It turns out {S72} was erroneously claimed as {P4} in their book.  Brian Scott constructed the modification below in {{mathse:1716095}} to provide an example with the desired properties.

Let $Q$ be the set of rational points in the interval $(0,1)$ and let $\{Q_q:q\in Q\}$ be a partition of $Q$ into countably many dense subsets. Let

$S=\bigcup_{q\in Q}(\{q\}\times Q\_q)$

and take the space to be $X=\{(0,0),(1,0)\}\cup S$.

Let $M=\{1/2\}\times Q_{1/2}$. Points of $S\setminus M$ have the neighborhoods that they inherit from the Euclidean topology.  Local bases at the points $(0,0)$, $(1,0)$ and $(1/2,q)\in M$ are given respectively by the collections of sets
- $U_n(0,0) = \{(0,0)\} \cup \{(x,y)\in S: 0<x<\frac14, \; 0<y<\frac1n\}$,
- $U_n(1,0) = \{(1,0)\} \cup \{(x,y)\in S: \frac34<x<1, \; 0<y<\frac1n\}$,
- $U_n(1/2,q) = \{(x,y)\in S: \frac{1}{4}<x<\frac34, \; q-\frac1n < y < q+\frac1n\}.$

The properties and justifications given for counterexample #80 in {{doi:10.1007/978-1-4612-6290-9}} are valid for this space with minimal modifications.
