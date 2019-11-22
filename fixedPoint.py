import math 

def g(x):
   return math.exp(-x)

def fixedPoint(x, xs):
 
   for i in range(20):
     x_old = x
     x = g(x)
     error = abs(x - x_old)
     if error < xs:
      break
     print('New Root', x, 'error', error)


fixedPoint(-5., 0.01)



