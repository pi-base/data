---
uid: I000221
if:
  and:
  - countable: true
  - locally-compact: true
  - t_2: true
then:
  and:
  - metrizable: true
  - zero-dimensional: true
---
We show that the one-point compactification of this space has these properties, and therefore the original space does as well.

The compactification is countable and $T_4$; an application of Urysohn's Lemma shows that any connected subspace of a normal space must be a singleton or at least of cardinality $\mathfrak c$, so the space is totally disconnected. Every compact neighborhood in a $T_2$ totally disconnected space must be clopen, so the space is zero-dimensional. Finally, any countably compact $T_2$ space is first-countable, and a countable first-countable space is second-countable, giving us that the compactification is metrizable.

