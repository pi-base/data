---
uid: S000072
name: Arens square
counterexamples_id: 80
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
---

Let $S=\big((0,1)_{\mathbb Q}\setminus\{\frac{1}{2}\}\big)\times(0,1)_{\mathbb Q}$ and
$X=S\cup\{\langle 0,0\rangle,\langle 1,0\rangle\}\cup\{\langle\frac{1}{2},r\sqrt{2}\rangle:r\in(0,\frac{1}{\sqrt 2})_{\mathbb Q}\}$
(where $I_{\mathbb Q}=I\cap\mathbb Q$).

This space is $X$ with the topology such that points of $S$ have their usual neighborhoods as a subspace of {S176}, and

- $U_n(0,0) = \{\langle 0,0\rangle\} \cup \left((0,\frac{1}{4})_{\mathbb Q}\times(0,\frac{1}{n})_{\mathbb Q}\right)$,
- $U_n(1,0) = \{\langle 1,0\rangle\} \cup \left((\frac{3}{4},1)_{\mathbb Q}\times(0,\frac{1}{n})_{\mathbb Q}\right)$, and
- $U_n(\frac{1}{2},r\sqrt{2}) = \left((\frac{1}{4},\frac{3}{4})\times(r\sqrt{2}-\frac{1}{n},r\sqrt{2}+\frac{1}{n})\right)\cap X$
  for $r\in(0,\frac{1}{\sqrt 2})_{\mathbb Q}$.

are local bases at $\langle 0,0\rangle$, $\langle 1,0\rangle$ and $\langle\frac{1}{2},r\sqrt{2}\rangle$ respectively.

Defined as counterexample #80 ("Arens Square") in {{doi:10.1007/978-1-4612-6290-9}}, where
this space was erroneously claimed to be {P4}.
Compare with {S80} which modifies the construction to
obtain a valid {P4} example.
