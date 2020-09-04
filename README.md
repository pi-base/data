![compile](https://github.com/pi-base/data/workflows/compile/badge.svg)

Moving forward, this repository will be the primary way of collaborating and contributing to the [pi-base](https://topology.jdabbs.com), and we'll be building and distributing tools to make that collaboration easier and richer.

# Conventions

The historical literature isn't always consistent on notation or terms. We adhere to the following conventions:

## Primary Texts

Where there is no contradiction with each other or the following conventions, we use terminology established in the following texts:
- [General Topology](https://mathscinet.ams.org/mathscinet-getitem?mr=2048350) by Stephen Willard
- [Topology](https://mathscinet.ams.org/mathscinet-getitem?mr=3728284) by James Munkres

## Separation Axioms

For the separation axioms, `T_n ⇒ T_m` whenever `n ≥ m`. For example [regular](https://github.com/pi-base/data/blob/master/properties/P000011.md) is defined to assert that closed points and sets can be separated; [T₃](https://github.com/pi-base/data/blob/master/properties/P000005.md) is defined to be both `regular` and `T₀`. See e.g. [wikipedia](https://en.wikipedia.org/wiki/Separation_axiom#Main_definitions) for more information.

## Local Properties

If a property is named "locally `P`", then that means that every point in the space has a neighborhood base satisfying P for every member of the base. On the other hand, some authors define "locally `P`" to mean there is a single neighborhood satisfying `P` for each point. These definitions are occasionally equivalent (e.g. locally metrizable), but are not equivalent in general (e.g. locally compact). See [this issue](https://github.com/pi-base/data/issues/42) for discussion.

Use "locally P" when there's a basis of P neighborhoods, and (when not equivalent) use "weakly locally P" when there's a single P neighborhood.
