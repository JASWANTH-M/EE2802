import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')
from line.funcs import *
from conics.funcs import *

O = np.array([0,0])
r1 = 2
r2 = 3

c1 = circ_gen(O, r1)
c2 = circ_gen(O, r2)

A = np.array([1,2*np.sqrt(2)])
B = np.array([1, np.sqrt(3)])
C = np.array([1, -np.sqrt(3)])
D = np.array([1,-2*np.sqrt(2)])

plt.figure(figsize=(4,4))
tri_coords = np.vstack((A,B,C,D)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','D']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,0), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.plot(c1[0], c1[1])
plt.plot(c2[0], c2[1])

plt.vlines(x = 1, ymin = -4, ymax = 4, colors='green')
plt.plot(O[0],O[1], 'go')
plt.text(O[0]+0.2,O[1],'O(0,0)')
arr = np.arange(-4,5)
plt.xticks(arr)
plt.yticks(arr)
plt.grid()
plt.savefig("fig.png")
plt.show()
