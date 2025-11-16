---
uid: S000052
name: Relatively prime integer topology
counterexamples_id: 60
aliases:
- Golomb Topology
refs:
  - zb: "0386.54001" 
    name: Counterexamples in Topology
  - wikipedia: Arithmetic_progression_topologies
    name: Arithmetic progression topologies on Wikipedia
  - mathse: 4460847
    name: The Kirch topology is the same as the prime integer topology
---
Let $X=\mathbb{Z}^+$, the set of positive integers.  For $a,b \in X$, let $U_a(b) = \{b+na \in X : n \in \mathbb{Z}\} = (b+a\mathbb{Z})\cap X$.  Then $\{U_a(b) : a,b \in X, \gcd\!(a,b)=1\}$ forms a basis for the relatively prime integer topology on $X$.

Alternatively, a basis is given by $\{U'_a(b) : a,b \in X, \gcd\!(a,b)=1\}$ with $U'_a(b) = \{b+na \in X : n\ge 0\}$.
See {{mathse:4460847}} for a proof of the equivalence.

Defined as counterexample #60 ("Relatively Prime Integer Topology")
in {{zb:0386.54001}}.
