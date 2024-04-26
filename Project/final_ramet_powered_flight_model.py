import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Gravitational constant (m/s^2)
lift_coefficient = 0.4  # Lift coefficient: what research I could find suggests max for this type of aircraft is .4
x0 = 0.0
y0 = 0.0

# Air density data table
data_table = {
    "Altitude (m)": [-1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000,
                     40000, 50000, 60000, 70000, 80000, 90000],
    "Density (kg/m^3)": [1.347, 1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5900, 0.5258, 0.4671, 0.4135,
                         0.1948, 0.08891, 0.04008, 0.01841, 0.003996, 0.001027, 0.0003097, 0.00008283, 0.00001846, 0.0]
}


# Main function
def main():
    # Get initial conditions
    v0_horizontal, v0_vertical, x, y, mass, lifting_area, intake_area = get_initial_conditions()

    # Time parameters
    dt = 0.01  # Time step size
    t_max = 100  # Maximum time

    # Initialize arrays to store results
    time_values = np.arange(0, t_max, dt)
    acceleration_values = np.zeros((len(time_values), 2))
    velocity_values = np.zeros((len(time_values), 2))
    position_values = np.zeros((len(time_values), 2))
    thrust_values = np.zeros((len(time_values), 1))

    # Initial state
    state = [v0_horizontal, v0_vertical]

    # Evolve the system forward in time
    for i, t in enumerate(time_values):
        # Calculate acceleration
        a_horizontal, a_vertical, T = acceleration_function(state, y,  mass, lifting_area, intake_area)

        # Store acceleration
        acceleration_values[i] = [a_horizontal, a_vertical]
        # Store thrust
        thrust_values[i] = [T]

        # Update velocity
        state[0] += a_horizontal * dt
        state[1] += a_vertical * dt

        # Store velocity
        velocity_values[i] = state

        # Update position
        x, y = position_values[i - 1] + velocity_values[i] * dt
        position_values[i] = [x, y]

    # Plot results
    plot_results(time_values, acceleration_values, velocity_values, position_values, thrust_values)


# Function to get initial conditions
def get_initial_conditions():
    try:
        mass = float(input("Enter the initial mass of the craft (kg): "))
        velocity_mag = float(input(
            "Enter the initial velocity magnitude (m/s) ex: 100 m/s would be the minimum to be within the edge of "
            "believability for Ramjet operation : "))
        angle_of_attack = float(input("Enter the angle of attack (degrees): "))
        lifting_area = float(input(
            "Enter the lifting area (m^2) ex: Lifting body designs have like the x-24 which the drag calculations "
            "are based on had 31 m^2: "))
        intake_area = float(input(
            "Enter the intake area (m^2) *realistically should be somewhere between .1-1.5 based on scaling nasa's "
            "xf43 experimental ramjet craft to size of the space shuttle but is purely an estimate* : "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_initial_conditions()

    v0_horizontal = velocity_mag * np.cos(np.radians(angle_of_attack))
    v0_vertical = velocity_mag * np.sin(np.radians(angle_of_attack))
    x = 0.0
    y = 0.0

    return v0_horizontal, v0_vertical, x, y, mass, lifting_area, intake_area


# Function to calculate air density
def air_density_func(y):
    altitudes = data_table["Altitude (m)"]
    densities = data_table["Density (kg/m^3)"]
    return np.interp(y, altitudes, densities)


# Function to calculate thrust
def thrust_function(air_density, velocity, intake_area):  # This could be modified to switch to a traditional rocket
    # thrust calculation once air density reaches either zero or whenever the constant thrust of a rocket engine would
    # be greater than the air breathing engine
    mass_flow_rate_of_oxygen = 0.21 * air_density * intake_area * velocity
    methane_to_oxygen_ratio = 0.25
    mass_flow_rate_of_fuel = methane_to_oxygen_ratio * mass_flow_rate_of_oxygen
    T = (mass_flow_rate_of_fuel * g) * 3200
    return T, mass_flow_rate_of_fuel


# Function to calculate lift
def lift_function(air_density, v_horizontal, lifting_area):
    lift = 0.5 * lift_coefficient * air_density * lifting_area * v_horizontal ** 2
    return lift


# Function to calculate acceleration
def acceleration_function(state, y, mass, lifting_area, intake_area):
    v_horizontal, v_vertical = state
    air_density = air_density_func(y)

    # Calculate thrust
    T, mass_flow_rate_of_fuel = thrust_function(air_density, v_horizontal, intake_area)
    mass -= mass_flow_rate_of_fuel
    # Calculate lift
    lift = lift_function(air_density, v_horizontal, lifting_area)

    # Calculate drag
    drag_coefficient = 0.025
    cross_sectional_area = 0.5 * np.pi * (lifting_area / 4.5) ** 2  # Possibly the most extreme simplification I've made
    drag_horizontal = 0.5 * drag_coefficient * air_density * cross_sectional_area * v_horizontal ** 2
    drag_vertical = 0.5 * drag_coefficient * air_density * cross_sectional_area * v_vertical ** 2
    # Calculate gravitational force
    gravity_force = mass * g

    # Calculate horizontal acceleration ignoring lift's affect in the horizontal
    a_horizontal = (T - drag_horizontal) / mass

    # Calculate vertical acceleration
    a_vertical = (lift - gravity_force - drag_vertical) / mass

    return a_horizontal, a_vertical, T


# Function to plot results
def plot_results(time_values, acceleration_values, velocity_values, position_values, thrust_values):
    print("start and end values:")
    print("t:", time_values)
    print("accel:", acceleration_values)
    print("vel:", velocity_values)
    print("x,y:", position_values)
    plt.figure(figsize=(12, 12))

    plt.subplot(3, 2, 1)
    plt.plot(time_values, acceleration_values[:, 1], label='Vertical Acceleration')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Vertical Acceleration vs Time')
    plt.legend()
    plt.grid()

    plt.subplot(3, 2, 2)
    plt.plot(time_values, acceleration_values[:, 0], label='Horizontal Acceleration')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.title('Horizontal Acceleration vs Time')
    plt.legend()
    plt.grid()

    plt.subplot(3, 2, 3)
    plt.plot(time_values, velocity_values[:, 1], label='Vertical Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Vertical Velocity vs Time')
    plt.legend()
    plt.grid()

    plt.subplot(3, 2, 4)
    plt.plot(time_values, velocity_values[:, 0], label='Horizontal Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Horizontal Velocity vs Time')
    plt.legend()
    plt.grid()

    plt.subplot(3, 2, 5)
    plt.plot(time_values, position_values[:, 1], label='Vertical Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Vertical Position vs Time')
    plt.legend()
    plt.grid()

    plt.subplot(3, 2, 6)
    plt.plot(time_values, position_values[:, 0], label='Horizontal Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Horizontal Position vs Time')
    plt.legend()
    plt.grid()

    plt.figure(figsize=(12, 8))
    plt.plot(time_values, thrust_values[:, 0], label='Thrust')
    plt.xlabel('Time (s)')
    plt.ylabel('Newtons (N)')
    plt.title('Thrust vs Time')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
