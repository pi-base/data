---
uid: S000109
name: Novak space
counterexamples_id: 112
refs:
  - zb: "0053.12404"
    name: On the Cartesian product of two compact spaces (J. Novak)
  - zb: "0386.54001"
    name: Counterexamples in Topology
---

The space $X$ is the subspace $A_1 = \mathbb N\cup P$ of $\beta\mathbb N$
({S108}) constructed in the proof
of Theorem 3 in {{zb:0053.12404}}.

Using the alternative notation $\beta\omega$, the construction goes as follows.
There are $2^\mathfrak{c}$ countably infinite subsets of $\beta\omega$.
Let $\{S_\xi : \xi<\lambda\}$ enumerate them all,
where $\lambda$ is the first ordinal of cardinality $2^\mathfrak{c}$.
By transfinite recursion one can find elements $x_\xi,y_\xi\in\beta\omega\setminus\omega$ for all $\xi$
such that:

1. $x_\xi, y_\xi\in \overline{S_\xi}\setminus S_\xi$;

2. all the $x_\xi$ are distinct and all the $y_\xi$ are distinct;

3. the sets $\{x_\xi:\xi<\lambda\}$ and $\{y_\xi:\xi<\lambda\}$
form a partition of $\beta\omega\setminus\omega$.

Then $X=\omega\cup\{x_\xi:\xi<\lambda\}$ with the subspace topology induced from $\beta\omega$.

Defined as counterexample #112 ("Novak Space") in {{zb:0386.54001}}.
However, the construction in that book is incorrect as it assumes that
$2^\mathfrak{c}$ is a regular cardinal, while it is consistent with ZFC that it isn't.
