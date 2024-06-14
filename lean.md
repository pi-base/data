manually writing down steps to set up mathlib4, obviously need to automate this...

see <https://github.com/leanprover-community/mathlib4/wiki/Using-mathlib4-as-a-dependency>

## install elan

```
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
```
<!-- 
## start new project

```
lake +leanprover-community/mathlib4:lean-toolchain init πBase math
``` -->

## install lean4 extension

do it

## get mathlib4 cache and build

```
lake exe cache get && lake build
```

