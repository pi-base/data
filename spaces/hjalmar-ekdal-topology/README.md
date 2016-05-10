---
uid: S000047
slug: hjalmar-ekdal-topology
name: Hjalmar Ekdal Topology
---
Let $X$ be the set of all positive integers and define a topology on a by declaring $U \subset X$ to be open if for every odd $p \in U$, $p+1 \in U$. Equivalently, note that $A \subset X$ is closed if for every $p \in A$, $p-1 \in A$.

Note that $X$ is a countable topological sum of the [Sierpinski space](http://www.jdabbs.com/brubeck/spaces/sierpinski-space/).

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 78-79.
* [Hjalmar Ekdal topology](http://en.wikipedia.org/wiki/Hjalmar_Ekdal_topology) on Wikipedia.

[[Proof of Topology]]
1. Note that $X$ contains all positive integers thus every integer $p$ is in $X$ thus $X$ is open. See that $\emptyset$ contains no integers therefore $\emptyset$ satisfies the condition vacuously therefore it is open.

2. Let $\left\{U_i | i \in I \right\}$ be an arbitrary collection of open sets. Consider any odd $p \in \bigcup\limits_{i \in I} U_i$ since every $U_i$ is open this means $p+1$ is also in the union therefore the union is open.

3. Given any intersection $\bigcap\limits_{n=1}^N U_n$ with $U_n$ an open set and $N \in \mathbb{N}$. Given an odd $p \in \bigcap\limits_{n=1}^N U_n$ then $p \in U_n$ for all $n \leq N$. Thus by definition of open $p+1$ also exists in $U_n$ for all $n \leq N$ therefore $p+1 \in \bigcap\limits_{n=1}^N U_n$ thus $\bigcap\limits_{n=1}^N U_n$ is open.

