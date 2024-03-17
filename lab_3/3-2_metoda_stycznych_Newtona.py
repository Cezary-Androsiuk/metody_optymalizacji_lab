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
# start_a = 1.0
# start_b = 2.0
e = 0.01

def f(x):
    return 2 * (x**3) + 3 * (x**2) - 36 * x + 1
    # return 1/3 * (x**3) + 1/2 * (x**2) - 5 * x + 2

def fp(x):
    return 6 * (x**2) + 6 * x - 36
    # return x**2 + x - 5

def fpp(x):
    return 12 * x + 6
    # return 2 * x + 1

def fppp(x):
    return 12
    # return 2

x = np.linspace(start_a, start_b, 100)

plt.plot(x, f(x), color='black')
plt.plot(x, x*0, '--')
plt.plot(x, fp(x), color='lightgray')


def warunek_konieczny_msn(a: float, b: float):
    if fp(a) * fp(b) >= 0:
        print("warunek konieczny nie został spełniony")
        return 0

    if fpp(a) * fpp(b) >= 0 and fppp(a) * fppp(b) >= 0:
        return m_stycznych_newtona(a, b);
    else:
        print("waruneki zbieżności nie zostały spełnione")
        return 0



def m_stycznych_newtona(a: float, b: float):
    if fppp(a) * fp(a) >= 0:
        x_0 = a
    else:
        x_0 = b

    x_n_old = x_0
    x_n = x_0 - fp(x_0) / fpp(x_0)
    
    while abs(fp(x_n)) >= e and abs(x_n - x_n_old) >= e:
        x_n_old = x_n
        x_n = x_n - fp(x_n) / fpp(x_n)
        plt.plot([x_n_old, x_n], [f(x_n_old), f(x_n)], 'ro-')

    plt.plot(x_n, f(x_n), 'go')
    return x_n
    
print(warunek_konieczny_msn(start_a, start_b))

plt.show()