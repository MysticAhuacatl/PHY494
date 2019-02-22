# Problem 4.2b

def factorial(n):
    if n in (-1, 0):
        return 1
    product = 1
    for i in range(1, n+1):
        product *= i
    return product


# alternative recursive solution

def factorial_recursive(n):
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n-1)
