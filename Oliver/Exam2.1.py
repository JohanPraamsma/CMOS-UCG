import math

def f(x):
    return math.log(x, 2)

def inter(x, x0, x1, x2):
    b0 = f(x0)
    b1 = (f(x1) - f(x0))/(x1 - x0)
    b2 = (((f(x2) - f(x1))/(x2 - x1)) - ((f(x1) - f(x0))/(x1 - x0)))/(x2 - x0)
    a0 = b0 - b1*x0 + b2*x0*x1
    a1 = b1 - b2*x0 - b2*x1
    a2 = b2
    fx = a0 + a1*x + a2*x**2
    return fx

print("Calculated value is:", inter(3, 1, 4, 6))
print("Exact value is:", f(3))
