---
uid: I000010
if:
  and:
  - extremally-disconnected: true
  - metrizable: true
then:
  discrete: true
converse:
- !ruby/object:Uid
  prefix: I
  id: 143
- !ruby/object:Uid
  prefix: I
  id: 44
---
If $X$ is metrizable and $p \in X$ is not open, $U = \cup_{n \in \omega} [B(p,\frac{1}{2n}) \setminus cl(B(p,\frac{1}{2n+1}))]$ is an open set containing $p$ as a non-interior limit point and thus $X$ is not extremally disconnected.

