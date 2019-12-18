#Exam question 1 Rung-Kutta 

import numpy as np
import matplotlib.pyplot as plt 

def true(x):
    return (-0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1)
    #this is the real function, so the antiderivative of dy/dx 

y0 = 1

def f(x):
    return (-2*x**3 + 12*x**2 - 20*x + 8.5)

def y_2(low, high, step):
    y = y0
    n = int((high - low)/step) #this is een float, so you need to make it an integer 
    true_list = []
    approximation_list = []
    #new value = old value + slope times the step 
    for i in range(n):
        k1 = f(i*step)
        k2 = f(i*step + (step/2))
        #there is no y-dependence so there is no need to add the change of the y-variable it. 
        approximation_list.append(y)
        y = y + k2*step
        true_value = true(i*step)
        true_list.append(true_value)
        true_error = abs((true_value - y)/true_value)
        #print(error)
    return approximation_list, true_list, true_error

y_2(0., 4., 0.5)
