import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'/home/jaswanth/6th-Sem/EE2802/CoordGeo')
from line.funcs import *

#Quadratic function
def quad(x):
    return 2* x**2 - 8*x + 16
def der(x):
    return 4*x - 8

#Create the quadratic curve
X = np.linspace(0,5,1000)
plt.plot(X,quad(X))

alpha = 0.01
lambda_n = -1
eps = 1e-6
cnt = 0
N = 10000

#Run the gradient descent algorithm
while cnt < N and (abs(alpha*der(lambda_n)) >= eps):
    nxt = lambda_n - alpha*der(lambda_n)
    cnt += 1
    nxt_coord = np.array([[nxt],[quad(nxt)]])
    lambda_coord = np.array([[lambda_n],[quad(lambda_n)]])
    # print(nxt)
    L = line_gen(nxt_coord,lambda_coord)
    plt.plot(L[0],L[1],'r')
    plt.plot(lambda_coord[0],lambda_coord[1],'k.')
    plt.plot(nxt_coord[0],nxt_coord[1],'k.')
    lambda_n = nxt

print(lambda_n)
plt.grid()
plt.tight_layout()
plt.savefig('../figs/grad_desc.png')