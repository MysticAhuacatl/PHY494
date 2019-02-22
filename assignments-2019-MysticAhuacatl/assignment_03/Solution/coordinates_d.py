# problem 3.4d

# Write a Python function translate() to translate all particles by a vector t:
# print the translated coordinates for t and t2

positions = [[0.0, 0.0, 0.0],
             [1.34234, 1.34234, 0.0],
             [1.34234, 0.0, 1.34234],
             [0.0, 1.34234, 1.34234]]

positions2 = [[1.5, -1.5, 3],
              [-1.5, -1.5, -3]]

t = [1.34234, -1.34234, -1.34234]
t2 = [-1.5, 1.5, 3]



def translate(positions, t):
    return [[xi + ti for xi, ti in zip(x, t)] for x in positions]



print(translate(positions, t))
print(translate(positions2, t2))





