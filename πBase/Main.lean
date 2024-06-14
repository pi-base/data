import Mathlib.Topology.Basic

universe u

def TopologicalSpace.Property : Type (u + 1) := ∀ (X : Type u) [TopologicalSpace X], Prop
  deriving CompleteBooleanAlgebra
