# Problem 4.2c

def double_factorial(n):
    result = 1
    if n == 0:
            print(result)
    if n > 0:
        if (n % 2) == 0:
            for i in range(2, n + 1, 2):
                result = result * i
            print(result)
        else:
            for i in range(1, n + 1, 2):
                result = result * i
            print(result)

for x in range(21):
    double_factorial(x)
