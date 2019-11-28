import matplotlib.pyplot as plt
import numpy as np


def two_equations(a1, b1, c1, a2, b2, c2):
    solution = []
    x = np.linspace(16,-13,50)
    y1 = (-c1-a1*x)/b1
    y2 = (-c2-a2*x)/b2
    plt.plot(x, y1)
    plt.plot(x, y2)
    x2 = (a2*-c1 - a1*-c2)/(a1*b2 - a2*b1)
    solution.append(x2)
    if a1 != 0:
        x1 = (-b1*x2 +c1)/a1
        solution.append(x1)
    else:
        x1 = (-b2*x2 + c2)/a2
        solution.append(x1)
    return solution

two_equations(3, 2, 18, -1, 2, 2)
