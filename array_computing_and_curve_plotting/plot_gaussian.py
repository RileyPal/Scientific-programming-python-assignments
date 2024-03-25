import numpy as np
import matplotlib.pyplot as plt

def gaussian(position):
    return np.exp(-position**2 / 2) / np.sqrt(2 * np.pi)

if __name__ == '__main__':
    positions = np.linspace(-4, 4, 1000)
    gaussian_values = gaussian(positions)
    plt.plot(positions, gaussian_values)
    plt.title("Gaussian Function")
    plt.xlabel("Position")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()
