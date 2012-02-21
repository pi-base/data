---
uid: I000107
if:
  and:
  - countably-compact: true
  - metacompact: true
then:
  compact: true
converse:
- !ruby/object:Uid
  prefix: I
  id: 1
- !ruby/object:Uid
  prefix: I
  id: 13
- !ruby/object:Uid
  prefix: I
  id: 14
---
Let $X$ be metacompact and countably compact. If $\{U_\alpha\}$ is an open cover, let $\{V_\beta\}$ be a point finite refinement of $\{U_\alpha\}$. Without loss of generality, assume $\{V_\beta\}$ is a minimal such subcovering. Choose an $x_\beta$ in each $V_\beta \setminus \cup_{\gamma \neq \beta} V_\gamma$. Then if $\{V_\beta\}$ is infinite, $\{x_\beta\}$ is an infinite set with no limit point.

