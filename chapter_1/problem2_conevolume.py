# https://dmoj.ca/problem/dmopc14c5p1

import math

def conevolume(r,h):
    r = int(r)
    h = int(h)
    volume = (math.pi * (r * r) * h) / 3
    return volume

r = input()
h = input ()

print(round(conevolume(r,h),2))
