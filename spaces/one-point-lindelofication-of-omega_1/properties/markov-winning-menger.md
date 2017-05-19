---
uid: T023676
space: one-point-lindelofication-of-omega_1
property: markov-winning-menger
value: false
---
For all functions $\tau:\omega_1\times\omega \rightarrow [\omega_1]^{<\omega}$, there exists a sequence $\alpha_0, \alpha_1, \dots < \omega_1$ such that $\{\tau(\alpha_n,n): n<\omega\}$ is not a cover for $\{\beta:\forall n<\omega (\beta < \alpha_n)\}$.

Suppose that $\sigma(\mathcal{U}, n)$ was a winning Markov strategy and aim for a contradiction. Consider the covers $\mathcal{U}(\alpha) = \{[\alpha,\omega_1)\cup\{\infty\}\} \cup \{\{\beta\}:\beta < \alpha\}$ and define $\tau(\alpha,n)$ to be the union of singletons chosen by $\sigma(\mathcal{U}(\alpha),n)$. 

Using the sequence $\alpha_0, \alpha_1,\dots<\omega_1$ from the previous lemma, we consider the play $\mathcal{U}(\alpha_0),\mathcal{U}(\alpha_1),\dots$.

As $\sigma$ was a winning strategy, $\{\sigma(\mathcal{U}(\alpha_n),n): n<\omega\}$ must cover $\omega_1^\dagger$, and thus $\{\tau(\alpha_n,n): n<\omega\}$ must cover $\{\beta:\forall n<\omega (\beta < \alpha_n)\}$, contradiction.

