---
uid: T007907
space: niemytzki's-tangent-disc-topology
property: čech-complete
value: true
---
Let $X$ denote the tangent disk space and $\mathcal{U}$ be a cover of $X$ by basic open setsand $\mathcal{U}_i = \mathcal{U}$ foreach $i \in \omega$. Let $\mathcal{F}$ be a filter of closed sets such that for every $n \in \omega$ there is some $F_n \in \mathcal{F}$ with $F_n \in U_n \in \mathcal{U}_n$. 

There are two cases:

* If there is some $G \in F$ such that $G \cap \mathbb{R} = \emptyset$, then for every $F \in \mathcal{F}$, $F \cap G$ is a nonempty bounded (and thus compact) subset of $\mathbb{R}^2$. Thus $\cap \mathcal{F} \neq \emptyset$.
* If not, then for every $F \in \mathcal{F}$, $F \cap \mathbb{R} \neq \emptyset$. Since $F_0 \subset U_0$, $F_0 \cap \mathbb{R} = \{p\}$ and since $F \cap F_0 \in \mathcal{F}$, $F \cap \mathbb{R} \supset \{p\}$ as well. Thus $p \in \cap \mathcal{F} \neq \emptyset$.

