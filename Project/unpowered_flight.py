import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
g = 9.81  # Gravitational constant (m/s^2)
k = 0.048  # Drag coefficient


# Function to calculate acceleration
def acceleration_function(v, t, angle_deg, mass):
    theta_rad = np.radians(angle_deg)  # Convert angle to radians

    # Constants
    drag_coefficient = 0.05
    air_density = 1.225  # Air density at sea level in kg/m^3
    cross_sectional_area = 2.0  # Cross-sectional area in m^2

    # Calculate drag force magnitude
    v_magnitude = np.sqrt(v[0] ** 2 + v[1] ** 2)
    drag_magnitude = 0.5 * drag_coefficient * air_density * cross_sectional_area * v_magnitude ** 2

    # Calculate drag force components
    drag_horizontal = -drag_magnitude * v[0] / v_magnitude
    drag_vertical = -drag_magnitude * v[1] / v_magnitude

    # Calculate acceleration components
    a_horizontal = drag_horizontal / mass
    a_vertical = -g + drag_vertical / mass

    return [a_horizontal, a_vertical]


# Main function
def main():
    try:
        # Prompt the user for input values
        initial_velocity = float(input("Enter the initial velocity (m/s) *should really use take off speed at minimum since putting in zero will break the calculations*: "))
        angle_of_attack = float(input("Enter the angle of attack (degrees): "))
        mass = float(input("Enter the mass of the craft (kg) ex: for the f-104 starfighter(template used for drag calculation) use a mass of 6350 kg for mass when its empty: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Time points for integration (0 to 100 seconds)
    t = np.linspace(0, 1000, 10000)

    # Initial conditions: horizontal and vertical velocities
    initial_conditions = [initial_velocity * np.cos(np.radians(angle_of_attack)),
                          initial_velocity * np.sin(np.radians(angle_of_attack))]

    # Integrate the differential equations
    v = odeint(acceleration_function, initial_conditions, t, args=(angle_of_attack, mass))

    # Extract horizontal and vertical velocities
    v_horizontal = v[:, 0]
    v_vertical = v[:, 1]

    # Calculate velocity magnitude
    v_magnitude = np.sqrt(v_horizontal ** 2 + v_vertical ** 2)

    # Integrate velocity to get position
    x = np.cumsum(v_horizontal) * (t[1] - t[0])  # Horizontal position
    y = np.cumsum(v_vertical) * (t[1] - t[0]) - 0.5 * g * t ** 2  # Vertical position

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
