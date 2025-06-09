# Ivy-Wire  —  B₂ N₂ C₁₂ H₈ (self-replicating, room-T super-conductor)

| Property | Value | Source |
|----------|-------|--------|
| Σ parity | 0 with **10** bonds | `theory/B2N2C12H8.cif` + `common/parity_scan.py` |
| Loop length L | 3 (kagome) | Lean proof `LoopGap.lean` |
| Gap 2Δ/kT | **1.76** (ledger constant) | theory |
| Tc (from EPW) | 307 ± 15 K | `theory/qe_stdout/` |
| μ_net | 0.112  <  1/3 → replicates | Lean proof |

Folders  
* **theory/** CIF, QE inputs, EPW stdout (tar, SHA)  
* **fabrication/** PECVD recipe, growth video  
* **data_raw/** 4-probe resistance CSV, Meissner levitation MP4  
* **notebooks/** plots that regenerate key figures 