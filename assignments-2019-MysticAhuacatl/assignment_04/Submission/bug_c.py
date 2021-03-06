# Problem 4.3c
# Fix the bug(s) so that the code runs correctly and submit the file.

# The 2D sinc function is defined as
#
#    sinc(x, y) = sin(x)/x * sin(y)/y
#
# Make sure that the function below produces correct output for floating point numbers x and y
import math

def sinc(x, y):
   ""'2D sinc function'""
   value = (math.sin(x)/x * (math.sin(y)/y))
   return value
