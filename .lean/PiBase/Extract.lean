import Lean
import Lean.Data.Json
import Lean.Environment
import Mathlib
import Mathlib.Data.List.Sort

namespace PiBase

open Lean

structure Property where
  id : String
  module : String
deriving Lean.ToJson, Lean.FromJson, Inhabited, Repr

structure Extract where
  properties : List Property
deriving Lean.ToJson, Lean.FromJson, Inhabited, Repr

def isProp (name : Name) : MetaM Bool := do
  let prop := Lean.Expr.const name [.param `u]
  let type := Lean.Expr.sort (.succ (.param `u))
  let x ← Lean.Meta.mkFreshExprMVar type

  let spaceType := Lean.Expr.app (Lean.Expr.const ``TopologicalSpace [.param `u]) x
  let spaceX ← Lean.Meta.mkFreshExprMVar spaceType

  let e := Lean.Expr.app (Lean.Expr.app prop x) spaceX
  let t <- Lean.Meta.inferType e

  pure $ t.isProp

def unname (n : Name) := n.toString
  |> fun s => String.replace s "«" ""
  |> fun s => String.replace s "»"  ""

unsafe def findProperties (handle : Json -> IO Unit) : IO Unit := do
  Lean.searchPathRef.set compile_time_search_path%
  Lean.withImportModules #[`Mathlib] {} (trustLevel := 1024) (fun env => do
    let state := {}
    let sCore : Lean.Core.State := {env}
    let ctx := {fileName := "", fileMap := default}
    let mctx : Lean.Meta.Context := {}

    let constants := env.constants.map₁.toList |> List.map (fun a => a.1)

    let rec run : List Name -> List Name -> MetaM (List Name) := fun
      | (n :: ns), acc => do
        try
          let b <- isProp n
          run ns (if b then n :: acc else acc)
        catch _ => run ns acc
      | [], acc => return acc

    let (rs, _, _) <- Lean.Meta.MetaM.toIO (run constants []) ctx sCore mctx state

    let rec lookups := fun
      | (n :: ns), acc =>
        match env.const2ModIdx.find? n with
        | some (x : Nat) => lookups ns (⟨unname n, match env.header.moduleNames[x]? with | some n => n.toString | _ => ""⟩ :: acc)
        | none => lookups ns acc
      | [], acc => acc

    let properties : List Property := lookups rs []

    handle $ toJson $ Extract.mk properties
  )

end PiBase
