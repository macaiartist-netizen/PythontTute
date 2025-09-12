# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
#         Square root of the number
#         Natural logarithm (log base e) of the number
#         Sine of the number (in radians)
# 3.   Displays the calculated results.

a = int(input("Enter a number: "))
import math
print(math.sqrt(a))
print(math.log(a))
print(math.sin(a))

