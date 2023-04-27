# https://dmoj.ca/problem/coci18c3p1

word = input()

H = False
O = False
N = False

HONI = 0

for i in range(len(word)):
    if word[i] == "H" and H == False:
        H = True
    if word[i] == "O" and H == True and O == False:
        O = True
    if word[i] == "N" and H == True and O == True and N == False:
        N = True
    if word[i] == "I" and H == True and O == True and N == True:
        HONI += 1
        H = False
        O = False
        N = False

print(HONI)