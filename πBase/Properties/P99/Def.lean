import πBase.Main
import Mathlib.Topology.Separation

universe u

open Filter Topology

class USSpace (X : Type u) [TopologicalSpace X] : Prop where
  us : ∀ x y : X, ∀ f : ℕ → X, Tendsto f atTop (𝓝 x) → Tendsto f atTop (𝓝 y) → x = y

abbrev P99 : TopologicalSpace.Property := USSpace
