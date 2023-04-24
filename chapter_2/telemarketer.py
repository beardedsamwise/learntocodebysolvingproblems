https://dmoj.ca/problem/ccc18j1

def is_telemarketer(digit_1, digit_2, digit_3, digit_4):
    digit_1 = int(digit_1)
    digit_2 = int(digit_2)
    digit_3 = int(digit_3)
    digit_4 = int(digit_4)
    if (8 <= digit_1 <= 9) and (digit_2 == digit_3) and (8 <= digit_4 <= 9):
        return "ignore"
    else:
        return "answer"

digit_1 = input()
digit_2 = input()
digit_3 = input()
digit_4 = input()

print(is_telemarketer(digit_1, digit_2, digit_3, digit_4))