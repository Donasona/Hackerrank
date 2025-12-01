# You are given the names and grades of N students.  
# You must:

# 1. Store them in a nested list (each student as [name, grade]).
# 2. Find the second lowest grade among all students.
# 3. Print the names of all students who have the second lowest grade, in alphabetical order, each on a new line

# answer

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    # Get all unique scores and sort them
    scores = sorted(set([s for _, s in records]))
    second_lowest = scores[1]

    # Get names with the second lowest score and sort alphabetically
    names = sorted([name for name, score in records if score == second_lowest])
    
    for name in names:
        print(name)
