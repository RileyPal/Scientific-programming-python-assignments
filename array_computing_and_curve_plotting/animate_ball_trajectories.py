import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

def x(t, v0, theta):
    return v0 * np.cos(theta * t)

def y(t, v0, theta):
    return v0 * np.sin(theta * t) - 0.5 * g * t**2

def time_of_flight(v0, theta):
    v0 = np.array(v0)
    theta = np.array(theta)
    return (2 * v0 * np.sin(theta)**2) / g

def max_height(v0, theta):
    return (v0**2 * np.sin(theta)**2) / (2 * g)

def animate_trajectory(v0, theta, y0):
    fig, ax = plt.subplots()
    ax.set_xlabel("Horizontal Distance (m)")
    ax.set_ylabel("Vertical Distance (m)")

    lines = []
    for i in range(len(v0)):
        t_flight = time_of_flight(v0[i], theta[i])
        max_h = max_height(v0[i], theta[i])

        line, = ax.plot([], [], label=f"v0={v0[i]}, theta={np.degrees(theta[i])}", lw=2)
        lines.append(line)

        ax.legend(loc="upper right")

    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    def update(frame):
        for i in range(len(v0)):
            t = np.linspace(0, frame, 100)
            x_vals = x(t, v0[i], theta[i])
            y_vals = y(t, v0[i], theta[i]) + y0
            mask = y_vals >= 0
            lines[i].set_data(x_vals[mask], y_vals[mask])
            ax.axhline(y=max_h + y0, linestyle='--', color=lines[i].get_color())
        return lines

    ani = FuncAnimation(fig, update, frames=np.linspace(0, max(time_of_flight(v0, theta)), 200), init_func=init, blit=True)
    plt.grid(True)
    plt.show()

# Initial conditions
initial_conditions = {
    "v0": [10, 15, 20],  # Initial velocity (m/s)
    "theta": [np.pi/4, np.pi/3, np.pi/6],  # Launch angle (radians)
    "y0": [0, 5, 10]  # Initial height (m)
}

# Simulate trajectories
animate_trajectory(initial_conditions["v0"], initial_conditions["theta"], initial_conditions["y0"])