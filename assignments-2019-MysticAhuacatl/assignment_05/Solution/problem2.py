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
result2d = positions[1, 1]


# (e)
result2e = positions + t


# (f)
def translate(coordinates, t):
    # add your code and return the translated array
    return coordinates + t

