import numpy as np
import matplotlib.pyplot as plt


def trajectory(x, theta, v0, g, y0):
    return x * np.tan(theta) - (1 / 2 * v0 ** 2) * (g * x ** 2 / (2 * np.cos(theta) ** 2)) + y0


def plot_trajectory(theta, v0, g, y0):
    x_values = np.linspace(0, 10, 100)  # Adjust the range as needed
    y_values = trajectory(x_values, theta, v0, g, y0)

    plt.plot(x_values, y_values)
    plt.title("Trajectory of a Ball")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Distance (m)")
    plt.grid(True)
    plt.show()


# Example usage
theta = np.deg2rad(45)  # Angle in radians
v0 = 10  # Initial velocity (m/s)
g = 9.81  # Acceleration due to gravity (m/s^2)
y0 = 0  # Initial height (m)

plot_trajectory(theta, v0, g, y0)
