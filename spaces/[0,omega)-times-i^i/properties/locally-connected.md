---
uid: T001206
space: "[0,omega)-times-i^i"
property: locally-connected
value: false
---
The point $\omega_0\times 0$ has no connected neighborhood.  Indeed, let $U$ be an open neighborhood of $\omega_0\times 0$.  Then $U$ contains a set of the form $(a,b)\times V$, with $a < \omega_0 < b$.  Let $A=([0,a+2)\times I^I)\cap U$ and $B=((a+1,\Omega)\times I^I)\cap U$.  Each is open since it is the intersection of two open sets.  They are clearly disjoint, and $U=A\cup B$, so they form a separation of $U$, hence $U$ is not connected.  

It is noted that this works replacing $\omega_0$ with any limit ordinal and relies only on the fact that $[0,\Omega)$ is not locally connected.

