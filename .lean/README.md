# pi-base-mathlib

## What is this?

The π-Base is a community database of examples of topological spaces.

In https://github.com/pi-base/data a file like `properties/P000003.md` begins with some YAML

```
uid: P000003
name: "$T_2$"
mathlib: T2Space
aliases:
  - Hausdorff
  - T2
refs:
  - doi: 10.1007/978-1-4612-6290-9
    name: Counterexamples in Topology
```

The `mathlib:` line is the new contribution: it links the π-Base property [P000003](https://topology.pi-base.org/properties/P000003) to the mathlib4 property [T2Space](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Separation.html#T2Space).

## How to run this

After cloning this repo, fetch the forked https://github.com/pi-base/data as a submodule:

```
git submodule update --init --recursive
```

Then build the `pibase` executable:

```
lake exe cache get
lake update
lake build
```

Finally run

```
./build/bin/pibase verify
```

to verify the `mathlib:` in the `.md` files.

Running `pibase verify` will verify, for each property, that its
corresponding `mathlib:` is a property of topological spaces.
