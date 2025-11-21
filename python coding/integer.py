# You are given an integer n.  
# Without using any string methods, print the numbers from 1 to n without spaces, on the same line.

# Sample Input  
# 3

# Sample Output  
# 123

# answer

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
    
        