---
uid: T000351
space: alexandroff-square
property: first-countable
value: false
---
We will prove that for each $x \in [0,1]$ there doesn't exist countable base at point $(x,x)$. Let's assert opposite, that is, that there exists $x \in [0,1]$ such that there exists countable base $\mathcal{B}=\{B_{n}:n \in \mathbb{N}\}$ at point $(x,x)$. For each $n \in \mathbb{N}$ let $A_{n}= \{x_{0},\dots ,x_k\}$ where $B_n=\{(t,y) \in X: |y-x|<\epsilon , t \notin \{x_0,\dots,x_k\}\}$. Let $A=\bigcup\limits_{n \in \mathbb{N}}A_n$. Then $cardA\leq\aleph_0$.
Suppose $z \in [0,1]$ is an arbitrary element.Then $U=([0,1]\setminus z)\times[0,1]$ is an open set which contains $(x,x)$. So there exists $B \in \mathcal{B}$ such that $ (x,x) \in B \subseteq U$.That implies $z\notin B$ so it must be $z \in A_n\subseteq A$. We conclude $[0,1]\subseteq A$,but that is contradiction with $card[0,1]=\mathfrak{c}>cardA=\aleph_0$.

