"""
Our goal is to conduct PCA 
This is multi-line comment
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


x = np.linspace(1,10)




# Artificial data, category 1
n = 20
m = 100
A = np.random.rand(m,n)
# Artificial data, category 2
B = np.random.rand(m,n) + 0.2
# M is a feature matrix, copntaining categories 1 and 2
M = np.concatenate((A, B), axis=0)



# First step: Normalize
N = M-M.mean(0)

# Second step: inner product
O = N.T @ N

# eigen
w, v = np.linalg.eig(O)

idx = w.argsort()[::-1]   
w = w[idx]
v = v[:,idx]

x = M @ v[:,0]
y = M @ v[:,1]
z = M @ v[:,2]

fig = plt.figure(1)
fig.clf()
plt.scatter(x[0:m-1],y[0:m-1])
plt.scatter(x[m:-1],y[m:-1])
plt.show()

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[0:m-1],y[0:m-1], z[0:m-1])
ax.scatter(x[m:-1],y[m:-1], z[m:-1])
plt.show()
