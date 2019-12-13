import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(42)
x = 10 * rng.rand(300)
y = 2*x**2 + 10*x - 1 + 10*rng.randn(300)
plt.scatter(x, y)
#plt.plot(x, 2*x**2 + 10*x - 1)

def F(x, y, a, b, c):
    e = 0.
    for i in range(len(y)):
        e = e + (y[i] - ((a*x**2)[i] + b*x[i] + c))**2
    return e/(2*(len(y)))

F(x, y, 2, 10, -1)

def derivative(x, y, a, b, c):
    f = y - (a*x**2 + b*x + c)
    dfa = f*(-x**2)
    dfb = f*(-x)
    dfc = f*(-1)
    return np.sum(dfa)/len(y), np.sum(dfb)/len(y), np.sum(dfc)/len(y)

print(derivative(x, y, 2, 10, -1))
#print((F(x, y, 2.0001, 10, -1) - F(x, y, 2, 10, -1))/0.0001) 
#print((F(x, y, 2, 10.0001, -1) - F(x, y, 2, 10, -1))/0.0001)
#print((F(x, y, 2, 10, -0.9999) - F(x, y, 2, 10, -1))/0.0001)

def gradient_descent(x, y, a, b, c):
    function = []
    midpoints = []
    for n in range(100):
        for i in range(1000):
            df = derivative(x, y, a, b, c)
            a = a - 0.00001*df[0]
            b = b - 0.00001*df[1] 
            c = c - 0.00001*df[2]
            f = a*x**2 + b*x + c
            function.append(f)
        add = [a, b, c]
        midpoints.append(add)
    return round(a), round(b), round(c), function, midpoints

solution = gradient_descent(x, y, 3, 15, 1)
y2 = solution[0]*(x**2) + solution[1]*x + solution[2]
x2 = np.linspace(0, 10, 300)

pp = solution[4]


for i in range(len(pp) - 1):
    y3 = pp[i][0]*(x2**2) + pp[i][1]*x2 + pp[i][2]
    plt.plot(x2, y3)
    
    
plt.scatter(x, y2)
