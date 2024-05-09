"""
Author: Riley Palermo
"""

import numpy as np


# Function to fit a quadratic polynomial to the data and return the coefficients
def calculate_quadratic_fit(data: np.ndarray) -> np.ndarray:
    """
    Fits a quadratic polynomial to the provided data and returns the coefficients.
    :param data: np.ndarray: The data points to fit the quadratic polynomial.
    :return: np.ndarray: The coefficients of the fitted quadratic polynomial.
    """
    x_values = data[0]
    y_values = data[1]
    quadratic_coefficients = np.polyfit(x_values, y_values, 2)
    return quadratic_coefficients
