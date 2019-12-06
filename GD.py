import numpy as np
import matplotlib.pyplot as plt 
rng = np.random.RandomState(42) 
x = 10 * rng.rand(500) 
y=2*x-1 +rng.randn(500)

#x = np.array([1., 3., 5.])
#y = np.array([3., 7., 11.])

def F(y,x,a,b):
    cost = 0.5*np.sum((y-(a*x+b))**2)/len(y)
    return cost

def dF(y,x,a,b):
    f = y-(a*x+b)
    dfa = f*(-x)
    dfb = f*(-1)
    return np.sum(dfa)/len(y), np.sum(dfb)/len(y)


def GD(y,x,a,b,n):
  d = 0.01
  hist=[]
  #df = dF(y,x,a,b)
  for i in range(n):
    df = dF(y,x,a,b)
    a = a - d * df[0]
    b = b - d * df[1]
    hist.append((a,b))
  return a,b, hist

#print((F(y,x,3.01,1)-F(y,x,3.,1))/0.01, dF(y,x,3,1))
#print((F(y,x,3,1.01)-F(y,x,3,1))/0.01, dF(y,x,3,1))

a,b,hist =GD(y,x,5,1, 1000)
print(a,b)
#ym=a*x+b
#plt.scatter(x,y)
#plt.plot(x,ym)
#plt.show()
fig, ax = plt.subplots()
#ax.scatter(x,y)
for i in range(len(hist)):
    ax.cla()
    ym=hist[i][0]*x+hist[i][1]
    ax.plot(x,ym)
    ax.scatter(x,y)
    ax.set_title(str(hist[i]))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)
