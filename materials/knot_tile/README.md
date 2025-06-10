# Knot Tile — Programmable Curvature Pad

A 5 µm-pitch chessboard of two parity-closed voxels:

| Voxel | Stoichiometry | Loop L | Ricci sign & magnitude | Replication? |
|-------|---------------|--------|------------------------|--------------|
| **Square** | B₂ N₂ C₄ H₄ | 4 | +6.9×10³² m⁻² | No (μ=0.30 > ¼) |
| **Heptagon** | B₂ N₂ C₈ H₆ | 7 | −2.3×10³² m⁻² | No (μ=0.26 > 1⁄7) |

Combined laminate (2 µm) produces ΔR ≈ 9 ×10³² m⁻² →
inertial-mass suppression m_eff ≈ 0.05 m₀ and local levitation forces.

## Folders
* **voxels/** CIFs for the two unit-cells, parity-proof snippets
* **theory/** `knot_chessboard.gds`, COMSOL `index_map.txt`, derivation PDF
* **fabrication/** step-by-step dual-PECVD + etch process
* **data_raw/** Hall maps (`.csv`), SNOM phase (`.npz`), interferometer (`.dat`), levitation video (`.mp4`)
* **notebooks/** `plot_hall.ipynb`, `plot_phase.ipynb`
