# Solution for BONUS Problem 3c

import numpy as np
import matplotlib.pyplot as plt

def zeta(s, Nmax=1000):
    """Approximation to the real Riemann zeta function"""
    # This advanced solution uses broadcasting between the arange
    # array (reshaped to have shape (Nmax, 1)) and the array of s
    # values. Then sum over the "arange" axis (axis=0) to get one
    # value for each s. This allows use of the function as a "numpy
    # ufunc", i.e., one that operates on whole arrays.
    #
    # Instead of 1/k^s we write k^(-s).
    return np.sum(
        np.power(
            np.arange(1, Nmax+1, dtype=np.float64)[:, np.newaxis],
            -s), axis=0)

s = np.arange(1, 10, 0.1)
Nmax_values = np.array([10, 100, 1000, 100000])

fig = plt.figure(figsize=(6, 6))   # new figure
ax = fig.add_subplot(111)          # add "axes", i.e., graph to figure

# plot each graph into the same axes and label by Nmax
for Nmax in Nmax_values:
   ax.plot(s, zeta(s, Nmax=Nmax), label="Nmax="+str(Nmax))

# finish the axes by adding labels and legend
ax.set_xlabel(r"$s$")         # fancy LaTeX typeset label
ax.set_ylabel(r"$\zeta(s)$")  # fancy LaTeX typeset label
ax.legend(loc="best")         # place legends

fig.savefig("zeta.png")


