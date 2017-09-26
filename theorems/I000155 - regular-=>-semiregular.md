---
uid: I000155
if:
  regular: true
then:
  semiregular: true
refs:
  - mr: MR2048350
    name: General Topology (Willard)
---
Let $(X,\tau)$ be a regular topological space. Let also $x \in X$ and $V \in \tau$ be arbitrary. To show that $(X,\tau)$ has a base of regular open sets, we show there is $U$ satisfying $x \in U \subset V$ and $\operatorname{int}(\operatorname{cl} (U)) = U$.

Since $x \notin V^c$, it follows from regularity that $x$ and $V^c$ can be separated by open sets. Let $U_0$ be the open set containing $x$ in this separation. Define $U$ to be $\operatorname{int}(\operatorname{cl} (U_0))$.

Since $U_0$ is open, we know $U_0 \subset U$, and so $x \in U$.

Since $U_0$ is a separation of $x$ from $V^c$, we know $\operatorname{cl}(U_0) \subset V$, and so $U \subset V$.

Finally, $\operatorname{int}(\operatorname{cl} (U)) = \operatorname{int}(\operatorname{cl} (\operatorname{int}(\operatorname{cl} (U_0)))) = \operatorname{int}(\operatorname{cl} (U_0)) = U$.

Asserted in 14E of {{mr:MR2048350}}.
