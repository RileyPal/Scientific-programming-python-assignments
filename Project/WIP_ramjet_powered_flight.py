import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
specific_fuel_consumption = 0.5  # Specific fuel consumption (kg/N)
initial_fuel = 1000  # Initial fuel amount (kg)
g = 9.81  # Gravitational constant (m/s^2)

# Thrust calculation function using NASA model
def thrust_function(fuel, tsfc):
    # Calculate thrust based on fuel consumption and TSFC
    return fuel / tsfc

# Velocity function with drag and powered flight
def velocity_function(t, g, k, m, thrust_func, theta_deg, v0, fuel):
    theta_rad = np.radians(theta_deg)  # Convert angle to radians
    integrand = lambda tau: (thrust_func(fuel, specific_fuel_consumption) / m) - k / m * v0 * np.exp(-k / m * tau)
    integral, _ = quad(integrand, 0, t)
    v = (thrust_func(fuel, specific_fuel_consumption) / k) * (1 - np.exp(-k / m * t)) - (m * g / k) * (1 - np.exp(-k / m * t)) * np.sin(theta_rad) - v0 * np.exp(-k / m * t) - integral
    return v

# Main function
def main():
    try:
        # Prompt the user for input values
        initial_velocity = float(input("Enter the initial velocity (m/s): "))
        m = float(input("Enter the mass of the object (kg): "))
        thrust_coefficient = float(input("Enter the thrust coefficient: "))
        theta_deg = float(input("Enter the launch angle in degrees: "))
        k = float(input("Enter the drag coefficient: "))
        end_time = float(input("Enter the end time for graphs (s): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Generate time values
    t_values = np.linspace(0, end_time, 1000)

    # Calculate velocity with drag and powered flight
    v_values = [velocity_function(t, g, k, m, thrust_function, theta_deg, initial_velocity, initial_fuel - specific_fuel_consumption * thrust_function(initial_fuel, specific_fuel_consumption) * t) for t in t_values]

    # Plot the velocity graph
    plt.plot(t_values, v_values)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    plt.grid(True)
    plt.show()

# Execute the main function
if __name__ == "__main__":
    main()