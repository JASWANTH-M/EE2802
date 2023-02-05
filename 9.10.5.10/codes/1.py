import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')
from line.funcs import *
from conics.funcs import *

A = np.array([0,4])
B = np.array([0,-4])
C = np.array([6,6])

C1 = (A+B)/2
r1 = np.linalg.norm(A-B)/2


C2 = (A+C)/2
r2 = np.linalg.norm(A-C)/2


c1 = circ_gen(C1, r1)
c2 = circ_gen(C2, r2)

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

plt.figure(figsize=(7,7.8))
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])

tri_coords = np.vstack((A,B,C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,0), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.plot(c1[0], c1[1])
plt.plot(c2[0], c2[1])

plt.plot(C1[0],C1[1], 'go')
# plt.text(C[0]+0.2,C[1],'C1)')
plt.plot(C2[0],C2[1],'go')
# plt.text(A[0]+0.2,A[1],'A (4,5)')

plt.grid()
plt.savefig("fig.png")
# plt.show()
