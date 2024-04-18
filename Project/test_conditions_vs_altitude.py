# Air density data table pulled from Nasa's website
import numpy as np

g = 9.81  # Gravitational constant (m/s^2)
lift_coefficient = 0.5  # Lift coefficient *can't seem to find a good source to base this on for lifting body craft so this is bordering on being made up, simply a guess based on range of realworld values that exist.*
y = 100000
velocity = 100
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
    # Define energy density of methane and mass flow rate of methane (sample values) may use in other thrust calculation approaches
    energy_density = 42  # MJ/kg theoretical max for hydrocarbon fuels in air
    energy_density_joules_per_kg = energy_density * 1e6  # 1 MJ = 1e6 J
    # Calculate the mass flow rate of oxygen based on air density and intake area
    mass_flow_rate_of_oxygen = 0.21 * air_density * intake_area * velocity  # for clarity, 21% of the air is oxygen thus .21*air density*intake area*velocity gives oxygen available in units of kg/s
    # Assuming stoichiometric combustion, determine the mass flow rate of methane
    # For each unit of oxygen, methane requires a certain amount according to the stoichiometry
    # Adjust the scaling factor according to the stoichiometry of the reaction
    methane_to_oxygen_ratio = 0.25  # required for complete combustion
    mass_flow_rate_of_fuel = methane_to_oxygen_ratio * mass_flow_rate_of_oxygen
    # Calculate thrust based on intake area, air density, and velocity
    # P.S that 3200 figure, it's the Isp value for the exact type of engine I intend this program to try and simulate. It's a value I had to pull from a well researched Sim called Kerbal Space program(since numbers like that aren't publicly available for real world counter parts).
    T = ((mass_flow_rate_of_fuel * g)*3200)
    return T, mass_flow_rate_of_fuel

print(thrust_function(air_density_func(y), 100, 1))