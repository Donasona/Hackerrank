# Question:  
# Write a function to determine whether a given year is a leap year in the Gregorian calendar.  
# A leap year occurs:  
# - On every year that is evenly divisible by 4  
# - Except every year that is evenly divisible by 100  
# - Unless the year is also evenly divisible by 400  

# Input:  
# A single integer, year (1900 ≤ year ≤ 10⁵) 

# answer

def is_leap(year):
    leap = False
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True

    # Write your logic here
    
    return leap

year = int(input("enter the number:"))
print(is_leap(year))