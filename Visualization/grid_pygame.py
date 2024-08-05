'''Somehow draw a grid'''
'''Ideas: Pygame, Matplotlib, taichi lang'''
import math
import pygame as pg 

def drawGrid():
    num_lines = 10
    steps = int(800/num_lines)
    for x in range(0,800,steps):
        pg.draw.line(SCREEN,BLUE,(x,0),(x,800))
    for y in range(0,800,steps):
        pg.draw.line(SCREEN,BLUE,(0,y),(800,y))

BLACK = (0,0,0)
ORANGE = (237,85,59)
BLUE = (6,133,135)



pg.init()
SCREEN = pg.display.set_mode((800,800))
CLOCK = pg.time.Clock()
SCREEN.fill(BLACK)

while True: 
    drawGrid()
    pg.draw.circle(SCREEN,ORANGE,(400,400),10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
                
    pg.display.update()
    CLOCK.tick(60)


