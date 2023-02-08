import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')

from line.funcs import *
from conics.funcs import ellipse_gen
from params import *

A = np.array([[16,-1],[36,-1]])
B = np.array([[25],[40]])

C1 = np.linalg.solve(A,B)

e = np.sqrt(C1[0][0])
f = C1[1][0]

# Given major axis on y-axis
n = np.array([[0],[1]])
V = (np.linalg.norm(n)**2 * np.eye(2)) - ((e**2)* (n@n.T))
print(V)

# Given center of the ellipse is origin
C = np.array([[0],[0]])
u = -1 * V@C
print(u)
print(f)

lamda, v = np.linalg.eig(V)
lamda1 = lamda[0]
lamda2 = lamda[1]

print(lamda1, lamda2)

f0 = (u.T@np.linalg.inv(V)@u)-f
f0 = f0[0][0]

a = np.sqrt(abs(f0/lamda1))
b = np.sqrt(abs(f0/lamda2))
print(a,b)

E = ellipse_gen(a,b)
plt.figure(figsize = (5,6))
plt.plot(E[0], E[1])
plt.grid()
plt.tight_layout()
plt.savefig("fig1.png")
