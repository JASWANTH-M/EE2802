import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')

from line.funcs import *
from conics.funcs import parab_gen
from params import *

def g(x, V, u, f):
    return x.T@V@x + 2*u.T@x + f

def affine_transform(P,c,x):
    return P@x + c

n = np.array([[0],[1]])
vertex = np.array([[0],[0]])

#Input parameters
V = np.array([[1,0],[0,0]])
f = 0

P = np.array([[5/2],[-10]])
Q = np.array([[-5/2],[-10]])

a = np.array([[4,-16],[-4,-16]])
b = np.array([[-5],[-5]])
u = np.linalg.solve(a,b)
print(u)

# Parameters of line
h = np.array([[0],[-2]])
m = np.array([[1],[0]])

# Points of intersection of Parabola, line
a1 = m.T@V@m
b1 = 2*m.T @(V@h + u)
c1= g(h, V, u, f)

alpha1= (-b1 + np.sqrt(b1**2 - 4*a1*c1))/2*a1
beta1 = (-b1 - np.sqrt(b1**2 - 4*a1*c1))/2*a1

A = h + alpha1*m
B = h + beta1*m

print(A)
print(B)

w = np.linalg.norm(A-B)
print(w)

P.resize(1,2)
Q.resize(1,2)
A.resize(1,2)
B.resize(1,2)

# Generating lines after transforming points
x_PQ = line_gen(P[0],Q[0])
x_AB = line_gen(A[0],B[0])

#Plotting all shapes
plt.plot(x_PQ[0,:],x_PQ[1,:])
plt.plot(x_AB[0,:],x_AB[1,:])

#Labeling the coordinates
plot_coords = np.vstack((P,Q,A,B)).T
plt.scatter(plot_coords[0,:], plot_coords[1,:])
vert_labels = ['P(5/2,-10)','Q(-5/2,-10)','A','B']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (plot_coords[0,i], plot_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


n = n.reshape(1,2)[0]
u = u.reshape(1,2)[0]
vertex = vertex.reshape(1,2)[0]

lamda,P = np.linalg.eigh(V)
# print(lamda[0], lamda[1])

c = 0.5*(np.linalg.norm(u) **2 - lamda[1]*f)/ (u.T@ n)
F = (c*n - u)/lamda[1]
fl = np.linalg.norm(F)
 
num_points = 100
delta = 2*np.abs(fl)/10
p_y = np.linspace(-18*np.abs(fl)-delta,18*np.abs(fl)+delta,num_points)

x1 = 5/2
y1=-10
t = x1**2/(y1)

# Generating all shapes
p_x = parab_gen(p_y,t)
p_std = np.vstack((p_x,p_y)).T

# Affine transformation
p = np.array([affine_transform(P,vertex,p_std[i,:]) for i in range(0,num_points)]).T

# print(p)
plt.plot(p[0,:], p[1,:])

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() 
plt.axis('equal')
plt.savefig("fig.png")