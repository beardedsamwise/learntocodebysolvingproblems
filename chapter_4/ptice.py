# https://dmoj.ca/problem/coci08c1p2

adrian_strategy = ["A","B","C","A","B","C","A","B","C","A","B","C"]
bruno_strategy = ["B","A","B","C","B","A","B","C","B","A","B","C"]
goran_strategy = ["C","C","A","A","B","B","C","C","A","A","B","B"]

adrian_score = 0
bruno_score = 0
goran_score = 0

questions = int(input())

answers = input()

for i in range(questions):
    if answers[i] == adrian_strategy[i % 12]:
        adrian_score += 1
    if answers[i] == bruno_strategy[i % 12]:
        bruno_score += 1
    if answers[i] == goran_strategy[i % 12]:
        goran_score += 1

high_score = max(adrian_score, bruno_score, goran_score)

print(high_score)

if adrian_score >= high_score:
    print("Adrian")
if bruno_score >= high_score:
    print("Bruno")
if goran_score >= high_score:
    print("Goran")