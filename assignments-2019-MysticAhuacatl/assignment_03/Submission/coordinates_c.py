# problem 3.4c

# Write Python code to translate all particles by a vector t:
# print the translated coordinates
from operator import add

positions = [[0.0, 0.0, 0.0],
             [1.34234, 1.34234, 0.0],
             [1.34234, 0.0, 1.34234],
             [0.0, 1.34234, 1.34234]]

t = [1.34234, -1.34234, -1.34234]


new_positions = list(map(add, positions[0], t))
new_positions += list(map(add, positions[1], t))
new_positions += list(map(add, positions[2], t))
new_positions += list(map(add, positions[3], t))

print(new_positions)
