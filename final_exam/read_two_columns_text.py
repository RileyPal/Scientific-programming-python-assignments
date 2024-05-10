"""
Author: Riley Palermo
"""

import numpy as np


def read_two_columns_text(chemical_symbol_crystal_symmetry_approximation_acronym: str) -> np.ndarray:
    try:
        data = np.loadtxt(chemical_symbol_crystal_symmetry_approximation_acronym, dtype=float).T
        if data.shape[0] != 2:
            raise ValueError("File should contain exactly two columns")
        return data
    except OSError:
        raise OSError("File not found for reading")


if __name__ == "__main__":
    filename = "Si.Fd-3m.GGA-PBEsol.volumes_energies.dat"
    try:
        data = read_two_columns_text(filename)
        print(f"{data=}, shape={data.shape}")
    except OSError as e:
        print(e)
