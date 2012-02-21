---
uid: I000231
if:
  and:
  - compact: true
  - kc: true
then:
  maximal-compact: true
---
Let $(K, \tau)$ be a compact KC space. Assume that $K$ is not maximal compact, meaning that there there is a compact topology $\tau'$ strictly finer than $\tau$. Then there is a $\tau'$-closed set $A \subseteq K$ which is not $\tau$-closed. As a closed subset of a compact space, $A$ is $\tau'$-compact. Since $\tau$ is coarser than $\tau'$ it follows that $A$ is $\tau$-compact. From the KC property we deduce that $A$ is $\tau$-closed, contradiction.

