import numpy as np

def gaussian(position):
    return np.exp(-position**2 / 2) / np.sqrt(2 * np.pi)

if __name__ == '__main__':
    positions = np.linspace(-4, 4, 41)
    gaussian_values = gaussian(positions)
    print("Positions:", positions)
    print("Gaussian Values:", gaussian_values)
