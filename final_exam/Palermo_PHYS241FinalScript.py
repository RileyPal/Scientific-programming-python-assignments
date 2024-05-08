# Riley_Palermo_PHYS241FinalScript.py

"""
Author: Riley Palermo
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime

from read_two_columns_text import read_two_columns_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratics_fit import calculate_quadratic_fit
from equation_of_state import fit_eos
from convert_units import convert_units
from annotate_plot import annotate_plot
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from generate_matrix import generate_matrix


# Function to parse file name and extract chemical symbol, crystal symmetry symbol, and approximation acronym
def parse_file_name(file_name):
    """
    Extracts the chemical symbol, crystal symmetry symbol, and density functional exchange-correlation approximation
    acronym from the given file name.
    :param file_name: str: The name of the file containing the data.
    :return: tuple: A tuple containing the extracted strings.
    """
    # Split the file name into components using underscores as delimiters
    components = file_name.split('_')

    # Check if the components list has enough elements
    if len(components) < 3:
        raise ValueError("Invalid file name format. Unable to extract required components.")

    # Extract the chemical symbol
    chemical_symbol = components[0]

    # Extract the crystal symmetry symbol
    crystal_symmetry = components[1]

    # Extract the approximation acronym
    approximation_acronym = components[2]

    return chemical_symbol, crystal_symmetry, approximation_acronym


# Main function to perform the tasks
def main():
    # Part 1: Fit an Equation of State
    file_name = "chemical_symbol_crystal_symmetry_approximation_acronym.dat"
    chemical_symbol, crystal_symmetry, approximation_acronym = parse_file_name(file_name)

    # Read data
    data = read_two_columns_text(file_name)

    # Divide by number of atoms if needed
    # data /= 2  # Uncomment this line if needed

    # Calculate statistics
    statistics = calculate_bivariate_statistics(data)

    # Fit a quadratic polynomial to the data
    quadratic_coefficients = calculate_quadratic_fit(data)

    # Fit EOS
    eos_fit = fit_eos(data[0], data[1], quadratic_coefficients)

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
            'position': (np.mean(converted_volume), np.min(converted_energy) + 0.2), 'alignment': ['center', 'bottom'],
            'fontsize': 10},
        f'Equilibrium Volume: {np.min(converted_volume):.2f} Å^3/atom': {
            'position': (np.min(converted_volume), np.min(converted_energy) + 0.5), 'alignment': ['left', 'bottom'],
            'fontsize': 10},
        f'Created by Riley {datetime.date.today().isoformat()}': {
            'position': (np.min(converted_volume), np.min(converted_energy)), 'alignment': ['left', 'bottom'],
            'fontsize': 8}
    })

    # Part 2: Visualize Vectors in Space
    Ndim = 100  # Number of grid points
    matrix_parameters = (Ndim, 2, 2)  # Update with your matrix parameters
    matrix = generate_matrix(*matrix_parameters)

    # Calculate lowest eigenvectors and eigenvalues
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(matrix, 3)

    # Generate grid of spatial points
    grid_points = np.linspace(-10, 10, Ndim)

    # Plot eigenvectors against the grid
    plt.figure()
    for i in range(3):
        eigenvector = eigenvectors[i]
        if eigenvector[0] < 0:
            eigenvector *= -1
        plt.plot(grid_points, eigenvector, label=f'ψ{i + 1}, E{i + 1} = {eigenvalues[i]:.3f} a.u.')
    plt.plot(grid_points, np.zeros_like(grid_points), 'k-')  # Horizontal line at y=0
    plt.xlabel('x [a.u.]')
    plt.ylabel('ψ [a.u.]')
    plt.title(f'Select Wavefunctions for a {crystal_symmetry} Potential on a Spatial Grid of {Ndim} Points')
    plt.legend()
    annotate_plot({f'Created by Riley {datetime.date.today().isoformat()}': {'position': (-10, -1.5),
                                                                             'alignment': ['left',
                                                                                           'bottom'],
                                                                             'fontsize': 8}})

    # Display or save plots based on the display_graph flag
    if display_graph:
        plt.show()
    else:
        plt.savefig(f'{chemical_symbol}_{crystal_symmetry}_{Ndim}_Eigenvectors.png')
        plt.close()


# Boolean flag to display or save plots
display_graph = True

if __name__ == "__main__":
    main()
