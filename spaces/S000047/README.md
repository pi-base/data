---
uid: S000047
name: Countable sum of Sierpinski spaces
aliases:
  - Hjalmar Ekdal topology
counterexamples_id: 55
refs:
  - doi: 10.1007/978-1-4612-6290-9 
    name: Counterexamples in Topology
---
Let $X$ be the set of positive integers and define a topology by declaring $U \subseteq X$ to be open if for every odd $p \in U$, $p+1 \in U$. Equivalently, $A \subseteq X$ is closed iff for every even $p \in A$, $p-1 \in A$.

This space is a topological sum of countably-many copies of the {S10}.

Defined as counterexample #55 ("Hjalmar Ekdal Topology")
in {{doi:10.1007/978-1-4612-6290-9}}.

A piece of trivia: the origin of the name Hjalmar Ekdal is explained [here](https://proofwiki.org/wiki/Mathematician:Hjalmar_Ekdal).


<!-- [[Proof of Topology]]
1. Note that $X$ contains all positive integers thus every integer $p$ is in $X$ thus $X$ is open. See that $\emptyset$ contains no integers therefore $\emptyset$ satisfies the condition vacuously therefore it is open.

2. Let $\left\{U_i | i \in I \right\}$ be an arbitrary collection of open sets. Consider any odd $p \in \bigcup\limits_{i \in I} U_i$ since every $U_i$ is open this means $p+1$ is also in the union therefore the union is open.

3. Given any intersection $\bigcap\limits_{n=1}^N U_n$ with $U_n$ an open set and $N \in \mathbb{N}$. Given an odd $p \in \bigcap\limits_{n=1}^N U_n$ then $p \in U_n$ for all $n \leq N$. Thus by definition of open $p+1$ also exists in $U_n$ for all $n \leq N$ therefore $p+1 \in \bigcap\limits_{n=1}^N U_n$ thus $\bigcap\limits_{n=1}^N U_n$ is open. -->
