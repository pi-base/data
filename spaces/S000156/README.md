---
uid: S000156
name: Arens space
aliases:
- $S_2$
refs:
  - mr: 37500
    name: Note on convergence in topology (Arens)
  - mr: 3269014
    name: Mapping theorems on countable tightness and a question of F. Siwiec (Lin & Zhang)
---

Let $X=\omega\cup\{\infty\}$ be the one-point compactification of a
countable discrete space. Arens space $S_2$ is the minimal topology
on $(X\times\omega)\cup\{\infty'\}$ where
$(\{\infty\}\times\omega)\cup\{\infty'\}$ is homeomorphic to $X$.

Note the subspace $(\omega\times\omega)\cup\{\infty'\}$ of the Arens space is homeomorphic to {S23}, as mentioned in Examples 2.10 and 3.10 of {{mr:3269014}}.

Alternatively, let $\mathbb{N}$ be the set of all positive integers. In this formulation, the Arens' space is the set
$X = \{\infty\} \cup \mathbb{N} \cup (\mathbb{N} \times \mathbb{N})$ with the open neighborhoods defined according to the following conditions:

- The points in $\mathbb{N} \times \mathbb{N}$ are isolated
- The neighborhoods at each $n \in \mathbb{N}$ are of the form
    \[
      B_{n,m} = \{n\} \cup \{(n,j) \in \mathbb{N} \times \mathbb{N} : j \geq m\}
    \]
    for some $m \in \mathbb{N}$;
- The neighborhoods at $\infty$ are obtained by removing from $X$ finitely many $B_{n,1}$
    and by removing finitely many isolated points in each of the remaining $B_{n,1}$.

This space was originally defined by Richard Arens in {{mr:0037500}}.
