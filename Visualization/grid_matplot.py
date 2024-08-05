import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 10, 10)
y = np.linspace(0, 10, 10)

X, Y = np.meshgrid(x, y)

#metric in 2d
def metric(x,y):
    return np.array([[np.sin(y)**2,0],[0,1]])





fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(X, Y, np.zeros_like(X))


# ax2 = fig.add_subplot(122, projection='3d')
# ax2.plot_surface(X_new,Y_new,np.zeros_like(X_new))
plt.show()