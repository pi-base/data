---
uid: T026538
space: euclidean-topology
property: rothberger
value: false
---
For each $m \geq 1$ let $\mathcal{U}_m$ be the collection of all open cubes of side $\frac{1}{2^m}$. (That is, each set in $\mathcal{U}_m$ is a product of $n$ open intervals each of length $\frac{1}{2^m}$.) Note that each set in $\mathcal{U}_m$ has Lebesgue measure $\frac{1}{2^{mn}}$.

If $U_m \in \mathcal{U}_m$ for each $m \geq 1$, then the Lebesgue measure of their union is at most $$\sum_{m=1}^\infty \frac{1}{2^{mn}} \leq \sum_{m=1}^\infty \frac{1}{2^m} = 1.$$ As $\mathbb{R}^n$ has infinite Lebesgue measure, $\bigcup_{m=1}^\infty U_n \neq \mathbb{R}^n$.

