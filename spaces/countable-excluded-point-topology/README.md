---
uid: S000012
slug: countable-excluded-point-topology
name: Countable Excluded Point Topology
---
The excluded point topology on a set $X$ consists of $X$ along with all subsets of $X$ which do not contain some fixed point $p$, $\tau = \{U \subset X : p \not\in U \} \cup \{X\}$.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 47-48.
* [Excluded point topology](http://en.wikipedia.org/wiki/Excluded_point_topology) on Wikipedia.

[[Proof of Topology]]
To prove the first condition, note that $X\in \tau$ by definition. Now, note that $\emptyset \subset X$ and $p\notin \emptyset$. It follows that $\emptyset \in \tau$. 
Now to prove the second condition, consider $\bigcup_{i\in I} U_i$ where $I$ is some arbitrary indexing set. It follows that there are two cases, either $p\in \bigcup_{i\in I} U_i$ or $p\notin \bigcup_{i\in I} U_i$. For the case in which $p$ is in the union, it must be the case that $X$ is in the union, because the only open set containing $p$ is $X$. It follows then that the union is $X$. So in this case, the second condition holds. To prove the second case, when $p$ is not in the union, we simply have an arbitrary union of subsets of $X$ which must be a subset of $X$ that does not contain $p$. So, the second condition holds for this case. 
To prove the final condition, consider $\bigcap_i^n U_i$. Again, there are two cases here, either $p$ is in the intersection, or it is not. For when $p$ is in the intersection, note that every open set other than $X$ does not contain $p$. So for $p$ to be in the intersection, it must be the case that $X$ is the only set in the intersection and thus it is open. Now if $p$ is not in the intersection, it must be a subset of $X$ that does not contain $p$. So in both cases, the intersection is open, and thus the final condition holds and $\tau$ is a topology on $X$.

