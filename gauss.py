import numpy as np
import time
"""
a = np.array( [[6., -2., 2., 4.],
               [12., -8., 6., 10.],
               [3., -13., 9., 3.],
               [-6., 4., 1., -18.]])

"""
a = [[6., -2., 2., 4.],
     [12., -8., 6., 10.],
     [3., -13., 9., 3.],
     [-6., 4., 1., -18.]]


b = [16., 26., -19., -34.]
"""
def gauss(a): 
   n = len(a)
   for j in range(n-1):
     for i in range(j+1, n):
       factor = a[i][j]/a[j][j]
       a[i] = a[i] - factor * a[j]
   return (a)
"""
def gauss(a, b):
   n = len(a)
   for k in range(n-1):
     print("I'm in pivot", k)
     for i in range(k+1, n):
       print("I'm in row", i)
       factor = a[i][k]/a[k][k]
       print("my factor is ", a[i][k], "divided by", a[k][k], "which is", factor)
       for j in range(k, n):
         print("I'm subtracting", factor, "multiplied by", a[k][j], "from", a[i][j]) 
         a[i][j] = a[i][j] - factor * a[k][j]
       b[i] = b[i] -factor * b[k]
   return (a)

print(a)
t1 = time.time()
for i in range(100):
  gauss(a,b)
t2 = time.time()-t1
print('time used', t2)
