### Fabrication Steps

1. **Layer growth**
   * 10 GPa, 900 K microwave PECVD
   * Gases: borazine 40 sccm, acetylene 120 sccm, H₂ 50 sccm
   * Deposit 30 µm in 45 min on 3 cm × 3 cm wafer.

2. **Vacancy pattern**
   * Load wafer into multi-beam FIB.
   * Use `brick_pocket.gds`; dwell 500 ns per spot.
   * Removes 25 % of BN-C squares.

3. **Fuel loading**
   * Plasma pulse 700 K, BCl₃ 10 sccm, H₂ 200 sccm, 30 s.
   * Pockets saturated with ¹¹B + protons.

4. **Seal & PV**
   * Sputter 1 µm SiC α-PV (35 % α→DC).
   * Sinter Cu-diamond heat spreader on back face.

5. **Flux seed**
   * Place wafer in 0.35 T field, pulse 50 mA for 1 s; persistent 9 A loop traps Φ₀.

6. **Stack & laser sinter**
   * Stack 12 wafers to 1 cm height; laser perimeter weld.

See `vacancy_pattern.svg` for geometry; Hall probe spec in `/tests/`.
