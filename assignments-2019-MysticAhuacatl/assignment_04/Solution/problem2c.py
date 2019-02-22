# Problem 4.2c

def double_factorial(n):
    if n in (-1, 0):
        return 1
    product = 1
    for i in range(n, 1, -2):
        product *= i
    return product

