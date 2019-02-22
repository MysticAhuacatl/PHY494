# Problem 2

import numpy as np
positions = np.array(
    [[0.0, 0.0, 0.0], [1.34234, 1.34234, 0.0],
     [1.34234, 0.0,  1.34234], [0.0, 1.34234, 1.34234]])
t = np.array([1.34234, -1.34234, -1.34234])

# replace NotImplemented with your solution

# (c)
result2c = positions[1]


# (d) (i)
result2d = positions[1][1]


# (e)
problem2e = positions[:]
for i in problem2e:
     i += t
result2e = problem2e[:]


# (f)
def translate(coordinates, t):
    for i in coordinates:
        i += t
    return coordinates
