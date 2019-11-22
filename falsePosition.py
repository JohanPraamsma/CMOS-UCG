from math import exp
  
def f(c):
  return 668.06/c * (1-exp(-0.146843*c))-40

def falsePosition(xl, xu):
   if f(xl)*f(xu)>0:
     print("Stupid Guess, will not work")
     return None
   for i in range(5):
     root = xu - f(xu)*(xl-xu)/(f(xl)-f(xu))
     if f(root)== 0.:
        return root
     elif f(root) * f(xl) > 0:
        xl = root
     elif f(root) * f(xl) < 0:
        xu = root
     print('value at new root', f(root), root)
   return root
falsePosition(14, 16)

