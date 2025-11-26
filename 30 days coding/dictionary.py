# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of queries — each containing a name — and must print the associated phone number or Not found if the name isn't in the phone book.

# answer

n = int(input())
phonebook = {}

for _ in range(n):
    name, number = input().split()
    phonebook[name] = number

while True:
    try:
        query = input()
        if query in phonebook:
            print(f"{query}={phonebook[query]}")
        else:
            print("Not found")
    except EOFError:
        break
