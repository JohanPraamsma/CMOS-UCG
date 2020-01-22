#final exam 

#Question 1 Interpolation 

import math

def f(x):
    return math.log(x, 2)

def inter(x, x0, x1, x2):
    fx0 = f(x0)
    fx1 = f(x1)
    fx2 = f(x2)
    #shows what f is at x0 x1 and x2
    b0 = fx0
    b1 = ((fx1 - fx0)/(x1 -x0))
    b2 = (((fx2 - fx1)/(x2-x1)) - b1) / (x2 - x0) 
    a0 = b0 - b1*x0 + b2*x0*x1 
    a1 = b1 - b2*x0 - b2*x1 
    a2 = b2 
    #all the functions from the sheet 
    fx = a0 + a1*x + a2*(x**2)
    #calculates the value of f given the x0 x1 and x2 
    return fx

inter(2, 1, 4, 6)
