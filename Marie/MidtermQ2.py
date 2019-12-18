#Exam question 2 Gradient Descent 

import numpy as np 
import matplotlib.pyplot as plt 

rng = np.random.RandomState(42)
x = 10 * rng.rand(500)
y = 3*(x**7) + x  + 200*rng.randn(500)
plt.scatter(x,y)

def F(x, y, a, b):
    err = 0. 
    n = len(y)
    for i in range(n): 
        err = err + (y[i] - ((a*x**7)[i] + (b*x)[i]))**2
        
    E = err/(2*n)
    return E

F(x, y, 2, -1)
#check derivative 
def derivative(x, y, a, b):
    f = y - (a*(x**7) + b*x)
    dfa = f * (-x**7)
    #first derivative 
    dfb = f * (-x)
    #second derivative 
    return np.sum(dfa)/(len(y)), np.sum(dfb)/(len(y))

derivative(x, y, 2, -1)

dev_check = (F(x, y, 2.001, -1.) - F(x, y, 2.0, -1.))/ (0.001)
dev_check2 = (F(x, y, 2, -0.9999) - F(x, y, 2, -1))/ (0.0001)
#These check if the derivative is correct 

#print(dev_check)
#print(dev_check2)

def GD(x, y, a, b):
    for i in range(10):
        #for a bigger range I get runtimewarning 
        df = derivative(x, y, a, b)
        a = a - (0.001 * df[0])
        b = b - (0.001 * df[1])
    return a, b

print(GD(x,y, 2, -1))
a,b = GD(x,y, 2, -1)
ym = a*x**7 + b*x 
plt.scatter(x,y)
plt.scatter(x,ym)
