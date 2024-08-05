import math 
import pygame as pg 
import numpy as np

'''Check matplot_dArea.py for explanation'''
def metric(x,y):
    return np.array([[0.2,0],[0,5]])
    return np.array([[np.sin(y)**2,0],[0,1]])

BLACK = (0,0,0)
BLUE = (6,133,135)


pg.init()
SCREEN = pg.display.set_mode((500,500))
CLOCK = pg.time.Clock()
SCREEN.fill(BLACK)
dx,dy = 10,10
precision = 5 
WIDTH = 200
HEIGHT = 200

while True: 
    
    
    for x in np.round(np.linspace(250, 250+WIDTH, int(WIDTH/dx)+1),precision):
        for y in np.round(np.linspace(250, 250+HEIGHT, int(HEIGHT/dy)+1),precision):
        #draw dx dy rectangle
            
            pg.draw.line(SCREEN,BLUE, (x,y),(x+dx,y))
            pg.draw.line(SCREEN,BLUE, (x,y), (x,y+dy))
            pg.draw.line(SCREEN,BLUE, (x+dx,y) , (x+dx,y+dy))
            pg.draw.line(SCREEN,BLUE, (x,y+dy), (x+dx,y+dy))
    
    for x in np.round(np.linspace(20, 20+WIDTH, int(WIDTH/dx)+1),precision):
        for y in np.round(np.linspace(20,20+ HEIGHT, int(HEIGHT/dy)+1),precision):
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
            
            pg.draw.line(SCREEN,BLUE, (x,y),(x+dx_new,y))
            pg.draw.line(SCREEN,BLUE, (x,y), (x+x_offset,y+y_offset))
            pg.draw.line(SCREEN,BLUE, (x+dx_new,y) , (x+dx_new + x_offset,y+y_offset))
            pg.draw.line(SCREEN,BLUE, (x+x_offset,y+y_offset), (x+dx_new+x_offset,y+y_offset))
            
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
                
    pg.display.update()
    CLOCK.tick(60)