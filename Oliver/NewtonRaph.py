import math

def function(x):
    return math.exp(-x) - x


def derivative(x):
    return -(math.exp(-x)) - 1


def roots_nr(guess, error):
    ec = 100
    while ec > error:
        xn = guess - (function(guess)/derivative(guess))
        ec = (guess - xn)/xn * 100
        guess = xn
    return xn

roots_nr(1, 0)
