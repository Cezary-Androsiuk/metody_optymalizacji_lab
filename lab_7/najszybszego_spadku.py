# python -m venv env
# env\Scripts\activate
# where pip

# 1. 8x^3 + y^2 - 3xy - y + 1   start point (1,1)

import numpy as np
from matplotlib import pyplot as plt

h = 0.00001
e = 0.01
max_iterations = 1000
start_point = [1, 1]
# start_point = [10,12]

def f(x, y):
    return  8 * x**3 + y**2 - 3*x*y - y + 1
    # return  10 * x**2 + 12*x*y + 10 * y**2


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


# make a plot
#################################################################################
# plane_height = 30
# plane_width = 30
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


def matrix_subtract(a, b): # [] - []
    return np.subtract(a, b)

def matrix_multiply(a, b): # [] * []
    return np.matmul(a, b)

def matrix_division(a, b): # [] / []
    return np.divide(a, b)

def matrix_invert(a): # []^{-1}
    return np.linalg.inv(a)

def matrix_transpose(a): # []^{T}
    return a.getT();


def najszybszego_spadku(in_point, iter=0):
    # dodatek
    if(iter >= max_iterations):
        return in_point
    
    # dodatek
    if(abs(in_point[0]) > plane_width/2 + offset_x 
       or abs(in_point[1]) > plane_height/2 + offset_y):
        return in_point;

    current_vec_of_axes = np.matrix( # x_k
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

    up = matrix_multiply(matrix_transpose(gradient), gradient)
    down = matrix_multiply(matrix_multiply(
        matrix_transpose(gradient),macierz_Hessego), gradient)
    ak = up[0,0] / down[0,0] # a_k

    next_vec_of_axes = matrix_subtract(
        current_vec_of_axes,
        ak * gradient
    )
    
    gradient_norm = np.linalg.norm(next_vec_of_axes)

    out_point = [next_vec_of_axes[0,0], next_vec_of_axes[1,0]]

    draw_line(in_point, out_point)

    # print(out_point)

    if gradient_norm <= e \
        or (abs(out_point[0] - in_point[0]) <= e 
            and abs(out_point[1] - in_point[1]) <= e):
        
        draw_point(out_point)
        return out_point
    
    najszybszego_spadku(out_point, iter+1)


# random
import random
for i in range(100):
    x = plane_width/2 + offset_x
    y = plane_height/2 + offset_y
    # print(x, y)
    rnd_x = random.uniform(0, x)
    rnd_y = random.uniform(0, y)
    najszybszego_spadku([rnd_x, rnd_y])
    # print()
    
# najszybszego_spadku([-0.5, 2.75])

# najszybszego_spadku(start_point)

plt.show()
