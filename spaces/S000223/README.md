---
uid: S000223
name: Ellentuck topology on $[\omega]^\omega$
refs:
  - zb: "0292.02054"
    name: A new proof that analytic sets are Ramsey (E. Ellentuck)
  - zb: "1007.03002"
    name: Set theory (T. Jech, 2003)
  - zb: "1400.03002"
    name: Combinatorial set theory (L. Halbeisen, 2017)
---

Let $X = [\omega]^\omega$, the set of infinite sets of nonnegative integers, and give it the topology with basis consisting of all sets

$$[s, A] = \{B \in X: s \subseteq B \subseteq s \cup A \;\text{ and }\; \max(s) < \min(B \setminus s)\}$$

for a finite $s\subseteq\omega$ and an infinite $A\subseteq\omega$.
If $s = \emptyset$ we let $\max(s) = -1$.

*Note*: Omitting the condition $\max(s) < \min(B \setminus s)$ would give another base for the same topology, but the form chosen above is usually more convenient.

Introduced by Ellentuck in {{zb:0292.02054}} (<https://www.jstor.org/stable/2272356>). See also Definition 26.25 in {{zb:1007.03002}} and the section "The Ellentuck Topology" on p. 248 of {{zb:1400.03002}}
