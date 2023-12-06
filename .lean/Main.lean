import PiBase

import Lean
import Lean.Data.Json
import Cli

open Lean Cli

unsafe def runExtractCmd (p : Parsed) : IO UInt32 := do
  let bundlePath := match p.positionalArgs[0]? with
    | some a => a.value
    | _ => "bundle.json"
  let raw <- Json.parse <$> IO.FS.readFile bundlePath
  match raw with
    | Except.error err => do
      IO.println err
      return 1
    | Except.ok (Json.obj bundle) => do
      PiBase.findProperties $ fun lean => do
        -- TODO - non-partial version
        let merged := Json.setObjVal! (Json.obj bundle) "lean" lean
        IO.println merged
      return 0
    | Except.ok _ => do
      IO.println "Bundle is not an object"
      return 1

unsafe def runVerifyCmd (_ : Parsed) : IO UInt32 := do
  return 0

unsafe def extract := `[Cli|
  extract VIA runExtractCmd;
  "extract ."

  ARGS:
    input : String;      "Path to the input bundle file"
]

unsafe def runPiBaseCmd (p : Parsed) : IO UInt32 := do
  p.printHelp
  return 0

unsafe def piBaseCmd : Cmd := `[Cli|
  pibase VIA runPiBaseCmd; ["0.0.1"]
  "Validate formal proofs referenced by https://github.com/pi-base"

  FLAGS:
    "data" : String; "Path to https://github.com/pi-base/data"

  SUBCOMMANDS:
    extract
]

unsafe def main (args : List String) : IO UInt32 :=
  piBaseCmd.validate args
