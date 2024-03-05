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

def fib(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def maximum(a: float, b: float):
    
    n_limit = 2 * e
    n = 0
    while (b-a)/fib(n) >= n_limit:
        n += 1
    n -= 1

    x_1 = b - (fib(n-1)/fib(n)) * (b - a)
    x_2 = a + (fib(n-1)/fib(n)) * (b - a)

    protector = 0
    while abs(x_2 - x_1) >= e:
        if protector == 100_000:
            print("!PROTECTOR")
            return 0
        else:
            protector += 1

        plt.plot((a+b)/2, f((a+b)/2), 'go')

        if f(x_1) > f(x_2):
            b = x_2
            x_2 = x_1
            n = n + 1
            x_1 = b - (fib(n-1)/fib(n)) * (b - a)
        else:
            a = x_1
            x_1 = x_2
            n = n - 1
            x_2 = a + (fib(n-1)/fib(n)) * (b - a)

    # print(protector)
    return (a+b)/2
    

        
    
def minimum(a: float, b: float):
    
    n_limit = 2 * e
    n = 0
    while (b-a)/fib(n) >= n_limit:
        n += 1
    n -= 1

    x_1 = b - (fib(n-1)/fib(n)) * (b - a)
    x_2 = a + (fib(n-1)/fib(n)) * (b - a)

    protector = 0
    while abs(x_2 - x_1) >= e:
        if protector == 100_000:
            print("!PROTECTOR")
            return 0
        else:
            protector += 1

        plt.plot((a+b)/2, f((a+b)/2), 'bo')

        if f(x_1) < f(x_2):
            b = x_2
            x_2 = x_1
            n = n + 1
            x_1 = b - (fib(n-1)/fib(n)) * (b - a)
        else:
            a = x_1
            x_1 = x_2
            n = n - 1
            x_2 = a + (fib(n-1)/fib(n)) * (b - a)

    # print(protector)
    return (a+b)/2
        
print(maximum(start_a, start_b));
print(minimum(start_a, start_b));


plt.show()