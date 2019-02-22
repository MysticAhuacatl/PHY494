import numpy as np

positions = np.array(\
      [[0.0, 0.0, 0.0], [1.34234, 1.34234, 0.0], \
       [1.34234, 0.0,  1.34234], [0.0, 1.34234, 1.34234]])
t = np.array([1.34234, -1.34234, -1.34234])

for i in positions:
     i += t
result2e = positions[:]

print(result2e)
