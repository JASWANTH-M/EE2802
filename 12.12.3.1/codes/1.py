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

#Drawing lines
x1 = np.linspace(-10,100,400) 
t = np.zeros(len(x1))
y1 = (80-4*x1)
y2 = (115-x1)/5
y3 = (150-3*x1)/2
y4 = np.linspace(-10,100,400)

plt.plot(x1,y1,label = '$4x+y=80 $')
plt.plot(x1,y2,label = '$x+5y=115$')
plt.plot(x1,y3,label = '$3x+2y=150$')
plt.plot(x1,t,label = '$x=0$')
plt.plot(t,y4,label = '$y=0$')

plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Corner point method')
plt.ylim(-10,100)

#Corner Points
P = np.array([2, 72])
Q = np.array([15, 20])
R = np.array([40, 15])

#Filling the feasible region
fill_cords = np.vstack((P,Q,R))
plt.fill(fill_cords[:,0], fill_cords[:,1],'plum',label =  "Feasible Region")


#Labeling the coordinates
tri_coords = np.vstack((P,Q,R)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R']
for i, txt in enumerate(vert_labels):
    label = "{}({},{})".format(txt, int(tri_coords[0,i]),int(tri_coords[1,i])) #Form label as A(x,y)
    plt.annotate(label, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.legend(loc='best')
plt.grid('on')
plt.savefig('../figs/fig.png')
plt.show()