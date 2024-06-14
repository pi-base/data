import πBase.Properties.P2.Def
import πBase.Properties.P99.Def

open Filter Topology

theorem T226 : P99 ≤ P2 := fun X _ ⟨p99⟩ ↦ by
  suffices ∀ y, IsClosed ({y} : Set X) by exact { t1 := this }
  apply fun y ↦ isClosed_of_closure_subset ?_
  apply fun x xincly ↦ Set.mem_singleton_iff.mp <| p99 x y (fun _ ↦ y) (fun U Unhd ↦ ?_)
    tendsto_const_nhds
  apply mem_map.mpr <| mem_atTop_sets.mpr ?_
  simp only [ge_iff_le, Set.mem_preimage]
  exact ⟨0,
    fun _ _ ↦ Set.inter_singleton_nonempty.mp <| (mem_closure_iff_nhds.mp xincly) U Unhd⟩
