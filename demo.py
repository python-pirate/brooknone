import random

def max_min(ar):
    y = 0
    bmax = ar[0]
    while y < len(ar):
        if bmax < ar[y]:
            bmax = ar[y]
        y += 1

    return bmax
