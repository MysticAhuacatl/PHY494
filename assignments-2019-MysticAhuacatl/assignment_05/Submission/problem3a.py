import matplotlib.pyplot as plt
import numpy as np

X = np.arange(-6,6,0.2)
Y = np.sinc(X)
plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y = sinc(x)")
plt.savefig("sinc.png")
