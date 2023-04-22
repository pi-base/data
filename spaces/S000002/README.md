---
uid: S000002
name: Discrete Topology on a Countably Infinite Set
aliases:
  - Countable Discrete Topology
  - Sierpinski's metric space
counterexamples_id: 2
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
  - wikipedia: Discrete_space
    name: Discrete Space on Wikipedia
---
Let $X=\omega=\{0,1,2,\dots\}$ be the space containing countably-many
points and let all subsets of $X$ be open.

Defined as counterexample #2 ("Countable Discrete Topology")
in {{doi:10.1007/978-1-4612-6290-9}}.

This space is metrizable, with the standard metric for a discrete space given by $d(x,y)=1$ for $x\ne y$.  A different metric that generates the same topology for $X$ is the Sierpinski metric ($d(x,y)=1+1/(x+y+2)$ for $x\ne y$ in $\omega$) given in counterexample #135 in {{doi:10.1007/978-1-4612-6290-9}}.  Since pi-base is meant to model topological properties and not properties of metrics, it only keeps track of topological spaces up to homeomorphism, and thus does not keep a separate entry for the Sierpinski metric.

<!-- [[Proof of Topology]]
1) $U=\emptyset$ is open by definition. Let $U = X$ is open by definition.

2) Let $A$ be an arbitrary union of the elements of any subcollection of $\tau$. Since every element in the subcollection are subsets of $X$ their union must be a subset of $X$. Thus, $A$ is a subset of $X$ and is open by definition.

3) Let $A$ be a finite intersection of elements from any subcollection of $\tau$. Since every element in the subcollection are subsets of $X$ their intersection must necessarily be a subset of $X$. Thus, $A$ is a subset of $X$ and is open by definition. -->
