import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = np.exp(x) - x


plt.plot(x, y)
#visible from the graph that function does not have a root
print("The function does not have a root.")

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return np.exp(x) - x

def lowest_point(xu, xl, error):
    ec = 100
    while ec > error:
        xn = (xu + xl)/2
        value = function(xn)
        if function(xl) * value < 0:
            ec = (xu - xn)/xn * 100
            xu = xn
        elif function(xu) * value < 0:
            ec = (xl - xn)/xn * 100
            xl = xn
        else:
            ec = 0
    return xn
    
print("The lowest point of the function is:", lowest_point(3, -3, 5))

#function to find the root of the equation that has a root
#returns 'That's a bad guess' for given function, regardless of numbers
def root_bisection(xu, xl, error):
    ec = 100
    if function(xu) * function(xl) > 0:
        return print("That's a bad guess.")
    else:
        while ec > error:
            xn = (xu + xl)/2
            value = function(xn)
            if function(xl) * value < 0:
                ec = (xu - xn)/xn * 100
                xu = xn
            elif function(xu) * value < 0:
                ec = (xl - xn)/xn * 100
                xl = xn
            else:
                ec = 0
        return xn
    
root_bisection(2, -2, 10)
