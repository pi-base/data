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
  - zb: "0298.57008"
    name: Characteristic classes (Milnor-Stasheff)
  - zb: "0307.55015"
    name: Fibre bundles. 2nd ed. (Husemoller)
  - zb: "1280.54001"
    name: Geometric aspects of general topology. (Sakai)
  - wikipedia: Fréchet–Urysohn_space
    name: Fréchet–Urysohn space on Wikipedia
---
$X$ is the subset $\mathbb{R}^\infty$ of eventually $0$ sequences in $\mathbb{R}^\omega$,
with the [final topology](https://en.wikipedia.org/wiki/Final_topology)
with respect to the standard inclusion maps $\mathbb{R}^n \hookrightarrow \mathbb{R}^\infty$,
$x \mapsto (x^1, \ldots, x^n, 0, \ldots)$.
Thus, a set $U \subseteq \mathbb{R}^\infty$ is open iff $U \cap \mathbb{R}^n$
is open in $\mathbb{R}^n$ for each $n$,
where we identify each Euclidean space $\mathbb{R}^n$ with its image. 

Equivalently, $\mathbb{R}^\infty$ is the direct limit $\varinjlim \mathbb{R}^n := (\bigsqcup_{i = 1}^\infty \mathbb{R}^i)/\sim$ of the directed 
system consisting of Euclidean spaces and standard inclusion maps 
$\mathbb{R}^i \hookrightarrow \mathbb{R}^j$, $x \mapsto (x^1, \ldots, x^i, 0, \ldots)$, 
for each $i < j$. The equivalence relation $\sim$ identifies points which correspond under these inclusions.
For general discussion on direct limits, see {{wikipedia:Direct_limit}}.

Equivalently, $\mathbb{R}^\infty \subset \mathbb{R}^\omega$ has the subspace topology, where
$\mathbb{R}^\omega$ is given the box topology; this is shown in {{mathse:3961052}}. Moreover,
it is shown in {{mathse:5012784}} that $\mathbb{R}^\infty$ is a quasi-component of the origin in
$\mathbb{R}^\omega$. Hence $\mathbb{R}^\infty$ embeds into {S107}
as a path component.

Defined on page 62 of {{zb:0298.57008}}, on page 2 of {{zb:0307.55015}}, 
on page 56 of {{zb:1280.54001}}, and on {{wikipedia:Fréchet–Urysohn_space}} 
under Direct limit of finite-dimensional Euclidean spaces.
