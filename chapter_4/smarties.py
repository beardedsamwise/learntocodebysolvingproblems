# https://dmoj.ca/problem/ecoo15r1p1

# This problem goes against typical DMOJ convention and provides input for all test cases at once and I can't be bothered refactoring my code to handle this 😅

smarties = []

smartie_totals = {"orange": 0, "blue" : 0, "green" : 0, "yellow" : 0, "pink" : 0, "violet" : 0, "brown" : 0, "red" : 0}

time = 0

while True:
    user_input = input()

    if user_input == "end of box":
        break
    else:
        smarties.append(user_input)

for smartie in smarties:
    smartie_totals[smartie] = smartie_totals.get(smartie) + 1

for smartie in smartie_totals:
    while smartie_totals.get(smartie) > 0:
        if not smartie == "red":
            time = time + 13
            smartie_totals[smartie] = smartie_totals.get(smartie) - 7
            # print("Ate smarties of colour ", smartie, " with total now left ", smartie_totals[smartie])
        else:
            time = time + 16
            smartie_totals[smartie] = smartie_totals.get(smartie) - 1

print(time)


