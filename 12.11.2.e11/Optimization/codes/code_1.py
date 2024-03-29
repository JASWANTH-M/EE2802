import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

x1 = np.array([1,1,0])
x2 = np.array([2,1,-1])

#Direction vectors
m1 = np.array([[2],[-1],[1]])
m2 = np.array([[3],[-5],[2]])

M = np.block([m1,m2])
x = np.array([1,2])
print(M@x)
A = x2-x1
print(M)
print(A)

# Define variables
l = cp.Variable(2)

# Define constraints
constraints = []

# Define objective
objective = cp.Minimize(cp.norm(A - M@l))

# Solve problem
prob = cp.Problem(objective, constraints)
result = prob.solve()

# Print solution
print(round(result,4))
print("l =", np.round(l.value,4))

l1 = l.value[0]
l2 = l.value[1]

print(l1, -l2)

x1.resize(3,1)
x2.resize(3,1)


#Points
P = x1 + (l1)*m1
Q = x2 + (-l2)*m2

print(P) 
print(Q)
print(np.linalg.norm(P-Q))

#Arrays for plotting
M = np.hstack((P-2*m1,P+2*m1))
N = np.hstack((Q-2*m2,Q+2*m2))
P = np.hstack((P,Q))

# Plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(M[0], M[1], M[2])
ax.plot(N[0], N[1], N[2])
ax.plot(P[0], P[1], P[2])
ax.scatter(M[0], M[1], M[2])
ax.scatter(N[0], N[1], N[2])
ax.scatter(P[0], P[1], P[2])
ax.text(P[0][0],P[1][0],P[2][0],'P')
ax.text(Q[0][0],Q[1][0],Q[2][0],'Q')
plt.legend(['L1','L2','Normal'])
ax.view_init(60,30)
plt.grid()
plt.tight_layout()
plt.savefig('../figs/skew.png', dpi=600)
