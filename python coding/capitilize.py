# You're given a full name as a string. Your task is to capitalize the first letter of each word (first name, last name, etc.).

# ---

# 🧠 What does “capitalize” mean here?

# If the input is:

# chris alan


# The output should be:

# Chris Alan

# answer

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
     return ' '.join(word.capitalize() for word in s.split(' '))
     
if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
