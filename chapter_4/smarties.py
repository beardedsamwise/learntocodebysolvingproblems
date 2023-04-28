# https://dmoj.ca/problem/ecoo15r1p1

# This problem goes against typical DMOJ convention and provides input for all test cases at once 

smarties_boxes = []

# create a list of lists where the inner list is a smarties box and it's contents
# end the loop when the end of file is reached
while True:
    try:
        temp_list = []
        while True:
            user_input = input()

            if user_input == "end of box":
                break
            else:
                temp_list.append(user_input)
        smarties_boxes.append(temp_list)
    except EOFError:
        break

# process the smarties in each box and print the time taken to eat each box at the end of each loop
for smarties_box in smarties_boxes:
    time = 0
    smartie_totals = {"orange": 0, "blue" : 0, "green" : 0, "yellow" : 0, "pink" : 0, "violet" : 0, "brown" : 0, "red" : 0}
    for smartie in smarties_box:
        smartie_totals[smartie] = smartie_totals.get(smartie) + 1

    for smartie in smartie_totals:
        while smartie_totals.get(smartie) > 0:
            if not smartie == "red":
                time = time + 13
                smartie_totals[smartie] = smartie_totals.get(smartie) - 7
            else:
                time = time + 16
                smartie_totals[smartie] = smartie_totals.get(smartie) - 1
    print(time)




