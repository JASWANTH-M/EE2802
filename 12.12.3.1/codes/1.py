import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

A = np.array([[-1,0],
              [0,-1],
              [-4,-1],
              [-1,-5],
              [3,2]])

B = np.array([0,0,-80,-115,150])

# Define variables
x = cp.Variable(2)

# Define constraints
constraints = [A@x <= B]

n = np.array([-6,-3])

# Define objective
objective = cp.Minimize(n.T@x)

# Solve problem
prob = cp.Problem(objective, constraints)
result = prob.solve()

# Print solution
print(round(result,4))
print("x =", np.round(x.value,4))
