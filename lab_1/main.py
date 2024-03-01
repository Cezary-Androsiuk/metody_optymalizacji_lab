# python -m venv env
# env\Scripts\activate
# where pip
    # C:\Users\cezar\Desktop\Semestr_6\mo-Metody_obliczeniowe\lab\2024-02-27\env\Scripts\pip.exe
    # C:\Users\cezar\AppData\Local\Programs\Python\Python312\Scripts\pip.exe

# 1. [-6, -1]  2x^3 + 3x^2 -36x + 1

import numpy as np
from matplotlib import pyplot as plt


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

start_a = -6.0
start_b = -1.0
e = 0.001

def f(x):
   return 2 * (x**3) + 3 * (x**2) - 36 * x + 1

x = np.linspace(-6, -1, 100)

plt.plot(x, f(x), color='black')

def maximum(a: float, b: float, protector):
    protector += 1
    if protector == 1_000_000:
        print("!PROTECTOR")
        return 0
    
    x_sr = (a + b) / 2
    L = b-a;
    x_1 = a + L/4
    x_2 = b - L/4
    plt.plot([x_1, x_2], [f(x_1), f(x_2)], 'ro-')

    # krok 3
    if f(x_1) > f(x_sr):
    # krok 3a
        b = x_sr
        x_sr = x_1
        # krok 5
        if L <= e: 
            plt.plot(x_sr, f(x_sr), 'go')
            print(f"maximum: x: {x_sr}")
            return x_sr
        else:
            return maximum(a, b, protector)
    else: 
    # krok 3b
        # krok 4
        if f(x_2) > f(x_sr):
            a = x_sr
            x_sr = x_2
        else:
            a = x_1
            b = x_2

        # krok 5
        if L <= e: 
            plt.plot(x_sr, f(x_sr), 'go')
            print(f"maximum: x: {x_sr}")
            return x_sr
        else:
            return maximum(a, b, protector)
        
    
def minimum(a: float, b: float, protector):
    protector += 1
    if protector == 1_000_000:
        print("!PROTECTOR")
        return 0
    
    x_sr = (a + b) / 2
    L = b-a;
    x_1 = a + L/4
    x_2 = b - L/4
    plt.plot([x_1, x_2], [f(x_1), f(x_2)], 'ro-')

    # krok 3
    if f(x_1) < f(x_sr):
    # krok 3a
        b = x_sr
        x_sr = x_1
        # krok 5
        if L <= e: 
            plt.plot(x_sr, f(x_sr), 'go')
            print(f"minimum: x: {x_sr}")
            return x_sr
        else:
            return minimum(a, b, protector)
    else: 
    # krok 3b
        # krok 4
        if f(x_2) < f(x_sr):
            a = x_sr
            x_sr = x_2
        else:
            a = x_1
            b = x_2

        # krok 5
        if L <= e: 
            plt.plot(x_sr, f(x_sr), 'go')
            print(f"minimum: x: {x_sr}")
            return x_sr
        else:
            return minimum(a, b, protector)
        
maximum(start_a, start_b, 0);
minimum(start_a, start_b, 0);


plt.show()