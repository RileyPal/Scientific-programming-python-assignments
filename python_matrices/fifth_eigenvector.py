import numpy as np

matrix = np.array([[0,1],[1,0]])
print(f'A = {matrix}')
determinant = np.linalg.det(matrix)
print(f'Determinant = {determinant}')

inverse_matix = np.linalg.inv(matrix)
print(f'inv(A) = {inverse_matix}')
for eigenvalue, eigenvector in zip(eigenvalues, eigenvectors):
    print(f'lambda = {eigenvalue}')
    print(f'v = {eigenvector}')