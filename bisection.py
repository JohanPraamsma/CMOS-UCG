from math import exp

def f(c):
  return 668.06/c * (1-exp(-0.146843*c))-40

def bisection(xl, xu):
   if f(xl)*f(xu)>0:
     print("Stupid Guess, will not work")
     return None
   for i in range(100):
     root = (xl+xu)/2.
     if f(root)== 0.:
        return root
     elif f(root) * f(xl) > 0:
        xl = root
     elif f(root) * f(xl) < 0:
        xu = root 
     print('value at new root', f(root), root)
   return root


bisection(14, 16)
