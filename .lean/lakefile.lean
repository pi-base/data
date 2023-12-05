import Lake
open Lake DSL

package «pi-base-mathlib»

require Cli from git
  "https://github.com/mhuisi/lean4-cli" @ "nightly"

require CMark from git
  "https://github.com/xubaiw/CMark.lean" @ "main"

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "ac00de12d4cdf0e1ef8927c6fe6fd14020a390c0"

lean_lib PiBase

@[default_target]
lean_exe «pibase» {
  root := `Main
  supportInterpreter := true
}
