# https://dmoj.ca/problem/wc16c1j1

def spooky(spookiness):
    spookiness = int(spookiness)
    if (spookiness > 1) and (spookiness < 21):
        return "sp" + (spookiness * "o") + "ky"
    else:
        raise ValueError("The integer must be between 2 and 20")

spookiness = input()

print(spooky(spookiness))