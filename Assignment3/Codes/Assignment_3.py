import numpy as np

x=5
y=2
z=9
a=3
b=7
c=12

V= np.array([[x,a,x+a],[y,b,y+b],[z,c,z+c]])

print("Determinant of matrix V=",np.linalg.det(V))
