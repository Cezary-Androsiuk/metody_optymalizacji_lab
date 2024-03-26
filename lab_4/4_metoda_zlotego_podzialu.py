# python -m venv env
# env\Scripts\activate
# where pip
    # C:\Users\cezar\Desktop\Semestr_6\mo-Metody_obliczeniowe\lab\2024-02-27\env\Scripts\pip.exe
    # C:\Users\cezar\AppData\Local\Programs\Python\Python312\Scripts\pip.exe

# 1. [-6, -1]  2x^3 + 3x^2 -36x + 1

import numpy as np
from matplotlib import pyplot as plt
from math import sqrt


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

start_a = -6.0
start_b = -1.0
e = 0.001

def f(x):
   return 2 * (x**3) + 3 * (x**2) - 36 * x + 1

k = (sqrt(5) - 1) / 2

x = np.linspace(-6, -1, 100)

plt.plot(x, f(x), color='black')



def m_zlotego_podzialu_maximum(a: float, b: float):
    x_1 = b - k * (b-a)
    x_2 = a + k * (b-a)

    while abs(x_2 - x_1) >= e:
        if f(x_1) > f(x_2):
            plt.plot([x_1, x_2], [f(x_1), f(x_2)], 'ro-')
            b = x_2
            x_2 = x_1
            x_1 = b - k * (b-a)
        else:
            plt.plot([x_1, x_2], [f(x_1), f(x_2)], 'ro-')
            a = x_1
            x_1 = x_2
            x_2 = a + k * (b-a)

    plt.plot((a+b)/2, f((a+b)/2), 'go')
    return (a+b)/2
        
        

def m_zlotego_podzialu_minimum(a: float, b: float):
    x_1 = b - k * (b-a)
    x_2 = a + k * (b-a)

    while abs(x_2 - x_1) >= e:
        if f(x_1) < f(x_2):
            plt.plot([x_1, x_2], [f(x_1), f(x_2)], 'ro-')
            b = x_2
            x_2 = x_1
            x_1 = b - k * (b-a)
        else:
            plt.plot([x_1, x_2], [f(x_1), f(x_2)], 'ro-')
            a = x_1
            x_1 = x_2
            x_2 = a + k * (b-a)

    plt.plot((a+b)/2, f((a+b)/2), 'go')
    return (a+b)/2
    
print(m_zlotego_podzialu_maximum(start_a, start_b))
print(m_zlotego_podzialu_minimum(start_a, start_b))

plt.show()