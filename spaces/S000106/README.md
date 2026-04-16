---
uid: S000106
name: Direct limit $\mathbb R^\infty$ of Euclidean spaces $\mathbb R^n$
refs:
  - wikipedia: Direct_limit
    name: Direct limit on Wikipedia
  - mathse: 3961052
    name: Answer to "Is the weak topology on $\mathbb{R}^{\infty}$ the same as the box topology?"
  - mathse: 5012784
    name: Answer to "Is $\ell^\infty$ with box topology connected?"
---
The subset $\mathbb{R}^\infty$ of eventually $0$ sequences in $\mathbb{R}^\omega$, with the finest 
topology such that the standard inclusion maps $\mathbb{R}^n \hookrightarrow \mathbb{R}^\infty$, 
$x \mapsto (x^1, \ldots, x^n, 0, \ldots)$, are continuous for each $n$, where $\mathbb{R}^n$ has 
the Euclidean topology.

Equivalently, the set $U \subset \mathbb{R}^\infty$ is open if and only if $U \cap \mathbb{R}^n$ 
is open in $\mathbb{R}^n$ for each $n$, where we identify each Euclidean space $\mathbb{R}^n$ with 
its image.

Equivalently, $\mathbb{R}^\infty$ is the direct limit $\varinjlim \mathbb{R}^n$ of the directed 
system consisting of Euclidean spaces and standard inclusion maps 
$\mathbb{R}^i \hookrightarrow \mathbb{R}^j$, $x \mapsto (x^1, \ldots, x^i, 0, \ldots)$, 
for each $i < j$.

Equivalently, $\mathbb{R}^\infty \subset \mathbb{R}^\omega$ has the subspace topology, where
$\mathbb{R}^\omega$ is given the box topology; this is shown in {{mathse:3961052}}. Moreover,
it is shown in {{mathse:5012784}} that $\mathbb{R}^\infty$ is a quasi-component of the origin in
$\mathbb{R}^\omega$. Hence $\mathbb{R}^\infty$ embeds into {{S107}}
as a path component.

For general discussion on direct limits, see {{wikipedia:Direct_limit}}.
