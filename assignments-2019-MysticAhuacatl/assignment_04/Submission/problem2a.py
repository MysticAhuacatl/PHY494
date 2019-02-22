# Problem 4.2a

import math

def factorial_math(n):
    if n == 0:
        print(1)
    if n > 0:
        print(math.factorial(n))

for x in range(21):
    factorial_math(x)
