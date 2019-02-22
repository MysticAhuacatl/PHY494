# problem 3.4c

# Write Python code to translate all particles by a vector t:
# print the translated coordinates

positions = [[0.0, 0.0, 0.0],
             [1.34234, 1.34234, 0.0],
             [1.34234, 0.0, 1.34234],
             [0.0, 1.34234, 1.34234]]

t = [1.34234, -1.34234, -1.34234]


# new_positions = []
# for x in positions:
#     x_new = [xi + ti for xi, ti in zip(x, t)]
#     new_positions.append(x_new)

# or more compact
new_positions = [[xi + ti for xi, ti in zip(x, t)] for x in positions]

print(new_positions)


