# Air density data table pulled from Nasa's website
import numpy as np

data_table = {
    "Altitude (m)": [-1000, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000,
                     40000, 50000, 60000, 70000, 80000, 90000],
    "Density (kg/m^3)": [1.347, 1.225, 1.112, 1.007, 0.9093, 0.8194, 0.7364, 0.6601, 0.5900, 0.5258, 0.4671, 0.4135,
                         0.1948, 0.08891, 0.04008, 0.01841, 0.003996, 0.001027, 0.0003097, 0.00008283, 0.00001846, 0.0]
}
y = 0

def air_density_func(y):
    # Retrieve altitude and density data from the data table
    altitudes = data_table["Altitude (m)"]
    densities = data_table["Density (kg/m^3)"]
    # Interpolate air density based on altitude
    return np.interp(y, altitudes, densities)

print(air_density_func(y))