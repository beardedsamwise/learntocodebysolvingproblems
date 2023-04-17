# https://dmoj.ca/problem/wc15c2j1

def hope(hopeness):
    hopeness = int(hopeness)
    if hopeness == 1:
        return "A long time ago in a galaxy far away..."
    elif hopeness > 1 and hopeness < 6:
        return "A long time ago in a galaxy" + ((hopeness - 1) * " far,") + " far away..."
    else:
        raise ValueError("The integer must be between 1 and 5")

hopeness = input()

print(hope(hopeness))
