---
uid: S000100
slug: mathbb{z}^{mathbb{z}}
name: Countable power of a countable discrete space
aliases:
  - Z^Z
  - Omega to the omega power
  - Baire space
  - Baire product
counterexamples_id: 102
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
  - wikipedia: Baire_space_(set_theory)
    name: Baire space (set theory) on Wikipedia
---
The product topology on \(\omega^\omega\). This space is homeomorphic to the
irrationals.

Defined as counterexample #102 ("\(\mathbb{Z}^{\mathbb{Z}}\)")
in {{doi:10.1007/978-1-4612-6290-9}}.

<!-- [[Proof of Topology]]
We will verify the function $\rho((x_n),(y_n))=\sum_{n\in\mathbb{Z}}2^{-|n|}d(x_n,y_n)$ where $d(x_n,y_n)$ is the discrete metric, is a metric.

$\textbf{M1}:$ When $(x_n)=(y_n)$, each $x_n=y_n$, so $2^{-|n|}d(x_n,y_n)=0$ for all $n\in \mathbb{Z}$. Therefore, $\rho((x_n),(y_n)) = 0$.  

$\textbf{M2}:$ For $(x_n),(y_n),(z_n) \in \mathbb{Z}^{\mathbb{Z}}$, observe
\begin{align*}
\rho((x_n),(y_n)) + \rho((y_n),(z_n)) &= \sum_{n\in\mathbb{Z}}2^{-|n|}d(x_n,y_n) + \sum_{n\in\mathbb{Z}}2^{-|n|}d(y_n,z_n)\\
&= \sum_{n\in\mathbb{Z}}(2^{-|n|}d(x_n,y_n)+2^{-|n|}d(y_n,z_n)) \\
&= \sum_{n\in\mathbb{Z}}2^{-|n|}(d(x_n,y_n)+d(y_n,z_n)) \\
&\geq \sum_{n\in\mathbb{Z}}2^{-|n|}d(x_n,z_n)\\
&= \rho((x_n),(z_n))
\end{align*}
noting $d(x_n,y_n)+d(y_n,z_n) \geq d(x_n,z_n)$, since $d$ is a metric.

$\textbf{M3}:$ Observe
\begin{align*}
\rho((x_n),(y_n))&=\sum_{n\in\mathbb{Z}}2^{-|n|}d(x_n,y_n)\\
&=\sum_{n\in\mathbb{Z}}2^{-|n|}d(y_n,x_n)\\
&= \rho((y_n),(x_n))\\
\end{align*}
noting $d(x_n,y_n)=d(y_n,x_n)$, since $d$ is a metric.  

$\textbf{M4}:$ For $(x_n) \ne (y_n)$ where $(x_n),(y_n) \in \mathbb{Z}^{\mathbb{Z}}$, there is at least one place in the sequences where $x_i \ne y_i$.  So,
\begin{align*}
/\rho((x_n),(y_n))&=\sum_{n\in\mathbb{Z}}2^{-|n|}d(x_n,y_n)\\
&\geq 2^{-|i|}d(x_i,y_i)\\
&= 2^{-|i|}\\
&> 0.
\end{align*}
 -->
