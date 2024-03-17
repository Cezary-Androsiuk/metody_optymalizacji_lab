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

def fp(x):
    return 6 * (x**2) + 6 * x - 36

x = np.linspace(-6, -1, 100)

plt.plot(x, f(x), color='black')
plt.plot(x, x*0, '--')
plt.plot(x, fp(x), color='lightgray')


def warunek_konieczny_mbpp(a: float, b: float):
    if fp(a) * fp(b) < 0:
        return m_bisekcji_polowienia_przedzialow(a, b);
    else:
        print("warunek konieczny nie został spełniony")
        return 0



def m_bisekcji_polowienia_przedzialow(a: float, b: float):
    x_sr = (a + b) /2
    if fp(x_sr) == 0:
        plt.plot(x_sr, f(x_sr), 'go')
        return x_sr
    elif abs(fp(x_sr)) < e:
        plt.plot(x_sr, f(x_sr), 'go')
        return x_sr
    elif fp(x_sr) * fp(a) < 0:
        plt.plot([a, x_sr], [f(a), f(x_sr)], 'ro-')
        return m_bisekcji_polowienia_przedzialow(a, x_sr)
    else:
        plt.plot([x_sr, b], [f(x_sr), f(b)], 'ro-')
        return m_bisekcji_polowienia_przedzialow(x_sr, b)
        
    
print(warunek_konieczny_mbpp(start_a, start_b))

plt.show()