# Problem 3.5b
# Fix the bug(s) so that the code runs correctly and submit the file.

# a and b are two vectors. Calculate c = 5*a - 3*b

a = (12.3, 3.90, 4.5)
b = (1.3, 0.91, -3.3)

c = []
for i in range(len(a)):
    c.append(5*a[i] - 3*b[i])

print(c)

