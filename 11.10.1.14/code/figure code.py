import numpy as np
import matplotlib.pyplot as plt

x = np.array([1985, 1995])
y = np.array([92, 97])

plt.plot(x,y, marker = 'o')
plt.plot (x, y)
plt.annotate ("A (1985, 92)", (1985, 91.1))
plt.annotate ("B (1995, 97)", (1995, 97.4)) 

plt.xlim(1980, 2005)
plt.ylim(88,100)
plt.xlabel("Years")
plt.ylabel("Population in Crores")
plt.savefig("fig1.png")
