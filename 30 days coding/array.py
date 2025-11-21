# Given an array of integers, print the elements in reverse order, space-separated.
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])
