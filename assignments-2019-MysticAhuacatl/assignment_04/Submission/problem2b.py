# Problem 4.2b

def factorial(n):
    result = 1
    if n == 0:
        print(result)
    if n > 0:
        for i in range(1, n + 1):
            result = result * i
        print(result)

for x in range(21):
    factorial(x)
