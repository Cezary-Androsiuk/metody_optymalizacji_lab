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

method = 1

if method == 1:
    start_a = -6.0
    start_b = -1.0
elif method == 0:
    start_a = 1.0
    start_b = 2.0

e = 0.01

def f(x):
    if method == 1:
        return 2 * (x**3) + 3 * (x**2) - 36 * x + 1
    elif method == 0:
        return 1/3 * (x**3) + 1/2 * (x**2) - 5 * x + 2

def fp(x):
    if method == 1:
        return 6 * (x**2) + 6 * x - 36
    elif method == 0:
        return x**2 + x - 5

def fpp(x):
    if method == 1:
        return 12 * x + 6
    elif method == 0:
        return 2 * x + 1

def fppp(x):
    if method == 1:
        return 12
    elif method == 0:
        return 2

x = np.linspace(start_a, start_b, 100)

plt.plot(x, f(x), color='black')
plt.plot(x, x*0, '--')
plt.plot(x, fp(x), color='lightgray')


def warunek_konieczny_ms(a: float, b: float):
    if fp(a) * fp(b) < 0:
        return m_siecznych(a, b);
    else:
        print("warunek konieczny nie został spełniony")
        return 0


def m_siecznych(a: float, b: float):
    if fp(a) * fppp(a) >= 0: # nieruchome a
        x_0 = b

        x_old = x_0
        x_n = x_old - ( fp(x_old) / (fp(x_old) - fp(a)) ) * (x_old - a)

        while abs(fp(x_n)) > e and abs(x_n - x_old) > e:
            x_old = x_n
            x_n = x_old - ( fp(x_old) / (fp(x_old) - fp(a)) ) * (x_old - a)
            plt.plot([x_old, x_n], [f(x_old), f(x_n)], 'ro-')
            
        plt.plot(x_n, f(x_n), 'go')
        return x_n
    
    elif fp(b) * fppp(b) >= 0: # nieruchome b
        x_0 = a

        x_old = x_0
        x_n = x_old - ( fp(x_old) / (fp(b) - fp(x_old)) ) * (b - x_old)

        while abs(fp(x_n)) > e and abs(x_n - x_old) > e:
            x_old = x_n
            x_n = x_old - ( fp(x_old) / (fp(b) - fp(x_old)) ) * (b - x_old)
            plt.plot([x_old, x_n], [f(x_old), f(x_n)], 'ro-')
        
        plt.plot(x_n, f(x_n), 'go')
        return x_n
    
    else:
        print("error")
        return None

print(warunek_konieczny_ms(start_a, start_b))

plt.show()