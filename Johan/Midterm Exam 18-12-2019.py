# Problem 1

def function(x):
    return(-0.5)*x**4 + 4*x**3 -10*x**2 + 8.5*x + 1 

    
def f(x,y):
    return -2*x**3+12*x**2-20*x+8.5

def RKdifferential(f, y0, h, n):
    y = y0
    for x in range(n):
        k1 = f(x*h, y)
        k2 = f(x*h + h/2, y + 0.5 * k1 * h)
        y = y + k2 * h
        Real = function(x)
        E = (abs((Real - y)/Real)) 
        print(E)
    return E
        
RKdifferential(f,1,0.2,5)

#Problem 2 
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(10)
x = 2 * rng.rand(500)
y = 3*x**7 + x + rng.rand(500)
plt.scatter(x,y)
plt.scatter(x,3*x**7 + x)

def Function(x,y,a,c): 
    E = 0
    for i in range(len(y)):
        E = E + (y[i]-(a*(x[i])**7+c*x[i]))**2
    return E/(2 * len(y))
Function(x,y,3,1)

def dF(x,y,a,c):
    f = y - (a*x**7+c*x)
    dfa = f * (-x**7)
    dfc = f * (-x)
    return np.sum(dfa)/len(y), np.sum(dfc)/len(y)

dF(x,y,3,1)

print((Function(x,y,3.001,1)-Function(x,y,3.0,1))/0.001)
print((Function(x,y,3,1.001)-Function(x,y,3.0,1,))/0.001)

def GD(a,c):
    for i in range(10000):
        df = dF(x,y,a,c)
        a = a - (0.001*df[0])
        c = c - (0.001*df[1])
        
    plt.scatter(x, a*x**7+c*x)
    return a, c

GD(10,20)
