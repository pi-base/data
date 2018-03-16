---
uid: I000131
if:
  and:
  - sigma-locally-finite-base: true
  - weakly-lindelof: true
then:
  second-countable: true
converse:
- I000090
- I000125
- I000128
---
Let $\mathcal{V}$ be a $\sigma$-locally finite base. For each $x \in X$, there is a neighborhood $N_x$ meeting countably many members of $\mathcal{V}$. If $X$ is weakly Lindelöf, there is a countable $\{N_i\}$ which covers a dense subset of $X$. Then $\mathcal{U} = \{ V \in \mathcal{V}\ |\ N_i \cap V \neq \emptyset\}$ is a countable basis for $X$.
