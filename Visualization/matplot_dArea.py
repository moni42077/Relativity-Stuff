import numpy as np
import matplotlib.pyplot as plt

'''             dx
y+dy    +-------------------+
        |                   |
        |                   |
    dy  |                   | dy
        |                   |
        |                   |
y       +-------------------+
        x                 x+dx
        
        will become 
        
                      dx_new
y+y_offset       +-------------+
                /             /
        dy_new /             / dy_new
              / θ           /
y            +-------------+
             x           x+dx_new
        
'''
# We want to plot the grid by seperating it into small rectangles dx by dy
fig, axs = plt.subplots(2)
fig.suptitle("Spacetime")

dx, dy = 1,1
precision = 5
WIDTH = 10 
HEIGHT = 10 

def metric(x,y):
    return np.array([[np.sin(y)**2,0],[0,1]])

for x in np.round(np.linspace(0, WIDTH, int(WIDTH/dx)+1),precision):
    for y in np.round(np.linspace(0, HEIGHT, int(HEIGHT/dy)+1),precision):
        #draw dx dy rectangle
        axs[0].plot([x,x+dx],[y,y],color = 'blue')
        axs[0].plot([x,x],[y,y+dy],color = 'blue')
        axs[0].plot([x+dx,x+dx],[y,y+dy],color = 'blue')
        axs[0].plot([x,x+dx],[y+dy,y+dy],color = 'blue')

        
for x in np.round(np.linspace(0, WIDTH, int(WIDTH/dx)+1),precision):
    for y in np.round(np.linspace(0, HEIGHT, int(HEIGHT/dy)+1),precision):
        #draw dx dy rectangle
        g_xx = metric(x,y)[0][0]
        g_yy = metric(x,y)[1][1]
        g_xy = metric(x,y)[0][1]
        
        if g_xy == 0: 
            cos_theta = 0 
        else:
            cos_theta = g_xy/(np.sqrt(g_xx)*np.sqrt(g_yy))
        
            
        dx_new = np.sqrt(g_xx) * dx
        dy_new = np.sqrt(g_yy) * dy 
        
        sin_theta = np.sqrt(1-cos_theta**2)
        
        x_offset = cos_theta * dy_new
        y_offset = sin_theta * dy_new
        axs[1].plot([x,x+dx_new],[y,y],color = 'blue')
        axs[1].plot([x,x+x_offset],[y,y+y_offset],color = 'blue')
        axs[1].plot([x+dx_new,x+dx_new + x_offset], [y,y+y_offset],color = 'blue')
        axs[1].plot([x+x_offset,x+dx_new + x_offset], [y+y_offset,y+y_offset],color = 'blue')
        
         
        
plt.show()