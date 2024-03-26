import numpy as np
import matplotlib.pyplot as plt


def velocity_function(t, g, k, m, F_thrust_func, theta_deg, v0):
    # velocity function with drag and powered flight
    theta_rad = np.radians(theta_deg)  # Convert angle to radians
    # Initialize the previous velocity value
    v_prev = v0
    v = (F_thrust_func(v_prev) / m) * t - g * m / k * (1 - np.exp(-k / m * t)) * np.sin(theta_rad)
    return v

def acceleration_function(t, g, k, m, F_thrust_func, theta_deg, v0):
    # Calculate acceleration using the velocity function
    v = velocity_function(t, g, k, m, F_thrust_func, theta_deg, v0)
    a = (F_thrust_func(v) / m) - k / m * v
    return a

def find_change_in_acceleration(g, k, m, F_thrust_func, theta_deg, v0, start_time=0, end_time=10, step_size=0.1):
    # Find the point where the change in acceleration becomes negative
    t = start_time
    while t < end_time:
        a = acceleration_function(t, g, k, m, F_thrust_func, theta_deg, v0)
        next_a = acceleration_function(t + step_size, g, k, m, F_thrust_func, theta_deg, v0)
        delta_a = next_a - a
        if delta_a < 0:
            return t + step_size
        t += step_size
    return None

# Example scenario
def example_scenario():
    # Parameters for the example scenario
    initial_velocity = 1000  # m/s
    g = 9.81  # m/s^2
    m = 100.0  # kg
    thrust_equation = "lambda v: 0.1 * v + 100"  # Thrust equation: constant times velocity plus baseline thrust
    theta_deg = 0.0  # Launch angle in degrees

    # Convert the thrust equation string to a callable function
    F_thrust_func = eval(thrust_equation)

    # Find the point where the change in acceleration becomes negative
    t_change = find_change_in_acceleration(g, 0.1, m, F_thrust_func, theta_deg, initial_velocity)
    if t_change is not None:
        print("Example scenario:")
        print("Initial velocity:", initial_velocity, "m/s")
        print("Gravitational constant:", g, "m/s^2")
        print("Mass of the object:", m, "kg")
        print("Thrust equation:", thrust_equation)
        print("Launch angle:", theta_deg, "degrees")
        print("The change in acceleration becomes negative at t =", t_change)

        # Plot the velocity graph
        t_values = np.linspace(0, t_change, 100)
        v_values = [velocity_function(t, g, 0.1, m, F_thrust_func, theta_deg, initial_velocity) for t in t_values]
        plt.plot(t_values, v_values)
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.title('Velocity vs Time')
        plt.grid(True)
        plt.show()
    else:
        print("No change in acceleration becoming negative within the specified range.")

# Call the example scenario
example_scenario()

def main():
    # Prompt the user for input values
    initial_velocity = float(input("Enter the initial velocity (m/s): "))
    g = float(input("Enter the gravitational constant (m/s^2): "))
    m = float(input("Enter the mass of the object (kg): "))
    baseline_thrust = float(input("Enter the baseline thrust (N): "))
    thrust_coefficient = float(input("Enter the thrust coefficient: "))
    theta_deg = float(input("Enter the launch angle in degrees: "))

    # Define the thrust equation with baseline thrust and velocity term
    thrust_equation = f"lambda v: {baseline_thrust} + {thrust_coefficient} * v"

    # Convert the thrust equation string to a callable function
    F_thrust_func = eval(thrust_equation)

    # Find the point where the change in acceleration becomes negative
    t_change = find_change_in_acceleration(g, 0.1, m, F_thrust_func, theta_deg, initial_velocity)
    if t_change is not None:
        print("The change in acceleration becomes negative at t =", t_change)

        # Plot the velocity graph
        t_values = np.linspace(0, t_change, 100)
        v_values = [velocity_function(t, g, 0.1, m, F_thrust_func, theta_deg, initial_velocity) for t in t_values]
        plt.plot(t_values, v_values)
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.title('Velocity vs Time')
        plt.grid(True)
        plt.show()
    else:
        print("No change in acceleration becoming negative within the specified range.")

    if __name__ == "__main__":
        main()