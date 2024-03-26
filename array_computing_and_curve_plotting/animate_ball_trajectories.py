import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

def x(t, v0, theta):
    return v0 * np.cos(theta * t)

def y(t, v0, theta):
    return v0 * np.sin(theta * t) - 0.5 * g * t**2

def time_of_flight(v0, theta):
    return (2 * v0 * np.sin(theta)**2) / g

def max_height(v0, theta):
    return (v0**2 * np.sin(theta)**2) / (2 * g)

def animate_trajectory(v0, theta, y0):
    fig, ax = plt.subplots()
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Distance (m)")

    # Set the range of the plot axes
    ax.set_xlim(0, 25)  # Adjust as needed
    ax.set_ylim(0, 12)  # Adjust as needed

    # Initialize lines
    lines = []
    for i in range(len(v0)):
        line, = ax.plot([], [], label=f"v0={v0[i]}, theta={np.degrees(theta[i])}", lw=2)
        lines.append(line)

    ax.legend(loc="upper right")

    # Calculate maximum time
    max_time = max([time_of_flight(v0_val, theta_val) for v0_val, theta_val in zip(v0, theta)])

    # Continuously update the plot
    while True:
        for t in np.linspace(0, max_time, 400):  # Increase the number of frames
            for i in range(len(v0)):
                x_vals = x(t, v0[i], theta[i])
                y_vals = y(t, v0[i], theta[i]) + y0

                # Ensure x_vals and y_vals are arrays
                x_vals = np.array([x_vals]) if np.isscalar(x_vals) else x_vals
                y_vals = np.array([y_vals]) if np.isscalar(y_vals) else y_vals

                mask = y_vals >= 0
                x_vals = np.where(mask, x_vals, np.nan)  # Set invalid values to NaN
                y_vals = np.where(mask, y_vals, np.nan)  # Set invalid values to NaN

                lines[i].set_data(x_vals, y_vals)

                # Mark maximum height with dashed line
                max_h = max_height(v0[i], theta[i])
                for y0_val in y0:
                    ax.axhline(y=max_h + y0_val, linestyle='--', color=lines[i].get_color())  # Iterate over y0 values

            plt.pause(0.01)  # Pause to display the plot
            plt.draw()  # Draw the plot

# Initial conditions
initial_conditions = {
    "v0": [10, 15, 20],  # Initial velocity (m/s)
    "theta": [np.pi/4, np.pi/3, np.pi/6],  # Launch angle (radians)
    "y0": [0, 5, 10]  # Initial height (m)
}

# Simulate trajectories
animate_trajectory(initial_conditions["v0"], initial_conditions["theta"], initial_conditions["y0"])