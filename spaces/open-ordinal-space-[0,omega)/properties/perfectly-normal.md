---
uid: T000999
space: open-ordinal-space-[0,omega)
property: perfectly-normal
value: false
---
Let $A = \{\alpha \in \Omega\ |\ \alpha \text{ a limit ordinal}\}$. Clearly $A$ is closed. Let $O_n$ be a collection of open supersets of $A$. For a fixed $O_n$ and any $\alpha \in A$ there is some $g(\alpha) < \alpha$ with $[g(\alpha),\alpha] \subset O_n$. By the Pressing Down Lemma, there is some $\alpha_n \in \Omega$ and stationary $S \subset \Omega$ such that $g(s) = \alpha_n$ for all $s \in S$. It follows that $[\alpha_n, \Omega) \subset O_n$. Taking $\alpha = \sup \alpha_n$, $[\alpha,\Omega) \subset \bigcap_n O_n \neq A$ and so $A$ is not $G_\delta$.

