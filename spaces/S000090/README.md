---
uid: S000090
name: Hewitt's condensed corkscrew
counterexamples_id: 92
refs:
  - zb: "0386.54001"
    name: Counterexamples in Topology
---

If $T = \text{DJ}(Y, H, K)$ is the {S88},
*Hewitt's condensed corkscrew* is the set $X = (T\setminus \{a^+, a^-\}) \times \omega_1$ with the subspace topology induced from
a certain topology $\tau_A$ on $A = T \times \omega_1$ which we define below.

Let $\Gamma:X \times X \rightarrow \omega_1$ be a fixed bijection and $\pi_i:X\times X\to X$ be the coordinate projections. Define $\psi: A \setminus X \rightarrow X$ by $\psi(a^+, \lambda) = \pi_1 (\Gamma^{-1}(\lambda))$ and $\psi(a^-, \lambda) = \pi_2 (\Gamma^{-1}(\lambda))$. Define $A_\lambda = T\times \{\lambda\}$ for $\lambda\in \omega_1$ and let $\sigma_\lambda$ be the product topology on $A_\lambda$ (so that $(A_\lambda, \sigma_\lambda)$ and $T$ are homeomorphic). Then define $$\tau_A = \{U\subseteq A : \psi^{-1}(U)\subseteq U \text{ and }U\cap A_\lambda\in \sigma_\lambda\text{ for all }\lambda\in\omega_1\}.$$
Note that the topology $\tau_A\restriction A_\lambda$ is coarser than $\sigma_\lambda$, and can be strictly coarser for a given $\lambda$.

Defined as counterexample #92 ("Hewitt's Condensed Corkscrew")
in {{zb:0386.54001}}.
