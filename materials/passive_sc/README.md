# Passive-SC — B₂ N₂ C₄ H₄ (static room-T super-conductor)

| Property | Value | Source |
|----------|-------|--------|
| Σ parity | 0 with **4** heavy–heavy σ-bonds | `theory/B2N2C4H4.cif` + `common/parity_scan.py`
| Loop length L | 4 (BN–C–C square) | Lean proof `LoopGap.lean`
| Gap 2Δ/kT | 1.76 (ledger constant) | theory
| Tc (EPW) | 310 ± 10 K | `theory/qe_stdout/`
| μ_net | 0.30  >  1/4 — _non-replicating_ | calculation
| Current density J_c | ≈ 10⁷ A cm⁻² | London length 10⁻⁷ m

Folders  
* **theory/** CIF, QE inputs, EPW stdout (SHA-pinned)  
* **fabrication/** single-pass PECVD recipe  
* **data_raw/** 4-probe R(T) CSV, Meissner levitation MP4  
* **notebooks/** plots that regenerate key figures 