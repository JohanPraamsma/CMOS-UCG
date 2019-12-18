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
