# https://dmoj.ca/problem/wc18c3j1

def pokedollars(P, B, D):
    P = int(P)
    B = int(B)
    D = int(D)
    if (1 <= P <= 100) and (1 <= B <= 100) and (1 <= D <= 100):
        painted_badges = P // B
        leftover_paint = P % B
        dollars_earnt = (painted_badges * D) + leftover_paint
        return dollars_earnt
    else:
        raise ValueError("All values must be within the range of 1-100 inclusive")

paint = input()
bottlecap_paint = input()
dollar_rate = input()

print(pokedollars(paint, bottlecap_paint, dollar_rate))