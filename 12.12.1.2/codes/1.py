import numpy as np
import cvxpy as cp

A = np.array([[1,2],
              [3,2],
              [-1,0],
              [0,-1]])

B = np.array([8,12,0,0])

# Define variables
x = cp.Variable(2)

# Define constraints
constraints = [A@x <= B]

n = np.array([-3,4])

# Define objective
objective = cp.Minimize(n.T@x)

# Solve problem
prob = cp.Problem(objective, constraints)
result = prob.solve()

# Print solution
print(round(result,4))
print("x =", np.round(x.value,4))
