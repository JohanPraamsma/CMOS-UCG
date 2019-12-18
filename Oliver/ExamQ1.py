
import matplotlib.pyplot as plt

def function(x):
    return (-0.5)*x**4 + 4*x**3 -10*x**2 + 8.5*x + 1 
    
def phi(x):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

y0 = 1

def y(h, mini, maxi):
    y2 = y0
    n = int((maxi - mini)/h)
    solutions_app = []
    true = []
    x = []
    for i in range(n):
        solutions_app.append(y2)
        add = function(i*h)
        true.append(add)
        x.append(i*h)
        k1 = phi(i*h)
        k2 = phi(i*h + (0.5)*h)
        y2 = y2 + k2*h
        error = (abs((add - y2)/add)) 
        print(error)
    return solutions_app, true, x

out = y(0.25, 0, 4)

plt.plot(out[2], out[0])
plt.plot(out[2], out[1])


