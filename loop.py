# Write a Python program that takes an integer n as input and prints its multiplication table up to 10 in the format:  
# n x i = result  
# where i ranges from 1 to 10.

# answer

#!/bin/python3



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

