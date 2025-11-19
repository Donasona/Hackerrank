# Question:  
# Given a string S, print two space-separated strings: one with characters at even indices and one with characters at odd indices.

# Input:  
# - An integer T (number of test cases).  
# - T lines, each with a string S.

# answer

t = int(input())
for _ in range(t):
    s = input()
    even = s[::2]
    odd = s[1::2]
    print(f"{even} {odd}")


