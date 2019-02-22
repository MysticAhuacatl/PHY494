# Problem 3.5c
# Fix the bug(s) so that the code runs correctly and submit the file.

# The 2D sinc function is defined as
#
#    sinc(x, y) = sin(x)/x * sin(y)/y
#
# Make sure that the function below produces correct output for floating point numbers x and y

import math

def sinc1d(x):
    if x == 0:
        return 1
    return math.sin(x)/x

def sinc(x, y):
   """2D sinc function"""
   return sinc1d(x) * sinc1d(y)

