import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import cumulative_trapezoid

# Constants
g = 9.81  # Gravitational constant (m/s^2)
lift_coefficient = 0.5  # Lift coefficient *can't seem to find a good source to base this on for lifting body craft
# so this is bordering on being made up, simply a guess based on range of realworld values that exist.*

# Air density data table pulled from Nasa's website
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
    # Calculate the mass flow rate of oxygen based on air density and intake area
    mass_flow_rate_of_oxygen = 0.21 * air_density * intake_area * velocity  # for clarity, 21% of the air is oxygen
    # thus .21*air density*intake area*velocity gives oxygen available in units of kg/s
    # Assuming stoichiometric combustion, determine the mass flow rate of methane
    # For each unit of oxygen, methane requires a certain amount according to the stoichiometry
    # Adjust the scaling factor according to the stoichiometry of the reaction
    methane_to_oxygen_ratio = 0.25  # required for complete combustion
    mass_flow_rate_of_fuel = methane_to_oxygen_ratio * mass_flow_rate_of_oxygen
    # Calculate thrust based on intake area, air density, and velocity P.S that 3200 figure, it's the Isp value for
    # the exact type of engine I intend this program to try and simulate. It's a value I had to pull from a well
    # researched Sim called Kerbal Space program(since numbers like that aren't publicly available for real world
    # counter parts).
    T = ((mass_flow_rate_of_fuel * g) * 3200)
    return T, mass_flow_rate_of_fuel


# Function to calculate acceleration
def acceleration_function(t, state, angle_of_attack, mass, lifting_area, intake_area):
    v, vertical_positions_values = state  # Unpack state
    theta_rad = np.radians(angle_of_attack)  # Convert angle to radians
    # Calculate air density at current altitude
    air_density = air_density_func(vertical_positions_values)
    # Calculate thrust
    T, mass_flow_rate_of_fuel = thrust_function(air_density, v, intake_area)
    # Constants
    drag_coefficient = 0.025  # x-24B experimental lifting body was the basis for this value
    cross_sectional_area = 0.5 * np.pi * (
            lifting_area / 4.5) ** 2  # front cross sectional area will be roughly semi-circular with radius
    # equal to 1/4.5 * lifting area
    # Adjust the mass
    mass -= mass_flow_rate_of_fuel
    # Calculate drag force magnitude
    v_magnitude = v
    drag_magnitude = 0.5 * drag_coefficient * air_density * cross_sectional_area * v_magnitude ** 2
    # Calculate lift force magnitude
    lift_magnitude = 0.5 * lift_coefficient * air_density * lifting_area * v_magnitude ** 2
    # Calculate drag force components *need to revise this in the future since the angle used for the drag should
    # change with velocity components but right now just stays whatever the angle of attack was*
    drag_horizontal = -drag_magnitude * np.cos(theta_rad)
    drag_vertical = -drag_magnitude * np.sin(theta_rad)
    # Calculate lift force components
    lift_vertical = lift_magnitude * np.cos(theta_rad)
    lift_horizontal = lift_magnitude * -np.sin(theta_rad)
    # Calculate thrust components
    T_vertical = T * np.sin(theta_rad)
    T_horizontal = T * np.cos(theta_rad)
    # Calculate acceleration components
    a_vertical = -g + (drag_vertical + lift_vertical + T_vertical) / mass
    a_horizontal = (drag_horizontal + lift_horizontal + T_horizontal) / mass
    return [a_horizontal,
            a_vertical]  # Return [horizontal acceleration, vertical acceleration, horizontal thrust, vertical thrust]


# Main function
def main():
    while True:
        try:
            # Prompt the user for input values
            mass = float(input("Enter the initial mass of the craft (kg): "))
            velocity_mag = float(input(
                "Enter the initial velocity magnitude (m/s) ex: 100 m/s would be the minimum to be within the edge of "
                "believability for Ramjet operation : "))
            angle_of_attack = float(input("Enter the angle of attack (degrees): "))
            lifting_area = float(input(
                "Enter the lifting area (m^2) ex: Lifting body designs have like the x-24 which the drag calculations "
                "are based on had 31 m^2: "))
            intake_area = float(input(
                "Enter the intake area (m^2) *realistically should be somewhere between .1-1.5 based on scaling nasas "
                "xf43 experimental ramjet craft to size of the space shuttle but is purely an estimate* : "))
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
        sol = solve_ivp(
            lambda t, state: acceleration_function(t, state, angle_of_attack, mass, lifting_area, intake_area),
            t_span,
            state_initial,
            method='RK45',
            t_eval=np.linspace(t_span[0], t_span[1], 100000))

        # Extract velocity
        v_values = sol.y[:2]

        # Calculate acceleration values
        acceleration_values = np.array(
            [acceleration_function(t, sol.y[:, i], angle_of_attack, mass, lifting_area, intake_area) for i, t in
             enumerate(sol.t)])

        # Calculate thrust magnitude
        thrust_magnitudes = np.array(
            [thrust_function(air_density_func(y), v, intake_area) for v, y in zip(v_values[1], sol.y[1])])
        # Calculate positions by integrating velocities
        horizontal_position = cumulative_trapezoid(v_values[0], sol.t)
        vertical_position_values = cumulative_trapezoid(v_values[1], sol.t)
        time_adjusted = sol.t[:-1]

        # Plot the velocity, position, and acceleration graphs
        plt.figure(figsize=(12, 12))

        # Velocity plots
        plt.subplot(3, 2, 1)
        plt.plot(sol.t, v_values[0], label='Horizontal Velocity')
        plt.xlabel('Time (s)')
        plt.ylabel('Horizontal Velocity (m/s)')
        plt.title('Horizontal Velocity vs Time')
        plt.grid(True)
        plt.legend()

        plt.subplot(3, 2, 2)
        plt.plot(sol.t, v_values[1], label='Vertical Velocity')
        plt.xlabel('Time (s)')
        plt.ylabel('Vertical Velocity (m/s)')
        plt.title('Vertical Velocity vs Time')
        plt.grid(True)
        plt.legend()

        # Acceleration plots
        plt.subplot(3, 2, 3)
        plt.plot(sol.t, acceleration_values[:, 0], label='Horizontal Acceleration', color='blue')
        plt.xlabel('Time (s)')
        plt.ylabel('Horizontal Acceleration (m/s^2)')
        plt.title('Horizontal Acceleration vs Time')
        plt.grid(True)
        plt.legend()

        plt.subplot(3, 2, 4)
        plt.plot(sol.t, acceleration_values[:, 1], label='Vertical Acceleration', color='green')
        plt.xlabel('Time (s)')
        plt.ylabel('Vertical Acceleration (m/s^2)')
        plt.title('Vertical Acceleration vs Time')
        plt.grid(True)
        plt.legend()

        # Position plots
        plt.subplot(3, 2, 5)
        plt.plot(time_adjusted, horizontal_position, label='Horizontal Position', color='red')
        plt.xlabel('Time (s)')
        plt.ylabel('Horizontal Position (m)')
        plt.title('Horizontal Position vs Time')
        plt.grid(True)
        plt.legend()

        # Plot the vertical position graph
        plt.subplot(3, 2, 6)
        plt.plot(time_adjusted, vertical_position_values, label='Vertical Position', color='orange')
        plt.xlabel('Time (s)')
        plt.ylabel('Vertical Position (m)')
        plt.title('Vertical Position vs Time')
        plt.grid(True)
        plt.legend()

        # Thrust plot
        plt.figure(figsize=(6, 6))
        plt.plot(sol.t, thrust_magnitudes, label='Thrust Magnitude', color='purple')
        plt.xlabel('Time (s)')
        plt.ylabel('Thrust Magnitude (N)')
        plt.title('Thrust Magnitude vs Time')
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

# Currently don't trust the result im getting at all. I suspect the way the components are being handled by the ivp is
# just wrong.
