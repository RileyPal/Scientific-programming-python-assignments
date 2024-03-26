import numpy as np
import matplotlib.pyplot as plt

# Define parameters
a_values = [0.5, 1, 2]
f = 3
k = 3 * np.pi
w = np.pi
t = 0

# Define the function
def wave_packet(x, a):
    return np.exp(-(a * x - f * t)**2) * np.sin(k * x - w * t)

# Generate x values
x_values = np.linspace(-4, 4, 1000)

# Plot the wave packets for different values of a
plt.figure(figsize=(10, 6))
for a in a_values:
    plt.plot(x_values, wave_packet(x_values, a), label=f'a = {a}')

# Add labels and legend
plt.title('Wave Packet for Different Values of $a$')
plt.xlabel('$x$')
plt.ylabel('$f(x, t)$')
plt.legend()
plt.grid(True)
plt.show()
