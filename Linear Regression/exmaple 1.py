import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0) #gives the same random sequence even different times of execution
x= np.random.rand(100, 1)
y=2+3*x+np.random.rand(100,1)

plt.scatter(x,y,s=10)#s specifies area of scatter in graph
plt.xlabel('x')
plt.ylabel('y')
plt.show()

