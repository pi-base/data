import πBase.Properties.P2.Def
import πBase.Properties.P99.Def

open Filter Topology

theorem T226 : P99 ≤ P2 := fun X _ ⟨p99⟩ ↦ by
  rw [P2, t1Space_iff_exists_open]
  intro x y
  contrapose; simp at *
  intro hyp
  let f : ℕ → X := fun _ ↦ y
  have h : Tendsto f atTop (𝓝 x) →
      Tendsto f atTop (𝓝 y) → x = y := by
    apply p99
  apply h
  · intro N NNx
    have yinN : y ∈ N := by
      rw [mem_nhds_iff] at NNx
      rcases NNx with ⟨ U, ⟨ UsubN, Uopen, xinU⟩ ⟩
      apply UsubN
      apply hyp
      exact Uopen
      exact xinU
    apply mem_map.mpr
    simp
    use 0
    simp
    intro b
    have : f b = y := by
      simp
    rw [this]
    exact yinN
  · exact tendsto_const_nhds
