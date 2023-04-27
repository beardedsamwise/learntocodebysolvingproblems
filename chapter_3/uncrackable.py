# https://dmoj.ca/problem/wc17c3j3

password = input()

lower = 0
upper = 0
digit = 0

for char in password:
    if char.isnumeric():
        digit += 1
    elif char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

if lower >= 3 and upper >= 2 and digit >= 1 and 8 <= len(password) <= 12:
    print("Valid")
else:
    print("Invalid")
