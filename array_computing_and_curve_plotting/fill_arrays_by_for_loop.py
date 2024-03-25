import numpy as np

def gaussian(position):
    return np.exp(-position**2 / 2) / np.sqrt(2 * np.pi)

if __name__ == '__main__':
    x_values = np.empty(41)
    y_values = np.empty(41)
    positions = np.linspace(-4, 4, 41)
    for i, pos in enumerate(positions):
        x_values[i] = pos
        y_values[i] = gaussian(pos)
    print("X Values:", x_values)
    print("Y Values:", y_values)
