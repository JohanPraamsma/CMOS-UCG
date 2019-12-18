#!/usr/bin/env python
# coding: utf-8

# In[119]:


import matplotlib.pyplot as plt

def function(x):
    return (-0.5)*x**4 + 4*x**3 -10*x**2 + 8.5*x + 1 
    
def phi(x):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

y0 = 1

def y(h, mini, maxi):
    y2 = y0
    n = int((maxi - mini)/h)
    solutions_app = []
    true = []
    x = []
    for i in range(n):
        solutions_app.append(y2)
        add = function(i*h)
        true.append(add)
        x.append(i*h)
        k1 = phi(i*h)
        k2 = phi(i*h + (0.5)*h)
        y2 = y2 + k2*h
        error = (abs((add - y2)/add)) 
        print(error)
    return solutions_app, true, x

out = y(0.25, 0, 4)

plt.plot(out[2], out[0])
plt.plot(out[2], out[1])


# In[120]:


import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(37)
x = rng.rand(200)
y = 3*x**7 + x + rng.randn(200)
y3 = 3*x**7 + x
plt.scatter(x, y)
plt.scatter(x, y3)

def F(x, y, a, c):
    e = 0.
    for i in range(len(y)):
        e = e + (y[i] - ((-a*x**7)[i] + c*x[i]))**2
    return e/(2*(len(y)))

F(x, y, 3, 1)

def derivative(x, y, a, c):
    f = y - (-a*x**7 + c*x)
    dfa = f*(-x**7)
    dfc = f*(x)
    return np.sum(dfa)/len(y), np.sum(dfc)/len(y)

print(derivative(x, y, 3, 1))

def gradient_descent(x, y, a, c):
    for i in range(100000):
        df = derivative(x, y, a, c)
        a -= 0.00001*(abs(df[0]))
        c -= 0.00001*df[1]
    return a, c

solution = gradient_descent(x, y, 3.5, 1.4)
y2 = solution[0]*(x**7) + solution[1]*x

plt.scatter(x, y2)


# In[ ]:




