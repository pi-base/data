---
uid: I000037
if:
  and:
  - regular: true
  - normal: true
then:
  completely-regular: true
---
If $X$ is regular and normal, given any $a \in X$ and $B \subset X$ closed with $a \notin B$, by regularity there is some open set $U$ containing $a$ with $cl(U)$ disjoint from $B$. By Urysohn's Lemma, there is a continuous function $f:X \rightarrow [0,1]$ with $f(cl(U))=\{0\}$ and $f(B)=\{1\}$. Then clearly $f(a)=0$.

