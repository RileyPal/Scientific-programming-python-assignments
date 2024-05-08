"""
Author: Riley Palermo
"""

import numpy as np
from scipy import stats


def calculate_bivariate_statistics(data: np.ndarray) -> np.ndarray:
    if data.shape[0] != 2 or data.shape[1] <= 1:
        raise IndexError("Data array has inappropriate dimensions")

    mean_y = np.mean(data[1])
    std_y = np.std(data[1])
    min_x = np.min(data[0])
    max_x = np.max(data[0])
    min_y = np.min(data[1])
    max_y = np.max(data[1])

    return np.array([mean_y, std_y, min_x, max_x, min_y, max_y])


if __name__ == "__main__":
    # Test with a sample data set where y = x^2
    x_values = np.linspace(-10, 10, 100)
    y_values = x_values ** 2
    data = np.array([x_values, y_values])

    try:
        data = np.loadtxt("volumes_energies.dat").T
        statistics = calculate_bivariate_statistics(data)
        print("Statistics for volumes_energies.dat:")
        print("Mean of y:", statistics[0])
        print("Standard deviation of y:", statistics[1])
        print("Minimum x-value:", statistics[2])
        print("Maximum x-value:", statistics[3])
        print("Minimum y-value:", statistics[4])
        print("Maximum y-value:", statistics[5])
        print(stats.describe(statistics))
        print(stats.describe(data))
    except IndexError as e:
        print(e)
