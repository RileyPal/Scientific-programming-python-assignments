"""
Author: Riley Palermo
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_data_with_fit(data: np.ndarray, fit_curve: np.ndarray, data_format: str = 'x', fit_format: str = '-') -> list:
    data_plot = plt.plot(data[0], data[1], data_format)
    fit_plot = plt.plot(fit_curve[0], fit_curve[1], fit_format)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Data and Fit Curve')
    plt.legend(['Data', 'Fit Curve'])
    return data_plot + fit_plot


if __name__ == "__main__":
    # Test with data and fit_curve
    data = np.array([[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
    fit_curve = np.array([np.linspace(-2, 2), np.linspace(-2, 2) ** 2])

    combined_plot = plot_data_with_fit(data, fit_curve, data_format='x', fit_format='--')
    plt.show()
