import numpy as np
import matplotlib.pyplot as plt

Train_data = np.loadtxt('Training_Data.txt')
n1, m1 = Train_data.shape
Volt = Train_data[:,0]
print(Volt.T)
X = np.vstack((Volt.T, np.ones((1,n1))))
Temp = Train_data[:,[1]]

print(X.T)
print(Temp)

# Least Squares Method - Model Training
n = np.linalg.lstsq(X.T, Temp, rcond=None)[0]
print(n)

plt.plot(Volt, X.T @n, label= 'Fitted line')
plt.scatter(Volt,Temp, label='Original data', color = 'red')
plt.grid()
plt.xlabel("Voltage (in Volts)")
plt.ylabel("Temperature (in $^{\circ}$C)")
plt.legend()
plt.savefig('../figs/Train.png')
plt.close()

# Testing the Model - Model Evaluation
Test_data = np.loadtxt('Test_Data.txt')
n2, m2 = Test_data.shape
Volt_test = Test_data[:,0]
X_test = np.vstack((Volt_test,np.ones((1,n2))))
Temp_test = Test_data[:,[1]]

plt.plot( Volt_test,X_test.T @n, label= 'Fitted line')
plt.scatter(Volt_test,Temp_test,  label='Original data', color = 'red')
plt.xlabel("Voltage (in Volts)")
plt.ylabel("Temperature (in $^{\circ}$C)")
plt.legend()
plt.grid()
plt.savefig("../figs/Test.png")
