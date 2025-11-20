# You are given three integers x, y, z representing the dimensions of a cuboid and an integer n.  
# Print a list of all possible coordinates (i, j, k) such that the sum i + j + k ≠ n.

# Sample Input

# 1  
# 1  
# 2  
# 3


# Sample Output

# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1]]

# answer

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i, j, k] 
         for i in range(x + 1) 
         for j in range(y + 1) 
         for k in range(z + 1) 
         if (i + j + k) != n]

    print(result)

