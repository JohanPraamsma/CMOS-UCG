#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Exercise 1: Rung Kutta

import matplotlib.pyplot as plt

def F(x):
    return (-2*x**3 + 12*x**2 - 20*x + 8.5)

def integ(x):
    return (0.5*x**4 + 4*x**3 - 10*x**2 + 8.5)

y_0 = 1

def Y(Min, Max , h):
    y = y_0
    y2 = y_0
    n = int((Max - Min)/h)
    
    true_list = []
    approx_list = []
    new_list = []
    
    for i in range(n):
        k_1 = F(i*h)
        k_2 = F(i*h + 0.5*h)
        
        approx_list.append(y)
        
        y += k2*h

        true_list.append(integ(i*h))
        
        E = (integ(i*h) - y)/(integ(i*h))
        
        
    return (approx_list, true_list, E)



# In[ ]:


#Exercise 2: Gradient Descent

import numpy as np

rng = np.random.RandomState(42)
x = 2*rng.rand(50)
y = 3*x**7 + x + 2*rng.randn(50)

plt.scatter(x,y)


def f(x, y, a, b):
    e = 0.
    n = len(y)
    for i in range(n):
        e += (y[i] -((a*x**3)[i] + b*x))**2
    E = e/(2*n)
    
    return (E)

f(x, y, 3, 1)



def dF(x, y, a, b):
    n = len(y)
    f = y - (a*x**7 + b*x)
    d_fa = f*(-x**7)
    d_fb = f*(-x)
    return (np.sum(d_fa)/n, np.sum(d_fb)/n)

print(dF(x, y, 3., 1.))


def GD(x, y, a, b):
    function = []
    for i in range(100000):
        
        d_f = dF(x, y, a, b)
        a = a - 0.00001*d_f[0] 
        b = b - 0.00001*d_f[1]
        f = a*x**7 + b*x
        
        function.append(f)
        
    return (round(a), round(b), function)


def GD(x, y, a, b):
    function = []
    for i in range(100000):
        d_f = dF(x, y, a, b)
        
        a = a - 0.00001*d_f[0] 
        b = b - 0.00001*d_f[1]
        
        f = a*x**7 + b*x
        
        function.append(f)
        
    return round(a), round(b), function

GD(x, y, 3, 1)






# In[ ]:





# In[ ]:




