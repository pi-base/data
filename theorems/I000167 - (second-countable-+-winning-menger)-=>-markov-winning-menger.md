---
uid: I000167
if:
  and:
  - second-countable: true
  - winning-menger: true
then:
  markov-winning-menger: true
refs:
  - doi: 10.14712/1213-7243.2015.201
    name: Applications of limited information strategies in Menger's game
---
Let $\sigma(\mathcal{U}_0,\dots,\mathcal{U}_{n-1})$ be a winning strategy for $F$, and observe that since $X$ is second-countable, we may assume all covers are countable. Let $\mathfrak{C}$ be the collection of all countable covers of $X$. We define $R_s,\mathcal{U}_s$ for $s\in\omega^{<\omega}$ as follows:


* $R_\emptyset = \bigcap_{\mathcal{U}\in\mathfrak{C}} \left(\bigcup \sigma(\mathcal{U})\right)$
* Note that there are only countably many distinct finite subsets $\sigma(\mathcal{U})$ of the countable collection $\mathcal U$. Thus define each $\mathcal U_{\langle n\rangle}$ so that
  $$ R_\emptyset = \bigcap_{n<\omega}\left(\bigcup\sigma(\mathcal{U}_{\langle n\rangle})\right) $$
* $R_s = \bigcap_{\mathcal{U}\in\mathfrak{C}} \left(\bigcup \sigma(\mathcal{U}_{s\restriction 1},\mathcal{U}_{s\restriction 2},\dots,\mathcal{U}_s,\mathcal{U})\right)$
* Again, note that there are only countably many distinct finite subsets $\sigma(\mathcal{U}_{s\restriction 1},\mathcal{U}_{s\restriction 2},\dots,\mathcal{U}_s,\mathcal{U})$ of the countable collection $\mathcal U$. Thus define each $\mathcal U_{s{^\frown}\langle n\rangle}$ so that
  $$R_s = \bigcap_{n<\omega} \left(\bigcup \sigma(\mathcal{U}_{s\restriction 1}, \mathcal{U}_{s\restriction 2}, \dots, \mathcal{U}_s, \mathcal{U}_{s{^\frown}\langle n\rangle})\right)$$



See Lemma 4.10 of
{{10.14712/1213-7243.2015.201}}.
