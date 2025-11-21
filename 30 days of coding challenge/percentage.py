# You're given student names and their marks.  
# You must:

# 1. Store them in a dictionary like:  
#    {'alpha': [20, 30, 40], 'beta': [30, 50, 70]}
# 2. Take a name as input (query_name)
# 3. Print the average of that student's marks — rounded to 2 decimal places

# answer

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = sum(student_marks[query_name]) / 3
    print("{:.2f}".format(avg))                


