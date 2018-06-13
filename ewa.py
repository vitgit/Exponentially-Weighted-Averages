import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,100)
y = np.sin(x) + np.random.random(100) * 0.5

bet = 0.8
# v = v*bet + (1 - bet)*y
v = []
v.append(0.)
for ii in range(x.size):
    print (ii)
    vv = v[ii]*bet + (1. - bet)* y[ii]
    v.append(vv)
v.pop(0)
print (v)
v = np.array(v)
print (v)
print (x.size, v.size)

plt.plot(x,y, 'o')
plt.plot(x,v)
plt.show()