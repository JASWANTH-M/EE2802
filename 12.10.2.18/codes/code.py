import numpy as np
import matplotlib.pyplot as plt

x = np.array ([1,4,6,1])
y = np.array ([1,10,3,1])

plt.plot (x, y)
plt.annotate ("A", (0.9,1.1))
plt.annotate ("B", (6.1, 2.9))
plt.annotate ("C", (4.1, 10.1))
plt.savefig("ffig.png")
