# https://dmoj.ca/problem/ccc13j1

def age_gap(youngest, middle):
    youngest = int(youngest)
    middle = int(middle)
    if (0 <= youngest <= 50) and  (0 <= middle <= 50):
        difference = middle - youngest
        return middle + difference
    else:
        raise ValueError("The integer must be between 0 and 50")

youngest = input()
middle = input()

print(age_gap(youngest, middle))