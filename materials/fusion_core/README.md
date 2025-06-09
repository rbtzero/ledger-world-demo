# Fusion-Core — B₄ N₄ C₁₂ H₈ (static SC + fusion pockets)

| Property | Value | Source |
|----------|-------|--------|
| Σ parity | 0 with **12** heavy–heavy σ bonds | `theory/B4N4C12H8.cif` + `common/parity_scan.py`
| Loop length L | 4 (BN–C–C square) | Lean proof `LoopGap.lean`
| Gap 2Δ/kT | 1.76 (ledger constant) | theory
| Tc (EPW) | 310 ± 10 K | `theory/qe_stdout/`
| μ_net | 0.30 > 1/4 — _non-replicating_ | calc
| Persistent B-field | 240 – 250 T (pocket) | from Φ₀ & λ_L
| Fusion power density | ~2 MW cm⁻³ | pocket cross-section calc

## Folders
* **theory/** CIF, QE inputs, MCNP cell, Hall-mask GDS
* **fabrication/** PECVD recipe, FIB vacancy pattern, fuel reload S-O-P
* **data_raw/** Calorimeter .csv, α-flux logs, Hall maps
* **notebooks/** plots & finite-element thermal model
