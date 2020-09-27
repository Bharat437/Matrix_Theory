import numpy as np
A=np.array([[1.,4.],[3.,-5.]])
print("Given matrix A : \n",A)

Q=np.array([[1/np.sqrt(10),3/np.sqrt(10)],[3/np.sqrt(10),-1/np.sqrt(10)]])
R=np.array([[np.sqrt(10),-11/np.sqrt(10)],[0,17/np.sqrt(10)]])

print("\nOrthogonal Matrix Q :\n",Q)

print("\nQ^TQ:\n",Q.T@Q)

print("\nUpper Triangular Matrix R : \n",R)

print("\nA=QR=\n",Q@R)
