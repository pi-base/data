---
uid: T026537
space: uncountable-fort-space
property: fixed-point-property
value: false
---
Pick $a \in X \setminus \{ p \}$, and define $f : X \to X$ by $$f(x) = \begin{cases}
p, &\text{if $x = a$} \\\
a, &\text{if $x \neq a$.}
\end{cases}$$

For any $A \subseteq X$ we have that $$f^{-1} ( A ) = \begin{cases}
\emptyset, &\text{if $a,p \notin A$} \\\
\lbrace a \rbrace, &\text{if $p \in A$ and $a \notin A$} \\\
X \setminus \lbrace a \rbrace, &\text{if $p \notin A$ and $a \in A$} \\\
X, &\text{if $a,p \in A$.}
\end{cases}$$
As each of these sets is open in $X$, then $f$ is continuous. However $f$ clearly has no fixed point.

