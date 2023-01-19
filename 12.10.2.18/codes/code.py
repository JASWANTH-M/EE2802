import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')
from line.funcs import *

#x = np.array ([1,4,6,1])
#y = np.array ([1,10,3,1])
A = np.array([1,1])
B = np.array([4,10])
C = np.array([6,3])

x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CA[0,:],x_CA[1,:])

x = [1, 4, 6]
y = [1, 10,3]
pts = ['A','B','C']

vert_labels = ['A','B','C']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (x[i], y[i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(2,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.grid()
plt.savefig("triangel.png")
plt.show()
