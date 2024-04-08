import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Gravitational constant (m/s^2)
k = 0.048  # Drag coefficient
lift_coefficient = 0.8  # Lift coefficient

data_table = {
    "Altitude (m)": [-1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000,
                      40000, 50000, 60000, 70000, 80000],
    "Density (kg/m^3)": [1.347, 1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5900, 0.5258, 0.4671, 0.4135,
                         0.1948, 0.08891, 0.04008, 0.01841, 0.003996, 0.001027, 0.0003097, 0.00008283, 0.00001846]
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


# Function to calculate thrust based on air density, velocity, and intake area
def thrust_function(air_density, velocity, intake_area):
    # Assuming methane is fuel being used with and energy density of 50 MJ/kg of fuel only 70% is usable
    # For clarity know that methane requires 4 kg of oxygen for every kg of fuel and has an Isp of 300 seconds
    # Theoretical max thrust/kg of fuel calculation in the form of (mass flow rate*energy density*Isp)*g
    # You may replace this with an appropriate model for your application
    return (((((0.2 * air_density * velocity * intake_area) / 4) * ((50000000*.7) * 300) * 9.81)))


# Function to calculate acceleration
def acceleration_function(t, state, angle_of_attack, mass, lifting_area, intake_area):
    v, y = state  # Unpack state
    theta_rad = np.radians(angle_of_attack)  # Convert angle to radians

    # Calculate air density at current altitude
    air_density = air_density_func(y)

    # Calculate thrust based on air density, velocity, and intake area
    T = thrust_function(air_density, v, intake_area)

    # Constants
    drag_coefficient = 0.05
    cross_sectional_area = lifting_area  # Cross-sectional area in m^2

    # Calculate drag force magnitude
    v_magnitude = np.abs(v)
    drag_magnitude = 0.5 * drag_coefficient * air_density * cross_sectional_area * v_magnitude ** 2

    # Calculate lift force magnitude
    lift_magnitude = lift_coefficient * air_density * lifting_area * v_magnitude ** 2 * np.sin(theta_rad)

    # Calculate drag force components
    drag_vertical = -np.sign(v) * drag_magnitude

    # Calculate lift force components
    lift_vertical = lift_magnitude * np.cos(theta_rad)

    # Calculate thrust components
    T_vertical = T * np.sin(theta_rad)

    # Calculate acceleration components
    a_vertical = (-g + drag_vertical + lift_vertical + T_vertical) / mass

    return [a_vertical, v]  # Return [acceleration, velocity]


# Main function
def main():
    while True:
        try:
            # Prompt the user for input values
            initial_velocity = float(input("Enter the initial velocity (m/s) for f104 use 100 m/s: "))
            angle_of_attack = float(input("Enter the angle of attack (degrees): "))
            mass = float(input(
                "Enter the mass of the craft (kg) ex: for the f-104 starfighter(template used for drag calculation) use a mass of 6350 kg for mass when its empty: "))
            lifting_area = float(input("Enter the lifting area (m^2) ex: f104 starfighter had a lifting area of 18.2 m^2: "))
            intake_area = float(input("Enter the intake area (m^2) *realistically should be somewhere between 0.1-0.5 based on nasas xf43 experimental ramjet craft but is purely an estimate* : "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Define initial vertical position
        y_initial = 0.0  # Assume starting from sea level

        # Define initial state
        state_initial = [initial_velocity, y_initial]

        # Time span for integration (0 to 100 seconds)
        t_span = [0, 100]

        # Solve the ODE
        sol = solve_ivp(lambda t, state: acceleration_function(t, state, angle_of_attack, mass, lifting_area, intake_area),
                        t_span,
                        state_initial,
                        method='RK45',
                        t_eval=np.linspace(t_span[0], t_span[1], 1000))

        # Extract velocity and position from solution
        v_values = sol.y[0]
        y_values = sol.y[1]

        # Calculate horizontal and vertical components
        v_horizontal = v_values
        v_vertical = np.gradient(y_values, sol.t)

        # Plot the velocity and position graphs
        plt.figure(figsize=(12, 8))

        # Velocity plots
        plt.subplot(2, 2, 1)
        plt.plot(sol.t, v_horizontal, label='Horizontal Velocity')
        plt.xlabel('Time (s)')
        plt.ylabel('Horizontal Velocity (m/s)')
        plt.title('Horizontal Velocity vs Time')
        plt.axhline(y=7672, color='purple', linestyle='--', label='Horizontal Velocity 7672 m/s')
        plt.grid(True)
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(sol.t, v_vertical, label='Vertical Velocity', color='orange')
        plt.xlabel('Time (s)')
        plt.ylabel('Vertical Velocity (m/s)')
        plt.title('Vertical Velocity vs Time')
        plt.grid(True)
        plt.legend()

        # Position plots
        plt.subplot(2, 2, 3)
        plt.plot(sol.t, v_horizontal * sol.t, label='Horizontal Position', color='green')
        plt.xlabel('Time (s)')
        plt.ylabel('Horizontal Position (m)')
        plt.title('Horizontal Position vs Time')
        plt.grid(True)
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.plot(sol.t, y_values, label='Vertical Position', color='red')
        plt.xlabel('Time (s)')
        plt.ylabel('Vertical Position (m)')
        plt.title('Vertical Position vs Time')

        # Add indicators for reaching 400,000 m and 7,672 m/s horizontal velocity
        plt.axhline(y=400000, color='blue', linestyle='--', label='Altitude 400,000m')

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
