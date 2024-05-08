"""
Author: Riley Palermo
"""

import numpy as np


def calculate_quadratic_fit(data: np.ndarray) -> np.ndarray:
    if data.shape[0] != 2:
        raise IndexError("Data array should have two rows")

    x = data[0]
    y = data[1]

    quadratic_coefficients = np.polyfit(x, y, 2)

    return quadratic_coefficients


if __name__ == "__main__":
    # Test with data y = x^2
    data = np.array([np.linspace(-1, 1), np.linspace(-1, 1) ** 2])

    try:
        coefficients = calculate_quadratic_fit(data)
        print("Quadratic polynomial coefficients:", coefficients)
    except IndexError as e:
        print(e)
