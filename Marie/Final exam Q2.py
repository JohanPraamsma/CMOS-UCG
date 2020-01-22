import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - x
    #e^x - x 

#bisection method
def root_bisection(xU, xL):
    if function(xU) * function(xL) > 0:
        return print("Wrong guess")
    else:
        for i in range(100):
            x_new = (xU + xL)/2
            f_new = f(x_new)
            #function f for the new value 
            if f(xL) * f_new < 0:
                xU = x_new
            elif f(xU) * f_new < 0:
                xL = x_new 
            else:
                return x_new
        return x_new
    

root_bisection(2, 3)


x = np.linspace(-1, 0.5, 100)
y = np.exp(x) - x
#array with all elements = 0 with length of the array of x

plt.plot(x, y)
