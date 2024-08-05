
import taichi as ti
import numpy as np
# *Problem : Using lines which would be hard to modify when the grid curves
ti.init(arch=ti.gpu)

gui = ti.GUI('Grid', res=(800, 800))

dx, dy = 10,10
precision = 5
WIDTH = 100
HEIGHT = 100

#! Doesn't work for some reason  

while gui.running:
    
    
    for x in np.round(np.linspace(0, WIDTH, int(WIDTH/dx)+1),precision):
        for y in np.round(np.linspace(0, HEIGHT, int(HEIGHT/dy)+1),precision):
        #draw dx dy rectangle
            gui.line(begin = [x,y],end = [x+dx,y],radius = 1,color = 0x068587)
            gui.line(begin = [x,y],end = [x,y+dy],radius = 1,color = 0x068587)
            gui.line(begin = [x+dx,y],end = [x+dx,y+dy],radius = 1,color = 0x068587)
            gui.line(begin = [x,y+dy],end = [x+dx,y+dy],radius = 1,color = 0x068587)

    
    gui.line(begin=[0,0],end=[400,400],radius=1,color = 0xED553B)   
    gui.show()