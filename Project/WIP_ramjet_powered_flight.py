import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
g = 9.81  # Gravitational constant (m/s^2)
lift_coefficient = 0.8  # Lift coefficient

data_table = {
    "Altitude (m)": [-1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000,
                      40000, 50000, 60000, 70000, 80000, 90000],
    "Density (kg/m^3)": [1.347, 1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5900, 0.5258, 0.4671, 0.4135,
                         0.1948, 0.08891, 0.04008, 0.01841, 0.003996, 0.001027, 0.0003097, 0.00008283, 0.00001846, 0.0]
}


def air_density_func(y):
    # Retrieve altitude and density data from the data table
    altitudes = data_table["Altitude (m)"]
    densities = data_table["Density (kg/m^3)"]
    # Interpolate air density based on altitude
    return np.interp(y, altitudes, densities)



# Function to calculate thrust based on air density, velocity, and intake area
def thrust_function(air_density, velocity, intake_area):
    # For clarity know that methane has an Isp of 300 seconds
    # Theoretical max thrust/kg of fuel calculation in the form of (mass flow rate*energy density*Isp)*g
    # You may replace this with an appropriate model for your application
    return  (air_density * velocity * intake_area + (0.2 * air_density * velocity * intake_area *15.625/19.625)) * ((300 * 9.81) - velocity)



# Function to calculate acceleration
def acceleration_function(t, state, angle_of_attack, mass, lifting_area, intake_area):
    v, y = state  # Unpack state
    theta_rad = np.radians(angle_of_attack)  # Convert angle to radians

    # Calculate air density at current altitude
    air_density = air_density_func(y)

    # Calculate thrust based on air density, velocity, and intake area
    T = thrust_function(air_density, v, intake_area)

    # Constants
    drag_coefficient = 0.25
    cross_sectional_area = 249

    # Calculate drag force magnitude
    v_magnitude = np.abs(v)
    drag_magnitude = 0.5 * drag_coefficient * air_density * cross_sectional_area * v_magnitude ** 2

    # Calculate lift force magnitude
    lift_magnitude = lift_coefficient * air_density * lifting_area * v_magnitude ** 2 * np.sin(theta_rad)

    # Calculate drag force components
    drag_horizontal = -np.sign(v) * drag_magnitude * np.cos(theta_rad)
    drag_vertical = -np.sign(v) * drag_magnitude  * np.sin(theta_rad)

    # Calculate lift force components
    lift_vertical = lift_magnitude * np.cos(theta_rad)
    lift_horizontal = lift_magnitude * -np.sin(theta_rad)

    # Calculate thrust components
    T_vertical = T * np.sin(theta_rad)
    T_horizontal = T * np.cos(theta_rad)

    # Calculate acceleration components
    a_vertical = (-g + drag_vertical + lift_vertical + T_vertical) / mass
    a_horizontal = (drag_horizontal + lift_horizontal + T_horizontal) / mass

    return [a_horizontal, a_vertical]  # Return [horizontal acceleration, vertical acceleration]


# Main function
def main():
    while True:
        try:
            # Prompt the user for input values
            velocity_mag = float(input("Enter the velocity magnitude (m/s) for f104 use 100 m/s: "))
            angle_of_attack = float(input("Enter the angle of attack (degrees): "))
            mass = float(input(
                "Enter the mass of the craft (kg) ex: for Nasa's space shuttle (template used for drag calculation) use a mass of 70000 kg for mass when its carrying 2 tons of load: "))
            lifting_area = float(input("Enter the lifting area (m^2) ex: f104 starfighter had a lifting area of 18.2 m^2 *should presumably be small since we are trying to get out of the atmosphere*: "))
            intake_area = float(input("Enter the intake area (m^2) *realistically should be somewhere between 0.1-0.5 based on nasas xf43 experimental ramjet craft but is purely an estimate* : "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Calculate initial velocity components
        v_horizontal = velocity_mag * np.cos(np.radians(angle_of_attack))
        v_vertical = velocity_mag * np.sin(np.radians(angle_of_attack))

        # Define initial vertical position
        y_initial = 0.0  # Assume starting from sea level

        # Define initial state
        state_initial = [v_horizontal, v_vertical]

        # Time span for integration (0 to 100 seconds)
        t_span = [0, 100]

        # Solve the ODE
        sol = solve_ivp(lambda t, state: acceleration_function(t, state, angle_of_attack, mass, lifting_area, intake_area),
                        t_span,
                        state_initial,
                        method='RK45',
                        t_eval=np.linspace(t_span[0], t_span[1], 1000))

        # Extract velocity and position from solution
        v_values = sol.y[:2]

        # Calculate acceleration values
        acceleration_values = np.array([acceleration_function(t, sol.y[:, i], angle_of_attack, mass, lifting_area, intake_area) for i, t in enumerate(sol.t)])

        # Plot the velocity and position graphs
        plt.figure(figsize=(12, 8))

        # Velocity plots
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

        # Acceleration plots
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
