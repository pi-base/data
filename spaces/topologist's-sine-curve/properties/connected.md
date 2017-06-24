---
uid: T000434
space: topologist's-sine-curve
property: connected
value: true
refs:
  - doi: 10.1007/978-1-4612-6290-9_6
    name: Counterexamples in Topology
---
We have two continuous functions which are inverse to each other:
$$p : S \setminus \{(0,0)\} \to (0,1],\ (x,y) \mapsto x$$
$$q : (0,1] \to S \setminus \{(0,0)\},\ x \mapsto (x, \sin \frac{1}{x})$$
which proves that $S \setminus \{(0,0)\}$ is homeomorphic to $(0,1]$.

Since $(0,1]$ is connected, also $S \setminus \{(0,0)\}$ is connected.

Now suppose $S = U \cup V$ is a disjoint union of open sets. WLOG $(0,0) \in U$, then $U' := U \setminus \{(0,0)\}$ is an open subset of $S \setminus \{(0,0)\}$ and $S \setminus \{(0,0)\} = U' \cup V$ is a disjoint union. Since this is a connected space, either $U'$ or $V$ must be empty.

If $U'$ were empty, $U$ would contain only the single point $(0,0)$. From the subspace topology of $S$ we know that there exists an open $W \subset \mathbb{R}^2$ such that $U = W \cap S$. On the other hand, every open subset of the euclidean topology $\mathbb{R}^2$ that contains the point $(0,0)$ also contains an open ball around the point $(0,0)$ of some radius $\epsilon > 0$. In particular, for all $x$ with $\sqrt{x^2 + sin^2 \frac{1}{x}} = d((0,0),(x, sin \frac{1}{x})) < \epsilon$ we already have $(x,sin \frac{1}{x}) \in W \cap S = U$. This shows that $U'$ cannot be empty, hence $V$ must be empty.

See item #3 for space #116 in {{doi:10.1007/978-1-4612-6290-9_6}}.
