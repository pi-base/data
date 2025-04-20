---
uid: S000132
name: Duncan's space
counterexamples_id: 136
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
  - zb: "0085.03002"
    name: A topology for sequences of integers I (R. L. Duncan)
  - zb: "0109.03302"
    name: A topology for sequences of integers I (R. L. Duncan)
---

Let $A$ be the set of all strictly increasing, infinite sequences of positive integers. For any $x\in A$, define $N(n,x)$ as the number of elements of $x$ less than $n$. Let $\delta (x) =\lim_{n\to\infty} \frac{N(n,x)}{n}$. Let $X$ be the subset of $A$ containing precisely the sequences $x$ for which $\delta(x)$ exists. Now for any $x,y\in X$ define $k(x,y)$ to be the smallest index $i$ such that $x_i\neq y_i$. We define a metric $d(x,y)$ on $X$ as $$d(x,y)=\frac{1}{k(x,y)}+|\delta (x) - \delta (y)| \text{ with } d(x,x)=0.$$ Duncan's Space is the topology on $X$ induced by this metric.

Defined as counterexample #136 ("Duncan's Space")
in {{doi:10.1007/978-1-4612-6290-9}}.

Introduced and studied by R. L. Duncan in 
{{zb:0085.03002}} (<https://www.jstor.org/stable/2309919>)
and {{zb:0109.03302}} (<https://www.jstor.org/stable/2309171>).
