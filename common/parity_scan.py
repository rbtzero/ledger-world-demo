#!/usr/bin/env python3
"""
Parity check: ensures Σ = 0 for every CIF passed on the command-line.
"""
import sys, re, pathlib
VAL = {'B':3, 'N':3, 'C':4, 'H':1}

def atoms_from_cif(path):
    pat = re.compile(r'^\s*([A-Z][a-z]?)\s+\w+\s+')
    atoms=[]
    for ln in open(path):
        m = pat.match(ln);  atoms.append(m.group(1)) if m else None
    return atoms

def sigma(atoms, bonds):
    heavy = sum(VAL[a]-2 for a in atoms if a!='H')
    hyd   = sum(VAL['H']-2 for a in atoms if a=='H')
    return heavy+hyd - 2*bonds

def main():
    ok=True
    for p in map(pathlib.Path, sys.argv[1:]):
        atoms = atoms_from_cif(p)
        bonds = len([a for a in atoms if a!='H']) - 1
        s = sigma(atoms,bonds)
        print(('✅' if s==0 else '❌'), p.name, f'Sigma={s}')
        ok &= (s==0)
    sys.exit(0 if ok else 1)

if __name__ == '__main__':
    if len(sys.argv)==1:
        print("usage: parity_scan.py *.cif"); sys.exit(1)
    main() 