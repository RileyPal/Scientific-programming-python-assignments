import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Gravitational constant (m/s^2)
k = 0.048  # Drag coefficient
lift_coefficient = 0.8  # Lift coefficient

data_table = {
    "Altitude (m)": [-1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000,
                      40000, 50000, 60000, 70000, 80000, 90000],
    "Density (kg/m^3)": [1.347, 1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5900, 0.5258, 0.4671, 0.4135,
                         0.1948, 0.08891, 0.04008, 0.01841, 0.003996, 0.001027, 0.0003097, 0.00008283, 0.00001846, 0.0]
}


def air_density_func(y):
    altitudes = data_table["Altitude (m)"]
    densities = data_table["Density (kg/m^3)"]
    return np.interp(y, altitudes, densities)

# Function to calculate thrust based on air density, velocity, and intake area

def thrust_function(air_density, velocity, intake_area):
    return ((((((0.2 * air_density * velocity * intake_area) / 4) + (0.2 * air_density * velocity * intake_area)) *
              ((50000000 * 0.7) * 300) * 9.81)))

def acceleration_function(t, state, angle_of_attack, mass, lifting_area, intake_area):
    v_horizontal, v_vertical = state[:2]  # Unpack state
    theta_rad = np.radians(angle_of_attack)  # Convert angle to radians

    air_density = air_density_func(state[2])  # Calculate air density at current altitude

    T = thrust_function(air_density, np.sqrt(v_horizontal**2 + v_vertical**2), intake_area)  # Calculate thrust

    drag_coefficient = 0.25
    cross_sectional_area = 249

    v_magnitude = np.sqrt(v_horizontal**2 + v_vertical**2)  # Calculate velocity magnitude
    drag_magnitude = 0.5 * drag_coefficient * air_density * cross_sectional_area * v_magnitude ** 2  # Drag force
    lift_magnitude = lift_coefficient * air_density * lifting_area * v_magnitude ** 2 * np.sin(theta_rad)  # Lift force

    # Calculate forces components
    drag_horizontal = -np.sign(v_horizontal) * drag_magnitude * np.cos(theta_rad)
    drag_vertical = -np.sign(v_vertical) * drag_magnitude * np.sin(theta_rad)
    lift_vertical = lift_magnitude * np.cos(theta_rad)
    lift_horizontal = -lift_magnitude * np.sin(theta_rad)

    # Calculate thrust components
    T_horizontal = T * np.cos(theta_rad)
    T_vertical = T * np.sin(theta_rad)

    # Calculate acceleration components
    a_horizontal = (drag_horizontal + lift_horizontal + T_horizontal) / mass
    a_vertical = (-g + drag_vertical + lift_vertical + T_vertical) / mass

    # Return derivatives of velocity in both directions
    return [a_horizontal, a_vertical, v_horizontal, v_vertical]

def main():
    while True:
        try:
            velocity_mag = float(input("Enter the velocity magnitude (m/s): "))
            angle_of_attack = float(input("Enter the angle of attack (degrees): "))
            mass = float(input("Enter the mass of the craft (kg): "))
            lifting_area = float(input("Enter the lifting area (m^2): "))
            intake_area = float(input("Enter the intake area (m^2): "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        v_horizontal = velocity_mag * np.cos(np.radians(angle_of_attack))
        v_vertical = velocity_mag * np.sin(np.radians(angle_of_attack))

        state_initial = [v_horizontal, v_vertical, 0.0]

        t_span = [0, 10]

        sol = solve_ivp(
            lambda t, state: acceleration_function(t, state, angle_of_attack, mass, lifting_area, intake_area),
            t_span,
            state_initial,
            method='RK45',
            t_eval=np.linspace(t_span[0], t_span[1], 1000))

        v_values = sol.y[2:4]
        acceleration_values = np.array([acceleration_function(t, sol.y[:, i], angle_of_attack, mass, lifting_area, intake_area) for i, t in enumerate(sol.t)])

        plt.figure(figsize=(12, 8))

        plt.subplot(2, 2, 1)
        plt.plot(sol.t, v_values[0], label='Horizontal Velocity')
        plt.xlabel('Time (s)')
        plt.ylabel('Horizontal Velocity (m/s)')
        plt.title('Horizontal Velocity vs Time')
        plt.grid(True)
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(sol.t, v_values[1], label='Vertical Velocity')
        plt.xlabel('Time (s)')
        plt.ylabel('Vertical Velocity (m/s)')
        plt.title('Vertical Velocity vs Time')
        plt.grid(True)
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.plot(sol.t, acceleration_values[:, 0], label='Horizontal Acceleration', color='blue')
        plt.xlabel('Time (s)')
        plt.ylabel('Horizontal Acceleration (m/s^2)')
        plt.title('Horizontal Acceleration vs Time')
        plt.grid(True)
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.plot(sol.t, acceleration_values[:, 1], label='Vertical Acceleration', color='green')
        plt.xlabel('Time (s)')
        plt.ylabel('Vertical Acceleration (m/s^2)')
        plt.title('Vertical Acceleration vs Time')
        plt.grid(True)
        plt.legend()

        plt.tight_layout()
        plt.show()

        # Ask the user if they want to continue or exit
        choice = input("Do you want to input another set of parameters? (yes/no): ").lower()
        if choice != 'yes':
            break


# Execute the main function
if __name__ == "__main__":
    main()
