import numpy as np
import matplotlib.pyplot as plt

# Set the matrix dimension
matrix_dimension = 10

# Define H matrix
diagonal_value = 2
off_diagonal_value = -1

# Create the diagonal matrix
diagonal_matrix = diagonal_value * np.eye(matrix_dimension)

# Create the off-diagonal matrix
off_diagonal_matrix = off_diagonal_value * np.eye(matrix_dimension, k=-1) + off_diagonal_value * np.eye(matrix_dimension, k=1)

# Combine the matrices
H = (1 / (2 * (1/6)**2)) * (diagonal_matrix + off_diagonal_matrix)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(H)

# Sort eigenvalues and eigenvectors
sorted_indices = np.argsort(eigenvalues)
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Extract the tenth eigenvector
tenth_eigenvector = eigenvectors[:, 9]

# Generate x values
x_values = np.linspace(1/(matrix_dimension+1), matrix_dimension/(matrix_dimension+1), matrix_dimension)

# Generate y values for sqrt(2) * sin(x * pi)
y_values = np.sqrt(2) * np.sin(x_values * np.pi)

# Plot the tenth eigenvector and the specified function
plt.plot(x_values, tenth_eigenvector, label='Tenth Eigenvector')
plt.plot(x_values, y_values, label=r'$\sqrt{2} \sin(\pi x)$')
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Tenth Eigenvector vs. Function')
plt.legend()
plt.grid(True)
plt.show()