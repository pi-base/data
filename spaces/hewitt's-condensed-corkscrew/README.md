---
uid: S000090
name: Hewitt's Condensed Corkscrew
---
If $T = S \cup \{a^\pm\}$ is the [Tychonoff corkscrew](/brubeck/spaces/tychonoff-corkscrew/) and $[0,\omega_1)$ the set of countable ordinals, let $A = T \times [0,\omega_1)$ and $X = S \times [0,\omega_1) \subset A$. Think of $A$ as an uncountable sequence of corkscrews $A_\lambda$ for $\lambda \in [0,\omega_1)$ and $X$ as the same sequence of corkscrews missing all infinity points. Let $\Gamma:X \times X \rightarrow [0,\omega_1)$ be a bijection and $\pi_i$ the coordinate projections $X \times X \rightarrow X$ and define $\psi: A \setminus X \rightarrow X$ by $\psi(a^+_\lambda) = \pi_1 \Gamma^{-1}(\lambda)$ and $\psi(a^-_\lambda) = \pi_2 \Gamma^{-1}(\lambda)$. Then if $x \neq y \in X$,
letting $\lambda = \Gamma(x,y)$, both $\psi^{-1}(x)$ and $\psi^{-1}(y)$ intersect $A_\lambda$.

Define a topology on $A$ by basis neighborhoods $N$ of each $x \in X$ with the property that $\psi^{-1}(N \cap X \subset N$ together with $A_\lambda$-basis neighborhoods of each point $a \in A \setminus X$. $X \subset A$ will carry the subspace topology. 

To construct a typical basis neighborhood of $x \in X$, begin with a $\sigma$-neighborhood $N_0$ of $x \cup \psi^{-1}(x)$ where $\sigma$ is the product topology on $A = T \times \omega_1$ where $\omega_1$ carries the discrete topology. Then inductively define $N_i$ to be a $\sigma$-neighborhood of $N_{i-1} \cup \psi^{-1}(N_{i-1} \cap X)$ and $N = \bigcup N_i$. Clearly $\psi^{-1}(N \cap X) \subset N$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 111-113.


