
# Task:
# Complete the recursive function to compute the factorial of a given integer n.

# ---

# Recursive Formula:

# factorial(N) = 
#     1                       if N <= 1
#     N * factorial(N - 1)    otherwise

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# def factorial(n):
#     # Write your code here
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     result = factorial(n)

#     fptr.write(str(result) + '\n')

#     fptr.close()

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# For local testing
n = int(input().strip())
print(factorial(n))
