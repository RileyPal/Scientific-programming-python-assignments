import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
g = 9.81  # Gravitational constant (m/s^2)
k = 0.048  # Drag coefficient
lift_coefficient = 0.8  # Lift coefficient

data_table = {
    "Altitude (m)": [-1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000, 80000],
    "Density (kg/m^3)": [1.347, 1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5900, 0.5258, 0.4671, 0.4135, 0.1948, 0.08891, 0.04008, 0.01841, 0.003996, 0.001027, 0.0003097, 0.00008283, 0.00001846]
}


def air_density_func(y):
    # Retrieve altitude and density data from the data table
    altitudes = data_table["Altitude (m)"]
    densities = data_table["Density (kg/m^3)"]

    # Find the index of the altitude closest to the current altitude y
    index = min(range(len(altitudes)), key=lambda i: abs(altitudes[i] - y))

    # Return the density corresponding to the nearest altitude
    rho = densities[index]
    return rho

# Function to calculate acceleration
def acceleration_function(v, t, angle_deg, mass, T, y, lifting_area):
    theta_rad = np.radians(angle_deg)  # Convert angle to radians

    # Constants
    drag_coefficient = 0.05
    air_density = air_density_func(y)  # Call air_density_func with current altitude
    cross_sectional_area = lifting_area  # Cross-sectional area in m^2

    # Calculate drag force magnitude
    v_magnitude = np.sqrt(v[0] ** 2 + v[1] ** 2)
    drag_magnitude = 0.5 * drag_coefficient * air_density * cross_sectional_area * v_magnitude ** 2

    # Calculate lift force magnitude
    lift_magnitude = lift_coefficient * air_density * lifting_area * v_magnitude ** 2 * np.sin(theta_rad)

    # Calculate thrust magnitude
    T_magnitude = T

    # Calculate drag force components
    drag_horizontal = -drag_magnitude * v[0] / v_magnitude
    drag_vertical = -drag_magnitude * v[1] / v_magnitude

    # Calculate lift force components
    lift_horizontal = lift_magnitude * np.sin(theta_rad)
    lift_vertical = lift_magnitude * np.cos(theta_rad)

    # Calculate thrust components
    T_horizontal = T_magnitude * np.cos(theta_rad)
    T_vertical = T_magnitude * np.sin(theta_rad)

    # Calculate acceleration components
    a_horizontal = (drag_horizontal + lift_horizontal + T_horizontal) / mass
    a_vertical = (-g + drag_vertical + lift_vertical + T_vertical) / mass

    return [a_horizontal, a_vertical]




# Main function
def main():
    try:
        # Prompt the user for input values
        initial_velocity = float(input("Enter the initial velocity (m/s) for f104 use 100 m/s: "))
        T = float(input(
            "Enter the max thrust of engine (N) ex: J79 afterburner turbojet is 79600 N while afterburner is on: "))
        angle_of_attack = float(input("Enter the angle of attack (degrees): "))
        mass = float(input(
            "Enter the mass of the craft (kg) ex: for the f-104 starfighter(template used for drag calculation) use a mass of 6350 kg for mass when its empty: "))
        lifting_area = float(input("Enter the lifting area (m^2) ex: f104 starfighter had a lifting area of 18.2 m^2: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Time points for integration (0 to 100 seconds)
    t = np.linspace(0, 1000, 10000)

    # Define initial vertical position
    y = 0.0  # Assume starting from sea level

    # Initial conditions: horizontal and vertical velocities
    initial_conditions = [initial_velocity * np.cos(np.radians(angle_of_attack)),
                          initial_velocity * np.sin(np.radians(angle_of_attack))]

    # Integrate the differential equations
    v = odeint(lambda v, t: acceleration_function(v, t, angle_of_attack, mass, T, y, lifting_area), initial_conditions,
               t)

    # Extract horizontal and vertical velocities
    v_horizontal = v[:, 0]
    v_vertical = v[:, 1]

    # Calculate velocity magnitude
    v_magnitude = np.sqrt(v_horizontal ** 2 + v_vertical ** 2)

    # Integrate velocity to get position
    x = np.cumsum(v_horizontal) * (t[1] - t[0])  # Horizontal position
    y = np.cumsum(v_vertical) * (t[1] - t[0])  # Vertical position

    # Plot the velocity and position graphs
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(t, v_horizontal, label='Horizontal Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Horizontal Velocity (m/s)')
    plt.title('Horizontal Velocity vs Time')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(t, v_vertical, label='Vertical Velocity', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Vertical Velocity (m/s)')
    plt.title('Vertical Velocity vs Time')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(t, x, label='Horizontal Position', color='green')
    plt.xlabel('Time (s)')
    plt.ylabel('Horizontal Position (m)')
    plt.title('Horizontal Position vs Time')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(t, y, label='Vertical Position', color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Vertical Position (m)')
    plt.title('Vertical Position vs Time')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


# Execute the main function
if __name__ == "__main__":
    main()
