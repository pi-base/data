---
uid: S000102
name: Baire space of weight continuum $B(\mathfrak c)$
aliases:
  - Countable product of continuum-sized discrete spaces
  - Baire metric on $\mathbb R^\omega$
counterexamples_id: 104
refs:
  - zb: "0684.54001"
    name: General Topology (Engelking, 1989)
  - zb: "0386.54001"
    name: Counterexamples in Topology
---

$X$ is the product of countably many copies of {S3}.
Specifically, one can give $\mathbb R$ the discrete topology
and take $X=\mathbb R^\omega$ with the product topology.

In general, the *Baire space of weight $\kappa$* for some infinite cardinal $\kappa$
is the countable power $D^\omega$ for some discrete space $D$ with $|D|=\kappa$,
and is denoted $B(\kappa)$.  It has weight $\kappa$.
The current space is $X=B(\mathfrak c)=B(2^{\aleph_0})$.

This space is metrizable using the Baire metric.  For distinct elements
$x=(x_i)_{i\ge 0}, y=(y_i)_{i\ge 0}$ in $X=$D^\omega$ the *Baire metric*
is defined by $d(x,y)=\frac{1}{i+1}$ where $i$ is the first coordinate with $x_i\neq y_i$.
And $d(x,x)=0$.

See Example 4.2.12 in {{zb:0684.54001}}.

Also defined as counterexample #104 ("Baire Metric on \(\mathbb{R}^\omega\)")
in {{zb:0386.54001}}, where the index starts at $i=1$.

This space has a finer topology than {S30}.

Compare with {S28}, which is the Baire space $B(\aleph_0)$.
