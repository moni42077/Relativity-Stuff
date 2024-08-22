import numpy as np
import taichi as ti

# *Problem : Using lines which would be hard to modify when the grid curves
ti.init(arch=ti.gpu)

gui = ti.GUI("Grid", res=(800, 800))
# flat grid
num_lines = 10
r = 5
d = 1 / num_lines
vertical0 = np.array([[round(i * d, r), 0] for i in range(num_lines)])
vertical1 = np.array([[round(i * d, r), 1] for i in range(num_lines)])

horizontal0 = np.array([[0, round(i * d, r)] for i in range(num_lines)])
horizontal1 = np.array([[1, round(i * d, 4)] for i in range(num_lines)])

obj = [0.5, 0.5]
while gui.running:
    gui.lines(begin=vertical0, end=vertical1, radius=1, color=0x068587)
    gui.lines(begin=horizontal0, end=horizontal1, radius=1, color=0x068587)
    gui.circle(pos=obj, radius=10, color=0xED553B)
    gui.show()
