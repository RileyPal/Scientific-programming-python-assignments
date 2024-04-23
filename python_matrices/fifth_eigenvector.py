import numpy as np
import matplotlib.pyplot as plt

# Define H matrix
H = np.array([[2.22222222, -1.11111111, 0., 0., 0.],
              [-1.11111111, 2.22222222, -1.11111111, 0., 0.],
              [0., -1.11111111, 2.22222222, -1.11111111, 0.],
              [0., 0., -1.11111111, 2.22222222, -1.11111111],
              [0., 0., 0., -1.11111111, 2.22222222]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(H)

# Sort eigenvalues and eigenvectors
sorted_indices = np.argsort(eigenvalues)
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Extract the fifth eigenvector
fifth_eigenvector = eigenvectors[:, 4]

# Generate x values
x_values = np.linspace(1 / (5 + 1), 5 / (5 + 1), 5)

# Generate y values for sqrt(2) * sin(x * pi)
y_values = np.sqrt(2) * np.sin(x_values * np.pi)

# Plot the fifth eigenvector and the specified function
plt.plot(x_values, fifth_eigenvector, label='Fifth Eigenvector')
plt.plot(x_values, y_values, label=r'$\sqrt{2} \sin(\pi x)$')
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Fifth Eigenvector vs. Function')
plt.legend()
plt.grid(True)
plt.show()
