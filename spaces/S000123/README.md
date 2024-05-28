---
uid: S000123
name: Roy's lattice space
counterexamples_id: 126
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
---
Let $\{C_i\ |\ i \in \omega\}$ be a collection of disjoint dense subsets of $\mathbb{Q}$. For specificity, let \(p(i)\) be the \((i+1)\)th prime,
and let \(C_i\) be the rational numbers of the form $\frac{a}{p(i)^n}$, with $a$ an integer not divisible by $p(i)$.

Let $X = \{(r,i) \in \mathbb{Q} \times \omega\ |\ r \in C_i\} \cup \{\omega\}$ as a set and define a topology on $X$ as follows: neighborhoods of points of the form $(r,2n)$ are open intervals $U_\epsilon(r,2n) = \{(t,2n)\ |\ |r-t|<\epsilon\}$; neighborhoods of points of the form $(r,2n-1)$ have the form $V_\epsilon(r,2n-1) = \{(t,m)\ |\ |r-t|<\epsilon, |m-n|\leq 1\}$; neighborhoods of $\omega$ have the form $W_n(\omega) = \{(s,i)\ |\ i \geq 2n\}$.

Defined as counterexample #126 ("Roy's Lattice Space")
in {{doi:10.1007/978-1-4612-6290-9}}.
