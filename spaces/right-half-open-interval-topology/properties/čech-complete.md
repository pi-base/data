---
uid: T007906
space: right-half-open-interval-topology
property: čech-complete
value: false
---
Let $S$ denote the Sorgenfrey line and $\mathcal{U}_i$ be an open cover of $S$ for every $i \in \omega$. We claim there are points $p \in S$ and $a_i \in S$ and open sets $U_i \in \mathcal{U}_i$ such that $[a_i, p) \subset U_i$ for every $i \in \omega$, which may be found as follows:

Pick any $U_0 \in \mathcal{U}_0$. Since $U_0$ is open there are $a_0,b_0 \in S$ such that $[a0,b0) \subset U_0$. Proceeding inductively, if $i \in \omega$ and $a_i,b_i$ have been defined, since $\mathcal{U}_{i+1}$ covers $S$, there is some $U_{i+1} \in \mathcal{U}_{i+1}$ such that $(a_i, b_i) ∩ U_{i+1}$ is nonempty and open. Choose $a_{i+1}, b_{i+1}$ such that $[a_{i+1}, b_{i+1}) \subset (a_i, b_i) \cap U_{i+1}$. This defines $a_i$ and $b_i$ for all $i \in \omega$. Since $\{ [ai,bi]\ |\ i \in \omega \}$ is a nested collection, there is some $p \in \cap [a_i,b_i]$. It follows that $[a_i, p)$ is a nonempty subset of $U_i$ for all $i \in \omega$.

Let $$\mathcal{F} = \{\text{ closed }\ C \subset S\ |\ C \supset [x,p) \text{ for some } x < p \in S\}$$ Then $F$ is a filter of closed sets such that for each $n$ there is some $F_n \in \mathcal{F}$ with $F_n \subset U$ for some $U \in \mathcal{U}_n$, but $\cap \mathcal{F} \subset \cap_{x<p} [x, p) = \emptyset$. By the filter characterization of Čech completeness, $S$ is not Čech complete.

