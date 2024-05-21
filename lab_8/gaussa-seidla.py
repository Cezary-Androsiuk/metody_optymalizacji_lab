# python -m venv env
# env\Scripts\activate
# where pip

# 1. 8x^3 + y^2 - 3xy - y + 1   start point (1,1)

import numpy as np
from matplotlib import pyplot as plt

glob_h = 0.1 # global variable
glob_e = 0.0001 # global variable
glob_limit = 1000 # global variable

start_point = [1, 1]
def f(x, y):
    return  8 * x**3 + y**2 - 3*x*y - y + 1 # wolframalpha min = ((3+sqrt(73))/32, (41+sqrt(73))/64)

# pierwsza pochodna po x (d * f) / (d * x)
def df_dx(x, y):
    h = glob_h
    return ( f(x+h, y) - f(x, y) ) / h

# pierwsza pochodna po y (d * f) / (d * x)
def df_dy(x, y):
    h = glob_h
    return ( f(x, y+h) - f(x, y) ) / h

# druga pochodna po x^2 (d^2 * f) / (d * x^2)
def d2f_dx2(x, y):
    h = glob_h
    return ( df_dx(x+h, y) - df_dx(x, y) ) / h

# druga pochodna po y^2 (d^2 * f) / (d * y^2)
def d2f_dy2(x, y):
    h = glob_h
    return ( df_dy(x, y+h) - df_dy(x, y) ) / h


# make a plot
#################################################################################
plane_height = 6
plane_width = 6
offset_x = 3
offset_y = 3

npx = np.linspace(-plane_width/2 + offset_x, plane_width/2 + offset_x, 100)
npy = np.linspace(-plane_height/2 + offset_y, plane_height/2 + offset_y, 100)
x,y = np.meshgrid(npx, npy)
z = f(x, y)
fig, ax = plt.subplots(1, 1) 
# compute what intesivity should be in what point depends on z axes
levels = np.linspace(np.min(z), np.max(z), 100)

# # colors
# import matplotlib.colors as mcolors
# colors = ['blue', 'red']
# num_intermediate_colors = 100
# cmap = mcolors.LinearSegmentedColormap.from_list('intermediate_colors', colors, N=num_intermediate_colors)
# ax.contour(x,y,z, levels=levels, cmap=cmap) 

ax.contour(x,y,z, levels=levels) 
#################################################################################



def draw_line(point1, point2):
    plt.plot([point1[0], point2[0]], [point1[1],point2[1]], 'ro-', alpha=0.4)

def draw_point(point, color="green"):
    plt.scatter(point[0], point[1], color=color, zorder=2)

# metoda stycznych (po x)
def find_better_x(x0, y0):
    for i in range(glob_limit):
        x1 = x0 - df_dx(x0, y0) / d2f_dx2(x0, y0)

        if abs(df_dx(x1, y0)) < glob_e or abs(x1 - x0) < glob_e:
            return x1
        else:
            x0 = x1

# metoda stycznych (po y)
def find_better_y(x0, y0):
    for i in range(glob_limit):
        y1 = y0 - df_dy(x0, y0) / d2f_dy2(x0, y0)

        if abs(df_dy(x0, y1)) < glob_e or abs(y1 - y0) < glob_e:
            return y1
        else:
            y0 = y1

# normalizacja, potrzebna do warunku końcowego
def normalize(m):
    return np.linalg.norm(m);

# warunek końcowy
def is_end(x0, y0) -> bool:
    x = df_dx(x0, y0)
    y = df_dy(x0, y0)
    return normalize(np.array([ [x],[y] ])) <= glob_e


def gaussa_seidla(point):
    draw_point(point)
    
    # previous point
    xp = point[0]
    yp = point[1]

    # current point
    x = point[0]
    y = point[1]

    for i in range(glob_limit):
        # sprawdź czy warunek końcowy został spełniony
        if is_end(x, y):
            draw_point((x, y, "red"))
            return x, y

        xp = x
        yp = y

        x = find_better_x(x, y)
        y = find_better_y(x, y)

        draw_line((xp, yp), (x, y))


# random
import random
for i in range(100):
    x = plane_width/2 + offset_x
    y = plane_height/2 + offset_y
    # print(x, y)
    rnd_x = random.uniform(0, x)
    rnd_y = random.uniform(0, y)
    gaussa_seidla([rnd_x, rnd_y])
    # print()
    
# gaussa_seidla([-0.5, 2.75])

gaussa_seidla(start_point)

plt.show()
