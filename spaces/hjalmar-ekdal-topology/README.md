---
uid: S000047
slug: hjalmar-ekdal-topology
name: Hjalmar Ekdal Topology
counterexamples_id: 55
refs:
  - doi: 10.1007/978-1-4612-6290-9 
    name: Counterexamples in Topology
  - wikipedia: Hjalmar_Ekdal_topology
    name: Hjalmar Ekdal topology on Wikipedia
---
Let $X$ be the set of all positive integers and define a topology on a by declaring $U \subset X$ to be open if for every odd $p \in U$, $p+1 \in U$. Equivalently, note that $A \subset X$ is closed if for every $p \in A$, $p-1 \in A$.

This space is a topological sum of countably-many copies of the Sierpinski
space.

Defined as counterexample #55 ("Hjalmar Ekdal Topology")
in {{doi:10.1007/978-1-4612-6290-9}}.



<!-- [[Proof of Topology]]
1. Note that $X$ contains all positive integers thus every integer $p$ is in $X$ thus $X$ is open. See that $\emptyset$ contains no integers therefore $\emptyset$ satisfies the condition vacuously therefore it is open.

2. Let $\left\{U_i | i \in I \right\}$ be an arbitrary collection of open sets. Consider any odd $p \in \bigcup\limits_{i \in I} U_i$ since every $U_i$ is open this means $p+1$ is also in the union therefore the union is open.

3. Given any intersection $\bigcap\limits_{n=1}^N U_n$ with $U_n$ an open set and $N \in \mathbb{N}$. Given an odd $p \in \bigcap\limits_{n=1}^N U_n$ then $p \in U_n$ for all $n \leq N$. Thus by definition of open $p+1$ also exists in $U_n$ for all $n \leq N$ therefore $p+1 \in \bigcap\limits_{n=1}^N U_n$ thus $\bigcap\limits_{n=1}^N U_n$ is open. -->
