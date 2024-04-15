# python -m venv env
# env\Scripts\activate
# where pip

# 1. 8x^3 + y^2 - 3xy - y + 1   start point (1,1)

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors
import random

def f(x, y):
    return  8 * x**3 + y**2 - 3*x*y - y + 1
    # return  10 * x**2 + 12*x*y + 10 * y**2

h = 0.00001
e = 0.001
start_point = [1, 1]
# start_point = [10,12]

def p_x(x, y): # pochodna po x
    return (f(x+h, y) - f(x, y)) / h

def p_y(x, y): # pochodna po y
    return (f(x, y+h) - f(x, y)) / h

def pp_x(x, y): # druga pochodna po x
    return (f(x+(2*h), y) - 2*f(x+h, y) + f(x, y)) / (h**2)

def pp_y(x, y): # druga pochodna po y
    return (f(x, y+(2*h)) - 2*f(x, y+h) + f(x, y)) / (h**2)

def p_xy(x, y): # pochodna po x i y
    return (f(x+h, y+h) - f(x+h, y) -f(x, y+h) + f(x, y)) / (h**2)



# make an enviroment
npx = np.linspace(-4, 4, 100)
npy = np.linspace(-4, 4, 100)
x,y = np.meshgrid(npx, npy)
z = f(x, y)
fig, ax = plt.subplots(1, 1) 
# compute what intesivity should be in what point depends on z axes
levels = np.linspace(np.min(z), np.max(z), 100)

# colors
colors = ['blue', 'red']
num_intermediate_colors = 100
cmap = mcolors.LinearSegmentedColormap.from_list('intermediate_colors', colors, N=num_intermediate_colors)

ax.contour(x,y,z, levels=levels, cmap=cmap) 



def draw_line(point1, point2):
    plt.plot([point1[0], point2[0]], [point1[1],point2[1]], 'ro-')

def draw_point(point, color="green"):
    plt.scatter(point[0], point[1], color=color, zorder=2)

def metoda_newtona(in_point):

    current_vec_of_axes = np.matrix(
        [[in_point[0]],
         [in_point[1]]]
    )
    gradient = np.matrix(
        [[p_x(in_point[0], in_point[1])],
         [p_y(in_point[0], in_point[1])]]
    )
    macierz_Hessego = np.matrix(
        [[pp_x(in_point[0], in_point[1]), p_xy(in_point[0], in_point[1])],
         [p_xy(in_point[0], in_point[1]), pp_y(in_point[0], in_point[1])]]
    )

    # x_k + 1
    next_vec_of_axes = np.subtract(
        current_vec_of_axes, 
        np.matmul(
            np.linalg.inv(macierz_Hessego), 
            gradient
        )
    )
    gradient_norm = np.linalg.norm(next_vec_of_axes)

    out_point = [next_vec_of_axes[0,0], next_vec_of_axes[1,0]]

    draw_line(in_point, out_point)

    print(out_point)

    if gradient_norm <= e \
        or (abs(out_point[0] - in_point[0]) <= e 
            and abs(out_point[1] - in_point[1]) <= e):
        
        draw_point(out_point)
        return out_point
    
    metoda_newtona(out_point)


# for i in range(20):
#     rnd_x = random.uniform(-4, 4)
#     rnd_y = random.uniform(-4, 4)
#     metoda_newtona([rnd_x, rnd_y])
#     print()
    
metoda_newtona(start_point)

plt.show()
