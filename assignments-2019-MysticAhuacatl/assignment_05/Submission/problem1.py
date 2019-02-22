# Problem 1

import numpy as np

sx = np.array([[0, 1], [1, 0]])
sy = np.array([[0, -1j],[1j, 0]])
sz = np.array([[1, 0], [0, -1]])

# replace NotImplemented with your solution

# b (i)
result1b1 = sx * sy * sz


# b (ii)
result1b2 = np.dot(np.dot(sx,sy),sz)


# b (iii)
result1b3 = np.dot(sx,sy) - np.dot(sy,sx)


# b (iv)
v = np.array([1/np.sqrt(2), (-1j)/np.sqrt(2)])
result1b4 = v.conjugate()
