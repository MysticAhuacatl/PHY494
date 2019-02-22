# Problem 1

import numpy as np

sx = np.array([[0, 1], [1, 0]])
sy = np.array([[0, -1j],[1j, 0]])
sz = np.array([[1, 0], [0, -1]])

# replace NotImplemented with your solution

# b (i)
result1b1 = sx * sy * sz


# b (ii)
result1b2 = sx.dot(sy.dot(sz))


# b (iii)
result1b3 = sx.dot(sy) - sy.dot(sx)


# b (iv)
v = 1/np.sqrt(2) * np.array([1, -1j])
result1b4 = v.conjugate().T.dot(sy.dot(v))


