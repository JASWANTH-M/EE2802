import numpy as np
import cvxpy as cp

# Load training data
train_data = np.loadtxt('Training_Data.txt')
n1, m1 = train_data.shape
volt = train_data[:, 0]
X_train = np.vstack((volt.T, np.ones((1, n1))))
y_train = train_data[:, [1]]

# Model training using CVXPY
n = cp.Variable((2, 1))
objective = cp.Minimize(cp.sum_squares(X_train.T @ n - y_train))
problem = cp.Problem(objective)
problem.solve()
n = n.value

print("Optimal parameter:\n", n)