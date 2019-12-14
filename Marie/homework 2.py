import matplotlib.pyplot as plt 
import numpy as np 

def function(x):
    return (x**5 + 1)

def root(xL, xU, ec): 
    if function(xL)*function(xU) > 0:
        print("wrong guess of limits")
        return None  
    error = 100
    while error > ec: 
        r = xU - function(xU)*(xL - xU)/(function(xL) - function(xU))
        
        if r == 0.:
            return r 
        elif function(r) * function(xL) > 0:
            xL = r 
            error = (r - xL)/r            
            print(xL)
        elif function(r) * function(xL) < 0: 
            xU = r 
            error = (r - xU)/ r
        print("value at new root", function(r), r)
    return r 
    
root(-2, 0) 
