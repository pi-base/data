---
uid: I000060
if:
  and:
  - sequentially-compact: true
  - metrizable: true
then:
  compact: true
---
If $\epsilon > 0$ such that $X$ cannot be covered by finitely many $\epsilon$-balls, then for each $n \in \omega$ choose inductively an $x \in X \cup_{i<n} B(x_i,\epsilon)$. Then $\{x_n\}$ has no convergent subsequence, contrary to hypothesis.

Let $\mathcal{A}$ be a cover of $X$ and suppose, towards a contradiction, that there is no $\delta > 0$ such that $diam(S) < \delta$ implies $S \subset A$ for some $A \in \mathcal{A}$. For each $n \in \omega$ choose a set $C_n$ of diameter at most $\frac{1}{n}$ with $C_n$ not a subset of $A$ for any $A \in \mathcal{A}$ and $x_n \in C_n$. Then some subsequence $x_{n_i}$ converges to some $a \in X$ and $a \in A$ for some $A \in \mathcal{A}$. Choosing $i$ large enough that $C_{n_i} \subset B(x_{n_i},\frac{\epsilon}{2})$ and $d(x_{n_i},a) < \frac{\epsilon}{2}$, $C_{n_i} \subset A$ contrary to hypothesis.

Now, if $X$ is sequentially compact and $\mathcal{A}$ is an open covering of $X$, choose $\delta > 0$ so that $diam(S) < \delta$ implies $S \subset A$ for some $A \in \mathcal{A}$. Let $\epsilon = \frac{\delta}{3}$. $X$ has a finite cover by open $\epsilon$-balls, each of which lies in some $A \in \mathcal{A}$. Thus, finitely many $A$ are required to cover $X$.

