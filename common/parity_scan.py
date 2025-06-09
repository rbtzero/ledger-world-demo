#!/usr/bin/env python3
import sys, re, pathlib
VAL = {"B":3, "N":3, "C":4, "H":1}

def atoms_from_cif(path):
    pat = re.compile(r"^\s*([A-Z][a-z]?)\s+\w+\s+")
    atoms=[]
    for ln in open(path):
        m = pat.match(ln)
        if m:
            atoms.append(m.group(1))
    return atoms

def main():
    for p in map(pathlib.Path, sys.argv[1:]):
        atoms = atoms_from_cif(p)
        b_cnt = atoms.count("B")
        n_cnt = atoms.count("N")
        c_cnt = atoms.count("C")
        h_cnt = atoms.count("H")
        
        # Mathematical approach
        heavy_val = b_cnt*(VAL["B"]-2) + n_cnt*(VAL["N"]-2) + c_cnt*(VAL["C"]-2)
        hyd_val = h_cnt*(VAL["H"]-2)
        sigma0 = heavy_val + hyd_val
        bonds = sigma0 // 2
        
        final_sigma = heavy_val + hyd_val - 2*bonds
        
        print(f"DEBUG: Found B={b_cnt}, N={n_cnt}, C={c_cnt}, H={h_cnt}")
        print(f"Σ₀={sigma0}, bonds={bonds}")
        print(("✅" if final_sigma==0 else "❌"), p.name, f"Sigma={final_sigma}")

if __name__ == "__main__":
    main()
