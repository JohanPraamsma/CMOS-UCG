import matplotlib.pyplot as plt

def two_equations(a1, b1, c1, a2, b2, c2):
    solution = []
    x2 = (a2*c1 - a1*c2)/(a1*b2 - a2*b1)
    solution.append(x2)
    if a1 != 0:
        x1 = (-b1*x2 - c1)/a1
        solution.append(x1)
    else:
        x1 = (-b2*x2 - c2)/a2
        solution.append(x1)
    return solution

two_equations(3, 5, 6, 2, 4, -1)
