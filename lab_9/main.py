# python -m venv env
# env\Scripts\activate
# where pip

# 1. 8x^3 + y^2 - 3xy - y + 1   start point (1,1)

import numpy as np
from matplotlib import pyplot as plt

# przykład z pdf
start_point = [-0.5, 1]
def f(x, y):
    return  2.5*(x**2 - y)**2 + (1 - x)**2 # wolframalpha min = (1, 1)


# start_point = [1, 1]
# def f(x, y):
#     return  8 * x**3 + y**2 - 3*x*y - y + 1 # wolframalpha min = ( (3+sqrt(73))/32 ~~ 0.360750, (41+3*sqrt(73))/64 ~~ 1.041125 )


# glob_h = 0.1 # global variable
glob_eps = 0.01 # global variable
glob_limit = 1000 # global variable
glob_e = 0.5 # initial step length
glob_n = 2 # numbers of arguments in function
glob_beta = 0.5 # step-down factor, 0 < beta < 1

orthogonalVectors = [
    [1,0],
    [0,1]
]

# make a plot
#################################################################################
plane_height = 6
plane_width = 6
offset_x = 0
offset_y = 0

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


def hookaJeevesa(point):
    run = True
    iterCounter = 0
    testPhase = True
    testPhaseStep = 1
    j = 0 # iterator
    e = glob_e

    # assign start values
    xb = xb0 = x = point[0]
    yb = yb0 = y = point[1]

    fj = fb = f0 = f(x,y)
    
    drawx, drawy = x, y
    while run:
        # test phase
        if testPhase:
            match testPhaseStep:
                case 1:
                    j = 0
                    f0 = f(x,y)
                    fb = f(xb0, yb0)
                    testPhaseStep = 2
                case 2:
                    # go to right
                    x = x + e * orthogonalVectors[j-1][0]
                    y = y + e * orthogonalVectors[j-1][1]
                    fj = f(x, y)
                    testPhaseStep = 3
                case 3:
                    # ckeck if right direction was a good choice
                    if fj < f0:
                        # right was good direction
                        f0 = fj
                        testPhaseStep = 6
                    else:
                        testPhaseStep = 4
                case 4:
                    # oh, no! go back to left 
                    x = x - 2 * e * orthogonalVectors[j-1][0]
                    y = y - 2 * e * orthogonalVectors[j-1][1]
                    fj = f(x, y)
                    testPhaseStep = 5
                case 5:
                    # ckeck if left direction was a good choice
                    if fj < f0:
                        # left was good direction
                        f0 = fj
                    else:
                        # neither left nor right was a good choise direction 
                        x = x + e * orthogonalVectors[j-1][0]
                        y = y + e * orthogonalVectors[j-1][1]
                    testPhaseStep = 6
                case 6:
                    # check if j reached end (n)
                    if j == glob_n:
                        testPhaseStep = 7
                    else:
                        j+=1
                        testPhaseStep = 2
                case 7:
                    if fb > f0:
                        xb = x
                        yb = y
                        testPhase = False
                    else:
                        testPhaseStep = 8
                case 8:
                    if e <= glob_eps:
                        run = False
                    elif glob_limit <= iterCounter:
                        print("reached limit")
                        run = False
                    else:
                        x = xb
                        y = yb
                        e *= glob_beta
                        testPhaseStep = 1
        # work phase
        else:
            x = 2 * xb - xb0
            y = 2 * yb - yb0
            xb0 = xb
            yb0 = yb
            testPhase = True
            testPhaseStep = 1
        
        # if point changed
        if drawx != x or drawy != y:
            # draw line from old point to new
            draw_line((drawx, drawy), (x, y))
            # draw new point
            draw_point((x, y, "red"))
            # set new point as an old
            drawx, drawy = x, y

        iterCounter += 1
        print(f"iter:{iterCounter} step x:{x}, y:{y}")
        

hookaJeevesa(start_point)

plt.show()