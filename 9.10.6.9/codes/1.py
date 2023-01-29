import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')
from line.funcs import *
from conics.funcs import *

C1 = np.array([2,0])
C2 = np.array([-2,0])

U1 = -C1
f1 = -4

U2 = -C2
f2 = -4

r1 = np.sqrt(np.linalg.norm(U1)**2-f1)
r2 = np.sqrt(np.linalg.norm(U2)**2-f1)

c1 = circ_gen(C1, r1)
c2 = circ_gen(C2, r2)

plt.figure(figsize=(5,5))
plt.plot(c1[0], c1[1])
plt.plot(c2[0], c2[1])

plt.plot(C1[0],C1[1], 'go')
plt.text(C1[0]+0.2,C1[1],'$C_1$(2,0)')
plt.plot(C2[0],C2[1], 'go')
plt.text(C2[0]-1.45,C2[1],'$C_2$(-2,0)')

A = np.array([0,2])
B = np.array([0,-2])
plt.plot(A[0],A[1])
plt.text(A[0]+0.2,A[1],'$A$(0,2)')

plt.plot(B[0],B[1])
plt.text(B[0]+0.2,B[1],'$B$(0,-2)')


P = np.array([12/5,-14/5])
Q = np.array([4/5,2/5])
x_AP = line_gen(A,P)
x_PQ = line_gen(P,Q)
x_BP = line_gen(B,P)
x_BQ = line_gen(B,Q)

plt.plot(x_AP[0,:],x_AP[1,:], 'g')
plt.plot(x_PQ[0,:],x_PQ[1,:], 'g')
plt.plot(x_BP[0,:],x_BP[1,:], ls = '--')
plt.plot(x_BQ[0,:],x_BQ[1,:], ls = '--')

tri_coords = np.vstack((P,Q)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,0), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
arr = np.arange(-5,6)
plt.xticks(arr)
plt.yticks(arr)
plt.xlabel("$x$")
plt.ylabel("$y$")    
plt.grid()
plt.savefig("fig.png")
plt.show()
