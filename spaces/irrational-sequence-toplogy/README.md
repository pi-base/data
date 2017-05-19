---
uid: S000159
slug: irrational-sequence-toplogy
name: Irrational sequence toplogy
---
We define topology on $\mathbb{R}$. For each $q\in \mathbb{Q}$ let $x^{q}=(x_n^q)_{n \in \mathbb{N}}$ be arbitrary but fixed sequence in $\mathbb{I}$ that converges to $q$ .
Let $A_n(q)=\{x_k^q:k\geq n\}$ be tail of a sequence $x^{q}$ for each $n \in \mathbb{N}$.
We define topology by defining it's basis:
$\mathcal{B}=\{\{x\}:x \in \mathbb{I}\}\cup \{A_n(q)\cup \{q\}:n \in \mathbb{N}, q \in  \mathbb{Q}\}$

[[Proof of Topology]]
It's enough to prove that $\mathcal{B}$ is cover for $\mathbb{R}$ and that for each $B_1,B_2 \in \mathcal{B}$ and for each $x \in B_1\cap B_2$ there exists $B \in B_1\cap B_2$ such that $x \in B \subseteq B_1\cap B_2$.
$\mathcal{B} $ is obviously cover for  $\mathbb{R}$ .
Suppose that $B_1,B_2 \in \mathcal{B}$ and $x \in B_1\cap B_2$. If $x \in \mathbb{I}$ then $B:=\{x\}$.
If $x\in \mathbb{Q}$ then $B_1=A_{n_1}(x)\cup \{x\}$ and $B_2=A_{n_2}(x)\cup \{x\}$. Suppose that $n_2\geq n_1$.Then $B:=B_2=A_{n_2}(x)\cup \{x\}\subseteq  B_1\cap B_2=B_2$

