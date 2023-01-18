import numpy as np

import sys
sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')
from line.funcs import *

A = np.array([1985,92])
B = np.array([1995,97])
 
# Direction vector of the line joining A, B
m = B-A
print(m)

# Slope
slope = m[1]/m[0]
print(slope)

# Normal vecor
n = omat@m
print(n)

# constant c
c = np.dot(n,A)
print (c)

# Basis vectors
e1 = np.array([1,0])
e2 = np.array([0,1])

# the value of y coordinate for x= 2010
y = (c - (2010* np.dot(e1,n)))/(np.dot(e2,n))

print(y)
