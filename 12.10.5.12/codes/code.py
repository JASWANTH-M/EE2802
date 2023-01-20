import numpy as np

A = np.array([[1, 4, 2],
              [3, -2, 7],
              [2, -1, 4]])

b = np.array([[0],
              [0],
              [15]])

X = np.linalg.solve(A,b)

print(X)
