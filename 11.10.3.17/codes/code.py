import numpy as np
import sys
sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')
from line.funcs import *

A = np.array([2,3])
B = np.array([4,-1])
C = np.array([1,2])

# Equation of line BC
m = B-C
print(m)

n = omat@m
print(n)

c = n@B

# Length of altitude from A to BC
d = (np.absolute(A@n - c))/np.linalg.norm(n)
print(d)
