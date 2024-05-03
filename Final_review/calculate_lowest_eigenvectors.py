"""
Author: Riley Palermo
"""

import numpy as np


def calculate_lowest_eigenvectors(square_matrix: np.ndarray, number_of_eigenvectors: int = 3) -> (
        np.ndarray, np.ndarray):
    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
    sorted_indices = np.argsort(eigenvalues)
    lowest_eigenvalues = eigenvalues[sorted_indices][:number_of_eigenvectors]
    lowest_eigenvectors = eigenvectors[:, sorted_indices][:, :number_of_eigenvectors]

    return lowest_eigenvalues, lowest_eigenvectors


if __name__ == "__main__":
    # Test with square_matrix = np.array([[2, -1], [-1, 2]]) and number_of_eigenvectors = 2
    square_matrix = np.array([[2, -1], [-1, 2]])
    number_of_eigenvectors = 2

    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:", eigenvectors)
