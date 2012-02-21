---
uid: T000095
space: countable-complement-topology
property: first-countable
value: false
---
Suppose at some point $x$ there exists a countable basis.  Then there exists a countable collection of open sets, $\mathcal{B}_x$, each of which contains $x$, such that every open neighborhood of $x$ contains some set $B \in \mathcal{B}_x$.  So $\cap \mathcal{B}_x = \{x\}$, and thus $X \setminus \{x\} = X \setminus \mathcal{B}_x = \bigcup_{B \in \mathcal{B}_x}(X\setminus B)$.  Each of the $X \setminus B$ is, by definition, countable.  Thus since the union of a countable collection of countable sets is countable, $X \setminus \{x\}$ must be countable.  This is a contradiction.

