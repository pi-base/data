---
uid: T001061
space: cantor's-teepee
property: totally-disconnected
value: true
---
Let $Y$ be any subset of Cantor's Teepee containing more than one point. Our goal is to produce two sets $A$ and $B$ such that 

*  $A$ and $B$ are separated open sets in the subspace topology induced by $Y$, and 
*  $Y = A \cup B$.

Since Cantor's Teepee is itself a subspace of the usual topology on $\mathbb{R}^2$, we may revise these conditions to read 

*  $A$ and $B$ are separated open sets in the usual topology on $\mathbb{R}$, and 
*  $Y \subseteq A \cup B$.

Now, suppose $Y$ contains points $p \in X_a$ and $q \in X_c$ with $a \neq c$ (that is, $Y$ witnesses more than one "strand" of the teepee). Choose any real number $b$ such that $a < b < c$ and $b$ lies in a deleted interval of the Cantor set. To obtain the separated open sets $A$ and $B$, take any open set containing $Y$ (or even the entire teepee) and "split" it along the line connecting $(b,0)$ and $(1/2,1/2)$ (see figure).

![enter image description here](http://i.stack.imgur.com/S2yxj.png)

Suppose instead that all points of $Y$ belong to a single strand. The $y$-coordinates of points belonging to this strand are either all rational or all irrational. In either case, we can easily separate the strand by passing our open sets through a point $r$ with $y$-coordinate of the opposite type (see figure).

![enter image description here](http://i.stack.imgur.com/qF3Lx.png)

Therefore every subset of Cantor's teepee with more than one point is disconnected, which is to say Cantor's teepee is totally disconnected.

