import numpy as np
import matplotlib.pyplot as plt


# Load the training data
Train_data = np.loadtxt('Training_Data.txt')
n1, m1 = Train_data.shape
Volt = Train_data[:,0]
X = np.vstack((Volt.T, np.ones((1,n1))))
Temp = Train_data[:,[1]]

# Define the error function
def error_function(n, X, Y):
    Y_pred = (X.T@n).reshape((-1,1))
    error = np.sum((Y - Y_pred)**2)
    return error

# Define the gradient of the error function
def gradient(n, X, Y):
    Y_pred = (X.T@n).reshape((-1,1))
    grad = -2*(X@(Y - Y_pred))
    return grad

alpha = 0.001
eps = 1e-4
n = np.array([[0], [0]])


while  np.linalg.norm(gradient(n, X, Temp)) >= eps:
    n = n - alpha*gradient(n, X, Temp)

print("Optimal parameter:", n)