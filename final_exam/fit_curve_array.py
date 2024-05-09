"""
Author: Riley Palermo
"""

import numpy as np


def fit_curve_array(quadratic_coefficients: np.ndarray, minimum_x: float, maximum_x: float,
                    number_of_points: int = 100) -> np.ndarray:
    if maximum_x < minimum_x:
        raise ArithmeticError("maximum_x should be greater than or equal to minimum_x")
    if number_of_points <= 2:
        raise IndexError("number_of_points should be greater than 2")

    x_values = np.linspace(minimum_x, maximum_x, number_of_points)
    y_values = np.polynomial.polynomial.polyval(x_values, quadratic_coefficients)

    return np.array([x_values, y_values])


if __name__ == "__main__":
    # Test with quadratic coefficients of [0, 0, 1], minimum x-value of -2, and maximum x-value of 2
    quadratic_coefficients = np.array([1, 0, 0])
    minimum_x = -2
    maximum_x = 2

    try:
        fit_curve = fit_curve_array(quadratic_coefficients, minimum_x, maximum_x)
        print("Fit curve:")
        print(fit_curve)
    except (ArithmeticError, IndexError) as e:
        print(e)
