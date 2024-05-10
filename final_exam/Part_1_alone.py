# Riley_Palermo_PHYS241FinalScript_Part1.py

"""
Author: Riley Palermo
"""
import sys

import numpy as np
import matplotlib.pyplot as plt
import datetime

from read_two_columns_text import read_two_columns_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratics_fit import calculate_quadratic_fit
from equation_of_state import fit_eos
from convert_units import convert_units
from annotate_plot import annotate_plot


# Function to parse file name and extract chemical symbol, crystal symmetry symbol, and approximation acronym
def parse_file_name(filename):
    global chemical_symbol
    try:
        split_filename = str.split(filename, '.')
        chemical_symbol = split_filename[0]
        crystal_symmetry_symbol = split_filename[1]
        density_functional_exchange_acronym = split_filename[2]
    except TypeError:
        print("Please input valid filename as string")
        sys.exit(1)
    except IndexError:
        print("Please input valid filename (separated by '.'s) as string")
        sys.exit(1)
    return chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym



# Main function to perform the tasks for part 1
def main():
    # Extract information from file name
    file_name = "Si.Fd-3m.GGA-PBEsol.volumes_energies.dat"
    chemical_symbol, crystal_symmetry, approximation_acronym = parse_file_name(file_name)

    # Read data
    data = read_two_columns_text(file_name)

    # Calculate statistics
    statistics = calculate_bivariate_statistics(data)

    # Fit a quadratic polynomial to the data
    quadratic_coefficients = calculate_quadratic_fit(data)

    # Fit EOS
    eos_fit = fit_eos(data[0], data[1], quadratic_coefficients)

    # Check if the fit was successful
    if len(eos_fit) >= 3:
        # Convert units
        converted_volume = convert_units(eos_fit[0], 'bohr3/atom', 'Angstrom3/atom')
        converted_energy = convert_units(eos_fit[1], 'rydberg/atom', 'eV/atom')
        converted_bulk_modulus = convert_units(eos_fit[2], 'rydberg/bohr3', 'GPa')

        # Plot data and fit function
        plt.figure()
        plt.plot(data[0], data[1], 'bo')  # Data points
        plt.plot(converted_volume, converted_energy, 'k-')  # Fit curve
        plt.xlabel(r'Volume ($\AA^3$/atom)')
        plt.ylabel(r'Energy (eV/atom)')
        plt.title(f'{approximation_acronym} Equation of State for {chemical_symbol} in DFT ({crystal_symmetry})')
        annotate_plot({
            chemical_symbol: {'position': (0.1, 0.9), 'alignment': ['left', 'top'], 'fontsize': 12},
            crystal_symmetry: {'position': (np.mean(converted_volume), np.min(converted_energy) + 0.1),
                               'alignment': ['center', 'bottom'], 'fontsize': 10},
            f'Bulk Modulus: {converted_bulk_modulus:.1f} GPa': {
                'position': (np.mean(converted_volume), np.min(converted_energy) + 0.2),
                'alignment': ['center', 'bottom'],
                'fontsize': 10},
            f'Equilibrium Volume: {np.min(converted_volume):.2f} Å^3/atom': {
                'position': (np.min(converted_volume), np.min(converted_energy) + 0.5), 'alignment': ['left', 'bottom'],
                'fontsize': 10},
            f'Created by Riley {datetime.date.today().isoformat()}': {
                'position': (np.min(converted_volume), np.min(converted_energy)), 'alignment': ['left', 'bottom'],
                'fontsize': 8}
        })

        # Display or save plots based on the display_graph flag
        display_graph = True
        if display_graph:
            plt.show()
        else:
            plt.savefig(f'{chemical_symbol}_{crystal_symmetry}_Equation_of_State.png')
            plt.close()
    else:
        print("Fit was unsuccessful. Unable to convert units and plot.")

if __name__ == "__main__":
    main()
