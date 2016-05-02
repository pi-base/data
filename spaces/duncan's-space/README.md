---
uid: S000132
slug: duncan's-space
name: Duncan's Space
---
Let $A$ be the set of all strictly increasing, infinite sequences of positive integers. For any $x\in A$, define $N(n,x)$ as the number of elements of $x$ less than $n$. Let $\delta (x) =\lim_{n\to\infty} \frac{N(n,x)}{n}$. Let $X$ be the subset of $A$ containing precisely the sequences, $x$, for which $\delta(x)$ exists. Now for any $x,y\in X$ define $k(x,y)$ to be the smallest index $i$ such that $x_i\neq y_i$. We define a metric $d(x,y)$ on $X$ as $$d(x,y)=\frac{1}{k(x,y)}+|\delta (x) - \delta (y)| \text{ with } d(x,x)=0.$$ Duncan's Space is the topology on $X$ induced by this metric.

See also:

* Steen, L. A.; Seebach, J. A. (1970), [Counterexamples in Topology](http://books.google.com/books/about/Counterexamples_in_Topology.html?id=DkEuGkOtSrUC), Dover, pp 153-154.

[[Proof of Topology]]
To prove $d(x,y)$ is a metric on $X$, we must prove for every $x,y \in X$:
\begin{enumerate}
\item{} $d(x,x)=0$
\item{}$d(x,y)>0$
\item{} $d(x,y)=d(y,x)$
\item{} $d(x,y)+d(y,z)\geq d(x,z)$
\end{enumerate}
\paragraph{}
1. By definition, $d(x,x)=0$.
\paragraph{}
2. Note that for all $x,y\in X$, $k(x,y)>0$, and clearly, $|\updelta (x) - \updelta (y)|>0$. It follows that $d(x,y)>0$.
\paragraph{}
3. Note, $k(x,y)=k(y,x)$ and $|\updelta (x) - \updelta (y)| = |\updelta (y)-\updelta (x)|$. So, $$d(x,y)=\frac{1}{k(x,y)}+|\updelta (x) - \updelta (y)|=\frac{1}{k(y,x)}+|\updelta (y)-\updelta (x)|=d(y,x).$$
\paragraph{}
4. We begin with the definition of our distance function. We must show $$\frac{1}{k(x,y)}+|\updelta(x)-\updelta(y)|+\frac{1}{k(y,z)}+|\updelta(y)-\updelta(z)|\geq \frac{1}{k(x,z)} +|\updelta(x)-\updelta(z)|.$$ It is sufficient to prove: 
\begin{enumerate}
\item{} $|\updelta(x)-\updelta(y)|+|\updelta(y)-\updelta(z)|\geq | \updelta(x)-\updelta(z)|$
\item{} $\frac{1}{k(x,y)}+\frac{1}{k(y,z)}\geq \frac{1}{k(x,z)}$
\end{enumerate}
To prove 1, we utilize the triangle inequality $|a|+|b|\geq |a+b|$ with $a=\updelta(x)-\updelta(y)$ and $b=\updelta(y)-\updelta(z)$. So, $$|\updelta(x)-\updelta(y)|+|\updelta(y)-\updelta(z)|\geq |\updelta(x)-\updelta(y)+\updelta(y)-\updelta(z)| = |\updelta(x)-\updelta(z)|.$$
\paragraph{}
Note that to prove 2, we will instead show that either $k(x,y) \text { or } k(y,z)$ is less than or equal to $k(x,z)$. It then will follow that 2) holds. There are two cases: 
\paragraph{}
\underline{\textit{Case 1:}} $k(x,y)\leq k(x,z)$
\paragraph{}
This directly implies $$\frac{1}{k(x,y)}\geq\frac{1}{k(x,z)}.$$
\paragraph{}
\underline{\textit{Case 2:}} $k(x,y)>k(x,z)$
\paragraph{}
By definition, $x_n=y_n$ for $n<k(x,y)$, and $x_n=z_n$ for $n<k(x,z)$. Because $k(x,y)>k(x,z)$, it follows $x_n=y_n=z_n$ for $n<k(x,z)$. Furthermore, $x_{k(x,z)}\neq z_{k(x,z)}$, so $y_{k(x,z)}\neq z_{k(x,z)}$. Thus, $k(y,z)=k(x,z)$.

