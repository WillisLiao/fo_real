import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
import random as rand

a = rand.randint(1, 10)
b = rand.randint(1, 10)
def fun1(x):
    return a*x**2 + b


x = Symbol('x')




plt.xlabel('x')
plt.ylabel('y')
xr = np.linspace(-10, 10, 100)
y1r = fun1(xr)

plt.plot(xr,y1r,'b-')   #b是blue , -是實線




plt.xlim(-10, 10)
plt.ylim(-10, 20)
plt.grid()
plt.show()